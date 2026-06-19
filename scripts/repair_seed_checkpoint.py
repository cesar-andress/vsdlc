#!/usr/bin/env python3
"""Repair a truncated seed-search checkpoint and sync enriched repos from JSONL."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.config import REPO_CANDIDATES_PATH, SEED_SEARCH_CHECKPOINT_PATH  # noqa: E402
from vsdlc_mining.seed_search import repair_checkpoint  # noqa: E402
from vsdlc_mining.utils import read_json, setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Salvage and rewrite seed-search checkpoint from JSONL progress.",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=SEED_SEARCH_CHECKPOINT_PATH,
        help="Checkpoint file to repair.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_CANDIDATES_PATH,
        help="JSONL file used as source of truth for enriched repositories.",
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
    logger = logging.getLogger("repair_seed_checkpoint")

    if not args.checkpoint.exists():
        logger.error("Checkpoint not found: %s", args.checkpoint)
        return 1

    repair_checkpoint(args.checkpoint, output_path=args.output)
    payload = read_json(args.checkpoint)
    aggregate = len(payload.get("aggregate", {}))
    enriched = len(payload.get("enriched_full_names", []))
    logger.info(
        "Checkpoint OK: %d/%d enriched (%.1f%%), faltan %d",
        enriched,
        aggregate,
        100 * enriched / aggregate if aggregate else 0,
        aggregate - enriched,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
