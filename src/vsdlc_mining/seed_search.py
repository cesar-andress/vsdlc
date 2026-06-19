"""Phase 1: discover repositories via GitHub code search."""

from __future__ import annotations

import json
import logging
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from vsdlc_mining.config import (
    MAX_SEARCH_RESULTS,
    SEARCH_QUERY_DELAY_SECONDS,
    SEED_SEARCH_QUERIES,
)
from vsdlc_mining.github_client import GitHubClient, GitHubClientError, GitHubRateLimitExceeded
from vsdlc_mining.metadata import extract_github_metadata
from vsdlc_mining.models import RepoCandidate
from vsdlc_mining.utils import append_jsonl, read_json, read_jsonl, salvage_json, write_json, write_jsonl

logger = logging.getLogger(__name__)


def _reraise_if_rate_limited(exc: Exception) -> None:
    if isinstance(exc, GitHubRateLimitExceeded):
        raise exc
    if isinstance(exc, GitHubClientError) and "quota exhausted" in str(exc).casefold():
        raise exc


def _parse_datetime(value: str | None) -> datetime:
    if not value:
        return datetime.min
    return datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)


def _license_spdx(repo_payload: dict[str, Any]) -> str | None:
    license_info = repo_payload.get("license")
    if isinstance(license_info, dict):
        return license_info.get("spdx_id")
    return None


def _merge_candidate(
    store: dict[str, dict[str, Any]],
    *,
    full_name: str,
    query_label: str,
    matched_path: str,
    repository_url: str,
) -> None:
    entry = store.setdefault(
        full_name,
        {
            "full_name": full_name,
            "repository_url": repository_url,
            "queries": set(),
            "matched_paths": set(),
        },
    )
    entry["queries"].add(query_label)
    entry["matched_paths"].add(matched_path)


def _serialize_aggregate(aggregate: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        full_name: {
            "full_name": entry["full_name"],
            "repository_url": entry["repository_url"],
            "queries": sorted(entry["queries"]),
            "matched_paths": sorted(entry["matched_paths"]),
        }
        for full_name, entry in aggregate.items()
    }


