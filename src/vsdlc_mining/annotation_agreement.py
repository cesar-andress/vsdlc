"""Inter-annotator agreement metrics for decontamination classification."""

from __future__ import annotations

import csv
import warnings
from collections import Counter
from pathlib import Path
from typing import Any

from vsdlc_mining.decontamination_schema import (
    BINARY_DECONTAMINATION_LABELS,
    LEGACY_PRIMARY_LABELS,
    PRIMARY_LABELS,
)


def _collapse_binary_decontamination(label: str) -> str | None:
    normalized = label.strip().upper()
    if normalized == "CONVENTIONAL_SOFTWARE":
        return "target_population"
    if normalized in {"AI_PRODUCT", "EXCLUDE"}:
        return "non_target"
    return None


def _read_annotations(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keyed: dict[str, dict[str, str]] = {}
    for row in rows:
        repo = row.get("repo_full_name", "").strip()
        if not repo:
            continue
        keyed[repo] = row
    return keyed


def _resolve_primary_label(
    row: dict[str, str],
    *,
    source: str,
    compatibility_warnings: list[str],
) -> str:
    primary = (row.get("primary_label") or "").strip().upper()
    if primary:
        if primary in LEGACY_PRIMARY_LABELS:
            compatibility_warnings.append(
                f"{source}: value '{primary}' in primary_label uses deprecated v0.1 schema; "
                "re-annotate with AI_PRODUCT / CONVENTIONAL_SOFTWARE / EXCLUDE."
            )
        return primary

    legacy = (row.get("label") or "").strip().upper()
    if legacy:
        compatibility_warnings.append(
            f"{source}: legacy 'label' column used for repo '{row.get('repo_full_name', '')}'. "
            "Migrate annotations to 'primary_label' (schema v0.2)."
        )
        return legacy
    return ""


def _paired_labels(
    left: dict[str, dict[str, str]],
    right: dict[str, dict[str, str]],
    *,
    compatibility_warnings: list[str],
) -> tuple[list[str], list[str], list[str]]:
    repos = sorted(set(left) & set(right))
    labels_a: list[str] = []
    labels_b: list[str] = []
    used_repos: list[str] = []
    for repo in repos:
        la = _resolve_primary_label(left[repo], source="annotator_a", compatibility_warnings=compatibility_warnings)
        lb = _resolve_primary_label(right[repo], source="annotator_b", compatibility_warnings=compatibility_warnings)
        if not la or not lb:
            continue
        labels_a.append(la)
        labels_b.append(lb)
        used_repos.append(repo)
    return labels_a, labels_b, used_repos


def cohens_kappa(labels_a: list[str], labels_b: list[str], categories: tuple[str, ...]) -> float | None:
    if not labels_a or len(labels_a) != len(labels_b):
        return None
    n = len(labels_a)
    observed = sum(1 for a, b in zip(labels_a, labels_b) if a == b) / n
    dist_a = Counter(labels_a)
    dist_b = Counter(labels_b)
    expected = sum((dist_a[cat] / n) * (dist_b[cat] / n) for cat in categories)
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1.0 - expected)


def confusion_matrix(
    labels_a: list[str],
    labels_b: list[str],
    categories: tuple[str, ...],
) -> dict[str, dict[str, int]]:
    matrix = {row: {col: 0 for col in categories} for row in categories}
    for a, b in zip(labels_a, labels_b):
        if a in matrix and b in matrix[a]:
            matrix[a][b] += 1
    return matrix


def per_class_metrics(
    predicted: list[str],
    gold: list[str],
    categories: tuple[str, ...],
) -> dict[str, dict[str, float | int]]:
    metrics: dict[str, dict[str, float | int]] = {}
    for cat in categories:
        tp = sum(1 for p, g in zip(predicted, gold) if p == cat and g == cat)
        fp = sum(1 for p, g in zip(predicted, gold) if p == cat and g != cat)
        fn = sum(1 for p, g in zip(predicted, gold) if p != cat and g == cat)
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        metrics[cat] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": precision,
            "recall": recall,
        }
    return metrics


