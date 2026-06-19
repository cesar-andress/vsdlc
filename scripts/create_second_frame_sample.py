#!/usr/bin/env python3
"""Sample second-frame eligible repositories and create annotation worksheets."""

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
    ELIGIBLE_REPOS_PATH,
    SECOND_FRAME_ANNOTATION_BLANK_PATH,
    SECOND_FRAME_ELIGIBLE_PATH,
    SECOND_FRAME_SAMPLE_PATH,
    SECOND_FRAME_SAMPLE_SEED,
    SECOND_FRAME_SAMPLE_SIZE,
)
from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.second_frame_sample import (  # noqa: E402
    SECOND_FRAME_ANNOTATION_FIELDS,
    SECOND_FRAME_SAMPLE_FIELDS,
    eligible_to_annotation_blank_row,
    eligible_to_second_frame_row,
    sample_second_frame_repositories,
    write_second_frame_csv,
)
from vsdlc_mining.utils import read_jsonl, setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eligible", type=Path, default=SECOND_FRAME_ELIGIBLE_PATH)
    parser.add_argument(
        "--instruction-frame-eligible",
        type=Path,
        default=ELIGIBLE_REPOS_PATH,
        help="Instruction-artifact eligible set used for overlap marking.",
    )
    parser.add_argument("--sample-output", type=Path, default=SECOND_FRAME_SAMPLE_PATH)
    parser.add_argument("--blank-output", type=Path, default=SECOND_FRAME_ANNOTATION_BLANK_PATH)
    parser.add_argument("--sample-size", type=int, default=SECOND_FRAME_SAMPLE_SIZE)
    parser.add_argument("--seed", type=int, default=SECOND_FRAME_SAMPLE_SEED)
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=SECOND_FRAME_SAMPLE_PATH.with_suffix(".summary.json"),
    )
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("create_second_frame_sample")

    if not args.eligible.exists():
        logger.error("Second-frame eligible file not found: %s", args.eligible)
        return 1

    eligible = read_jsonl(args.eligible, EligibleRepo)
    instruction_names: set[str] = set()
    if args.instruction_frame_eligible.exists():
        instruction_names = {
            repo.full_name for repo in read_jsonl(args.instruction_frame_eligible, EligibleRepo)
        }
        logger.info(
            "Loaded %d instruction-frame eligible repositories for overlap marking.",
            len(instruction_names),
        )
    else:
        logger.warning(
            "Instruction-frame eligible file missing at %s; overlap will be marked false.",
            args.instruction_frame_eligible,
        )

    selected, summary = sample_second_frame_repositories(
        eligible,
        instruction_frame_names=instruction_names,
        sample_size=args.sample_size,
        seed=args.seed,
    )

    sample_rows = [
        eligible_to_second_frame_row(
            repo,
            instruction_frame_overlap=repo.full_name in instruction_names,
            sample_seed=args.seed,
        )
        for repo in selected
    ]
    blank_rows = [eligible_to_annotation_blank_row(repo) for repo in selected]

    sample_count = write_second_frame_csv(args.sample_output, sample_rows, SECOND_FRAME_SAMPLE_FIELDS)
    blank_count = write_second_frame_csv(args.blank_output, blank_rows, SECOND_FRAME_ANNOTATION_FIELDS)

    summary["sample_output"] = str(args.sample_output)
    summary["blank_output"] = str(args.blank_output)
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    logger.info("Wrote %d repositories to %s", sample_count, args.sample_output)
    logger.info("Wrote %d repositories to %s", blank_count, args.blank_output)
    logger.info(
        "Overlap in sample: %d/%d",
        summary["overlap_in_sample"],
        summary["selected_sample_size"],
    )
    if summary["used_all_eligible"]:
        logger.warning(
            "Only %d eligible repositories available (requested %d).",
            summary["selected_sample_size"],
            args.sample_size,
        )
    logger.info("Summary -> %s", args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
