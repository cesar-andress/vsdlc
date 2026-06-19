from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from vsdlc_mining.inspection_sample import (
    DEFAULT_INSPECTION_SEED,
    INSPECTION_BLANK_FIELDS,
    INSPECTION_SAMPLE_FIELDS,
    INSPECTION_STRATUM_TARGETS,
    inspection_priority_score,
    stratified_inspection_sample,
    write_inspection_blank_csv,
    write_inspection_sample_csv,
)
from vsdlc_mining.inspection_validation import (
    collect_functional_evidence_warnings,
    compute_inspection_validation,
)
from vsdlc_mining.models import EligibleRepo, EvidenceFlags


def _comparison_row(
    repo_name: str,
    *,
    majority: str,
    claude: str,
    human1: str,
    human2: str,
) -> dict[str, str]:
    return {
        "repo_full_name": repo_name,
        "claude_label": claude,
        "human1_label": human1,
        "human2_label": human2,
        "majority_label": majority,
    }


def _eligible(full_name: str, *, stars: int = 100) -> EligibleRepo:
    return EligibleRepo(
        full_name=full_name,
        repository_url=f"https://github.com/{full_name}",
        stars=stars,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        queries=["AGENTS.md"],
        matched_paths=["AGENTS.md"],
        evidence=EvidenceFlags(has_ci_evidence=True, ci_paths=[".github/workflows/ci.yml"]),
        github_description="Example repository",
        github_topics=["ai"],
        primary_language="Python",
    )


def test_inspection_priority_score_weights_disagreements() -> None:
    agree = _comparison_row("a/r", majority="AI_PRODUCT", claude="AI_PRODUCT", human1="AI_PRODUCT", human2="AI_PRODUCT")
    disagree = _comparison_row(
        "b/r",
        majority="EXCLUDE",
        claude="CONVENTIONAL_SOFTWARE",
        human1="EXCLUDE",
        human2="AI_PRODUCT",
    )
    assert inspection_priority_score(agree) == 0
    assert inspection_priority_score(disagree) == 3


def test_stratified_sample_counts_and_seed_reproducibility() -> None:
    comparison_rows = []
    enriched: dict[str, EligibleRepo] = {}
    for index in range(60):
        majority = "CONVENTIONAL_SOFTWARE"
        if index >= 25:
            majority = "AI_PRODUCT"
        if index >= 45:
            majority = "EXCLUDE"
        name = f"org/repo{index:02d}"
        human2 = "EXCLUDE" if index % 5 == 0 else majority
        comparison_rows.append(
            _comparison_row(
                name,
                majority=majority,
                claude=majority,
                human1=majority,
                human2=human2,
            )
        )
        enriched[name] = _eligible(name, stars=50 + index)

    first = stratified_inspection_sample(
        comparison_rows,
        enriched_by_name=enriched,
        stratum_targets=INSPECTION_STRATUM_TARGETS,
        seed=DEFAULT_INSPECTION_SEED,
    )
    second = stratified_inspection_sample(
        comparison_rows,
        enriched_by_name=enriched,
        stratum_targets=INSPECTION_STRATUM_TARGETS,
        seed=DEFAULT_INSPECTION_SEED,
    )

    assert len(first) == 50
    assert [row["repo_full_name"] for row in first] == [row["repo_full_name"] for row in second]
    counts = {label: 0 for label in INSPECTION_STRATUM_TARGETS}
    for row in first:
        counts[row["majority_label"]] += 1
    assert counts == INSPECTION_STRATUM_TARGETS


def test_write_inspection_csv_outputs(tmp_path: Path) -> None:
    row = {
        "repo_full_name": "acme/service",
        "repo_url": "https://github.com/acme/service",
        "majority_label": "CONVENTIONAL_SOFTWARE",
        "claude_label": "CONVENTIONAL_SOFTWARE",
        "human1_label": "AI_PRODUCT",
        "human2_label": "CONVENTIONAL_SOFTWARE",
        "stars": "120",
        "primary_language": "Go",
        "github_description": "A service",
        "github_topics": "go|service",
        "detected_instruction_artifacts": '{"matched_paths": ["AGENTS.md"], "queries": ["AGENTS.md"]}',
        "ci_evidence": ".github/workflows/ci.yml",
        "release_evidence": "",
    }
    sample_path = tmp_path / "sample.csv"
    blank_path = tmp_path / "blank.csv"
    assert write_inspection_sample_csv(sample_path, [row]) == 1
    assert write_inspection_blank_csv(blank_path, [row]) == 1

    with sample_path.open(encoding="utf-8", newline="") as handle:
        sample = next(csv.DictReader(handle))
    with blank_path.open(encoding="utf-8", newline="") as handle:
        blank = next(csv.DictReader(handle))

    assert set(sample.keys()) == set(INSPECTION_SAMPLE_FIELDS)
    assert set(blank.keys()) == set(INSPECTION_BLANK_FIELDS)
    assert "majority_label" not in blank
    assert blank["inspection_label"] == ""
    assert blank["inspected_readme"] == ""
    assert blank["inspected_dependencies"] == ""
    assert blank["functional_evidence"] == ""


