# Zenodo release checklist — VSDLC Mining Pilot

Use this checklist before creating a Git tag, GitHub release, or Zenodo upload for this research artifact. **Do not publish until every required item is complete.**

## Code quality

- [ ] `python -m pip install -e ".[dev]"` succeeds on a clean environment (Python 3.11+)
- [ ] `pytest` passes with zero failures
- [ ] `ruff check src tests scripts` passes (or documented exceptions recorded)
- [ ] `mypy src/vsdlc_mining` passes (or documented exceptions recorded)

## Documentation

- [ ] `README.md` describes the mining pilot, provenance research direction, and reproducible artifact
- [ ] `docs/reproducibility.md` is up to date
- [ ] Repository traceability dataset schemas are documented in README or `docs/`

## Licensing and citation metadata

- [ ] `LICENSE` reviewed (MIT unless project policy changes)
- [ ] `CITATION.cff` authors, title, version, and date-released are correct
- [ ] `CITATION.cff` repository URL placeholder replaced with final public URL
- [ ] `CITATION.cff` DOI placeholder replaced after Zenodo minting
- [ ] No false claim that a DOI already exists in README or other documentation

## Versioning

- [ ] Version bumped consistently in:
  - `pyproject.toml`
  - `src/vsdlc_mining/__init__.py`
  - `CITATION.cff`
- [ ] `date-released` in `CITATION.cff` matches the Zenodo release date

## Data policy

- [ ] Large/raw data policy stated (what is included in Zenodo bundle vs. regenerated locally)
- [ ] No secrets, tokens, or `.env` files in the release archive
- [ ] `.cursor/` IDE rules excluded from the Zenodo bundle and repository
- [ ] `data/raw/` and `data/interim/` outputs documented (eligible/excluded/summary files)
- [ ] Redistribution constraints for mined GitHub metadata acknowledged

## Git and GitHub release

- [ ] All intended changes committed
- [ ] Git tag created (e.g. `v0.1.0`)
- [ ] GitHub release notes prepared (artifact summary, outputs, how to cite)
- [ ] GitHub release created from the tag

## Zenodo

- [ ] Zenodo account linked to GitHub (or upload prepared manually)
- [ ] Zenodo record draft reviewed (title, authors, license, files)
- [ ] DOI reserved or minted
- [ ] DOI propagated back to `CITATION.cff` and README citation section
- [ ] Zenodo record published (only when intentional)

## Post-release

- [ ] Archive copy of generated datasets uploaded or checksums recorded
- [ ] External references to this artifact updated with the final DOI (if any)
