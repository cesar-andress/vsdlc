from __future__ import annotations

from datetime import datetime
from pathlib import Path

from vsdlc_mining.config import MIN_PUSHED_AT, MIN_STARS
from vsdlc_mining.models import EligibleRepo, EvidenceFlags
from vsdlc_mining.second_frame_analysis import (
    analyze_second_frame_contamination,
    render_manuscript_paragraph,
    render_manuscript_table,
)
from vsdlc_mining.second_frame_sample import (
    SECOND_FRAME_ANNOTATION_FIELDS,
    eligible_to_annotation_blank_row,
    sample_second_frame_repositories,
    write_second_frame_csv,
)
from vsdlc_mining.second_frame_search import build_topic_repository_query


def _eligible(name: str, *, stars: int, query: str) -> EligibleRepo:
    return EligibleRepo(
        full_name=name,
        repository_url=f"https://github.com/{name}",
        stars=stars,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        queries=[query],
        matched_paths=[query],
        agent_product_flag=True,
        evidence=EvidenceFlags(has_ci_evidence=True, ci_paths=[".github/workflows"]),
        github_description="AI application",
        github_topics=["llm", "ai-agent"],
        primary_language="Python",
    )


def test_build_topic_repository_query() -> None:
    query = build_topic_repository_query("topic:llm")
    assert "topic:llm" in query
    assert f"stars:>={MIN_STARS}" in query
    assert f"pushed:>={MIN_PUSHED_AT.date().isoformat()}" in query
    assert "fork:false" in query
    assert "archived:false" in query


def test_sample_prefers_non_overlap() -> None:
    eligible = [_eligible(f"org/repo{i}", stars=100 - i, query="topic:llm") for i in range(10)]
    instruction_names = {f"org/repo{i}" for i in range(4)}
    selected, summary = sample_second_frame_repositories(
        eligible,
        instruction_frame_names=instruction_names,
        sample_size=5,
        seed=42,
    )
    assert len(selected) == 5
    assert summary["overlap_in_sample"] == 0
    assert all(repo.full_name not in instruction_names for repo in selected)


def test_analyze_second_frame_contamination(tmp_path: Path) -> None:
    repos = [_eligible(f"org/repo{i}", stars=50 + i, query="topic:llm") for i in range(8)]
    blank_rows = [eligible_to_annotation_blank_row(repo) for repo in repos]
    for index, row in enumerate(blank_rows):
        if index < 3:
            row["primary_label"] = "CONVENTIONAL_SOFTWARE"
        elif index < 6:
            row["primary_label"] = "AI_PRODUCT"
        else:
            row["primary_label"] = "EXCLUDE"

    annotation_path = tmp_path / "completed.csv"
    write_second_frame_csv(annotation_path, blank_rows, SECOND_FRAME_ANNOTATION_FIELDS)

    results = analyze_second_frame_contamination(
        annotation_path=annotation_path,
        n_bootstrap=500,
        seed=7,
    )
    assert results["annotated_repositories"] == 8
    assert results["binary_target_vs_non_target"]["non_target_count"] == 5
    assert "frame_comparison" in results
    table = render_manuscript_table(results)
    paragraph = render_manuscript_paragraph(results)
    assert "robustness" in paragraph.casefold()
    assert "Instruction-artifact" in table
