"""Lightweight GitHub metadata backfill for eligible repositories and gold samples."""

from __future__ import annotations

import csv
import logging
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

from vsdlc_mining.github_client import GitHubClientError, GitHubRateLimitExceeded
from vsdlc_mining.gold_sample import GOLD_SAMPLE_FIELDS
from vsdlc_mining.metadata import extract_github_metadata
from vsdlc_mining.models import EligibleRepo
from vsdlc_mining.utils import ensure_parent, write_jsonl

logger = logging.getLogger(__name__)

METADATA_FIELDS = ("github_description", "github_topics", "primary_language")
ANNOTATION_FIELDS = (
    "primary_label",
    "secondary_tags",
    "confidence",
    "evidence_notes",
    "annotator_id",
    "annotation_round",
    "adjudication_status",
    "adjudicated_label",
    "adjudication_notes",
    # Legacy v0.1 column; preserved if present but not written by backfill.
    "label",
)


class RepositoryClient(Protocol):
    def get_repository(self, full_name: str) -> dict[str, Any]:
        """Return GitHub repository metadata payload."""


@dataclass
class BackfillStats:
    total_repos: int = 0
    api_fetches: int = 0
    skipped_complete: int = 0
    successfully_enriched: int = 0
    failed_fetches: list[str] = field(default_factory=list)

    @property
    def enriched_count(self) -> int:
        return self.successfully_enriched


def is_missing_description(value: str | None) -> bool:
    return value is None or not str(value).strip()


def is_missing_topics(value: list[str] | None) -> bool:
    return not value


def is_missing_language(value: str | None) -> bool:
    return value is None or not str(value).strip()


def needs_metadata_backfill(repo: EligibleRepo) -> bool:
    return (
        is_missing_description(repo.github_description)
        or is_missing_topics(repo.github_topics)
        or is_missing_language(repo.primary_language)
    )


def merge_metadata(repo: EligibleRepo, fetched: dict[str, Any]) -> EligibleRepo:
    """Fill only missing metadata fields; preserve all other values."""
    updates: dict[str, Any] = {}
    if is_missing_description(repo.github_description):
        updates["github_description"] = fetched.get("github_description")
    if is_missing_topics(repo.github_topics):
        updates["github_topics"] = list(fetched.get("github_topics") or [])
    if is_missing_language(repo.primary_language):
        updates["primary_language"] = fetched.get("primary_language")
    if not updates:
        return repo
    return repo.model_copy(update=updates)


def _metadata_was_filled(before: EligibleRepo, after: EligibleRepo) -> bool:
    return (
        (is_missing_description(before.github_description) and not is_missing_description(after.github_description))
        or (is_missing_topics(before.github_topics) and not is_missing_topics(after.github_topics))
        or (is_missing_language(before.primary_language) and not is_missing_language(after.primary_language))
    )


def backfill_eligible_repos(
    client: RepositoryClient,
    repos: list[EligibleRepo],
) -> tuple[list[EligibleRepo], BackfillStats]:
    """Fetch GitHub metadata for repos with missing description/topics/language."""
    stats = BackfillStats(total_repos=len(repos))
    enriched: list[EligibleRepo] = []

    for repo in repos:
        if not needs_metadata_backfill(repo):
            enriched.append(repo)
            stats.skipped_complete += 1
            continue

        try:
            payload = client.get_repository(repo.full_name)
            metadata = extract_github_metadata(payload)
            updated = merge_metadata(repo, metadata)
            enriched.append(updated)
            stats.api_fetches += 1
            if _metadata_was_filled(repo, updated):
                stats.successfully_enriched += 1
        except GitHubRateLimitExceeded:
            raise
        except (GitHubClientError, ValueError, KeyError) as exc:
            logger.warning("Metadata fetch failed for %s: %s", repo.full_name, exc)
            enriched.append(repo)
            stats.api_fetches += 1
            stats.failed_fetches.append(repo.full_name)

    return enriched, stats


def metadata_lookup(repos: list[EligibleRepo]) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    for repo in repos:
        lookup[repo.full_name] = {
            "github_description": repo.github_description or "",
            "github_topics": "|".join(repo.github_topics or []),
            "primary_language": repo.primary_language or "",
        }
    return lookup


def _csv_fieldnames(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return list(GOLD_SAMPLE_FIELDS)
    return list(rows[0].keys())


def enrich_gold_csv_rows(
    rows: list[dict[str, str]],
    metadata_by_repo: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    """Fill missing metadata columns only; leave annotation fields unchanged."""
    enriched: list[dict[str, str]] = []
    for row in rows:
        updated = dict(row)
        repo_name = (row.get("repo_full_name") or "").strip()
        metadata = metadata_by_repo.get(repo_name)
        if metadata:
            for field in METADATA_FIELDS:
                if not (updated.get(field) or "").strip():
                    updated[field] = metadata.get(field, "")
        for field in ANNOTATION_FIELDS:
            if field in row:
                updated[field] = row[field]
        enriched.append(updated)
    return enriched


def read_gold_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    return rows, fieldnames


def write_gold_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> int:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def write_jsonl_atomic(path: Path, records: list[EligibleRepo]) -> int:
    """Write JSONL via a temporary file to make --in-place updates safer."""
    ensure_parent(path)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
        suffix=".tmp",
    ) as handle:
        tmp_path = Path(handle.name)
        for record in records:
            handle.write(record.model_dump_json())
            handle.write("\n")
        count = len(records)
    shutil.move(str(tmp_path), path)
    return count


def write_output_jsonl(path: Path, records: list[EligibleRepo], *, in_place: bool) -> int:
    if in_place:
        return write_jsonl_atomic(path, records)
    return write_jsonl(path, records)


def write_output_csv(
    path: Path,
    rows: list[dict[str, str]],
    fieldnames: list[str],
    *,
    in_place: bool,
) -> int:
    if not in_place:
        return write_gold_csv(path, rows, fieldnames)

    ensure_parent(path)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="",
        dir=path.parent,
        delete=False,
        suffix=".tmp",
    ) as handle:
        tmp_path = Path(handle.name)
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        count = len(rows)
    shutil.move(str(tmp_path), path)
    return count
