#!/usr/bin/env python3
"""Target-sensitivity analysis for RQ1 using frozen consensus labels only."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.rq2_contamination import wilson_ci  # noqa: E402

DEFAULT_INPUT = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
OUT_JSON = ROOT / "data/processed/target_sensitivity_results.json"
OUT_TEX = ROOT / "data/processed/manuscript_table_target_sensitivity.tex"

PRIMARY_LABELS = frozenset({"CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE", "TIE"})


def load_consensus_rows(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            label = (row.get("majority_label") or "").strip()
            if label not in PRIMARY_LABELS:
                raise ValueError(f"Unexpected majority_label: {label!r}")
            rows.append({"repo_full_name": row["repo_full_name"], "majority_label": label})
    return rows


def binary_scenario(
    rows: list[dict[str, str]],
    *,
    key: str,
    target_reading: str,
    on_target_definition: str,
    target_labels: frozenset[str],
    non_target_labels: frozenset[str],
) -> dict[str, Any]:
    counts = {label: 0 for label in PRIMARY_LABELS}
    for row in rows:
        counts[row["majority_label"]] += 1

    n = len(rows)
    target_count = sum(counts[label] for label in target_labels)
    non_target_count = sum(counts[label] for label in non_target_labels)
    tie_count = counts["TIE"]

    off_target_pct = round(100.0 * non_target_count / n, 1) if n else 0.0
    target_pct = round(100.0 * target_count / n, 1) if n else 0.0
    ci_low, ci_high = wilson_ci(non_target_count, n)

    return {
        "key": key,
        "target_reading": target_reading,
        "on_target_definition": on_target_definition,
        "target_labels": sorted(target_labels),
        "non_target_labels": sorted(non_target_labels),
        "n": n,
        "target_count": target_count,
        "target_pct": target_pct,
        "non_target_count": non_target_count,
        "non_target_pct": off_target_pct,
        "wilson_ci_pct": [ci_low, ci_high],
        "tie_count": tie_count,
    }


def product_role_scenario(rows: list[dict[str, str]]) -> dict[str, Any]:
    product_rows = [row for row in rows if row["majority_label"] != "EXCLUDE"]
    n = len(product_rows)
    conv_count = sum(1 for row in product_rows if row["majority_label"] == "CONVENTIONAL_SOFTWARE")
    ai_count = sum(1 for row in product_rows if row["majority_label"] == "AI_PRODUCT")
    tie_count = sum(1 for row in product_rows if row["majority_label"] == "TIE")

    conv_pct = round(100.0 * conv_count / n, 1) if n else 0.0
    ai_pct = round(100.0 * ai_count / n, 1) if n else 0.0
    conv_ci = list(wilson_ci(conv_count, n))
    ai_ci = list(wilson_ci(ai_count, n))

    return {
        "key": "product_role_contrast",
        "target_reading": "Product-role contrast, excluding EXCLUDE",
        "on_target_definition": "CONVENTIONAL_SOFTWARE vs. AI_PRODUCT (EXCLUDE omitted)",
        "n_total_consensus": len(rows),
        "n": n,
        "exclude_omitted_count": len(rows) - n,
        "conventional_count": conv_count,
        "conventional_pct": conv_pct,
        "conventional_wilson_ci_pct": conv_ci,
        "ai_product_count": ai_count,
        "ai_product_pct": ai_pct,
        "ai_product_wilson_ci_pct": ai_ci,
        "tie_count": tie_count,
        "off_target_pct": ai_pct,
        "wilson_ci_pct": ai_ci,
    }


def build_results(rows: list[dict[str, str]]) -> dict[str, Any]:
    scenarios = [
        binary_scenario(
            rows,
            key="conventional_application_software",
            target_reading="Conventional application software",
            on_target_definition="CONVENTIONAL_SOFTWARE",
            target_labels=frozenset({"CONVENTIONAL_SOFTWARE"}),
            non_target_labels=frozenset({"AI_PRODUCT", "EXCLUDE"}),
        ),
        binary_scenario(
            rows,
            key="any_software_product",
            target_reading="Any software product",
            on_target_definition="CONVENTIONAL_SOFTWARE + AI_PRODUCT",
            target_labels=frozenset({"CONVENTIONAL_SOFTWARE", "AI_PRODUCT"}),
            non_target_labels=frozenset({"EXCLUDE"}),
        ),
        binary_scenario(
            rows,
            key="ai_builder_tooling",
            target_reading="AI-builder tooling",
            on_target_definition="AI_PRODUCT",
            target_labels=frozenset({"AI_PRODUCT"}),
            non_target_labels=frozenset({"CONVENTIONAL_SOFTWARE", "EXCLUDE"}),
        ),
    ]
    product_role = product_role_scenario(rows)
    return {
        "source": str(DEFAULT_INPUT.name),
        "consensus_n": len(rows),
        "label_counts": {
            label: sum(1 for row in rows if row["majority_label"] == label)
            for label in sorted(PRIMARY_LABELS)
        },
        "scenarios": scenarios + [product_role],
        "notes": [
            "Uses frozen annotation consensus (majority_label) only; no relabeling.",
            "Binary scenarios keep n=300 and leave TIE rows in the denominator but unassigned.",
            "Product-role contrast excludes EXCLUDE rows before comparing CONVENTIONAL_SOFTWARE vs AI_PRODUCT.",
        ],
    }


def render_tex(results: dict[str, Any]) -> str:
    rows: list[str] = [
        "% Auto-generated by analyze_target_sensitivity.py",
        "\\begin{table}[t]",
        "  \\centering",
        "  \\footnotesize",
        "  \\caption{Target-sensitivity of off-target prevalence under alternative consensus-label collapses ($n{=}300$ unless noted).}",
        "  \\label{tab:target-sensitivity}",
        "  \\begin{tabular}{@{}p{0.22\\linewidth}p{0.30\\linewidth}rrl@{}}",
        "    \\toprule",
        "    Target reading & On-target definition & $n$ & Off-target \\% & 95\\% CI \\\\",
        "    \\midrule",
    ]

    for scenario in results["scenarios"]:
        if scenario["key"] == "product_role_contrast":
            on_target = "\\catconv{} vs.\\ \\cataip{} (\\catexcl{} omitted)"
            n = scenario["n"]
            off_pct = scenario["ai_product_pct"]
            ci = scenario["ai_product_wilson_ci_pct"]
            reading = "Product-role contrast"
        elif scenario["key"] == "conventional_application_software":
            on_target = "\\catconv{}"
            n = scenario["n"]
            off_pct = scenario["non_target_pct"]
            ci = scenario["wilson_ci_pct"]
            reading = "Conventional application software"
        elif scenario["key"] == "any_software_product":
            on_target = "\\catconv{} + \\cataip{}"
            n = scenario["n"]
            off_pct = scenario["non_target_pct"]
            ci = scenario["wilson_ci_pct"]
            reading = "Any software product"
        elif scenario["key"] == "ai_builder_tooling":
            on_target = "\\cataip{}"
            n = scenario["n"]
            off_pct = scenario["non_target_pct"]
            ci = scenario["wilson_ci_pct"]
            reading = "AI-builder tooling"
        else:
            raise ValueError(scenario["key"])

        rows.append(
            f"    {reading} & {on_target} & {n} & {off_pct:.1f} & [{ci[0]:.1f}, {ci[1]:.1f}] \\\\"
        )

    rows.extend(
        [
            "    \\bottomrule",
            "  \\end{tabular}",
            "\\end{table}",
        ]
    )
    return "\n".join(rows) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-json", type=Path, default=OUT_JSON)
    parser.add_argument("--out-tex", type=Path, default=OUT_TEX)
    args = parser.parse_args()

    rows = load_consensus_rows(args.input)
    results = build_results(rows)

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    args.out_tex.write_text(render_tex(results), encoding="utf-8")

    print(f"Wrote {args.out_json}")
    print(f"Wrote {args.out_tex}")
    for scenario in results["scenarios"]:
        if scenario["key"] == "product_role_contrast":
            print(
                f"{scenario['target_reading']}: n={scenario['n']}, "
                f"AI_PRODUCT={scenario['ai_product_pct']}% "
                f"[{scenario['ai_product_wilson_ci_pct'][0]}, {scenario['ai_product_wilson_ci_pct'][1]}]"
            )
        else:
            print(
                f"{scenario['target_reading']}: n={scenario['n']}, "
                f"off-target={scenario['non_target_pct']}% "
                f"[{scenario['wilson_ci_pct'][0]}, {scenario['wilson_ci_pct'][1]}]"
            )


if __name__ == "__main__":
    main()
