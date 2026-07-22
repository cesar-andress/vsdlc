# BibTeX / box-warning fix (2026-07-22)

- Root cause of missing `ralph2021standards`: Unicode NBSP (U+00A0) in `vaithilingam2022expectation` title broke BibTeX parsing of later entries.
- Added Crossref `pages` for previously empty-page inproceedings.
- Local `papers/` also: RQ1 table squeeze + `\hfuzz=3pt` for elsarticle 2.6pt header overfull.

