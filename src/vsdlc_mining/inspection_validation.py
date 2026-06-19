"""Metrics for metadata-vs-repository-inspection validation."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from vsdlc_mining.annotation_agreement import (
    cohens_kappa,
    confusion_matrix,
    per_class_metrics,
)
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS
from vsdlc_mining.inspection_sample import (
    INSPECTION_EVIDENCE_SOURCE_FIELDS,
    MIN_INSPECTION_EVIDENCE_SOURCES,
)

BINARY_EXCLUDE_LABELS = ("EXCLUDE", "NON_EXCLUDE")
BINARY_AI_CONVENTIONAL_LABELS = ("AI_PRODUCT", "CONVENTIONAL_SOFTWARE")


def _read_csv_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keyed: dict[str, dict[str, str]] = {}
    for row in rows:
        repo = row.get("repo_full_name", "").strip()
        if repo:
            keyed[repo] = row
    return keyed


def _normalize_label(label: str) -> str:
    return label.strip().upper()


def _parse_boolean(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"true", "1", "yes", "y"}


def _count_evidence_sources(row: dict[str, str]) -> int:
    return sum(1 for field in INSPECTION_EVIDENCE_SOURCE_FIELDS if _parse_boolean(row.get(field, "")))


def collect_functional_evidence_warnings(
    completed: dict[str, dict[str, str]],
    repos: list[str],
) -> list[dict[str, str | int]]:
    """Return protocol compliance warnings for functional inspection evidence."""
    warnings: list[dict[str, str | int]] = []
    for repo in repos:
        row = completed[repo]
        functional_evidence = row.get("functional_evidence", "").strip()
        evidence_source_count = _count_evidence_sources(row)
        if not functional_evidence:
            warnings.append(
                {
                    "repo_full_name": repo,
                    "warning_type": "missing_functional_evidence",
                    "message": (
                        f"{repo}: functional_evidence is missing; "
                        "record one sentence of functional repository evidence."
                    ),
                }
            )
        if evidence_source_count < MIN_INSPECTION_EVIDENCE_SOURCES:
            warnings.append(
                {
                    "repo_full_name": repo,
                    "warning_type": "insufficient_evidence_sources",
                    "message": (
                        f"{repo}: only {evidence_source_count} evidence-source boolean(s) are true; "
                        f"inspect at least {MIN_INSPECTION_EVIDENCE_SOURCES} sources when available."
                    ),
                    "evidence_source_count": evidence_source_count,
                }
            )
    return warnings


def _collapse_exclude_binary(label: str) -> str | None:
    normalized = _normalize_label(label)
    if normalized == "EXCLUDE":
        return "EXCLUDE"
    if normalized in {"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"}:
        return "NON_EXCLUDE"
    return None


def _paired_reference_inspection(
    reference: dict[str, dict[str, str]],
    completed: dict[str, dict[str, str]],
) -> tuple[list[str], list[str], list[str]]:
    repos = sorted(set(reference) & set(completed))
    majority_labels: list[str] = []
    inspection_labels: list[str] = []
    used_repos: list[str] = []

    for repo in repos:
        majority = _normalize_label(reference[repo].get("majority_label", ""))
        inspection = _normalize_label(completed[repo].get("inspection_label", ""))
        if majority not in PRIMARY_LABELS:
            continue
        if inspection not in PRIMARY_LABELS:
            continue
        majority_labels.append(majority)
        inspection_labels.append(inspection)
        used_repos.append(repo)

    return majority_labels, inspection_labels, used_repos


def agreement_by_class(
    reference_labels: list[str],
    inspection_labels: list[str],
    categories: tuple[str, ...],
) -> dict[str, dict[str, float | int]]:
    by_class: dict[str, dict[str, float | int]] = {}
    for category in categories:
        indices = [index for index, label in enumerate(reference_labels) if label == category]
        if not indices:
            by_class[category] = {"n_reference": 0, "agreement_count": 0, "agreement_rate": 0.0}
            continue
        agreements = sum(
            1 for index in indices if reference_labels[index] == inspection_labels[index]
        )
        by_class[category] = {
            "n_reference": len(indices),
            "agreement_count": agreements,
            "agreement_rate": agreements / len(indices),
        }
    return by_class


def compute_inspection_validation(
    reference_path: Path,
    completed_path: Path,
) -> dict[str, Any]:
    reference = _read_csv_rows(reference_path)
    completed = _read_csv_rows(completed_path)

    majority_labels, inspection_labels, repos = _paired_reference_inspection(reference, completed)
    if not repos:
        raise ValueError(
            "No paired repositories with valid majority_label and inspection_label. "
            "Complete inspection_sample_50_blank.csv before evaluation."
        )

    functional_evidence_warnings = collect_functional_evidence_warnings(completed, repos)

    disagreements = [
        {
            "repo_full_name": repo,
            "majority_label": majority_labels[index],
            "inspection_label": inspection_labels[index],
            "claude_label": _normalize_label(reference[repo].get("claude_label", "")),
            "human1_label": _normalize_label(reference[repo].get("human1_label", "")),
            "human2_label": _normalize_label(reference[repo].get("human2_label", "")),
            "inspection_evidence": completed[repo].get("inspection_evidence", ""),
            "functional_evidence": completed[repo].get("functional_evidence", ""),
            "evidence_source_count": _count_evidence_sources(completed[repo]),
        }
        for index, repo in enumerate(repos)
        if majority_labels[index] != inspection_labels[index]
    ]

    exclude_pairs = [
        (_collapse_exclude_binary(majority), _collapse_exclude_binary(inspection))
        for majority, inspection in zip(majority_labels, inspection_labels)
    ]
    exclude_majority = [majority for majority, _ in exclude_pairs if majority is not None]
    exclude_inspection = [inspection for _, inspection in exclude_pairs if inspection is not None]

    ai_conv_indices = [
        index
        for index, (majority, inspection) in enumerate(zip(majority_labels, inspection_labels))
        if majority in BINARY_AI_CONVENTIONAL_LABELS and inspection in BINARY_AI_CONVENTIONAL_LABELS
    ]
    ai_conv_majority = [majority_labels[index] for index in ai_conv_indices]
    ai_conv_inspection = [inspection_labels[index] for index in ai_conv_indices]

    agreement_count = sum(
        1 for majority, inspection in zip(majority_labels, inspection_labels) if majority == inspection
    )

    return {
        "schema_version": "0.2",
        "reference_file": str(reference_path),
        "completed_file": str(completed_path),
        "paired_repositories": len(repos),
        "agreement_rate": agreement_count / len(repos),
        "agreement_count": agreement_count,
        "cohens_kappa": cohens_kappa(majority_labels, inspection_labels, PRIMARY_LABELS),
        "confusion_matrix": confusion_matrix(majority_labels, inspection_labels, PRIMARY_LABELS),
        "disagreements": disagreements,
        "functional_evidence_warnings": functional_evidence_warnings,
        "functional_evidence_warning_count": len(functional_evidence_warnings),
        "agreement_by_class": agreement_by_class(
            majority_labels,
            inspection_labels,
            PRIMARY_LABELS,
        ),
        "per_class_metrics_inspection_vs_majority": per_class_metrics(
            inspection_labels,
            majority_labels,
            PRIMARY_LABELS,
        ),
        "exclude_vs_non_exclude": {
            "labels": list(BINARY_EXCLUDE_LABELS),
            "paired_repositories": len(exclude_majority),
            "agreement_rate": (
                sum(1 for a, b in zip(exclude_majority, exclude_inspection) if a == b) / len(exclude_majority)
                if exclude_majority
                else None
            ),
            "cohens_kappa": cohens_kappa(exclude_majority, exclude_inspection, BINARY_EXCLUDE_LABELS),
            "confusion_matrix": confusion_matrix(
                exclude_majority,
                exclude_inspection,
                BINARY_EXCLUDE_LABELS,
            ),
        },
        "ai_product_vs_conventional_excluding_exclude": {
            "labels": list(BINARY_AI_CONVENTIONAL_LABELS),
            "paired_repositories": len(ai_conv_majority),
            "agreement_rate": (
                sum(1 for a, b in zip(ai_conv_majority, ai_conv_inspection) if a == b) / len(ai_conv_majority)
                if ai_conv_majority
                else None
            ),
            "cohens_kappa": cohens_kappa(ai_conv_majority, ai_conv_inspection, BINARY_AI_CONVENTIONAL_LABELS),
            "confusion_matrix": confusion_matrix(
                ai_conv_majority,
                ai_conv_inspection,
                BINARY_AI_CONVENTIONAL_LABELS,
            ),
        },
    }
