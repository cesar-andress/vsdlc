from __future__ import annotations

from vsdlc_mining.learned_baselines import merge_metadata_with_labels
from vsdlc_mining.metadata_features import collapse_binary_decontamination, metadata_document


def test_collapse_binary_decontamination() -> None:
    assert collapse_binary_decontamination("CONVENTIONAL_SOFTWARE") == "target_population"
    assert collapse_binary_decontamination("AI_PRODUCT") == "non_target"
    assert collapse_binary_decontamination("EXCLUDE") == "non_target"


def test_metadata_document_uses_annotation_visible_fields() -> None:
    row = {
        "repo_full_name": "org/demo",
        "github_description": "Agent framework for builders",
        "github_topics": "agent|llm",
        "primary_language": "Python",
        "detected_instruction_artifacts": '{"queries": ["AGENTS.md"], "matched_paths": ["AGENTS.md"]}',
        "ci_evidence": ".github/workflows",
        "release_evidence": "tags=1",
        "sample_stratum": "stars:10-49",
    }
    document = metadata_document(row)
    assert "org/demo" in document
    assert "Agent framework" in document
    assert "AGENTS.md" in document
    assert "primary_label" not in document


def test_merge_metadata_with_labels() -> None:
    metadata_rows = [
        {
            "repo_full_name": "org/one",
            "github_description": "demo",
        }
    ]
    label_rows = [
        {
            "repo_full_name": "org/one",
            "majority_label": "AI_PRODUCT",
        }
    ]
    merged = merge_metadata_with_labels(metadata_rows, label_rows)
    assert len(merged) == 1
    assert merged[0]["majority_label"] == "AI_PRODUCT"
