#!/usr/bin/env python3
"""Create a stratified gold sample for decontamination annotation."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.gold_sample import DEFAULT_SAMPLE_SIZE, stratified_sample, write_gold_sample_csv  # noqa: E402
from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.utils import read_jsonl  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/interim/eligible_repos.jsonl"),
        help="Eligible repositories JSONL from Phase 2",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/gold_sample_repos.csv"),
        help="Gold sample CSV for manual annotation",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=DEFAULT_SAMPLE_SIZE,
        help="Target sample size (all repos used if fewer are eligible)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducible stratified sampling",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if not args.input.exists():
        raise SystemExit(f"Input not found: {args.input}")

    eligible = read_jsonl(args.input, EligibleRepo)
    logger.info("Loaded %d eligible repositories from %s", len(eligible), args.input)

    sample = stratified_sample(eligible, sample_size=args.sample_size, seed=args.seed)
    count = write_gold_sample_csv(args.output, sample)
    logger.info("Wrote %d repositories to %s", count, args.output)

    missing_description = sum(1 for repo in sample if not repo.github_description)
    missing_topics = sum(1 for repo in sample if not repo.github_topics)
    missing_language = sum(1 for repo in sample if not repo.primary_language)
    if missing_description or missing_topics or missing_language:
        logger.warning(
            "Missing metadata in sample — description: %d, topics: %d, language: %d "
            "(re-run Phase 1/2 enrichment; values are not fabricated)",
            missing_description,
            missing_topics,
            missing_language,
        )


if __name__ == "__main__":
    main()
