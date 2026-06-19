#!/usr/bin/env python3
"""Create a stratified inspection validation sample for repository-level review."""

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

from vsdlc_mining.inspection_sample import (  # noqa: E402
    DEFAULT_INSPECTION_SAMPLE_SIZE,
    DEFAULT_INSPECTION_SEED,
    INSPECTION_STRATUM_TARGETS,
    build_sampling_summary,
    eligible_repo_lookup,
    read_comparison_rows,
    stratified_inspection_sample,
    write_inspection_blank_csv,
    write_inspection_sample_csv,
)
from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.utils import read_jsonl  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--comparison",
        type=Path,
        default=Path("data/processed/gold_sample_330_three_annotator_comparison.csv"),
        help="Three-annotator comparison CSV with majority_label",
    )
    parser.add_argument(
        "--enriched",
        type=Path,
        default=Path("data/interim/eligible_repos_enriched.jsonl"),
        help="Enriched eligible repositories JSONL",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/inspection_sample_50.csv"),
        help="Inspection sample CSV with metadata labels",
    )
    parser.add_argument(
        "--blank-output",
        type=Path,
        default=Path("data/processed/inspection_sample_50_blank.csv"),
        help="Blind inspection worksheet CSV without prior labels",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=None,
        help="Optional JSON summary of sampling decisions",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_INSPECTION_SEED,
        help="Random seed for reproducible stratified sampling",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.comparison, args.enriched):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    comparison_rows = read_comparison_rows(args.comparison)
    enriched = read_jsonl(args.enriched, EligibleRepo)
    enriched_by_name = eligible_repo_lookup(enriched)

    sample = stratified_inspection_sample(
        comparison_rows,
        enriched_by_name=enriched_by_name,
        stratum_targets=INSPECTION_STRATUM_TARGETS,
        seed=args.seed,
    )

    expected_size = sum(INSPECTION_STRATUM_TARGETS.values())
    if len(sample) != expected_size:
        logger.warning(
            "Selected %d repositories (target %d). Check stratum pool sizes in comparison file.",
            len(sample),
            expected_size,
        )

    sample_count = write_inspection_sample_csv(args.output, sample)
    blank_count = write_inspection_blank_csv(args.blank_output, sample)
    logger.info("Wrote %d repositories to %s", sample_count, args.output)
    logger.info("Wrote %d repositories to %s", blank_count, args.blank_output)

    summary = build_sampling_summary(
        comparison_rows=comparison_rows,
        selected_rows=sample,
        seed=args.seed,
        stratum_targets=INSPECTION_STRATUM_TARGETS,
    )
    logger.info("Majority label distribution: %s", summary["majority_label_distribution"])
    logger.info("Priority score distribution: %s", summary["priority_score_distribution"])
    logger.info("Human disagreement cases in sample: %d", summary["human_disagreement_count"])
    logger.info("EXCLUDE-involved cases in sample: %d", summary["exclude_involved_count"])
    logger.info(
        "Claude-vs-human disagreement cases in sample: %d",
        summary["claude_human_disagreement_count"],
    )

    if args.summary_output is not None:
        args.summary_output.parent.mkdir(parents=True, exist_ok=True)
        args.summary_output.write_text(
            json.dumps(summary, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        logger.info("Wrote sampling summary to %s", args.summary_output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
