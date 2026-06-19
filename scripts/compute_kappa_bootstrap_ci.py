#!/usr/bin/env python3
"""Compute manuscript Cohen's kappa point estimates with 95% bootstrap CIs."""

from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.annotation_agreement import cohens_kappa  # noqa: E402
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS  # noqa: E402
from vsdlc_mining.inspection_validation import (  # noqa: E402
    BINARY_AI_CONVENTIONAL_LABELS,
    BINARY_EXCLUDE_LABELS,
    compute_inspection_validation,
)
from vsdlc_mining.kappa_bootstrap import (  # noqa: E402
    apply_pair_transform,
    bootstrap_paired_metrics,
    filter_pairs,
)

logger = logging.getLogger(__name__)

AI_CONV_LABELS = {"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"}


def _read_comparison_rows(path: Path) -> tuple[list[str], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
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


def _collapse_exclude_pair(left: str, right: str) -> tuple[str, str] | None:
    categories = {"EXCLUDE", "NON_EXCLUDE"}
    collapsed_left = "EXCLUDE" if left == "EXCLUDE" else "NON_EXCLUDE" if left in AI_CONV_LABELS else None
    collapsed_right = "EXCLUDE" if right == "EXCLUDE" else "NON_EXCLUDE" if right in AI_CONV_LABELS else None
    if collapsed_left not in categories or collapsed_right not in categories:
        return None
    return collapsed_left, collapsed_right


def _human_human_metrics(
    comparison_path: Path,
    *,
    n_bootstrap: int,
    seed: int,
) -> dict[str, Any]:
    labels_a, labels_b = _read_comparison_rows(comparison_path)

    three_class = bootstrap_paired_metrics(
        labels_a,
        labels_b,
        PRIMARY_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed,
    )

    ai_conv_a, ai_conv_b = filter_pairs(
        labels_a,
        labels_b,
        lambda left, right: left in AI_CONV_LABELS and right in AI_CONV_LABELS,
    )
    ai_conv = bootstrap_paired_metrics(
        ai_conv_a,
        ai_conv_b,
        BINARY_AI_CONVENTIONAL_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 1,
    )

    exclude_a, exclude_b = apply_pair_transform(labels_a, labels_b, _collapse_exclude_pair)
    exclude_binary = bootstrap_paired_metrics(
        exclude_a,
        exclude_b,
        BINARY_EXCLUDE_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 2,
    )

    return {
        "comparison_file": str(comparison_path),
        "paired_repositories": len(labels_a),
        "three_class": three_class,
        "ai_product_vs_conventional": ai_conv,
        "exclude_vs_non_exclude": exclude_binary,
    }


def _inspection_metrics(
    reference_path: Path,
    completed_path: Path,
    *,
    n_bootstrap: int,
    seed: int,
) -> dict[str, Any]:
    validation = compute_inspection_validation(reference_path, completed_path)

    majority_labels: list[str] = []
    inspection_labels: list[str] = []
    with reference_path.open(encoding="utf-8", newline="") as handle:
        reference_rows = {row["repo_full_name"]: row for row in csv.DictReader(handle) if row.get("repo_full_name")}
    with completed_path.open(encoding="utf-8", newline="") as handle:
        completed_rows = {row["repo_full_name"]: row for row in csv.DictReader(handle) if row.get("repo_full_name")}

    repos = sorted(set(reference_rows) & set(completed_rows))
    for repo in repos:
        majority = (reference_rows[repo].get("majority_label") or "").strip().upper()
        inspection = (completed_rows[repo].get("inspection_label") or "").strip().upper()
        if majority in PRIMARY_LABELS and inspection in PRIMARY_LABELS:
            majority_labels.append(majority)
            inspection_labels.append(inspection)

    three_class = bootstrap_paired_metrics(
        majority_labels,
        inspection_labels,
        PRIMARY_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 10,
    )

    ai_conv_a, ai_conv_b = filter_pairs(
        majority_labels,
        inspection_labels,
        lambda left, right: left in AI_CONV_LABELS and right in AI_CONV_LABELS,
    )
    ai_conv = bootstrap_paired_metrics(
        ai_conv_a,
        ai_conv_b,
        BINARY_AI_CONVENTIONAL_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 11,
    )

    exclude_a, exclude_b = apply_pair_transform(
        majority_labels,
        inspection_labels,
        _collapse_exclude_pair,
    )
    exclude_binary = bootstrap_paired_metrics(
        exclude_a,
        exclude_b,
        BINARY_EXCLUDE_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 12,
    )

    return {
        "reference_file": str(reference_path),
        "completed_file": str(completed_path),
        "paired_repositories": len(majority_labels),
        "three_class": three_class,
        "ai_product_vs_conventional": ai_conv,
        "exclude_vs_non_exclude": exclude_binary,
        "validation_point_estimates": {
            "cohens_kappa": validation["cohens_kappa"],
            "exclude_vs_non_exclude_kappa": validation["exclude_vs_non_exclude"]["cohens_kappa"],
            "ai_product_vs_conventional_kappa": validation[
                "ai_product_vs_conventional_excluding_exclude"
            ]["cohens_kappa"],
        },
    }


def _format_rate(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{100 * value:.1f}%"


def _format_kappa(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.3f}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--comparison",
        type=Path,
        default=Path("data/processed/gold_sample_330_three_annotator_comparison.csv"),
        help="Three-annotator comparison CSV for human1 vs human2",
    )
    parser.add_argument(
        "--inspection-reference",
        type=Path,
        default=Path("data/processed/inspection_sample_50.csv"),
        help="Inspection reference CSV with majority_label",
    )
    parser.add_argument(
        "--inspection-completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_completed_fixed.csv"),
        help="Completed inspection CSV with inspection_label filled",
    )
    parser.add_argument(
        "--bootstrap-replicates",
        type=int,
        default=10_000,
        help="Number of bootstrap resamples",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for bootstrap resampling",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/kappa_bootstrap_ci.json"),
        help="JSON output with point estimates and 95% bootstrap CIs",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.comparison, args.inspection_reference, args.inspection_completed):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    result = {
        "schema_version": "0.2",
        "method": {
            "ci_level": 0.95,
            "bootstrap_replicates": args.bootstrap_replicates,
            "seed": args.seed,
            "estimator": "percentile bootstrap on paired repository labels",
        },
        "human_human": _human_human_metrics(
            args.comparison,
            n_bootstrap=args.bootstrap_replicates,
            seed=args.seed,
        ),
        "metadata_vs_inspection": _inspection_metrics(
            args.inspection_reference,
            args.inspection_completed,
            n_bootstrap=args.bootstrap_replicates,
            seed=args.seed,
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for label, block in (
        ("Human-human three-class", result["human_human"]["three_class"]),
        ("Human-human AI vs CONV", result["human_human"]["ai_product_vs_conventional"]),
        ("Human-human EXCLUDE binary", result["human_human"]["exclude_vs_non_exclude"]),
        ("Inspection three-class", result["metadata_vs_inspection"]["three_class"]),
        ("Inspection AI vs CONV", result["metadata_vs_inspection"]["ai_product_vs_conventional"]),
        ("Inspection EXCLUDE binary", result["metadata_vs_inspection"]["exclude_vs_non_exclude"]),
    ):
        logger.info(
            "%s: n=%s agreement=%s [%s, %s] kappa=%s [%s, %s]",
            label,
            block["n"],
            _format_rate(block["agreement"]),
            _format_kappa(block["agreement_ci_lower"]),
            _format_kappa(block["agreement_ci_upper"]),
            _format_kappa(block["kappa"]),
            _format_kappa(block["kappa_ci_lower"]),
            _format_kappa(block["kappa_ci_upper"]),
        )

    logger.info("Wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
