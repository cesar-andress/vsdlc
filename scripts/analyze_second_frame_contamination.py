#!/usr/bin/env python3
"""Analyze contamination in the AI-topic second discovery frame after annotation."""

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

from vsdlc_mining.config import (  # noqa: E402
    SECOND_FRAME_ANNOTATION_COMPLETED_PATH,
    SECOND_FRAME_PARAGRAPH_PATH,
    SECOND_FRAME_RESULTS_PATH,
    SECOND_FRAME_SAMPLE_PATH,
    SECOND_FRAME_TABLE_PATH,
)
from vsdlc_mining.second_frame_analysis import (  # noqa: E402
    analyze_second_frame_contamination,
    render_manuscript_paragraph,
    render_manuscript_table,
)
from vsdlc_mining.utils import setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annotation",
        type=Path,
        default=SECOND_FRAME_ANNOTATION_COMPLETED_PATH,
        help="Completed annotation CSV with primary_label filled.",
    )
    parser.add_argument("--sample", type=Path, default=SECOND_FRAME_SAMPLE_PATH)
    parser.add_argument("--output", type=Path, default=SECOND_FRAME_RESULTS_PATH)
    parser.add_argument("--table-output", type=Path, default=SECOND_FRAME_TABLE_PATH)
    parser.add_argument("--paragraph-output", type=Path, default=SECOND_FRAME_PARAGRAPH_PATH)
    parser.add_argument("--bootstrap-replicates", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("analyze_second_frame_contamination")

    if not args.annotation.exists():
        logger.error("Completed annotation file not found: %s", args.annotation)
        logger.error(
            "Complete %s and save as %s before analysis.",
            "second_frame_annotation_blank.csv",
            args.annotation,
        )
        return 1

    try:
        results = analyze_second_frame_contamination(
            annotation_path=args.annotation,
            sample_path=args.sample if args.sample.exists() else None,
            n_bootstrap=args.bootstrap_replicates,
            seed=args.seed,
        )
    except ValueError as exc:
        logger.error("%s", exc)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.table_output.write_text(render_manuscript_table(results) + "\n", encoding="utf-8")
    args.paragraph_output.write_text(render_manuscript_paragraph(results) + "\n", encoding="utf-8")

    binary = results["binary_target_vs_non_target"]
    logger.info(
        "Second frame NON_TARGET: %.1f%% [%s, %s] (n=%d)",
        binary["non_target_rate_pct"],
        binary["wilson_ci_pct"][0],
        binary["wilson_ci_pct"][1],
        binary["n"],
    )
    logger.info(
        "Difference vs instruction frame: %+.1f pp",
        results["frame_comparison"]["absolute_difference_pct_points"],
    )
    logger.info("Wrote %s", args.output)
    logger.info("Wrote %s", args.table_output)
    logger.info("Wrote %s", args.paragraph_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
