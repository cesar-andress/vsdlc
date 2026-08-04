# Zenodo release checklist — replication package (PeerJ companion)

Use this checklist before creating a Git tag, GitHub release, or Zenodo upload for this replication package.

## Code quality

- [ ] `python -m pip install -e ".[dev]"` succeeds on a clean environment (Python 3.11+)
- [ ] `pytest` passes with zero failures
- [ ] `ruff check src tests scripts` passes (or documented exceptions recorded)
- [ ] `mypy src/vsdlc_mining` passes (or documented exceptions recorded)

## Documentation

- [x] `README.md` describes the PeerJ companion replication package, study scope, and reproducible materials
- [x] `docs/reproducibility.md` cites DOI `10.5281/zenodo.21794793`
- [ ] Repository traceability dataset schemas are documented in README or `docs/`

## Licensing and citation metadata

- [x] `LICENSE` reviewed (MIT)
- [x] `CITATION.cff` authors, title, version `1.0.0`, and date-released are correct
- [x] `CITATION.cff` DOI is `10.5281/zenodo.21794793`
- [x] README / RELEASE match PeerJ title and Zenodo DOI

## Versioning

- [x] Version bumped consistently in:
  - `pyproject.toml` (if present)
  - `src/vsdlc_mining/__init__.py` (if versioned)
  - `CITATION.cff`
- [x] `date-released` in `CITATION.cff` matches the Zenodo release date (2026-08-04)

## Data policy

- [x] Large/raw data policy stated (what is included in Zenodo bundle vs. regenerated locally)
- [x] No secrets, tokens, or `.env` files in the release archive
- [x] `.cursor/` IDE rules excluded from the Zenodo bundle and repository
- [x] `data/raw/` and `data/interim/` outputs documented
- [x] Redistribution constraints for mined GitHub metadata acknowledged

## Git and GitHub release

- [x] All intended changes committed
- [x] Git tag created: `v1.0.0`
- [x] GitHub release / tag points at the Zenodo-aligned commit
- [ ] GitHub About description updated (optional; may require UI if API token lacks permission)

## Zenodo

- [x] Zenodo record published: [10.5281/zenodo.21794793](https://doi.org/10.5281/zenodo.21794793)
- [x] DOI propagated to `CITATION.cff`, `README.md`, `docs/reproducibility.md`, `RELEASE.md`
- [x] Git tag: `v1.0.0`

## Historical note

Older tags such as `v0.1.0-msr-contamination-audit` and IST-era metadata drafts are superseded by `v1.0.0` / PeerJ alignment. Do not cite them for the current release.
