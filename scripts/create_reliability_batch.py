#!/usr/bin/env python3
"""Create a balanced reliability annotation batch for inter-rater agreement."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.reliability_batch import (  # noqa: E402
    DEFAULT_RELIABILITY_BATCH_SIZE,
    DEFAULT_RELIABILITY_SEED,
    artifact_type_distribution,
    balanced_stratified_sample,
    star_bucket_distribution,
    write_reliability_batch_csv,
)
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
        default=Path("data/processed/reliability_batch_50.csv"),
        help="Reliability annotation batch CSV",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=DEFAULT_RELIABILITY_BATCH_SIZE,
        help="Target batch size (all repos used if fewer are eligible)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_RELIABILITY_SEED,
        help="Random seed for reproducible balanced sampling",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if not args.input.exists():
        raise SystemExit(f"Input not found: {args.input}")

    if args.sample_size < 1:
        raise SystemExit("--sample-size must be >= 1")

    eligible = read_jsonl(args.input, EligibleRepo)
    logger.info("Loaded %d eligible repositories from %s", len(eligible), args.input)

    sample = balanced_stratified_sample(eligible, sample_size=args.sample_size, seed=args.seed)
    count = write_reliability_batch_csv(args.output, sample)
    logger.info("Wrote %d repositories to %s", count, args.output)
    logger.info("Star bucket distribution: %s", star_bucket_distribution(sample))
    logger.info("Artifact type distribution: %s", artifact_type_distribution(sample))

    missing_description = sum(1 for repo in sample if not repo.github_description)
    missing_topics = sum(1 for repo in sample if not repo.github_topics)
    missing_language = sum(1 for repo in sample if not repo.primary_language)
    if missing_description or missing_topics or missing_language:
        logger.warning(
            "Missing metadata in batch — description: %d, topics: %d, language: %d "
            "(run scripts/backfill_metadata.py; values are not fabricated)",
            missing_description,
            missing_topics,
            missing_language,
        )


if __name__ == "__main__":
    main()
