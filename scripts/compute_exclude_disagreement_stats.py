#!/usr/bin/env python3
"""Compute EXCLUDE-attributable disagreement statistics for the manuscript."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.annotation_agreement import confusion_matrix  # noqa: E402
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS  # noqa: E402

PRODUCT_LABELS = {"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"}


def _off_diagonal_cells(matrix: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []
    for row_label, row in matrix.items():
        for col_label, count in row.items():
            if row_label != col_label and count:
                cells.append(
                    {
                        "row_label": row_label,
                        "col_label": col_label,
                        "count": count,
                    }
                )
    return cells


def _classify_disagreement(row_label: str, col_label: str) -> str:
    labels = {row_label, col_label}
    if labels == {"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"}:
        return "ai_product_vs_conventional"
    if labels == {"EXCLUDE", "CONVENTIONAL_SOFTWARE"}:
        return "exclude_vs_conventional"
    if labels == {"EXCLUDE", "AI_PRODUCT"}:
        return "exclude_vs_ai_product"
    return "other"


def _summarize_pair(
    labels_a: list[str],
    labels_b: list[str],
    *,
    source: str,
) -> dict[str, Any]:
    matrix = confusion_matrix(labels_a, labels_b, PRIMARY_LABELS)
    cells = _off_diagonal_cells(matrix)
    total_disagreements = sum(cell["count"] for cell in cells)

    by_pattern: dict[str, int] = {
        "exclude_vs_conventional": 0,
        "exclude_vs_ai_product": 0,
        "ai_product_vs_conventional": 0,
        "other": 0,
    }
    for cell in cells:
        pattern = _classify_disagreement(cell["row_label"], cell["col_label"])
        by_pattern[pattern] += cell["count"]

    exclude_involving = by_pattern["exclude_vs_conventional"] + by_pattern["exclude_vs_ai_product"]
    product_role_only = by_pattern["ai_product_vs_conventional"]

    def pct(count: int) -> float:
        return round(100 * count / total_disagreements, 1) if total_disagreements else 0.0

    row_a_exclude = sum(1 for label in labels_a if label == "EXCLUDE")
    row_a_conv = sum(1 for label in labels_a if label == "CONVENTIONAL_SOFTWARE")
    agree_when_a_exclude = sum(
        1 for a, b in zip(labels_a, labels_b) if a == "EXCLUDE" and a == b
    )
    agree_when_a_conv = sum(
        1 for a, b in zip(labels_a, labels_b) if a == "CONVENTIONAL_SOFTWARE" and a == b
    )

    return {
        "source": source,
        "paired_repositories": len(labels_a),
        "total_disagreements": total_disagreements,
        "disagreement_rate": round(total_disagreements / len(labels_a), 3) if labels_a else 0.0,
        "patterns": {
            key: {
                "count": count,
                "percent_of_disagreements": pct(count),
            }
            for key, count in by_pattern.items()
        },
        "exclude_involving": {
            "count": exclude_involving,
            "percent_of_disagreements": pct(exclude_involving),
        },
        "product_role_only": {
            "count": product_role_only,
            "percent_of_disagreements": pct(product_role_only),
        },
        "conditional_agreement_when_reference_is": {
            "exclude": {
                "n": row_a_exclude,
                "agreement_count": agree_when_a_exclude,
                "agreement_rate": round(agree_when_a_exclude / row_a_exclude, 3)
                if row_a_exclude
                else None,
            },
            "conventional_software": {
                "n": row_a_conv,
                "agreement_count": agree_when_a_conv,
                "agreement_rate": round(agree_when_a_conv / row_a_conv, 3)
                if row_a_conv
                else None,
            },
        },
        "confusion_matrix": matrix,
    }


def _read_human_human(comparison_path: Path) -> tuple[list[str], list[str]]:
    with comparison_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    labels_a: list[str] = []
    labels_b: list[str] = []
    for row in rows:
        left = (row.get("human1_label") or "").strip().upper()
        right = (row.get("human2_label") or "").strip().upper()
        if left in PRIMARY_LABELS and right in PRIMARY_LABELS:
            labels_a.append(left)
            labels_b.append(right)
    return labels_a, labels_b


def _read_metadata_inspection(reference_path: Path, completed_path: Path) -> tuple[list[str], list[str]]:
    with reference_path.open(encoding="utf-8", newline="") as handle:
        reference = {row["repo_full_name"]: row for row in csv.DictReader(handle) if row.get("repo_full_name")}
    with completed_path.open(encoding="utf-8", newline="") as handle:
        completed = {row["repo_full_name"]: row for row in csv.DictReader(handle) if row.get("repo_full_name")}

    majority_labels: list[str] = []
    inspection_labels: list[str] = []
    for repo in sorted(set(reference) & set(completed)):
        majority = (reference[repo].get("majority_label") or "").strip().upper()
        inspection = (completed[repo].get("inspection_label") or "").strip().upper()
        if majority in PRIMARY_LABELS and inspection in PRIMARY_LABELS:
            majority_labels.append(majority)
            inspection_labels.append(inspection)
    return majority_labels, inspection_labels


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--comparison",
        type=Path,
        default=Path("data/processed/gold_sample_330_three_annotator_comparison.csv"),
    )
    parser.add_argument(
        "--inspection-reference",
        type=Path,
        default=Path("data/processed/inspection_sample_50.csv"),
    )
    parser.add_argument(
        "--inspection-completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_completed_fixed.csv"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/exclude_disagreement_stats.json"),
    )
    args = parser.parse_args()

    human_a, human_b = _read_human_human(args.comparison)
    majority, inspection = _read_metadata_inspection(
        args.inspection_reference,
        args.inspection_completed,
    )

    result = {
        "schema_version": "0.2",
        "human_human": _summarize_pair(human_a, human_b, source="human1_vs_human2"),
        "metadata_vs_inspection": _summarize_pair(
            majority,
            inspection,
            source="annotation_consensus_vs_inspection",
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
