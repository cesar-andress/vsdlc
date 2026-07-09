#!/usr/bin/env python3
"""Compare three-way plurality consensus against human-only consensus sensitivity."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.consensus_labels import prevalence_summary  # noqa: E402
from vsdlc_mining.rq2_contamination import (  # noqa: E402
    build_family_tables,
    primary_query_from_artifacts,
    query_to_family,
    wilson_ci,
)

DEFAULT_COMPARISON = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
DEFAULT_PILOT = ROOT / "data/processed/gold_sample_360b_pilot.csv"
OUT_JSON = ROOT / "data/processed/human_only_consensus_sensitivity.json"
OUT_TEX = ROOT / "data/processed/manuscript_table_human_only_consensus.tex"


def spearman(ranks_a: dict[str, int], ranks_b: dict[str, int]) -> float | None:
    common = sorted(set(ranks_a) & set(ranks_b))
    n = len(common)
    if n < 2:
        return None
    d2 = sum((ranks_a[f] - ranks_b[f]) ** 2 for f in common)
    return round(1.0 - (6.0 * d2) / (n * (n**2 - 1)), 3)


def rank_families(table: list[dict[str, Any]], *, min_n: int = 5) -> dict[str, int]:
    eligible = [row for row in table if row["n"] >= min_n]
    ordered = sorted(
        eligible,
        key=lambda row: (-row["pct_non_target"], -row["n"], row["family"]),
    )
    return {row["family"]: index + 1 for index, row in enumerate(ordered)}


def load_rq2_rows(comparison_csv: Path, pilot_csv: Path) -> list[dict[str, str]]:
    labels_by_repo: dict[str, dict[str, str]] = {}
    with comparison_csv.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            labels_by_repo[row["repo_full_name"]] = {
                "majority_label": row["majority_label"],
                "human_only_label": row["human_only_label"],
            }

    rows: list[dict[str, str]] = []
    with pilot_csv.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            repo = row["repo_full_name"]
            if repo not in labels_by_repo:
                continue
            family = query_to_family(primary_query_from_artifacts(row.get("detected_instruction_artifacts", "")))
            rows.append(
                {
                    "repo_full_name": repo,
                    "query_family": family,
                    "majority_label": labels_by_repo[repo]["majority_label"],
                    "human_only_label": labels_by_repo[repo]["human_only_label"],
                }
            )
    return rows


def build_results(comparison_csv: Path, pilot_csv: Path) -> dict[str, Any]:
    with comparison_csv.open(encoding="utf-8", newline="") as handle:
        comparison_rows = list(csv.DictReader(handle))

    three_way = prevalence_summary(comparison_rows, "majority_label")
    human_only = prevalence_summary(comparison_rows, "human_only_label")
    human_agree_rows = [row for row in comparison_rows if row.get("human_disagreement") == "false"]
    human_agree = prevalence_summary(human_agree_rows, "human_only_label")

    three_ci = wilson_ci(three_way["non_target_count"], three_way["n"])
    human_ci = wilson_ci(human_only["non_target_count"], human_only["n"])
    human_agree_ci = wilson_ci(human_agree["non_target_count"], human_agree["n"])

    rq2_rows = load_rq2_rows(comparison_csv, pilot_csv)
    three_tables = [s.to_dict() for s in build_family_tables(rq2_rows, "query_family")]
    human_tables = [
        s.to_dict()
        for s in build_family_tables(
            [{"query_family": row["query_family"], "majority_label": row["human_only_label"]} for row in rq2_rows],
            "query_family",
        )
    ]
    three_ranks = rank_families(three_tables)
    human_ranks = rank_families(human_tables)

    return {
        "source_comparison_csv": str(comparison_csv.relative_to(ROOT)),
        "three_way_plurality": {
            **three_way,
            "wilson_ci_pct": list(three_ci),
        },
        "human_only_full_cohort": {
            **human_only,
            "wilson_ci_pct": list(human_ci),
            "unresolved_human_disagreements": human_only["tie_count"],
        },
        "human_agreement_subset": {
            **human_agree,
            "wilson_ci_pct": list(human_agree_ci),
        },
        "voting_case_counts": dict(
            Counter(
                "humans_disagree_llm_resolves"
                if row.get("human_disagreement") == "true" and row["majority_label"] != "TIE"
                else "all_three_differ"
                if row["majority_label"] == "TIE"
                else "resolved_without_llm_tiebreak"
                for row in comparison_rows
            )
        ),
        "llm_resolved_human_disagreements": sum(
            1
            for row in comparison_rows
            if row.get("human_disagreement") == "true" and row["majority_label"] != "TIE"
        ),
        "all_three_differ_ties": sum(1 for row in comparison_rows if row["majority_label"] == "TIE"),
        "rq2_family_ranking": {
            "spearman_three_way_vs_human_only": spearman(three_ranks, human_ranks),
            "families_compared": len(set(three_ranks) & set(human_ranks)),
            "three_way_ranks": three_ranks,
            "human_only_ranks": human_ranks,
            "three_way_family_table": three_tables,
            "human_only_family_table": human_tables,
        },
        "notes": [
            "Primary headline prevalence uses three-way Round-1 plurality consensus (majority_label).",
            "Human-only consensus treats 1-1 human disagreements as TIE on the full n=300 cohort.",
            "Human-agreement subset restricts to repositories where human1_label == human2_label.",
        ],
    }


def render_tex(results: dict[str, Any]) -> str:
    three = results["three_way_plurality"]
    human = results["human_only_full_cohort"]
    subset = results["human_agreement_subset"]
    ranking = results["rq2_family_ranking"]
    lines = [
        "% Auto-generated by analyze_human_only_consensus_sensitivity.py",
        "\\begin{table}[t]",
        "  \\centering",
        "  \\footnotesize",
        "  \\caption{Consensus-rule sensitivity: three-way plurality vs.\\ human-only agreement ($n{=}300$ unless noted).}",
        "  \\label{tab:human-only-consensus}",
        "  \\begin{tabular}{@{}p{0.34\\linewidth}rrrl@{}}",
        "    \\toprule",
        "    Consensus rule & $n$ & Off-target \\% & Unresolved & 95\\% CI \\\\",
        "    \\midrule",
        (
            f"    Three-way plurality (primary) & {three['n']} & {three['non_target_pct']:.1f} & "
            f"{three['tie_count']} TIE & [{three['wilson_ci_pct'][0]:.1f}, {three['wilson_ci_pct'][1]:.1f}] \\\\"
        ),
        (
            f"    Human-only (disagreements=TIE) & {human['n']} & {human['non_target_pct']:.1f} & "
            f"{human['unresolved_human_disagreements']} & [{human['wilson_ci_pct'][0]:.1f}, {human['wilson_ci_pct'][1]:.1f}] \\\\"
        ),
        (
            f"    Human-agreement subset & {subset['n']} & {subset['non_target_pct']:.1f} & "
            f"0 & [{subset['wilson_ci_pct'][0]:.1f}, {subset['wilson_ci_pct'][1]:.1f}] \\\\"
        ),
        "    \\bottomrule",
        "  \\end{tabular}",
        "\\end{table}",
        "",
        f"% RQ2 family-rank Spearman rho (three-way vs human-only): {ranking['spearman_three_way_vs_human_only']}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison", type=Path, default=DEFAULT_COMPARISON)
    parser.add_argument("--pilot", type=Path, default=DEFAULT_PILOT)
    parser.add_argument("--out-json", type=Path, default=OUT_JSON)
    parser.add_argument("--out-tex", type=Path, default=OUT_TEX)
    args = parser.parse_args()

    if not args.comparison.exists() or not args.pilot.exists():
        print("Missing input files", file=sys.stderr)
        return 1

    results = build_results(args.comparison, args.pilot)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    args.out_tex.write_text(render_tex(results), encoding="utf-8")

    print(f"Wrote {args.out_json}")
    print(f"Wrote {args.out_tex}")
    print(
        "Three-way off-target:",
        f"{results['three_way_plurality']['non_target_pct']}%",
    )
    print(
        "Human-only off-target:",
        f"{results['human_only_full_cohort']['non_target_pct']}%",
        f"(unresolved={results['human_only_full_cohort']['unresolved_human_disagreements']})",
    )
    print(
        "RQ2 family-rank Spearman rho:",
        results["rq2_family_ranking"]["spearman_three_way_vs_human_only"],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
