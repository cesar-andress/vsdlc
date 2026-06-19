#!/usr/bin/env python3
"""RQ2: cross-tab primary query family vs majority_label (n=300 intersection)."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT_360B = ROOT / "data/processed/gold_sample_360b_pilot.csv"
COMPARISON_330 = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
OUT_JSON = ROOT / "data/processed/rq2_query_family_stats.json"

NON_TARGET_LABELS = frozenset({"AI_PRODUCT", "EXCLUDE"})


def query_to_family(primary_query: str) -> str:
    q = (primary_query or "").strip()
    if q == "AGENTS.md":
        return "AGENTS.md"
    if q in {"CLAUDE.md", "GEMINI.md"}:
        return "CLAUDE/GEMINI"
    if q in {".cursorrules", ".cursor/rules"}:
        return "Cursor rules"
    if q in {"copilot-instructions.md", ".github/copilot-instructions.md"}:
        return "Copilot instructions"
    if q in {".windsurfrules", ".clinerules"}:
        return "Editor rules"
    if q.startswith(".aider") or q in {".aider.conf.yml", ".aiderignore", ".aider.model.settings.yml"}:
        return "Aider"
    if q in {"prompts/", "*.prompt.md"}:
        return "Prompt paths"
    if q in {"system_prompt.*", "system-prompt.*"}:
        return "System prompts"
    if q == ".github/chatmodes":
        return "Chat modes"
    return "Other"


def primary_query_from_artifacts(raw: str) -> str:
    if not raw:
        return ""
    data = json.loads(raw)
    queries = data.get("queries") or []
    return str(queries[0]) if queries else ""


def primary_path_from_artifacts(raw: str) -> str:
    if not raw:
        return ""
    data = json.loads(raw)
    paths = data.get("matched_paths") or []
    return str(paths[0]) if paths else ""


def path_to_family(path: str) -> str:
    p = (path or "").strip()
    if not p:
        return "other"
    lower = p.lower()
    name = lower.rsplit("/", 1)[-1]

    if name == "agents.md" or lower.endswith("/agents.md"):
        return "AGENTS.md"
    if name in {"claude.md", "gemini.md"} or "/claude.md" in lower or "/gemini.md" in lower:
        return "CLAUDE/GEMINI"
    if ".cursor/rules" in lower or name.endswith(".cursorrules") or lower.endswith(".cursorrules"):
        return "cursor rules"
    if "copilot-instructions" in lower:
        return "copilot instructions"
    if ".windsurfrules" in lower or ".clinerules" in lower:
        return "editor rules"
    if ".aider" in lower or "aiderignore" in lower or "aider.conf" in lower:
        return "aider"
    if "chatmodes" in lower or "chatmode" in lower:
        return "chatmodes"
    if "system-prompt" in lower or "system_prompt" in lower or "system prompt" in lower:
        return "system-prompt"
    if "/prompts/" in lower or lower.startswith("prompts/") or name.endswith(".prompt.md"):
        return "prompts"
    return "other"


def pct(numerator: int, denominator: int) -> float:
    return round(100.0 * numerator / denominator, 1) if denominator else 0.0


def main() -> None:
    majority_by_repo: dict[str, str] = {}
    with COMPARISON_330.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            majority_by_repo[row["repo_full_name"]] = row["majority_label"]

    rows: list[tuple[str, str, str, str]] = []
    with PILOT_360B.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            repo = row["repo_full_name"]
            if repo not in majority_by_repo:
                continue
            artifacts = row.get("detected_instruction_artifacts", "")
            pq = primary_query_from_artifacts(artifacts)
            family = query_to_family(pq)
            path_family = path_to_family(primary_path_from_artifacts(artifacts))
            label = majority_by_repo[repo]
            rows.append((repo, family, path_family, label))

    n = len(rows)
    assert n == 300, f"expected n=300 intersection, got n={n}"

    by_family: dict[str, Counter[str]] = defaultdict(Counter)
    by_path_family: dict[str, Counter[str]] = defaultdict(Counter)
    family_counts: Counter[str] = Counter()
    path_family_counts: Counter[str] = Counter()
    for _repo, family, path_family, label in rows:
        by_family[family][label] += 1
        by_path_family[path_family][label] += 1
        family_counts[family] += 1
        path_family_counts[path_family] += 1

    top_families = [f for f, _ in family_counts.most_common()]
    display_families = top_families[:6]

    table_rows: list[dict] = []
    for family in display_families:
        counts = by_family[family]
        fn = family_counts[family]
        non_target = sum(counts[l] for l in NON_TARGET_LABELS)
        exclude = counts["EXCLUDE"]
        conventional = counts["CONVENTIONAL_SOFTWARE"]
        ai_product = counts["AI_PRODUCT"]
        table_rows.append(
            {
                "family": family,
                "n": fn,
                "pct_conventional": pct(conventional, fn),
                "pct_ai_product": pct(ai_product, fn),
                "pct_non_target": pct(non_target, fn),
                "pct_exclude": pct(exclude, fn),
                "counts": dict(counts),
            }
        )

    cross_tab = {
        family: dict(by_family[family]) for family in sorted(by_family, key=lambda f: -family_counts[f])
    }
    cross_tab_path = {
        family: dict(by_path_family[family])
        for family in sorted(by_path_family, key=lambda f: -path_family_counts[f])
    }

    payload = {
        "n_intersection": n,
        "sources": {
            "queries_csv": str(PILOT_360B.relative_to(ROOT)),
            "majority_csv": str(COMPARISON_330.relative_to(ROOT)),
        },
        "definitions": {
            "primary_query": "first element of detected_instruction_artifacts.queries",
            "primary_matched_path": "first element of detected_instruction_artifacts.matched_paths",
            "pct_conventional": "100 * CONVENTIONAL_SOFTWARE / n_family",
            "pct_ai_product": "100 * AI_PRODUCT / n_family",
            "pct_non_target": "100 * (AI_PRODUCT + EXCLUDE) / n_family",
            "pct_exclude": "100 * EXCLUDE / n_family",
        },
        "family_totals": dict(family_counts),
        "path_family_totals": dict(path_family_counts),
        "cross_tab_majority_by_family": cross_tab,
        "cross_tab_majority_by_matched_path_family": cross_tab_path,
        "table_top_families": table_rows,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"n={n}")
    print()
    print("| Query family | n | % CONV | % AI_PROD | % NON_TARGET | % EXCLUDE |")
    print("|---|---:|---:|---:|---:|---:|")
    for row in table_rows:
        print(
            f"| {row['family']} | {row['n']} | {row['pct_conventional']:.1f} | "
            f"{row['pct_ai_product']:.1f} | {row['pct_non_target']:.1f} | {row['pct_exclude']:.1f} |"
        )


if __name__ == "__main__":
    main()
