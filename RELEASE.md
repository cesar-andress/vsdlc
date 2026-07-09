# Release notes

## v1.0.0-ist — IST submission release (2026-07-09)

**Journal:** *Information and Software Technology* (Elsevier)  
**Manuscript title:** *Evidence-Based Reporting for Repository Discovery Frames from AI-Instruction Artifacts*  
**Git tag (repository root):** `v1.0.0-ist`  
**Zenodo record:** [10.5281/zenodo.20754778](https://doi.org/10.5281/zenodo.20754778)  
**Zenodo version:** `v1.0.0-ist` (upload pending — replaces published `v0.1.0-msr-contamination-audit`)

### Description

Frozen replication package for the IST journal submission on repository-discovery reporting methodology.
Supports replay of discovery-frame yield, annotation consensus, complementary consensus-rule sensitivity,
inter-coder reliability, predicate-family contamination structure (RQ2), EXCLUDE disagreement analysis,
LLM third-coder characterization, learned metadata baselines, and the functional-evidence proxy audit.

### Authors (all three manuscript authors)

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
| Evaluation scripts | $\kappa$ bootstrap, RQ2 query-family stats, EXCLUDE disagreement, learned baselines, proxy-audit comparison, consensus sensitivity, LLM adjudicator audit |
| Protocols | Worksheet schema v0.2, annotation and inspection protocols |
| Manuscript | `manuscript/main.pdf` — author-identified PDF matching `submission-ist-v1.0` |
| Documentation | `docs/reproducibility.md`, artifact ID map, rerun commands |

### Changes from v0.1.0-msr-contamination-audit

- Added consensus-label scripts and sensitivity outputs (`compute_majority_label.py`, `analyze_human_only_consensus_sensitivity.py`, `analyze_llm_third_adjudicator.py`)
- Updated processed datasets and manuscript table sources
- Aligned metadata with three-author IST manuscript (names, ORCIDs, affiliations)
- Bundled latest author-identified manuscript PDF
- Removed EMSE submission artifacts from the IST release bundle

### Citation

```bibtex
@software{sanchez2026vsdlcMiningPilot,
  author    = {Andr{\'e}s, C{\'e}sar and Mart{\'i}n-Moncunill, David and Ba\~nos, Jos{\'e} Manuel},
  title     = {{Replication Package: Evidence-Based Reporting for Repository Discovery Frames from AI-Instruction Artifacts}},
  year      = {2026},
  version   = {v1.0.0-ist},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20754778},
  url       = {https://doi.org/10.5281/zenodo.20754778},
  note      = {Frozen replication package for IST journal submission}
}
```

---

## v0.1.0-msr-contamination-audit — archived (2026-06-18)

Superseded by `v1.0.0-ist`. The live Zenodo deposit still serves this version until the IST upload is published.
