#!/usr/bin/env python3
"""Evaluate agreement between metadata-derived labels and repository inspection."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.inspection_validation import compute_inspection_validation  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference",
        type=Path,
        default=Path("data/processed/inspection_sample_50.csv"),
        help="Reference CSV with majority_label and annotator labels",
    )
    parser.add_argument(
        "--completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_completed.csv"),
        help="Completed inspection CSV with inspection_label filled",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/inspection_validation_results.json"),
        help="Validation metrics JSON output",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.reference, args.completed):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    try:
        result = compute_inspection_validation(args.reference, args.completed)
    except ValueError as exc:
        logger.error("%s", exc)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    logger.info("Paired repositories: %d", result["paired_repositories"])
    logger.info("Agreement rate (majority vs inspection): %.3f", result["agreement_rate"])
    logger.info("Cohen's kappa: %s", result["cohens_kappa"])
    logger.info("Disagreements: %d", len(result["disagreements"]))
    logger.info(
        "EXCLUDE vs non-EXCLUDE kappa: %s",
        result["exclude_vs_non_exclude"]["cohens_kappa"],
    )
    logger.info(
        "AI_PRODUCT vs CONVENTIONAL_SOFTWARE (excluding EXCLUDE) kappa: %s",
        result["ai_product_vs_conventional_excluding_exclude"]["cohens_kappa"],
    )
    for warning in result.get("functional_evidence_warnings", []):
        logger.warning("Functional evidence: %s", warning["message"])
    if result.get("functional_evidence_warning_count", 0):
        logger.warning(
            "Functional evidence compliance warnings: %d",
            result["functional_evidence_warning_count"],
        )
    logger.info("Wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
