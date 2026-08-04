# Repository Composition Across AI-Instruction File Searches — Replication Package

**Companion to:** Repository Composition Across AI-Instruction File Searches: A Labelled Study of an Eligible GitHub Frame  
**Venue:** PeerJ Computer Science (submitted)  
**Zenodo DOI:** [10.5281/zenodo.21794793](https://doi.org/10.5281/zenodo.21794793)  
**Version:** v1.0.0  
**License:** MIT

Frozen replication package for a labelled empirical study of public GitHub repositories retrieved by AI-instruction filename and path searches. The package supports replaying discovery/filter artefacts, Round-1 labelling worksheets, sensitivity tables, metadata-only baselines, and secondary inspection outputs within one eligible labelled analysis frame.

**Authors:** César Andrés, David Martín-Moncunill, and José Manuel Baños  
**Affiliation:** CRIA-BDHS Research Group, Escuela Politécnica Superior de Tecnología y Ciencia, Universidad Camilo José Cela, Spain

## What this artifact contains

| Component | Description |
|-----------|-------------|
| Mining pipeline | Python package for seed search and repository filtering |
| Frozen datasets | JSONL and interim filter outputs under `data/` |
| Annotation materials | Worksheets, codebook (schema v0.2), annotation and inspection protocols |
| Analysis scripts | Sensitivity, concordance, classifier, and figure/table regeneration helpers |
| Documentation | Reproducibility notes under `docs/` |

## Installation

Requires Python **3.11+** and a GitHub personal access token for live re-discovery (frozen artefacts do not require a token to inspect).

```bash
cd vsdlc
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
export GITHUB_TOKEN="..."   # required only for live API re-runs — never commit tokens
```

## Citation

Cite the PeerJ manuscript (when available) and this Zenodo record. See [`CITATION.cff`](CITATION.cff).

```
Andrés C, Martín-Moncunill D, Baños JM. 2026. Repository Composition Across
AI-Instruction File Searches: A Labelled Study of an Eligible GitHub Frame.
Manuscript submitted to PeerJ Computer Science.
Replication package: https://doi.org/10.5281/zenodo.21794793
```

## License

MIT — see [`LICENSE`](LICENSE).
