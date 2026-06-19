"""Phase 2: filter repository candidates for mining eligibility."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

from vsdlc_mining.config import (
    AGENT_PRODUCT_KEYWORDS,
    CI_PATH_HINTS,
    EXCLUSION_KEYWORDS,
    MIN_PUSHED_AT,
    MIN_STARS,
    TEST_DIR_HINTS,
    TEST_PATH_HINTS,
)
from vsdlc_mining.github_client import GitHubClient, GitHubClientError, GitHubRateLimitExceeded
from vsdlc_mining.metadata import extract_github_metadata
from vsdlc_mining.models import (
    EligibleRepo,
    EvidenceFlags,
    ExcludedRepo,
    FilterSummary,
    RepoCandidate,
)
from vsdlc_mining.utils import append_jsonl, contains_keyword, normalize_text, read_jsonl, write_json, write_jsonl

logger = logging.getLogger(__name__)

METADATA_FETCH_FAILED_REASON = "metadata_fetch_failed"


def _reraise_if_rate_limited(exc: Exception) -> None:
    if isinstance(exc, GitHubRateLimitExceeded):
        raise exc
    if isinstance(exc, GitHubClientError) and "quota exhausted" in str(exc).casefold():
        raise exc


def _parse_topics(repo_payload: dict) -> list[str]:
    topics = repo_payload.get("topics") or []
    return [normalize_text(topic) for topic in topics]


def detect_agent_product_flag(
    *,
    full_name: str,
    description: str | None,
    topics: list[str],
    matched_paths: list[str],
) -> bool:
    """Mark repos that likely document AI tooling products (never auto-exclude)."""
    corpus = " ".join(
        [
            full_name,
            description or "",
            " ".join(topics),
            " ".join(matched_paths),
        ]
    )
    return contains_keyword(corpus, AGENT_PRODUCT_KEYWORDS) is not None


def _structural_exclusion_reasons(repo_payload: dict) -> list[str]:
    reasons: list[str] = []
    if repo_payload.get("fork"):
        reasons.append("fork")
    if repo_payload.get("archived"):
        reasons.append("archived")
    if repo_payload.get("mirror_url"):
        reasons.append("mirror")
    if repo_payload.get("is_template"):
        reasons.append("template")
    return reasons


def _keyword_exclusion_reasons(
    *,
    full_name: str,
    description: str | None,
    topics: list[str],
    agent_product_flag: bool,
) -> list[str]:
    if agent_product_flag:
        return []

    corpus = " ".join([full_name, description or "", " ".join(topics)])
    matched = contains_keyword(corpus, EXCLUSION_KEYWORDS)
    if matched:
        return [f"keyword:{matched}"]
    return []


def _meets_activity_thresholds(
    *,
    stars: int,
    pushed_at: datetime,
) -> list[str]:
    failures: list[str] = []
    if stars < MIN_STARS:
        failures.append(f"stars_below_{MIN_STARS}")
    if pushed_at < MIN_PUSHED_AT:
        failures.append(f"pushed_before_{MIN_PUSHED_AT.date().isoformat()}")
    return failures


def detect_evidence(
    client: GitHubClient,
    full_name: str,
    *,
    probe_releases: bool = True,
) -> EvidenceFlags:
    """Detect CI, test, and release evidence via lightweight API probes."""
    flags = EvidenceFlags()
    root_entries = client.list_repo_root_entries(full_name)
    root_names = {entry.get("name", "") for entry in root_entries}
    root_paths = {entry.get("path", "") for entry in root_entries}

    for hint in CI_PATH_HINTS:
        if hint.endswith("/"):
            prefix = hint.rstrip("/")
            if any(path == prefix or path.startswith(prefix + "/") for path in root_paths):
                flags.has_ci_evidence = True
                flags.ci_paths.append(hint)
        elif hint in root_names:
            flags.has_ci_evidence = True
            flags.ci_paths.append(hint)

    if ".github" in root_names and not flags.has_ci_evidence:
        if client.path_exists(full_name, ".github/workflows"):
            flags.has_ci_evidence = True
            flags.ci_paths.append(".github/workflows")

    for hint in TEST_PATH_HINTS:
        if hint in root_names:
            flags.has_test_evidence = True
            flags.test_paths.append(hint)

    for hint in TEST_DIR_HINTS:
        dir_name = hint.rstrip("/")
        if dir_name in root_names:
            flags.has_test_evidence = True
            flags.test_paths.append(hint)

    if not probe_releases:
        return flags

    tags = client.list_tags(full_name, limit=1)
    releases = client.list_releases(full_name, limit=1)
    flags.release_tag_count = len(tags)
    flags.release_count = len(releases)
    flags.has_release_tag_evidence = bool(tags or releases)
    return flags


def enrich_release_evidence(
    client: GitHubClient,
    full_name: str,
    flags: EvidenceFlags,
) -> EvidenceFlags:
    """Attach release/tag counts after a repo passes CI/test checks."""
    tags = client.list_tags(full_name, limit=1)
    releases = client.list_releases(full_name, limit=1)
    flags.release_tag_count = len(tags)
    flags.release_count = len(releases)
    flags.has_release_tag_evidence = bool(tags or releases)
    return flags


def _count_exclusion_reasons(excluded: list[ExcludedRepo]) -> dict[str, int]:
    reason_counts: dict[str, int] = {}
    for record in excluded:
        for reason in record.exclusion_reasons:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
    return reason_counts


def _count_agent_flagged(
    eligible: list[EligibleRepo],
    excluded: list[ExcludedRepo],
) -> int:
    return sum(1 for record in eligible if record.agent_product_flag) + sum(
        1 for record in excluded if record.agent_product_flag
    )


def load_filter_progress(
    *,
    eligible_output_path: Path | None,
    excluded_output_path: Path | None,
    retry_metadata_failures: bool = False,
) -> tuple[set[str], list[EligibleRepo], list[ExcludedRepo]]:
    """Load repositories already written to Phase 2 JSONL outputs."""
    processed_names: set[str] = set()
    eligible: list[EligibleRepo] = []
    excluded: list[ExcludedRepo] = []

    if eligible_output_path is not None and eligible_output_path.exists():
        eligible = read_jsonl(eligible_output_path, EligibleRepo)
        processed_names.update(record.full_name for record in eligible)

    if excluded_output_path is not None and excluded_output_path.exists():
        excluded = read_jsonl(excluded_output_path, ExcludedRepo)
        if retry_metadata_failures:
            kept: list[ExcludedRepo] = []
            dropped = 0
            for record in excluded:
                if record.exclusion_reasons == [METADATA_FETCH_FAILED_REASON]:
                    dropped += 1
                    continue
                kept.append(record)
            if dropped:
                logger.warning(
                    "Dropping %d excluded repos with %s so they can be retried after "
                    "rate-limit interruption.",
                    dropped,
                    METADATA_FETCH_FAILED_REASON,
                )
                excluded = kept
                write_jsonl(excluded_output_path, excluded)
        processed_names.update(record.full_name for record in excluded)

    return processed_names, eligible, excluded


def _build_summary(
    *,
    input_candidates: int,
    eligible_count: int,
    excluded_count: int,
    agent_flagged: int,
    reason_counts: dict[str, int],
) -> FilterSummary:
    return FilterSummary(
        input_candidates=input_candidates,
        eligible_count=eligible_count,
        excluded_count=excluded_count,
        agent_product_flagged=agent_flagged,
        exclusion_reason_counts=dict(sorted(reason_counts.items())),
    )


def _persist_filter_progress(
    *,
    summary_output_path: Path | None,
    input_candidates: int,
    eligible_count: int,
    excluded_count: int,
    agent_flagged: int,
    reason_counts: dict[str, int],
) -> None:
    if summary_output_path is None:
        return
    write_json(
        summary_output_path,
        _build_summary(
            input_candidates=input_candidates,
            eligible_count=eligible_count,
            excluded_count=excluded_count,
            agent_flagged=agent_flagged,
            reason_counts=reason_counts,
        ).model_dump(),
    )


def _log_filter_progress(
    *,
    status: str,
    full_name: str,
    processed: int,
    total: int,
    eligible_count: int,
    excluded_count: int,
) -> None:
    logger.info(
        "%s %s — %d/%d processed, %d eligible, %d excluded",
        status,
        full_name,
        processed,
        total,
        eligible_count,
        excluded_count,
    )


def filter_repositories(
    client: GitHubClient,
    candidates: list[RepoCandidate],
    *,
    limit_repos: int | None = None,
    eligible_output_path: Path | None = None,
    excluded_output_path: Path | None = None,
    summary_output_path: Path | None = None,
    resume: bool = False,
) -> tuple[list[EligibleRepo], list[ExcludedRepo], FilterSummary]:
    """Apply inclusion and exclusion rules to seed-search candidates."""
    worklist = candidates[:limit_repos] if limit_repos is not None else candidates
    if limit_repos is not None:
        logger.info(
            "Processing first %d of %d candidates (limit_repos).",
            len(worklist),
            len(candidates),
        )

    processed_names: set[str] = set()
    eligible: list[EligibleRepo] = []
    excluded: list[ExcludedRepo] = []
    reason_counts: dict[str, int] = {}
    agent_flagged = 0

    if resume:
        processed_names, eligible, excluded = load_filter_progress(
            eligible_output_path=eligible_output_path,
            excluded_output_path=excluded_output_path,
            retry_metadata_failures=True,
        )
        reason_counts = _count_exclusion_reasons(excluded)
        agent_flagged = _count_agent_flagged(eligible, excluded)
        if processed_names:
            logger.info(
                "Resuming filter progress: %d repos already processed "
                "(%d eligible, %d excluded), %d pending.",
                len(processed_names),
                len(eligible),
                len(excluded),
                len(worklist) - len(processed_names),
            )
        _persist_filter_progress(
            summary_output_path=summary_output_path,
            input_candidates=len(worklist),
            eligible_count=len(eligible),
            excluded_count=len(excluded),
            agent_flagged=agent_flagged,
            reason_counts=reason_counts,
        )
    else:
        if eligible_output_path is not None:
            write_jsonl(eligible_output_path, [])
        if excluded_output_path is not None:
            write_jsonl(excluded_output_path, [])
        if summary_output_path is not None:
            write_json(
                summary_output_path,
                FilterSummary(input_candidates=len(worklist)).model_dump(),
            )

    processed_count = len(processed_names)

    for candidate in worklist:
        if candidate.full_name in processed_names:
            logger.debug("Skipping %s (already processed)", candidate.full_name)
            continue

        logger.info("Filtering %s", candidate.full_name)
        try:
            repo_payload = client.get_repository(candidate.full_name)

            metadata = extract_github_metadata(repo_payload)
            topics = metadata["github_topics"]
            description = metadata["github_description"]
            agent_product_flag = detect_agent_product_flag(
                full_name=candidate.full_name,
                description=description,
                topics=topics,
                matched_paths=candidate.matched_paths,
            )
            if agent_product_flag:
                agent_flagged += 1

            exclusion_reasons: list[str] = []
            exclusion_reasons.extend(_structural_exclusion_reasons(repo_payload))
            exclusion_reasons.extend(
                _keyword_exclusion_reasons(
                    full_name=candidate.full_name,
                    description=description,
                    topics=topics,
                    agent_product_flag=agent_product_flag,
                )
            )
            exclusion_reasons.extend(
                _meets_activity_thresholds(
                    stars=int(repo_payload.get("stargazers_count") or candidate.stars),
                    pushed_at=candidate.pushed_at,
                )
            )

            if not candidate.matched_paths:
                exclusion_reasons.append("missing_instruction_artifact")

            if exclusion_reasons:
                evidence = EvidenceFlags()
            else:
                evidence = detect_evidence(client, candidate.full_name, probe_releases=False)
                if not (evidence.has_ci_evidence or evidence.has_test_evidence):
                    exclusion_reasons.append("missing_ci_or_test_evidence")

            if exclusion_reasons:
                for reason in exclusion_reasons:
                    reason_counts[reason] = reason_counts.get(reason, 0) + 1
                excluded_record = ExcludedRepo(
                    full_name=candidate.full_name,
                    repository_url=candidate.repository_url,
                    stars=int(repo_payload.get("stargazers_count") or candidate.stars),
                    pushed_at=candidate.pushed_at,
                    exclusion_reasons=sorted(set(exclusion_reasons)),
                    agent_product_flag=agent_product_flag,
                    queries=candidate.queries,
                    matched_paths=candidate.matched_paths,
                )
                excluded.append(excluded_record)
                if excluded_output_path is not None:
                    append_jsonl(excluded_output_path, [excluded_record])
                _persist_filter_progress(
                    summary_output_path=summary_output_path,
                    input_candidates=len(worklist),
                    eligible_count=len(eligible),
                    excluded_count=len(excluded),
                    agent_flagged=agent_flagged,
                    reason_counts=reason_counts,
                )
                processed_count += 1
                _log_filter_progress(
                    status="Excluded",
                    full_name=candidate.full_name,
                    processed=processed_count,
                    total=len(worklist),
                    eligible_count=len(eligible),
                    excluded_count=len(excluded),
                )
                continue

            evidence = enrich_release_evidence(client, candidate.full_name, evidence)
            eligible_record = EligibleRepo(
                full_name=candidate.full_name,
                repository_url=candidate.repository_url,
                stars=int(repo_payload.get("stargazers_count") or candidate.stars),
                pushed_at=candidate.pushed_at,
                default_branch=repo_payload.get("default_branch") or candidate.default_branch,
                license=candidate.license,
                queries=candidate.queries,
                matched_paths=candidate.matched_paths,
                agent_product_flag=agent_product_flag,
                evidence=evidence,
                github_description=metadata["github_description"],
                github_topics=metadata["github_topics"],
                primary_language=metadata["primary_language"],
            )
            eligible.append(eligible_record)
            if eligible_output_path is not None:
                append_jsonl(eligible_output_path, [eligible_record])
            _persist_filter_progress(
                summary_output_path=summary_output_path,
                input_candidates=len(worklist),
                eligible_count=len(eligible),
                excluded_count=len(excluded),
                agent_flagged=agent_flagged,
                reason_counts=reason_counts,
            )
            processed_count += 1
            _log_filter_progress(
                status="Eligible",
                full_name=candidate.full_name,
                processed=processed_count,
                total=len(worklist),
                eligible_count=len(eligible),
                excluded_count=len(excluded),
            )
        except GitHubRateLimitExceeded:
            raise
        except Exception as exc:  # noqa: BLE001
            _reraise_if_rate_limited(exc)
            reason = METADATA_FETCH_FAILED_REASON
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
            excluded_record = ExcludedRepo(
                full_name=candidate.full_name,
                repository_url=candidate.repository_url,
                stars=candidate.stars,
                pushed_at=candidate.pushed_at,
                exclusion_reasons=[reason],
                queries=candidate.queries,
                matched_paths=candidate.matched_paths,
            )
            excluded.append(excluded_record)
            if excluded_output_path is not None:
                append_jsonl(excluded_output_path, [excluded_record])
            _persist_filter_progress(
                summary_output_path=summary_output_path,
                input_candidates=len(worklist),
                eligible_count=len(eligible),
                excluded_count=len(excluded),
                agent_flagged=agent_flagged,
                reason_counts=reason_counts,
            )
            processed_count += 1
            _log_filter_progress(
                status="Excluded",
                full_name=candidate.full_name,
                processed=processed_count,
                total=len(worklist),
                eligible_count=len(eligible),
                excluded_count=len(excluded),
            )
            logger.warning("Excluded %s: %s", candidate.full_name, exc)
            continue

    summary = _build_summary(
        input_candidates=len(worklist),
        eligible_count=len(eligible),
        excluded_count=len(excluded),
        agent_flagged=agent_flagged,
        reason_counts=reason_counts,
    )
    return eligible, excluded, summary
