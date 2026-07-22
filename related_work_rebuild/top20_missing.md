# Top 20 most important references missing from the current paper

Ranked by **necessity for an IST/JSS-strength Related Work** given the paper’s contamination-audit contribution.  
All entries below are Crossref-verified unless noted.

| Rank | Paper | Year | Venue | DOI / URL | Why it is missing-critical |
|---:|---|---:|---|---|---|
| 1 | Munaiah et al., *Curating GitHub for engineered software projects* | 2017 | EMSE | 10.1007/s10664-017-9512-6 | Closest curation cousin; reviewers will ask why RepoReapers is not discussed. |
| 2 | Kalliamvakou et al., *An in-depth study of the promises and perils of mining GitHub* | 2015 | EMSE | 10.1007/s10664-015-9393-5 | Journal-strength version of the perils argument beyond the MSR 2014 cite. |
| 3 | Dabic et al., *Sampling Projects in GitHub for MSR Studies* | 2021 | MSR | 10.1109/MSR52588.2021.00074 | Direct sampling-methodology paper for GitHub MSR samples. |
| 4 | Ampatzoglou et al., *Identifying, categorizing and mitigating threats to validity…* | 2019 | IST | 10.1016/j.infsof.2018.10.006 | Same target journal family; ToV taxonomy expected by IST reviewers. |
| 5 | Verdecchia et al., *Threats to validity in software engineering research* | 2023 | IST | 10.1016/j.infsof.2023.107329 | Recent critical reflection on ToV practice; strengthens motivation. |
| 6 | Siegmund et al., *Views on Internal and External Validity in ESE* | 2015 | ICSE | 10.1109/ICSE.2015.24 | Documents disagreement on validity priorities; supports explicit analytic targets. |
| 7 | Lopes et al., *DéjàVu: a map of code duplicates on GitHub* | 2017 | PACMPL/OOPSLA | 10.1145/3133908 | Forces clean disambiguation of “contamination” senses. |
| 8 | Allamanis, *Adverse effects of code duplication in ML models of code* | 2019 | MAPS | 10.1145/3359591.3359735 | Shows evaluation inflation from duplication; adjacent contamination literature. |
| 9 | Ma et al., *World of Code* | 2019 | MSR | 10.1109/MSR.2019.00031 | Canonical discovery infrastructure beyond GitHub Search. |
| 10 | Pietri et al., *Software Heritage Graph Dataset* | 2019 | MSR | 10.1109/MSR.2019.00030 | Archive-scale reproducible discovery; complements CACM Software Heritage cite. |
| 11 | PHANTOM (Pickerill et al.), *Curating GitHub… time-series clustering* | 2020 | EMSE | 10.1007/s10664-020-09825-8 | Modern engineered-project curation after RepoReapers. |
| 12 | Golzadeh et al., *Ground-truth dataset… detecting bots in GitHub* | 2021 | JSS | 10.1016/j.jss.2021.110911 | Same journal family; exemplifies membership ground-truth construction. |
| 13 | Shepperd et al., *Data Quality… NASA Software Defect Datasets* | 2013 | TSE | 10.1109/TSE.2013.11 | Classic dataset-validation warning. |
| 14 | Herzig & Zeller, *The impact of tangled code changes* | 2013 | MSR | 10.1109/MSR.2013.6624018 | Construct-validity failure mode for mined labels. |
| 15 | Kapoor & Narayanan, *Leakage and the reproducibility crisis…* | 2023 | Patterns | 10.1016/j.patter.2023.100804 | Contemporary leakage/reproducibility argument useful for disambiguation. |
| 16 | González-Barahona & Robles, *On the reproducibility… repositories* | 2011/12 | EMSE | 10.1007/s10664-011-9181-9 | Foundational reproducibility-of-mining paper. |
| 17 | González-Barahona & Robles, *Revisiting the reproducibility…* | 2023 | IST | 10.1016/j.infsof.2023.107318 | Updated reproducibility evidence in IST. |
| 18 | Ahmed et al., *Can LLMs Replace Manual Annotation of SE Artifacts?* | 2025 | MSR | 10.1109/MSR66628.2025.00086 | Best current SE-specific LLM-annotation peer-reviewed study. |
| 19 | Gilardi et al., *ChatGPT outperforms crowd workers…* | 2023 | PNAS | 10.1073/pnas.2305016120 | Highly cited LLM-annotation evidence (with domain caveats). |
| 20 | Cosentino et al., *Systematic Mapping Study of Software Development With GitHub* | 2017 | IEEE Access | 10.1109/ACCESS.2017.2682323 | Maps GitHub-based SE research practice; good scene-setting. |

## Honorable mentions (21–28)

| Paper | DOI | Note |
|---|---|---|
| Hassan, *The road ahead for MSR* (2008) | 10.1109/FoSM.2008.4659248 | Seminal MSR agenda |
| Howison & Crowston, SourceForge perils (2004) | 10.1049/ic:20040467 | Pre-GitHub perils lineage |
| Spadini et al., PyDriller (2018) | 10.1145/3236024.3264598 | Mining tooling |
| Borges et al., GitHub popularity (2016) | 10.1109/ICSME.2016.31 | Metadata proxy fragility |
| Petersen et al., mapping guidelines (2015) | 10.1016/j.infsof.2015.03.007 | Reporting lineage |
| Jedlitschka & Pfahl (2005) | 10.1109/ISESE.2005.1541818 | Experiment reporting |
| Vaithilingam et al., Copilot usability (2022) | 10.1145/3491101.3519665 | Stronger HCI Copilot cite than Storey bots |
| Zheng et al., LLM-as-a-Judge (2023) | 10.52202/075280-2020 | If LLM adjudication is claimed |

## Intentionally *not* ranked as must-cite

- Product docs already present (`AGENTS.md`, Copilot/Cursor/Claude/MCP) — keep, do not count as “missing scholarly refs”.  
- SWE-bench — influential, but only if benchmark-construction is a RW subsection.  
- Promptware (Chen 2026) — already in submission bib; ensure it is used for the instruction-artifact cluster, not buried.
