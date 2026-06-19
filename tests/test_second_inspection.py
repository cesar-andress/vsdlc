from __future__ import annotations

import csv
from pathlib import Path

from vsdlc_mining.inspection_sample import (
    INSPECTION_BLANK_METADATA_FIELDS,
    INSPECTION_SAMPLE_FIELDS,
    SECOND_INSPECTOR_BLANK_FIELDS,
    write_second_inspector_blank_csv,
)
from vsdlc_mining.second_inspection_validation import (
    compute_second_inspection_evaluation,
    validate_second_inspection_completed,
)


def _metadata_row(repo_name: str) -> dict[str, str]:
    return {
        "repo_full_name": repo_name,
        "repo_url": f"https://github.com/{repo_name}",
        "stars": "10",
        "primary_language": "Python",
        "github_description": "Example",
        "github_topics": "ai",
        "detected_instruction_artifacts": '{"matched_paths": ["AGENTS.md"], "queries": ["AGENTS.md"]}',
        "ci_evidence": ".github/workflows/ci.yml",
        "release_evidence": "",
    }


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fieldnames} for row in rows)


def test_write_second_inspector_blank_csv(tmp_path: Path) -> None:
    row = _metadata_row("acme/service")
    output = tmp_path / "blank.csv"
    assert write_second_inspector_blank_csv(output, [row]) == 1

    with output.open(encoding="utf-8", newline="") as handle:
        written = next(csv.DictReader(handle))

    assert set(written.keys()) == set(SECOND_INSPECTOR_BLANK_FIELDS)
    assert "majority_label" not in written
    assert written["inspector2_label"] == ""


def test_validate_second_inspection_completed(tmp_path: Path) -> None:
    repos = [f"org/repo{i:02d}" for i in range(50)]
    blank_rows = [_metadata_row(repo) for repo in repos]
    blank_path = tmp_path / "blank.csv"
    write_second_inspector_blank_csv(blank_path, blank_rows)

    completed_rows = []
    for index, repo in enumerate(repos):
        row = _metadata_row(repo)
        row.update(
            {
                "inspector2_label": "CONVENTIONAL_SOFTWARE" if index % 2 == 0 else "EXCLUDE",
                "inspector2_confidence": "high",
                "inspector2_evidence_sources": "readme,file_tree",
                "inspector2_functional_note": "package.json exposes a CLI for end users",
                "inspector2_free_notes": "",
            }
        )
        completed_rows.append(row)

    completed_path = tmp_path / "completed.csv"
    _write_csv(completed_path, SECOND_INSPECTOR_BLANK_FIELDS, completed_rows)

    result = validate_second_inspection_completed(blank_path, completed_path)
    assert result["valid"] is True
    assert result["expected_repositories"] == 50


def test_compute_second_inspection_evaluation(tmp_path: Path) -> None:
    repos = [f"org/repo{i:02d}" for i in range(50)]
    blank_rows = [_metadata_row(repo) for repo in repos]
    blank_path = tmp_path / "blank.csv"
    write_second_inspector_blank_csv(blank_path, blank_rows)

    reference_rows = []
    inspector1_rows = []
    inspector2_rows = []
    for index, repo in enumerate(repos):
        majority = "CONVENTIONAL_SOFTWARE" if index < 20 else "AI_PRODUCT" if index < 35 else "EXCLUDE"
        inspection = majority if index % 3 else "EXCLUDE"
        inspector2 = majority if index % 4 else inspection

        reference_rows.append(
            {
                **_metadata_row(repo),
                "majority_label": majority,
                "claude_label": majority,
                "human1_label": majority,
                "human2_label": majority,
            }
        )
        inspector1_rows.append(
            {
                **_metadata_row(repo),
                "inspection_label": inspection,
                "inspection_confidence": "high",
                "inspection_evidence": "summary",
                "inspected_readme": "true",
                "inspected_file_tree": "true",
                "inspected_dependencies": "false",
                "inspected_entrypoints": "false",
                "inspected_instruction_consumption": "false",
                "functional_evidence": "README describes an application for end users.",
                "inspection_notes": "",
            }
        )
        inspector2_rows.append(
            {
                **_metadata_row(repo),
                "inspector2_label": inspector2,
                "inspector2_confidence": "medium",
                "inspector2_evidence_sources": "readme,dependencies",
                "inspector2_functional_note": "src/app implements a desktop writing application.",
                "inspector2_free_notes": "",
            }
        )

    reference_path = tmp_path / "reference.csv"
    _write_csv(reference_path, INSPECTION_SAMPLE_FIELDS, reference_rows)
    inspector1_path = tmp_path / "inspector1.csv"
    _write_csv(
        inspector1_path,
        [
            *INSPECTION_BLANK_METADATA_FIELDS,
            "inspection_label",
            "inspection_confidence",
            "inspection_evidence",
            "inspected_readme",
            "inspected_file_tree",
            "inspected_dependencies",
            "inspected_entrypoints",
            "inspected_instruction_consumption",
            "functional_evidence",
            "inspection_notes",
        ],
        inspector1_rows,
    )
    inspector2_path = tmp_path / "inspector2.csv"
    _write_csv(inspector2_path, SECOND_INSPECTOR_BLANK_FIELDS, inspector2_rows)

    result = compute_second_inspection_evaluation(
        reference_path=reference_path,
        inspector1_completed_path=inspector1_path,
        inspector2_completed_path=inspector2_path,
        blank_path=blank_path,
        n_bootstrap=200,
        seed=7,
    )

    assert result["paired_repositories"] == 50
    assert set(result["comparisons"]) == {
        "metadata_consensus_vs_inspector1",
        "metadata_consensus_vs_inspector2",
        "inspector1_vs_inspector2",
    }
    assert len(result["confusion_matrices"]) > 0
    assert "exclude_vs_conventional" in result["disagreement_stats"]["inspector1_vs_inspector2"]["patterns"]
