# Documentation consistency audit — VSDLC Mining Pilot

Audit date: 2026-06-18  
Scope: `~/papers/vsdlc/vsdlc` (repository mining artifact only)

## Audit objective

Present the repository as an **initial public research artifact** for AI-assisted software development provenance — not as a journal/conference paper companion.

## Scan coverage

| Area | Files scanned |
|------|----------------|
| README | `README.md` |
| Docs | `docs/reproducibility.md`, `docs/zenodo_release_checklist.md` |
| Metadata | `CITATION.cff`, `pyproject.toml`, `MANIFEST.in`, `requirements.txt`, `LICENSE` |
| Source | `src/vsdlc_mining/*.py` |
| Scripts | `scripts/*.py` |
| Tests | `tests/*.py` |

Excluded from terminology audit (generated mining data, not project documentation):

- `data/interim/seed_search_checkpoint.json`
- `data/raw/repo_candidates.jsonl`

## Findings (pre-change)

No matches were found for: `paper_ieeesw`, `IEEE Computer`, `IEEE Software`, `rejected`, `desk reject`, `CSRCS`, `release justification paper`, `manuscript`, `submission draft`, `LaTeX`, `pdflatex`, `Overleaf`, `camera ready`, `reviewer`, `rebuttal`.

The following wording was **indirectly publication-oriented** or **terminology-inconsistent**:

| File | Line (approx.) | Problematic text | Suggested replacement | Action |
|------|----------------|------------------|----------------------|--------|
| `README.md` | 3 | `V-SDLC (Verified Software Development Lifecycle) research programme` | Frame as provenance research artifact | **Rewritten** |
| `README.md` | 149 | `After publication, cite using CITATION.cff` | `After the Zenodo record is released, cite using CITATION.cff` | **Rewritten** |
| `README.md` | 157 | `Pre-publication checklist` | `Release checklist` | **Rewritten** |
| `docs/reproducibility.md` | 119 | `Citation after Zenodo publication` | `Citation after Zenodo DOI assignment` | **Rewritten** |
| `docs/reproducibility.md` | 126 | `Example (fill after publication)` | `Example (fill after DOI assignment)` | **Rewritten** |
| `docs/zenodo_release_checklist.md` | 24 | `README or paper drafts` | `README or other documentation` | **Rewritten** |
| `docs/zenodo_release_checklist.md` | 32 | `matches publication date` | `matches the Zenodo release date` | **Rewritten** |
| `docs/zenodo_release_checklist.md` | 57–59 | `Post-publication` / `Paper/companion repository references` | `Post-release` / external artifact references only | **Rewritten** |
| `CITATION.cff` | 22–26 | `V-SDLC mining pipeline` abstract wording | Repository mining framework + traceability dataset | **Rewritten** |
| `pyproject.toml` | 8 | `V-SDLC traceability research` | `AI-assisted software development provenance` | **Rewritten** |
| `src/vsdlc_mining/__init__.py` | 1 | `V-SDLC GitHub repository mining pilot` | `VSDLC Mining Pilot — repository mining framework` | **Rewritten** |

### Clean areas (no changes required)

- `scripts/run_seed_search.py`, `scripts/run_repo_filter.py` — operational CLI only
- `src/vsdlc_mining/config.py`, `models.py`, `github_client.py`, etc. — no publication language
- `tests/` — no publication language
- `MANIFEST.in`, `requirements.txt`, `LICENSE` — neutral

### Generated data note

`data/interim/seed_search_checkpoint.json` contains third-party repository names and paths with substrings such as `paper`, `companion`, and `programming`. These are **mined GitHub metadata**, not project documentation. No edit applied.

## Terminology standardization applied

| Role | Canonical term |
|------|----------------|
| Project name | **VSDLC Mining Pilot** |
| Research theme | **AI-assisted software development provenance** |
| Software deliverable | **Repository mining framework** |
| Generated outputs | **Repository traceability dataset** |
| Release framing | **Initial public research artifact** / **reproducible research artifact** |

### Replacements made

| Former usage | Replaced with |
|--------------|---------------|
| V-SDLC research programme | AI-assisted software development provenance (research theme) |
| research programme / companion tone | initial public research artifact |
| publication (citation context) | Zenodo release / DOI assignment |
| Pre-publication checklist | Zenodo release checklist |
| Paper/companion repository | external references to this artifact |
| V-SDLC mining pipeline | repository mining framework |
| package / corpus (informal) | repository traceability dataset (where referring to outputs) |

## Changes applied

1. Rewrote `README.md` as canonical entry point with artifact table, research question, and standardized vocabulary.
2. Updated `docs/reproducibility.md` for consistent artifact framing and citation language.
3. Updated `docs/zenodo_release_checklist.md` to remove paper-companion wording.
4. Updated `CITATION.cff` abstract and keywords.
5. Updated `pyproject.toml` description and keywords.
6. Updated `src/vsdlc_mining/__init__.py` module docstring.
7. Added this audit report.

## Remaining manual decisions

| Item | Owner action |
|------|--------------|
| `CITATION.cff` DOI | Assigned: `10.5281/zenodo.20754778` (`v0.1.0-msr-contamination-audit`) |
| `CITATION.cff` `date-released` | Set to actual Zenodo release date |
| `pyproject.toml` `[project.urls]` | Align with final repository URL |
| Generated dataset inclusion in Zenodo | Decide whether to bundle `data/raw/*.jsonl` and `data/interim/*.jsonl` or publish regeneration instructions only |
| Parent repository `~/papers/vsdlc` | Out of scope for this audit; may still contain unrelated research materials |
| Package import name `vsdlc-mining` vs directory `vsdlc/` | Keep as-is unless renaming for public release |

## Unresolved inconsistencies

- **Directory vs. package naming:** repository path is `vsdlc/` while PyPI-style name is `vsdlc-mining`. Documented but not unified.
- **Historical git context:** parent monorepo may reference unrelated research outputs; this subdirectory is now self-consistent.
- **No dataset schema doc yet:** field-level schema for JSONL outputs is described in README tables but not in a standalone `docs/dataset_schema.md` (optional future improvement).

## Verification

After edits, re-scan of documentation files found **no remaining** matches for the blocked publication terms listed in the audit brief.
