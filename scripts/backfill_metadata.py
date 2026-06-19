#!/usr/bin/env python3
"""Backfill missing GitHub metadata for eligible repos and gold sample CSVs."""

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

from vsdlc_mining.backfill_metadata import (  # noqa: E402
    backfill_eligible_repos,
    enrich_gold_csv_rows,
    metadata_lookup,
    read_gold_csv,
    write_output_csv,
    write_output_jsonl,
)
from vsdlc_mining.github_client import GitHubClient, GitHubRateLimitExceeded  # noqa: E402
from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.utils import read_jsonl, setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Backfill github_description, github_topics, and primary_language "
            "for eligible repositories without rerunning Phase 2 filtering."
        )
    )
    parser.add_argument(
        "--eligible-input",
        type=Path,
        default=Path("data/interim/eligible_repos.jsonl"),
        help="Eligible repositories JSONL input.",
    )
    parser.add_argument(
        "--eligible-output",
        type=Path,
        default=Path("data/interim/eligible_repos_enriched.jsonl"),
        help="Enriched eligible repositories JSONL output.",
    )
    parser.add_argument(
        "--gold-input",
        type=Path,
        default=Path("data/processed/gold_sample_repos.csv"),
        help="Gold sample CSV to enrich (optional).",
    )
    parser.add_argument(
        "--gold-output",
        type=Path,
        default=Path("data/processed/gold_sample_repos_enriched.csv"),
        help="Enriched gold sample CSV output.",
    )
    parser.add_argument(
        "--no-gold",
        action="store_true",
        help="Skip gold sample CSV enrichment.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help=(
            "Overwrite --eligible-input and --gold-input in place using atomic writes. "
            "Default outputs are separate *_enriched.* files."
        ),
    )
    parser.add_argument(
        "--exit-on-rate-limit",
        action="store_true",
        help="Exit when core quota reset wait exceeds 5 minutes instead of blocking.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=Path("data/processed/metadata_backfill_summary.json"),
        help="JSON summary of backfill counts.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("backfill_metadata")

    if not args.eligible_input.exists():
        logger.error("Eligible input not found: %s", args.eligible_input)
        return 1

    eligible_output = args.eligible_input if args.in_place else args.eligible_output
    gold_output = args.gold_input if args.in_place and not args.no_gold else args.gold_output

    if args.in_place:
        logger.warning(
            "In-place mode enabled: %s and %s will be overwritten after successful writes.",
            args.eligible_input,
            args.gold_input if not args.no_gold else "(gold skipped)",
        )

    repos = read_jsonl(args.eligible_input, EligibleRepo)
    logger.info("Loaded %d eligible repositories from %s", len(repos), args.eligible_input)

    with GitHubClient(wait_for_rate_limit=not args.exit_on_rate_limit) as client:
        try:
            enriched_repos, stats = backfill_eligible_repos(client, repos)
        except GitHubRateLimitExceeded as exc:
            logger.warning("%s", exc)
            logger.info(
                "Resume after quota reset with the same command "
                "(already-complete repos are skipped on rerun)."
            )
            return 0

    eligible_count = write_output_jsonl(
        eligible_output,
        enriched_repos,
        in_place=args.in_place,
    )
    logger.info("Wrote %d eligible repositories to %s", eligible_count, eligible_output)

    gold_rows_enriched = 0
    if not args.no_gold and args.gold_input.exists():
        gold_rows, fieldnames = read_gold_csv(args.gold_input)
        lookup = metadata_lookup(enriched_repos)
        enriched_rows = enrich_gold_csv_rows(gold_rows, lookup)
        gold_rows_enriched = write_output_csv(
            gold_output,
            enriched_rows,
            fieldnames,
            in_place=args.in_place,
        )
        logger.info("Wrote %d gold sample rows to %s", gold_rows_enriched, gold_output)
    elif not args.no_gold:
        logger.warning("Gold input not found; skipping CSV enrichment: %s", args.gold_input)

    summary = {
        "eligible_input": str(args.eligible_input),
        "eligible_output": str(eligible_output),
        "gold_input": str(args.gold_input) if not args.no_gold else None,
        "gold_output": str(gold_output) if not args.no_gold else None,
        "in_place": args.in_place,
        "total_repos": stats.total_repos,
        "skipped_complete": stats.skipped_complete,
        "api_fetches": stats.api_fetches,
        "enriched_count": stats.enriched_count,
        "failed_fetches": stats.failed_fetches,
    }
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    logger.info("Summary -> %s", args.summary_output)

    if stats.failed_fetches:
        logger.warning(
            "Metadata fetch failed for %d repositories: %s",
            len(stats.failed_fetches),
            ", ".join(stats.failed_fetches[:5])
            + (" ..." if len(stats.failed_fetches) > 5 else ""),
        )

    logger.info(
        "Backfill complete: %d API fetches, %d enriched, %d failed, %d already complete",
        stats.api_fetches,
        stats.enriched_count,
        len(stats.failed_fetches),
        stats.skipped_complete,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
