"""Stratified sampling for metadata-vs-inspection validation studies."""

from __future__ import annotations

import csv
import random
from collections import Counter
from pathlib import Path
from typing import Any

from vsdlc_mining.decontamination_schema import PRIMARY_LABELS
from vsdlc_mining.metadata import (
    format_ci_evidence,
    format_instruction_artifacts,
    format_release_evidence,
)
from vsdlc_mining.models import EligibleRepo

DEFAULT_INSPECTION_SAMPLE_SIZE = 50
DEFAULT_INSPECTION_SEED = 42

INSPECTION_STRATUM_TARGETS: dict[str, int] = {
    "CONVENTIONAL_SOFTWARE": 20,
    "AI_PRODUCT": 15,
    "EXCLUDE": 15,
}

INSPECTION_SAMPLE_FIELDS = [
    "repo_full_name",
    "repo_url",
    "majority_label",
    "claude_label",
    "human1_label",
    "human2_label",
    "stars",
    "primary_language",
    "github_description",
    "github_topics",
    "detected_instruction_artifacts",
    "ci_evidence",
    "release_evidence",
]

INSPECTION_BLANK_METADATA_FIELDS = [
    "repo_full_name",
    "repo_url",
    "stars",
    "primary_language",
    "github_description",
    "github_topics",
    "detected_instruction_artifacts",
    "ci_evidence",
    "release_evidence",
]

INSPECTION_BLANK_INSPECTION_FIELDS = [
    "inspection_label",
    "inspection_confidence",
    "inspection_evidence",
    "inspected_readme",
    "inspected_file_tree",
    "inspected_dependencies",
    "inspected_entrypoints",
    "inspected_instruction_consumption",
    "functional_evidence",
    "inspection_notes",
]

INSPECTION_BLANK_FIELDS = INSPECTION_BLANK_METADATA_FIELDS + INSPECTION_BLANK_INSPECTION_FIELDS

SECOND_INSPECTOR_BLANK_INSPECTION_FIELDS = [
    "inspector2_label",
    "inspector2_confidence",
    "inspector2_evidence_sources",
    "inspector2_functional_note",
    "inspector2_free_notes",
]

SECOND_INSPECTOR_BLANK_FIELDS = (
    INSPECTION_BLANK_METADATA_FIELDS + SECOND_INSPECTOR_BLANK_INSPECTION_FIELDS
)

INSPECTOR2_EVIDENCE_SOURCE_TOKENS = frozenset(
    {
        "readme",
        "file_tree",
        "dependencies",
        "entrypoints",
        "instruction_consumption",
    }
)

INSPECTION_EVIDENCE_SOURCE_FIELDS = (
    "inspected_readme",
    "inspected_file_tree",
    "inspected_dependencies",
    "inspected_entrypoints",
    "inspected_instruction_consumption",
)

MIN_INSPECTION_EVIDENCE_SOURCES = 2


def _normalize_label(label: str) -> str:
    return label.strip().upper()


def inspection_priority_score(row: dict[str, str]) -> int:
    """Higher scores indicate disagreement-heavy cases to prefer in sampling."""
    claude = _normalize_label(row.get("claude_label", ""))
    human1 = _normalize_label(row.get("human1_label", ""))
    human2 = _normalize_label(row.get("human2_label", ""))
    score = 0
    if human1 and human2 and human1 != human2:
        score += 1
    if "EXCLUDE" in {claude, human1, human2}:
        score += 1
    if claude and ((human1 and claude != human1) or (human2 and claude != human2)):
        score += 1
    return score


def _comparison_row_key(row: dict[str, str]) -> str:
    return row.get("repo_full_name", "").strip()


def read_comparison_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def eligible_repo_lookup(repos: list[EligibleRepo]) -> dict[str, EligibleRepo]:
    return {repo.full_name: repo for repo in repos}


def _eligible_row(repo: EligibleRepo) -> dict[str, str]:
    topics = repo.github_topics or []
    return {
        "repo_full_name": repo.full_name,
        "repo_url": repo.repository_url,
        "stars": str(repo.stars),
        "primary_language": repo.primary_language or "",
        "github_description": repo.github_description or "",
        "github_topics": "|".join(topics),
        "detected_instruction_artifacts": format_instruction_artifacts(
            queries=repo.queries,
            matched_paths=repo.matched_paths,
        ),
        "ci_evidence": format_ci_evidence(repo.evidence),
        "release_evidence": format_release_evidence(repo.evidence),
    }


