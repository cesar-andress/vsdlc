"""Round-1 label consensus helpers for three-coder plurality and human-only rules."""

from __future__ import annotations

from collections import Counter
from typing import Any

PRIMARY_LABELS = frozenset({"CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE"})
NON_TARGET_LABELS = frozenset({"AI_PRODUCT", "EXCLUDE"})


def normalize_label(label: str) -> str:
    return (label or "").strip().upper()


def compute_majority_label(claude: str, human1: str, human2: str) -> str:
    votes = [normalize_label(claude), normalize_label(human1), normalize_label(human2)]
    counts = Counter(votes)
    top_label, top_count = counts.most_common(1)[0]
    if top_count >= 2:
        return top_label
    return "TIE"


def compute_human_only_label(human1: str, human2: str) -> str:
    left = normalize_label(human1)
    right = normalize_label(human2)
    if left == right:
        return left
    return "TIE"


def human_disagreement(human1: str, human2: str) -> bool:
    return normalize_label(human1) != normalize_label(human2)


def classify_voting_case(claude: str, human1: str, human2: str) -> str:
    c, h1, h2 = normalize_label(claude), normalize_label(human1), normalize_label(human2)
    if h1 == h2:
        if c == h1:
            return "all_agree_or_humans_agree_llm_agrees"
        return "humans_agree_llm_dissents"
    majority = compute_majority_label(claude, human1, human2)
    if majority == "TIE":
        return "all_three_differ"
    return "humans_disagree_llm_resolves"


def binary_off_target(label: str) -> bool:
    return normalize_label(label) in NON_TARGET_LABELS


def prevalence_summary(rows: list[dict[str, str]], label_field: str) -> dict[str, Any]:
    counts = Counter(normalize_label(row[label_field]) for row in rows)
    n = len(rows)
    target = counts.get("CONVENTIONAL_SOFTWARE", 0)
    non_target = counts.get("AI_PRODUCT", 0) + counts.get("EXCLUDE", 0)
    tie = counts.get("TIE", 0)
    return {
        "n": n,
        "label_field": label_field,
        "conventional_count": target,
        "ai_product_count": counts.get("AI_PRODUCT", 0),
        "exclude_count": counts.get("EXCLUDE", 0),
        "non_target_count": non_target,
        "tie_count": tie,
        "target_pct": round(100.0 * target / n, 1) if n else 0.0,
        "non_target_pct": round(100.0 * non_target / n, 1) if n else 0.0,
        "tie_pct": round(100.0 * tie / n, 1) if n else 0.0,
        "unresolved_human_disagreements": tie if label_field == "human_only_label" else 0,
    }
