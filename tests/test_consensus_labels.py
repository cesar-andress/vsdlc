from __future__ import annotations

from vsdlc_mining.consensus_labels import (
    classify_voting_case,
    compute_human_only_label,
    compute_majority_label,
)


def test_majority_label_three_way_plurality() -> None:
    assert compute_majority_label("EXCLUDE", "CONVENTIONAL_SOFTWARE", "EXCLUDE") == "EXCLUDE"
    assert compute_majority_label("EXCLUDE", "CONVENTIONAL_SOFTWARE", "AI_PRODUCT") == "TIE"
    assert compute_majority_label("AI_PRODUCT", "AI_PRODUCT", "AI_PRODUCT") == "AI_PRODUCT"


def test_human_only_label() -> None:
    assert compute_human_only_label("CONVENTIONAL_SOFTWARE", "CONVENTIONAL_SOFTWARE") == "CONVENTIONAL_SOFTWARE"
    assert compute_human_only_label("AI_PRODUCT", "EXCLUDE") == "TIE"


def test_classify_voting_case() -> None:
    assert (
        classify_voting_case("AI_PRODUCT", "CONVENTIONAL_SOFTWARE", "CONVENTIONAL_SOFTWARE")
        == "humans_agree_llm_dissents"
    )
    assert (
        classify_voting_case("EXCLUDE", "CONVENTIONAL_SOFTWARE", "AI_PRODUCT")
        == "all_three_differ"
    )
    assert (
        classify_voting_case("EXCLUDE", "CONVENTIONAL_SOFTWARE", "EXCLUDE")
        == "humans_disagree_llm_resolves"
    )
