#!/usr/bin/env python3
"""Evaluate dual functional-evidence inspectors on the fixed RQ4 sample."""

from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.second_inspection_validation import (  # noqa: E402
    compute_second_inspection_evaluation,
    render_manuscript_table_rq4,
)

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference",
        type=Path,
        default=Path("data/processed/inspection_sample_50.csv"),
        help="Reference CSV with metadata consensus labels",
    )
    parser.add_argument(
        "--inspector1-completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_completed_fixed.csv"),
        help="Completed first-inspector worksheet",
    )
    parser.add_argument(
        "--inspector2-completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_second_inspector_completed.csv"),
        help="Completed second-inspector worksheet",
    )
    parser.add_argument(
        "--blank",
        type=Path,
        default=Path("data/processed/inspection_sample_50_second_inspector_blank.csv"),
        help="Second-inspector blank worksheet defining the expected repository set",
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
        default=Path("data/processed/second_inspection_validation_results.json"),
        help="Primary evaluation JSON output",
    )
    parser.add_argument(
        "--confusion-output",
        type=Path,
        default=Path("data/processed/second_inspection_confusion_matrices.csv"),
        help="Confusion-matrix CSV output",
    )
    parser.add_argument(
        "--disagreement-output",
        type=Path,
        default=Path("data/processed/second_inspection_disagreement_stats.json"),
        help="Disagreement-decomposition JSON output",
    )
    parser.add_argument(
        "--table-output",
        type=Path,
        default=Path("data/processed/manuscript_table_rq4_second_inspector.tex"),
        help="LaTeX table snippet for the manuscript",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    required = (
        args.reference,
        args.inspector1_completed,
        args.inspector2_completed,
        args.blank,
    )
    for path in required:
        if not path.exists():
            logger.error("Input not found: %s", path)
            if path == args.inspector2_completed:
                logger.error(
                    "Complete %s before evaluation. Use validate_second_inspection.py first.",
                    args.inspector2_completed,
                )
            return 1

    try:
        result = compute_second_inspection_evaluation(
            reference_path=args.reference,
            inspector1_completed_path=args.inspector1_completed,
            inspector2_completed_path=args.inspector2_completed,
            blank_path=args.blank,
            n_bootstrap=args.bootstrap_replicates,
            seed=args.seed,
        )
    except ValueError as exc:
        logger.error("%s", exc)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    with args.confusion_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["comparison", "row_label", "col_label", "count"],
        )
        writer.writeheader()
        writer.writerows(result["confusion_matrices"])

    disagreement_payload = {
        "schema_version": result["schema_version"],
        "paired_repositories": result["paired_repositories"],
        "comparisons": result["disagreement_stats"],
    }
    args.disagreement_output.write_text(
        json.dumps(disagreement_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    args.table_output.write_text(render_manuscript_table_rq4(result), encoding="utf-8")

    for name, block in result["comparisons"].items():
        three_class = block["three_class"]
        logger.info(
            "%s: n=%d agreement=%.3f kappa=%s",
            name,
            three_class["n"],
            three_class["agreement"] or 0.0,
            three_class["kappa"],
        )

    logger.info("Wrote %s", args.output)
    logger.info("Wrote %s", args.confusion_output)
    logger.info("Wrote %s", args.disagreement_output)
    logger.info("Wrote %s", args.table_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
