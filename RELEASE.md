# Release notes

## v0.1.0-msr-contamination-audit

**Zenodo title:** VSDLC Mining Pilot

**Release name:** VSDLC Replication Package v0.1.0 — AI Instruction Artifact Contamination Audit

**DOI:** [10.5281/zenodo.20754778](https://doi.org/10.5281/zenodo.20754778)

**Git tag:** `v0.1.0-msr-contamination-audit`

### Description

Frozen replication package for the empirical study manuscript *Contamination in Repository Discovery Frames from AI-Instruction Artifacts*.
Supports replay of discovery-frame yield, annotation consensus, inter-coder reliability, query-family contamination (RQ2), EXCLUDE disagreement analysis, learned metadata baselines, and the functional-evidence proxy audit.

### Main contents

| Component | Description |
|-----------|-------------|
| Mining pipeline | Phase 1 seed search and Phase 2 repository filtering (`src/vsdlc_mining/`, `scripts/`) |
| Frozen datasets | Discovery candidates, eligible/excluded repositories, annotation exports, inspection worksheets (`data/`) |
| Evaluation scripts | $\kappa$ bootstrap, RQ2 query-family stats, EXCLUDE disagreement, learned baselines, proxy-audit comparison |
| Protocols | Exploratory codebook (schema v0.2), annotation and inspection worksheets |
| Documentation | `docs/reproducibility.md`, artifact ID map, rerun commands |

### Citation

```bibtex
@software{sanchez2026vsdlcMiningPilot,
  author    = {Andr{\'e}s, C{\'e}sar},
  title     = {{VSDLC Mining Pilot}},
  year      = {2026},
  version   = {v0.1.0-msr-contamination-audit},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20754778},
  url       = {https://doi.org/10.5281/zenodo.20754778},
  note      = {VSDLC Replication Package v0.1.0 --- AI Instruction Artifact Contamination Audit}
}
```
