# Release notes

## v0.1.0-msr-contamination-audit — current Zenodo tag (2026-07-22)

**Companion manuscript (IST):** *Discovery-Frame Validity in Mining Software Repositories: Protocol-Dependent Contamination Estimands Demonstrated on AI-Instruction Path Predicates*  
**Replication package title:** *Discovery-Frame Validity Audit: Replication Package for the AI-Instruction Predicate Case*  
**Git tag:** `v0.1.0-msr-contamination-audit`  
**Zenodo record:** [10.5281/zenodo.21794793](https://doi.org/10.5281/zenodo.21794793)

### Description

Frozen **replication-only** package for the discovery-frame validity audit on one AI-instruction path-predicate GitHub frame.
Supports replay of discovery-frame yield, annotation consensus, complementary consensus-rule sensitivity,
inter-coder reliability, predicate-family contamination structure (RQ2), EXCLUDE disagreement analysis,
LLM third-coder characterization, learned metadata baselines, and the functional-evidence inspection diagnostic.

This archive does **not** include manuscript LaTeX, bibliographies, cover letters, or editorial materials
(see `docs/ZENODO_PACKAGE.md`).

### Authors

| Author | ORCID |
|--------|-------|
| César Andrés | 0009-0001-8968-3404 |
| David Martín-Moncunill | 0000-0003-2422-9005 |
| José Manuel Baños | 0009-0004-9971-7390 |

### Main contents

| Component | Description |
|-----------|-------------|
| Mining pipeline | Phase 1 seed search and Phase 2 repository filtering (`src/vsdlc_mining/`, `scripts/`) |
| Frozen datasets | Discovery candidates, eligible/excluded repositories, annotation exports, inspection worksheets (`data/`) |
| Evaluation scripts | κ bootstrap, RQ2 family stats, EXCLUDE disagreement, learned baselines, inspection comparison, consensus sensitivity, LLM adjudicator audit |
| Protocols | Worksheet schema v0.2, annotation and inspection protocols |
| Documentation | `docs/reproducibility.md`, artifact map, rerun commands |

### Canonical numeric outputs

JSON/CSV under `data/processed/` (e.g. `human_only_consensus_sensitivity.json`, `target_sensitivity_results.json`, `llm_third_adjudicator_audit.json`).
Aligned with the frozen manuscript empirics (human resolution 222/300; human-resolved non-target 126/222; plurality full-sample non-target 173/300 with 4 ties).

### Citation

```bibtex
@software{sanchez2026vsdlcMiningPilot,
  author    = {Andr{\'e}s, C{\'e}sar and Mart{\'i}n-Moncunill, David and Ba\~nos, Jos{\'e} Manuel},
  title     = {{Discovery-Frame Validity Audit: Replication Package for the AI-Instruction Predicate Case}},
  year      = {2026},
  version   = {v0.1.0-msr-contamination-audit},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21794793},
  url       = {https://doi.org/10.5281/zenodo.21794793},
  note      = {Frozen replication package for the IST discovery-frame validity audit}
}
```