def test_collect_functional_evidence_warnings() -> None:
    completed = {
        "a/one": {
            "functional_evidence": "package.json exposes a CLI for MCP server tooling",
            "inspected_readme": "true",
            "inspected_file_tree": "true",
            "inspected_dependencies": "true",
            "inspected_entrypoints": "false",
            "inspected_instruction_consumption": "false",
        },
        "b/two": {
            "functional_evidence": "",
            "inspected_readme": "true",
            "inspected_file_tree": "false",
            "inspected_dependencies": "false",
            "inspected_entrypoints": "false",
            "inspected_instruction_consumption": "false",
        },
    }
    warnings = collect_functional_evidence_warnings(completed, ["a/one", "b/two"])
    assert len(warnings) == 2
    assert warnings[0]["warning_type"] == "missing_functional_evidence"
    assert warnings[1]["warning_type"] == "insufficient_evidence_sources"


def test_compute_inspection_validation_metrics(tmp_path: Path) -> None:
    reference_path = tmp_path / "reference.csv"
    completed_path = tmp_path / "completed.csv"
    rows = [
        {
            "repo_full_name": "a/one",
            "repo_url": "https://github.com/a/one",
            "majority_label": "CONVENTIONAL_SOFTWARE",
            "claude_label": "CONVENTIONAL_SOFTWARE",
            "human1_label": "CONVENTIONAL_SOFTWARE",
            "human2_label": "AI_PRODUCT",
            "stars": "10",
            "primary_language": "Python",
            "github_description": "",
            "github_topics": "",
            "detected_instruction_artifacts": "",
            "ci_evidence": "",
            "release_evidence": "",
            "inspection_label": "CONVENTIONAL_SOFTWARE",
            "inspection_confidence": "high",
            "inspection_evidence": "README describes an application for end users.",
            "inspected_readme": "true",
            "inspected_file_tree": "true",
            "inspected_dependencies": "true",
            "inspected_entrypoints": "true",
            "inspected_instruction_consumption": "false",
            "functional_evidence": "src/app implements a desktop writing application; prompts are internal assets",
            "inspection_notes": "",
        },
        {
            "repo_full_name": "b/two",
            "repo_url": "https://github.com/b/two",
            "majority_label": "EXCLUDE",
            "claude_label": "EXCLUDE",
            "human1_label": "EXCLUDE",
            "human2_label": "EXCLUDE",
            "stars": "20",
            "primary_language": "",
            "github_description": "",
            "github_topics": "",
            "detected_instruction_artifacts": "",
            "ci_evidence": "",
            "release_evidence": "",
            "inspection_label": "AI_PRODUCT",
            "inspection_confidence": "medium",
            "inspection_evidence": "README is a prompt collection for builders.",
            "inspected_readme": "true",
            "inspected_file_tree": "false",
            "inspected_dependencies": "false",
            "inspected_entrypoints": "false",
            "inspected_instruction_consumption": "false",
            "functional_evidence": "repository is docs-only; no executable source found",
            "inspection_notes": "",
        },
    ]

    with reference_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INSPECTION_SAMPLE_FIELDS)
        writer.writeheader()
        writer.writerows({field: row[field] for field in INSPECTION_SAMPLE_FIELDS} for row in rows)

    with completed_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INSPECTION_BLANK_FIELDS)
        writer.writeheader()
        writer.writerows({field: row[field] for field in INSPECTION_BLANK_FIELDS} for row in rows)

    result = compute_inspection_validation(reference_path, completed_path)
    assert result["paired_repositories"] == 2
    assert result["agreement_count"] == 1
    assert result["agreement_rate"] == 0.5
    assert len(result["disagreements"]) == 1
    assert result["disagreements"][0]["repo_full_name"] == "b/two"
    assert result["exclude_vs_non_exclude"]["paired_repositories"] == 2
    assert result["ai_product_vs_conventional_excluding_exclude"]["paired_repositories"] == 1
    assert result["functional_evidence_warning_count"] == 1
    assert result["functional_evidence_warnings"][0]["repo_full_name"] == "b/two"
