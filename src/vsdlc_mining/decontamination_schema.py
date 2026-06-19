"""Canonical decontamination annotation schema constants (v0.2)."""

from __future__ import annotations

PRIMARY_LABELS = ("AI_PRODUCT", "CONVENTIONAL_SOFTWARE", "EXCLUDE")

SECONDARY_TAGS = (
    "NON_PRODUCT",
    "INSUFFICIENT_EVIDENCE",
    "DUAL_REVIEW",
    "BENCHMARK_OR_EVAL",
    "PROMPT_COLLECTION",
    "AI_SECURITY_LAB",
    "AI_CENTRAL_END_USER_APP",
    "RUNNABLE_PROMPT_TOOL",
    "DOTFILES",
    "DOCS_ONLY",
)

# Deprecated v0.1 four-class primary labels — not valid in primary_label for v0.2 analysis.
LEGACY_PRIMARY_LABELS = frozenset({"TOOL", "ASSIST", "MIXED", "UNCLEAR"})

BINARY_DECONTAMINATION_LABELS = ("target_population", "non_target")

SCHEMA_VERSION = "0.2"
