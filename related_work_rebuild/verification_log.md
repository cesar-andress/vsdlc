# Citation verification log

**Date:** 2026-07-22  
**Sources used:** Crossref Works API, OpenAlex Works API, direct URL HTTP checks, OpenReview for SWE-bench.  
**Policy:** Reject any citation that cannot be verified. Never invent titles/authors/DOIs.

## Summary

| Category | Count |
|---|---:|
| Curated peer-reviewed / proceedings entries in final corpus | 60 |
| Crossref-verified (`Verified: YES`) | 59 |
| OpenReview-verified (`Verified: YES-OPENREVIEW`) | 1 (SWE-bench) |
| Grey literature URL-verified (`Verified: YES-URL`) | 5 |
| Candidates discarded during rebuild | see below |

## Discarded candidates (explicit)

| Candidate DOI / claim | Reason discarded |
|---|---|
| `10.1007/s10664-017-9512-2` (wrong Munaiah DOI guess) | Crossref HTTP 404 |
| `10.1145/2382535.2382537` (alt Kaufman DOI) | Crossref HTTP 404; correct Kaufman DOI is `10.1145/2382577.2382579` |
| `10.1016/j.infsoft.2015.02.007` (wrong Petersen DOI) | Crossref HTTP 404; correct is `10.1016/j.infsof.2015.03.007` |
| `10.48550/arXiv.*` as journal DOIs | Crossref does not resolve these as publisher DOIs; used only if peer-reviewed version absent |
| `10.1145/3342528.3342668` | Crossref 404 (bad Software Heritage DOI guess) |
| `10.1145/3613905.3648422` | Crossref 404 (bad Verdecchia DOI guess) |
| `10.1109/saner58917.2023.00085` | Crossref 404 |
| Multiple OpenAlex high-cited hits with biology/medicine titles matching “annotation/engineered/leakage” | Irrelevant; discarded by title relevance filter |
| SEKE 2023 Copilot practices (`10.18293/seke2023-077`) | Verified in Crossref but **demoted** (weaker venue than CHI/CACM/OOPSLA Copilot studies already curated) |
| SSRN-only Verdecchia (`10.2139/ssrn.4493848`) | Prefer peer-reviewed IST version `10.1016/j.infsof.2023.107329` |
| Previously INVALID manuscript keys (`bird2020`, `gottschalk2023`, `baltes2022replication`, `fucci2018`, `hempel2020reproducibility`, `herbold2020`) | Remain rejected per forensic audit |

## Author metadata caveats (not discarded)

| Entry | Caveat |
|---|---|
| Howison 2004 (`10.1049/ic:20040467`) | Crossref currently lists abbreviated authorship (`Howison, J.`); Crowston is widely attributed in MSR literature. **DOI/title/year/venue verified**; authorship string taken from Crossref without invention. |
| Ahmed 2025 | Full author list as returned by Crossref at verification time; confirm camera-ready author string before camera-ready cite. |
| PHANTOM 2020 | Authors refreshed from Crossref (`Pickerill et al.` expanded in bib). |

## Grey literature URL checks

| Resource | URL | HTTP |
|---|---|---|
| AGENTS.md | https://agents.md/ | 200 |
| Anthropic MCP | https://www.anthropic.com/news/model-context-protocol | 200 |
| GitHub Copilot custom instructions | https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot | 200 |
| Claude Code memory docs | https://docs.anthropic.com/en/docs/claude-code/memory | 200 |
| Cursor rules | https://cursor.com/docs/rules | 200 (canonical; old `docs.cursor.com/context/rules` redirects) |
| SWE-bench OpenReview | https://openreview.net/forum?id=VTF8yNQM66 | 200 |

## Search strategy executed

Areas queried (Crossref + OpenAlex): MSR methodology; repository sampling; sampling bias; construct validity / threats; dataset contamination/leakage; repository discovery; reproducibility/artifacts; reporting guidelines; AI-assisted mining; AI instruction / promptware; SE datasets/benchmarks; human/LLM annotation; GitHub metadata quality.

Preferencing rule: journals first; elite conferences (ICSE/FSE/ASE/MSR/ICSME/SANER/ESEC) when highly influential; arXiv only if no peer-reviewed version existed (none required in the final curated set except SWE-bench’s OpenReview archival).