def _deserialize_aggregate(payload: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    aggregate: dict[str, dict[str, Any]] = {}
    for full_name, entry in payload.items():
        aggregate[full_name] = {
            "full_name": entry["full_name"],
            "repository_url": entry["repository_url"],
            "queries": set(entry.get("queries", [])),
            "matched_paths": set(entry.get("matched_paths", [])),
        }
    return aggregate


def save_checkpoint(
    path: Path,
    *,
    completed_queries: list[str],
    aggregate: dict[str, dict[str, Any]],
    search_completed: bool,
    enriched_full_names: list[str],
) -> None:
    write_json(
        path,
        {
            "completed_queries": completed_queries,
            "search_completed": search_completed,
            "enriched_full_names": enriched_full_names,
            "aggregate": _serialize_aggregate(aggregate),
        },
    )


def load_checkpoint(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return read_json(path)
    except json.JSONDecodeError:
        payload, trimmed = salvage_json(path)
        logger.warning(
            "Salvaged truncated checkpoint at %s (trimmed %d trailing bytes).",
            path,
            trimmed,
        )
        return payload


def repair_checkpoint(
    checkpoint_path: Path,
    *,
    output_path: Path,
) -> dict[str, Any]:
    """Rewrite a checkpoint from salvage + JSONL, syncing enriched repo names."""
    payload = load_checkpoint(checkpoint_path)
    if payload is None:
        raise FileNotFoundError(f"No checkpoint at {checkpoint_path}")

    enriched_from_jsonl: list[str] = []
    if output_path.exists():
        enriched_from_jsonl = sorted(
            {candidate.full_name for candidate in read_jsonl(output_path, RepoCandidate)}
        )

    checkpoint_enriched = sorted(payload.get("enriched_full_names", []))
    if enriched_from_jsonl:
        payload["enriched_full_names"] = enriched_from_jsonl
    else:
        payload["enriched_full_names"] = checkpoint_enriched

    save_checkpoint(
        checkpoint_path,
        completed_queries=list(payload.get("completed_queries", [])),
        aggregate=_deserialize_aggregate(payload.get("aggregate", {})),
        search_completed=bool(payload.get("search_completed", False)),
        enriched_full_names=list(payload["enriched_full_names"]),
    )
    logger.info(
        "Repaired checkpoint: %d aggregate repos, %d enriched (JSONL had %d).",
        len(payload.get("aggregate", {})),
        len(payload["enriched_full_names"]),
        len(enriched_from_jsonl),
    )
    if checkpoint_enriched and enriched_from_jsonl:
        only_checkpoint = set(checkpoint_enriched) - set(enriched_from_jsonl)
        if only_checkpoint:
            logger.warning(
                "Dropped %d enriched names present only in checkpoint; "
                "they will be re-fetched on resume.",
                len(only_checkpoint),
            )
    return payload


def _enrich_candidates(
    client: GitHubClient,
    aggregate: dict[str, dict[str, Any]],
    *,
    enriched_full_names: set[str],
    output_path: Path,
    checkpoint_path: Path,
    completed_queries: list[str],
    search_completed: bool,
) -> list[RepoCandidate]:
    candidates: list[RepoCandidate] = []
    for full_name in sorted(aggregate):
        if full_name in enriched_full_names:
            continue
        entry = aggregate[full_name]
        try:
            repo_payload = client.get_repository(full_name)
        except GitHubRateLimitExceeded:
            raise
        except Exception as exc:  # noqa: BLE001
            _reraise_if_rate_limited(exc)
            logger.warning("Skipping %s — metadata fetch failed: %s", full_name, exc)
            enriched_full_names.add(full_name)
            save_checkpoint(
                checkpoint_path,
                completed_queries=completed_queries,
                aggregate=aggregate,
                search_completed=search_completed,
                enriched_full_names=sorted(enriched_full_names),
            )
            continue

        queries = sorted(entry["queries"])
        matched_paths = sorted(entry["matched_paths"])
        metadata = extract_github_metadata(repo_payload)
        candidate = RepoCandidate(
            query=queries[0],
            full_name=full_name,
            repository_url=entry["repository_url"],
            stars=int(repo_payload.get("stargazers_count") or 0),
            pushed_at=_parse_datetime(repo_payload.get("pushed_at")),
            default_branch=repo_payload.get("default_branch") or "main",
            matched_path=matched_paths[0],
            license=_license_spdx(repo_payload),
            queries=queries,
            matched_paths=matched_paths,
            github_description=metadata["github_description"],
            github_topics=metadata["github_topics"],
            primary_language=metadata["primary_language"],
        )
        candidates.append(candidate)
        append_jsonl(output_path, [candidate])
        enriched_full_names.add(full_name)
        save_checkpoint(
            checkpoint_path,
            completed_queries=completed_queries,
            aggregate=aggregate,
            search_completed=search_completed,
            enriched_full_names=sorted(enriched_full_names),
        )

    return candidates


def select_seed_queries(query_text: str | None) -> list[tuple[str, str]]:
    """Return configured seed queries, optionally filtered by label or API query text."""
    if not query_text:
        return list(SEED_SEARCH_QUERIES)
    needle = query_text.casefold()
    matched = [
        (api_query, label)
        for api_query, label in SEED_SEARCH_QUERIES
        if needle in label.casefold() or needle in api_query.casefold()
    ]
    if not matched:
        raise ValueError(f"No seed query matches {query_text!r}")
    return matched


def run_seed_search(
    client: GitHubClient,
    *,
    resume: bool = False,
    fresh_start: bool = False,
    checkpoint_path: Path,
    output_path: Path,
    query_filter: str | None = None,
    max_pages: int | None = None,
) -> list[RepoCandidate]:
    """Execute seed queries with checkpointing and incremental JSONL output."""
    aggregate: dict[str, dict[str, Any]] = {}
    completed_queries: list[str] = []
    enriched_full_names: set[str] = set()
    search_completed = False
    query_hit_counts: dict[str, int] = defaultdict(int)
    seed_queries = select_seed_queries(query_filter)
    max_results = MAX_SEARCH_RESULTS
    if max_pages is not None:
        max_results = min(max_results, max_pages * client.per_page)

    if fresh_start and checkpoint_path.exists():
        checkpoint_path.unlink()
        logger.info("Fresh start: removed checkpoint at %s", checkpoint_path)

    if resume and not fresh_start:
        checkpoint = load_checkpoint(checkpoint_path)
        if checkpoint:
            aggregate = _deserialize_aggregate(checkpoint.get("aggregate", {}))
            completed_queries = list(checkpoint.get("completed_queries", []))
            enriched_full_names = set(checkpoint.get("enriched_full_names", []))
            search_completed = bool(checkpoint.get("search_completed", False))
            logger.info(
                "Resuming from checkpoint: %d queries done, %d repos, %d enriched.",
                len(completed_queries),
                len(aggregate),
                len(enriched_full_names),
            )
        else:
            logger.warning("No checkpoint found at %s; starting fresh.", checkpoint_path)

    if not search_completed:
        pending = [
            (api_query, label)
            for api_query, label in seed_queries
            if label not in completed_queries
        ]
        if query_filter:
            logger.info(
                "Query filter %r selected %d seed queries.",
                query_filter,
                len(seed_queries),
            )
        if max_pages is not None:
            logger.info(
                "Max pages per query set to %d (up to %d results each).",
                max_pages,
                max_results,
            )
        for index, (api_query, label) in enumerate(pending):
            if index > 0:
                logger.debug(
                    "Sleeping %.1fs between seed queries to respect search rate limits.",
                    SEARCH_QUERY_DELAY_SECONDS,
                )
                time.sleep(SEARCH_QUERY_DELAY_SECONDS)

            logger.info("Searching code: %s (%s)", label, api_query)
            try:
                items = client.search_code(
                    api_query,
                    max_results=max_results,
                    max_pages=max_pages,
                )
            except GitHubRateLimitExceeded:
                raise
            except Exception as exc:  # noqa: BLE001 — continue other queries
                logger.error("Query failed for %s: %s", label, exc)
                continue

            query_hit_counts[label] = len(items)
            logger.info("Query %s returned %d hits", label, len(items))

            for item in items:
                repo = item.get("repository") or {}
                full_name = repo.get("full_name")
                if not full_name:
                    continue
                matched_path = item.get("path") or label
                repository_url = repo.get("html_url") or f"https://github.com/{full_name}"
                _merge_candidate(
                    aggregate,
                    full_name=full_name,
                    query_label=label,
                    matched_path=matched_path,
                    repository_url=repository_url,
                )

            completed_queries.append(label)
            save_checkpoint(
                checkpoint_path,
                completed_queries=completed_queries,
                aggregate=aggregate,
                search_completed=False,
                enriched_full_names=sorted(enriched_full_names),
            )

        search_completed = True
        save_checkpoint(
            checkpoint_path,
            completed_queries=completed_queries,
            aggregate=aggregate,
            search_completed=True,
            enriched_full_names=sorted(enriched_full_names),
        )

    logger.info("Unique repositories after deduplication: %d", len(aggregate))

    if fresh_start or not resume or not output_path.exists():
        write_jsonl(output_path, [])

    new_candidates = _enrich_candidates(
        client,
        aggregate,
        enriched_full_names=enriched_full_names,
        output_path=output_path,
        checkpoint_path=checkpoint_path,
        completed_queries=completed_queries,
        search_completed=search_completed,
    )

    if enriched_full_names:
        all_candidates = read_jsonl(output_path, RepoCandidate) if output_path.exists() else []
    else:
        all_candidates = new_candidates

    logger.info("Enriched candidates: %d", len(all_candidates))
    for label, count in sorted(query_hit_counts.items()):
        logger.debug("Raw hits for %s: %d", label, count)
    return all_candidates
