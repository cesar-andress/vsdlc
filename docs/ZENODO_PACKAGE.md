# Zenodo replication package policy

## Rule

Zenodo archives built from this repository must contain **reproducibility material only**.
They must never include manuscript PDFs, LaTeX sources, bibliographies, cover letters,
reviewer responses, or editorial audits.

## Current clean archive

- Path (local build): `releases/zenodo-v1.0.1-replication-only.tar.gz` (gitignored)
- Contents: source, scripts, tests, permitted `data/processed` outputs, docs, LICENSE,
  CITATION.cff, dependency files, and documented generated tables
  (`docs/GENERATED_TEX_TABLES.md`).
- Explicitly excluded: `manuscript/`, `papers/`, `submission/`, `related_work_rebuild/`,
  `*.bib`, `*.pdf` (except none), editorial markdown.

## Legacy archives

Older archives under `../release/zenodo-v1.0.0-ist.tar.gz` and
`releases/zenodo-v0.1.0-msr-contamination-audit.tar.gz` may predate this policy.
Do **not** upload them to Zenodo. Use only the replication-only build.
