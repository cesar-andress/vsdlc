"""Metadata-visible feature construction for learned baseline models."""

from __future__ import annotations

import json
import math
import re
from typing import Any

from vsdlc_mining.baseline_heuristics import _parse_instruction_artifacts


def collapse_binary_decontamination(label: str) -> str:
    normalized = label.strip().upper()
    if normalized == "CONVENTIONAL_SOFTWARE":
        return "target_population"
    if normalized in {"AI_PRODUCT", "EXCLUDE"}:
        return "non_target"
    return ""


def metadata_document(row: dict[str, str]) -> str:
    queries, matched_paths = _parse_instruction_artifacts(row.get("detected_instruction_artifacts") or "")
    parts = [
        row.get("repo_full_name") or "",
        row.get("github_description") or "",
        (row.get("github_topics") or "").replace("|", " "),
        row.get("primary_language") or "",
        row.get("ci_evidence") or "",
        row.get("release_evidence") or "",
        row.get("sample_stratum") or "",
        " ".join(queries),
        " ".join(matched_paths),
    ]
    return "\n".join(part.strip() for part in parts if part and part.strip())


def _parse_bool_flag(value: str) -> float:
    return 1.0 if value.strip().lower() in {"true", "1", "yes"} else 0.0


def metadata_numeric_features(row: dict[str, str]) -> list[float]:
    queries, matched_paths = _parse_instruction_artifacts(row.get("detected_instruction_artifacts") or "")
    stars_raw = (row.get("stars") or "0").strip()
    try:
        stars = max(0.0, float(stars_raw))
    except ValueError:
        stars = 0.0
    ci_evidence = (row.get("ci_evidence") or "").strip()
    release_evidence = (row.get("release_evidence") or "").strip()
    return [
        math.log1p(stars),
        _parse_bool_flag(row.get("agent_product_flag") or ""),
        1.0 if ci_evidence else 0.0,
        1.0 if release_evidence else 0.0,
        float(len(queries)),
        float(len(matched_paths)),
        float(len(re.findall(r"\|", row.get("github_topics") or "")) + (1 if row.get("github_topics") else 0)),
        1.0 if (row.get("github_description") or "").strip() else 0.0,
    ]


NUMERIC_FEATURE_NAMES = (
    "log1p_stars",
    "agent_product_flag",
    "has_ci_evidence",
    "has_release_evidence",
    "n_queries",
    "n_matched_paths",
    "n_topics",
    "has_description",
)


def rows_to_feature_records(rows: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "documents": [metadata_document(row) for row in rows],
        "numeric": [metadata_numeric_features(row) for row in rows],
        "repo_full_name": [row.get("repo_full_name", "") for row in rows],
    }
