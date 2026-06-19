"""Baseline heuristic predictors for decontamination instrument comparison."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from vsdlc_mining.annotation_agreement import per_class_metrics
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS

BASELINE_PREDICTIONS = ("AI_PRODUCT", "CONVENTIONAL_SOFTWARE")

BASELINE_1_KEYWORDS = (
    "ai",
    "agent",
    "llm",
    "prompt",
    "mcp",
    "copilot",
    "claude",
    "openai",
)

BASELINE_2_NAME_TOPIC_KEYWORDS = (
    "agent",
    "framework",
    "sdk",
    "library",
    "benchmark",
    "eval",
)

BASELINE_3_ARTIFACT_TRIGGERS = (
    "AGENTS.md",
    "CLAUDE.md",
    "prompts/",
    "system_prompt.*",
)


def _normalize(value: str) -> str:
    return value.strip().lower()


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _resolve_adjudicated_label(row: dict[str, str]) -> str:
    for field in ("adjudicated_label", "primary_label", "label"):
        value = (row.get(field) or "").strip().upper()
        if value:
            return value
    return ""


def _parse_instruction_artifacts(raw: str) -> tuple[list[str], list[str]]:
    if not raw.strip():
        return [], []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return [], []
    queries = payload.get("queries") or []
    matched_paths = payload.get("matched_paths") or []
    if not isinstance(queries, list):
        queries = []
    if not isinstance(matched_paths, list):
        matched_paths = []
    return [str(item) for item in queries], [str(item) for item in matched_paths]


def _contains_keyword(haystack: str, keywords: tuple[str, ...]) -> bool:
    text = _normalize(haystack)
    return any(keyword in text for keyword in keywords)


def _artifact_triggered(queries: list[str], matched_paths: list[str]) -> bool:
    for query in queries:
        normalized = query.strip()
        if normalized in {"AGENTS.md", "CLAUDE.md"}:
            return True
        if normalized == "prompts/" or normalized.startswith("prompts/"):
            return True
        if normalized == "system_prompt.*" or "system_prompt" in normalized.lower():
            return True

    for path in matched_paths:
        lowered = path.lower()
        if lowered.endswith("/agents.md") or lowered == "agents.md":
            return True
        if lowered.endswith("/claude.md") or lowered == "claude.md":
            return True
        if "prompts/" in lowered:
            return True
        if "system_prompt" in lowered:
            return True
    return False


def predict_baseline_1(row: dict[str, str]) -> str:
    haystack = " ".join(
        [
            row.get("github_description") or "",
            (row.get("github_topics") or "").replace("|", " "),
        ]
    )
    if _contains_keyword(haystack, BASELINE_1_KEYWORDS):
        return "AI_PRODUCT"
    return "CONVENTIONAL_SOFTWARE"


def predict_baseline_2(row: dict[str, str]) -> str:
    haystack = " ".join(
        [
            row.get("repo_full_name") or "",
            (row.get("github_topics") or "").replace("|", " "),
        ]
    )
    if _contains_keyword(haystack, BASELINE_2_NAME_TOPIC_KEYWORDS):
        return "AI_PRODUCT"
    return "CONVENTIONAL_SOFTWARE"


def predict_baseline_3(row: dict[str, str]) -> str:
    queries, matched_paths = _parse_instruction_artifacts(row.get("detected_instruction_artifacts") or "")
    if _artifact_triggered(queries, matched_paths):
        return "AI_PRODUCT"
    return "CONVENTIONAL_SOFTWARE"


BASELINE_PREDICTORS = {
    "baseline_1_description_topics_keywords": predict_baseline_1,
    "baseline_2_name_topics_keywords": predict_baseline_2,
    "baseline_3_instruction_artifact_triggers": predict_baseline_3,
}


def confusion_matrix_gold_pred(
    gold: list[str],
    predicted: list[str],
    *,
    gold_categories: tuple[str, ...] = PRIMARY_LABELS,
    pred_categories: tuple[str, ...] = BASELINE_PREDICTIONS,
) -> dict[str, dict[str, int]]:
    matrix = {gold_label: {pred_label: 0 for pred_label in pred_categories} for gold_label in gold_categories}
    for gold_label, pred_label in zip(gold, predicted):
        if gold_label in matrix and pred_label in matrix[gold_label]:
            matrix[gold_label][pred_label] += 1
    return matrix


def evaluate_baseline_predictions(
    gold: list[str],
    predicted: list[str],
    *,
    repos: list[str],
) -> dict[str, Any]:
    if not gold or len(gold) != len(predicted):
        return {
            "evaluated_repositories": 0,
            "accuracy": None,
            "per_class": {},
            "confusion_matrix": {},
            "disagreements": [],
        }

    correct = sum(1 for g, p in zip(gold, predicted) if g == p)
    disagreements = [
        {
            "repo_full_name": repo,
            "adjudicated_label": gold_label,
            "baseline_prediction": pred_label,
        }
        for repo, gold_label, pred_label in zip(repos, gold, predicted)
        if gold_label != pred_label
    ]

    return {
        "evaluated_repositories": len(gold),
        "accuracy": correct / len(gold),
        "per_class": per_class_metrics(predicted, gold, PRIMARY_LABELS),
        "confusion_matrix": confusion_matrix_gold_pred(gold, predicted),
        "disagreements": disagreements,
    }


def evaluate_all_baselines(rows: list[dict[str, str]]) -> dict[str, Any]:
    evaluated: list[dict[str, str]] = []
    warnings: list[str] = []

    for row in rows:
        adjudicated = _resolve_adjudicated_label(row)
        if not adjudicated:
            continue
        if adjudicated not in PRIMARY_LABELS:
            warnings.append(
                f"Skipping {row.get('repo_full_name', '')}: unsupported adjudicated label '{adjudicated}'."
            )
            continue
        evaluated.append(row)

    if not evaluated:
        return {
            "evaluated_repositories": 0,
            "warnings": warnings + ["No adjudicated labels found in input."],
            "baselines": {},
            "valuable_cases": [],
        }

    repos = [row["repo_full_name"] for row in evaluated]
    gold = [_resolve_adjudicated_label(row) for row in evaluated]

    baseline_results: dict[str, Any] = {}
    valuable_cases: dict[str, dict[str, Any]] = {}

    for baseline_name, predictor in BASELINE_PREDICTORS.items():
        predicted = [predictor(row) for row in evaluated]
        baseline_results[baseline_name] = evaluate_baseline_predictions(
            gold,
            predicted,
            repos=repos,
        )

        for repo, gold_label, pred_label in zip(repos, gold, predicted):
            if gold_label == pred_label:
                continue
            entry = valuable_cases.setdefault(
                repo,
                {
                    "repo_full_name": repo,
                    "adjudicated_label": gold_label,
                    "baseline_predictions": {},
                },
            )
            entry["baseline_predictions"][baseline_name] = pred_label

    return {
        "evaluated_repositories": len(evaluated),
        "warnings": warnings,
        "baselines": baseline_results,
        "valuable_cases": sorted(valuable_cases.values(), key=lambda item: item["repo_full_name"]),
    }


def run_baseline_comparison(input_path: Path) -> dict[str, Any]:
    rows = _read_rows(input_path)
    result = evaluate_all_baselines(rows)
    result["input"] = str(input_path)
    result["adjudicated_label_fields"] = ["adjudicated_label", "primary_label", "label"]
    result["gold_categories"] = list(PRIMARY_LABELS)
    result["baseline_prediction_categories"] = list(BASELINE_PREDICTIONS)
    return result
