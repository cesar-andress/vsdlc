"""RQ2 contamination-structure helpers: family mapping and rate tables."""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any

PRIMARY_LABELS = frozenset(
    {"CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE", "TIE"}
)
NON_TARGET_LABELS = frozenset({"AI_PRODUCT", "EXCLUDE"})
RATE_LABELS = frozenset({"CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE"})


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
        return "Editor rule files"
    if q.startswith(".aider") or q in {
        ".aider.conf.yml",
        ".aiderignore",
        ".aider.model.settings.yml",
    }:
        return "Aider config"
    if q in {"prompts/", "*.prompt.md"}:
        return "Prompt paths"
    if q in {"system_prompt.*", "system-prompt.*"}:
        return "System prompts"
    if q == ".github/chatmodes":
        return "Chat modes"
    return "Other"


def matched_path_to_family(path: str) -> str:
    p = (path or "").strip()
    if not p:
        return "unknown/other"
    lower = p.lower()
    name = lower.rsplit("/", 1)[-1]
    depth = lower.count("/")

    if "chatmodes" in lower or "chatmode" in lower:
        return ".github/chatmodes"
    if ".cursor/rules" in lower:
        return ".cursor/rules"
    if (
        depth == 0
        or name
        in {
            "agents.md",
            "claude.md",
            "gemini.md",
            ".cursorrules",
            "copilot-instructions.md",
            ".windsurfrules",
            ".clinerules",
        }
        or lower.endswith("/agents.md")
        and depth <= 1
    ):
        if name in {"agents.md", "claude.md", "gemini.md", ".cursorrules"} or (
            "copilot-instructions" in name and depth <= 1
        ):
            return "root instruction file"
    if name in {"agents.md", "claude.md", "gemini.md"} and depth <= 2:
        return "root instruction file"
    if "copilot-instructions" in lower and depth <= 1:
        return "root instruction file"
    if "/prompts/" in lower or lower.startswith("prompts/") or name.endswith(".prompt.md"):
        return "prompts directory"
    if (
        "system-prompt" in lower
        or "system_prompt" in lower
        or "system prompt" in lower
    ):
        return "system prompt source"
    if any(token in lower for token in ("/docs/", "/doc/", "/wiki/", "landingpage/")):
        return "docs/wiki"
    if any(
        token in lower
        for token in (
            "/src/",
            "/app/",
            "/lib/",
            "/pkg/",
            "/internal/",
            "/server/",
            "/client/",
            "/packages/",
        )
    ):
        return "package/application source"
    if depth == 0:
        return "root instruction file"
    return "unknown/other"


def metadata_sparsity(description: str, topics: str) -> str:
    desc = (description or "").strip()
    top = (topics or "").strip()
    if not desc and not top:
        return "missing_description_and_topics"
    if not desc:
        return "missing_description"
    if not top:
        return "missing_topics"
    return "complete_metadata"


def primary_language_group(language: str) -> str:
    lang = (language or "").strip()
    if not lang:
        return "Docs/Markdown"
    lower = lang.lower()
    if lower == "python":
        return "Python"
    if lower in {"typescript", "javascript", "vue", "svelte"}:
        return "TypeScript/JavaScript"
    if lower in {"rust", "go"}:
        return "Rust/Go"
    if lower in {"markdown", "html", "css"}:
        return "Docs/Markdown"
    return "Other"


def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n <= 0:
        return (0.0, 0.0)
    p = successes / n
    z2 = z * z
    denom = 1.0 + z2 / n
    center = (p + z2 / (2.0 * n)) / denom
    margin = z * math.sqrt((p * (1.0 - p) / n) + (z2 / (4.0 * n * n))) / denom
    return (round(100.0 * max(0.0, center - margin), 1), round(100.0 * min(1.0, center + margin), 1))


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


def pct(numerator: int, denominator: int) -> float:
    return round(100.0 * numerator / denominator, 1) if denominator else 0.0


@dataclass
class FamilyStats:
    family: str
    n: int
    tie_count: int
    conventional: int
    ai_product: int
    exclude: int
    non_target: int
    pct_conventional: float
    pct_ai_product: float
    pct_exclude: float
    pct_non_target: float
    non_target_ci_low: float
    non_target_ci_high: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "family": self.family,
            "n": self.n,
            "tie_count": self.tie_count,
            "conventional_count": self.conventional,
            "ai_product_count": self.ai_product,
            "exclude_count": self.exclude,
            "non_target_count": self.non_target,
            "pct_conventional": self.pct_conventional,
            "pct_ai_product": self.pct_ai_product,
            "pct_exclude": self.pct_exclude,
            "pct_non_target": self.pct_non_target,
            "non_target_ci_95": [self.non_target_ci_low, self.non_target_ci_high],
            "counts": {
                "CONVENTIONAL_SOFTWARE": self.conventional,
                "AI_PRODUCT": self.ai_product,
                "EXCLUDE": self.exclude,
                "TIE": self.tie_count,
            },
        }


def summarize_family(family: str, labels: list[str]) -> FamilyStats:
    counts = Counter(labels)
    tie_count = counts.get("TIE", 0)
    rate_n = sum(counts[l] for l in RATE_LABELS)
    conventional = counts.get("CONVENTIONAL_SOFTWARE", 0)
    ai_product = counts.get("AI_PRODUCT", 0)
    exclude = counts.get("EXCLUDE", 0)
    non_target = ai_product + exclude
    ci_low, ci_high = wilson_ci(non_target, rate_n)
    return FamilyStats(
        family=family,
        n=len(labels),
        tie_count=tie_count,
        conventional=conventional,
        ai_product=ai_product,
        exclude=exclude,
        non_target=non_target,
        pct_conventional=pct(conventional, rate_n),
        pct_ai_product=pct(ai_product, rate_n),
        pct_exclude=pct(exclude, rate_n),
        pct_non_target=pct(non_target, rate_n),
        non_target_ci_low=ci_low,
        non_target_ci_high=ci_high,
    )


def build_family_tables(
    rows: list[dict[str, str]],
    dimension: str,
) -> list[FamilyStats]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        grouped[row[dimension]].append(row["majority_label"])
    stats = [summarize_family(family, labels) for family, labels in grouped.items()]
    return sorted(stats, key=lambda s: (-s.n, s.family))


def identify_risk_families(stats: list[FamilyStats]) -> dict[str, list[dict[str, Any]]]:
    high_risk = [
        s.to_dict()
        for s in stats
        if s.n >= 5 and s.pct_non_target >= 60.0
    ]
    high_risk.sort(key=lambda d: (-d["pct_non_target"], -d["n"]))
    lower_risk = [
        s.to_dict()
        for s in stats
        if s.n >= 5 and s.pct_conventional >= 50.0
    ]
    lower_risk.sort(key=lambda d: (-d["pct_conventional"], -d["n"]))
    return {"high_non_target": high_risk, "lower_non_target": lower_risk}
