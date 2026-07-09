#!/usr/bin/env python3
"""Regenerate three-coder comparison labels from raw Round-1 annotation files."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.consensus_labels import (  # noqa: E402
    classify_voting_case,
    compute_human_only_label,
    compute_majority_label,
    human_disagreement,
    normalize_label,
    prevalence_summary,
)
from vsdlc_mining.rq2_contamination import wilson_ci  # noqa: E402

DEFAULT_HUMAN1 = ROOT / "data/processed/gold_sample_330_human1.csv"
DEFAULT_HUMAN2 = ROOT / "data/processed/gold_sample_330_human2.csv"
DEFAULT_CLAUDE = ROOT / "data/processed/gold_sample_330_claude.csv"
DEFAULT_EXISTING = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
DEFAULT_OUTPUT = DEFAULT_EXISTING

OUTPUT_FIELDS = [
    "repo_full_name",
    "claude_label",
    "human1_label",
    "human2_label",
    "majority_label",
    "human_only_label",
    "human_disagreement",
]


def _read_labels(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keyed: dict[str, str] = {}
    for row in rows:
        repo = (row.get("repo_full_name") or "").strip()
        if not repo:
            continue
        keyed[repo] = normalize_label(row.get("primary_label") or row.get("label") or "")
    return keyed


def build_comparison_rows(
    human1: dict[str, str],
    human2: dict[str, str],
    claude: dict[str, str],
) -> list[dict[str, str]]:
    repos = sorted(set(human1) & set(human2) & set(claude))
    rows: list[dict[str, str]] = []
    for repo in repos:
        h1 = human1[repo]
        h2 = human2[repo]
        cl = claude[repo]
        rows.append(
            {
                "repo_full_name": repo,
                "claude_label": cl,
                "human1_label": h1,
                "human2_label": h2,
                "majority_label": compute_majority_label(cl, h1, h2),
                "human_only_label": compute_human_only_label(h1, h2),
                "human_disagreement": "true" if human_disagreement(h1, h2) else "false",
            }
        )
    return rows


def validate_against_existing(
    regenerated: list[dict[str, str]],
    existing_path: Path,
) -> list[str]:
    mismatches: list[str] = []
    with existing_path.open(encoding="utf-8", newline="") as handle:
        existing = {row["repo_full_name"]: row for row in csv.DictReader(handle)}
    for row in regenerated:
        repo = row["repo_full_name"]
        if repo not in existing:
            mismatches.append(f"{repo}: missing from existing comparison CSV")
            continue
        expected = normalize_label(existing[repo].get("majority_label", ""))
        actual = normalize_label(row["majority_label"])
        if expected != actual:
            mismatches.append(
                f"{repo}: expected majority_label={expected!r}, got {actual!r}"
            )
    if len(existing) != len(regenerated):
        mismatches.append(
            f"row count mismatch: existing={len(existing)} regenerated={len(regenerated)}"
        )
    return mismatches


def print_summary(rows: list[dict[str, str]]) -> None:
    case_counts = Counter(
        classify_voting_case(row["claude_label"], row["human1_label"], row["human2_label"])
        for row in rows
    )
    three_way = prevalence_summary(rows, "majority_label")
    human_only = prevalence_summary(rows, "human_only_label")
    three_ci = wilson_ci(three_way["non_target_count"], three_way["n"])
    human_ci = wilson_ci(human_only["non_target_count"], human_only["n"])

    human_agree_rows = [row for row in rows if row["human_disagreement"] == "false"]
    human_agree = prevalence_summary(human_agree_rows, "human_only_label")
    human_agree_ci = wilson_ci(human_agree["non_target_count"], human_agree["n"])

    print("Consensus label summary")
    print(f"  repositories: {len(rows)}")
    print(f"  all three agree: {case_counts['all_agree_or_humans_agree_llm_agrees']}")
    print(f"  humans agree, LLM dissents: {case_counts['humans_agree_llm_dissents']}")
    print(f"  humans disagree, LLM resolves: {case_counts['humans_disagree_llm_resolves']}")
    print(f"  all three labels differ (TIE): {case_counts['all_three_differ']}")
    print(
        "  three-way off-target prevalence: "
        f"{three_way['non_target_pct']}% "
        f"({three_way['non_target_count']}/{three_way['n']}); "
        f"Wilson 95% CI [{three_ci[0]:.1f}, {three_ci[1]:.1f}]"
    )
    print(
        "  human-only off-target prevalence (disagreements=TIE): "
        f"{human_only['non_target_pct']}% "
        f"({human_only['non_target_count']}/{human_only['n']}); "
        f"unresolved={human_only['tie_count']}; "
        f"Wilson 95% CI [{human_ci[0]:.1f}, {human_ci[1]:.1f}]"
    )
    print(
        "  human-agreement subset off-target prevalence: "
        f"{human_agree['non_target_pct']}% "
        f"({human_agree['non_target_count']}/{human_agree['n']}); "
        f"Wilson 95% CI [{human_agree_ci[0]:.1f}, {human_agree_ci[1]:.1f}]"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--human1", type=Path, default=DEFAULT_HUMAN1)
    parser.add_argument("--human2", type=Path, default=DEFAULT_HUMAN2)
    parser.add_argument("--claude", type=Path, default=DEFAULT_CLAUDE)
    parser.add_argument("--existing", type=Path, default=DEFAULT_EXISTING)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    for path in (args.human1, args.human2, args.claude, args.existing):
        if not path.exists():
            print(f"Missing input: {path}", file=sys.stderr)
            return 1

    human1 = _read_labels(args.human1)
    human2 = _read_labels(args.human2)
    claude = _read_labels(args.claude)
    rows = build_comparison_rows(human1, human2, claude)

    mismatches = validate_against_existing(rows, args.existing)
    if mismatches:
        print("Validation failed:", file=sys.stderr)
        for item in mismatches[:20]:
            print(f"  {item}", file=sys.stderr)
        if len(mismatches) > 20:
            print(f"  ... and {len(mismatches) - 20} more", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {args.output} ({len(rows)} rows)")
    print("Validation: regenerated majority_label matches existing frozen column for all repositories")
    print_summary(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
