# Related Work rebuild — deliverables

Research package produced 2026-07-22 for strengthening the State of the Art of the VSDLC / instruction-artifact frame-audit manuscript (IST/JSS track).

**This package does not rewrite the manuscript by default.** The proposed section is a draft for integration.

## Outputs

| # | File | Description |
|---|---|---|
| 1 | `related_work.bib` | Verified scholarly bibliography (60 entries) |
| 1b | `grey_literature.bib` | URL-verified AI-instruction primary docs |
| 2 | `literature_table.csv` | Title, Authors, Venue, Year, DOI, Area, Relation, Verified |
| 2b | `literature_table.md` | Markdown rendering of the table (compact) |
| 3 | `concept_map.md` | Mermaid concept map of literature clusters |
| 4 | `gap_analysis.md` | Solved / partial / unsolved / contribution boundary |
| 5 | `07_related_work_proposed.tex` | Proposed Related Work section |
| 6 | `references_to_remove.md` | Weak/redundant/outdated citations to demote |
| 7 | `top20_missing.md` | Ranked missing must-cites |
| — | `critical_reviews.md` | Per-paper critical notes |
| — | `verification_log.md` | DOI/URL verification + discards |
| — | `curated_corpus.json` | Machine-readable curated corpus |
| — | `search_raw.json` | Raw Crossref/OpenAlex search dump |

## Paper problem (for reading the package)

Discovery via AI-instruction file predicates ≠ analytic-population membership.  
Contribution focus: target-conditional contamination audit + consensus-protocol sensitivity + predicate-family structure + worksheet/replay reporting.

## Integration recommendation

1. Replace manuscript §Related Work with `07_related_work_proposed.tex` (after author polish).  
2. Merge `related_work.bib` + `grey_literature.bib` keys into the submission bibliography.  
3. Apply `references_to_remove.md` demotions.  
4. Add at least ranks 1–12 from `top20_missing.md` before resubmission.
