"""Tests for target-sensitivity analysis."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

SCRIPT = ROOT / "scripts/analyze_target_sensitivity.py"
spec = importlib.util.spec_from_file_location("analyze_target_sensitivity", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

COMPARISON_CSV = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"


@pytest.mark.skipif(not COMPARISON_CSV.exists(), reason="frozen pilot CSV missing")
def test_target_sensitivity_headline_matches_rq1() -> None:
    rows = mod.load_consensus_rows(COMPARISON_CSV)
    results = mod.build_results(rows)
    headline = next(
        s for s in results["scenarios"] if s["key"] == "conventional_application_software"
    )
    assert results["consensus_n"] == 300
    assert headline["non_target_count"] == 173
    assert headline["non_target_pct"] == 57.7
    assert headline["wilson_ci_pct"] == [52.0, 63.1]
    assert headline["target_count"] == 123


@pytest.mark.skipif(not COMPARISON_CSV.exists(), reason="frozen pilot CSV missing")
def test_target_sensitivity_alternative_collapses() -> None:
    rows = mod.load_consensus_rows(COMPARISON_CSV)
    results = mod.build_results(rows)
    product_target = next(s for s in results["scenarios"] if s["key"] == "any_software_product")
    ai_builder = next(s for s in results["scenarios"] if s["key"] == "ai_builder_tooling")
    role = next(s for s in results["scenarios"] if s["key"] == "product_role_contrast")

    assert product_target["non_target_pct"] == 21.7
    assert product_target["wilson_ci_pct"] == [17.4, 26.7]
    assert ai_builder["non_target_pct"] == 62.7
    assert ai_builder["wilson_ci_pct"] == [57.1, 67.9]
    assert role["n"] == 235
    assert role["ai_product_pct"] == 46.0
    assert role["conventional_pct"] == 52.3


def test_render_tex_contains_label() -> None:
    payload = json.loads(
        (ROOT / "data/processed/target_sensitivity_results.json").read_text(encoding="utf-8")
        if (ROOT / "data/processed/target_sensitivity_results.json").exists()
        else '{"scenarios": []}'
    )
    if not payload.get("scenarios"):
        pytest.skip("target_sensitivity_results.json not generated yet")
    tex = mod.render_tex(payload)
    assert "tab:target-sensitivity" in tex
