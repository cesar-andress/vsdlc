#!/usr/bin/env python3
"""Compute inter-annotator agreement for decontamination labels."""

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

from vsdlc_mining.annotation_agreement import compute_annotation_agreement  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annotator-a",
        type=Path,
        required=True,
        help="Annotation CSV from annotator A",
    )
    parser.add_argument(
        "--annotator-b",
        type=Path,
        required=True,
        help="Annotation CSV from annotator B",
    )
    parser.add_argument(
        "--adjudicated",
        type=Path,
        default=None,
        help="Optional adjudicated CSV for per-class precision/recall",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/annotation_agreement.json"),
        help="Agreement metrics JSON output",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.annotator_a, args.annotator_b):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    result = compute_annotation_agreement(
        args.annotator_a,
        args.annotator_b,
        adjudicated_path=args.adjudicated,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for message in result.get("compatibility_warnings", []):
        logger.warning("Compatibility: %s", message)

    primary_kappa = result["primary_three_class"]["kappa"]
    binary_kappa = result["binary_decontamination"]["kappa"]
    logger.info("Paired repositories: %d", result["paired_repositories"])
    logger.info("Primary three-class Cohen's kappa: %s", primary_kappa)
    logger.info("Binary decontamination Cohen's kappa: %s", binary_kappa)
    logger.info("Disagreements: %d", len(result["disagreements"]))
    logger.info("Wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
