from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from vsdlc_mining.rq2_contamination import (
    build_family_tables,
    matched_path_to_family,
    metadata_sparsity,
    primary_language_group,
    query_to_family,
    summarize_family,
    wilson_ci,
)


def test_query_to_family_mappings() -> None:
    assert query_to_family("AGENTS.md") == "AGENTS.md"
    assert query_to_family("system_prompt.*") == "System prompts"
    assert query_to_family("unknown-query") == "Other"


def test_matched_path_to_family_root_and_nested() -> None:
    assert matched_path_to_family("AGENTS.md") == "root instruction file"
    assert matched_path_to_family(".cursor/rules/foo.mdc") == ".cursor/rules"
    assert matched_path_to_family("prompts/foo/bar.prompt.md") == "prompts directory"
    assert matched_path_to_family(
        "LandingPage/src/app/docs/documents/configuration/system_prompts.md"
    ) == "system prompt source"


def test_metadata_sparsity_buckets() -> None:
    assert metadata_sparsity("desc", "topic") == "complete_metadata"
    assert metadata_sparsity("", "topic") == "missing_description"
    assert metadata_sparsity("desc", "") == "missing_topics"
    assert metadata_sparsity("", "") == "missing_description_and_topics"


def test_primary_language_group() -> None:
    assert primary_language_group("Python") == "Python"
    assert primary_language_group("TypeScript") == "TypeScript/JavaScript"
    assert primary_language_group("Rust") == "Rust/Go"
    assert primary_language_group("") == "Docs/Markdown"


def test_summarize_family_excludes_tie_from_rates() -> None:
    stats = summarize_family(
        "demo",
        ["CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE", "TIE"],
    )
    assert stats.n == 4
    assert stats.tie_count == 1
    assert stats.pct_non_target == 66.7
    assert stats.pct_conventional == 33.3


def test_wilson_ci_bounds() -> None:
    low, high = wilson_ci(173, 296)
    assert 0.0 <= low < high <= 100.0


def test_build_family_tables_groups_rows() -> None:
    rows = [
        {"query_family": "AGENTS.md", "majority_label": "AI_PRODUCT"},
        {"query_family": "AGENTS.md", "majority_label": "CONVENTIONAL_SOFTWARE"},
    ]
    stats = build_family_tables(rows, "query_family")
    assert len(stats) == 1
    assert stats[0].family == "AGENTS.md"
    assert stats[0].n == 2


def test_analyze_rq2_contamination_structure_cli() -> None:
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts" / "analyze_rq2_contamination_structure.py"
    output = root / "data" / "processed" / "rq2_contamination_structure.json"
    subprocess.run([sys.executable, str(script)], check=True, cwd=root)
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["n_intersection"] == 300
    assert len(payload["query_family_table"]) >= 6
    assert len(payload["matched_path_family_table"]) >= 5
    assert len(payload["sparse_metadata_table"]) == 4