def stratified_inspection_sample(
    comparison_rows: list[dict[str, str]],
    *,
    enriched_by_name: dict[str, EligibleRepo],
    stratum_targets: dict[str, int] | None = None,
    seed: int = DEFAULT_INSPECTION_SEED,
) -> list[dict[str, str]]:
    """Sample repositories stratified by majority_label, preferring disagreements."""
    targets = stratum_targets or INSPECTION_STRATUM_TARGETS
    rng = random.Random(seed)

    eligible_rows = [
        row
        for row in comparison_rows
        if _normalize_label(row.get("majority_label", "")) in PRIMARY_LABELS
        and _comparison_row_key(row) in enriched_by_name
    ]

    by_majority: dict[str, list[dict[str, str]]] = {label: [] for label in PRIMARY_LABELS}
    for row in eligible_rows:
        majority = _normalize_label(row["majority_label"])
        by_majority[majority].append(row)

    selected: list[dict[str, str]] = []
    selected_names: set[str] = set()

    for majority_label in PRIMARY_LABELS:
        target = targets.get(majority_label, 0)
        pool = by_majority[majority_label]
        if target <= 0:
            continue
        if not pool:
            continue

        ranked = sorted(
            pool,
            key=lambda row: (
                -inspection_priority_score(row),
                rng.random(),
                _comparison_row_key(row),
            ),
        )
        for row in ranked:
            repo_name = _comparison_row_key(row)
            if repo_name in selected_names:
                continue
            repo = enriched_by_name[repo_name]
            merged = _eligible_row(repo)
            merged.update(
                {
                    "majority_label": _normalize_label(row["majority_label"]),
                    "claude_label": _normalize_label(row.get("claude_label", "")),
                    "human1_label": _normalize_label(row.get("human1_label", "")),
                    "human2_label": _normalize_label(row.get("human2_label", "")),
                }
            )
            selected.append(merged)
            selected_names.add(repo_name)
            if len([item for item in selected if item["majority_label"] == majority_label]) >= target:
                break

    return sorted(selected, key=lambda row: row["repo_full_name"])


def majority_label_distribution(rows: list[dict[str, str]]) -> dict[str, int]:
    return dict(Counter(row.get("majority_label", "") for row in rows))


def priority_score_distribution(comparison_rows: list[dict[str, str]], selected_names: set[str]) -> dict[str, int]:
    selected_scores = [
        inspection_priority_score(row)
        for row in comparison_rows
        if _comparison_row_key(row) in selected_names
    ]
    return dict(Counter(str(score) for score in selected_scores))


def write_inspection_sample_csv(path: Path, rows: list[dict[str, str]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INSPECTION_SAMPLE_FIELDS)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in INSPECTION_SAMPLE_FIELDS} for row in rows)
    return len(rows)


def write_inspection_blank_csv(path: Path, rows: list[dict[str, str]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    blank_rows: list[dict[str, str]] = []
    for row in rows:
        blank = {field: row.get(field, "") for field in INSPECTION_BLANK_METADATA_FIELDS}
        blank.update(dict.fromkeys(INSPECTION_BLANK_INSPECTION_FIELDS, ""))
        blank_rows.append(blank)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INSPECTION_BLANK_FIELDS)
        writer.writeheader()
        writer.writerows(blank_rows)
    return len(blank_rows)


def write_second_inspector_blank_csv(path: Path, rows: list[dict[str, str]]) -> int:
    """Write a blind worksheet for a second functional-evidence inspector."""
    path.parent.mkdir(parents=True, exist_ok=True)
    blank_rows: list[dict[str, str]] = []
    for row in rows:
        blank = {field: row.get(field, "") for field in INSPECTION_BLANK_METADATA_FIELDS}
        blank.update(dict.fromkeys(SECOND_INSPECTOR_BLANK_INSPECTION_FIELDS, ""))
        blank_rows.append(blank)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SECOND_INSPECTOR_BLANK_FIELDS)
        writer.writeheader()
        writer.writerows(blank_rows)
    return len(blank_rows)


def read_second_inspector_blank_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def build_sampling_summary(
    *,
    comparison_rows: list[dict[str, str]],
    selected_rows: list[dict[str, str]],
    seed: int,
    stratum_targets: dict[str, int],
) -> dict[str, Any]:
    selected_names = {row["repo_full_name"] for row in selected_rows}
    return {
        "seed": seed,
        "stratum_targets": stratum_targets,
        "comparison_pool_size": len(comparison_rows),
        "selected_size": len(selected_rows),
        "majority_label_distribution": majority_label_distribution(selected_rows),
        "priority_score_distribution": priority_score_distribution(comparison_rows, selected_names),
        "human_disagreement_count": sum(
            1
            for row in comparison_rows
            if _comparison_row_key(row) in selected_names
            and _normalize_label(row.get("human1_label", "")) != _normalize_label(row.get("human2_label", ""))
        ),
        "exclude_involved_count": sum(
            1
            for row in comparison_rows
            if _comparison_row_key(row) in selected_names
            and "EXCLUDE"
            in {
                _normalize_label(row.get("claude_label", "")),
                _normalize_label(row.get("human1_label", "")),
                _normalize_label(row.get("human2_label", "")),
            }
        ),
        "claude_human_disagreement_count": sum(
            1
            for row in comparison_rows
            if _comparison_row_key(row) in selected_names
            and (
                _normalize_label(row.get("claude_label", "")) != _normalize_label(row.get("human1_label", ""))
                or _normalize_label(row.get("claude_label", "")) != _normalize_label(row.get("human2_label", ""))
            )
        ),
    }
