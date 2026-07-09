# Zenodo upload metadata — IST submission release v1.0.0-ist

Use this checklist when publishing a **new version** on the existing record
[10.5281/zenodo.20754778](https://doi.org/10.5281/zenodo.20754778).

## Record fields

| Field | Value |
|-------|-------|
| **Upload type** | Software |
| **Title** | Replication Package: Evidence-Based Reporting for Repository Discovery Frames from AI-Instruction Artifacts |
| **Version** | v1.0.0-ist |
| **Publication date** | 2026-07-09 |
| **License** | MIT |
| **Access right** | Open access |

## Authors (all three manuscript authors, in this order)

| Name | ORCID | Affiliation |
|------|-------|-------------|
| César Andrés | 0009-0001-8968-3404 | Universidad Camilo José Cela, Spain |
| David Martín-Moncunill | 0000-0003-2422-9005 | Universidad Camilo José Cela, Spain |
| José Manuel Baños | 0009-0004-9971-7390 | Universidad Camilo José Cela, Spain |

**Fix required:** The live deposit (v0.1.0-msr-contamination-audit) lists only two authors with incorrect names (`Sánchez, César Andrés`; `Moncunill, David Martin`). José Manuel Baños is missing.

## Keywords

- empirical software engineering
- mining software repositories
- repository discovery
- sampling validity
- reporting guidelines
- reproducibility
- AI-instruction artifacts
- construct validity

## Description (paste into Zenodo)

Frozen replication package for the journal submission *Evidence-Based Reporting for Repository Discovery Frames from AI-Instruction Artifacts* (Information and Software Technology).

The archive contains:

- A reproducible GitHub audit protocol (discover, filter, annotate, inspect)
- Frozen study datasets and annotation worksheets
- Analysis scripts for consensus-protocol sensitivity, predicate-family structure, coder reliability, and functional-evidence concordance
- The author-identified manuscript PDF matching git tag `v1.0.0-ist`

The package supports independent replay under alternative analytic targets and coder-aggregation rules. Instruction-file search predicates retrieve candidates; they do not define study populations. Reported prevalence is target-conditional and consensus-protocol-dependent.

## Related publication

- **Journal:** Information and Software Technology (under review)
- **Manuscript title:** Evidence-Based Reporting for Repository Discovery Frames from AI-Instruction Artifacts

## Release notes (paste into Zenodo version notes)

### v1.0.0-ist (2026-07-09)

IST submission release aligned with git tag `v1.0.0-ist`.

**Added**
- Consensus-label scripts and sensitivity outputs
- LLM third-coder characterization audit
- Updated processed datasets and manuscript table sources
- Author-identified manuscript PDF

**Fixed**
- Author metadata: three authors with correct names and ORCIDs
- Documentation aligned with IST methodological framing

**Supersedes**
- v0.1.0-msr-contamination-audit (2026-06-18)

## File to upload

```
release/zenodo-v1.0.0-ist.tar.gz
```

Built by:

```bash
./scripts/build_zenodo_release.sh
```

## Post-upload verification

- [ ] All three authors visible on the Zenodo record
- [ ] Version shows `v1.0.0-ist` as latest
- [ ] Description and keywords match this document
- [ ] Archive contains `manuscript/main.pdf`, `vsdlc/`, `CITATION.cff`, `RELEASE.md`
- [ ] DOI `10.5281/zenodo.20754778` still resolves (same concept DOI)
