from __future__ import annotations

import json
from pathlib import Path

import pytest

from vsdlc_mining.baseline_heuristics import (
    evaluate_all_baselines,
    predict_baseline_1,
    predict_baseline_2,
    predict_baseline_3,
    run_baseline_comparison,
)


def _row(**kwargs: str) -> dict[str, str]:
    base = {
        "repo_full_name": "acme/service",
        "github_description": "",
        "github_topics": "",
        "detected_instruction_artifacts": json.dumps(
            {"queries": ["AGENTS.md"], "matched_paths": ["AGENTS.md"]}
        ),
        "adjudicated_label": "CONVENTIONAL_SOFTWARE",
    }
    base.update(kwargs)
    return base


def test_baseline_1_description_keyword() -> None:
    row = _row(github_description="REST API for inventory management")
    assert predict_baseline_1(row) == "CONVENTIONAL_SOFTWARE"
    row = _row(github_description="MCP server for Claude agents", github_topics="")
    assert predict_baseline_1(row) == "AI_PRODUCT"


def test_baseline_2_name_topic_keyword() -> None:
    row = _row(repo_full_name="acme/service", github_topics="react|web")
    assert predict_baseline_2(row) == "CONVENTIONAL_SOFTWARE"
    row = _row(repo_full_name="acme/agent-framework", github_topics="")
    assert predict_baseline_2(row) == "AI_PRODUCT"


def test_baseline_3_artifact_trigger() -> None:
    row = _row(
        detected_instruction_artifacts=json.dumps(
            {"queries": [".cursor/rules"], "matched_paths": [".cursor/rules/CLAUDE.md"]}
        )
    )
    assert predict_baseline_3(row) == "AI_PRODUCT"
    row = _row(
        detected_instruction_artifacts=json.dumps(
            {"queries": [".cursor/rules"], "matched_paths": [".cursor/rules/cache.md"]}
        )
    )
    assert predict_baseline_3(row) == "CONVENTIONAL_SOFTWARE"


def test_evaluate_all_baselines_reports_metrics_and_disagreements() -> None:
    rows = [
        _row(
            repo_full_name="acme/app",
            adjudicated_label="CONVENTIONAL_SOFTWARE",
            github_description="Inventory SaaS",
            detected_instruction_artifacts=json.dumps(
                {"queries": ["AGENTS.md"], "matched_paths": ["apps/api/AGENTS.md"]}
            ),
        ),
        _row(
            repo_full_name="acme/agent-kit",
            adjudicated_label="AI_PRODUCT",
            github_description="Orchestration platform for operators",
            github_topics="kubernetes|platform",
            detected_instruction_artifacts=json.dumps(
                {"queries": [".cursor/rules"], "matched_paths": [".cursor/rules/cache.md"]}
            ),
        ),
    ]
    result = evaluate_all_baselines(rows)
    assert result["evaluated_repositories"] == 2
    baseline_1 = result["baselines"]["baseline_1_description_topics_keywords"]
    assert baseline_1["accuracy"] == 0.5
    assert len(baseline_1["disagreements"]) == 1
    assert len(result["valuable_cases"]) >= 1


def test_run_baseline_comparison_from_csv(tmp_path: Path) -> None:
    import csv

    artifacts = json.dumps({"queries": ["AGENTS.md"], "matched_paths": ["AGENTS.md"]})
    input_path = tmp_path / "sample.csv"
    with input_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "repo_full_name",
                "github_description",
                "github_topics",
                "detected_instruction_artifacts",
                "adjudicated_label",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "repo_full_name": "acme/app",
                "github_description": "Inventory SaaS",
                "github_topics": "",
                "detected_instruction_artifacts": artifacts,
                "adjudicated_label": "CONVENTIONAL_SOFTWARE",
            }
        )
    result = run_baseline_comparison(input_path)
    assert result["evaluated_repositories"] == 1
    assert "baseline_3_instruction_artifact_triggers" in result["baselines"]


def test_evaluate_without_adjudicated_labels_warns() -> None:
    rows = [_row(adjudicated_label="")]
    result = evaluate_all_baselines(rows)
    assert result["evaluated_repositories"] == 0
    assert any("No adjudicated labels" in warning for warning in result["warnings"])
