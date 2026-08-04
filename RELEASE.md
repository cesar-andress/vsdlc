# Release notes

## v1.0.0: current Zenodo / GitHub release (2026-08-04)

**Companion manuscript (PeerJ Computer Science):** *Repository composition across AI-instruction file searches: a labelled study of an eligible GitHub frame*  
**Replication package title:** *Repository composition across AI-instruction file searches: a labelled study of an eligible GitHub frame (replication package)*  
**Git tag:** `v1.0.0`  
**Zenodo record:** [10.5281/zenodo.21794793](https://doi.org/10.5281/zenodo.21794793)

### Description

Frozen **replication-only** package for a labelled empirical study of public GitHub repositories retrieved by AI-instruction filename and path searches within one eligible labelled frame.
Supports replay of discovery/filter artefacts, Round-1 labelling worksheets, sensitivity tables, inter-pass concordance, predicate-family composition, metadata-only baselines, and the secondary inspection comparison.

This archive does **not** include manuscript LaTeX, bibliographies, cover letters, or editorial materials
(see `docs/ZENODO_PACKAGE.md`).

### Authors

| Author | ORCID | Email |
|---|---|---|
| César Andrés (corresponding) | 0009-0001-8968-3404 | cesar.andress@ucjc.edu |
| David Martín-Moncunill | 0000-0003-2422-9005 | david.martinm@ucjc.edu |
| José Manuel Baños | 0009-0004-9971-7390 | jmanuel.banos@ucjc.edu |

**Affiliation:** CRIA-BDHS Research Group, Escuela Politécnica Superior de Tecnología y Ciencia, Universidad Camilo José Cela, Spain

### Main contents

| Component | Description |
|---|---|
| Mining pipeline | Phase 1 seed search and Phase 2 repository filtering (`src/vsdlc_mining/`, `scripts/`) |
| Frozen datasets | Discovery candidates, eligible/excluded repositories, annotation exports, inspection worksheets (`data/`) |
| Evaluation scripts | Concordance / κ bootstrap, family composition, sensitivity tables, learned baselines, inspection comparison |
| Protocols | Worksheet schema v0.2, annotation and inspection protocols |
| Documentation | `docs/reproducibility.md`, artifact map, rerun commands |

### Canonical numeric outputs

JSON/CSV under `data/processed/` (e.g. sensitivity and concordance artefacts aligned with the frozen PeerJ manuscript empirics: human resolution 222/300; human-resolved non-target 126/222; plurality full-sample non-target 173/300 with 4 ties).

### Citation

```bibtex
@software{andres2026vsdlcReplication,
  author    = {Andr{\'e}s, C{\'e}sar and Mart{\'i}n-Moncunill, David and Ba\~nos, Jos{\'e} Manuel},
  title     = {{Repository composition across AI-instruction file searches: a labelled study of an eligible GitHub frame (replication package)}},
  year      = {2026},
  version   = {v1.0.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21794793},
  url       = {https://doi.org/10.5281/zenodo.21794793},
  note      = {Frozen replication package accompanying the PeerJ Computer Science manuscript}
}
```

### Prior tags

Historical tags such as `v0.1.0-msr-contamination-audit` refer to earlier package metadata and must not be used for the PeerJ / Zenodo v1.0.0 release.
