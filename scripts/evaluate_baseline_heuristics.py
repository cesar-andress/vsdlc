#!/usr/bin/env python3
"""Compare decontamination adjudicated labels against trivial baseline heuristics."""

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

from vsdlc_mining.baseline_heuristics import run_baseline_comparison  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/processed/gold_sample_repos_enriched.csv"),
        help="Annotated gold sample CSV with adjudicated labels",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/baseline_comparison.json"),
        help="Baseline comparison report JSON",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if not args.input.exists():
        logger.error("Input not found: %s", args.input)
        return 1

    result = run_baseline_comparison(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for warning in result.get("warnings", []):
        logger.warning("%s", warning)

    evaluated = result.get("evaluated_repositories", 0)
    logger.info("Evaluated repositories: %d", evaluated)
    for baseline_name, metrics in result.get("baselines", {}).items():
        logger.info("%s accuracy: %s", baseline_name, metrics.get("accuracy"))
        logger.info("%s disagreements: %d", baseline_name, len(metrics.get("disagreements", [])))
    logger.info("Valuable disagreement cases: %d", len(result.get("valuable_cases", [])))
    logger.info("Wrote %s", args.output)

    if evaluated == 0:
        logger.error(
            "No adjudicated labels available. Populate adjudicated_label (or primary_label) "
            "before running baseline comparison."
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
