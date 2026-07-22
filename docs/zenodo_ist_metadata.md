# Zenodo upload metadata — replication package

Use this checklist when updating the existing record
[10.5281/zenodo.20754778](https://doi.org/10.5281/zenodo.20754778).

## Record fields

| Field | Value |
|-------|-------|
| **Upload type** | Software |
| **Title** | Discovery-Frame Validity Audit: Replication Package for the AI-Instruction Predicate Case |
| **Version** | v0.1.0-msr-contamination-audit |
| **Publication date** | 2026-07-22 |
| **License** | MIT |
| **Access right** | Open access |

## Authors (in this order)

| Name | ORCID | Affiliation |
|------|-------|-------------|
| César Andrés | 0009-0001-8968-3404 | Universidad Camilo José Cela, Spain |
| David Martín-Moncunill | 0000-0003-2422-9005 | Universidad Camilo José Cela, Spain |
| José Manuel Baños | 0009-0004-9971-7390 | Universidad Camilo José Cela, Spain |

## Keywords

- empirical software engineering
- mining software repositories
- discovery frames
- sampling validity
- construct validity
- reproducibility
- AI-instruction path predicates

## Description (paste into Zenodo)

Frozen replication package for the discovery-frame validity audit demonstrated on one public GitHub frame of AI-instruction path predicates (companion *Information and Software Technology* manuscript).

The archive contains:

- A reproducible GitHub audit protocol (discover, filter, annotate, inspect)
- Frozen study datasets and annotation worksheets
- Analysis scripts for consensus-protocol sensitivity, predicate-family structure, coder reliability, and functional-evidence concordance
- JSON/CSV outputs for independent replay

Replication material only: no manuscript LaTeX, PDFs, bibliographies, or editorial documents.

Reported prevalence is target-conditional and consensus-protocol-dependent. Instruction-file search predicates retrieve candidates; they do not define study populations.

## Related publication

- **Journal:** Information and Software Technology (under review)
- **Manuscript title:** Discovery-Frame Validity in Mining Software Repositories: Protocol-Dependent Contamination Estimands Demonstrated on AI-Instruction Path Predicates

## Post-upload verification

- [ ] All three authors visible on the Zenodo record
- [ ] Version / git tag `v0.1.0-msr-contamination-audit` matches this release
- [ ] Description and keywords match this document
- [ ] Archive contains `vsdlc` sources, `CITATION.cff`, `RELEASE.md` — **no** manuscript PDF/LaTeX
- [ ] DOI `10.5281/zenodo.20754778` still resolves (same concept DOI)