def compute_annotation_agreement(
    annotator_a_path: Path,
    annotator_b_path: Path,
    *,
    adjudicated_path: Path | None = None,
) -> dict[str, Any]:
    compatibility_warnings: list[str] = []
    ann_a = _read_annotations(annotator_a_path)
    ann_b = _read_annotations(annotator_b_path)

    labels_a, labels_b, repos = _paired_labels(
        ann_a,
        ann_b,
        compatibility_warnings=compatibility_warnings,
    )
    binary_a = [_collapse_binary_decontamination(label) for label in labels_a]
    binary_b = [_collapse_binary_decontamination(label) for label in labels_b]
    binary_pairs = [
        (a, b)
        for a, b in zip(binary_a, binary_b)
        if a is not None and b is not None
    ]
    binary_a_clean = [a for a, _ in binary_pairs]
    binary_b_clean = [b for _, b in binary_pairs]

    disagreements = [
        {
            "repo_full_name": repo,
            "annotator_a_primary_label": _resolve_primary_label(
                ann_a[repo],
                source="annotator_a",
                compatibility_warnings=[],
            ),
            "annotator_b_primary_label": _resolve_primary_label(
                ann_b[repo],
                source="annotator_b",
                compatibility_warnings=[],
            ),
            "annotator_a_confidence": ann_a[repo].get("confidence", ""),
            "annotator_b_confidence": ann_b[repo].get("confidence", ""),
        }
        for repo in repos
        if _resolve_primary_label(ann_a[repo], source="annotator_a", compatibility_warnings=[])
        != _resolve_primary_label(ann_b[repo], source="annotator_b", compatibility_warnings=[])
    ]

    result: dict[str, Any] = {
        "schema_version": "0.2",
        "annotator_a": str(annotator_a_path),
        "annotator_b": str(annotator_b_path),
        "paired_repositories": len(repos),
        "compatibility_warnings": compatibility_warnings,
        "primary_three_class": {
            "labels": list(PRIMARY_LABELS),
            "kappa": cohens_kappa(labels_a, labels_b, PRIMARY_LABELS),
            "confusion_matrix": confusion_matrix(labels_a, labels_b, PRIMARY_LABELS),
            "label_distribution_a": dict(Counter(labels_a)),
            "label_distribution_b": dict(Counter(labels_b)),
        },
        "binary_decontamination": {
            "definition": {
                "target_population": ["CONVENTIONAL_SOFTWARE"],
                "non_target": ["AI_PRODUCT", "EXCLUDE"],
            },
            "kappa": cohens_kappa(binary_a_clean, binary_b_clean, BINARY_DECONTAMINATION_LABELS),
            "confusion_matrix": confusion_matrix(
                binary_a_clean,
                binary_b_clean,
                BINARY_DECONTAMINATION_LABELS,
            ),
        },
        "disagreements": disagreements,
    }

    if compatibility_warnings:
        for message in compatibility_warnings:
            warnings.warn(message, stacklevel=2)

    if adjudicated_path is not None and adjudicated_path.exists():
        adjudicated = _read_annotations(adjudicated_path)
        shared = [repo for repo in repos if repo in adjudicated]
        gold = [
            _resolve_primary_label(
                adjudicated[repo],
                source="adjudicated",
                compatibility_warnings=compatibility_warnings,
            )
            or (adjudicated[repo].get("adjudicated_label") or "").strip().upper()
            for repo in shared
        ]
        pred_a = [
            _resolve_primary_label(ann_a[repo], source="annotator_a", compatibility_warnings=[])
            for repo in shared
        ]
        pred_b = [
            _resolve_primary_label(ann_b[repo], source="annotator_b", compatibility_warnings=[])
            for repo in shared
        ]
        valid_idx = [i for i, g in enumerate(gold) if g in PRIMARY_LABELS]
        gold_valid = [gold[i] for i in valid_idx]
        pred_a_valid = [pred_a[i] for i in valid_idx]
        pred_b_valid = [pred_b[i] for i in valid_idx]
        result["adjudicated_evaluation"] = {
            "adjudicated_file": str(adjudicated_path),
            "paired_repositories": len(gold_valid),
            "annotator_a": per_class_metrics(pred_a_valid, gold_valid, PRIMARY_LABELS),
            "annotator_b": per_class_metrics(pred_b_valid, gold_valid, PRIMARY_LABELS),
        }

    return result
