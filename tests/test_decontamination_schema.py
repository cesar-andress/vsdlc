from __future__ import annotations

from vsdlc_mining.decontamination_schema import (
    LEGACY_PRIMARY_LABELS,
    PRIMARY_LABELS,
    SCHEMA_VERSION,
    SECONDARY_TAGS,
)


def test_primary_labels_three_class() -> None:
    assert len(PRIMARY_LABELS) == 3
    assert "CONVENTIONAL_SOFTWARE" in PRIMARY_LABELS
    assert "EXCLUDE" in PRIMARY_LABELS


def test_secondary_tags_include_packaging_cues() -> None:
    assert "RUNNABLE_PROMPT_TOOL" in SECONDARY_TAGS
    assert "DOTFILES" in SECONDARY_TAGS
    assert "DOCS_ONLY" in SECONDARY_TAGS
    assert len(SECONDARY_TAGS) == 10


def test_legacy_primary_labels_deprecated() -> None:
    assert LEGACY_PRIMARY_LABELS == frozenset({"TOOL", "ASSIST", "MIXED", "UNCLEAR"})


def test_schema_version() -> None:
    assert SCHEMA_VERSION == "0.2"
