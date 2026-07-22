# State of the Art Investigation Report

**Purpose:** Systematic, verified literature base to support a future rewrite of the Related Work section (IST).
**Manuscript status:** Not modified.
**Investigation date:** 2026-07-22
**Verification policy:** Every scholarly DOI checked via Crossref Works API; grey sources via HTTP URL check; SWE-bench via OpenReview. Unverifiable candidates rejected.

## 0. Target paper (for relevance judgments)

This investigation supports an empirical methodology paper that:

- discovers GitHub repositories via **AI-instruction-file predicates** (e.g., `AGENTS.md`, Cursor rules, Copilot instructions);
- defines **contamination** as *satisfied search predicate ∧ outside the stated analytic population*;
- audits **consensus-protocol sensitivity**, **predicate-family structure**, coder disagreement, and inspection concordance;
- releases a worksheet protocol, frozen labels, and replay scripts.

Novelty must **not** be overstated: GitHub perils and sampling guidelines are known. The open gap is the **operational audit** above.

## 1. Search method

| Item | Detail |
|---|---|
| Sources used in this run | Crossref (primary bibliographic + DOI verification), OpenAlex (with API key for abstracts/metadata), Semantic Scholar (abstract fallback), OpenReview (SWE-bench), direct URL checks (grey literature) |
| Sources requested but not directly queried as proprietary UIs | Scopus, Web of Science, IEEE Xplore UI, ACM DL UI, SpringerLink UI, ScienceDirect UI, Wiley UI — coverage approximated via Crossref/OpenAlex publisher records from those venues |
| Topics | 30 (listed below) |
| arXiv policy | Used only if no peer-reviewed version exists; final curated set prefers peer-reviewed/OpenReview |
| Unique DOIs seen in topic search | 567 |
| DOI-verified then quality-curated records | 136 |
| Records with recoverable abstract | 122 |
| Recommended cite (YES*) | 119 |

### 1.1 Topic list

1. Mining Software Repositories (MSR)
2. Repository discovery
3. Repository sampling
4. Sampling methodology
5. Sampling bias
6. Construct validity
7. Internal validity
8. External validity
9. Dataset contamination
10. GitHub repository mining
11. Dataset construction
12. Benchmark construction
13. Research artifacts
14. Reproducibility
15. Reporting guidelines
16. Metadata quality
17. Human annotation
18. Consensus annotation
19. Multi-annotator protocols
20. LLM-assisted annotation
21. AI-assisted annotation
22. AI instruction artifacts
23. AGENTS.md
24. Cursor Rules
25. Claude.md
26. Copilot Instructions
27. Promptware
28. MCP
29. Repository discovery frames
30. Software Engineering methodology

## 2. Executive gap synthesis

### Already solved
- Awareness that forge/GitHub mining is perilous (Howison; Kalliamvakou).
- Sampling-frame/population reporting guidelines (Baltes & Ralph).
- Engineered-project curation classifiers (Munaiah; PHANTOM).
- Discovery/retrieval infrastructure (GHTorrent; World of Code; Software Heritage).
- Dataset/label validation culture (Shepperd; Herbold; Herzig).
- Leakage/duplication contamination for ML evaluations (Kaufman; Lopes; Allamanis; Kapoor).
- Artifact/reproducibility norms (González-Barahona; Heumüller; Winter; Liu).

### Partially solved
- Operational sample–target audits for *new* discovery predicates.
- Threats-to-validity discourse without instruction-frame worksheets (Ampatzoglou; Verdecchia; Siegmund).
- LLM-assisted annotation transfer to SE membership labels (Gilardi vs Ahmed — conflicting).

### Not solved (contribution boundary)
No verified peer-reviewed study jointly delivers: AI-instruction path-predicate discovery + target-conditional contamination + consensus-protocol sensitivity of rates + predicate-family structure + tiered inspection + reusable worksheet/replay package.

### Conflicting evidence
- **LLM annotation:** Gilardi et al. (2023) optimistic on crowd-comparable annotation; Ahmed et al. (2025) more cautious for SE artifacts.
- **Validity priorities:** Siegmund et al. (2015) show community disagreement on internal vs external validity.

---

## 3. Papers by research area

Each entry includes the requested fields. Papers mapped to multiple topics are repeated under each relevant topic.

## Topic 1. Mining Software Repositories (MSR)

_Verified entries in this topic after curation: **13**_

### 1. Mining Software Repositories to Assist Developers and Support Managers

- **Authors:** Hassan, Ahmed
- **Venue:** 2006 22nd IEEE International Conference on Software Maintenance
- **Year:** 2006
- **DOI:** `10.1109/icsm.2006.38`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icsm.2006.38
- **Verification:** YES (Crossref)
- **Abstract:** Software repositories (such as source control repositories) contain a wealth of valuable information regarding the evolutionary history of a software project. This paper presents approaches and tools which mine and transform static record keeping software repositories to active repositories used by researchers to gain empirically based understanding of software development, and by practitioners to predict, plan and understand various aspects of their project. Our work is validated empirically using data based on over 60 years of development history for several open source projects
- **Main contribution:** Software repositories (such as source control repositories) contain a wealth of valuable information regarding the evolutionary history of a software project. This paper presents approaches and tools which mine and transform static record keeping software repositories to active repositories used by researchers to gain empirically based understanding of software development, and by practitioners to predict, plan and understand various aspects o...
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 2. Mining software repositories with CVSgrab

- **Authors:** Voinea, Lucian, Telea, Alexandru
- **Venue:** Proceedings of the 2006 international workshop on Mining software repositories
- **Year:** 2006
- **DOI:** `10.1145/1137983.1138024`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/1137983.1138024
- **Verification:** YES (Crossref)
- **Abstract:** In this paper we address the process and team analysis categories of the MSR Mining Challenge 2006. We use our CVSgrab tool to acquire the data and interactively visualize the evolution of ArgoUML and PostgreSQL, in order to answer three relevant questions. We conclude summarizing the strong and weak points of using CVSgrab for mining large software repositories.
- **Main contribution:** In this paper we address the process and team analysis categories of the MSR Mining Challenge 2006. We use our CVSgrab tool to acquire the data and interactively visualize the evolution of ArgoUML and PostgreSQL, in order to answer three relevant questions.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. The road ahead for Mining Software Repositories

- **Authors:** Hassan, Ahmed E.
- **Venue:** 2008 Frontiers of Software Maintenance
- **Year:** 2008
- **DOI:** `10.1109/fosm.2008.4659248`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/fosm.2008.4659248
- **Verification:** YES (Crossref)
- **Abstract:** Source control repositories, bug repositories, archived communications, deployment logs, and code repositories are examples of software repositories that are commonly available for most software projects. The mining software repositories (MSR) field analyzes and cross-links the rich data available in these repositories to uncover interesting and actionable information about software systems. By transforming these repositories from static record-keeping ones into active repositories, we can guide decision processes in modern software projects. For example, data in source control repositories, traditionally used to archive code, could be linked with data in bug repositories to help practitioners propagate complex changes and to warn them about risky code based on prior changes and bugs. In this paper, we present a brief history of the MSR field and discuss several recent achievements and results of using MSR techniques to support software research and practice. We then discuss the various opportunities and challenges that lie in the road ahead for this important and emerging field.
- **Main contribution:** Source control repositories, bug repositories, archived communications, deployment logs, and code repositories are examples of software repositories that are commonly available for most software projects. The mining software repositories (MSR) field analyzes and cross-links the rich data available in these repositories to uncover interesting and actionable information about software systems.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. MapReduce as a general framework to support research in Mining Software Repositories (MSR)

- **Authors:** Weiyi Shang, Zhen Ming Jiang, Adams, Bram, Hassan, Ahmed E.
- **Venue:** 2009 6th IEEE International Working Conference on Mining Software Repositories
- **Year:** 2009
- **DOI:** `10.1109/msr.2009.5069477`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2009.5069477
- **Verification:** YES (Crossref)
- **Abstract:** Researchers continue to demonstrate the benefits of Mining Software Repositories (MSR) for supporting software development and research activities. However, as the mining process is time and resource intensive, they often create their own distributed platforms and use various optimizations to speed up and scale up their analysis. These platforms are project-specific, hard to reuse, and offer minimal debugging and deployment support. In this paper, we propose the use of MapReduce, a distributed computing platform, to support research in MSR. As a proof-of-concept, we migrate J-REX, an optimized evolutionary code extractor, to run on Hadoop, an open source implementation of MapReduce. Through a case study on the source control repositories of the Eclipse, BIRT and Datatools projects, we demonstrate that the migration effort to MapReduce is minimal and that the benefits are significant, as running time of the migrated J-REX is only 30% to 50% of the original J-REX's. This paper documents our experience with the migration, and highlights the benefits and challenges of the MapReduce framework in the MSR community.
- **Main contribution:** Researchers continue to demonstrate the benefits of Mining Software Repositories (MSR) for supporting software development and research activities. However, as the mining process is time and resource intensive, they often create their own distributed platforms and use various optimizations to speed up and scale up their analysis.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 5. On mining data across software repositories

- **Authors:** Anbalagan, Prasanth, Vouk, Mladen
- **Venue:** 2009 6th IEEE International Working Conference on Mining Software Repositories
- **Year:** 2009
- **DOI:** `10.1109/msr.2009.5069498`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2009.5069498
- **Verification:** YES (Crossref)
- **Abstract:** Software repositories provide abundance of valuable information about open source projects. With the increase in the size of the data maintained by the repositories, automated extraction of such data from individual repositories, as well as of linked information across repositories, has become a necessity. In this paper we describe a framework that uses web scraping to automatically mine repositories and link information across repositories. We discuss two implementations of the framework. In the first implementation, we automatically identify and collect security problem reports from project repositories that deploy the Bugzilla bug tracker using related vulnerability information from the National Vulnerability Database. In the second, we collect security problem reports for projects that deploy the Launchpad bug tracker along with related vulnerability information from the National Vulnerability Database. We have evaluated our tool on various releases of Fedora, Ubuntu, Suse, RedHat, and Firefox projects. The percentage of security bugs identified using our tool is consistent with that reported by other researchers.
- **Main contribution:** Software repositories provide abundance of valuable information about open source projects. With the increase in the size of the data maintained by the repositories, automated extraction of such data from individual repositories, as well as of linked information across repositories, has become a necessity.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 6. GHTorrent: Github's data from a firehose

- **Authors:** Gousios, Georgios, Spinellis, D.
- **Venue:** 2012 9th IEEE Working Conference on Mining Software Repositories (MSR)
- **Year:** 2012
- **DOI:** `10.1109/msr.2012.6224294`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2012.6224294
- **Verification:** YES (Crossref)
- **Abstract:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform. GitHub provides an extensive REST API, which enables researchers to retrieve both the commits to the projects' repositories and events generated through user actions on project resources. GHTorrent aims to create a scalable off line mirror of GitHub's event streams and persistent data, and offer it to the research community as a service. In this paper, we present the project's design and initial implementation and demonstrate how the provided datasets can be queried and processed.
- **Main contribution:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 7. Is mining software repositories data science? (keynote)

- **Authors:** Mockus, Audris
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2600728`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2600728
- **Verification:** YES (Crossref)
- **Abstract:** Trick question: what is Data Science? The collection and use of low-veracity data in software repositories and other operational support systems is exploding. It is, therefore, imperative to elucidate basic principles of how such data comes into being and what it means. Are there practices of constructing software data analysis tools that could raise the integrity of their results despite the problematic nature of the underlying data? The talk explores the basic nature of data in operational support systems and considers approaches to develop engineering practices for software mining tools.
- **Main contribution:** Trick question: what is Data Science? The collection and use of low-veracity data in software repositories and other operational support systems is exploding.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 8. Lean GHTorrent: GitHub data on demand

- **Authors:** Gousios, Georgios, Vasilescu, Bogdan, Serebrenik, Alexander, Zaidman, Andy
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597126`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597126
- **Verification:** YES (Crossref)
- **Abstract:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it. GitHub offers a tremendous research potential. For instance, it is a flagship for current open source development, a place for developers to showcase their expertise to peers or potential recruiters, and the platform where social coding features or pull requests emerged. However, GitHub data is, to date, largely underexplored. To facilitate studies of GitHub, we have created GHTorrent, a scalable, queriable, offline mirror of the data offered through the GitHub REST API. In this paper we present a novel feature of GHTorrent designed to offer customisable data dumps on demand. The new GHTorrent data-on-demand service offers users the possibility to request via a web form up-to-date GHTorrent data dumps for any collection of GitHub repositories. We hope that by offering customisable GHTorrent data dumps we will not only lower the "barrier for entry" even further for researchers interested in mining GitHub data (thus encourage researchers to intensify their mining efforts), but also enhance the replicability of GitHub studies (since a snapshot of the data on which the results were obtained can now easily accompany each study).
- **Main contribution:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 9. Raising MSR researchers

- **Authors:** Hassan, Ahmed E.
- **Venue:** Proceedings of the 13th International Conference on Mining Software Repositories
- **Year:** 2016
- **DOI:** `10.1145/2901739.2901780`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2901739.2901780
- **Verification:** YES (Crossref)
- **Abstract:** This experience report discusses my views on raising MSR researchers through a graduate-level seminar course. A key goal of this report is to kick start a discussion on this topic within our growing community. A discussion for which there is rarely a suitable venue. Yet, it is an essential discussion to have as a community grows, especially given the rapid growth of the MSR community over the past decade.
- **Main contribution:** This experience report discusses my views on raising MSR researchers through a graduate-level seminar course. A key goal of this report is to kick start a discussion on this topic within our growing community.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 10. A Systematic Mapping Study of Software Development With GitHub

- **Authors:** Cosentino, Valerio, Canovas Izquierdo, Javier L., Cabot, Jordi
- **Venue:** IEEE Access
- **Year:** 2017
- **DOI:** `10.1109/access.2017.2682323`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/access.2017.2682323
- **Verification:** YES (Crossref)
- **Abstract:** Context: GitHub, nowadays the most popular social coding platform, has become the reference for mining Open Source repositories, a growing research trend aiming at learning from previous software projects to improve the development of new ones. In the last years, a considerable amount of research papers have been published reporting findings based on data mined from GitHub. As the community continues to deepen in its understanding of software engineering thanks to the analysis performed on this platform, we believe that it is worthwhile to reflect on how research papers have addressed the task of mining GitHub and what findings they have reported. Objective: The main objective of this paper is to identify the quantity, topic, and empirical methods of research works, targeting the analysis of how software development practices are influenced by the use of a distributed social coding platform like GitHub. Method: A systematic mapping study was conducted with four research questions and assessed 80 publications from 2009 to 2016. Results: Most works focused on the interaction around coding-related tasks and project communities. We also identified some concerns about how reliable were these results based on the fact that, overall, papers used small data sets and poor sampling techniques, employed a scarce variety of methodologies and/or were hard to replicate. Conclusions: This paper attested the high activity of research work around the field of Open Source collaboration, especially in the software domain, revealed a set of shortcomings and proposed some actions to mitigate them. We hope that this paper can also create the basis for additional studies on other collaborative activities (like book writing for instance) that are also moving to GitHub.
- **Main contribution:** Context: GitHub, nowadays the most popular social coding platform, has become the reference for mining Open Source repositories, a growing research trend aiming at learning from previous software projects to improve the development of new ones. In the last years, a considerable amount of research papers have been published reporting findings based on data mined from GitHub.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 11. PyDriller: Python framework for mining software repositories

- **Authors:** Spadini, Davide, Aniche, Maurício, Bacchelli, Alberto
- **Venue:** Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
- **Year:** 2018
- **DOI:** `10.1145/3236024.3264598`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3236024.3264598
- **Verification:** YES (Crossref)
- **Abstract:** Software repositories contain historical and valuable information about the overall development of software systems. Mining software repositories (MSR) is nowadays considered one of the most interesting growing fields within software engineering. MSR focuses on extracting and analyzing data available in software repositories to uncover interesting, useful, and actionable information about the system. Even though MSR plays an important role in software engineering research, few tools have been created and made public to support developers in extracting information from Git repository. In this paper, we present PyDriller, a Python Framework that eases the process of mining Git. We compare our tool against the state-of-the-art Python Framework GitPython, demonstrating that PyDriller can achieve the same results with, on average, 50% less LOC and significantly lower complexity. URL: https://github.com/ishepard/pydriller Materials: https://doi.org/10.5281/zenodo.1327363 Pre-print: https://doi.org/10.5281/zenodo.1327411
- **Main contribution:** Software repositories contain historical and valuable information about the overall development of software systems. Mining software repositories (MSR) is nowadays considered one of the most interesting growing fields within software engineering.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR). Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 12. World of Code: An Infrastructure for Mining the Universe of Open Source VCS Data

- **Authors:** Ma, Yuxing, Bogart, Chris, Amreen, Sadika, Zaretzki, Russell, Mockus, Audris
- **Venue:** 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)
- **Year:** 2019
- **DOI:** `10.1109/msr.2019.00031`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2019.00031
- **Verification:** YES (Crossref)
- **Abstract:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flows? To answer such questions we a) create a very large and frequently updated collection of version control data for FLOSS projects named World of Code (WoC) and b) provide basic tools for conducting research that depends on measuring interdependencies among all FLOSS projects. Our current WoC implementation is capable of being updated on a monthly basis and contains over 12B git objects. To evaluate its research potential and to create vignettes for its usage, we employ WoC in conducting several research tasks. In particular, we find that it is capable of supporting trend evaluation, ecosystem measurement, and the determination of package usage. We expect WoC to spur investigation into global properties of OSS development leading to increased resiliency of the entire OSS ecosystem. Our infrastructure facilitates the discovery of key technical dependencies, code flow, and social networks that provide the basis to determine the structure and evolution of the relationships that drive FLOSS activities and innovation.
- **Main contribution:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flows?
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 13. Large Language Models for Software Engineering: A Systematic Literature Review

- **Authors:** Hou, Xinyi, Zhao, Yanjie, Liu, Yue, Yang, Zhou, Wang, Kailong, Li, Li, Luo, Xiapu, Lo, David, Grundy, John, Wang, Haoyu
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2024
- **DOI:** `10.1145/3695988`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3695988
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) have significantly impacted numerous domains, including Software Engineering (SE). Many recent publications have explored LLMs applied to various SE tasks. Nevertheless, a comprehensive understanding of the application, effects, and possible limitations of LLMs on SE is still in its early stages. To bridge this gap, we conducted a Systematic Literature Review (SLR) on LLM4SE, with a particular focus on understanding how LLMs can be exploited to optimize processes and outcomes. We selected and analyzed 395 research articles from January 2017 to January 2024 to answer four key Research Questions (RQs). In RQ1, we categorize different LLMs that have been employed in SE tasks, characterizing their distinctive features and uses. In RQ2, we analyze the methods used in data collection, pre-processing, and application, highlighting the role of well-curated datasets for successful LLM for SE implementation. RQ3 investigates the strategies employed to optimize and evaluate the performance of LLMs in SE. Finally, RQ4 examines the specific SE tasks where LLMs have shown success to date, illustrating their practical contributions to the field. From the answers to these RQs, we discuss the current state-of-the-art and trends, identifying gaps in existing research, and highlighting promising areas for future study. Our artifacts are publicly available at https://github.com/security-pride/LLM4SE_SLR .
- **Main contribution:** Large Language Models (LLMs) have significantly impacted numerous domains, including Software Engineering (SE). Many recent publications have explored LLMs applied to various SE tasks.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work


## Topic 2. Repository discovery

_Verified entries in this topic after curation: **9**_

### 1. GHTorrent: Github's data from a firehose

- **Authors:** Gousios, Georgios, Spinellis, D.
- **Venue:** 2012 9th IEEE Working Conference on Mining Software Repositories (MSR)
- **Year:** 2012
- **DOI:** `10.1109/msr.2012.6224294`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2012.6224294
- **Verification:** YES (Crossref)
- **Abstract:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform. GitHub provides an extensive REST API, which enables researchers to retrieve both the commits to the projects' repositories and events generated through user actions on project resources. GHTorrent aims to create a scalable off line mirror of GitHub's event streams and persistent data, and offer it to the research community as a service. In this paper, we present the project's design and initial implementation and demonstrate how the provided datasets can be queried and processed.
- **Main contribution:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 2. Lean GHTorrent: GitHub data on demand

- **Authors:** Gousios, Georgios, Vasilescu, Bogdan, Serebrenik, Alexander, Zaidman, Andy
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597126`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597126
- **Verification:** YES (Crossref)
- **Abstract:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it. GitHub offers a tremendous research potential. For instance, it is a flagship for current open source development, a place for developers to showcase their expertise to peers or potential recruiters, and the platform where social coding features or pull requests emerged. However, GitHub data is, to date, largely underexplored. To facilitate studies of GitHub, we have created GHTorrent, a scalable, queriable, offline mirror of the data offered through the GitHub REST API. In this paper we present a novel feature of GHTorrent designed to offer customisable data dumps on demand. The new GHTorrent data-on-demand service offers users the possibility to request via a web form up-to-date GHTorrent data dumps for any collection of GitHub repositories. We hope that by offering customisable GHTorrent data dumps we will not only lower the "barrier for entry" even further for researchers interested in mining GitHub data (thus encourage researchers to intensify their mining efforts), but also enhance the replicability of GitHub studies (since a snapshot of the data on which the results were obtained can now easily accompany each study).
- **Main contribution:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 3. Building the universal archive of source code

- **Authors:** Abramatic, Jean-François, Di Cosmo, Roberto, Zacchiroli, Stefano
- **Venue:** Communications of the ACM
- **Year:** 2018
- **DOI:** `10.1145/3183558`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3183558
- **Verification:** YES (Crossref)
- **Abstract:** A global collaborative project for the benefit of all.
- **Main contribution:** A global collaborative project for the benefit of all.
- **Relation with our paper:** Topic mapping: Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. The Software Heritage Graph Dataset: Public Software Development Under One Roof

- **Authors:** Pietri, Antoine, Spinellis, Diomidis, Zacchiroli, Stefano
- **Venue:** 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)
- **Year:** 2019
- **DOI:** `10.1109/msr.2019.00030`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2019.00030
- **Verification:** YES (Crossref)
- **Abstract:** Software Heritage is the largest existing public archive of software source code and accompanying development history: it currently spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects. This paper introduces the Software Heritage graph dataset: a fully-deduplicated Merkle DAG representation of the Software Heritage archive. The dataset links together file content identifiers, source code directories, Version Control System (VCS) commits tracking evolution over time, up to the full states of VCS repositories as observed by Software Heritage during periodic crawls. The dataset's contents come from major development forges (including GitHub and GitLab), FOSS distributions (e.g., Debian), and language-specific package managers (e.g., PyPI). Crawling information is also included, providing timestamps about when and where all archived source code artifacts have been observed in the wild. The Software Heritage graph dataset is available in multiple formats, including downloadable CSV dumps and Apache Parquet files for local use, as well as a public instance on Amazon Athena interactive query service for ready-to-use powerful analytical processing. Source code file contents are cross-referenced at the graph leaves, and can be retrieved through individual requests using the Software Heritage archive API.
- **Main contribution:** Software Heritage is the largest existing public archive of software source code and accompanying development history: it currently spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects. This paper introduces the Software Heritage graph dataset: a fully-deduplicated Merkle DAG representation of the Software Heritage archive.
- **Relation with our paper:** Topic mapping: Repository discovery, Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 5. World of Code: An Infrastructure for Mining the Universe of Open Source VCS Data

- **Authors:** Ma, Yuxing, Bogart, Chris, Amreen, Sadika, Zaretzki, Russell, Mockus, Audris
- **Venue:** 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)
- **Year:** 2019
- **DOI:** `10.1109/msr.2019.00031`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2019.00031
- **Verification:** YES (Crossref)
- **Abstract:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flows? To answer such questions we a) create a very large and frequently updated collection of version control data for FLOSS projects named World of Code (WoC) and b) provide basic tools for conducting research that depends on measuring interdependencies among all FLOSS projects. Our current WoC implementation is capable of being updated on a monthly basis and contains over 12B git objects. To evaluate its research potential and to create vignettes for its usage, we employ WoC in conducting several research tasks. In particular, we find that it is capable of supporting trend evaluation, ecosystem measurement, and the determination of package usage. We expect WoC to spur investigation into global properties of OSS development leading to increased resiliency of the entire OSS ecosystem. Our infrastructure facilitates the discovery of key technical dependencies, code flow, and social networks that provide the basis to determine the structure and evolution of the relationships that drive FLOSS activities and innovation.
- **Main contribution:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flows?
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 6. The Software Heritage Graph Dataset

- **Authors:** Pietri, Antoine, Spinellis, Diomidis, Zacchiroli, Stefano
- **Venue:** Proceedings of the 17th International Conference on Mining Software Repositories
- **Year:** 2020
- **DOI:** `10.1145/3379597.3387510`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3379597.3387510
- **Verification:** YES (Crossref)
- **Abstract:** Software Heritage is the largest existing public archive of software source code and accompanying development history. It spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects. These software artifacts were retrieved from major collaborative development platforms (e.g., GitHub, GitLab) and package repositories (e.g., PyPI, Debian, NPM), and stored in a uniform representation linking together source code files, directories, commits, and full snapshots of version control systems (VCS) repositories as observed by Software Heritage during periodic crawls. This dataset is unique in terms of accessibility and scale, and allows to explore a number of research questions on the long tail of public software development, instead of solely focusing on “most starred” repositories as it often happens.
- **Main contribution:** Software Heritage is the largest existing public archive of software source code and accompanying development history. It spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects.
- **Relation with our paper:** Topic mapping: Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 7. World of code: enabling a research workflow for mining and analyzing the universe of open source VCS data

- **Authors:** Ma, Yuxing, Dey, Tapajit, Bogart, Chris, Amreen, Sadika, Valiev, Marat, Tutko, Adam, Kennard, David, Zaretzki, Russell, Mockus, Audris
- **Venue:** Empirical Software Engineering
- **Year:** 2021
- **DOI:** `10.1007/s10664-020-09905-9`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-020-09905-9
- **Verification:** YES (Crossref)
- **Abstract:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are the tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flow? To answer such questions we: a) create a very large and frequently updated collection of version control data in the entire FLOSS ecosystems named World of Code (WoC), that can completely cross-reference authors, projects, commits, blobs, dependencies, and history of the FLOSS ecosystems and b) provide capabilities to efficiently correct, augment, query, and analyze that data. Our current WoC implementation is capable of being updated on a monthly basis and contains over 18B Git objects. To evaluate its research potential and to create vignettes for its usage, we employ WoC in conducting several research tasks. In particular, we find that it is capable of supporting trend evaluation, ecosystem measurement, and the determination of package usage. We expect WoC to spur investigation into global properties of OSS development leading to increased resiliency of the entire OSS ecosystem. Our infrastructure facilitates the discovery of key technical dependencies, code flow, and social networks that provide the basis to determine the structure and evolution of the relationships that drive FLOSS activities and innovation.
- **Main contribution:** Open source software (OSS) is essential for modern society and, while substantial research has been done on individual (typically central) projects, only a limited understanding of the periphery of the entire OSS ecosystem exists. For example, how are the tens of millions of projects in the periphery interconnected through technical dependencies, code sharing, or knowledge flow?
- **Relation with our paper:** Topic mapping: Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 8. GitHub Proxy Server: A tool for supporting massive data collection on GitHub

- **Authors:** Borges, Hudson Silva, Valente, Marco Tulio
- **Venue:** Proceedings of the XXXVI Brazilian Symposium on Software Engineering
- **Year:** 2022
- **DOI:** `10.1145/3555228.3555276`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3555228.3555276
- **Verification:** YES (Crossref)
- **Abstract:** GitHub é a plataforma de codificação social mais popular e amplamente utilizada por comunidades e empresas para hospedagem de projetos open-source. Além disso, a plataforma conta com uma poderosa API que permite a pesquisadores coletarem informações públicas de projetos hospedados nela. Contudo, a coleta massiva de dados pode ser bastante desafiadora devido a limitações e mecanismos de detecção de abusos existentes. O presente trabalho apresentada uma ferramenta, chamada GitHub Proxy Server, que abstrai tais complexidades por meio de uma arquitetura independente de plataforma e linguagem de programação. Experimentos realizados com a ferramenta mostram que é possível melhorar o desempenho de tarefas de mineração do GitHub sem que complexidades adicionais sejam inseridas nos projetos.
- **Main contribution:** GitHub é a plataforma de codificação social mais popular e amplamente utilizada por comunidades e empresas para hospedagem de projetos open-source. Além disso, a plataforma conta com uma poderosa API que permite a pesquisadores coletarem informações públicas de projetos hospedados nela.
- **Relation with our paper:** Topic mapping: Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 9. The software heritage license dataset (2022 edition)

- **Authors:** Gonzalez-Barahona, Jesus M., Montes-Leon, Sergio, Robles, Gregorio, Zacchiroli, Stefano
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10377-w`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10377-w
- **Verification:** YES (Crossref)
- **Abstract:** Context: When software is released publicly, it is common to include with it either the full text of the license or licenses under which it is published, or a detailed reference to them. Therefore public licenses, including FOSS (free, open source software) licenses, are usually publicly available in source code repositories Objective: To compile a dataset containing as many documents as possible that contain the text of software licenses, or references to the license terms. Once compiled, characterize the dataset so that it can be used for further research, or practical purposes related to license analysis Method: Retrieve from Software Heritage—the largest publicly available archive of FOSS source code—all versions of all files whose names are commonly used to convey licensing terms. All retrieved documents will be characterized in various ways, using automated and manual analyses Results: The dataset consists of 6.9 million unique license files. Additional metadata about shipped license files is also provided, making the dataset ready to use in various contexts, including: file length measures, MIME type, SPDX license (detected using ScanCode), and oldest appearance. The results of a manual analysis of 8102 documents is also included, providing a ground truth for further analysis. The dataset is released as open data as an archive file containing all deduplicated license files, plus several portable CSV files with metadata, referencing files via cryptographic checksums Conclusions: Thanks to the extensive coverage of Software Heritage, the dataset presented in this paper covers a very large fraction of all software licenses for public code. We have assembled a large body of software licenses, characterized it quantitatively and qualitatively, and validated that it is mostly composed of licensing information and includes almost all known license texts. The dataset can be used to conduct empirical studies on open source licensing, training of automated license classifiers, natural language processing (NLP) analyses of legal texts, as well as historical and phylogenetic studies on FOSS licensing. It can also be used in practice to improve tools detecting licenses in source code
- **Main contribution:** Context: When software is released publicly, it is common to include with it either the full text of the license or licenses under which it is published, or a detailed reference to them. Therefore public licenses, including FOSS (free, open source software) licenses, are usually publicly available in source code repositories Objective: To compile a dataset containing as many documents as possible that contain the text of software licenses, or ...
- **Relation with our paper:** Topic mapping: Repository discovery. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — supporting citation


## Topic 3. Repository sampling

_Verified entries in this topic after curation: **8**_

### 1. Curating GitHub for engineered software projects

- **Authors:** Munaiah, Nuthan, Kroh, Steven, Cabrey, Craig, Nagappan, Meiyappan
- **Venue:** Empirical Software Engineering
- **Year:** 2017
- **DOI:** `10.1007/s10664-017-9512-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-017-9512-6
- **Verification:** YES (Crossref)
- **Abstract:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa. However, the simplicity in querying comes with a caveat: there are limited means of separating the signal (e.g. repositories containing engineered software projects) from the noise (e.g. repositories containing home work assignments). The proportion of noise in a random sample of repositories could skew the study and may lead to researchers reaching unrealistic, potentially inaccurate, conclusions. We argue that it is imperative to have the ability to sieve out the noise in such large repository forges. We propose a framework, and present a reference implementation of the framework as a tool called reaper, to enable researchers to select GitHub repositories that contain evidence of an engineered software project. We identify software engineering practices (called dimensions) and propose means for validating their existence in a GitHub repository. We used reaper to measure the dimensions of 1,857,423 GitHub repositories. We then used manually classified data sets of repositories to train classifiers capable of predicting if a given GitHub repository contains an engineered software project. The performance of the classifiers was evaluated using a set of 200 repositories with known ground truth classification. We also compared the performance of the classifiers to other approaches to classification (e.g. number of GitHub Stargazers) and found our classifiers to outperform existing approaches. We found stargazers-based classifier (with 10 as the threshold for number of stargazers) to exhibit high precision (97%) but an inversely proportional recall (32%). On the other hand, our best classifier exhibited a high precision (82%) and a high recall (86%). The stargazer-based criteria offers precision but fails to recall a significant portion of the population.
- **Main contribution:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa.
- **Relation with our paper:** Closest curation cousin (engineered vs non-engineered); related but different construct from our analytic-population membership. Topic mapping: Repository sampling, Sampling methodology, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Engineered status is neither necessary nor sufficient for instruction-artifact analytic-population membership.
- **Should be cited:** YES — cite in Related Work

### 2. RapidRelease - A Dataset of Projects and Issues on Github with Rapid Releases

- **Authors:** Joshi, Saket Dattatray, Chimalakonda, Sridhar
- **Venue:** 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)
- **Year:** 2019
- **DOI:** `10.1109/msr.2019.00088`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2019.00088
- **Verification:** YES (Crossref)
- **Abstract:** In the recent years, there has been a surge in the adoption of agile development model and continuous integration (CI) in software development. Recent trends have reduced average release cycle lengths to as low as 1-2 weeks, leading to an extensive number of studies in release engineering. Open-source development (OSD) has also witnessed a rapid increase in release rates, however, no large dataset of open-source projects exists which features high release rates. In this paper, we introduce the RapidRelease dataset, a data showcase of high release frequency open-source projects. The dataset hosts 994 projects from Github, with over 2 million issue reports. To the best of our knowledge, this is the first dataset that can facilitate researchers to empirically study release engineering and agile software development in open-source projects with rapid releases.
- **Main contribution:** In the recent years, there has been a surge in the adoption of agile development model and continuous integration (CI) in software development. Recent trends have reduced average release cycle lengths to as low as 1-2 weeks, leading to an extensive number of studies in release engineering.
- **Relation with our paper:** Topic mapping: Repository sampling. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. PHANTOM: Curating GitHub for engineered software projects using time-series clustering

- **Authors:** Pickerill, Peter, Jungen, Heiko Joshua, Ochodek, Mirosław, Maćkowiak, Michał, Staron, Miroslaw
- **Venue:** Empirical Software Engineering
- **Year:** 2020
- **DOI:** `10.1007/s10664-020-09825-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-020-09825-8
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Within the field of Mining Software Repositories, there are numerous methods employed to filter datasets in order to avoid analysing low-quality projects. Unfortunately, the existing filtering methods have not kept up with the growth of existing data sources, such as GitHub, and researchers often rely on quick and dirty techniques to curate datasets. Objective The objective of this study is to develop a method capable of filtering large quantities of software projects in a resource-efficient way. Method This study follows the Design Science Research (DSR) methodology. The proposed method, PHANTOM, extracts five measures from Git logs. Each measure is transformed into a time-series, which is represented as a feature vector for clustering using the k-means algorithm. Results Using the ground truth from a previous study, PHANTOM was shown to be able to rediscover the ground truth on the training dataset, and was able to identify “engineered” projects with up to 0.87 Precision and 0.94 Recall on the validation dataset. PHANTOM downloaded and processed the metadata of 1,786,601 GitHub repositories in 21.5 days using a single personal computer, which is over 33% faster than the previous study which used a computer cluster of 200 nodes. The possibility of applying the method outside of the open-source community was investigated by curating 100 repositories owned by two companies. Conclusions It is possible to use an unsupervised approach to identify engineered projects. PHANTOM was shown to be competitive compared to the existing supervised approaches while reducing the hardware requirements by two orders of magnitude.
- **Main contribution:** Abstract Context Within the field of Mining Software Repositories, there are numerous methods employed to filter datasets in order to avoid analysing low-quality projects. Unfortunately, the existing filtering methods have not kept up with the growth of existing data sources, such as GitHub, and researchers often rely on quick and dirty techniques to curate datasets.
- **Relation with our paper:** Closest curation cousin (engineered vs non-engineered); related but different construct from our analytic-population membership. Topic mapping: Repository sampling, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Engineered status is neither necessary nor sufficient for instruction-artifact analytic-population membership.
- **Should be cited:** YES — cite in Related Work

### 4. Sampling Projects in GitHub for MSR Studies

- **Authors:** Dabic, Ozren, Aghajani, Emad, Bavota, Gabriele
- **Venue:** 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)
- **Year:** 2021
- **DOI:** `10.1109/msr52588.2021.00074`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr52588.2021.00074
- **Verification:** YES (Crossref)
- **Abstract:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal. For example, a study related to licensing might be interested in selecting projects explicitly declaring a license. Once the selection criteria have been defined, utilities such as the GitHub APIs can be used to "query" the hosting service. However, researchers have to deal with usage limitations imposed by these APIs and a lack of required information. For example, the GitHub search APIs allow 30 requests per minute and, when searching repositories, only provide limited information (e.g., the number of commits in a repository is not included). To support researchers in sampling projects from GitHub, we present GHS (GitHub Search), a dataset containing 25 characteristics (e.g., number of commits, license, etc.) of 735,669 repositories written in 10 programming languages. The set of characteristics has been derived by looking for frequently used project selection criteria in MSR studies and the dataset is continuously updated to (i) always provide fresh data about the existing projects, and (ii) increase the number of indexed projects. The GHS dataset can be queried through a web application we built that allows to set many combinations of selection criteria needed for a study and download the information of matching repositories: https://seart-ghs.si.usi.ch.
- **Main contribution:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal.
- **Relation with our paper:** Empirical study of how MSR papers sample GitHub projects. Topic mapping: Repository sampling, Sampling methodology, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 5. GIRT-Data: Sampling GitHub Issue Report Templates

- **Authors:** Nikeghbal, Nafiseh, Hossein Kargaran, Amir, Heydarnoori, Abbas, Schütze, Hinrich
- **Venue:** 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)
- **Year:** 2023
- **DOI:** `10.1109/msr59073.2023.00026`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr59073.2023.00026
- **Verification:** YES (Crossref)
- **Abstract:** GitHub’s issue reports provide developers with valuable information that is essential to the evolution of a software development project. Contributors can use these reports to perform software engineering tasks like submitting bugs, requesting features, and collaborating on ideas. In the initial versions of issue reports, there was no standard way of using them. As a result, the quality of issue reports varied widely. To improve the quality of issue reports, GitHub introduced issue report templates (IRTs), which pre-fill issue descriptions when a new issue is opened. An IRT usually contains greeting contributors, describing project guidelines, and collecting relevant information. However, despite of effectiveness of this feature which was introduced in 2016, only nearly 5% of GitHub repositories (with more than 10 stars) utilize it. There are currently few articles on IRTs, and the available ones only consider a small number of repositories.In this work, we introduce GIRT-DATA, the first and largest dataset of IRTs in both YAML and Markdown format. This dataset and its corresponding open-source crawler tool are intended to support research in this area and to encourage more developers to use IRTs in their repositories. The stable version of the dataset contains 1,084,300 repositories and 50,032 of them support IRTs. The stable version of the dataset and crawler is available here: https://github.com/kargaranamir/girt-data
- **Main contribution:** GitHub’s issue reports provide developers with valuable information that is essential to the evolution of a software development project. Contributors can use these reports to perform software engineering tasks like submitting bugs, requesting features, and collaborating on ideas.
- **Relation with our paper:** Topic mapping: Repository sampling. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — supporting citation

### 6. Keep the Ball Rolling: Analyzing Release Cadence in GitHub Projects

- **Authors:** Kilic, Oz, Bowness, Nathaniel, Baysal, Olga
- **Venue:** 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)
- **Year:** 2023
- **DOI:** `10.1109/msr59073.2023.00058`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr59073.2023.00058
- **Verification:** YES (Crossref)
- **Abstract:** Release cadence is the measure of time between software releases, both internal and external. Few studies analyze popular open-source projects’ release cadence and use. In this work, we gathered over 8,000 GitHub projects from four popular programming languages; Go, Java, Python, and Ruby. Project were categorized into slow, modern, rapid, and rapid+ release cadence groups. We determined that only 13% of projects had a rapid release cadence of under 30 days. Applying NLP and topic modeling, we extracted the top 5 frequent topics for programming languages and obtained insights into their common uses. For example, Go projects are commonly used for Kubernetes tooling, while Ruby projects often leverage Rails for web development. We observed no significant relationship between frequent topics and the release cadence categories. This finding suggests release cadences are independent of the type of software delivered for a programming language.
- **Main contribution:** Release cadence is the measure of time between software releases, both internal and external. Few studies analyze popular open-source projects’ release cadence and use.
- **Relation with our paper:** Topic mapping: Repository sampling. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 7. Using Architecture Decision Records in Open Source Projects—An MSR Study on GitHub

- **Authors:** Buchgeher, Georg, Schöberl, Stefan, Geist, Verena, Dorninger, Bernhard, Haindl, Philipp, Weinreich, Rainer
- **Venue:** IEEE Access
- **Year:** 2023
- **DOI:** `10.1109/access.2023.3287654`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/access.2023.3287654
- **Verification:** YES (Crossref)
- **Abstract:** Architecture decision records (ADRs) have been proposed as a resource-efficient means for capturing architectural design decisions (ADDs), and have received attention not only from researchers but also from practitioners. We conducted a mining software repositories (MSR) study, in which we analyzed the use of ADRs in open source repositories at GitHub. Our results show that the adoption of ADRs is still low, although the number of repositories using ADRs is increasing every year. About 50% of all repositories with ADRs contain just one to five ADRs suggesting that the concept has been tried but not yet definitively adopted. In repositories that use ADRs more systematically, we observed that recording decisions is a team activity conducted by two or more users over a longer period of time. In most repositories the template proposed by Michael Nygrad is used. We, finally, provide an interpretation of the obtained results and discuss open future research challenges by elaborating on implications of the study’s findings as well as on recommendations on how to further increase the adoption of ADRs.
- **Main contribution:** Architecture decision records (ADRs) have been proposed as a resource-efficient means for capturing architectural design decisions (ADDs), and have received attention not only from researchers but also from practitioners. We conducted a mining software repositories (MSR) study, in which we analyzed the use of ADRs in open source repositories at GitHub.
- **Relation with our paper:** Topic mapping: Repository sampling. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 8. Wasmizer: Curating WebAssembly-driven Projects on GitHub

- **Authors:** Nicholson, Alexander, Stiévenart, Quentin, Mazidi, Arash, Ghafari, Mohammad
- **Venue:** 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)
- **Year:** 2023
- **DOI:** `10.1109/msr59073.2023.00031`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr59073.2023.00031
- **Verification:** YES (Crossref)
- **Abstract:** WebAssembly has attracted great attention as a portable compilation target for programming languages. To facilitate in-depth studies about this technology, we have deployed Wasmizer, a tool that regularly mines GitHub projects and makes an up-to-date dataset of WebAssembly sources and their binaries publicly available. Presently, we have collected 2540 C and C++ projects that are highly-related to WebAssembly, and built a dataset of 8915 binaries that are linked to their source projects. To demonstrate an application of this dataset, we have investigated the presence of eight WebAssembly compilation smells in the wild.
- **Main contribution:** WebAssembly has attracted great attention as a portable compilation target for programming languages. To facilitate in-depth studies about this technology, we have deployed Wasmizer, a tool that regularly mines GitHub projects and makes an up-to-date dataset of WebAssembly sources and their binaries publicly available.
- **Relation with our paper:** Topic mapping: Repository sampling. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation


## Topic 4. Sampling methodology

_Verified entries in this topic after curation: **5**_

### 1. Curating GitHub for engineered software projects

- **Authors:** Munaiah, Nuthan, Kroh, Steven, Cabrey, Craig, Nagappan, Meiyappan
- **Venue:** Empirical Software Engineering
- **Year:** 2017
- **DOI:** `10.1007/s10664-017-9512-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-017-9512-6
- **Verification:** YES (Crossref)
- **Abstract:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa. However, the simplicity in querying comes with a caveat: there are limited means of separating the signal (e.g. repositories containing engineered software projects) from the noise (e.g. repositories containing home work assignments). The proportion of noise in a random sample of repositories could skew the study and may lead to researchers reaching unrealistic, potentially inaccurate, conclusions. We argue that it is imperative to have the ability to sieve out the noise in such large repository forges. We propose a framework, and present a reference implementation of the framework as a tool called reaper, to enable researchers to select GitHub repositories that contain evidence of an engineered software project. We identify software engineering practices (called dimensions) and propose means for validating their existence in a GitHub repository. We used reaper to measure the dimensions of 1,857,423 GitHub repositories. We then used manually classified data sets of repositories to train classifiers capable of predicting if a given GitHub repository contains an engineered software project. The performance of the classifiers was evaluated using a set of 200 repositories with known ground truth classification. We also compared the performance of the classifiers to other approaches to classification (e.g. number of GitHub Stargazers) and found our classifiers to outperform existing approaches. We found stargazers-based classifier (with 10 as the threshold for number of stargazers) to exhibit high precision (97%) but an inversely proportional recall (32%). On the other hand, our best classifier exhibited a high precision (82%) and a high recall (86%). The stargazer-based criteria offers precision but fails to recall a significant portion of the population.
- **Main contribution:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa.
- **Relation with our paper:** Closest curation cousin (engineered vs non-engineered); related but different construct from our analytic-population membership. Topic mapping: Repository sampling, Sampling methodology, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Engineered status is neither necessary nor sufficient for instruction-artifact analytic-population membership.
- **Should be cited:** YES — cite in Related Work

### 2. Empirical software engineering experts on the use of students and professionals in experiments

- **Authors:** Falessi, Davide, Juristo, Natalia, Wohlin, Claes, Turhan, Burak, Münch, Jürgen, Jedlitschka, Andreas, Oivo, Markku
- **Venue:** Empirical Software Engineering
- **Year:** 2017
- **DOI:** `10.1007/s10664-017-9523-3`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-017-9523-3
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Empirical software engineering experts on the use of students and professionals in experiments” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Sampling methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. There is no random sampling in software engineering research

- **Authors:** Amir, Bilal, Ralph, Paul
- **Venue:** Proceedings of the 40th International Conference on Software Engineering: Companion Proceeedings
- **Year:** 2018
- **DOI:** `10.1145/3183440.3195001`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3183440.3195001
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling is considered crucial for predominately quantitative, positivist research. Researchers typically argue that a sample is representative when items are selected randomly from a population. However, random sampling is rare in empirical software engineering research because there are no credible sampling frames (population lists) for the units of analysis software engineering researchers study (e.g. software projects, code libraries, developers, projects). This means that most software engineering research does not support statistical generalization, but rejecting any particular study for lack of random sampling is capricious.
- **Main contribution:** Representative sampling is considered crucial for predominately quantitative, positivist research. Researchers typically argue that a sample is representative when items are selected randomly from a population.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 4. Sampling Projects in GitHub for MSR Studies

- **Authors:** Dabic, Ozren, Aghajani, Emad, Bavota, Gabriele
- **Venue:** 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)
- **Year:** 2021
- **DOI:** `10.1109/msr52588.2021.00074`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr52588.2021.00074
- **Verification:** YES (Crossref)
- **Abstract:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal. For example, a study related to licensing might be interested in selecting projects explicitly declaring a license. Once the selection criteria have been defined, utilities such as the GitHub APIs can be used to "query" the hosting service. However, researchers have to deal with usage limitations imposed by these APIs and a lack of required information. For example, the GitHub search APIs allow 30 requests per minute and, when searching repositories, only provide limited information (e.g., the number of commits in a repository is not included). To support researchers in sampling projects from GitHub, we present GHS (GitHub Search), a dataset containing 25 characteristics (e.g., number of commits, license, etc.) of 735,669 repositories written in 10 programming languages. The set of characteristics has been derived by looking for frequently used project selection criteria in MSR studies and the dataset is continuously updated to (i) always provide fresh data about the existing projects, and (ii) increase the number of indexed projects. The GHS dataset can be queried through a web application we built that allows to set many combinations of selection criteria needed for a study and download the information of matching repositories: https://seart-ghs.si.usi.ch.
- **Main contribution:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal.
- **Relation with our paper:** Empirical study of how MSR papers sample GitHub projects. Topic mapping: Repository sampling, Sampling methodology, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 5. Sampling in software engineering research: a critical review and guidelines

- **Authors:** Baltes, Sebastian, Ralph, Paul
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10072-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10072-8
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field. This article therefore reports a critical review of the state of sampling in recent, high-quality software engineering research. The key findings are: (1) random sampling is rare; (2) sophisticated sampling strategies are very rare; (3) sampling, representativeness and randomness often appear misunderstood. These findings suggest that software engineering research has a generalizability crisis. To address these problems, this paper synthesizes existing knowledge of sampling into a succinct primer and proposes extensive guidelines for improving the conduct, presentation and evaluation of sampling in software engineering research. It is further recommended that while researchers should strive for more representative samples, disparaging non-probability sampling is generally capricious and particularly misguided for predominately qualitative research.
- **Main contribution:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Sampling bias, Repository discovery frames, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work


## Topic 5. Sampling bias

_Verified entries in this topic after curation: **10**_

### 1. The perils and pitfalls of mining SourceForge

- **Authors:** Howison, J.
- **Venue:** "International Workshop on Mining Software Repositories (MSR 2004)" W17S Workshop - 26th International Conference on Software Engineering
- **Year:** 2004
- **DOI:** `10.1049/ic:20040467`
- **Publisher:** IEE
- **URL:** https://doi.org/10.1049/ic:20040467
- **Verification:** YES (Crossref)
- **Abstract:** SourceForge provides abundant accessible data from Open Source Software development projects, making it an attractive data source for software engineering research. However it is not without theoretical peril and practical pitfalls. In this paper, we outline practical lessons gained from our spidering, parsing and analysis of SourceForge data. SourceForge can be practically difficult: projects are defunct, data from earlier systems has been dumped in and crucial data is hosted outside SourceForge, dirtying the retrieved data. These practical issues play directly into analysis: decisions made in screening projects can reduce the range of variables, skewing data and biasing correlations. SourceForge is theoretically perilous: because it provides easily accessible data items for each project, tempting researchers to fit their theories to these limited data. Worse, few are plausible dependent variables. Studies are thus likely to test the same hypotheses even if they start from different theoretical bases. To avoid these problems, analyses of SourceForge projects should go beyond project level variables and carefully consider which variables are used for screening projects and which for testing hypotheses.
- **Main contribution:** SourceForge provides abundant accessible data from Open Source Software development projects, making it an attractive data source for software engineering research. However it is not without theoretical peril and practical pitfalls.
- **Relation with our paper:** Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 2. Open Borders? Immigration in Open Source Projects

- **Authors:** Bird, Christian, Gourley, Alex, Devanbu, Prem, Swaminathan, Anand, Hsu, Greta
- **Venue:** Fourth International Workshop on Mining Software Repositories (MSR'07:ICSE Workshops 2007)
- **Year:** 2007
- **DOI:** `10.1109/msr.2007.23`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2007.23
- **Verification:** YES (Crossref)
- **Abstract:** Open source software is built by teams of volunteers. Each project has a core team of developers, who have the authority to commit changes to the repository; this team is the elite, committed foundation of the project, selected through a meritocratic process from a larger number of people who participate on the mailing list. Most projects carefully regulate admission of outsiders to full developer privileges; some projects even have formal descriptions of this process. Understanding the factors that influence the "who, how and when" of this process is critical, both for the sustainability of FLOSS projects, and for outside stakeholders who want to gain entry and succeed. In this paper we mount a quantitative case study of the process by which people join FLOSS projects, using data mined from the Apache Web server, Postgres, and Python. We develop a theory of open source project joining, and evaluate this theory based on our data.
- **Main contribution:** Open source software is built by teams of volunteers. Each project has a core team of developers, who have the authority to commit changes to the repository; this team is the elite, committed foundation of the project, selected through a meritocratic process from a larger number of people who participate on the mailing list.
- **Relation with our paper:** Topic mapping: Sampling bias. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. The promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597074`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597074
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software. However, so far there have been no studies describing the quality and properties of the data available from GitHub. We document the results of an empirical study aimed at understanding the characteristics of the repositories in GitHub and how users take advantage of GitHub's main features---namely commits, pull requests, and issues. Our results indicate that, while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. We show, for example, that the majority of the projects are personal and inactive; that GitHub is also being used for free storage and as a Web hosting service; and that almost 40% of all pull requests do not appear as merged, even though they were. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 4. An in-depth study of the promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Empirical Software Engineering
- **Year:** 2015
- **DOI:** `10.1007/s10664-015-9393-5`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-015-9393-5
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data. We document the results of an empirical study aimed at understanding the characteristics of the repositories and users in GitHub; we see how users take advantage of GitHub’s main features and how their activity is tracked on GitHub and related datasets to point out misalignment between the real and mined data. Our results indicate that while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. For example, we show that the majority of the projects are personal and inactive, and that almost 40 % of all pull requests do not appear as merged even though they were. Also, approximately half of GitHub’s registered users do not have public activity, while the activity of GitHub users in repositories is not always easy to pinpoint. We use our identified perils to see if they can pose validity threats; we review selected papers from the MSR 2014 Mining Challenge and see if there are potential impacts to consider. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 5. Understanding the Factors That Impact the Popularity of GitHub Repositories

- **Authors:** Borges, Hudson, Hora, Andre, Valente, Marco Tulio
- **Venue:** 2016 IEEE International Conference on Software Maintenance and Evolution (ICSME)
- **Year:** 2016
- **DOI:** `10.1109/icsme.2016.31`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icsme.2016.31
- **Verification:** YES (Crossref)
- **Abstract:** Software popularity is a valuable information to modern open source developers, who constantly want to know if their systems are attracting new users, if new releases are gaining acceptance, or if they are meeting user's expectations. In this paper, we describe a study on the popularity of software systems hosted at GitHub, which is the world's largest collection of open source software. GitHub provides an explicit way for users to manifest their satisfaction with a hosted repository: the stargazers button. In our study, we reveal the main factors that impact the number of stars of GitHub projects, including programming language and application domain. We also study the impact of new features on project popularity. Finally, we identify four main patterns of popularity growth, which are derived after clustering the time series representing the number of stars of 2,279 popular GitHub repositories. We hope our results provide valuable insights to developers and maintainers, which could help them on building and evolving systems in a competitive software market.
- **Main contribution:** Software popularity is a valuable information to modern open source developers, who constantly want to know if their systems are attracting new users, if new releases are gaining acceptance, or if they are meeting user's expectations. In this paper, we describe a study on the popularity of software systems hosted at GitHub, which is the world's largest collection of open source software.
- **Relation with our paper:** Topic mapping: Sampling bias, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 6. Promises and Perils of Inferring Personality on GitHub

- **Authors:** van Mil, Frenk C.J., Rastogi, Ayushi, Zaidman, Andy
- **Venue:** Proceedings of the 15th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)
- **Year:** 2021
- **DOI:** `10.1145/3475716.3475775`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3475716.3475775
- **Verification:** YES (Crossref)
- **Abstract:** Background: Personality plays a pivotal role in our understanding of human actions and behavior. Today, the applications of personality are widespread, built on the solutions from psychology to infer personality. Aim: In software engineering, for instance, one widely used solution to infer personality uses textual communication data. As studies on personality in software engineering continue to grow, it is imperative to understand the performance of these solutions. Method: This paper compares the inferential ability of three widely studied text-based personality tests against each other and the ground truth on GitHub. We explore the challenges and potential solutions to improve the inferential ability of personality tests. Results: Our study shows that solutions for inferring personality are far from being perfect. Software engineering communications data can infer individual developer personality with an average error rate of 41%. In the best case, the error rate can be reduced up to 36% by following our recommendations1.
- **Main contribution:** Background: Personality plays a pivotal role in our understanding of human actions and behavior. Today, the applications of personality are widespread, built on the solutions from psychology to infer personality.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — supporting citation

### 7. Bot detection in GitHub repositories

- **Authors:** Chidambaram, Natarajan, Mazrae, Pooya Rostami
- **Venue:** Proceedings of the 19th International Conference on Mining Software Repositories
- **Year:** 2022
- **DOI:** `10.1145/3524842.3528520`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3524842.3528520
- **Verification:** YES (Crossref)
- **Abstract:** Contemporary social coding platforms like GitHub promote collaborative development. Many open-source software repositories hosted in these platforms use machine accounts (bots) to automate and facilitate a wide range of effort-intensive and repetitive activities. Determining if an account corresponds to a bot or a human contributor is important for socio-technical development analytics, for example, to understand how humans collaborate and interact in the presence of bots, to assess the positive and negative impact of using bots, to identify the top project contributors, to identify potential bus factors, and so on. Our project aims to include the trained machine learning (ML) classifier from the BoDeGHa bot detection tool as a plugin to the GrimoireLab software development analytics platform. In this work, we present the procedure to form a pipeline for retrieving contribution and contributor data using Perceval, distinguishing bots from humans using BoDeGHa, and visualising the results using Kibana.
- **Main contribution:** Contemporary social coding platforms like GitHub promote collaborative development. Many open-source software repositories hosted in these platforms use machine accounts (bots) to automate and facilitate a wide range of effort-intensive and repetitive activities.
- **Relation with our paper:** Topic mapping: Sampling bias. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 8. Sampling in software engineering research: a critical review and guidelines

- **Authors:** Baltes, Sebastian, Ralph, Paul
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10072-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10072-8
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field. This article therefore reports a critical review of the state of sampling in recent, high-quality software engineering research. The key findings are: (1) random sampling is rare; (2) sophisticated sampling strategies are very rare; (3) sampling, representativeness and randomness often appear misunderstood. These findings suggest that software engineering research has a generalizability crisis. To address these problems, this paper synthesizes existing knowledge of sampling into a succinct primer and proposes extensive guidelines for improving the conduct, presentation and evaluation of sampling in software engineering research. It is further recommended that while researchers should strive for more representative samples, disparaging non-probability sampling is generally capricious and particularly misguided for predominately qualitative research.
- **Main contribution:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Sampling bias, Repository discovery frames, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 9. DocMine: A Software Documentation-Related Dataset of 950 GitHub Repositories

- **Authors:** Manasa Venigalla, Akhila Sri, Chimalakonda, Sridhar
- **Venue:** 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)
- **Year:** 2023
- **DOI:** `10.1109/msr59073.2023.00062`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr59073.2023.00062
- **Verification:** YES (Crossref)
- **Abstract:** Software documentation is one of the critical aspects of a software project, that could support multiple tasks throughout the software development life-cycle. There is extensive research on understanding issues and challenges with existing documentation, which is typically available as readme files. In projects that support collaborative development, such as those on GitHub, other software artifacts such as commits, pull requests and issues, apart from the conventional readme files, wikis and source code comments, also contain useful information, that supports in understanding, using, extending and maintaining the project. However, we are not aware of any dataset that explicitly focuses on documentation-related information in multiple software artifacts such as readme files, commits and pull requests across a repository. To address this concern and to facilitate further research in software documentation, we present DocMine, as a dataset of documentation-related information, extracted from around 1.35M software artifacts in 950 GitHub repositories, spanning across four different programming languages. The dataset along with its documentation is made available in CSV and .sql formats at - https://doi.org/10.5281/zenodo.5195084.
- **Main contribution:** Software documentation is one of the critical aspects of a software project, that could support multiple tasks throughout the software development life-cycle. There is extensive research on understanding issues and challenges with existing documentation, which is typically available as readme files.
- **Relation with our paper:** Topic mapping: Sampling bias. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 10. The promises and perils of open source software release and usage by government – evidence from GitHub and literature

- **Authors:** Eibl, Gregor, Thurnay, Lőrinc
- **Venue:** Proceedings of the 24th Annual International Conference on Digital Government Research
- **Year:** 2023
- **DOI:** `10.1145/3598469.3598489`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3598469.3598489
- **Verification:** YES (Crossref)
- **Abstract:** Abstract: Open Source Software (OSS) is extensively utilized in industry and government because it allows for open access to the source code and allows for external involvement in the software development process. There are several factors driving this movement in a government setting, making it difficult to assess the adoption's success. Through a study of billions of rows of GitHub activity data, this research analyzes the production of OSS by administrations in German-speaking countries in detail and analyses the motivating factors and challenges to OSS adoption through a literature review. Similar studies have been conducted in other nations, with somewhat different approaches, foci, and different ways to identify public GitHub users as well as insiders and outsiders of OSS projects. 16 consequences of OSS usage and development are listed in the paper. On GitHub, we found 1021 OSS projects run by public agencies in largly German-speaking nations. We then compiled a list of the most popular projects based on commits and the most active public agencies in terms of projects. The research also finds automatic contributions by bots, which have not been taken into account in the literature so far, and demonstrates highly substantial positive correlations between commits, forks, and stars as proxy for the popularity of these projects. This research introduces a new method for identifying government organizations in OSS platforms and illuminates the possible positive and negative effects of the public sector's release and adoption of open source software.
- **Main contribution:** Abstract: Open Source Software (OSS) is extensively utilized in industry and government because it allows for open access to the source code and allows for external involvement in the software development process. There are several factors driving this movement in a government setting, making it difficult to assess the adoption's success.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — supporting citation


## Topic 6. Construct validity

_Verified entries in this topic after curation: **9**_

### 1. Experimentation in Software Engineering

- **Authors:** Wohlin, Claes, Runeson, Per, Höst, Martin, Ohlsson, Magnus C., Regnell, Björn, Wesslén, Anders
- **Venue:** 
- **Year:** 2012
- **DOI:** `10.1007/978-3-642-29044-2`
- **Publisher:** Springer Berlin Heidelberg
- **URL:** https://doi.org/10.1007/978-3-642-29044-2
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Experimentation in Software Engineering” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 2. The impact of tangled code changes

- **Authors:** Herzig, Kim, Zeller, Andreas
- **Venue:** 2013 10th Working Conference on Mining Software Repositories (MSR)
- **Year:** 2013
- **DOI:** `10.1109/msr.2013.6624018`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2013.6624018
- **Verification:** YES (Crossref)
- **Abstract:** When interacting with version control systems, developers often commit unrelated or loosely related code changes in a single transaction. When analyzing the version history, such tangled changes will make all changes to all modules appear related, possibly compromising the resulting analyses through noise and bias. In an investigation of five open-source Java projects, we found up to 15% of all bug fixes to consist of multiple tangled changes. Using a multi-predictor approach to untangle changes, we show that on average at least 16.6% of all source files are incorrectly associated with bug reports. We recommend better change organization to limit the impact of tangled changes.
- **Main contribution:** When interacting with version control systems, developers often commit unrelated or loosely related code changes in a single transaction. When analyzing the version history, such tangled changes will make all changes to all modules appear related, possibly compromising the resulting analyses through noise and bias.
- **Relation with our paper:** Topic mapping: Construct validity, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. Confounding parameters on program comprehension: a literature survey

- **Authors:** Siegmund, Janet, Schumann, Jana
- **Venue:** Empirical Software Engineering
- **Year:** 2014
- **DOI:** `10.1007/s10664-014-9318-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-014-9318-8
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Confounding parameters on program comprehension: a literature survey” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 4. The impact of tangled code changes on defect prediction models

- **Authors:** Herzig, Kim, Just, Sascha, Zeller, Andreas
- **Venue:** Empirical Software Engineering
- **Year:** 2015
- **DOI:** `10.1007/s10664-015-9376-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-015-9376-6
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “The impact of tangled code changes on defect prediction models” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 5. Views on Internal and External Validity in Empirical Software Engineering

- **Authors:** Siegmund, Janet, Siegmund, Norbert, Apel, Sven
- **Venue:** 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering
- **Year:** 2015
- **DOI:** `10.1109/icse.2015.24`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icse.2015.24
- **Verification:** YES (Crossref)
- **Abstract:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key? Do internally valid studies have any value? Should we replicate more to address the tradeoff between internal and external validity? We asked the community how empirical research should take place in software engineering, with a focus on the tradeoff between internal and external validity and replication, complemented with a literature review about the status of empirical research in software engineering. We found that the opinions differ considerably, and that there is no consensus in the community when to focus on internal or external validity and how to conduct and review replications.
- **Main contribution:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key?
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 6. Identifying, categorizing and mitigating threats to validity in software engineering secondary studies

- **Authors:** Ampatzoglou, Apostolos, Bibi, Stamatia, Avgeriou, Paris, Verbeek, Marijn, Chatzigeorgiou, Alexander
- **Venue:** Information and Software Technology
- **Year:** 2019
- **DOI:** `10.1016/j.infsof.2018.10.006`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2018.10.006
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies. Objective In this paper, we review the corpus of secondary studies, with the aim to identify: (a) the trend of reporting threats to validity, (b) the most common threats to validity and corresponding mitigation actions, and (c) possible categories in which threats to validity can be classified. Method To achieve this goal we employ the tertiary study research method that is used for synthesizing knowledge from existing secondary studies. In particular, we collected data from more than 100 studies, published until December 2016 in top quality software engineering venues (both journals and conference). Results Our results suggest that in recent years, secondary studies are more likely to report their threats to validity. However, the presentation of such threats is rather ad hoc, e.g., the same threat may be presented with a different name, or under a different category. To alleviate this problem, we propose a classification schema for reporting threats to validity and possible mitigation actions. Both the classification of threats and the associated mitigation actions have been validated by an empirical study, i.e., Delphi rounds with experts. Conclusion Based on the proposed schema, we provide a checklist, which authors of secondary studies can use for identifying and categorizing threats to validity and corresponding mitigation actions, while readers of secondary studies can use the checklist for assessing the validity of the reported results.
- **Main contribution:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 7. Construct Validity in Software Engineering

- **Authors:** Sjøberg, Dag I. K., Bergersen, Gunnar Rye
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2023
- **DOI:** `10.1109/tse.2022.3176725`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2022.3176725
- **Verification:** YES (Crossref)
- **Abstract:** Empirical research aims to establish generalizable claims from data. Such claims may involve concepts that must be measured indirectly by using indicators. Construct validity is concerned with whether one can justifiably make claims at the conceptual level that are supported by results at the operational level. We report a quantitative analysis of the awareness of construct validity in the software engineering literature between 2000 and 2019 and a qualitative review of 83 articles about human-centric experiments published in five high-quality journals between 2015 and 2019. Over the two decades, the appearance in the literature of the term construct validity increased sevenfold. Some of the reviewed articles we reviewed employed various ways to ensure that the indicators span the concept in an unbiased manner. We also found articles that reuse formerly validated constructs. However, the articles disagree about how to define construct validity. Several interpret construct validity excessively by including threats to internal, external, or statistical conclusion validity. A few articles also include fundamental challenges of a study, such as cheating and misunderstanding of experiment material. The diversity of topics included as threats to construct validity calls for a more minimalist approach. Based on the review, we propose seven guidelines to improve how construct validity is handled and reported in software engineering.
- **Main contribution:** Empirical research aims to establish generalizable claims from data. Such claims may involve concepts that must be measured indirectly by using indicators.
- **Relation with our paper:** Topic mapping: Construct validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 8. Operationalizing validity of empirical software engineering studies

- **Authors:** Härtel, Johannes, Lämmel, Ralf
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10370-3`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10370-3
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Operationalizing validity of empirical software engineering studies” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 9. Threats to validity in software engineering research: A critical reflection

- **Authors:** Verdecchia, Roberto, Engström, Emelie, Lago, Patricia, Runeson, Per, Song, Qunying
- **Venue:** Information and Software Technology
- **Year:** 2023
- **DOI:** `10.1016/j.infsof.2023.107329`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2023.107329
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Threats to validity in software engineering research: A critical reflection” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work


## Topic 7. Internal validity

_Verified entries in this topic after curation: **11**_

### 1. Quantitative Determination of the Relationship between Internal Validity and Bias in Software Engineering Experiments: Consequences for Systematic Literature Reviews

- **Authors:** Dieste, Oscar, Grim´n, Anna, Juristo, Natalia, Saxena, Himanshu
- **Venue:** 2011 International Symposium on Empirical Software Engineering and Measurement
- **Year:** 2011
- **DOI:** `10.1109/esem.2011.37`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/esem.2011.37
- **Verification:** YES (Crossref)
- **Abstract:** Quality assessment is one of the activities performed as part of systematic literature reviews. It is commonly accepted that a good quality experiment is bias free. Bias is considered to be related to internal validity (e.g., how adequately the experiment is planned, executed and analysed). Quality assessment is usually conducted using checklists and quality scales. It has not yet been proven, however, that quality is related to experimental bias. Aim: Identify whether there is a relationship between internal validity and bias in software engineering experiments. Method: We built a quality scale to determine the quality of the studies, which we applied to 28 experiments included in two systematic literature reviews. We proposed an objective indicator of experimental bias, which we applied to the same 28 experiments. Finally, we analysed the correlations between the quality scores and the proposed measure of bias. Results: We failed to find a relationship between the global quality score (resulting from the quality scale) and bias, however, we did identify interesting correlations between bias and some particular aspects of internal validity measured by the instrument. Conclusions: There is an empirically provable relationship between internal validity and bias. It is feasible to apply quality assessment in systematic literature reviews, subject to limits on the internal validity aspects for consideration.
- **Main contribution:** Quality assessment is one of the activities performed as part of systematic literature reviews. It is commonly accepted that a good quality experiment is bias free.
- **Relation with our paper:** Topic mapping: Internal validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** OPTIONAL — cite only if space permits

### 2. Experimentation in Software Engineering

- **Authors:** Wohlin, Claes, Runeson, Per, Höst, Martin, Ohlsson, Magnus C., Regnell, Björn, Wesslén, Anders
- **Venue:** 
- **Year:** 2012
- **DOI:** `10.1007/978-3-642-29044-2`
- **Publisher:** Springer Berlin Heidelberg
- **URL:** https://doi.org/10.1007/978-3-642-29044-2
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Experimentation in Software Engineering” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 3. Researcher Bias: The Use of Machine Learning in Software Defect Prediction

- **Authors:** Shepperd, Martin, Bowes, David, Hall, Tracy
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2014
- **DOI:** `10.1109/tse.2014.2322358`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2014.2322358
- **Verification:** YES (Crossref)
- **Abstract:** Background. The ability to predict defect-prone software components would be valuable. Consequently, there have been many empirical studies to evaluate the performance of different techniques endeavouring to accomplish this effectively. However no one technique dominates and so designing a reliable defect prediction model remains problematic. Objective. We seek to make sense of the many conflicting experimental results and understand which factors have the largest effect on predictive performance. Method. We conduct a meta-analysis of all relevant, high quality primary studies of defect prediction to determine what factors influence predictive performance. This is based on 42 primary studies that satisfy our inclusion criteria that collectively report 600 sets of empirical prediction results. By reverse engineering a common response variable we build a random effects ANOVA model to examine the relative contribution of four model building factors (classifier, data set, input metrics and researcher group) to model prediction performance. Results. Surprisingly we find that the choice of classifier has little impact upon performance (1.3 percent) and in contrast the major (31 percent) explanatory factor is the researcher group. It matters more who does the work than what is done. Conclusion. To overcome this high level of researcher bias, defect prediction researchers should (i) conduct blind analysis, (ii) improve reporting protocols and (iii) conduct more intergroup studies in order to alleviate expertise issues. Lastly, research is required to determine whether this bias is prevalent in other applications domains.
- **Main contribution:** Background. The ability to predict defect-prone software components would be valuable.
- **Relation with our paper:** Topic mapping: Internal validity, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. Views on Internal and External Validity in Empirical Software Engineering

- **Authors:** Siegmund, Janet, Siegmund, Norbert, Apel, Sven
- **Venue:** 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering
- **Year:** 2015
- **DOI:** `10.1109/icse.2015.24`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icse.2015.24
- **Verification:** YES (Crossref)
- **Abstract:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key? Do internally valid studies have any value? Should we replicate more to address the tradeoff between internal and external validity? We asked the community how empirical research should take place in software engineering, with a focus on the tradeoff between internal and external validity and replication, complemented with a literature review about the status of empirical research in software engineering. We found that the opinions differ considerably, and that there is no consensus in the community when to focus on internal or external validity and how to conduct and review replications.
- **Main contribution:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key?
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 5. Comments on “Researcher Bias: The Use of Machine Learning in Software Defect Prediction”

- **Authors:** Tantithamthavorn, Chakkrit, McIntosh, Shane, Hassan, Ahmed E., Matsumoto, Kenichi
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2016
- **DOI:** `10.1109/tse.2016.2553030`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2016.2553030
- **Verification:** YES (Crossref)
- **Abstract:** Shepperd et al. find that the reported performance of a defect prediction model shares a strong relationship with the group of researchers who construct the models. In this paper, we perform an alternative investigation of Shepperd et al.'s data. We observe that (a) research group shares a strong association with other explanatory variables (i.e., the dataset and metric families that are used to build a model); (b) the strong association among these explanatory variables makes it difficult to discern the impact of the research group on model performance; and (c) after mitigating the impact of this strong association, we find that the research group has a smaller impact than the metric family. These observations lead us to conclude that the relationship between the research group and the performance of a defect prediction model are more likely due to the tendency of researchers to reuse experimental components (e.g., datasets and metrics). We recommend that researchers experiment with a broader selection of datasets and metrics to combat any potential bias in their results.
- **Main contribution:** Shepperd et al. find that the reported performance of a defect prediction model shares a strong relationship with the group of researchers who construct the models.
- **Relation with our paper:** Topic mapping: Internal validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 6. An Empirical Comparison of Model Validation Techniques for Defect Prediction Models

- **Authors:** Tantithamthavorn, Chakkrit, McIntosh, Shane, Hassan, Ahmed E., Matsumoto, Kenichi
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2017
- **DOI:** `10.1109/tse.2016.2584050`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2016.2584050
- **Verification:** YES (Crossref)
- **Abstract:** Defect prediction models help software quality assurance teams to allocate their limited resources to the most defect-prone modules. Model validation techniques, such as <inline-formula><tex-math notation="LaTeX">$k$</tex-math> </inline-formula> -fold cross-validation, use historical data to estimate how well a model will perform in the future. However, little is known about how accurate the estimates of model validation techniques tend to be. In this paper, we investigate the bias and variance of model validation techniques in the domain of defect prediction. Analysis of 101 public defect datasets suggests that 77 percent of them are highly susceptible to producing unstable results– - selecting an appropriate model validation technique is a critical experimental design choice. Based on an analysis of 256 studies in the defect prediction literature, we select the 12 most commonly adopted model validation techniques for evaluation. Through a case study of 18 systems, we find that single-repetition holdout validation tends to produce estimates with 46-229 percent more bias and 53-863 percent more variance than the top-ranked model validation techniques. On the other hand, out-of-sample bootstrap validation yields the best balance between the bias and variance of estimates in the context of our study. Therefore, we recommend that future defect prediction studies avoid single-repetition holdout validation, and instead, use out-of-sample bootstrap validation.
- **Main contribution:** Defect prediction models help software quality assurance teams to allocate their limited resources to the most defect-prone modules. Model validation techniques, such as <inline-formula><tex-math notation="LaTeX">$k$</tex-math> </inline-formula> -fold cross-validation, use historical data to estimate how well a model will perform in the future.
- **Relation with our paper:** Topic mapping: Internal validity, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 7. Authors’ Reply to “Comments on ‘Researcher Bias: The Use of Machine Learning in Software Defect Prediction’”

- **Authors:** Shepperd, Martin, Hall, Tracy, Bowes, David
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2018
- **DOI:** `10.1109/tse.2017.2731308`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2017.2731308
- **Verification:** YES (Crossref)
- **Abstract:** In 2014 we published a meta-analysis of software defect prediction studies [1] . This suggested that the most important factor in determining results was Research Group, i.e., who conducts the experiment is more important than the classifier algorithms being investigated. A recent re-analysis [2] sought to argue that the effect is less strong than originally claimed since there is a relationship between Research Group and Dataset. In this response we show (i) the re-analysis is based on a small (21 percent) subset of our original data, (ii) using the same re-analysis approach with a larger subset shows that Research Group is more important than type of Classifier and (iii) however the data are analysed there is compelling evidence that who conducts the research has an effect on the results. This means that the problem of researcher bias remains. Addressing it should be seen as a matter of priority amongst those of us who conduct and publish experiments comparing the performance of competing software defect prediction systems.
- **Main contribution:** In 2014 we published a meta-analysis of software defect prediction studies [1] . This suggested that the most important factor in determining results was Research Group, i.e., who conducts the experiment is more important than the classifier algorithms being investigated.
- **Relation with our paper:** Topic mapping: Internal validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 8. Identifying, categorizing and mitigating threats to validity in software engineering secondary studies

- **Authors:** Ampatzoglou, Apostolos, Bibi, Stamatia, Avgeriou, Paris, Verbeek, Marijn, Chatzigeorgiou, Alexander
- **Venue:** Information and Software Technology
- **Year:** 2019
- **DOI:** `10.1016/j.infsof.2018.10.006`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2018.10.006
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies. Objective In this paper, we review the corpus of secondary studies, with the aim to identify: (a) the trend of reporting threats to validity, (b) the most common threats to validity and corresponding mitigation actions, and (c) possible categories in which threats to validity can be classified. Method To achieve this goal we employ the tertiary study research method that is used for synthesizing knowledge from existing secondary studies. In particular, we collected data from more than 100 studies, published until December 2016 in top quality software engineering venues (both journals and conference). Results Our results suggest that in recent years, secondary studies are more likely to report their threats to validity. However, the presentation of such threats is rather ad hoc, e.g., the same threat may be presented with a different name, or under a different category. To alleviate this problem, we propose a classification schema for reporting threats to validity and possible mitigation actions. Both the classification of threats and the associated mitigation actions have been validated by an empirical study, i.e., Delphi rounds with experts. Conclusion Based on the proposed schema, we provide a checklist, which authors of secondary studies can use for identifying and categorizing threats to validity and corresponding mitigation actions, while readers of secondary studies can use the checklist for assessing the validity of the reported results.
- **Main contribution:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 9. Operationalizing validity of empirical software engineering studies

- **Authors:** Härtel, Johannes, Lämmel, Ralf
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10370-3`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10370-3
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Operationalizing validity of empirical software engineering studies” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 10. Threats to validity in software engineering research: A critical reflection

- **Authors:** Verdecchia, Roberto, Engström, Emelie, Lago, Patricia, Runeson, Per, Song, Qunying
- **Venue:** Information and Software Technology
- **Year:** 2023
- **DOI:** `10.1016/j.infsof.2023.107329`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2023.107329
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Threats to validity in software engineering research: A critical reflection” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 11. An audit of machine learning experiments on software defect prediction

- **Authors:** Destefanis, Giuseppe, Yousefi, Leila, Shepperd, Martin, Tucker, Allan, Swift, Stephen, Counsell, Steve, Arzoky, Mahir
- **Venue:** Empirical Software Engineering
- **Year:** 2026
- **DOI:** `10.1007/s10664-025-10797-w`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-025-10797-w
- **Verification:** YES (Crossref)
- **Abstract:** Machine learning algorithms are increasingly being proposed to solve the problem of predicting defect-prone software components. In this literature, computational experiments are the primary means of evaluating and comparing learners and the credibility of findings depends critically on their experimental design and reporting. This paper audits recent software defect prediction (SDP) experiments by assessing their experimental design, analysis and reporting practices against widely accepted norms from statistics, machine learning and empirical software engineering. Our aim is to characterise the current state of practice and evaluate the reproducibility of published findings. We undertook an audit of relevant studies published from the SCOPUS database (2019-2023) focusing on their experimental design and analysis choices e.g., the outcome variables such as F-measure and the type of out of sample (OOS) validation regime, e.g., cross-validation, plus the statistical analysis and inference mechanisms. In all, we evaluated nine different study issues. This was complemented by an assessment of reproducibility using the instrument proposed by González-Barahona and Robles. Our search located approximately 1,585 experiments in SDP (2019-2023), a substantial body of work. From this, we randomly sampled 101 (\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$ \approx 6.4\%$$\end{document}) papers, 61 journal and 40 conference papers. Almost 50% are behind ‘paywalls’. We found considerable divergence in research practice. The number of datasets used ranged 1-365, the number of learners or learner variants evaluated from 1-34 and the number of performance metrics from 1 to 9. Approximately 45% of papers made use of formal statistical inference. We detected a total of 427 issues distributed across 101 papers (median=4) with only one paper being entirely issue-free. In terms of reproducibility, experiments ranged from near perfect to lacking almost all required information. We also found two examples of tortured phrases and potential “paper mill” activity. Approaches to designing and reporting computational experiments varied greatly, but almost half the studies provided insufficient information such that reproduction would be challenging. Overall, our audit suggests that as a research community, we have considerable scope for improvement. Fortunately, many improvements should be neither difficult nor costly to achieve.
- **Main contribution:** Machine learning algorithms are increasingly being proposed to solve the problem of predicting defect-prone software components. In this literature, computational experiments are the primary means of evaluating and comparing learners and the credibility of findings depends critically on their experimental design and reporting.
- **Relation with our paper:** Topic mapping: Internal validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits


## Topic 8. External validity

_Verified entries in this topic after curation: **6**_

### 1. Cross-project defect prediction

- **Authors:** Zimmermann, Thomas, Nagappan, Nachiappan, Gall, Harald, Giger, Emanuel, Murphy, Brendan
- **Venue:** Proceedings of the 7th joint meeting of the European software engineering conference and the ACM SIGSOFT symposium on The foundations of software engineering
- **Year:** 2009
- **DOI:** `10.1145/1595696.1595713`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/1595696.1595713
- **Verification:** YES (Crossref)
- **Abstract:** Prediction of software defects works well within projects as long as there is a sufficient amount of data available to train any models. However, this is rarely the case for new software projects and for many companies. So far, only a few have studies focused on transferring prediction models from one project to another. In this paper, we study cross-project defect prediction models on a large scale. For 12 real-world applications, we ran 622 cross-project predictions. Our results indicate that cross-project prediction is a serious challenge, i.e., simply using models from projects in the same domain or with the same process does not lead to accurate predictions. To help software engineers choose models wisely, we identified factors that do influence the success of cross-project predictions. We also derived decision trees that can provide early estimates for precision, recall, and accuracy before a prediction is attempted.
- **Main contribution:** Prediction of software defects works well within projects as long as there is a sufficient amount of data available to train any models. However, this is rarely the case for new software projects and for many companies.
- **Relation with our paper:** Topic mapping: External validity, Dataset contamination. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. Experimentation in Software Engineering

- **Authors:** Wohlin, Claes, Runeson, Per, Höst, Martin, Ohlsson, Magnus C., Regnell, Björn, Wesslén, Anders
- **Venue:** 
- **Year:** 2012
- **DOI:** `10.1007/978-3-642-29044-2`
- **Publisher:** Springer Berlin Heidelberg
- **URL:** https://doi.org/10.1007/978-3-642-29044-2
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Experimentation in Software Engineering” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 3. Views on Internal and External Validity in Empirical Software Engineering

- **Authors:** Siegmund, Janet, Siegmund, Norbert, Apel, Sven
- **Venue:** 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering
- **Year:** 2015
- **DOI:** `10.1109/icse.2015.24`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icse.2015.24
- **Verification:** YES (Crossref)
- **Abstract:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key? Do internally valid studies have any value? Should we replicate more to address the tradeoff between internal and external validity? We asked the community how empirical research should take place in software engineering, with a focus on the tradeoff between internal and external validity and replication, complemented with a literature review about the status of empirical research in software engineering. We found that the opinions differ considerably, and that there is no consensus in the community when to focus on internal or external validity and how to conduct and review replications.
- **Main contribution:** Empirical methods have grown common in software engineering, but there is no consensus on how to apply them properly. Is practical relevance key?
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 4. Identifying, categorizing and mitigating threats to validity in software engineering secondary studies

- **Authors:** Ampatzoglou, Apostolos, Bibi, Stamatia, Avgeriou, Paris, Verbeek, Marijn, Chatzigeorgiou, Alexander
- **Venue:** Information and Software Technology
- **Year:** 2019
- **DOI:** `10.1016/j.infsof.2018.10.006`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2018.10.006
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies. Objective In this paper, we review the corpus of secondary studies, with the aim to identify: (a) the trend of reporting threats to validity, (b) the most common threats to validity and corresponding mitigation actions, and (c) possible categories in which threats to validity can be classified. Method To achieve this goal we employ the tertiary study research method that is used for synthesizing knowledge from existing secondary studies. In particular, we collected data from more than 100 studies, published until December 2016 in top quality software engineering venues (both journals and conference). Results Our results suggest that in recent years, secondary studies are more likely to report their threats to validity. However, the presentation of such threats is rather ad hoc, e.g., the same threat may be presented with a different name, or under a different category. To alleviate this problem, we propose a classification schema for reporting threats to validity and possible mitigation actions. Both the classification of threats and the associated mitigation actions have been validated by an empirical study, i.e., Delphi rounds with experts. Conclusion Based on the proposed schema, we provide a checklist, which authors of secondary studies can use for identifying and categorizing threats to validity and corresponding mitigation actions, while readers of secondary studies can use the checklist for assessing the validity of the reported results.
- **Main contribution:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 5. Operationalizing validity of empirical software engineering studies

- **Authors:** Härtel, Johannes, Lämmel, Ralf
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10370-3`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10370-3
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Operationalizing validity of empirical software engineering studies” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 6. Threats to validity in software engineering research: A critical reflection

- **Authors:** Verdecchia, Roberto, Engström, Emelie, Lago, Patricia, Runeson, Per, Song, Qunying
- **Venue:** Information and Software Technology
- **Year:** 2023
- **DOI:** `10.1016/j.infsof.2023.107329`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2023.107329
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Threats to validity in software engineering research: A critical reflection” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work


## Topic 9. Dataset contamination

_Verified entries in this topic after curation: **6**_

### 1. Cross-project defect prediction

- **Authors:** Zimmermann, Thomas, Nagappan, Nachiappan, Gall, Harald, Giger, Emanuel, Murphy, Brendan
- **Venue:** Proceedings of the 7th joint meeting of the European software engineering conference and the ACM SIGSOFT symposium on The foundations of software engineering
- **Year:** 2009
- **DOI:** `10.1145/1595696.1595713`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/1595696.1595713
- **Verification:** YES (Crossref)
- **Abstract:** Prediction of software defects works well within projects as long as there is a sufficient amount of data available to train any models. However, this is rarely the case for new software projects and for many companies. So far, only a few have studies focused on transferring prediction models from one project to another. In this paper, we study cross-project defect prediction models on a large scale. For 12 real-world applications, we ran 622 cross-project predictions. Our results indicate that cross-project prediction is a serious challenge, i.e., simply using models from projects in the same domain or with the same process does not lead to accurate predictions. To help software engineers choose models wisely, we identified factors that do influence the success of cross-project predictions. We also derived decision trees that can provide early estimates for precision, recall, and accuracy before a prediction is attempted.
- **Main contribution:** Prediction of software defects works well within projects as long as there is a sufficient amount of data available to train any models. However, this is rarely the case for new software projects and for many companies.
- **Relation with our paper:** Topic mapping: External validity, Dataset contamination. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. A unifying view on dataset shift in classification

- **Authors:** Moreno-Torres, Jose G., Raeder, Troy, Alaiz-Rodríguez, Rocío, Chawla, Nitesh V., Herrera, Francisco
- **Venue:** Pattern Recognition
- **Year:** 2012
- **DOI:** `10.1016/j.patcog.2011.06.019`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.patcog.2011.06.019
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “A unifying view on dataset shift in classification” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 3. Leakage in data mining

- **Authors:** Kaufman, Shachar, Rosset, Saharon, Perlich, Claudia, Stitelman, Ori
- **Venue:** ACM Transactions on Knowledge Discovery from Data
- **Year:** 2012
- **DOI:** `10.1145/2382577.2382579`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/2382577.2382579
- **Verification:** YES (Crossref)
- **Abstract:** Deemed “one of the top ten data mining mistakes”, leakage is the introduction of information about the data mining target that should not be legitimately available to mine from. In addition to our own industry experience with real-life projects, controversies around several major public data mining competitions held recently such as the INFORMS 2010 Data Mining Challenge and the IJCNN 2011 Social Network Challenge are evidence that this issue is as relevant today as it has ever been. While acknowledging the importance and prevalence of leakage in both synthetic competitions and real-life data mining projects, existing literature has largely left this idea unexplored. What little has been said turns out not to be broad enough to cover more complex cases of leakage, such as those where the classical independently and identically distributed (i.i.d.) assumption is violated, that have been recently documented. In our new approach, these cases and others are explained by explicitly defining modeling goals and analyzing the broader framework of the data mining problem. The resulting definition enables us to derive general methodology for dealing with the issue. We show that it is possible to avoid leakage with a simple specific approach to data management followed by what we call a learn-predict separation, and present several ways of detecting leakage when the modeler has no control over how the data have been collected. We also offer an alternative point of view on leakage that is based on causal graph modeling concepts.
- **Main contribution:** Deemed “one of the top ten data mining mistakes”, leakage is the introduction of information about the data mining target that should not be legitimately available to mine from. In addition to our own industry experience with real-life projects, controversies around several major public data mining competitions held recently such as the INFORMS 2010 Data Mining Challenge and the IJCNN 2011 Social Network Challenge are evidence that this issue ...
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 4. DéjàVu: a map of code duplicates on GitHub

- **Authors:** Lopes, Cristina V., Maj, Petr, Martins, Pedro, Saini, Vaibhav, Yang, Di, Zitny, Jakub, Sajnani, Hitesh, Vitek, Jan
- **Venue:** Proceedings of the ACM on Programming Languages
- **Year:** 2017
- **DOI:** `10.1145/3133908`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3133908
- **Verification:** YES (Crossref)
- **Abstract:** Previous studies have shown that there is a non-trivial amount of duplication in source code. This paper analyzes a corpus of 4.5 million non-fork projects hosted on GitHub representing over 428 million files written in Java, C++, Python, and JavaScript. We found that this corpus has a mere 85 million unique files. In other words, 70% of the code on GitHub consists of clones of previously created files. There is considerable variation between language ecosystems. JavaScript has the highest rate of file duplication, only 6% of the files are distinct. Java, on the other hand, has the least duplication, 60% of files are distinct. Lastly, a project-level analysis shows that between 9% and 31% of the projects contain at least 80% of files that can be found elsewhere. These rates of duplication have implications for systems built on open source software as well as for researchers interested in analyzing large code bases. As a concrete artifact of this study, we have created DéjàVu, a publicly available map of code duplicates in GitHub repositories.
- **Main contribution:** Previous studies have shown that there is a non-trivial amount of duplication in source code. This paper analyzes a corpus of 4.5 million non-fork projects hosted on GitHub representing over 428 million files written in Java, C++, Python, and JavaScript.
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 5. The adverse effects of code duplication in machine learning models of code

- **Authors:** Allamanis, Miltiadis
- **Venue:** Proceedings of the 2019 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software
- **Year:** 2019
- **DOI:** `10.1145/3359591.3359735`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3359591.3359735
- **Verification:** YES (Crossref)
- **Abstract:** The field of big code relies on mining large corpora of code to perform some learning task towards creating better tools for software engineers. A significant threat to this approach was recently identified by Lopes et al. (2017) who found a large amount of near-duplicate code on GitHub. However, the impact of code duplication has not been noticed by researchers devising machine learning models for source code. In this work, we explore the effects of code duplication on machine learning models showing that reported performance metrics are sometimes inflated by up to 100% when testing on duplicated code corpora compared to the performance on de-duplicated corpora which more accurately represent how machine learning models of code are used by software engineers. We present a duplication index for widely used datasets, list best practices for collecting code corpora and evaluating machine learning models on them. Finally, we release tools to help the community avoid this problem in future research.
- **Main contribution:** The field of big code relies on mining large corpora of code to perform some learning task towards creating better tools for software engineers. A significant threat to this approach was recently identified by Lopes et al.
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 6. Leakage and the reproducibility crisis in machine-learning-based science

- **Authors:** Kapoor, Sayash, Narayanan, Arvind
- **Venue:** Patterns
- **Year:** 2023
- **DOI:** `10.1016/j.patter.2023.100804`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.patter.2023.100804
- **Verification:** YES (Crossref)
- **Abstract:** Summary Machine-learning (ML) methods have gained prominence in the quantitative sciences. However, there are many known methodological pitfalls, including data leakage, in ML-based science. We systematically investigate reproducibility issues in ML-based science. Through a survey of literature in fields that have adopted ML methods, we find 17 fields where leakage has been found, collectively affecting 294 papers and, in some cases, leading to wildly overoptimistic conclusions. Based on our survey, we introduce a detailed taxonomy of eight types of leakage, ranging from textbook errors to open research problems. We propose that researchers test for each type of leakage by filling out model info sheets, which we introduce. Finally, we conduct a reproducibility study of civil war prediction, where complex ML models are believed to vastly outperform traditional statistical models such as logistic regression (LR). When the errors are corrected, complex ML models do not perform substantively better than decades-old LR models.
- **Main contribution:** Summary Machine-learning (ML) methods have gained prominence in the quantitative sciences. However, there are many known methodological pitfalls, including data leakage, in ML-based science.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Dataset contamination, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch. Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work


## Topic 10. GitHub repository mining

_Verified entries in this topic after curation: **11**_

### 1. The perils and pitfalls of mining SourceForge

- **Authors:** Howison, J.
- **Venue:** "International Workshop on Mining Software Repositories (MSR 2004)" W17S Workshop - 26th International Conference on Software Engineering
- **Year:** 2004
- **DOI:** `10.1049/ic:20040467`
- **Publisher:** IEE
- **URL:** https://doi.org/10.1049/ic:20040467
- **Verification:** YES (Crossref)
- **Abstract:** SourceForge provides abundant accessible data from Open Source Software development projects, making it an attractive data source for software engineering research. However it is not without theoretical peril and practical pitfalls. In this paper, we outline practical lessons gained from our spidering, parsing and analysis of SourceForge data. SourceForge can be practically difficult: projects are defunct, data from earlier systems has been dumped in and crucial data is hosted outside SourceForge, dirtying the retrieved data. These practical issues play directly into analysis: decisions made in screening projects can reduce the range of variables, skewing data and biasing correlations. SourceForge is theoretically perilous: because it provides easily accessible data items for each project, tempting researchers to fit their theories to these limited data. Worse, few are plausible dependent variables. Studies are thus likely to test the same hypotheses even if they start from different theoretical bases. To avoid these problems, analyses of SourceForge projects should go beyond project level variables and carefully consider which variables are used for screening projects and which for testing hypotheses.
- **Main contribution:** SourceForge provides abundant accessible data from Open Source Software development projects, making it an attractive data source for software engineering research. However it is not without theoretical peril and practical pitfalls.
- **Relation with our paper:** Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 2. GHTorrent: Github's data from a firehose

- **Authors:** Gousios, Georgios, Spinellis, D.
- **Venue:** 2012 9th IEEE Working Conference on Mining Software Repositories (MSR)
- **Year:** 2012
- **DOI:** `10.1109/msr.2012.6224294`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2012.6224294
- **Verification:** YES (Crossref)
- **Abstract:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform. GitHub provides an extensive REST API, which enables researchers to retrieve both the commits to the projects' repositories and events generated through user actions on project resources. GHTorrent aims to create a scalable off line mirror of GitHub's event streams and persistent data, and offer it to the research community as a service. In this paper, we present the project's design and initial implementation and demonstrate how the provided datasets can be queried and processed.
- **Main contribution:** A common requirement of many empirical software engineering studies is the acquisition and curation of data from software repositories. During the last few years, GitHub has emerged as a popular project hosting, mirroring and collaboration platform.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 3. Lean GHTorrent: GitHub data on demand

- **Authors:** Gousios, Georgios, Vasilescu, Bogdan, Serebrenik, Alexander, Zaidman, Andy
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597126`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597126
- **Verification:** YES (Crossref)
- **Abstract:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it. GitHub offers a tremendous research potential. For instance, it is a flagship for current open source development, a place for developers to showcase their expertise to peers or potential recruiters, and the platform where social coding features or pull requests emerged. However, GitHub data is, to date, largely underexplored. To facilitate studies of GitHub, we have created GHTorrent, a scalable, queriable, offline mirror of the data offered through the GitHub REST API. In this paper we present a novel feature of GHTorrent designed to offer customisable data dumps on demand. The new GHTorrent data-on-demand service offers users the possibility to request via a web form up-to-date GHTorrent data dumps for any collection of GitHub repositories. We hope that by offering customisable GHTorrent data dumps we will not only lower the "barrier for entry" even further for researchers interested in mining GitHub data (thus encourage researchers to intensify their mining efforts), but also enhance the replicability of GitHub studies (since a snapshot of the data on which the results were obtained can now easily accompany each study).
- **Main contribution:** In recent years, GitHub has become the largest code host in the world, with more than 5M developers collaborating across 10M repositories. Numerous popular open source projects (such as Ruby on Rails, Homebrew, Bootstrap, Django or jQuery) have chosen GitHub as their host and have migrated their code base to it.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Repository discovery, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 4. The promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597074`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597074
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software. However, so far there have been no studies describing the quality and properties of the data available from GitHub. We document the results of an empirical study aimed at understanding the characteristics of the repositories in GitHub and how users take advantage of GitHub's main features---namely commits, pull requests, and issues. Our results indicate that, while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. We show, for example, that the majority of the projects are personal and inactive; that GitHub is also being used for free storage and as a Web hosting service; and that almost 40% of all pull requests do not appear as merged, even though they were. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 5. An in-depth study of the promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Empirical Software Engineering
- **Year:** 2015
- **DOI:** `10.1007/s10664-015-9393-5`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-015-9393-5
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data. We document the results of an empirical study aimed at understanding the characteristics of the repositories and users in GitHub; we see how users take advantage of GitHub’s main features and how their activity is tracked on GitHub and related datasets to point out misalignment between the real and mined data. Our results indicate that while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. For example, we show that the majority of the projects are personal and inactive, and that almost 40 % of all pull requests do not appear as merged even though they were. Also, approximately half of GitHub’s registered users do not have public activity, while the activity of GitHub users in repositories is not always easy to pinpoint. We use our identified perils to see if they can pose validity threats; we review selected papers from the MSR 2014 Mining Challenge and see if there are potential impacts to consider. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 6. A Systematic Mapping Study of Software Development With GitHub

- **Authors:** Cosentino, Valerio, Canovas Izquierdo, Javier L., Cabot, Jordi
- **Venue:** IEEE Access
- **Year:** 2017
- **DOI:** `10.1109/access.2017.2682323`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/access.2017.2682323
- **Verification:** YES (Crossref)
- **Abstract:** Context: GitHub, nowadays the most popular social coding platform, has become the reference for mining Open Source repositories, a growing research trend aiming at learning from previous software projects to improve the development of new ones. In the last years, a considerable amount of research papers have been published reporting findings based on data mined from GitHub. As the community continues to deepen in its understanding of software engineering thanks to the analysis performed on this platform, we believe that it is worthwhile to reflect on how research papers have addressed the task of mining GitHub and what findings they have reported. Objective: The main objective of this paper is to identify the quantity, topic, and empirical methods of research works, targeting the analysis of how software development practices are influenced by the use of a distributed social coding platform like GitHub. Method: A systematic mapping study was conducted with four research questions and assessed 80 publications from 2009 to 2016. Results: Most works focused on the interaction around coding-related tasks and project communities. We also identified some concerns about how reliable were these results based on the fact that, overall, papers used small data sets and poor sampling techniques, employed a scarce variety of methodologies and/or were hard to replicate. Conclusions: This paper attested the high activity of research work around the field of Open Source collaboration, especially in the software domain, revealed a set of shortcomings and proposed some actions to mitigate them. We hope that this paper can also create the basis for additional studies on other collaborative activities (like book writing for instance) that are also moving to GitHub.
- **Main contribution:** Context: GitHub, nowadays the most popular social coding platform, has become the reference for mining Open Source repositories, a growing research trend aiming at learning from previous software projects to improve the development of new ones. In the last years, a considerable amount of research papers have been published reporting findings based on data mined from GitHub.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 7. DéjàVu: a map of code duplicates on GitHub

- **Authors:** Lopes, Cristina V., Maj, Petr, Martins, Pedro, Saini, Vaibhav, Yang, Di, Zitny, Jakub, Sajnani, Hitesh, Vitek, Jan
- **Venue:** Proceedings of the ACM on Programming Languages
- **Year:** 2017
- **DOI:** `10.1145/3133908`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3133908
- **Verification:** YES (Crossref)
- **Abstract:** Previous studies have shown that there is a non-trivial amount of duplication in source code. This paper analyzes a corpus of 4.5 million non-fork projects hosted on GitHub representing over 428 million files written in Java, C++, Python, and JavaScript. We found that this corpus has a mere 85 million unique files. In other words, 70% of the code on GitHub consists of clones of previously created files. There is considerable variation between language ecosystems. JavaScript has the highest rate of file duplication, only 6% of the files are distinct. Java, on the other hand, has the least duplication, 60% of files are distinct. Lastly, a project-level analysis shows that between 9% and 31% of the projects contain at least 80% of files that can be found elsewhere. These rates of duplication have implications for systems built on open source software as well as for researchers interested in analyzing large code bases. As a concrete artifact of this study, we have created DéjàVu, a publicly available map of code duplicates in GitHub repositories.
- **Main contribution:** Previous studies have shown that there is a non-trivial amount of duplication in source code. This paper analyzes a corpus of 4.5 million non-fork projects hosted on GitHub representing over 428 million files written in Java, C++, Python, and JavaScript.
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 8. Promises and Perils of Inferring Personality on GitHub

- **Authors:** van Mil, Frenk C.J., Rastogi, Ayushi, Zaidman, Andy
- **Venue:** Proceedings of the 15th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)
- **Year:** 2021
- **DOI:** `10.1145/3475716.3475775`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3475716.3475775
- **Verification:** YES (Crossref)
- **Abstract:** Background: Personality plays a pivotal role in our understanding of human actions and behavior. Today, the applications of personality are widespread, built on the solutions from psychology to infer personality. Aim: In software engineering, for instance, one widely used solution to infer personality uses textual communication data. As studies on personality in software engineering continue to grow, it is imperative to understand the performance of these solutions. Method: This paper compares the inferential ability of three widely studied text-based personality tests against each other and the ground truth on GitHub. We explore the challenges and potential solutions to improve the inferential ability of personality tests. Results: Our study shows that solutions for inferring personality are far from being perfect. Software engineering communications data can infer individual developer personality with an average error rate of 41%. In the best case, the error rate can be reduced up to 36% by following our recommendations1.
- **Main contribution:** Background: Personality plays a pivotal role in our understanding of human actions and behavior. Today, the applications of personality are widespread, built on the solutions from psychology to infer personality.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — supporting citation

### 9. Sampling Projects in GitHub for MSR Studies

- **Authors:** Dabic, Ozren, Aghajani, Emad, Bavota, Gabriele
- **Venue:** 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)
- **Year:** 2021
- **DOI:** `10.1109/msr52588.2021.00074`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr52588.2021.00074
- **Verification:** YES (Crossref)
- **Abstract:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal. For example, a study related to licensing might be interested in selecting projects explicitly declaring a license. Once the selection criteria have been defined, utilities such as the GitHub APIs can be used to "query" the hosting service. However, researchers have to deal with usage limitations imposed by these APIs and a lack of required information. For example, the GitHub search APIs allow 30 requests per minute and, when searching repositories, only provide limited information (e.g., the number of commits in a repository is not included). To support researchers in sampling projects from GitHub, we present GHS (GitHub Search), a dataset containing 25 characteristics (e.g., number of commits, license, etc.) of 735,669 repositories written in 10 programming languages. The set of characteristics has been derived by looking for frequently used project selection criteria in MSR studies and the dataset is continuously updated to (i) always provide fresh data about the existing projects, and (ii) increase the number of indexed projects. The GHS dataset can be queried through a web application we built that allows to set many combinations of selection criteria needed for a study and download the information of matching repositories: https://seart-ghs.si.usi.ch.
- **Main contribution:** Almost every Mining Software Repositories (MSR) study requires, as first step, the selection of the subject software repositories. These repositories are usually collected from hosting services like GitHub using specific selection criteria dictated by the study goal.
- **Relation with our paper:** Empirical study of how MSR papers sample GitHub projects. Topic mapping: Repository sampling, Sampling methodology, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 10. The promises and perils of open source software release and usage by government – evidence from GitHub and literature

- **Authors:** Eibl, Gregor, Thurnay, Lőrinc
- **Venue:** Proceedings of the 24th Annual International Conference on Digital Government Research
- **Year:** 2023
- **DOI:** `10.1145/3598469.3598489`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3598469.3598489
- **Verification:** YES (Crossref)
- **Abstract:** Abstract: Open Source Software (OSS) is extensively utilized in industry and government because it allows for open access to the source code and allows for external involvement in the software development process. There are several factors driving this movement in a government setting, making it difficult to assess the adoption's success. Through a study of billions of rows of GitHub activity data, this research analyzes the production of OSS by administrations in German-speaking countries in detail and analyses the motivating factors and challenges to OSS adoption through a literature review. Similar studies have been conducted in other nations, with somewhat different approaches, foci, and different ways to identify public GitHub users as well as insiders and outsiders of OSS projects. 16 consequences of OSS usage and development are listed in the paper. On GitHub, we found 1021 OSS projects run by public agencies in largly German-speaking nations. We then compiled a list of the most popular projects based on commits and the most active public agencies in terms of projects. The research also finds automatic contributions by bots, which have not been taken into account in the literature so far, and demonstrates highly substantial positive correlations between commits, forks, and stars as proxy for the popularity of these projects. This research introduces a new method for identifying government organizations in OSS platforms and illuminates the possible positive and negative effects of the public sector's release and adoption of open source software.
- **Main contribution:** Abstract: Open Source Software (OSS) is extensively utilized in industry and government because it allows for open access to the source code and allows for external involvement in the software development process. There are several factors driving this movement in a government setting, making it difficult to assess the adoption's success.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — supporting citation

### 11. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **Authors:** Jimenez, Carlos E., Yang, John, Wettig, Alexander, Yao, Shunyu, Pei, Kexin, Press, Ofir, Narasimhan, Karthik R.
- **Venue:** ICLR
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** OpenReview
- **URL:** https://openreview.net/forum?id=VTF8yNQM66
- **Verification:** YES-OPENREVIEW (OpenReview + arXiv:2310.06770)
- **Abstract:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Main contribution:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Relation with our paper:** Topic mapping: Benchmark construction, Dataset construction, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — influential benchmark (OpenReview/ICLR; no Crossref DOI)


## Topic 11. Dataset construction

_Verified entries in this topic after curation: **10**_

### 1. Evaluating defect prediction approaches: a benchmark and an extensive comparison

- **Authors:** D’Ambros, Marco, Lanza, Michele, Robbes, Romain
- **Venue:** Empirical Software Engineering
- **Year:** 2011
- **DOI:** `10.1007/s10664-011-9173-9`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-011-9173-9
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Evaluating defect prediction approaches: a benchmark and an extensive comparison” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Dataset construction, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. Data Quality: Some Comments on the NASA Software Defect Datasets

- **Authors:** Shepperd, Martin, Song, Qinbao, Sun, Zhongbin, Mair, Carolyn
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2013
- **DOI:** `10.1109/tse.2013.11`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2013.11
- **Verification:** YES (Crossref)
- **Abstract:** Background--Self-evidently empirical analyses rely upon the quality of their data. Likewise, replications rely upon accurate reporting and using the same rather than similar versions of datasets. In recent years, there has been much interest in using machine learners to classify software modules into defect-prone and not defect-prone categories. The publicly available NASA datasets have been extensively used as part of this research. Objective--This short note investigates the extent to which published analyses based on the NASA defect datasets are meaningful and comparable. Method--We analyze the five studies published in the IEEE Transactions on Software Engineering since 2007 that have utilized these datasets and compare the two versions of the datasets currently in use. Results--We find important differences between the two versions of the datasets, implausible values in one dataset and generally insufficient detail documented on dataset preprocessing. Conclusions--It is recommended that researchers 1) indicate the provenance of the datasets they use, 2) report any preprocessing in sufficient detail to enable meaningful replication, and 3) invest effort in understanding the data prior to applying machine learners.
- **Main contribution:** Background--Self-evidently empirical analyses rely upon the quality of their data. Likewise, replications rely upon accurate reporting and using the same rather than similar versions of datasets.
- **Relation with our paper:** Topic mapping: Dataset construction, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. The impact of tangled code changes

- **Authors:** Herzig, Kim, Zeller, Andreas
- **Venue:** 2013 10th Working Conference on Mining Software Repositories (MSR)
- **Year:** 2013
- **DOI:** `10.1109/msr.2013.6624018`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2013.6624018
- **Verification:** YES (Crossref)
- **Abstract:** When interacting with version control systems, developers often commit unrelated or loosely related code changes in a single transaction. When analyzing the version history, such tangled changes will make all changes to all modules appear related, possibly compromising the resulting analyses through noise and bias. In an investigation of five open-source Java projects, we found up to 15% of all bug fixes to consist of multiple tangled changes. Using a multi-predictor approach to untangle changes, we show that on average at least 16.6% of all source files are incorrectly associated with bug reports. We recommend better change organization to limit the impact of tangled changes.
- **Main contribution:** When interacting with version control systems, developers often commit unrelated or loosely related code changes in a single transaction. When analyzing the version history, such tangled changes will make all changes to all modules appear related, possibly compromising the resulting analyses through noise and bias.
- **Relation with our paper:** Topic mapping: Construct validity, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. Researcher Bias: The Use of Machine Learning in Software Defect Prediction

- **Authors:** Shepperd, Martin, Bowes, David, Hall, Tracy
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2014
- **DOI:** `10.1109/tse.2014.2322358`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2014.2322358
- **Verification:** YES (Crossref)
- **Abstract:** Background. The ability to predict defect-prone software components would be valuable. Consequently, there have been many empirical studies to evaluate the performance of different techniques endeavouring to accomplish this effectively. However no one technique dominates and so designing a reliable defect prediction model remains problematic. Objective. We seek to make sense of the many conflicting experimental results and understand which factors have the largest effect on predictive performance. Method. We conduct a meta-analysis of all relevant, high quality primary studies of defect prediction to determine what factors influence predictive performance. This is based on 42 primary studies that satisfy our inclusion criteria that collectively report 600 sets of empirical prediction results. By reverse engineering a common response variable we build a random effects ANOVA model to examine the relative contribution of four model building factors (classifier, data set, input metrics and researcher group) to model prediction performance. Results. Surprisingly we find that the choice of classifier has little impact upon performance (1.3 percent) and in contrast the major (31 percent) explanatory factor is the researcher group. It matters more who does the work than what is done. Conclusion. To overcome this high level of researcher bias, defect prediction researchers should (i) conduct blind analysis, (ii) improve reporting protocols and (iii) conduct more intergroup studies in order to alleviate expertise issues. Lastly, research is required to determine whether this bias is prevalent in other applications domains.
- **Main contribution:** Background. The ability to predict defect-prone software components would be valuable.
- **Relation with our paper:** Topic mapping: Internal validity, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 5. Curating GitHub for engineered software projects

- **Authors:** Munaiah, Nuthan, Kroh, Steven, Cabrey, Craig, Nagappan, Meiyappan
- **Venue:** Empirical Software Engineering
- **Year:** 2017
- **DOI:** `10.1007/s10664-017-9512-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-017-9512-6
- **Verification:** YES (Crossref)
- **Abstract:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa. However, the simplicity in querying comes with a caveat: there are limited means of separating the signal (e.g. repositories containing engineered software projects) from the noise (e.g. repositories containing home work assignments). The proportion of noise in a random sample of repositories could skew the study and may lead to researchers reaching unrealistic, potentially inaccurate, conclusions. We argue that it is imperative to have the ability to sieve out the noise in such large repository forges. We propose a framework, and present a reference implementation of the framework as a tool called reaper, to enable researchers to select GitHub repositories that contain evidence of an engineered software project. We identify software engineering practices (called dimensions) and propose means for validating their existence in a GitHub repository. We used reaper to measure the dimensions of 1,857,423 GitHub repositories. We then used manually classified data sets of repositories to train classifiers capable of predicting if a given GitHub repository contains an engineered software project. The performance of the classifiers was evaluated using a set of 200 repositories with known ground truth classification. We also compared the performance of the classifiers to other approaches to classification (e.g. number of GitHub Stargazers) and found our classifiers to outperform existing approaches. We found stargazers-based classifier (with 10 as the threshold for number of stargazers) to exhibit high precision (97%) but an inversely proportional recall (32%). On the other hand, our best classifier exhibited a high precision (82%) and a high recall (86%). The stargazer-based criteria offers precision but fails to recall a significant portion of the population.
- **Main contribution:** Software forges like GitHub host millions of repositories. Software engineering researchers have been able to take advantage of such a large corpora of potential study subjects with the help of tools like GHTorrent and Boa.
- **Relation with our paper:** Closest curation cousin (engineered vs non-engineered); related but different construct from our analytic-population membership. Topic mapping: Repository sampling, Sampling methodology, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Engineered status is neither necessary nor sufficient for instruction-artifact analytic-population membership.
- **Should be cited:** YES — cite in Related Work

### 6. PHANTOM: Curating GitHub for engineered software projects using time-series clustering

- **Authors:** Pickerill, Peter, Jungen, Heiko Joshua, Ochodek, Mirosław, Maćkowiak, Michał, Staron, Miroslaw
- **Venue:** Empirical Software Engineering
- **Year:** 2020
- **DOI:** `10.1007/s10664-020-09825-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-020-09825-8
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Within the field of Mining Software Repositories, there are numerous methods employed to filter datasets in order to avoid analysing low-quality projects. Unfortunately, the existing filtering methods have not kept up with the growth of existing data sources, such as GitHub, and researchers often rely on quick and dirty techniques to curate datasets. Objective The objective of this study is to develop a method capable of filtering large quantities of software projects in a resource-efficient way. Method This study follows the Design Science Research (DSR) methodology. The proposed method, PHANTOM, extracts five measures from Git logs. Each measure is transformed into a time-series, which is represented as a feature vector for clustering using the k-means algorithm. Results Using the ground truth from a previous study, PHANTOM was shown to be able to rediscover the ground truth on the training dataset, and was able to identify “engineered” projects with up to 0.87 Precision and 0.94 Recall on the validation dataset. PHANTOM downloaded and processed the metadata of 1,786,601 GitHub repositories in 21.5 days using a single personal computer, which is over 33% faster than the previous study which used a computer cluster of 200 nodes. The possibility of applying the method outside of the open-source community was investigated by curating 100 repositories owned by two companies. Conclusions It is possible to use an unsupervised approach to identify engineered projects. PHANTOM was shown to be competitive compared to the existing supervised approaches while reducing the hardware requirements by two orders of magnitude.
- **Main contribution:** Abstract Context Within the field of Mining Software Repositories, there are numerous methods employed to filter datasets in order to avoid analysing low-quality projects. Unfortunately, the existing filtering methods have not kept up with the growth of existing data sources, such as GitHub, and researchers often rely on quick and dirty techniques to curate datasets.
- **Relation with our paper:** Closest curation cousin (engineered vs non-engineered); related but different construct from our analytic-population membership. Topic mapping: Repository sampling, Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Engineered status is neither necessary nor sufficient for instruction-artifact analytic-population membership.
- **Should be cited:** YES — cite in Related Work

### 7. A ground-truth dataset and classification model for detecting bots in GitHub issue and PR comments

- **Authors:** Golzadeh, Mehdi, Decan, Alexandre, Legay, Damien, Mens, Tom
- **Venue:** Journal of Systems and Software
- **Year:** 2021
- **DOI:** `10.1016/j.jss.2021.110911`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2021.110911
- **Verification:** YES (Crossref)
- **Abstract:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments. While detecting their presence is important for many reasons, no large and representative ground-truth dataset is available, nor are classification models to detect and validate bots on the basis of such a dataset. This paper proposes such a ground-truth dataset, based on a manual analysis with high interrater agreement, of pull request and issue comments in 5,000 distinct Github accounts of which 527 accounts have been identified as bots. Using this dataset we propose an automated classification model based on the random forest classifier, taking as main features the number of empty and non-empty comments of each account, the number of comment patterns, and the inequality between comments within comment patterns. We obtained a very high accuracy (weighted F1-score of 0.99) on the remaining test set containing 40% of the data. Only 8 out of 211 bots in the test set are misclassified as humans. We integrated the classification model into an open source command-line tool, to allow practitioners to detect which accounts in a given Github repository actually correspond to bots.
- **Main contribution:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments.
- **Relation with our paper:** Topic mapping: Dataset construction, Metadata quality, Human annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 8. Problems with SZZ and features: An empirical study of the state of practice of defect prediction data collection

- **Authors:** Herbold, Steffen, Trautsch, Alexander, Trautsch, Fabian, Ledel, Benjamin
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10092-4`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10092-4
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context The SZZ algorithm is the de facto standard for labeling bug fixing commits and finding inducing changes for defect prediction data. Recent research uncovered potential problems in different parts of the SZZ algorithm. Most defect prediction data sets provide only static code metrics as features, while research indicates that other features are also important. Objective We provide an empirical analysis of the defect labels created with the SZZ algorithm and the impact of commonly used features on results. Method We used a combination of manual validation and adopted or improved heuristics for the collection of defect data. We conducted an empirical study on 398 releases of 38 Apache projects. Results We found that only half of the bug fixing commits determined by SZZ are actually bug fixing. If a six-month time frame is used in combination with SZZ to determine which bugs affect a release, one file is incorrectly labeled as defective for every file that is correctly labeled as defective. In addition, two defective files are missed. We also explored the impact of the relatively small set of features that are available in most defect prediction data sets, as there are multiple publications that indicate that, e.g., churn related features are important for defect prediction. We found that the difference of using more features is not significant. Conclusion Problems with inaccurate defect labels are a severe threat to the validity of the state of the art of defect prediction. Small feature sets seem to be a less severe threat.
- **Main contribution:** Abstract Context The SZZ algorithm is the de facto standard for labeling bug fixing commits and finding inducing changes for defect prediction data. Recent research uncovered potential problems in different parts of the SZZ algorithm.
- **Relation with our paper:** Topic mapping: Dataset construction, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 9. PI-Link: A Ground-Truth Dataset of Links Between Pull-Requests and Issues in GitHub

- **Authors:** Alshara, Zakarea, Shatnawi, Anas, Eyal-Salman, Hamzeh, Seriai, Abdelhak-Djamel, Shatnawi, Maad
- **Venue:** IEEE Access
- **Year:** 2023
- **DOI:** `10.1109/access.2022.3232982`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/access.2022.3232982
- **Verification:** YES (Crossref)
- **Abstract:** GitHub hosts Git repositories and provides issues-tracking services to provide a better collaboration environment for software developers. Issues and Pull-Requests are frequently used in GitHub to discuss and review the software requirements (new features, bugs, etc.) and software solutions (source code, test cases, etc.) respectively. The links between Issues and their corresponding Pull-Requests comprise valuable information to keep tracking current development as well as documenting knowledge for future development. Considering a large number of links, such information can be used to train machine learning models for several purposes such as feature location, bug prediction and localization, recommendation systems and documentation generation. To the best of our knowledge, no dataset has been proposed as a ground-truth of links between Issues and Pull-Requests. In this paper, we propose, PI-Link, a new significant and reliable ground-truth dataset composed of 50369 links that explicitly connect 34732 Issues with 50369 Pull-Requests. These links are automatically extracted from all (907,139) Android projects in GitHub created between January 1, 2011 and January 1, 2021. To better organize and store the collected data, we propose a metamodel based on the concepts of Issues and Pull Requests. Moreover, we analyze the relationships between Issues and their linked Pull Requests based on four features related to their titles, bodies, labels and comments. The selected features are analyzed in terms of their lengths and similarities based on three lexical and one semantic similarity metrics. The results showed promising similarities between Issues and their linked PRs at the lexical and semantic levels. In addition, some feature similarities are sensitive to the text length, whereas other feature similarities are sensitive to the term frequency.
- **Main contribution:** GitHub hosts Git repositories and provides issues-tracking services to provide a better collaboration environment for software developers. Issues and Pull-Requests are frequently used in GitHub to discuss and review the software requirements (new features, bugs, etc.) and software solutions (source code, test cases, etc.) respectively.
- **Relation with our paper:** Topic mapping: Dataset construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 10. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **Authors:** Jimenez, Carlos E., Yang, John, Wettig, Alexander, Yao, Shunyu, Pei, Kexin, Press, Ofir, Narasimhan, Karthik R.
- **Venue:** ICLR
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** OpenReview
- **URL:** https://openreview.net/forum?id=VTF8yNQM66
- **Verification:** YES-OPENREVIEW (OpenReview + arXiv:2310.06770)
- **Abstract:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Main contribution:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Relation with our paper:** Topic mapping: Benchmark construction, Dataset construction, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — influential benchmark (OpenReview/ICLR; no Crossref DOI)


## Topic 12. Benchmark construction

_Verified entries in this topic after curation: **12**_

### 1. Evaluating defect prediction approaches: a benchmark and an extensive comparison

- **Authors:** D’Ambros, Marco, Lanza, Michele, Robbes, Romain
- **Venue:** Empirical Software Engineering
- **Year:** 2011
- **DOI:** `10.1007/s10664-011-9173-9`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-011-9173-9
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Evaluating defect prediction approaches: a benchmark and an extensive comparison” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Dataset construction, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. An Empirical Comparison of Model Validation Techniques for Defect Prediction Models

- **Authors:** Tantithamthavorn, Chakkrit, McIntosh, Shane, Hassan, Ahmed E., Matsumoto, Kenichi
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2017
- **DOI:** `10.1109/tse.2016.2584050`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2016.2584050
- **Verification:** YES (Crossref)
- **Abstract:** Defect prediction models help software quality assurance teams to allocate their limited resources to the most defect-prone modules. Model validation techniques, such as <inline-formula><tex-math notation="LaTeX">$k$</tex-math> </inline-formula> -fold cross-validation, use historical data to estimate how well a model will perform in the future. However, little is known about how accurate the estimates of model validation techniques tend to be. In this paper, we investigate the bias and variance of model validation techniques in the domain of defect prediction. Analysis of 101 public defect datasets suggests that 77 percent of them are highly susceptible to producing unstable results– - selecting an appropriate model validation technique is a critical experimental design choice. Based on an analysis of 256 studies in the defect prediction literature, we select the 12 most commonly adopted model validation techniques for evaluation. Through a case study of 18 systems, we find that single-repetition holdout validation tends to produce estimates with 46-229 percent more bias and 53-863 percent more variance than the top-ranked model validation techniques. On the other hand, out-of-sample bootstrap validation yields the best balance between the bias and variance of estimates in the context of our study. Therefore, we recommend that future defect prediction studies avoid single-repetition holdout validation, and instead, use out-of-sample bootstrap validation.
- **Main contribution:** Defect prediction models help software quality assurance teams to allocate their limited resources to the most defect-prone modules. Model validation techniques, such as <inline-formula><tex-math notation="LaTeX">$k$</tex-math> </inline-formula> -fold cross-validation, use historical data to estimate how well a model will perform in the future.
- **Relation with our paper:** Topic mapping: Internal validity, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. Comments on ScottKnottESD in response to "An empirical comparison of model validation techniques for defect prediction models"

- **Authors:** Herbold, Steffen
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2017
- **DOI:** `10.1109/tse.2017.2748129`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2017.2748129
- **Verification:** YES (Crossref)
- **Abstract:** In this article, we discuss the ScottKnottESD test, which was proposed in a recent paper “An Empirical Comparison of Model Validation Techniques for Defect Prediction Models” that was published in this journal. We discuss the implications and the empirical impact of the proposed normality correction of ScottKnottESD and come to the conclusion that this correction does not necessarily lead to the fulfillment of the assumptions of the original Scott-Knott test and may cause problems with the statistical analysis.
- **Main contribution:** In this article, we discuss the ScottKnottESD test, which was proposed in a recent paper “An Empirical Comparison of Model Validation Techniques for Defect Prediction Models” that was published in this journal. We discuss the implications and the empirical impact of the proposed normality correction of ScottKnottESD and come to the conclusion that this correction does not necessarily lead to the fulfillment of the assumptions of the original S...
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. A Comparative Study to Benchmark Cross-Project Defect Prediction Approaches

- **Authors:** Herbold, Steffen, Trautsch, Alexander, Grabowski, Jens
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2018
- **DOI:** `10.1109/tse.2017.2724538`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2017.2724538
- **Verification:** YES (Crossref)
- **Abstract:** Cross-Project Defect Prediction (CPDP) as a means to focus quality assurance of software projects was under heavy investigation in recent years. However, within the current state-of-the-art it is unclear which of the many proposals performs best due to a lack of replication of results and diverse experiment setups that utilize different performance metrics and are based on different underlying data. Within this article, we provide a benchmark for CPDP. We replicate 24 approaches proposed by researchers between 2008 and 2015 and evaluate their performance on software products from five different data sets. Based on our benchmark, we determined that an approach proposed by Camargo Cruz and Ochimizu (2009) based on data standardization performs best and is always ranked among the statistically significant best results for all metrics and data sets. Approaches proposed by Turhan et al. (2009), Menzies et al. (2011), and Watanabe et al. (2008) are also nearly always among the best results. Moreover, we determined that predictions only seldom achieve a high performance of 0.75 recall, precision, and accuracy. Thus, CPDP still has not reached a point where the performance of the results is sufficient for the application in practice.
- **Main contribution:** Cross-Project Defect Prediction (CPDP) as a means to focus quality assurance of software projects was under heavy investigation in recent years. However, within the current state-of-the-art it is unclear which of the many proposals performs best due to a lack of replication of results and diverse experiment setups that utilize different performance metrics and are based on different underlying data.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 5. A comparative study to benchmark cross-project defect prediction approaches

- **Authors:** Herbold, Steffen, Trautsch, Alexander, Grabowski, Jens
- **Venue:** Proceedings of the 40th International Conference on Software Engineering
- **Year:** 2018
- **DOI:** `10.1145/3180155.3182542`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3180155.3182542
- **Verification:** YES (Crossref)
- **Abstract:** Cross-Project Defect Prediction (CPDP) as a means to focus quality assurance of software projects was under heavy investigation in recent years. However, within the current state-of-the-art it is unclear which of the many proposals performs best due to a lack of replication of results and diverse experiment setups that utilize different performance metrics and are based on different underlying data. Within this article, we provide a benchmark for CPDP. We replicate 24 approaches proposed by researchers between 2008 and 2015 and evaluate their performance on software products from five different data sets. Based on our benchmark, we determined that an approach proposed by Camargo Cruz and Ochimizu (2009) based on data standardization performs best and is always ranked among the statistically significant best results for all metrics and data sets. Approaches proposed by Turhan et al. (2009), Menzies et al. (2011), and Watanabe et al. (2008) are also nearly always among the best results. Moreover, we determined that predictions only seldom achieve a high performance of 0.75 recall, precision, and accuracy. Thus, CPDP still has not reached a point where the performance of the results is sufficient for the application in practice.
- **Main contribution:** Cross-Project Defect Prediction (CPDP) as a means to focus quality assurance of software projects was under heavy investigation in recent years. However, within the current state-of-the-art it is unclear which of the many proposals performs best due to a lack of replication of results and diverse experiment setups that utilize different performance metrics and are based on different underlying data.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 6. Correction of “A Comparative Study to Benchmark Cross-Project Defect Prediction Approaches”

- **Authors:** Herbold, Steffen, Trautsch, Alexander, Grabowski, Jens
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2019
- **DOI:** `10.1109/tse.2018.2790413`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2018.2790413
- **Verification:** YES (Crossref)
- **Abstract:** Unfortunately, the article "A Comparative Study to Benchmark Cross-project Defect Prediction Approaches" has a problem in the statistical analysis which was pointed out almost immediately after the pre-print of the article appeared online. While the problem does not negate the contribution of the the article and all key findings remain the same, it does alter some rankings of approaches used in the study. Within this correction, we will explain the problem, how we resolved it, and present the updated results.
- **Main contribution:** Unfortunately, the article "A Comparative Study to Benchmark Cross-project Defect Prediction Approaches" has a problem in the statistical analysis which was pointed out almost immediately after the pre-print of the article appeared online. While the problem does not negate the contribution of the the article and all key findings remain the same, it does alter some rankings of approaches used in the study.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 7. The adverse effects of code duplication in machine learning models of code

- **Authors:** Allamanis, Miltiadis
- **Venue:** Proceedings of the 2019 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software
- **Year:** 2019
- **DOI:** `10.1145/3359591.3359735`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3359591.3359735
- **Verification:** YES (Crossref)
- **Abstract:** The field of big code relies on mining large corpora of code to perform some learning task towards creating better tools for software engineers. A significant threat to this approach was recently identified by Lopes et al. (2017) who found a large amount of near-duplicate code on GitHub. However, the impact of code duplication has not been noticed by researchers devising machine learning models for source code. In this work, we explore the effects of code duplication on machine learning models showing that reported performance metrics are sometimes inflated by up to 100% when testing on duplicated code corpora compared to the performance on de-duplicated corpora which more accurately represent how machine learning models of code are used by software engineers. We present a duplication index for widely used datasets, list best practices for collecting code corpora and evaluating machine learning models on them. Finally, we release tools to help the community avoid this problem in future research.
- **Main contribution:** The field of big code relies on mining large corpora of code to perform some learning task towards creating better tools for software engineers. A significant threat to this approach was recently identified by Lopes et al.
- **Relation with our paper:** Adjacent “contamination” literature (leakage/duplication/shift), which we must disambiguate from sample–target mismatch. Topic mapping: Dataset contamination, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch.
- **Should be cited:** YES — cite in Related Work

### 8. An Empirical Study of Model-Agnostic Techniques for Defect Prediction Models

- **Authors:** Jiarpakdee, Jirayus, Tantithamthavorn, Chakkrit Kla, Dam, Hoa Khanh, Grundy, John
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2022
- **DOI:** `10.1109/tse.2020.2982385`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2020.2982385
- **Verification:** YES (Crossref)
- **Abstract:** Software analytics have empowered software organisations to support a wide range of improved decision-making and policy-making. However, such predictions made by software analytics to date have not been explained and justified. Specifically, current defect prediction models still fail to explain why models make such a prediction and fail to uphold the privacy laws in terms of the requirement to explain any decision made by an algorithm. In this paper, we empirically evaluate three model-agnostic techniques, i.e., two state-of-the-art Local Interpretability Model-agnostic Explanations technique (LIME) and BreakDown techniques, and our improvement of LIME with Hyper Parameter Optimisation (LIME-HPO). Through a case study of 32 highly-curated defect datasets that span across 9 open-source software systems, we conclude that (1) model-agnostic techniques are needed to explain individual predictions of defect models; (2) instance explanations generated by model-agnostic techniques are mostly overlapping (but not exactly the same) with the global explanation of defect models and reliable when they are re-generated; (3) model-agnostic techniques take less than a minute to generate instance explanations; and (4) more than half of the practitioners perceive that the contrastive explanations are necessary and useful to understand the predictions of defect models. Since the implementation of the studied model-agnostic techniques is available in both Python and R, we recommend model-agnostic techniques be used in the future.
- **Main contribution:** Software analytics have empowered software organisations to support a wide range of improved decision-making and policy-making. However, such predictions made by software analytics to date have not been explained and justified.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 9. Problems with SZZ and features: An empirical study of the state of practice of defect prediction data collection

- **Authors:** Herbold, Steffen, Trautsch, Alexander, Trautsch, Fabian, Ledel, Benjamin
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10092-4`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10092-4
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context The SZZ algorithm is the de facto standard for labeling bug fixing commits and finding inducing changes for defect prediction data. Recent research uncovered potential problems in different parts of the SZZ algorithm. Most defect prediction data sets provide only static code metrics as features, while research indicates that other features are also important. Objective We provide an empirical analysis of the defect labels created with the SZZ algorithm and the impact of commonly used features on results. Method We used a combination of manual validation and adopted or improved heuristics for the collection of defect data. We conducted an empirical study on 398 releases of 38 Apache projects. Results We found that only half of the bug fixing commits determined by SZZ are actually bug fixing. If a six-month time frame is used in combination with SZZ to determine which bugs affect a release, one file is incorrectly labeled as defective for every file that is correctly labeled as defective. In addition, two defective files are missed. We also explored the impact of the relatively small set of features that are available in most defect prediction data sets, as there are multiple publications that indicate that, e.g., churn related features are important for defect prediction. We found that the difference of using more features is not significant. Conclusion Problems with inaccurate defect labels are a severe threat to the validity of the state of the art of defect prediction. Small feature sets seem to be a less severe threat.
- **Main contribution:** Abstract Context The SZZ algorithm is the de facto standard for labeling bug fixing commits and finding inducing changes for defect prediction data. Recent research uncovered potential problems in different parts of the SZZ algorithm.
- **Relation with our paper:** Topic mapping: Dataset construction, Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 10. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **Authors:** Jimenez, Carlos E., Yang, John, Wettig, Alexander, Yao, Shunyu, Pei, Kexin, Press, Ofir, Narasimhan, Karthik R.
- **Venue:** ICLR
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** OpenReview
- **URL:** https://openreview.net/forum?id=VTF8yNQM66
- **Verification:** YES-OPENREVIEW (OpenReview + arXiv:2310.06770)
- **Abstract:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Main contribution:** SWE-bench evaluates language models on resolving real GitHub issues by generating patches that must pass repository tests; construction involves filtering issue–PR pairs from popular GitHub repositories.
- **Relation with our paper:** Topic mapping: Benchmark construction, Dataset construction, GitHub repository mining. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — influential benchmark (OpenReview/ICLR; no Crossref DOI)

### 11. Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Based Code Models

- **Authors:** Aleithan, Reem
- **Venue:** 2025 IEEE/ACM 47th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion)
- **Year:** 2025
- **DOI:** `10.1109/icse-companion66252.2025.00075`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icse-companion66252.2025.00075
- **Verification:** YES (Crossref)
- **Abstract:** The use of Large Language Models (LLMs) for code generation has emerged as a rapidly growing field, gaining substantial traction within software engineering. However, ensuring the reliability and accuracy of generated code requires robust evaluation frameworks. To address this gap, Carlos et al. introduced the SWE-bench dataset, which consists of 2,294 GitHub issues paired with their corresponding pull requests, collected from 12 prominent Python repositories. This dataset has become a key benchmark for evaluating code generation models, with resolution rates prominently featured on the SWE-bench leaderboard. Despite its widespread adoption, the dataset has yet to undergo a systematic reliability assessment. Motivated by this gap, we conducted the first empirical study aimed at evaluating the reliability of the SWE-Bench dataset to ensure it provides meaningful and realistic model evaluations. We centered our analysis on the highest-performing model reported on the leaderboard at the time of the study: SWE-Agent + GPT-4. A thorough investigation was conducted by comparing the model-generated patches with the corresponding pull requests from the dataset. Our findings revealed two key issues: (1) 32.67% of successful cases were influenced by solution leakage, and (2) 31.08% succeeded due to weak test cases. When these problematic instances were excluded, the resolution rate of SWE-Agent + GPT-4 dropped from 12.47% to 3.97%.
- **Main contribution:** The use of Large Language Models (LLMs) for code generation has emerged as a rapidly growing field, gaining substantial traction within software engineering. However, ensuring the reliability and accuracy of generated code requires robust evaluation frameworks.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 12. Software Traceability with Explainable Pretrained Language Models: Tracing GitHub Issues to Commits

- **Authors:** Puspa, Hanun Shaka, Ahmadiyah, Adhatus Solichah, Akbar, Rizky Januar
- **Venue:** 2025 15th International Conference on Information &amp;amp; Communication Technology and System (ICTS)
- **Year:** 2025
- **DOI:** `10.1109/icts67612.2025.11369619`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icts67612.2025.11369619
- **Verification:** YES (Crossref)
- **Abstract:** Software traceability links between issues and commits are essential for understanding software evolution, yet they are often created manually and therefore incomplete or neglected. Existing methods lack automation and explainability, limiting their practical use in development. This work proposes a transfer learning–based framework that fine-tunes pretrained language models (RoBERTa, BERT, AlBERT, and DistilBERT) using different tuning strategies, including full fine-tuning, adapter-based tuning, LoRA, and prefix tuning. Experiments were conducted on three benchmark datasets (LinkFormer, 20-MAD, and CariKado) under both disordered and time-ordered splits. The best performance was achieved by RoBERTa with full fine-tuning, reaching an F1-score of 96.4% on the random split. To enhance interpretability, we applied Local Interpretable Model-Agnostic Explanations (LIME) and Shapley Additive Explanations (SHAP). The results reveal that summaries and commit messages are the most influential features, while code diffs also play a key role according to SHAP. These findings demonstrate that our method could provide transparent insights, which makes automated traceability more practical and trustworthy for software engineering.
- **Main contribution:** Software traceability links between issues and commits are essential for understanding software evolution, yet they are often created manually and therefore incomplete or neglected. Existing methods lack automation and explainability, limiting their practical use in development.
- **Relation with our paper:** Topic mapping: Benchmark construction. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits


## Topic 13. Research artifacts

_Verified entries in this topic after curation: **8**_

### 1. Incremental Maintenance of Software Artifacts

- **Authors:** Reiss, S.P.
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2006
- **DOI:** `10.1109/tse.2006.91`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2006.91
- **Verification:** YES (Crossref)
- **Abstract:** Software is multidimensional, but the tools that support it are not. This lack of tool support causes the software artifacts representing different dimensions to evolve independently and to become inconsistent over time. In order to properly support the evolution of software, one must ensure that the different dimensions evolve concurrently. We have built a software development tool, CLIME that uses constraints implemented as database queries to ensure just this. Our approach makes the tool responsible for detecting inconsistencies between software design, specifications, documentation, source code, test cases, and other artifacts without requiring any of these to be a primary representation. The tool works incrementally as the software evolves, without imposing a particular methodology or process. It includes a front end that lets the user explore and fix current inconsistencies. This paper describes the basis for CLIME, the techniques underlying the tool, the interface provided to the programmer, the incremental maintenance of constraints between these artifacts, and our experiences
- **Main contribution:** Software is multidimensional, but the tools that support it are not. This lack of tool support causes the software artifacts representing different dimensions to evolve independently and to become inconsistent over time.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 2. Towards Gamification in Software Traceability: Between Test and Code Artifacts

- **Authors:** Meimandi Parizi, Reza, Kasem, Asem, Abdullah, Azween
- **Venue:** Proceedings of the 10th International Conference on Software Engineering and Applications
- **Year:** 2015
- **DOI:** `10.5220/0005555503930400`
- **Publisher:** SCITEPRESS - Science and and Technology Publications
- **URL:** https://doi.org/10.5220/0005555503930400
- **Verification:** YES (Crossref)
- **Abstract:** With the ever-increasing dependence of our civil and social infrastructures to the correct functioning of software systems, the need for approaches to engineer reliable and validated software systems grows rapidly. Traceability is the ability to trace the influence of one software artifact on another by linking dependencies. Test-to-code traceability (relationships between test and system code) plays a vital role in the production, verification, reliability and certification of highly software-intensive dependable systems. Prior work on test-to-code traceability in contemporary software engineering environments and tools is not satisfactory and is limited with respect to the need regarding results accuracy, lack of motivation, and high required effort by developers/testers. This paper argues that a new research is necessary to tackle the above weaknesses. Thus, it advocates for the induction of gamification concepts in software traceability, and takes a position that the use of gamificaiton metrics can contribute to software traceability tasks in validating software and critical systems. We propose a research agenda to execute this position by providing a unifying foundation for gamified software traceability that combines self-adaptive, visualization, and predictive features for trace links.
- **Main contribution:** With the ever-increasing dependence of our civil and social infrastructures to the correct functioning of software systems, the need for approaches to engineer reliable and validated software systems grows rapidly. Traceability is the ability to trace the influence of one software artifact on another by linking dependencies.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 3. The Software Heritage Graph Dataset: Public Software Development Under One Roof

- **Authors:** Pietri, Antoine, Spinellis, Diomidis, Zacchiroli, Stefano
- **Venue:** 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)
- **Year:** 2019
- **DOI:** `10.1109/msr.2019.00030`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr.2019.00030
- **Verification:** YES (Crossref)
- **Abstract:** Software Heritage is the largest existing public archive of software source code and accompanying development history: it currently spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects. This paper introduces the Software Heritage graph dataset: a fully-deduplicated Merkle DAG representation of the Software Heritage archive. The dataset links together file content identifiers, source code directories, Version Control System (VCS) commits tracking evolution over time, up to the full states of VCS repositories as observed by Software Heritage during periodic crawls. The dataset's contents come from major development forges (including GitHub and GitLab), FOSS distributions (e.g., Debian), and language-specific package managers (e.g., PyPI). Crawling information is also included, providing timestamps about when and where all archived source code artifacts have been observed in the wild. The Software Heritage graph dataset is available in multiple formats, including downloadable CSV dumps and Apache Parquet files for local use, as well as a public instance on Amazon Athena interactive query service for ready-to-use powerful analytical processing. Source code file contents are cross-referenced at the graph leaves, and can be retrieved through individual requests using the Software Heritage archive API.
- **Main contribution:** Software Heritage is the largest existing public archive of software source code and accompanying development history: it currently spans more than five billion unique source code files and one billion unique commits, coming from more than 80 million software projects. This paper introduces the Software Heritage graph dataset: a fully-deduplicated Merkle DAG representation of the Software Heritage archive.
- **Relation with our paper:** Topic mapping: Repository discovery, Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Solves retrieval/coverage/tooling, not analytic-population membership after path predicates.
- **Should be cited:** YES — cite in Related Work

### 4. Publish or perish, but do not forget your software artifacts

- **Authors:** Heumüller, Robert, Nielebock, Sebastian, Krüger, Jacob, Ortmeier, Frank
- **Venue:** Empirical Software Engineering
- **Year:** 2020
- **DOI:** `10.1007/s10664-020-09851-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-020-09851-6
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Open-science initiatives have gained substantial momentum in computer science, and particularly in software-engineering research. A critical aspect of open-science is the public availability of artifacts (e.g., tools), which facilitates the replication, reproduction, extension, and verification of results. While we experienced that many artifacts are not publicly available, we are not aware of empirical evidence supporting this subjective claim. In this article, we report an empirical study on software artifact papers (SAPs) published at the International Conference on Software Engineering (ICSE), in which we investigated whether and how researchers have published their software artifacts, and whether this had scientific impact. Our dataset comprises 789 ICSE research track papers, including 604 SAPs (76.6 %), from the years 2007 to 2017. While showing a positive trend towards artifact availability, our results are still sobering. Even in 2017, only 58.5 % of the papers that stated to have developed a software artifact made that artifact publicly available. As we did find a small, but statistically significant, positive correlation between linking to artifacts in a paper and its scientific impact in terms of citations, we hope to motivate the research community to share more artifacts. With our insights, we aim to support the advancement of open science by discussing our results in the context of existing initiatives and guidelines. In particular, our findings advocate the need for clearly communicating artifacts and the use of non-commercial, persistent archives to provide replication packages.
- **Main contribution:** Abstract Open-science initiatives have gained substantial momentum in computer science, and particularly in software-engineering research. A critical aspect of open-science is the public availability of artifacts (e.g., tools), which facilitates the replication, reproduction, extension, and verification of results.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 5. A retrospective study of one decade of artifact evaluations

- **Authors:** Winter, Stefan, Timperley, Christopher S., Hermann, Ben, Cito, Jürgen, Bell, Jonathan, Hilton, Michael, Beyer, Dirk
- **Venue:** Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
- **Year:** 2022
- **DOI:** `10.1145/3540250.3549172`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3540250.3549172
- **Verification:** YES (Crossref)
- **Abstract:** Most software engineering research involves the development of a prototype, a proof of concept, or a measurement apparatus. Together with the data collected in the research process, they are collectively referred to as research artifacts and are subject to artifact evaluation (AE) at scientific conferences. Since its initiation in the SE community at ESEC/FSE 2011, both the goals and the process of AE have evolved and today expectations towards AE are strongly linked with reproducible research results and reusable tools that other researchers can build their work on. However, to date little evidence has been provided that artifacts which have passed AE actually live up to these high expectations, i.e., to which degree AE processes contribute to AE's goals and whether the overhead they impose is justified. We aim to fill this gap by providing an in-depth analysis of research artifacts from a decade of software engineering (SE) and programming languages (PL) conferences, based on which we reflect on the goals and mechanisms of AE in our community. In summary, our analyses (1) suggest that articles with artifacts do not generally have better visibility in the community, (2) provide evidence how evaluated and not evaluated artifacts differ with respect to different quality criteria, and (3) highlight opportunities for further improving AE processes.
- **Main contribution:** Most software engineering research involves the development of a prototype, a proof of concept, or a measurement apparatus. Together with the data collected in the research process, they are collectively referred to as research artifacts and are subject to artifact evaluation (AE) at scientific conferences.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 6. Research artifacts in software engineering publications: Status and trends

- **Authors:** Liu, Mugeng, Huang, Xiaolong, He, Wei, Xie, Yibing, Zhang, Jie M., Jing, Xiang, Chen, Zhenpeng, Ma, Yun
- **Venue:** Journal of Systems and Software
- **Year:** 2024
- **DOI:** `10.1016/j.jss.2024.112032`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2024.112032
- **Verification:** YES (Crossref)
- **Abstract:** The Software Engineering (SE) community has been embracing the open science policy and encouraging researchers to disclose artifacts in their publications. However, the status and trends of artifact practice and quality remain unclear, lacking insights on further improvement. In this paper, we present an empirical study to characterize the research artifacts in SE publications. Specifically, we manually collect 1,487 artifacts from all 2,196 papers published in top-tier SE conferences (ASE, FSE, ICSE, and ISSTA) from 2017 to 2022. We investigate the common practices (e.g., URL location and format, storage websites), maintenance activities (e.g., last update time and URL validity), popularity (e.g., the number of stars on GitHub and characteristics), and quality (e.g., documentation and code smell) of these artifacts. Based on our analysis, we reveal a rise in publications providing artifacts. The usage of Zenodo for sharing artifacts has significantly increased. However, artifacts stored in GitHub tend to receive few stars, indicating a limited influence on real-world SE applications. We summarize the results and provide suggestions to different stakeholders in conjunction with current guidelines.
- **Main contribution:** The Software Engineering (SE) community has been embracing the open science policy and encouraging researchers to disclose artifacts in their publications. However, the status and trends of artifact practice and quality remain unclear, lacking insights on further improvement.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 7. Artifact Evaluations for Stronger Research Results

- **Authors:** Beyer, Dirk, Winter, Stefan
- **Venue:** Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering
- **Year:** 2025
- **DOI:** `10.1145/3696630.3728623`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3696630.3728623
- **Verification:** YES (Crossref)
- **Abstract:** Over the past decades, reports of reproducibility crises have surfaced in various scientific communities. Independent confirmations of published research results failed, casting doubt on the validity of these results. Even before the magnitude of the problem has become apparent in many domains, the software-engineering community introduced artifact evaluations, for the first time at ESEC/FSE 2011, in which research artifacts that support published results were voluntarily submitted for peer review. Since then, artifact evaluations have become immensely popular and are today being offered to authors at most software-engineering venues, where large artifact-evaluation committees handle large numbers of artifact submissions. At some venues, papers are accepted for publication only if their artifacts pass the artifact evaluation. To make sure that this enormous and important effort from our community to (a) create and (b) assess research artifacts is well-spent, knowledge and insights from successful and unsuccessful artifact-evaluation practices as well as publishing implications need to be conserved and shared with prospective participants, i.e., authors, reviewers, and organizers. Based on insights from empirical studies about artifact evaluations in the software-engineering community, from running artifact evaluations at different conferences, and from managing publication processes after artifact acceptance, this tutorial presents an overview what artifact evaluations are and how they are conducted, along with known pitfalls and established best practices to overcome them. The presented insights will be accompanied by a hands-on training session on artifact evaluation using published research artifacts. The tutorial targets prospective artifact-evaluation organizers and reviewers as well as researchers wishing to strengthen their research results through the research artifacts they create.
- **Main contribution:** Over the past decades, reports of reproducibility crises have surfaced in various scientific communities. Independent confirmations of published research results failed, casting doubt on the validity of these results.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 8. Research artifacts in secondary studies: A systematic mapping in software engineering

- **Authors:** Huotala, Aleksi, Kuutila, Miikka, Mäntylä, Mika
- **Venue:** Information and Software Technology
- **Year:** 2025
- **DOI:** `10.1016/j.infsof.2025.107830`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2025.107830
- **Verification:** YES (Crossref)
- **Abstract:** Context: Systematic reviews (SRs) summarize state-of-the-art evidence in science, including software engineering (SE). Objective: Our objective is to evaluate how SRs report research artifacts and to provide a comprehensive list of these artifacts. Method: We examined 537 secondary studies published between 2013 and 2023 to analyze the availability and reporting of research artifacts. Results: Our findings indicate that only 31.5% of the reviewed studies include research artifacts. Encouragingly, the situation is gradually improving, as our regression analysis shows a significant increase in the availability of research artifacts over time. However, in 2023, just 62.0% of secondary studies provide a research artifact while an even lower percentage, 30.4% use a permanent repository with a digital object identifier (DOI) for storage. Conclusion: To enhance transparency and reproducibility in SE research, we advocate for the mandatory publication of research artifacts in secondary studies.
- **Main contribution:** Context: Systematic reviews (SRs) summarize state-of-the-art evidence in science, including software engineering (SE). Objective: Our objective is to evaluate how SRs report research artifacts and to provide a comprehensive list of these artifacts.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation


## Topic 14. Reproducibility

_Verified entries in this topic after curation: **13**_

### 1. On the reproducibility of empirical software engineering studies based on data retrieved from development repositories

- **Authors:** González-Barahona, Jesús M., Robles, Gregorio
- **Venue:** Empirical Software Engineering
- **Year:** 2011
- **DOI:** `10.1007/s10664-011-9181-9`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-011-9181-9
- **Verification:** YES (Crossref)
- **Abstract:** Among empirical software engineering studies, those based on data retrieved from development repositories (such as those of source code management, issue tracking or communication systems) are specially suitable for reproduction. However their reproducibility status can vary a lot, from easy to almost impossible to reproduce. This paper explores which elements can be considered to characterize the reproducibility of a study in this area, and how they can be analyzed to better understand the type of reproduction studies they enable or obstruct. One of the main results of this exploration is the need of a systematic approach to asses the reproducibility of a study, due to the complexity of the processes usually involved, and the many details to be taken into account. To address this need, a methodology for assessing the reproducibility of studies is also presented and discussed, as a tool to help to raise awareness about research reproducibility in this field. The application of the methodology in practice has shown how, even for papers aimed to be reproducible, a systematic analysis raises important aspects that render reproduction difficult or impossible. We also show how, by identifying elements and attributes related to reproducibility, it can be better understood which kind of reproduction can be done for a specific study, given the description of datasets, methodologies and parameters it uses.
- **Main contribution:** Among empirical software engineering studies, those based on data retrieved from development repositories (such as those of source code management, issue tracking or communication systems) are specially suitable for reproduction. However their reproducibility status can vary a lot, from easy to almost impossible to reproduce.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 2. Replication of Empirical Studies in Software Engineering: Preliminary Findings from a Systematic Mapping Study

- **Authors:** Silva, Fabio Q. B. da, Suassuna, Marcos, Lopes, Rodrigo. F., Gouveia, Tatiana B., Franca, A. Cesar A., Oliveira, Joao Paulo N. de, Oliveira, Leonardo F.M. de, Santos, Andre L. M.
- **Venue:** 2011 Second International Workshop on Replication in Empirical Software Engineering Research
- **Year:** 2011
- **DOI:** `10.1109/reser.2011.14`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/reser.2011.14
- **Verification:** YES (Crossref)
- **Abstract:** Our goal in this study is to review the research related to the replication of empirical studies in software engineering in terms of replications of empirical studies and conceptual or theoretical work about replications. In this article we present the preliminary findings of this review, concentrating on the studies reporting replications and the related original studies. We applied the systematic review method to perform a mapping study about the current state of the replication work of empirical studies performed in software engineering research. We analyzed 16,126 articles, from which we extracted 93 articles reporting 125 replications performed between 1994 and 2010, of 76 original studies. Over 60% of the replications were performed in the last six years and 71% percent of the studies were internal replications. The topics of software construction, testing, and maintenance concentrate nearly 50% of the replication work, while software design, configuration management and software tools and methods are the topics with least replications. The number of replications grew in the last few years, but the absolute number of replications is still very small, in particular considering the breadth of topics in software engineering. Incentive to perform external replications and better standards to report empirical studies and their replications are still needed.
- **Main contribution:** Our goal in this study is to review the research related to the replication of empirical studies in software engineering in terms of replications of empirical studies and conceptual or theoretical work about replications. In this article we present the preliminary findings of this review, concentrating on the studies reporting replications and the related original studies.
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 3. Replication of empirical studies in software engineering research: a systematic mapping study

- **Authors:** da Silva, Fabio Q. B., Suassuna, Marcos, França, A. César C., Grubb, Alicia M., Gouveia, Tatiana B., Monteiro, Cleviton V. F., dos Santos, Igor Ebrahim
- **Venue:** Empirical Software Engineering
- **Year:** 2012
- **DOI:** `10.1007/s10664-012-9227-7`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-012-9227-7
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Replication of empirical studies in software engineering research: a systematic mapping study” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 4. Towards a Taxonomy of Replications in Empirical Software Engineering Research: A Research Proposal

- **Authors:** Magalhaes, Cleyton V.C. de, Silva, Fabio Q.B. da
- **Venue:** 2013 3rd International Workshop on Replication in Empirical Software Engineering Research
- **Year:** 2013
- **DOI:** `10.1109/reser.2013.10`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/reser.2013.10
- **Verification:** YES (Crossref)
- **Abstract:** Goal: We present a research proposal that aims to collect, analyze, and synthesize data towards the construction of a taxonomy of replications in empirical software engineering research. Method: We propose a cross-sectional survey with researchers that performed replications of empirical studies in software engineering. The population of participants is comprised of all researchers that published replications in software engineering and that were identified in a recently published mapping study. Expected Results: We expect to collect data from researchers that have performed different types of replications in order to support the definition of types or categories of replication using a grounded approach. Conclusion: We expect that the study proposed in this article will motivate a discussion in the empirical software engineering community about the need for a clear cut classification of types of replications among other definitions that will be investigated.
- **Main contribution:** Goal: We present a research proposal that aims to collect, analyze, and synthesize data towards the construction of a taxonomy of replications in empirical software engineering research. Method: We propose a cross-sectional survey with researchers that performed replications of empirical studies in software engineering.
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 5. Estimating development effort in Free/Open source software projects by mining software repositories: a case study of OpenStack

- **Authors:** Robles, Gregorio, González-Barahona, Jesús M., Cervigón, Carlos, Capiluppi, Andrea, Izquierdo-Cortázar, Daniel
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597107`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597107
- **Verification:** YES (Crossref)
- **Abstract:** Because of the distributed and collaborative nature of free / open source software (FOSS) projects, the development effort invested in a project is usually unknown, even after the software has been released. However, this information is becoming of major interest, especially ---but not only--- because of the growth in the number of companies for which FOSS has become relevant for their business strategy. In this paper we present a novel approach to estimate effort by considering data from source code management repositories. We apply our model to the OpenStack project, a FOSS project with more than 1,000 authors, in which several tens of companies cooperate. Based on data from its repositories and together with the input from a survey answered by more than 100 developers, we show that the model offers a simple, but sound way of obtaining software development estimations with bounded margins of error.
- **Main contribution:** Because of the distributed and collaborative nature of free / open source software (FOSS) projects, the development effort invested in a project is usually unknown, even after the software has been released. However, this information is becoming of major interest, especially ---but not only--- because of the growth in the number of companies for which FOSS has become relevant for their business strategy.
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 6. Investigations about replication of empirical studies in software engineering: A systematic mapping study

- **Authors:** de Magalhães, Cleyton V.C., da Silva, Fabio Q.B., Santos, Ronnie E.S., Suassuna, Marcos
- **Venue:** Information and Software Technology
- **Year:** 2015
- **DOI:** `10.1016/j.infsof.2015.02.001`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2015.02.001
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Investigations about replication of empirical studies in software engineering: A systematic mapping study” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 7. Replication of Empirical Studies in Software Engineering: An Update of a Systematic Mapping Study

- **Authors:** Bezerra, Roberta M. M., da Silva, Fabio Q. B., Santana, Anderson M., Magalhaes, Cleyton V. C., Santos, Ronnie E. S.
- **Venue:** 2015 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)
- **Year:** 2015
- **DOI:** `10.1109/esem.2015.7321213`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/esem.2015.7321213
- **Verification:** YES (Crossref)
- **Abstract:** Context: Current empirical research highlight the need for replications of empirical studies because replications plays an important role in the construction of scientific knowledge. Objective: Considering the importance of replications in the consolidation of the knowledge produced in the software engineering research, this study aims to update and extend the results produced in a previous mapping study seeking to discuss the current state of the replication work of empirical studies performed in software engineering research between 2011 and 2012. Method: We applied the systematic review method to search and select published papers, to extract, and synthesize data from reported replications. Results: This study analyzed more than 7,000 articles, from which 39 articles that published replications between 2011 and 2012 were selected. Data extracted from these studies were used to update the information about the replications work in software engineering. Conclusion: The number of replications increased significantly in the period, when compared to the previous mapping study. In particular, the percentage of external replications also increased, with respect to internal ones. However, several other limitations identified in the previous mapping studies are still observed in this new set of replications.
- **Main contribution:** Context: Current empirical research highlight the need for replications of empirical studies because replications plays an important role in the construction of scientific knowledge. Objective: Considering the importance of replications in the consolidation of the knowledge produced in the software engineering research, this study aims to update and extend the results produced in a previous mapping study seeking to discuss the current state of...
- **Relation with our paper:** Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — supporting citation

### 8. Reproducibility and credibility in empirical software engineering: A case study based on a systematic literature review of the use of the SZZ algorithm

- **Authors:** Rodríguez-Pérez, Gema, Robles, Gregorio, González-Barahona, Jesús M.
- **Venue:** Information and Software Technology
- **Year:** 2018
- **DOI:** `10.1016/j.infsof.2018.03.009`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2018.03.009
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Reproducibility of Empirical Software Engineering (ESE) studies is an essential part for improving their credibility, as it offers the opportunity to the research community to verify, evaluate and improve their research outcomes. Objective We aim to study reproducibility and credibility in ESE with a case study, by investigating how they have been addressed in studies where SZZ, a widely-used algorithm by Śliwerski, Zimmermann and Zeller to detect the origin of a bug, has been applied. Methodology We have performed a systematic literature review to evaluate publications that use SZZ. In total, 187 papers have been analyzed for reproducibility, reporting of limitations and use of improved versions of the algorithm. Results We have found a situation with a lot of room for improvement in ESE as reproducibility is not commonly found; factors that undermine the credibility of results are common. We offer some lessons learned and guidelines for researchers and reviewers to address this problem. Conclusion Reproducibility and other related aspects that ensure a high quality scientific process should be taken more into consideration by the ESE community in order to increase the credibility of the research results.
- **Main contribution:** Abstract Context Reproducibility of Empirical Software Engineering (ESE) studies is an essential part for improving their credibility, as it offers the opportunity to the research community to verify, evaluate and improve their research outcomes. Objective We aim to study reproducibility and credibility in ESE with a case study, by investigating how they have been addressed in studies where SZZ, a widely-used algorithm by Śliwerski, Zimmermann...
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit. Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — supporting citation

### 9. Publish or perish, but do not forget your software artifacts

- **Authors:** Heumüller, Robert, Nielebock, Sebastian, Krüger, Jacob, Ortmeier, Frank
- **Venue:** Empirical Software Engineering
- **Year:** 2020
- **DOI:** `10.1007/s10664-020-09851-6`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-020-09851-6
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Open-science initiatives have gained substantial momentum in computer science, and particularly in software-engineering research. A critical aspect of open-science is the public availability of artifacts (e.g., tools), which facilitates the replication, reproduction, extension, and verification of results. While we experienced that many artifacts are not publicly available, we are not aware of empirical evidence supporting this subjective claim. In this article, we report an empirical study on software artifact papers (SAPs) published at the International Conference on Software Engineering (ICSE), in which we investigated whether and how researchers have published their software artifacts, and whether this had scientific impact. Our dataset comprises 789 ICSE research track papers, including 604 SAPs (76.6 %), from the years 2007 to 2017. While showing a positive trend towards artifact availability, our results are still sobering. Even in 2017, only 58.5 % of the papers that stated to have developed a software artifact made that artifact publicly available. As we did find a small, but statistically significant, positive correlation between linking to artifacts in a paper and its scientific impact in terms of citations, we hope to motivate the research community to share more artifacts. With our insights, we aim to support the advancement of open science by discussing our results in the context of existing initiatives and guidelines. In particular, our findings advocate the need for clearly communicating artifacts and the use of non-commercial, persistent archives to provide replication packages.
- **Main contribution:** Abstract Open-science initiatives have gained substantial momentum in computer science, and particularly in software-engineering research. A critical aspect of open-science is the public availability of artifacts (e.g., tools), which facilitates the replication, reproduction, extension, and verification of results.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 10. A retrospective study of one decade of artifact evaluations

- **Authors:** Winter, Stefan, Timperley, Christopher S., Hermann, Ben, Cito, Jürgen, Bell, Jonathan, Hilton, Michael, Beyer, Dirk
- **Venue:** Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
- **Year:** 2022
- **DOI:** `10.1145/3540250.3549172`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3540250.3549172
- **Verification:** YES (Crossref)
- **Abstract:** Most software engineering research involves the development of a prototype, a proof of concept, or a measurement apparatus. Together with the data collected in the research process, they are collectively referred to as research artifacts and are subject to artifact evaluation (AE) at scientific conferences. Since its initiation in the SE community at ESEC/FSE 2011, both the goals and the process of AE have evolved and today expectations towards AE are strongly linked with reproducible research results and reusable tools that other researchers can build their work on. However, to date little evidence has been provided that artifacts which have passed AE actually live up to these high expectations, i.e., to which degree AE processes contribute to AE's goals and whether the overhead they impose is justified. We aim to fill this gap by providing an in-depth analysis of research artifacts from a decade of software engineering (SE) and programming languages (PL) conferences, based on which we reflect on the goals and mechanisms of AE in our community. In summary, our analyses (1) suggest that articles with artifacts do not generally have better visibility in the community, (2) provide evidence how evaluated and not evaluated artifacts differ with respect to different quality criteria, and (3) highlight opportunities for further improving AE processes.
- **Main contribution:** Most software engineering research involves the development of a prototype, a proof of concept, or a measurement apparatus. Together with the data collected in the research process, they are collectively referred to as research artifacts and are subject to artifact evaluation (AE) at scientific conferences.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 11. Leakage and the reproducibility crisis in machine-learning-based science

- **Authors:** Kapoor, Sayash, Narayanan, Arvind
- **Venue:** Patterns
- **Year:** 2023
- **DOI:** `10.1016/j.patter.2023.100804`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.patter.2023.100804
- **Verification:** YES (Crossref)
- **Abstract:** Summary Machine-learning (ML) methods have gained prominence in the quantitative sciences. However, there are many known methodological pitfalls, including data leakage, in ML-based science. We systematically investigate reproducibility issues in ML-based science. Through a survey of literature in fields that have adopted ML methods, we find 17 fields where leakage has been found, collectively affecting 294 papers and, in some cases, leading to wildly overoptimistic conclusions. Based on our survey, we introduce a detailed taxonomy of eight types of leakage, ranging from textbook errors to open research problems. We propose that researchers test for each type of leakage by filling out model info sheets, which we introduce. Finally, we conduct a reproducibility study of civil war prediction, where complex ML models are believed to vastly outperform traditional statistical models such as logistic regression (LR). When the errors are corrected, complex ML models do not perform substantively better than decades-old LR models.
- **Main contribution:** Summary Machine-learning (ML) methods have gained prominence in the quantitative sciences. However, there are many known methodological pitfalls, including data leakage, in ML-based science.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Dataset contamination, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Different contamination construct than path-search population mismatch. Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 12. Revisiting the reproducibility of empirical software engineering studies based on data retrieved from development repositories

- **Authors:** Gonzalez-Barahona, Jesus M., Robles, Gregorio
- **Venue:** Information and Software Technology
- **Year:** 2023
- **DOI:** `10.1016/j.infsof.2023.107318`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2023.107318
- **Verification:** YES (Crossref)
- **Abstract:** In 2012, our paper “On the reproducibility of empirical software engineering studies based on data retrieved from development repositories” was published. It proposed a method for assessing the reproducibility of studies based on mining software repositories (MSR studies). Since then, several approaches have happened with respect to the study of the reproducibility of this kind of studies. To revisit the proposals of that paper, analyzing to which extent they remain valid, and how they relate to current initiatives and studies on reproducibility and validation of research results in empirical software engineering. We analyze the most relevant studies affecting assumptions or consequences of the approach of the original paper, and other initiatives related to the evaluation of replicability aspects of empirical software engineering studies. We compare the results of that analysis with the results of the original study, finding similarities and differences. We also run a reproducibility assessment study on current MSR papers. Based on the comparison, and the applicability of the method to current papers, we draw conclusions on the validity of the approach of the original paper. The method proposed in the original paper is still valid, and compares well with other more recent methods. It matches the results of relevant studies on reproducibility, and a systematic comparison with them shows that our approach is aligned with their proposals. Our method has practical use, and complements well the current major initiatives on the review of reproducibility artifacts. As a side result, we learn that the reproducibility of MSR studies has improved during the last decade. We propose to use our approach as a fundamental element of a more profound review of the reproducibility of MSR studies, and of the characterization of validation studies in this realm.
- **Main contribution:** In 2012, our paper “On the reproducibility of empirical software engineering studies based on data retrieved from development repositories” was published. It proposed a method for assessing the reproducibility of studies based on mining software repositories (MSR studies).
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work

### 13. Research artifacts in software engineering publications: Status and trends

- **Authors:** Liu, Mugeng, Huang, Xiaolong, He, Wei, Xie, Yibing, Zhang, Jie M., Jing, Xiang, Chen, Zhenpeng, Ma, Yun
- **Venue:** Journal of Systems and Software
- **Year:** 2024
- **DOI:** `10.1016/j.jss.2024.112032`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2024.112032
- **Verification:** YES (Crossref)
- **Abstract:** The Software Engineering (SE) community has been embracing the open science policy and encouraging researchers to disclose artifacts in their publications. However, the status and trends of artifact practice and quality remain unclear, lacking insights on further improvement. In this paper, we present an empirical study to characterize the research artifacts in SE publications. Specifically, we manually collect 1,487 artifacts from all 2,196 papers published in top-tier SE conferences (ASE, FSE, ICSE, and ISSTA) from 2017 to 2022. We investigate the common practices (e.g., URL location and format, storage websites), maintenance activities (e.g., last update time and URL validity), popularity (e.g., the number of stars on GitHub and characteristics), and quality (e.g., documentation and code smell) of these artifacts. Based on our analysis, we reveal a rise in publications providing artifacts. The usage of Zenodo for sharing artifacts has significantly increased. However, artifacts stored in GitHub tend to receive few stars, indicating a limited influence on real-world SE applications. We summarize the results and provide suggestions to different stakeholders in conjunction with current guidelines.
- **Main contribution:** The Software Engineering (SE) community has been embracing the open science policy and encouraging researchers to disclose artifacts in their publications. However, the status and trends of artifact practice and quality remain unclear, lacking insights on further improvement.
- **Relation with our paper:** Supports releasing worksheets/frozen labels/replay scripts. Topic mapping: Research artifacts, Reproducibility. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit.
- **Should be cited:** YES — cite in Related Work


## Topic 15. Reporting guidelines

_Verified entries in this topic after curation: **6**_

### 1. Reporting guidelines for controlled experiments in software engineering

- **Authors:** Jedlitschka, A., Pfahl, D.
- **Venue:** 2005 International Symposium on Empirical Software Engineering, 2005.
- **Year:** 2005
- **DOI:** `10.1109/isese.2005.1541818`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/isese.2005.1541818
- **Verification:** YES (Crossref)
- **Abstract:** One major problem for integrating study results into a common body of knowledge is the heterogeneity of reporting styles: (1) it is difficult to locate relevant information and (2) important information is often missing. Reporting guidelines are expected to support a systematic, standardized presentation of empirical research, thus improving reporting in order to support readers in (1) finding the information they are looking for, (2) understanding how an experiment is conducted, and (3) assessing the validity of its results. The objective of this paper is to survey the most prominent published proposals for reporting guidelines, and to derive a unified standard that which can serve as a starting point for further discussion. We provide detailed guidance on the expected content of the sections and subsections for reporting a specific type of empirical studies, i.e., controlled experiments. Before the guidelines can be evaluated, feedback from the research community is required. For this purpose, we propose to adapt guideline development processes from other disciplines.
- **Main contribution:** One major problem for integrating study results into a common body of knowledge is the heterogeneity of reporting styles: (1) it is difficult to locate relevant information and (2) important information is often missing. Reporting guidelines are expected to support a systematic, standardized presentation of empirical research, thus improving reporting in order to support readers in (1) finding the information they are looking for, (2) understa...
- **Relation with our paper:** Topic mapping: Reporting guidelines. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. Guidelines for conducting and reporting case study research in software engineering

- **Authors:** Runeson, Per, Höst, Martin
- **Venue:** Empirical Software Engineering
- **Year:** 2008
- **DOI:** `10.1007/s10664-008-9102-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-008-9102-8
- **Verification:** YES (Crossref)
- **Abstract:** Case study is a suitable research methodology for software engineering research since it studies contemporary phenomena in its natural context. However, the understanding of what constitutes a case study varies, and hence the quality of the resulting studies. This paper aims at providing an introduction to case study methodology and guidelines for researchers conducting case studies and readers studying reports of such studies. The content is based on the authors’ own experience from conducting and reading case studies. The terminology and guidelines are compiled from different methodology handbooks in other research domains, in particular social science and information systems, and adapted to the needs in software engineering. We present recommended practices for software engineering case studies as well as empirically derived and evaluated checklists for researchers and readers of case study research.
- **Main contribution:** Case study is a suitable research methodology for software engineering research since it studies contemporary phenomena in its natural context. However, the understanding of what constitutes a case study varies, and hence the quality of the resulting studies.
- **Relation with our paper:** Topic mapping: Reporting guidelines, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 3. Systematic literature reviews in software engineering – A systematic literature review

- **Authors:** Kitchenham, Barbara, Pearl Brereton, O., Budgen, David, Turner, Mark, Bailey, John, Linkman, Stephen
- **Venue:** Information and Software Technology
- **Year:** 2009
- **DOI:** `10.1016/j.infsof.2008.09.009`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2008.09.009
- **Verification:** YES (Crossref)
- **Abstract:** Background: In 2004 the concept of evidence-based software engineering (EBSE) was introduced at the ICSE04 conference. Aims: This study assesses the impact of systematic literature reviews (SLRs) which are the recommended EBSE method for aggregating evidence. Method: We used the standard systematic literature review method employing a manual search of 10 journals and 4 conference proceedings. Results: Of 20 relevant studies, eight addressed research trends rather than technique evaluation. Seven SLRs addressed cost estimation. The quality of SLRs was fair with only three scoring less than 2 out of 4. Conclusions: Currently, the topic areas covered by SLRs are limited. European researchers, particularly those at the Simula Laboratory appear to be the leading exponents of systematic literature reviews. The series of cost estimation SLRs demonstrate the potential value of EBSE for synthesising evidence and making it available to practitioners.
- **Main contribution:** Background: In 2004 the concept of evidence-based software engineering (EBSE) was introduced at the ICSE04 conference. Aims: This study assesses the impact of systematic literature reviews (SLRs) which are the recommended EBSE method for aggregating evidence.
- **Relation with our paper:** Topic mapping: Reporting guidelines. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 4. Guidelines for conducting systematic mapping studies in software engineering: An update

- **Authors:** Petersen, Kai, Vakkalanka, Sairam, Kuzniarz, Ludwik
- **Venue:** Information and Software Technology
- **Year:** 2015
- **DOI:** `10.1016/j.infsof.2015.03.007`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2015.03.007
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Guidelines for conducting systematic mapping studies in software engineering: An update” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Reporting guidelines. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 5. ACM SIGSOFT Empirical Standards Released

- **Authors:** Ralph, Paul
- **Venue:** ACM SIGSOFT Software Engineering Notes
- **Year:** 2021
- **DOI:** `10.1145/3437479.3437483`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3437479.3437483
- **Verification:** YES (Crossref)
- **Abstract:** In October 2020, The ACM SIGSOFT Paper and Peer Review Quality Task Force released its first empirical standards. An empirical standard is "a brief public document that communicates expectations for a specific kind of study (e.g. a questionnaire survey)" [1]. (All quotations below are from the Empirical Standards report [1] unless otherwise noted.)
- **Main contribution:** In October 2020, The ACM SIGSOFT Paper and Peer Review Quality Task Force released its first empirical standards. An empirical standard is "a brief public document that communicates expectations for a specific kind of study (e.g.
- **Relation with our paper:** Topic mapping: Reporting guidelines. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 6. ACM SIGSOFT SEN Empirical Software Engineering: Introducing Our New Regular Column

- **Authors:** Bogner, Justus, Verdecchia, Roberto
- **Venue:** ACM SIGSOFT Software Engineering Notes
- **Year:** 2025
- **DOI:** `10.1145/3772008.3772012`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3772008.3772012
- **Verification:** YES (Crossref)
- **Abstract:** From its early foundations in the 1970s, empirical software engineering (ESE) has evolved into a mature research discipline that embraces a plethora of different topics, methodologies, and industrial practices. Despite its remarkable progress, the ESE research field still needs to keep evolving, as new impediments, shortcoming, and technologies emerge. Research reproducibility, limited external validity, subjectivity of reviews, and porting research results to industrial practices are just some examples of the drivers for improvements to ESE research. Additionally, several facets of ESE research are not documented very explicitly, which makes it difficult for newcomers to pick them up. With this new regular ACM SIGSOFT SEN column (SEN-ESE), we introduce a venue for discussing meta-aspects of ESE research, ranging from general topics such as the nature and best practices for replication packages, to more nuanced themes such as statistical methods, interview transcription tools, and publishing interdisciplinary research. Our aim for the column is to be a place where we can regularly spark conversations on ESE topics that might not often be touched upon or are left implicit. Contributions to this column will be grounded in expert interviews, focus groups, surveys, and position pieces, with the goal of encouraging reflection and improvement in how we conduct, communicate, teach, and ultimately improve ESE research. Finally, we invite feedback from the ESE community on challenging, controversial, or underexplored topics, as well as suggestions for voices you would like to hear from. While we cannot promise to act on every idea, we aim to shape this column around the community interests and are grateful for all contributions.
- **Main contribution:** From its early foundations in the 1970s, empirical software engineering (ESE) has evolved into a mature research discipline that embraces a plethora of different topics, methodologies, and industrial practices. Despite its remarkable progress, the ESE research field still needs to keep evolving, as new impediments, shortcoming, and technologies emerge.
- **Relation with our paper:** Topic mapping: Reporting guidelines. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation


## Topic 16. Metadata quality

_Verified entries in this topic after curation: **12**_

### 1. Social coding in GitHub

- **Authors:** Dabbish, Laura, Stuart, Colleen, Tsay, Jason, Herbsleb, Jim
- **Venue:** Proceedings of the ACM 2012 conference on Computer Supported Cooperative Work
- **Year:** 2012
- **DOI:** `10.1145/2145204.2145396`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2145204.2145396
- **Verification:** YES (Crossref)
- **Abstract:** Social applications on the web let users track and follow the activities of a large number of others regardless of location or affiliation. There is a potential for this transparency to radically improve collaboration and learning in complex knowledge-based activities. Based on a series of in-depth interviews with central and peripheral GitHub users, we examined the value of transparency for large-scale distributed collaborations and communities of practice. We find that people make a surprisingly rich set of social inferences from the networked activity information in GitHub, such as inferring someone else's technical goals and vision when they edit code, or guessing which of several similar projects has the best chance of thriving in the long term. Users combine these inferences into effective strategies for coordinating work, advancing technical skills and managing their reputation.
- **Main contribution:** Social applications on the web let users track and follow the activities of a large number of others regardless of location or affiliation. There is a potential for this transparency to radically improve collaboration and learning in complex knowledge-based activities.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 2. Data Quality: Some Comments on the NASA Software Defect Datasets

- **Authors:** Shepperd, Martin, Song, Qinbao, Sun, Zhongbin, Mair, Carolyn
- **Venue:** IEEE Transactions on Software Engineering
- **Year:** 2013
- **DOI:** `10.1109/tse.2013.11`
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **URL:** https://doi.org/10.1109/tse.2013.11
- **Verification:** YES (Crossref)
- **Abstract:** Background--Self-evidently empirical analyses rely upon the quality of their data. Likewise, replications rely upon accurate reporting and using the same rather than similar versions of datasets. In recent years, there has been much interest in using machine learners to classify software modules into defect-prone and not defect-prone categories. The publicly available NASA datasets have been extensively used as part of this research. Objective--This short note investigates the extent to which published analyses based on the NASA defect datasets are meaningful and comparable. Method--We analyze the five studies published in the IEEE Transactions on Software Engineering since 2007 that have utilized these datasets and compare the two versions of the datasets currently in use. Results--We find important differences between the two versions of the datasets, implausible values in one dataset and generally insufficient detail documented on dataset preprocessing. Conclusions--It is recommended that researchers 1) indicate the provenance of the datasets they use, 2) report any preprocessing in sufficient detail to enable meaningful replication, and 3) invest effort in understanding the data prior to applying machine learners.
- **Main contribution:** Background--Self-evidently empirical analyses rely upon the quality of their data. Likewise, replications rely upon accurate reporting and using the same rather than similar versions of datasets.
- **Relation with our paper:** Topic mapping: Dataset construction, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. Co-evolution of project documentation and popularity within github

- **Authors:** Aggarwal, Karan, Hindle, Abram, Stroulia, Eleni
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597120`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597120
- **Verification:** YES (Crossref)
- **Abstract:** Github is a very popular collaborative software-development platform that provides typical source-code management and issue tracking features augmented by strong social-networking features such as following developers and watching projects. These features help ``spread the word'' about individuals and projects, building the reputation of the former and increasing the popularity of the latter. In this paper, we investigate the relation between project popularity and regular, consistent documentation updates. We found strong indicators that consistently popular projects exhibited consistent documentation effort and that this effort tended to attract more documentation collaborators. We also found that frameworks required more documentation effort than libraries to achieve similar adoption success, especially in the initial phase.
- **Main contribution:** Github is a very popular collaborative software-development platform that provides typical source-code management and issue tracking features augmented by strong social-networking features such as following developers and watching projects. These features help ``spread the word'' about individuals and projects, building the reputation of the former and increasing the popularity of the latter.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 4. Influence of social and technical factors for evaluating contribution in GitHub

- **Authors:** Tsay, Jason, Dabbish, Laura, Herbsleb, James
- **Venue:** Proceedings of the 36th International Conference on Software Engineering
- **Year:** 2014
- **DOI:** `10.1145/2568225.2568315`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2568225.2568315
- **Verification:** YES (Crossref)
- **Abstract:** Open source software is commonly portrayed as a meritocracy, where decisions are based solely on their technical merit. However, literature on open source suggests a complex social structure underlying the meritocracy. Social work environments such as GitHub make the relationships between users and between users and work artifacts transparent. This transparency enables developers to better use information such as technical value and social connections when making work decisions. We present a study on open source software contribution in GitHub that focuses on the task of evaluating pull requests, which are one of the primary methods for contributing code in GitHub. We analyzed the association of various technical and social measures with the likelihood of contribution acceptance. We found that project managers made use of information signaling both good technical contribution practices for a pull request and the strength of the social connection between the submitter and project manager when evaluating pull requests. Pull requests with many comments were much less likely to be accepted, moderated by the submitter's prior interaction in the project. Well-established projects were more conservative in accepting pull requests. These findings provide evidence that developers use both technical and social information when evaluating potential contributions to open source software projects.
- **Main contribution:** Open source software is commonly portrayed as a meritocracy, where decisions are based solely on their technical merit. However, literature on open source suggests a complex social structure underlying the meritocracy.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 5. Let's talk about it: evaluating contributions through discussion in GitHub

- **Authors:** Tsay, Jason, Dabbish, Laura, Herbsleb, James
- **Venue:** Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering
- **Year:** 2014
- **DOI:** `10.1145/2635868.2635882`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2635868.2635882
- **Verification:** YES (Crossref)
- **Abstract:** Open source software projects often rely on code contributions from a wide variety of developers to extend the capabilities of their software. Project members evaluate these contributions and often engage in extended discussions to decide whether to integrate changes. These discussions have important implications for project management regarding new contributors and evolution of project requirements and direction. We present a study of how developers in open work environments evaluate and discuss pull requests, a primary method of contribution in GitHub, analyzing a sample of extended discussions around pull requests and interviews with GitHub developers. We found that developers raised issues around contributions over both the appropriateness of the problem that the submitter attempted to solve and the correctness of the implemented solution. Both core project members and third-party stakeholders discussed and sometimes implemented alternative solutions to address these issues. Different stakeholders also influenced the outcome of the evaluation by eliciting support from different communities such as dependent projects or even companies. We also found that evaluation outcomes may be more complex than simply acceptance or rejection. In some cases, although a submitter's contribution was rejected, the core team fulfilled the submitter's technical goals by implementing an alternative solution. We found that the level of a submitter's prior interaction on a project changed how politely developers discussed the contribution and the nature of proposed alternative solutions.
- **Main contribution:** Open source software projects often rely on code contributions from a wide variety of developers to extend the capabilities of their software. Project members evaluate these contributions and often engage in extended discussions to decide whether to integrate changes.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 6. The promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Proceedings of the 11th Working Conference on Mining Software Repositories
- **Year:** 2014
- **DOI:** `10.1145/2597073.2597074`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2597073.2597074
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software. However, so far there have been no studies describing the quality and properties of the data available from GitHub. We document the results of an empirical study aimed at understanding the characteristics of the repositories in GitHub and how users take advantage of GitHub's main features---namely commits, pull requests, and issues. Our results indicate that, while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. We show, for example, that the majority of the projects are personal and inactive; that GitHub is also being used for free storage and as a Web hosting service; and that almost 40% of all pull requests do not appear as merged, even though they were. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important source of software artifacts on the Internet. Researchers are starting to mine the information stored in GitHub's event logs, trying to understand how its users employ the site to collaborate on software.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 7. An in-depth study of the promises and perils of mining GitHub

- **Authors:** Kalliamvakou, Eirini, Gousios, Georgios, Blincoe, Kelly, Singer, Leif, German, Daniel M., Damian, Daniela
- **Venue:** Empirical Software Engineering
- **Year:** 2015
- **DOI:** `10.1007/s10664-015-9393-5`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-015-9393-5
- **Verification:** YES (Crossref)
- **Abstract:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data. We document the results of an empirical study aimed at understanding the characteristics of the repositories and users in GitHub; we see how users take advantage of GitHub’s main features and how their activity is tracked on GitHub and related datasets to point out misalignment between the real and mined data. Our results indicate that while GitHub is a rich source of data on software development, mining GitHub for research purposes should take various potential perils into consideration. For example, we show that the majority of the projects are personal and inactive, and that almost 40 % of all pull requests do not appear as merged even though they were. Also, approximately half of GitHub’s registered users do not have public activity, while the activity of GitHub users in repositories is not always easy to pinpoint. We use our identified perils to see if they can pose validity threats; we review selected papers from the MSR 2014 Mining Challenge and see if there are potential impacts to consider. We provide a set of recommendations for software engineering researchers on how to approach the data in GitHub.
- **Main contribution:** With over 10 million git repositories, GitHub is becoming one of the most important sources of software artifacts on the Internet. Researchers mine the information stored in GitHub’s event logs to understand how its users employ the site to collaborate on software, but so far there have been no studies describing the quality and properties of the available GitHub data.
- **Relation with our paper:** Closest classical warning that GitHub entities/metadata mislead mining samples. Topic mapping: Sampling bias, GitHub repository mining, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 8. On the popularity of GitHub software

- **Authors:** Borges, Hudson
- **Venue:** 2016 IEEE International Conference on Software Maintenance and Evolution (ICSME)
- **Year:** 2016
- **DOI:** `10.1109/icsme.2016.103`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icsme.2016.103
- **Verification:** YES (Crossref)
- **Abstract:** The document was not made available for publication as part of the conference proceedings.
- **Main contribution:** The document was not made available for publication as part of the conference proceedings.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 9. Predicting the Popularity of GitHub Repositories

- **Authors:** Borges, Hudson, Hora, Andre, Valente, Marco Tulio
- **Venue:** Proceedings of the The 12th International Conference on Predictive Models and Data Analytics in Software Engineering
- **Year:** 2016
- **DOI:** `10.1145/2972958.2972966`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2972958.2972966
- **Verification:** YES (Crossref)
- **Abstract:** GitHub is the largest source code repository in the world. It provides a git-based source code management platform and also many features inspired by social networks. For example, GitHub users can show appreciation to projects by adding stars to them. Therefore, the number of stars of a repository is a direct measure of its popularity. In this paper, we use multiple linear regressions to predict the number of stars of GitHub repositories. These predictions are useful both to repository owners and clients, who usually want to know how their projects are performing in a competitive open source development market. In a large-scale analysis, we show that the proposed models start to provide accurate predictions after being trained with the number of stars received in the last six months. Furthermore, specific models---generated using data from repositories that share the same growth trends---are recommended for repositories with slow growth and/or for repositories with less stars. Finally, we evaluate the ability to predict not the number of stars of a repository but its rank among the GitHub repositories. We found a very strong correlation between predicted and real rankings (Spearman's rho greater than 0.95).
- **Main contribution:** GitHub is the largest source code repository in the world. It provides a git-based source code management platform and also many features inspired by social networks.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 10. Understanding the Factors That Impact the Popularity of GitHub Repositories

- **Authors:** Borges, Hudson, Hora, Andre, Valente, Marco Tulio
- **Venue:** 2016 IEEE International Conference on Software Maintenance and Evolution (ICSME)
- **Year:** 2016
- **DOI:** `10.1109/icsme.2016.31`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icsme.2016.31
- **Verification:** YES (Crossref)
- **Abstract:** Software popularity is a valuable information to modern open source developers, who constantly want to know if their systems are attracting new users, if new releases are gaining acceptance, or if they are meeting user's expectations. In this paper, we describe a study on the popularity of software systems hosted at GitHub, which is the world's largest collection of open source software. GitHub provides an explicit way for users to manifest their satisfaction with a hosted repository: the stargazers button. In our study, we reveal the main factors that impact the number of stars of GitHub projects, including programming language and application domain. We also study the impact of new features on project popularity. Finally, we identify four main patterns of popularity growth, which are derived after clustering the time series representing the number of stars of 2,279 popular GitHub repositories. We hope our results provide valuable insights to developers and maintainers, which could help them on building and evolving systems in a competitive software market.
- **Main contribution:** Software popularity is a valuable information to modern open source developers, who constantly want to know if their systems are attracting new users, if new releases are gaining acceptance, or if they are meeting user's expectations. In this paper, we describe a study on the popularity of software systems hosted at GitHub, which is the world's largest collection of open source software.
- **Relation with our paper:** Topic mapping: Sampling bias, Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 11. Understanding How GitHub Supports Curation Repositories

- **Authors:** Wu, Yu, Kropczynski, Jessica, Prates, Raquel, Carroll, John
- **Venue:** Future Internet
- **Year:** 2018
- **DOI:** `10.3390/fi10030029`
- **Publisher:** MDPI AG
- **URL:** https://doi.org/10.3390/fi10030029
- **Verification:** YES (Crossref)
- **Abstract:** In recent years, software developers have started to appropriate GitHub repositories to curate resources, in order to systematically select, evaluate, and organize existing artifacts for preservation and future use. Curation behaviors in social media sites, such as users’ experiences to curate tweets from Twitter and pins on Pinterest, are well documented. However, GitHub, as a social coding platform, presents a new context for this activity, raising questions about the nature of curation on this task-driven online work site. To explore and understand curation on GitHub, we compared and contrasted curation repositories with software repositories using activity logs and analyzed the content of popular curation repositories. Our results show that: (1) curation repositories have become a favorite category of repositories in GitHub; (2) curation repositories leverage collaborative features and practices native to GitHub in new ways; (3) curation repositories collect and preserve high-quality resources for the software developers’ community. Our results suggest that curation is becoming increasingly important to the software developers’ community, and current practices can be better supported with tools designed specifically for curation.
- **Main contribution:** In recent years, software developers have started to appropriate GitHub repositories to curate resources, in order to systematically select, evaluate, and organize existing artifacts for preservation and future use. Curation behaviors in social media sites, such as users’ experiences to curate tweets from Twitter and pins on Pinterest, are well documented.
- **Relation with our paper:** Topic mapping: Metadata quality. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 12. A ground-truth dataset and classification model for detecting bots in GitHub issue and PR comments

- **Authors:** Golzadeh, Mehdi, Decan, Alexandre, Legay, Damien, Mens, Tom
- **Venue:** Journal of Systems and Software
- **Year:** 2021
- **DOI:** `10.1016/j.jss.2021.110911`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2021.110911
- **Verification:** YES (Crossref)
- **Abstract:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments. While detecting their presence is important for many reasons, no large and representative ground-truth dataset is available, nor are classification models to detect and validate bots on the basis of such a dataset. This paper proposes such a ground-truth dataset, based on a manual analysis with high interrater agreement, of pull request and issue comments in 5,000 distinct Github accounts of which 527 accounts have been identified as bots. Using this dataset we propose an automated classification model based on the random forest classifier, taking as main features the number of empty and non-empty comments of each account, the number of comment patterns, and the inequality between comments within comment patterns. We obtained a very high accuracy (weighted F1-score of 0.99) on the remaining test set containing 40% of the data. Only 8 out of 211 bots in the test set are misclassified as humans. We integrated the classification model into an open source command-line tool, to allow practitioners to detect which accounts in a given Github repository actually correspond to bots.
- **Main contribution:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments.
- **Relation with our paper:** Topic mapping: Dataset construction, Metadata quality, Human annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work


## Topic 17. Human annotation

_Verified entries in this topic after curation: **5**_

### 1. A Coefficient of Agreement for Nominal Scales

- **Authors:** Cohen, Jacob
- **Venue:** Educational and Psychological Measurement
- **Year:** 1960
- **DOI:** `10.1177/001316446002000104`
- **Publisher:** SAGE Publications
- **URL:** https://doi.org/10.1177/001316446002000104
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “A Coefficient of Agreement for Nominal Scales” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Human annotation, Consensus annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. The Measurement of Observer Agreement for Categorical Data

- **Authors:** Landis, J. Richard, Koch, Gary G.
- **Venue:** Biometrics
- **Year:** 1977
- **DOI:** `10.2307/2529310`
- **Publisher:** JSTOR
- **URL:** https://doi.org/10.2307/2529310
- **Verification:** YES (Crossref)
- **Abstract:** This paper presents a general statistical methodology for the analysis of multivariate categorical data arising from observer reliability studies. The procedure essentially involves the construction of functions of the observed proportions which are directed at the extent to which the observers agree among themselves and the construction of test statistics for hypotheses involving these functions. Tests for interobserver bias are presented in terms of first-order marginal homogeneity and measures of interobserver agreement are developed as generalized kappa-type statistics. These procedures are illustrated with a clinical diagnosis example from the epidemiological literature.
- **Main contribution:** This paper presents a general statistical methodology for the analysis of multivariate categorical data arising from observer reliability studies. The procedure essentially involves the construction of functions of the observed proportions which are directed at the extent to which the observers agree among themselves and the construction of test statistics for hypotheses involving these functions.
- **Relation with our paper:** Topic mapping: Human annotation, Consensus annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. A Coefficient of Agreement for Nominal Scales: An Asymmetric Version of Kappa

- **Authors:** Kvalseth, Tarald O.
- **Venue:** Educational and Psychological Measurement
- **Year:** 1991
- **DOI:** `10.1177/0013164491511008`
- **Publisher:** SAGE Publications
- **URL:** https://doi.org/10.1177/0013164491511008
- **Verification:** YES (Crossref)
- **Abstract:** This paper is concerned with the measurement of agreement between two observers classifying items into nominal categories, with one of the observers being viewed as the "standard". An asymmetric version of Cohen's Kappa is proposed as an appropriate measure. Properties of this measure are outlined, and a numerical example is given.
- **Main contribution:** This paper is concerned with the measurement of agreement between two observers classifying items into nominal categories, with one of the observers being viewed as the "standard". An asymmetric version of Cohen's Kappa is proposed as an appropriate measure.
- **Relation with our paper:** Topic mapping: Human annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 4. A ground-truth dataset and classification model for detecting bots in GitHub issue and PR comments

- **Authors:** Golzadeh, Mehdi, Decan, Alexandre, Legay, Damien, Mens, Tom
- **Venue:** Journal of Systems and Software
- **Year:** 2021
- **DOI:** `10.1016/j.jss.2021.110911`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2021.110911
- **Verification:** YES (Crossref)
- **Abstract:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments. While detecting their presence is important for many reasons, no large and representative ground-truth dataset is available, nor are classification models to detect and validate bots on the basis of such a dataset. This paper proposes such a ground-truth dataset, based on a manual analysis with high interrater agreement, of pull request and issue comments in 5,000 distinct Github accounts of which 527 accounts have been identified as bots. Using this dataset we propose an automated classification model based on the random forest classifier, taking as main features the number of empty and non-empty comments of each account, the number of comment patterns, and the inequality between comments within comment patterns. We obtained a very high accuracy (weighted F1-score of 0.99) on the remaining test set containing 40% of the data. Only 8 out of 211 bots in the test set are misclassified as humans. We integrated the classification model into an open source command-line tool, to allow practitioners to detect which accounts in a given Github repository actually correspond to bots.
- **Main contribution:** Bots are frequently used in Github repositories to automate repetitive activities that are part of the distributed software development process. They communicate with human actors through comments.
- **Relation with our paper:** Topic mapping: Dataset construction, Metadata quality, Human annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 5. Can LLMs Replace Manual Annotation of Software Engineering Artifacts?

- **Authors:** Ahmed, Toufique, Devanbu, Premkumar, Treude, Christoph, Pradel, Michael
- **Venue:** 2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)
- **Year:** 2025
- **DOI:** `10.1109/msr66628.2025.00086`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr66628.2025.00086
- **Verification:** YES (Crossref)
- **Abstract:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience. Meanwhile, large language models (LLMs) have recently started to demonstrate human-level performance in several areas. This paper explores the possibility of substituting costly human subjects with much cheaper LLM queries in evaluations of code and coderelated artifacts. We study this idea by applying six state-of-theart LLMs to ten annotation tasks from five datasets created by prior work, such as judging the accuracy of a natural language summary of a method or deciding whether a code change fixes a static analysis warning. Our results show that replacing some human annotation effort with LLMs can produce inter-rater agreements equal or close to human-rater agreement. To help decide when and how to use LLMs in human-subject studies, we propose model-model agreement as a predictor of whether a given task is suitable for LLMs at all, and model confidence as a means to select specific samples where LLMs can safely replace human annotators. Overall, our work is the first step toward mixed human-LLM evaluations in software engineering.
- **Main contribution:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Human annotation, Multi-annotator protocols, LLM-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit. Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work


## Topic 18. Consensus annotation

_Verified entries in this topic after curation: **5**_

### 1. A Coefficient of Agreement for Nominal Scales

- **Authors:** Cohen, Jacob
- **Venue:** Educational and Psychological Measurement
- **Year:** 1960
- **DOI:** `10.1177/001316446002000104`
- **Publisher:** SAGE Publications
- **URL:** https://doi.org/10.1177/001316446002000104
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “A Coefficient of Agreement for Nominal Scales” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Human annotation, Consensus annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. The Measurement of Observer Agreement for Categorical Data

- **Authors:** Landis, J. Richard, Koch, Gary G.
- **Venue:** Biometrics
- **Year:** 1977
- **DOI:** `10.2307/2529310`
- **Publisher:** JSTOR
- **URL:** https://doi.org/10.2307/2529310
- **Verification:** YES (Crossref)
- **Abstract:** This paper presents a general statistical methodology for the analysis of multivariate categorical data arising from observer reliability studies. The procedure essentially involves the construction of functions of the observed proportions which are directed at the extent to which the observers agree among themselves and the construction of test statistics for hypotheses involving these functions. Tests for interobserver bias are presented in terms of first-order marginal homogeneity and measures of interobserver agreement are developed as generalized kappa-type statistics. These procedures are illustrated with a clinical diagnosis example from the epidemiological literature.
- **Main contribution:** This paper presents a general statistical methodology for the analysis of multivariate categorical data arising from observer reliability studies. The procedure essentially involves the construction of functions of the observed proportions which are directed at the extent to which the observers agree among themselves and the construction of test statistics for hypotheses involving these functions.
- **Relation with our paper:** Topic mapping: Human annotation, Consensus annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. Multi-granular software annotation using file-level weak labelling

- **Authors:** Sas, Cezar, Capiluppi, Andrea
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10423-7`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10423-7
- **Verification:** YES (Crossref)
- **Abstract:** Context One of the most time-consuming tasks for developers is the comprehension of new code bases. An effective approach to aid this process is to label source code files with meaningful annotations, which can help developers understand the content and functionality of a code base quicker. However, most existing solutions for code annotation focus on project-level classification: manually labelling individual files is time-consuming, error-prone and hard to scale. Objective The work presented in this paper aims to automate the annotation of files by leveraging project-level labels; and using the file-level annotations to annotate items at larger levels of granularity, for example, packages and a whole project. Method We propose a novel approach to annotate source code files using a weak labelling approach and a subsequent hierarchical aggregation. We investigate whether this approach is effective in achieving multi-granular annotations of software projects, which can aid developers in understanding the content and functionalities of a code base more quickly. Results Our evaluation uses a combination of human assessment and automated metrics to evaluate the annotations’ quality. Our approach correctly annotated 50% of files and more than 50% of packages. Moreover, the information captured at the file-level allowed us to identify, on average, three new relevant labels for any given project. We can conclude that the proposed approach is a convenient and promising way to generate noisy (not precise) annotations for files. Furthermore, hierarchical aggregation effectively preserves the information captured at file-level, and it can be propagated to packages and the overall project itself. Conclusions We can conclude that the proposed approach is a convenient and promising way to generate noisy (not precise) annotations for files. Furthermore, hierarchical aggregation effectively preserves the information captured at file-level, and it can be propagated to packages and the overall project itself.
- **Main contribution:** Context One of the most time-consuming tasks for developers is the comprehension of new code bases. An effective approach to aid this process is to label source code files with meaningful annotations, which can help developers understand the content and functionality of a code base quicker.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Consensus annotation, Multi-annotator protocols. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** OPTIONAL — cite only if space permits

### 4. OLAF: Towards Robust LLM-Based Annotation Framework in Empirical Software Engineering

- **Authors:** Imran, Mia Mohammad, Zaman, Tarannum Shaila
- **Venue:** Proceedings of the 2026 IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering
- **Year:** 2026
- **DOI:** `10.1145/3786149.3788306`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3786149.3788306
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) are increasingly used in empirical software engineering (ESE) to automate or assist annotation tasks such as labeling commits, issues, and qualitative artifacts. Yet the reliability and reproducibility of such annotations remain underexplored. Existing studies often lack standardized measures for reliability, calibration, and drift, and frequently omit essential configuration details. We argue that LLM-based annotation should be treated as a measurement process rather than a purely automated activity. In this position paper, we outline the \textbf{Operationalization for LLM-based Annotation Framework (OLAF)}, a conceptual framework that organizes key constructs: \textit{reliability, calibration, drift, consensus, aggregation}, and \textit{transparency}. The paper aims to motivate methodological discussion and future empirical work toward more transparent and reproducible LLM-based annotation in software engineering research.
- **Main contribution:** Large Language Models (LLMs) are increasingly used in empirical software engineering (ESE) to automate or assist annotation tasks such as labeling commits, issues, and qualitative artifacts. Yet the reliability and reproducibility of such annotations remain underexplored.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Consensus annotation, Multi-annotator protocols. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** OPTIONAL — cite only if space permits

### 5. Performance analysis of AI-generated code: A case study of Copilot, Copilot Chat, CodeLlaMa, and DeepSeek-Coder models

- **Authors:** Li, Shuang, Cheng, Yuntao, Chen, Jinfu, Xuan, Jifeng, He, Sen, Shang, Weiyi
- **Venue:** Empirical Software Engineering
- **Year:** 2026
- **DOI:** `10.1007/s10664-025-10776-1`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-025-10776-1
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Performance analysis of AI-generated code: A case study of Copilot, Copilot Chat, CodeLlaMa, and DeepSeek-Coder models” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: Consensus annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol. Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** OPTIONAL — cite only if space permits


## Topic 19. Multi-annotator protocols

_Verified entries in this topic after curation: **3**_

### 1. Multi-granular software annotation using file-level weak labelling

- **Authors:** Sas, Cezar, Capiluppi, Andrea
- **Venue:** Empirical Software Engineering
- **Year:** 2023
- **DOI:** `10.1007/s10664-023-10423-7`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-023-10423-7
- **Verification:** YES (Crossref)
- **Abstract:** Context One of the most time-consuming tasks for developers is the comprehension of new code bases. An effective approach to aid this process is to label source code files with meaningful annotations, which can help developers understand the content and functionality of a code base quicker. However, most existing solutions for code annotation focus on project-level classification: manually labelling individual files is time-consuming, error-prone and hard to scale. Objective The work presented in this paper aims to automate the annotation of files by leveraging project-level labels; and using the file-level annotations to annotate items at larger levels of granularity, for example, packages and a whole project. Method We propose a novel approach to annotate source code files using a weak labelling approach and a subsequent hierarchical aggregation. We investigate whether this approach is effective in achieving multi-granular annotations of software projects, which can aid developers in understanding the content and functionalities of a code base more quickly. Results Our evaluation uses a combination of human assessment and automated metrics to evaluate the annotations’ quality. Our approach correctly annotated 50% of files and more than 50% of packages. Moreover, the information captured at the file-level allowed us to identify, on average, three new relevant labels for any given project. We can conclude that the proposed approach is a convenient and promising way to generate noisy (not precise) annotations for files. Furthermore, hierarchical aggregation effectively preserves the information captured at file-level, and it can be propagated to packages and the overall project itself. Conclusions We can conclude that the proposed approach is a convenient and promising way to generate noisy (not precise) annotations for files. Furthermore, hierarchical aggregation effectively preserves the information captured at file-level, and it can be propagated to packages and the overall project itself.
- **Main contribution:** Context One of the most time-consuming tasks for developers is the comprehension of new code bases. An effective approach to aid this process is to label source code files with meaningful annotations, which can help developers understand the content and functionality of a code base quicker.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Consensus annotation, Multi-annotator protocols. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** OPTIONAL — cite only if space permits

### 2. Can LLMs Replace Manual Annotation of Software Engineering Artifacts?

- **Authors:** Ahmed, Toufique, Devanbu, Premkumar, Treude, Christoph, Pradel, Michael
- **Venue:** 2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)
- **Year:** 2025
- **DOI:** `10.1109/msr66628.2025.00086`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr66628.2025.00086
- **Verification:** YES (Crossref)
- **Abstract:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience. Meanwhile, large language models (LLMs) have recently started to demonstrate human-level performance in several areas. This paper explores the possibility of substituting costly human subjects with much cheaper LLM queries in evaluations of code and coderelated artifacts. We study this idea by applying six state-of-theart LLMs to ten annotation tasks from five datasets created by prior work, such as judging the accuracy of a natural language summary of a method or deciding whether a code change fixes a static analysis warning. Our results show that replacing some human annotation effort with LLMs can produce inter-rater agreements equal or close to human-rater agreement. To help decide when and how to use LLMs in human-subject studies, we propose model-model agreement as a predictor of whether a given task is suitable for LLMs at all, and model confidence as a means to select specific samples where LLMs can safely replace human annotators. Overall, our work is the first step toward mixed human-LLM evaluations in software engineering.
- **Main contribution:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Human annotation, Multi-annotator protocols, LLM-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit. Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work

### 3. OLAF: Towards Robust LLM-Based Annotation Framework in Empirical Software Engineering

- **Authors:** Imran, Mia Mohammad, Zaman, Tarannum Shaila
- **Venue:** Proceedings of the 2026 IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering
- **Year:** 2026
- **DOI:** `10.1145/3786149.3788306`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3786149.3788306
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) are increasingly used in empirical software engineering (ESE) to automate or assist annotation tasks such as labeling commits, issues, and qualitative artifacts. Yet the reliability and reproducibility of such annotations remain underexplored. Existing studies often lack standardized measures for reliability, calibration, and drift, and frequently omit essential configuration details. We argue that LLM-based annotation should be treated as a measurement process rather than a purely automated activity. In this position paper, we outline the \textbf{Operationalization for LLM-based Annotation Framework (OLAF)}, a conceptual framework that organizes key constructs: \textit{reliability, calibration, drift, consensus, aggregation}, and \textit{transparency}. The paper aims to motivate methodological discussion and future empirical work toward more transparent and reproducible LLM-based annotation in software engineering research.
- **Main contribution:** Large Language Models (LLMs) are increasingly used in empirical software engineering (ESE) to automate or assist annotation tasks such as labeling commits, issues, and qualitative artifacts. Yet the reliability and reproducibility of such annotations remain underexplored.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Consensus annotation, Multi-annotator protocols. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** OPTIONAL — cite only if space permits


## Topic 20. LLM-assisted annotation

_Verified entries in this topic after curation: **3**_

### 1. ChatGPT outperforms crowd workers for text-annotation tasks

- **Authors:** Gilardi, Fabrizio, Alizadeh, Meysam, Kubli, Maël
- **Venue:** Proceedings of the National Academy of Sciences
- **Year:** 2023
- **DOI:** `10.1073/pnas.2305016120`
- **Publisher:** National Academy of Sciences
- **URL:** https://doi.org/10.1073/pnas.2305016120
- **Verification:** YES (Crossref)
- **Abstract:** Many NLP applications require manual text annotations for a variety of tasks, notably to train classifiers or evaluate the performance of unsupervised models. Depending on the size and degree of complexity, the tasks may be conducted by crowd workers on platforms such as MTurk as well as trained annotators, such as research assistants. Using four samples of tweets and news articles ( n = 6,183), we show that ChatGPT outperforms crowd workers for several annotation tasks, including relevance, stance, topics, and frame detection. Across the four datasets, the zero-shot accuracy of ChatGPT exceeds that of crowd workers by about 25 percentage points on average, while ChatGPT’s intercoder agreement exceeds that of both crowd workers and trained annotators for all tasks. Moreover, the per-annotation cost of ChatGPT is less than $0.003—about thirty times cheaper than MTurk. These results demonstrate the potential of large language models to drastically increase the efficiency of text classification.
- **Main contribution:** Many NLP applications require manual text annotations for a variety of tasks, notably to train classifiers or evaluate the performance of unsupervised models. Depending on the size and degree of complexity, the tasks may be conducted by crowd workers on platforms such as MTurk as well as trained annotators, such as research assistants.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: LLM-assisted annotation, AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work

### 2. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

- **Authors:** Zheng, Lianmin, Chiang, Wei-Lin, Sheng, Ying, Zhuang, Siyuan, Wu, Zhanghao, Zhuang, Yonghao, Lin, Zi, Li, Zhuohan, Li, Dacheng, Xing, Eric, Zhang, Hao, Gonzalez, Joseph, Stoica, Ion
- **Venue:** Advances in Neural Information Processing Systems 36
- **Year:** 2023
- **DOI:** `10.52202/075280-2020`
- **Publisher:** Neural Information Processing Systems Foundation, Inc. (NeurIPS)
- **URL:** https://doi.org/10.52202/075280-2020
- **Verification:** YES (Crossref)
- **Abstract:** Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions. We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. We then verify the agreement between LLM judges and human preferences by introducing two benchmarks: MT-bench, a multi-turn question set; and Chatbot Arena, a crowdsourced battle platform. Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans. Hence, LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain. Additionally, we show our benchmark and traditional benchmarks complement each other by evaluating several variants of LLaMA and Vicuna. The MT-bench questions, 3K expert votes, and 30K conversations with human preferences are publicly available at https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge.
- **Main contribution:** Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions.
- **Relation with our paper:** Topic mapping: LLM-assisted annotation, AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work

### 3. Can LLMs Replace Manual Annotation of Software Engineering Artifacts?

- **Authors:** Ahmed, Toufique, Devanbu, Premkumar, Treude, Christoph, Pradel, Michael
- **Venue:** 2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)
- **Year:** 2025
- **DOI:** `10.1109/msr66628.2025.00086`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/msr66628.2025.00086
- **Verification:** YES (Crossref)
- **Abstract:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience. Meanwhile, large language models (LLMs) have recently started to demonstrate human-level performance in several areas. This paper explores the possibility of substituting costly human subjects with much cheaper LLM queries in evaluations of code and coderelated artifacts. We study this idea by applying six state-of-theart LLMs to ten annotation tasks from five datasets created by prior work, such as judging the accuracy of a natural language summary of a method or deciding whether a code change fixes a static analysis warning. Our results show that replacing some human annotation effort with LLMs can produce inter-rater agreements equal or close to human-rater agreement. To help decide when and how to use LLMs in human-subject studies, we propose model-model agreement as a predictor of whether a given task is suitable for LLMs at all, and model confidence as a means to select specific samples where LLMs can safely replace human annotators. Overall, our work is the first step toward mixed human-LLM evaluations in software engineering.
- **Main contribution:** Experimental evaluations of software engineering innovations, e.g., tools and processes, often include human-subject studies as a component of a multi-pronged strategy to obtain greater generalizability of the findings. However, human-subject studies in our field are challenging, due to the cost and difficulty of finding and employing suitable subjects, ideally, professional programmers with varying degrees of experience.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: Human annotation, Multi-annotator protocols, LLM-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Addresses replayability/availability rather than sample–target fit. Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work


## Topic 21. AI-assisted annotation

_Verified entries in this topic after curation: **5**_

### 1. Guidelines for Human-AI Interaction

- **Authors:** Amershi, Saleema, Weld, Dan, Vorvoreanu, Mihaela, Fourney, Adam, Nushi, Besmira, Collisson, Penny, Suh, Jina, Iqbal, Shamsi, Bennett, Paul N., Inkpen, Kori, Teevan, Jaime, Kikin-Gil, Ruth, Horvitz, Eric
- **Venue:** Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems
- **Year:** 2019
- **DOI:** `10.1145/3290605.3300233`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3290605.3300233
- **Verification:** YES (Crossref)
- **Abstract:** Advances in artificial intelligence (AI) frame opportunities and challenges for user interface design. Principles for human-AI interaction have been discussed in the human-computer interaction community for over two decades, but more study and innovation are needed in light of advances in AI and the growing uses of AI technologies in human-facing applications. We propose 18 generally applicable design guidelines for human-AI interaction. These guidelines are validated through multiple rounds of evaluation including a user study with 49 design practitioners who tested the guidelines against 20 popular AI-infused products. The results verify the relevance of the guidelines over a spectrum of interaction scenarios and reveal gaps in our knowledge, highlighting opportunities for further research. Based on the evaluations, we believe the set of design guidelines can serve as a resource to practitioners working on the design of applications and features that harness AI technologies, and to researchers interested in the further development of human-AI interaction design principles.
- **Main contribution:** Advances in artificial intelligence (AI) frame opportunities and challenges for user interface design. Principles for human-AI interaction have been discussed in the human-computer interaction community for over two decades, but more study and innovation are needed in light of advances in AI and the growing uses of AI technologies in human-facing applications.
- **Relation with our paper:** Topic mapping: AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 2. ChatGPT outperforms crowd workers for text-annotation tasks

- **Authors:** Gilardi, Fabrizio, Alizadeh, Meysam, Kubli, Maël
- **Venue:** Proceedings of the National Academy of Sciences
- **Year:** 2023
- **DOI:** `10.1073/pnas.2305016120`
- **Publisher:** National Academy of Sciences
- **URL:** https://doi.org/10.1073/pnas.2305016120
- **Verification:** YES (Crossref)
- **Abstract:** Many NLP applications require manual text annotations for a variety of tasks, notably to train classifiers or evaluate the performance of unsupervised models. Depending on the size and degree of complexity, the tasks may be conducted by crowd workers on platforms such as MTurk as well as trained annotators, such as research assistants. Using four samples of tweets and news articles ( n = 6,183), we show that ChatGPT outperforms crowd workers for several annotation tasks, including relevance, stance, topics, and frame detection. Across the four datasets, the zero-shot accuracy of ChatGPT exceeds that of crowd workers by about 25 percentage points on average, while ChatGPT’s intercoder agreement exceeds that of both crowd workers and trained annotators for all tasks. Moreover, the per-annotation cost of ChatGPT is less than $0.003—about thirty times cheaper than MTurk. These results demonstrate the potential of large language models to drastically increase the efficiency of text classification.
- **Main contribution:** Many NLP applications require manual text annotations for a variety of tasks, notably to train classifiers or evaluate the performance of unsupervised models. Depending on the size and degree of complexity, the tasks may be conducted by crowd workers on platforms such as MTurk as well as trained annotators, such as research assistants.
- **Relation with our paper:** Evidence on (LLM-assisted) annotation quality relevant to our coding/consensus design. Topic mapping: LLM-assisted annotation, AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work

### 3. Inconsistency Detection in Natural Language Requirements using ChatGPT: a Preliminary Evaluation

- **Authors:** Fantechi, Alessandro, Gnesi, Stefania, Passaro, Lucia, Semini, Laura
- **Venue:** 2023 IEEE 31st International Requirements Engineering Conference (RE)
- **Year:** 2023
- **DOI:** `10.1109/re57278.2023.00045`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/re57278.2023.00045
- **Verification:** YES (Crossref)
- **Abstract:** With the rapid advancement of tools based on Artificial Intelligence, it is interesting to assess their usefulness in requirements engineering. In early experiments, we have seen that ChatGPT can detect inconsistency defects in natural language (NL) requirements, that traditional NLP tools cannot identify or can identify with difficulties even after domain-focused training. This study is devoted to specifically measuring the performance of ChatGPT in finding inconsistency in requirements. Positive results in this respect could lead to the use of ChatGPT to complement existing requirements analysis tools to automatically detect this important quality criterion. For this purpose, we consider GPT-3.5, the Generative Pretrained Transformer language model developed by OpenAI. We evaluate its ability to detect inconsistency by comparing its predictions with those obtained from expert judgments by students with a proven knowledge of RE issues on a few example requirements documents.
- **Main contribution:** With the rapid advancement of tools based on Artificial Intelligence, it is interesting to assess their usefulness in requirements engineering. In early experiments, we have seen that ChatGPT can detect inconsistency defects in natural language (NL) requirements, that traditional NLP tools cannot identify or can identify with difficulties even after domain-focused training.
- **Relation with our paper:** Topic mapping: AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** OPTIONAL — cite only if space permits

### 4. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

- **Authors:** Zheng, Lianmin, Chiang, Wei-Lin, Sheng, Ying, Zhuang, Siyuan, Wu, Zhanghao, Zhuang, Yonghao, Lin, Zi, Li, Zhuohan, Li, Dacheng, Xing, Eric, Zhang, Hao, Gonzalez, Joseph, Stoica, Ion
- **Venue:** Advances in Neural Information Processing Systems 36
- **Year:** 2023
- **DOI:** `10.52202/075280-2020`
- **Publisher:** Neural Information Processing Systems Foundation, Inc. (NeurIPS)
- **URL:** https://doi.org/10.52202/075280-2020
- **Verification:** YES (Crossref)
- **Abstract:** Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions. We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. We then verify the agreement between LLM judges and human preferences by introducing two benchmarks: MT-bench, a multi-turn question set; and Chatbot Arena, a crowdsourced battle platform. Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans. Hence, LLM-as-a-judge is a scalable and explainable way to approximate human preferences, which are otherwise very expensive to obtain. Additionally, we show our benchmark and traditional benchmarks complement each other by evaluating several variants of LLaMA and Vicuna. The MT-bench questions, 3K expert votes, and 30K conversations with human preferences are publicly available at https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge.
- **Main contribution:** Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, we explore using strong LLMs as judges to evaluate these models on more open-ended questions.
- **Relation with our paper:** Topic mapping: LLM-assisted annotation, AI-assisted annotation. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames.
- **Should be cited:** YES — cite in Related Work

### 5. Generative AI for Requirements Engineering: A Systematic Literature Review

- **Authors:** Cheng, Haowei, Husen, Jati H., Lu, Yijun, Racharak, Teeradaj, Yoshioka, Nobukazu, Ubayashi, Naoyasu, Washizaki, Hironori
- **Venue:** Software: Practice and Experience
- **Year:** 2025
- **DOI:** `10.1002/spe.70029`
- **Publisher:** Wiley
- **URL:** https://doi.org/10.1002/spe.70029
- **Verification:** YES (Crossref)
- **Abstract:** ABSTRACT Introduction Requirements engineering (RE) faces challenges due to the handling of increasingly complex software systems. These challenges can be addressed using generative artificial intelligence (GenAI). Given that GenAI‐based RE has not been systematically analyzed in detail, this review examines the related research, focusing on trends, methodologies, challenges, and future work directions. Methods A systematic methodology for paper selection, data extraction, and feature analysis is used to comprehensively review 238 articles published from 2019 to 2025 and available from major academic databases. Results Although generative pretrained transformer models dominate current applications (67.3% of studies), the research focus remains unevenly distributed across RE phases, with analysis (30.0%) and elicitation (22.1%) receiving the most attention and management (6.8%) remaining underexplored. Three core challenges—reproducibility (66.8%), hallucinations (63.4%), and interpretability (57.1%)—form a tightly interlinked triad affecting trust and consistency, and strong correlations ( co‐occurrence) indicate that these challenges must be addressed holistically. Industrial adoption remains nascent, with > 90% of studies corresponding to early‐stage development and only 1.3% reaching production‐level integration. Evaluation practices show maturity gaps, limited tool/dataset availability, and fragmented benchmarking approaches. Conclusions Despite the transformative potential of GenAI‐based RE, several barriers hinder its practical adoption. The strong correlations among core challenges demand specialized architectures targeting interdependencies rather than isolated solutions. The limited real‐world deployment reflects systemic bottlenecks in generalizability, data quality, and scalable evaluation methods. Successful adoption requires coordinated development across technical robustness, methodological maturity, and governance integration. A multiphase research roadmap emphasizing evaluation infrastructure strengthening, governance‐aware development, and industrial‐scale standardization is proposed.
- **Main contribution:** ABSTRACT Introduction Requirements engineering (RE) faces challenges due to the handling of increasingly complex software systems. These challenges can be addressed using generative artificial intelligence (GenAI).
- **Relation with our paper:** Topic mapping: AI-assisted annotation, AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation


## Topic 22. AI instruction artifacts

_Verified entries in this topic after curation: **15**_

### 1. Disrupting developer productivity one bot at a time

- **Authors:** Storey, Margaret-Anne, Zagalsky, Alexey
- **Venue:** Proceedings of the 2016 24th ACM SIGSOFT International Symposium on Foundations of Software Engineering
- **Year:** 2016
- **DOI:** `10.1145/2950290.2983989`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/2950290.2983989
- **Verification:** YES (Crossref)
- **Abstract:** Bots are used to support different software development activities, from automating repetitive tasks to bridging knowledge and communication gaps in software teams. We anticipate the use of Bots will increase and lead to improvements in software quality and developer and team productivity, but what if the disruptive effect is not what we expect?
- **Main contribution:** Bots are used to support different software development activities, from automating repetitive tasks to bridging knowledge and communication gaps in software teams. We anticipate the use of Bots will increase and lead to improvements in software quality and developer and team productivity, but what if the disruptive effect is not what we expect?
- **Relation with our paper:** Topic mapping: AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 2. Large Language Models for Software Engineering: Survey and Open Problems

- **Authors:** Fan, Angela, Gokkaya, Beliz, Harman, Mark, Lyubarskiy, Mitya, Sengupta, Shubho, Yoo, Shin, Zhang, Jie M.
- **Venue:** 2023 IEEE/ACM International Conference on Software Engineering: Future of Software Engineering (ICSE-FoSE)
- **Year:** 2023
- **DOI:** `10.1109/icse-fose59343.2023.00008`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/icse-fose59343.2023.00008
- **Verification:** YES (Crossref)
- **Abstract:** This paper provides a survey of the emerging area of Large Language Models (LLMs) for Software Engineering (SE). It also sets out open research challenges for the application of LLMs to technical problems faced by software engineers. LLMs' emergent properties bring novelty and creativity with applications right across the spectrum of Software Engineering activities including coding, design, requirements, repair, refactoring, performance improvement, documentation and analytics. However, these very same emergent properties also pose significant technical challenges; we need techniques that can reliably weed out incorrect solutions, such as hallucinations. Our survey reveals the pivotal role that hybrid techniques (traditional SE plus LLMs) have to play in the development and deployment of reliable, efficient and effective LLM-based SE.
- **Main contribution:** This paper provides a survey of the emerging area of Large Language Models (LLMs) for Software Engineering (SE). It also sets out open research challenges for the application of LLMs to technical problems faced by software engineers.
- **Relation with our paper:** Topic mapping: AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. Adding repository custom instructions for GitHub Copilot

- **Authors:** GitHub
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** GitHub
- **URL:** https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Main contribution:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Copilot Instructions, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 4. Claude Code: Memory and project configuration

- **Authors:** Anthropic
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Anthropic
- **URL:** https://docs.anthropic.com/en/docs/claude-code/memory
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Main contribution:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Claude.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 5. Introducing the Model Context Protocol

- **Authors:** Anthropic
- **Venue:** Product announcement
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Anthropic
- **URL:** https://www.anthropic.com/news/model-context-protocol
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Announcement of the Model Context Protocol (MCP), an interface for connecting AI assistants to tools and data sources.
- **Main contribution:** Announcement of the Model Context Protocol (MCP), an interface for connecting AI assistants to tools and data sources.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, MCP. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 6. Large Language Models for Software Engineering: A Systematic Literature Review

- **Authors:** Hou, Xinyi, Zhao, Yanjie, Liu, Yue, Yang, Zhou, Wang, Kailong, Li, Li, Luo, Xiapu, Lo, David, Grundy, John, Wang, Haoyu
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2024
- **DOI:** `10.1145/3695988`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3695988
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) have significantly impacted numerous domains, including Software Engineering (SE). Many recent publications have explored LLMs applied to various SE tasks. Nevertheless, a comprehensive understanding of the application, effects, and possible limitations of LLMs on SE is still in its early stages. To bridge this gap, we conducted a Systematic Literature Review (SLR) on LLM4SE, with a particular focus on understanding how LLMs can be exploited to optimize processes and outcomes. We selected and analyzed 395 research articles from January 2017 to January 2024 to answer four key Research Questions (RQs). In RQ1, we categorize different LLMs that have been employed in SE tasks, characterizing their distinctive features and uses. In RQ2, we analyze the methods used in data collection, pre-processing, and application, highlighting the role of well-curated datasets for successful LLM for SE implementation. RQ3 investigates the strategies employed to optimize and evaluate the performance of LLMs in SE. Finally, RQ4 examines the specific SE tasks where LLMs have shown success to date, illustrating their practical contributions to the field. From the answers to these RQs, we discuss the current state-of-the-art and trends, identifying gaps in existing research, and highlighting promising areas for future study. Our artifacts are publicly available at https://github.com/security-pride/LLM4SE_SLR .
- **Main contribution:** Large Language Models (LLMs) have significantly impacted numerous domains, including Software Engineering (SE). Many recent publications have explored LLMs applied to various SE tasks.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 7. Rules for AI: Project rules in Cursor

- **Authors:** Cursor
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Cursor
- **URL:** https://cursor.com/docs/rules
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Main contribution:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Cursor Rules, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 8. AGENTS.md: Open format for repository agent context

- **Authors:** Agentic AI Foundation
- **Venue:** Web specification
- **Year:** 2025
- **DOI:** `—`
- **Publisher:** Agentic AI Foundation
- **URL:** https://agents.md/
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Main contribution:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, AGENTS.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 9. Generative AI for Requirements Engineering: A Systematic Literature Review

- **Authors:** Cheng, Haowei, Husen, Jati H., Lu, Yijun, Racharak, Teeradaj, Yoshioka, Nobukazu, Ubayashi, Naoyasu, Washizaki, Hironori
- **Venue:** Software: Practice and Experience
- **Year:** 2025
- **DOI:** `10.1002/spe.70029`
- **Publisher:** Wiley
- **URL:** https://doi.org/10.1002/spe.70029
- **Verification:** YES (Crossref)
- **Abstract:** ABSTRACT Introduction Requirements engineering (RE) faces challenges due to the handling of increasingly complex software systems. These challenges can be addressed using generative artificial intelligence (GenAI). Given that GenAI‐based RE has not been systematically analyzed in detail, this review examines the related research, focusing on trends, methodologies, challenges, and future work directions. Methods A systematic methodology for paper selection, data extraction, and feature analysis is used to comprehensively review 238 articles published from 2019 to 2025 and available from major academic databases. Results Although generative pretrained transformer models dominate current applications (67.3% of studies), the research focus remains unevenly distributed across RE phases, with analysis (30.0%) and elicitation (22.1%) receiving the most attention and management (6.8%) remaining underexplored. Three core challenges—reproducibility (66.8%), hallucinations (63.4%), and interpretability (57.1%)—form a tightly interlinked triad affecting trust and consistency, and strong correlations ( co‐occurrence) indicate that these challenges must be addressed holistically. Industrial adoption remains nascent, with > 90% of studies corresponding to early‐stage development and only 1.3% reaching production‐level integration. Evaluation practices show maturity gaps, limited tool/dataset availability, and fragmented benchmarking approaches. Conclusions Despite the transformative potential of GenAI‐based RE, several barriers hinder its practical adoption. The strong correlations among core challenges demand specialized architectures targeting interdependencies rather than isolated solutions. The limited real‐world deployment reflects systemic bottlenecks in generalizability, data quality, and scalable evaluation methods. Successful adoption requires coordinated development across technical robustness, methodological maturity, and governance integration. A multiphase research roadmap emphasizing evaluation infrastructure strengthening, governance‐aware development, and industrial‐scale standardization is proposed.
- **Main contribution:** ABSTRACT Introduction Requirements engineering (RE) faces challenges due to the handling of increasingly complex software systems. These challenges can be addressed using generative artificial intelligence (GenAI).
- **Relation with our paper:** Topic mapping: AI-assisted annotation, AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 10. Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven Software Engineering

- **Authors:** Li, Ziyou, Sergeyuk, Agnia, Izadi, Maliheh
- **Venue:** 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)
- **Year:** 2025
- **DOI:** `10.1109/ase63991.2025.00276`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/ase63991.2025.00276
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models are transforming software engineering, yet prompt management in practice remains ad hoc, hindering reliability, reuse, and integration into industrial workflows. We present Prompt-with-Me, a practical solution for structured prompt management embedded directly in the development environment. The system automatically classifies prompts using a four-dimensional taxonomy that encompasses intent, author role, software development lifecycle stage, and prompt type. To improve prompt reuse and quality, Prompt-with-Me suggests language refinements, masks sensitive information, and extracts reusable templates from a developer’s prompt library.Our taxonomy study of 1,108 real-world prompts demonstrates that modern LLMs can accurately classify software engineering prompts. Furthermore, our user study with 11 participants shows strong developer acceptance, with high usability (Mean SUS=73), low cognitive load (Mean NASA-TLX=21), and reported gains in prompt quality and efficiency through reduced repetitive effort. Lastly, we offer actionable insights for building the next generation of prompt management and maintenance tools for software engineering workflows.
- **Main contribution:** Large Language Models are transforming software engineering, yet prompt management in practice remains ad hoc, hindering reliability, reuse, and integration into industrial workflows. We present Prompt-with-Me, a practical solution for structured prompt management embedded directly in the development environment.
- **Relation with our paper:** Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 11. A Systematic Literature Review on Detecting Software Vulnerabilities with Large Language Models

- **Authors:** Kaniewski, Sabrina, Schmidt, Fabian, Enzweiler, Markus, Menth, Michael, Heer, Tobias
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2026
- **DOI:** `10.1145/3815425`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3815425
- **Verification:** YES (Crossref)
- **Abstract:** The increasing adoption of Large Language Models (LLMs) in software engineering has sparked interest in their use for software vulnerability detection. However, the rapid development of this field has resulted in a fragmented research landscape, with diverse studies that are difficult to compare due to differences in, e.g., system designs and dataset usage. This fragmentation makes it difficult to obtain a clear overview of the state-of-the-art or compare and categorize studies meaningfully. In this work, we present a comprehensive systematic literature review (SLR) of LLM-based software vulnerability detection. We analyze 263 studies published between January 2020 and November 2025, categorizing them by task formulation, input representation, system architecture, and techniques. Further, we analyze the datasets used, including their characteristics, vulnerability coverage, and diversity. We present a fine-grained taxonomy of vulnerability detection approaches, identify key limitations, and outline actionable future research opportunities. By providing a structured overview of the field, this review improves transparency and serves as a practical guide for researchers and practitioners aiming to conduct more comparable and reproducible research. We publicly release all artifacts and maintain a living repository of LLM-based software vulnerability detection studies at https://github.com/hs-esslingen-it-security/Awesome-LLM4SVD .
- **Main contribution:** The increasing adoption of Large Language Models (LLMs) in software engineering has sparked interest in their use for software vulnerability detection. However, the rapid development of this field has resulted in a fragmented research landscape, with diverse studies that are difficult to compare due to differences in, e.g., system designs and dataset usage.
- **Relation with our paper:** Topic mapping: AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 12. Enhancing Automated Unit Test Generation with Large Language Models: A Systematic Literature Review

- **Authors:** Zhang, Junwei, Hu, Xing, Gao, Cuiyun, Xia, Xin, Li, Shanping
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2026
- **DOI:** `10.1145/3802827`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3802827
- **Verification:** YES (Crossref)
- **Abstract:** Automated unit test generation is a fundamental yet challenging task in software engineering, playing a critical role in ensuring software correctness, reliability, and maintainability. While traditional approaches such as search-based software testing and symbolic execution have achieved notable success, they often suffer from limited semantic understanding, high configuration costs, and scalability constraints. Recent advances in Large Language Models (LLMs) have fundamentally reshaped the landscape of automated unit testing by enabling models to reason over source code semantics and generate executable, context-aware test cases. Despite the rapid growth of this research area, a comprehensive and task-oriented synthesis of existing work remains lacking. This paper presents a systematic literature review of LLM-based unit test generation. This review draws on research from leading SE and AI conferences and journals, including 69 papers published across 25 distinct venues, along with 47 high-quality preprint papers, bringing the total to 116. Our review aims to answer three key research questions: (1) which unit testing tasks have been addressed using LLMs, (2) how LLMs are adapted and integrated into the unit test generation pipeline, and (3) what datasets, benchmarks, and evaluation practices are employed in existing studies. To this end, we organize the literature from a task-centric perspective, covering test generation, test input generation, test oracle generation, and test evolution, and from a methodological perspective, categorizing LLM adaptation strategies into fine-tuning, prompt engineering, and agent-based approaches. Our analysis reveals that current research predominantly focuses on function- and class-level test generation, with comparatively limited attention given to test input generation, oracle construction, and long-term test evolution. Decoder-only LLMs, particularly GPT-family and LLaMA-based models, dominate the field, while encoder-only and encoder–decoder models remain underexplored. We further observe substantial disparities in dataset characteristics, programming language coverage, and evaluation metrics, which hinder fair comparison and reproducibility across studies. Based on empirical evidence extracted from the surveyed literature, we identify key challenges facing LLM-based unit test generation. Building on these findings, we outline several promising research directions, such as dataset optimization, structure-aware context modeling, agent coordination mechanisms, and benchmark enhancement. This review provides a consolidated and evidence-driven foundation for future research, aiming to advance the development of scalable, reliable, and practically applicable LLM-driven unit testing techniques.
- **Main contribution:** Automated unit test generation is a fundamental yet challenging task in software engineering, playing a critical role in ensuring software correctness, reliability, and maintainability. While traditional approaches such as search-based software testing and symbolic execution have achieved notable success, they often suffer from limited semantic understanding, high configuration costs, and scalability constraints.
- **Relation with our paper:** Topic mapping: AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 13. Prompt Engineering in Software Engineering Education: An Empirical Study of Demand, Supply, and Assessment

- **Authors:** Kassab, Mohamad
- **Venue:** Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering
- **Year:** 2026
- **DOI:** `10.1145/3803437.3805788`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3803437.3805788
- **Verification:** YES (Crossref)
- **Abstract:** Prompt engineering is increasingly embedded in software development practice, yet software engineering curricula lack evidence-grounded guidance on which prompt-related competencies to prioritize and how to assess them. This paper presents a large-scale empirical triangulation of industry demand and curricular supply for prompt-engineering competencies in software development. By analysing prompt-related job advertisements across major economies and auditing course descriptions from leading computer science programs, we identify systematic mismatches between practice-facing expectations and formal educational coverage. Industry demand consistently emphasizes prompt design alongside evaluation and testing, with strong signals for prompt optimization and a substantial subset of postings highlighting retrieval augmentation and orchestration. In contrast, university curricula predominantly foreground prompt creation and refinement, with limited explicit emphasis on systematic evaluation. Building on this triangulated evidence, we distil three recurring gaps and derive assessment-oriented implications, specifying inspectable student artefacts, such as evaluation harnesses, lifecycle documentation, and safety testing evidence, that allow prompt-engineering competence to be evaluated in software engineering terms. Collectively, the study provides an empirical foundation to inform curriculum design and assessment in software engineering education amid the rapid diffusion of large language models.
- **Main contribution:** Prompt engineering is increasingly embedded in software development practice, yet software engineering curricula lack evidence-grounded guidance on which prompt-related competencies to prioritize and how to assess them. This paper presents a large-scale empirical triangulation of industry demand and curricular supply for prompt-engineering competencies in software development.
- **Relation with our paper:** Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 14. Promptware Engineering: Software Engineering for Prompt-Enabled Systems

- **Authors:** Chen, Zhenpeng, Wang, Chong, Sun, Weisong, Liu, Xuanzhe, Zhang, Jie M., Liu, Yang
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2026
- **DOI:** `10.1145/3796535`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3796535
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary ‘programming’ interface for guiding system behavior. Building on this trend, a new software paradigm, promptware , has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs. Unlike traditional software, which relies on formal programming languages and deterministic runtime environments, promptware is based on ambiguous, unstructured, and context-dependent natural language and operates on LLMs as runtime environments, which are probabilistic and non-deterministic. These fundamental differences introduce unique challenges in prompt development. In practice, prompt development remains largely ad hoc and relies heavily on time-consuming trial-and-error, a challenge we term the promptware crisis . To address this, we propose promptware engineering , a new methodology that adapts established Software Engineering (SE) principles to prompt development. Drawing on decades of success in traditional SE, we envision a systematic framework encompassing prompt requirements engineering, design, implementation, testing, debugging, evolution, deployment, and monitoring. Our framework re-contextualizes emerging prompt-related challenges within the SE lifecycle, providing principled guidance beyond ad-hoc practices. Without the SE discipline, prompt development is likely to remain mired in trial-and-error. This paper outlines a comprehensive roadmap for promptware engineering, identifying key research directions and offering actionable insights to advance the development of prompt-enabled systems.
- **Main contribution:** Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary ‘programming’ interface for guiding system behavior. Building on this trend, a new software paradigm, promptware , has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — cite in Related Work

### 15. Software refactoring research with large language models: A systematic literature review

- **Authors:** Martinez, Sofia, Xu, Luo, Elnaggar, Mariam, Abdullah Alomar, Eman
- **Venue:** Journal of Systems and Software
- **Year:** 2026
- **DOI:** `10.1016/j.jss.2025.112762`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.jss.2025.112762
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Software refactoring research with large language models: A systematic literature review” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: AI instruction artifacts. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation


## Topic 23. AGENTS.md

_Verified entries in this topic after curation: **1**_

### 1. AGENTS.md: Open format for repository agent context

- **Authors:** Agentic AI Foundation
- **Venue:** Web specification
- **Year:** 2025
- **DOI:** `—`
- **Publisher:** Agentic AI Foundation
- **URL:** https://agents.md/
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Main contribution:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, AGENTS.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)


## Topic 24. Cursor Rules

_Verified entries in this topic after curation: **3**_

### 1. Lessons from Building StackSpot AI: A Contextualized AI Coding Assistant

- **Authors:** Pinto, Gustavo, De Souza, Cleidson, Neto, Joao Batista, Souza, Alberto, Gotto, Tarci­sio, Monteiro, Edward
- **Venue:** Proceedings of the 46th International Conference on Software Engineering: Software Engineering in Practice
- **Year:** 2024
- **DOI:** `10.1145/3639477.3639751`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3639477.3639751
- **Verification:** YES (Crossref)
- **Abstract:** With their exceptional natural language processing capabilities, tools based on Large Language Models (LLMs) like ChatGPT and Co-Pilot have swiftly become indispensable resources in the software developer's toolkit. While recent studies suggest the potential productivity gains these tools can unlock, users still encounter drawbacks, such as generic or incorrect answers. Additionally, the pursuit of improved responses often leads to extensive prompt engineering efforts, diverting valuable time from writing code that delivers actual value. To address these challenges, a new breed of tools, built atop LLMs, is emerging. These tools aim to mitigate drawbacks by employing techniques like fine-tuning or enriching user prompts with contextualized information. In this paper, we delve into the lessons learned by a software development team venturing into the creation of such a contextualized LLM-based application, using retrieval-based techniques, called StackSpot Al. Over a four-month period, the team, despite lacking prior professional experience in LLM-based applications, built the product from scratch. Following the initial product release, we engaged with the development team responsible for the code generative components. Through interviews and analysis of the application's issue tracker, we uncover various intriguing challenges that teams working on LLM-based applications might encounter. For instance, we found three main group of lessons: LLM-based lessons, User-based lessons, and Technical lessons. By understanding these lessons, software development teams could become better prepared to build LLM-based applications.
- **Main contribution:** With their exceptional natural language processing capabilities, tools based on Large Language Models (LLMs) like ChatGPT and Co-Pilot have swiftly become indispensable resources in the software developer's toolkit. While recent studies suggest the potential productivity gains these tools can unlock, users still encounter drawbacks, such as generic or incorrect answers.
- **Relation with our paper:** Topic mapping: Cursor Rules. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits

### 2. Rules for AI: Project rules in Cursor

- **Authors:** Cursor
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Cursor
- **URL:** https://cursor.com/docs/rules
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Main contribution:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Cursor Rules, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 3. Understanding and Enhancing CS Students’ Interaction Experience with AI Coding Assistant Tools

- **Authors:** Long, Xiao, Tan, Xin, Zhu, Yinghao, Jiang, Jing, Zhang, Li
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2025
- **DOI:** `10.1145/3785479`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3785479
- **Verification:** YES (Crossref)
- **Abstract:** AI coding assistants (ACATs) are reshaping computer science (CS) education, yet students’ perception and responses to ACATs’ suggestions remains limited understood, especially regarding behavioral patterns, decision-making, and usability challenges. To address this gap, we conducted a study with 27 CS students, examining their interactions with three widely used ACATs across five key dimensions: interaction frequency and acceptance rate, self-perceived productivity, behavioral patterns, decision-making factors, and challenges and expectations. To support this investigation, we developed an experimental platform incorporating a VSCode extension for log data collection, screen recording and automatic generation of personalized interview and survey questions. Our findings reveal substantial variation in ACAT acceptance rates depending on task types, recommendation methods, and content. We propose a novel five-layer interaction behavior model that captures different stages of user interaction. Notable insights include the problem-solving value of rejected AI suggestions, the inefficiencies introduced by modifying existing code that often lead to backtracking, and the high stability of “slowly accepted” suggestions. Moreover, we identify 22 decision-making factors, 11 challenges, and 23 student expectations for future ACAT improvements—such as enhanced debugging accuracy and adaptive learning of individual coding styles. This study contributes actionable design implications for improving ACAT usability, informing student interaction strategies, and guiding future research in human-software interaction, ultimately aiming to better support CS education.
- **Main contribution:** AI coding assistants (ACATs) are reshaping computer science (CS) education, yet students’ perception and responses to ACATs’ suggestions remains limited understood, especially regarding behavioral patterns, decision-making, and usability challenges. To address this gap, we conducted a study with 27 CS students, examining their interactions with three widely used ACATs across five key dimensions: interaction frequency and acceptance rate, self-...
- **Relation with our paper:** Topic mapping: Cursor Rules. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** OPTIONAL — cite only if space permits


## Topic 25. Claude.md

_Verified entries in this topic after curation: **1**_

### 1. Claude Code: Memory and project configuration

- **Authors:** Anthropic
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Anthropic
- **URL:** https://docs.anthropic.com/en/docs/claude-code/memory
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Main contribution:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Claude.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)


## Topic 26. Copilot Instructions

_Verified entries in this topic after curation: **5**_

### 1. Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models

- **Authors:** Vaithilingam, Priyan, Zhang, Tianyi, Glassman, Elena L.
- **Venue:** CHI Conference on Human Factors in Computing Systems Extended Abstracts
- **Year:** 2022
- **DOI:** `10.1145/3491101.3519665`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3491101.3519665
- **Verification:** YES (Crossref)
- **Abstract:** Recent advances in Large Language Models (LLM) have made automatic code generation possible for real-world programming tasks in general-purpose programming languages such as Python. However, there are few human studies on the usability of these tools and how they fit the programming workflow. In this work, we conducted a within-subjects user study with 24 participants to understand how programmers use and perceive Copilot, a LLM-based code generation tool. We found that, while Copilot did not necessarily improve the task completion time or success rate, most participants preferred to use Copilot in daily programming tasks, since Copilot often provided a useful starting point and saved the effort of searching online. However, participants did face difficulties in understanding, editing, and debugging code snippets generated by Copilot, which significantly hindered their task-solving effectiveness. Finally, we highlighted several promising directions for improving the design of Copilot based on our observations and participants’ feedback.
- **Main contribution:** Recent advances in Large Language Models (LLM) have made automatic code generation possible for real-world programming tasks in general-purpose programming languages such as Python. However, there are few human studies on the usability of these tools and how they fit the programming workflow.
- **Relation with our paper:** Topic mapping: Copilot Instructions. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 2. Grounded Copilot: How Programmers Interact with Code-Generating Models

- **Authors:** Barke, Shraddha, James, Michael B., Polikarpova, Nadia
- **Venue:** Proceedings of the ACM on Programming Languages
- **Year:** 2023
- **DOI:** `10.1145/3586030`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3586030
- **Verification:** YES (Crossref)
- **Abstract:** Powered by recent advances in code-generating models, AI assistants like Github Copilot promise to change the face of programming forever. But what is this new face of programming? We present the first grounded theory analysis of how programmers interact with Copilot, based on observing 20 participants—with a range of prior experience using the assistant—as they solve diverse programming tasks across four languages. Our main finding is that interactions with programming assistants are bimodal : in acceleration mode , the programmer knows what to do next and uses Copilot to get there faster; in exploration mode , the programmer is unsure how to proceed and uses Copilot to explore their options. Based on our theory, we provide recommendations for improving the usability of future AI programming assistants.
- **Main contribution:** Powered by recent advances in code-generating models, AI assistants like Github Copilot promise to change the face of programming forever. But what is this new face of programming?
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: Copilot Instructions. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — cite in Related Work

### 3. Adding repository custom instructions for GitHub Copilot

- **Authors:** GitHub
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** GitHub
- **URL:** https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Main contribution:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Copilot Instructions, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 4. Measuring GitHub Copilot's Impact on Productivity

- **Authors:** Ziegler, Albert, Kalliamvakou, Eirini, Li, X. Alice, Rice, Andrew, Rifkin, Devon, Simister, Shawn, Sittampalam, Ganesh, Aftandilian, Edward
- **Venue:** Communications of the ACM
- **Year:** 2024
- **DOI:** `10.1145/3633453`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3633453
- **Verification:** YES (Crossref)
- **Abstract:** Case study asks Copilot users about its impact on their productivity, and seeks to find their perceptions mirrored in user data.
- **Main contribution:** Case study asks Copilot users about its impact on their productivity, and seeks to find their perceptions mirrored in user data.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: Copilot Instructions. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — cite in Related Work

### 5. Measuring the Impact of AI Coding Assistants (e.g., GitHub Copilot, ChatGPT) on Programming Productivity among BSCS Students

- **Authors:** Dua Nadeem, Nosheen Asif, Mariam Tanveer, Kinza Javed
- **Venue:** Kashf Journal of Multidisciplinary Research
- **Year:** 2026
- **DOI:** `10.71146/kjmr877`
- **Publisher:** Kashf Institute of Development & Studies
- **URL:** https://doi.org/10.71146/kjmr877
- **Verification:** YES (Crossref)
- **Abstract:** This study examines the impact of AI coding assistants on programming productivity among undergraduate computing students, with a focus on BSCS learners. The rapid adoption of tools such as GitHub Copilot and ChatGPT has transformed how students approach coding tasks, raising questions about whether these tools enhance productivity or alter learning behavior. Existing research largely emphasizes efficiency gains in controlled or professional settings by creating a gap in understanding their real-world academic impact on students. A quantitative, cross-sectional survey design was employed, collecting data from 127 participants through a structured questionnaire. The study measures productivity as a multi-dimensional construct, including task completion time, code quality, debugging efficiency, and perceived problem-solving independence. The findings suggest that AI coding assistants contribute to improved task efficiency and support learning processes, particularly in understanding programming concepts and completing coding tasks more effectively. Students reported benefits in terms of ease of coding and assistance during debugging, while also acknowledging concerns regarding the reliability of AI-generated outputs. Additionally, the use of these tools appears to influence students’ approach to problem-solving and their level of independence. In conclusion, AI coding assistants offer notable benefits in supporting programming tasks and learning experiences, but they also introduce challenges related to over-reliance. Their overall impact depends on how they are used, highlighting the importance of guided and balanced integration within programming education to ensure that productivity gains do not come at the expense of independent skill development.
- **Main contribution:** This study examines the impact of AI coding assistants on programming productivity among undergraduate computing students, with a focus on BSCS learners. The rapid adoption of tools such as GitHub Copilot and ChatGPT has transformed how students approach coding tasks, raising questions about whether these tools enhance productivity or alter learning behavior.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: Copilot Instructions. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Does not measure contamination rates of repository discovery frames. Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — supporting citation


## Topic 27. Promptware

_Verified entries in this topic after curation: **3**_

### 1. Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven Software Engineering

- **Authors:** Li, Ziyou, Sergeyuk, Agnia, Izadi, Maliheh
- **Venue:** 2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)
- **Year:** 2025
- **DOI:** `10.1109/ase63991.2025.00276`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/ase63991.2025.00276
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models are transforming software engineering, yet prompt management in practice remains ad hoc, hindering reliability, reuse, and integration into industrial workflows. We present Prompt-with-Me, a practical solution for structured prompt management embedded directly in the development environment. The system automatically classifies prompts using a four-dimensional taxonomy that encompasses intent, author role, software development lifecycle stage, and prompt type. To improve prompt reuse and quality, Prompt-with-Me suggests language refinements, masks sensitive information, and extracts reusable templates from a developer’s prompt library.Our taxonomy study of 1,108 real-world prompts demonstrates that modern LLMs can accurately classify software engineering prompts. Furthermore, our user study with 11 participants shows strong developer acceptance, with high usability (Mean SUS=73), low cognitive load (Mean NASA-TLX=21), and reported gains in prompt quality and efficiency through reduced repetitive effort. Lastly, we offer actionable insights for building the next generation of prompt management and maintenance tools for software engineering workflows.
- **Main contribution:** Large Language Models are transforming software engineering, yet prompt management in practice remains ad hoc, hindering reliability, reuse, and integration into industrial workflows. We present Prompt-with-Me, a practical solution for structured prompt management embedded directly in the development environment.
- **Relation with our paper:** Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 2. Prompt Engineering in Software Engineering Education: An Empirical Study of Demand, Supply, and Assessment

- **Authors:** Kassab, Mohamad
- **Venue:** Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering
- **Year:** 2026
- **DOI:** `10.1145/3803437.3805788`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3803437.3805788
- **Verification:** YES (Crossref)
- **Abstract:** Prompt engineering is increasingly embedded in software development practice, yet software engineering curricula lack evidence-grounded guidance on which prompt-related competencies to prioritize and how to assess them. This paper presents a large-scale empirical triangulation of industry demand and curricular supply for prompt-engineering competencies in software development. By analysing prompt-related job advertisements across major economies and auditing course descriptions from leading computer science programs, we identify systematic mismatches between practice-facing expectations and formal educational coverage. Industry demand consistently emphasizes prompt design alongside evaluation and testing, with strong signals for prompt optimization and a substantial subset of postings highlighting retrieval augmentation and orchestration. In contrast, university curricula predominantly foreground prompt creation and refinement, with limited explicit emphasis on systematic evaluation. Building on this triangulated evidence, we distil three recurring gaps and derive assessment-oriented implications, specifying inspectable student artefacts, such as evaluation harnesses, lifecycle documentation, and safety testing evidence, that allow prompt-engineering competence to be evaluated in software engineering terms. Collectively, the study provides an empirical foundation to inform curriculum design and assessment in software engineering education amid the rapid diffusion of large language models.
- **Main contribution:** Prompt engineering is increasingly embedded in software development practice, yet software engineering curricula lack evidence-grounded guidance on which prompt-related competencies to prioritize and how to assess them. This paper presents a large-scale empirical triangulation of industry demand and curricular supply for prompt-engineering competencies in software development.
- **Relation with our paper:** Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — supporting citation

### 3. Promptware Engineering: Software Engineering for Prompt-Enabled Systems

- **Authors:** Chen, Zhenpeng, Wang, Chong, Sun, Weisong, Liu, Xuanzhe, Zhang, Jie M., Liu, Yang
- **Venue:** ACM Transactions on Software Engineering and Methodology
- **Year:** 2026
- **DOI:** `10.1145/3796535`
- **Publisher:** Association for Computing Machinery (ACM)
- **URL:** https://doi.org/10.1145/3796535
- **Verification:** YES (Crossref)
- **Abstract:** Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary ‘programming’ interface for guiding system behavior. Building on this trend, a new software paradigm, promptware , has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs. Unlike traditional software, which relies on formal programming languages and deterministic runtime environments, promptware is based on ambiguous, unstructured, and context-dependent natural language and operates on LLMs as runtime environments, which are probabilistic and non-deterministic. These fundamental differences introduce unique challenges in prompt development. In practice, prompt development remains largely ad hoc and relies heavily on time-consuming trial-and-error, a challenge we term the promptware crisis . To address this, we propose promptware engineering , a new methodology that adapts established Software Engineering (SE) principles to prompt development. Drawing on decades of success in traditional SE, we envision a systematic framework encompassing prompt requirements engineering, design, implementation, testing, debugging, evolution, deployment, and monitoring. Our framework re-contextualizes emerging prompt-related challenges within the SE lifecycle, providing principled guidance beyond ad-hoc practices. Without the SE discipline, prompt development is likely to remain mired in trial-and-error. This paper outlines a comprehensive roadmap for promptware engineering, identifying key research directions and offering actionable insights to advance the development of prompt-enabled systems.
- **Main contribution:** Large Language Models (LLMs) are increasingly integrated into software applications, giving rise to a broad class of prompt-enabled systems, in which prompts serve as the primary ‘programming’ interface for guiding system behavior. Building on this trend, a new software paradigm, promptware , has emerged, which treats natural language prompts as first-class software artifacts for interacting with LLMs.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Promptware. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — cite in Related Work


## Topic 28. MCP

_Verified entries in this topic after curation: **1**_

### 1. Introducing the Model Context Protocol

- **Authors:** Anthropic
- **Venue:** Product announcement
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Anthropic
- **URL:** https://www.anthropic.com/news/model-context-protocol
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Announcement of the Model Context Protocol (MCP), an interface for connecting AI assistants to tools and data sources.
- **Main contribution:** Announcement of the Model Context Protocol (MCP), an interface for connecting AI assistants to tools and data sources.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, MCP. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)


## Topic 29. Repository discovery frames

_Verified entries in this topic after curation: **6**_

### 1. There is no random sampling in software engineering research

- **Authors:** Amir, Bilal, Ralph, Paul
- **Venue:** Proceedings of the 40th International Conference on Software Engineering: Companion Proceeedings
- **Year:** 2018
- **DOI:** `10.1145/3183440.3195001`
- **Publisher:** ACM
- **URL:** https://doi.org/10.1145/3183440.3195001
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling is considered crucial for predominately quantitative, positivist research. Researchers typically argue that a sample is representative when items are selected randomly from a population. However, random sampling is rare in empirical software engineering research because there are no credible sampling frames (population lists) for the units of analysis software engineering researchers study (e.g. software projects, code libraries, developers, projects). This means that most software engineering research does not support statistical generalization, but rejecting any particular study for lack of random sampling is capricious.
- **Main contribution:** Representative sampling is considered crucial for predominately quantitative, positivist research. Researchers typically argue that a sample is representative when items are selected randomly from a population.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 2. Sampling in software engineering research: a critical review and guidelines

- **Authors:** Baltes, Sebastian, Ralph, Paul
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10072-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10072-8
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field. This article therefore reports a critical review of the state of sampling in recent, high-quality software engineering research. The key findings are: (1) random sampling is rare; (2) sophisticated sampling strategies are very rare; (3) sampling, representativeness and randomness often appear misunderstood. These findings suggest that software engineering research has a generalizability crisis. To address these problems, this paper synthesizes existing knowledge of sampling into a succinct primer and proposes extensive guidelines for improving the conduct, presentation and evaluation of sampling in software engineering research. It is further recommended that while researchers should strive for more representative samples, disparaging non-probability sampling is generally capricious and particularly misguided for predominately qualitative research.
- **Main contribution:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Sampling bias, Repository discovery frames, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 3. Adding repository custom instructions for GitHub Copilot

- **Authors:** GitHub
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** GitHub
- **URL:** https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Main contribution:** Official GitHub documentation for repository custom instructions paths used by GitHub Copilot.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Copilot Instructions, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 4. Claude Code: Memory and project configuration

- **Authors:** Anthropic
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Anthropic
- **URL:** https://docs.anthropic.com/en/docs/claude-code/memory
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Main contribution:** Documentation of Claude Code memory and project configuration artifacts that store persistent agent instructions in a software project.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Claude.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 5. Rules for AI: Project rules in Cursor

- **Authors:** Cursor
- **Venue:** Product documentation
- **Year:** 2024
- **DOI:** `—`
- **Publisher:** Cursor
- **URL:** https://cursor.com/docs/rules
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Main contribution:** Official documentation describing Cursor project rules files used to steer AI coding assistants within a repository.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, Cursor Rules, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)

### 6. AGENTS.md: Open format for repository agent context

- **Authors:** Agentic AI Foundation
- **Venue:** Web specification
- **Year:** 2025
- **DOI:** `—`
- **Publisher:** Agentic AI Foundation
- **URL:** https://agents.md/
- **Verification:** YES-URL (HTTP 200)
- **Abstract:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Main contribution:** Public specification of AGENTS.md, a repository-level file format for providing coding agents with project context and instructions.
- **Relation with our paper:** Documents AI-instruction/assistant phenomenon that our discovery predicates target. Topic mapping: AI instruction artifacts, AGENTS.md, Repository discovery frames. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Phenomenon/tool documentation without mining-frame validity protocol.
- **Should be cited:** YES — primary phenomenon source (grey literature; no peer-reviewed substitute found)


## Topic 30. Software Engineering methodology

_Verified entries in this topic after curation: **9**_

### 1. Guidelines for conducting and reporting case study research in software engineering

- **Authors:** Runeson, Per, Höst, Martin
- **Venue:** Empirical Software Engineering
- **Year:** 2008
- **DOI:** `10.1007/s10664-008-9102-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-008-9102-8
- **Verification:** YES (Crossref)
- **Abstract:** Case study is a suitable research methodology for software engineering research since it studies contemporary phenomena in its natural context. However, the understanding of what constitutes a case study varies, and hence the quality of the resulting studies. This paper aims at providing an introduction to case study methodology and guidelines for researchers conducting case studies and readers studying reports of such studies. The content is based on the authors’ own experience from conducting and reading case studies. The terminology and guidelines are compiled from different methodology handbooks in other research domains, in particular social science and information systems, and adapted to the needs in software engineering. We present recommended practices for software engineering case studies as well as empirically derived and evaluated checklists for researchers and readers of case study research.
- **Main contribution:** Case study is a suitable research methodology for software engineering research since it studies contemporary phenomena in its natural context. However, the understanding of what constitutes a case study varies, and hence the quality of the resulting studies.
- **Relation with our paper:** Topic mapping: Reporting guidelines, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 2. The road ahead for Mining Software Repositories

- **Authors:** Hassan, Ahmed E.
- **Venue:** 2008 Frontiers of Software Maintenance
- **Year:** 2008
- **DOI:** `10.1109/fosm.2008.4659248`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/fosm.2008.4659248
- **Verification:** YES (Crossref)
- **Abstract:** Source control repositories, bug repositories, archived communications, deployment logs, and code repositories are examples of software repositories that are commonly available for most software projects. The mining software repositories (MSR) field analyzes and cross-links the rich data available in these repositories to uncover interesting and actionable information about software systems. By transforming these repositories from static record-keeping ones into active repositories, we can guide decision processes in modern software projects. For example, data in source control repositories, traditionally used to archive code, could be linked with data in bug repositories to help practitioners propagate complex changes and to warn them about risky code based on prior changes and bugs. In this paper, we present a brief history of the MSR field and discuss several recent achievements and results of using MSR techniques to support software research and practice. We then discuss the various opportunities and challenges that lie in the road ahead for this important and emerging field.
- **Main contribution:** Source control repositories, bug repositories, archived communications, deployment logs, and code repositories are examples of software repositories that are commonly available for most software projects. The mining software repositories (MSR) field analyzes and cross-links the rich data available in these repositories to uncover interesting and actionable information about software systems.
- **Relation with our paper:** Topic mapping: Mining Software Repositories (MSR), Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Scope only partially overlaps our estimand; use strictly for the mapped topic.
- **Should be cited:** YES — cite in Related Work

### 3. Experimentation in Software Engineering

- **Authors:** Wohlin, Claes, Runeson, Per, Höst, Martin, Ohlsson, Magnus C., Regnell, Björn, Wesslén, Anders
- **Venue:** 
- **Year:** 2012
- **DOI:** `10.1007/978-3-642-29044-2`
- **Publisher:** Springer Berlin Heidelberg
- **URL:** https://doi.org/10.1007/978-3-642-29044-2
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Experimentation in Software Engineering” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 4. A Map of Threats to Validity of Systematic Literature Reviews in Software Engineering

- **Authors:** Zhou, Xin, Jin, Yuqin, Zhang, He, Li, Shanshan, Huang, Xin
- **Venue:** 2016 23rd Asia-Pacific Software Engineering Conference (APSEC)
- **Year:** 2016
- **DOI:** `10.1109/apsec.2016.031`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/apsec.2016.031
- **Verification:** YES (Crossref)
- **Abstract:** Context: The assessment of Threats to Validity (TTVs) is critical to secure the quality of empirical studies in Software Engineering (SE). In the recent decade, Systematic Literature Review (SLR) was becoming an increasingly important empirical research method in SE. One of the mechanisms of insuring the level of scientific value in the findings of an SLR is to rigorously assess its validity. Hence, it is necessary to realize the status quo and issues of TTVs of SLRs in SE. Objective: This study aims to investigate the-state-of-the-practice of TTVs of the SLRs published in SE, and further support SE researchers to improve the assessment and strategies against TTVs in order to increase the quality of SLRs in SE. Method: We conducted a tertiary study by reviewing the SLRs in SE that report the assessment of TTVs. Results: We identified 316 SLRs published from 2004 to the first half of 2015, in which TTVs are discussed. The issues associated to TTVs were also summarized and categorized. Conclusion: The common TTVs related to SLR research, such as internal validity and reliability, were thoroughly discussed in most SLRs. The threats to construct validity and external validity drew less attention. Moreover, there are few strategies and tactics being reported to cope with the various TTVs.
- **Main contribution:** Context: The assessment of Threats to Validity (TTVs) is critical to secure the quality of empirical studies in Software Engineering (SE). In the recent decade, Systematic Literature Review (SLR) was becoming an increasingly important empirical research method in SE.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 5. Threats to validity in search‐based predictive modelling for software engineering

- **Authors:** Malhotra, Ruchika, Khanna, Megha
- **Venue:** IET Software
- **Year:** 2018
- **DOI:** `10.1049/iet-sen.2018.5143`
- **Publisher:** Institution of Engineering and Technology (IET)
- **URL:** https://doi.org/10.1049/iet-sen.2018.5143
- **Verification:** YES (Crossref)
- **Abstract:** A number of studies in the literature have developed effective models to address prediction tasks related to a software product such as estimating its development effort, or its change/defect proneness. These predictions are critical as they help in identifying weak areas of a software product and thus guide software project managers in effective allocation of project resources to these weak parts. Such practices assure good quality software products. Recently, the use of search‐based approaches (SBAs) for developing software prediction models (SPMs) has been successfully explored by a number of researchers. However, in order to develop effective and practical SPMs it is imperative to analyse various sources of threats. This study extensively reviews 93 primary studies, which use SBAs for developing SPMs of four commonly used software attributes (effort, defect‐proneness, maintainability and change‐proneness) in order to discuss and identify the various sources of threats while using these approaches for SPMs. The study also lists various actions that may be taken in order to minimise these threats. Furthermore, best practice examples in literature and the year‐wise trends of threats indicating the most common threats missed by researchers are provided to help academicians and practitioners in designing effective studies for developing SPMs using SBAs.
- **Main contribution:** A number of studies in the literature have developed effective models to address prediction tasks related to a software product such as estimating its development effort, or its change/defect proneness. These predictions are critical as they help in identifying weak areas of a software product and thus guide software project managers in effective allocation of project resources to these weak parts.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 6. Identifying, categorizing and mitigating threats to validity in software engineering secondary studies

- **Authors:** Ampatzoglou, Apostolos, Bibi, Stamatia, Avgeriou, Paris, Verbeek, Marijn, Chatzigeorgiou, Alexander
- **Venue:** Information and Software Technology
- **Year:** 2019
- **DOI:** `10.1016/j.infsof.2018.10.006`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2018.10.006
- **Verification:** YES (Crossref)
- **Abstract:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies. Objective In this paper, we review the corpus of secondary studies, with the aim to identify: (a) the trend of reporting threats to validity, (b) the most common threats to validity and corresponding mitigation actions, and (c) possible categories in which threats to validity can be classified. Method To achieve this goal we employ the tertiary study research method that is used for synthesizing knowledge from existing secondary studies. In particular, we collected data from more than 100 studies, published until December 2016 in top quality software engineering venues (both journals and conference). Results Our results suggest that in recent years, secondary studies are more likely to report their threats to validity. However, the presentation of such threats is rather ad hoc, e.g., the same threat may be presented with a different name, or under a different category. To alleviate this problem, we propose a classification schema for reporting threats to validity and possible mitigation actions. Both the classification of threats and the associated mitigation actions have been validated by an empirical study, i.e., Delphi rounds with experts. Conclusion Based on the proposed schema, we provide a checklist, which authors of secondary studies can use for identifying and categorizing threats to validity and corresponding mitigation actions, while readers of secondary studies can use the checklist for assessing the validity of the reported results.
- **Main contribution:** Abstract Context Secondary studies are vulnerable to threats to validity. Although, mitigating these threats is crucial for the credibility of these studies, we currently lack a systematic approach to identify, categorize and mitigate threats to validity for secondary studies.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 7. Mitigating Threats to Validity in Empirical Software Engineering: A Traceability Case Study

- **Authors:** Mustafa, Nasser, Labiche, Yvan, Towey, Dave
- **Venue:** 2019 IEEE 43rd Annual Computer Software and Applications Conference (COMPSAC)
- **Year:** 2019
- **DOI:** `10.1109/compsac.2019.10227`
- **Publisher:** IEEE
- **URL:** https://doi.org/10.1109/compsac.2019.10227
- **Verification:** YES (Crossref)
- **Abstract:** The issue of validity threats in empirical software engineering research is important. However, some authors overlook this, focusing on validating their work through application of fundamental testing techniques, instead. However, testing is different to empirical validation, with the latter being more concerned about how experimental conclusions are justified. An important factor that can render an experimental conclusion incorrect is researcher’s bias, which can be especially relevant when setting the experimental parameters. Therefore, consideration of validity threats is essential to enable confidence in research results and assure the research quality. This paper provides a practical approach for mitigating threats to validity in empirical software engineering using a sequence of software activities. The paper is based on a real-world traceability case study for illustration purposes.
- **Main contribution:** The issue of validity threats in empirical software engineering research is important. However, some authors overlook this, focusing on validating their work through application of fundamental testing techniques, instead.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work

### 8. Sampling in software engineering research: a critical review and guidelines

- **Authors:** Baltes, Sebastian, Ralph, Paul
- **Venue:** Empirical Software Engineering
- **Year:** 2022
- **DOI:** `10.1007/s10664-021-10072-8`
- **Publisher:** Springer Science and Business Media LLC
- **URL:** https://doi.org/10.1007/s10664-021-10072-8
- **Verification:** YES (Crossref)
- **Abstract:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field. This article therefore reports a critical review of the state of sampling in recent, high-quality software engineering research. The key findings are: (1) random sampling is rare; (2) sophisticated sampling strategies are very rare; (3) sampling, representativeness and randomness often appear misunderstood. These findings suggest that software engineering research has a generalizability crisis. To address these problems, this paper synthesizes existing knowledge of sampling into a succinct primer and proposes extensive guidelines for improving the conduct, presentation and evaluation of sampling in software engineering research. It is further recommended that while researchers should strive for more representative samples, disparaging non-probability sampling is generally capricious and particularly misguided for predominately qualitative research.
- **Main contribution:** Representative sampling appears rare in empirical software engineering research. Not all studies need representative samples, but a general lack of representative sampling undermines a scientific field.
- **Relation with our paper:** Direct methodological guidance on frames/populations/generalization. Topic mapping: Sampling methodology, Sampling bias, Repository discovery frames, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** No instruction-artifact predicate families; no consensus-protocol sensitivity of contamination rates.
- **Should be cited:** YES — cite in Related Work

### 9. Threats to validity in software engineering research: A critical reflection

- **Authors:** Verdecchia, Roberto, Engström, Emelie, Lago, Patricia, Runeson, Per, Song, Qunying
- **Venue:** Information and Software Technology
- **Year:** 2023
- **DOI:** `10.1016/j.infsof.2023.107329`
- **Publisher:** Elsevier BV
- **URL:** https://doi.org/10.1016/j.infsof.2023.107329
- **Verification:** YES (Crossref)
- **Abstract:** [Abstract not available from Crossref/OpenAlex/Semantic Scholar at retrieval time. Bibliographic metadata verified.]
- **Main contribution:** Verified work titled “Threats to validity in software engineering research: A critical reflection” (see venue/year/DOI). Contribution inferred from title/venue pending abstract recovery.
- **Relation with our paper:** Validity-reporting discourse that motivates declaring analytic targets and protocols. Topic mapping: Construct validity, Internal validity, External validity, Software Engineering methodology. Does not provide a target-conditional contamination audit of AI-instruction discovery frames with consensus-protocol sensitivity and predicate-family reporting.
- **Limitations:** Guidance/taxonomy without an operational instruction-frame worksheet.
- **Should be cited:** YES — cite in Related Work


---

## 4. Master citation table

| Year | Title | Authors | Venue | DOI/URL | Topics | Cite? | Verified |
|---:|---|---|---|---|---|---|---|
| 1960 | A Coefficient of Agreement for Nominal Scales | Cohen, Jacob | Educational and Psychological Measure... | 10.1177/001316446002000104 | 17,18 | YES | YES |
| 1977 | The Measurement of Observer Agreement for Categorical Data | Landis et al. | Biometrics | 10.2307/2529310 | 17,18 | YES | YES |
| 1991 | A Coefficient of Agreement for Nominal Scales: An Asymmetric Versio... | Kvalseth, Tarald O. | Educational and Psychological Measure... | 10.1177/0013164491511008 | 17 | YES | YES |
| 2004 | The perils and pitfalls of mining SourceForge | Howison, J. | "International Workshop on Mining Sof... | 10.1049/ic:20040467 | 5,10 | YES | YES |
| 2005 | Reporting guidelines for controlled experiments in software enginee... | Jedlitschka et al. | 2005 International Symposium on Empir... | 10.1109/isese.2005.1541818 | 15 | YES | YES |
| 2006 | Incremental Maintenance of Software Artifacts | Reiss, S.P. | IEEE Transactions on Software Enginee... | 10.1109/tse.2006.91 | 13 | YES | YES |
| 2006 | Mining Software Repositories to Assist Developers and Support Managers | Hassan, Ahmed | 2006 22nd IEEE International Conferen... | 10.1109/icsm.2006.38 | 1 | YES | YES |
| 2006 | Mining software repositories with CVSgrab | Voinea et al. | Proceedings of the 2006 international... | 10.1145/1137983.1138024 | 1 | YES | YES |
| 2007 | Open Borders? Immigration in Open Source Projects | Bird et al. | Fourth International Workshop on Mini... | 10.1109/msr.2007.23 | 5 | YES | YES |
| 2008 | Guidelines for conducting and reporting case study research in soft... | Runeson et al. | Empirical Software Engineering | 10.1007/s10664-008-9102-8 | 15,30 | YES | YES |
| 2008 | The road ahead for Mining Software Repositories | Hassan, Ahmed E. | 2008 Frontiers of Software Maintenance | 10.1109/fosm.2008.4659248 | 1,30 | YES | YES |
| 2009 | Cross-project defect prediction | Zimmermann et al. | Proceedings of the 7th joint meeting ... | 10.1145/1595696.1595713 | 8,9 | YES | YES |
| 2009 | MapReduce as a general framework to support research in Mining Soft... | Weiyi Shang et al. | 2009 6th IEEE International Working C... | 10.1109/msr.2009.5069477 | 1 | YES | YES |
| 2009 | On mining data across software repositories | Anbalagan et al. | 2009 6th IEEE International Working C... | 10.1109/msr.2009.5069498 | 1 | YES | YES |
| 2009 | Systematic literature reviews in software engineering – A systemati... | Kitchenham et al. | Information and Software Technology | 10.1016/j.infsof.2008.09.009 | 15 | YES | YES |
| 2011 | Evaluating defect prediction approaches: a benchmark and an extensi... | D’Ambros et al. | Empirical Software Engineering | 10.1007/s10664-011-9173-9 | 11,12 | YES | YES |
| 2011 | On the reproducibility of empirical software engineering studies ba... | González-Barahona et al. | Empirical Software Engineering | 10.1007/s10664-011-9181-9 | 14 | YES | YES |
| 2011 | Quantitative Determination of the Relationship between Internal Val... | Dieste et al. | 2011 International Symposium on Empir... | 10.1109/esem.2011.37 | 7 | OPT | YES |
| 2011 | Replication of Empirical Studies in Software Engineering: Prelimina... | Silva et al. | 2011 Second International Workshop on... | 10.1109/reser.2011.14 | 14 | YES | YES |
| 2012 | A unifying view on dataset shift in classification | Moreno-Torres et al. | Pattern Recognition | 10.1016/j.patcog.2011.06.019 | 9 | YES | YES |
| 2012 | Experimentation in Software Engineering | Wohlin et al. |  | 10.1007/978-3-642-29044-2 | 6,7,8,30 | YES | YES |
| 2012 | GHTorrent: Github's data from a firehose | Gousios et al. | 2012 9th IEEE Working Conference on M... | 10.1109/msr.2012.6224294 | 1,2,10 | YES | YES |
| 2012 | Leakage in data mining | Kaufman et al. | ACM Transactions on Knowledge Discove... | 10.1145/2382577.2382579 | 9 | YES | YES |
| 2012 | Replication of empirical studies in software engineering research: ... | da Silva et al. | Empirical Software Engineering | 10.1007/s10664-012-9227-7 | 14 | YES | YES |
| 2012 | Social coding in GitHub | Dabbish et al. | Proceedings of the ACM 2012 conferenc... | 10.1145/2145204.2145396 | 16 | OPT | YES |
| 2013 | Data Quality: Some Comments on the NASA Software Defect Datasets | Shepperd et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2013.11 | 11,16 | YES | YES |
| 2013 | The impact of tangled code changes | Herzig et al. | 2013 10th Working Conference on Minin... | 10.1109/msr.2013.6624018 | 6,11 | YES | YES |
| 2013 | Towards a Taxonomy of Replications in Empirical Software Engineerin... | Magalhaes et al. | 2013 3rd International Workshop on Re... | 10.1109/reser.2013.10 | 14 | YES | YES |
| 2014 | Co-evolution of project documentation and popularity within github | Aggarwal et al. | Proceedings of the 11th Working Confe... | 10.1145/2597073.2597120 | 16 | OPT | YES |
| 2014 | Confounding parameters on program comprehension: a literature survey | Siegmund et al. | Empirical Software Engineering | 10.1007/s10664-014-9318-8 | 6 | YES | YES |
| 2014 | Estimating development effort in Free/Open source software projects... | Robles et al. | Proceedings of the 11th Working Confe... | 10.1145/2597073.2597107 | 14 | YES | YES |
| 2014 | Influence of social and technical factors for evaluating contributi... | Tsay et al. | Proceedings of the 36th International... | 10.1145/2568225.2568315 | 16 | YES | YES |
| 2014 | Is mining software repositories data science? (keynote) | Mockus, Audris | Proceedings of the 11th Working Confe... | 10.1145/2597073.2600728 | 1 | YES | YES |
| 2014 | Lean GHTorrent: GitHub data on demand | Gousios et al. | Proceedings of the 11th Working Confe... | 10.1145/2597073.2597126 | 1,2,10 | YES | YES |
| 2014 | Let's talk about it: evaluating contributions through discussion in... | Tsay et al. | Proceedings of the 22nd ACM SIGSOFT I... | 10.1145/2635868.2635882 | 16 | OPT | YES |
| 2014 | Researcher Bias: The Use of Machine Learning in Software Defect Pre... | Shepperd et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2014.2322358 | 7,11 | YES | YES |
| 2014 | The promises and perils of mining GitHub | Kalliamvakou et al. | Proceedings of the 11th Working Confe... | 10.1145/2597073.2597074 | 5,10,16 | YES | YES |
| 2015 | An in-depth study of the promises and perils of mining GitHub | Kalliamvakou et al. | Empirical Software Engineering | 10.1007/s10664-015-9393-5 | 5,10,16 | YES | YES |
| 2015 | Guidelines for conducting systematic mapping studies in software en... | Petersen et al. | Information and Software Technology | 10.1016/j.infsof.2015.03.007 | 15 | YES | YES |
| 2015 | Investigations about replication of empirical studies in software e... | de Magalhães et al. | Information and Software Technology | 10.1016/j.infsof.2015.02.001 | 14 | YES | YES |
| 2015 | Replication of Empirical Studies in Software Engineering: An Update... | Bezerra et al. | 2015 ACM/IEEE International Symposium... | 10.1109/esem.2015.7321213 | 14 | YES | YES |
| 2015 | The impact of tangled code changes on defect prediction models | Herzig et al. | Empirical Software Engineering | 10.1007/s10664-015-9376-6 | 6 | YES | YES |
| 2015 | Towards Gamification in Software Traceability: Between Test and Cod... | Meimandi Parizi et al. | Proceedings of the 10th International... | 10.5220/0005555503930400 | 13 | YES | YES |
| 2015 | Views on Internal and External Validity in Empirical Software Engin... | Siegmund et al. | 2015 IEEE/ACM 37th IEEE International... | 10.1109/icse.2015.24 | 6,7,8 | YES | YES |
| 2016 | A Map of Threats to Validity of Systematic Literature Reviews in So... | Zhou et al. | 2016 23rd Asia-Pacific Software Engin... | 10.1109/apsec.2016.031 | 30 | YES | YES |
| 2016 | Comments on “Researcher Bias: The Use of Machine Learning in Softwa... | Tantithamthavorn et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2016.2553030 | 7 | YES | YES |
| 2016 | Disrupting developer productivity one bot at a time | Storey et al. | Proceedings of the 2016 24th ACM SIGS... | 10.1145/2950290.2983989 | 22 | YES | YES |
| 2016 | On the popularity of GitHub software | Borges, Hudson | 2016 IEEE International Conference on... | 10.1109/icsme.2016.103 | 16 | OPT | YES |
| 2016 | Predicting the Popularity of GitHub Repositories | Borges et al. | Proceedings of the The 12th Internati... | 10.1145/2972958.2972966 | 16 | OPT | YES |
| 2016 | Raising MSR researchers | Hassan, Ahmed E. | Proceedings of the 13th International... | 10.1145/2901739.2901780 | 1 | YES | YES |
| 2016 | Understanding the Factors That Impact the Popularity of GitHub Repo... | Borges et al. | 2016 IEEE International Conference on... | 10.1109/icsme.2016.31 | 5,16 | YES | YES |
| 2017 | A Systematic Mapping Study of Software Development With GitHub | Cosentino et al. | IEEE Access | 10.1109/access.2017.2682323 | 1,10 | YES | YES |
| 2017 | An Empirical Comparison of Model Validation Techniques for Defect P... | Tantithamthavorn et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2016.2584050 | 7,12 | YES | YES |
| 2017 | Comments on ScottKnottESD in response to "An empirical comparison o... | Herbold, Steffen | IEEE Transactions on Software Enginee... | 10.1109/tse.2017.2748129 | 12 | YES | YES |
| 2017 | Curating GitHub for engineered software projects | Munaiah et al. | Empirical Software Engineering | 10.1007/s10664-017-9512-6 | 3,4,11 | YES | YES |
| 2017 | DéjàVu: a map of code duplicates on GitHub | Lopes et al. | Proceedings of the ACM on Programming... | 10.1145/3133908 | 9,10 | YES | YES |
| 2017 | Empirical software engineering experts on the use of students and p... | Falessi et al. | Empirical Software Engineering | 10.1007/s10664-017-9523-3 | 4 | YES | YES |
| 2018 | A Comparative Study to Benchmark Cross-Project Defect Prediction Ap... | Herbold et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2017.2724538 | 12 | YES | YES |
| 2018 | A comparative study to benchmark cross-project defect prediction ap... | Herbold et al. | Proceedings of the 40th International... | 10.1145/3180155.3182542 | 12 | YES | YES |
| 2018 | Authors’ Reply to “Comments on ‘Researcher Bias: The Use of Machine... | Shepperd et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2017.2731308 | 7 | YES | YES |
| 2018 | Building the universal archive of source code | Abramatic et al. | Communications of the ACM | 10.1145/3183558 | 2 | YES | YES |
| 2018 | PyDriller: Python framework for mining software repositories | Spadini et al. | Proceedings of the 2018 26th ACM Join... | 10.1145/3236024.3264598 | 1 | YES | YES |
| 2018 | Reproducibility and credibility in empirical software engineering: ... | Rodríguez-Pérez et al. | Information and Software Technology | 10.1016/j.infsof.2018.03.009 | 14 | YES | YES |
| 2018 | There is no random sampling in software engineering research | Amir et al. | Proceedings of the 40th International... | 10.1145/3183440.3195001 | 4,29 | YES | YES |
| 2018 | Threats to validity in search‐based predictive modelling for softwa... | Malhotra et al. | IET Software | 10.1049/iet-sen.2018.5143 | 30 | YES | YES |
| 2018 | Understanding How GitHub Supports Curation Repositories | Wu et al. | Future Internet | 10.3390/fi10030029 | 16 | OPT | YES |
| 2019 | Correction of “A Comparative Study to Benchmark Cross-Project Defec... | Herbold et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2018.2790413 | 12 | YES | YES |
| 2019 | Guidelines for Human-AI Interaction | Amershi et al. | Proceedings of the 2019 CHI Conferenc... | 10.1145/3290605.3300233 | 21 | OPT | YES |
| 2019 | Identifying, categorizing and mitigating threats to validity in sof... | Ampatzoglou et al. | Information and Software Technology | 10.1016/j.infsof.2018.10.006 | 6,7,8,30 | YES | YES |
| 2019 | Mitigating Threats to Validity in Empirical Software Engineering: A... | Mustafa et al. | 2019 IEEE 43rd Annual Computer Softwa... | 10.1109/compsac.2019.10227 | 30 | YES | YES |
| 2019 | RapidRelease - A Dataset of Projects and Issues on Github with Rapi... | Joshi et al. | 2019 IEEE/ACM 16th International Conf... | 10.1109/msr.2019.00088 | 3 | YES | YES |
| 2019 | The Software Heritage Graph Dataset: Public Software Development Un... | Pietri et al. | 2019 IEEE/ACM 16th International Conf... | 10.1109/msr.2019.00030 | 2,13 | YES | YES |
| 2019 | The adverse effects of code duplication in machine learning models ... | Allamanis, Miltiadis | Proceedings of the 2019 ACM SIGPLAN I... | 10.1145/3359591.3359735 | 9,12 | YES | YES |
| 2019 | World of Code: An Infrastructure for Mining the Universe of Open So... | Ma et al. | 2019 IEEE/ACM 16th International Conf... | 10.1109/msr.2019.00031 | 1,2 | YES | YES |
| 2020 | PHANTOM: Curating GitHub for engineered software projects using tim... | Pickerill et al. | Empirical Software Engineering | 10.1007/s10664-020-09825-8 | 3,11 | YES | YES |
| 2020 | Publish or perish, but do not forget your software artifacts | Heumüller et al. | Empirical Software Engineering | 10.1007/s10664-020-09851-6 | 13,14 | YES | YES |
| 2020 | The Software Heritage Graph Dataset | Pietri et al. | Proceedings of the 17th International... | 10.1145/3379597.3387510 | 2 | YES | YES |
| 2021 | A ground-truth dataset and classification model for detecting bots ... | Golzadeh et al. | Journal of Systems and Software | 10.1016/j.jss.2021.110911 | 11,16,17 | YES | YES |
| 2021 | ACM SIGSOFT Empirical Standards Released | Ralph, Paul | ACM SIGSOFT Software Engineering Notes | 10.1145/3437479.3437483 | 15 | YES | YES |
| 2021 | Promises and Perils of Inferring Personality on GitHub | van Mil et al. | Proceedings of the 15th ACM / IEEE In... | 10.1145/3475716.3475775 | 5,10 | YES | YES |
| 2021 | Sampling Projects in GitHub for MSR Studies | Dabic et al. | 2021 IEEE/ACM 18th International Conf... | 10.1109/msr52588.2021.00074 | 3,4,10 | YES | YES |
| 2021 | World of code: enabling a research workflow for mining and analyzin... | Ma et al. | Empirical Software Engineering | 10.1007/s10664-020-09905-9 | 2 | YES | YES |
| 2022 | A retrospective study of one decade of artifact evaluations | Winter et al. | Proceedings of the 30th ACM Joint Eur... | 10.1145/3540250.3549172 | 13,14 | YES | YES |
| 2022 | An Empirical Study of Model-Agnostic Techniques for Defect Predicti... | Jiarpakdee et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2020.2982385 | 12 | OPT | YES |
| 2022 | Bot detection in GitHub repositories | Chidambaram et al. | Proceedings of the 19th International... | 10.1145/3524842.3528520 | 5 | YES | YES |
| 2022 | Expectation vs. Experience: Evaluating the Usability of Code Genera... | Vaithilingam et al. | CHI Conference on Human Factors in Co... | 10.1145/3491101.3519665 | 26 | YES | YES |
| 2022 | GitHub Proxy Server: A tool for supporting massive data collection ... | Borges et al. | Proceedings of the XXXVI Brazilian Sy... | 10.1145/3555228.3555276 | 2 | YES | YES |
| 2022 | Problems with SZZ and features: An empirical study of the state of ... | Herbold et al. | Empirical Software Engineering | 10.1007/s10664-021-10092-4 | 11,12 | YES | YES |
| 2022 | Sampling in software engineering research: a critical review and gu... | Baltes et al. | Empirical Software Engineering | 10.1007/s10664-021-10072-8 | 4,5,29,30 | YES | YES |
| 2023 | ChatGPT outperforms crowd workers for text-annotation tasks | Gilardi et al. | Proceedings of the National Academy o... | 10.1073/pnas.2305016120 | 20,21 | YES | YES |
| 2023 | Construct Validity in Software Engineering | Sjøberg et al. | IEEE Transactions on Software Enginee... | 10.1109/tse.2022.3176725 | 6 | YES | YES |
| 2023 | DocMine: A Software Documentation-Related Dataset of 950 GitHub Rep... | Manasa Venigalla et al. | 2023 IEEE/ACM 20th International Conf... | 10.1109/msr59073.2023.00062 | 5 | YES | YES |
| 2023 | GIRT-Data: Sampling GitHub Issue Report Templates | Nikeghbal et al. | 2023 IEEE/ACM 20th International Conf... | 10.1109/msr59073.2023.00026 | 3 | YES | YES |
| 2023 | Grounded Copilot: How Programmers Interact with Code-Generating Models | Barke et al. | Proceedings of the ACM on Programming... | 10.1145/3586030 | 26 | YES | YES |
| 2023 | Inconsistency Detection in Natural Language Requirements using Chat... | Fantechi et al. | 2023 IEEE 31st International Requirem... | 10.1109/re57278.2023.00045 | 21 | OPT | YES |
| 2023 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | Advances in Neural Information Proces... | 10.52202/075280-2020 | 20,21 | YES | YES |
| 2023 | Keep the Ball Rolling: Analyzing Release Cadence in GitHub Projects | Kilic et al. | 2023 IEEE/ACM 20th International Conf... | 10.1109/msr59073.2023.00058 | 3 | YES | YES |
| 2023 | Large Language Models for Software Engineering: Survey and Open Pro... | Fan et al. | 2023 IEEE/ACM International Conferenc... | 10.1109/icse-fose59343.2023.00008 | 22 | YES | YES |
| 2023 | Leakage and the reproducibility crisis in machine-learning-based sc... | Kapoor et al. | Patterns | 10.1016/j.patter.2023.100804 | 9,14 | YES | YES |
| 2023 | Multi-granular software annotation using file-level weak labelling | Sas et al. | Empirical Software Engineering | 10.1007/s10664-023-10423-7 | 18,19 | OPT | YES |
| 2023 | Operationalizing validity of empirical software engineering studies | Härtel et al. | Empirical Software Engineering | 10.1007/s10664-023-10370-3 | 6,7,8 | YES | YES |
| 2023 | PI-Link: A Ground-Truth Dataset of Links Between Pull-Requests and ... | Alshara et al. | IEEE Access | 10.1109/access.2022.3232982 | 11 | YES | YES |
| 2023 | Revisiting the reproducibility of empirical software engineering st... | Gonzalez-Barahona et al. | Information and Software Technology | 10.1016/j.infsof.2023.107318 | 14 | YES | YES |
| 2023 | The promises and perils of open source software release and usage b... | Eibl et al. | Proceedings of the 24th Annual Intern... | 10.1145/3598469.3598489 | 5,10 | YES | YES |
| 2023 | The software heritage license dataset (2022 edition) | Gonzalez-Barahona et al. | Empirical Software Engineering | 10.1007/s10664-023-10377-w | 2 | YES | YES |
| 2023 | Threats to validity in software engineering research: A critical re... | Verdecchia et al. | Information and Software Technology | 10.1016/j.infsof.2023.107329 | 6,7,8,30 | YES | YES |
| 2023 | Using Architecture Decision Records in Open Source Projects—An MSR ... | Buchgeher et al. | IEEE Access | 10.1109/access.2023.3287654 | 3 | YES | YES |
| 2023 | Wasmizer: Curating WebAssembly-driven Projects on GitHub | Nicholson et al. | 2023 IEEE/ACM 20th International Conf... | 10.1109/msr59073.2023.00031 | 3 | YES | YES |
| 2024 | Adding repository custom instructions for GitHub Copilot | GitHub | Product documentation | https://docs.github.com/en/copilo... | 22,26,29 | YES | YES-URL |
| 2024 | Claude Code: Memory and project configuration | Anthropic | Product documentation | https://docs.anthropic.com/en/doc... | 22,25,29 | YES | YES-URL |
| 2024 | Introducing the Model Context Protocol | Anthropic | Product announcement | https://www.anthropic.com/news/mo... | 22,28 | YES | YES-URL |
| 2024 | Large Language Models for Software Engineering: A Systematic Litera... | Hou et al. | ACM Transactions on Software Engineer... | 10.1145/3695988 | 1,22 | YES | YES |
| 2024 | Lessons from Building StackSpot AI: A Contextualized AI Coding Assi... | Pinto et al. | Proceedings of the 46th International... | 10.1145/3639477.3639751 | 24 | OPT | YES |
| 2024 | Measuring GitHub Copilot's Impact on Productivity | Ziegler et al. | Communications of the ACM | 10.1145/3633453 | 26 | YES | YES |
| 2024 | Research artifacts in software engineering publications: Status and... | Liu et al. | Journal of Systems and Software | 10.1016/j.jss.2024.112032 | 13,14 | YES | YES |
| 2024 | Rules for AI: Project rules in Cursor | Cursor | Product documentation | https://cursor.com/docs/rules | 22,24,29 | YES | YES-URL |
| 2024 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Jimenez et al. | ICLR | https://openreview.net/forum?id=V... | 12,11,10 | YES | YES-OPENREVIEW |
| 2025 | ACM SIGSOFT SEN Empirical Software Engineering: Introducing Our New... | Bogner et al. | ACM SIGSOFT Software Engineering Notes | 10.1145/3772008.3772012 | 15 | YES | YES |
| 2025 | AGENTS.md: Open format for repository agent context | Agentic AI Foundation | Web specification | https://agents.md/ | 22,23,29 | YES | YES-URL |
| 2025 | Artifact Evaluations for Stronger Research Results | Beyer et al. | Proceedings of the 33rd ACM Internati... | 10.1145/3696630.3728623 | 13 | YES | YES |
| 2025 | Can LLMs Replace Manual Annotation of Software Engineering Artifacts? | Ahmed et al. | 2025 IEEE/ACM 22nd International Conf... | 10.1109/msr66628.2025.00086 | 17,19,20 | YES | YES |
| 2025 | Generative AI for Requirements Engineering: A Systematic Literature... | Cheng et al. | Software: Practice and Experience | 10.1002/spe.70029 | 21,22 | YES | YES |
| 2025 | Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven ... | Li et al. | 2025 40th IEEE/ACM International Conf... | 10.1109/ase63991.2025.00276 | 22,27 | YES | YES |
| 2025 | Research artifacts in secondary studies: A systematic mapping in so... | Huotala et al. | Information and Software Technology | 10.1016/j.infsof.2025.107830 | 13 | YES | YES |
| 2025 | Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Bas... | Aleithan, Reem | 2025 IEEE/ACM 47th International Conf... | 10.1109/icse-companion66252.2025.... | 12 | YES | YES |
| 2025 | Software Traceability with Explainable Pretrained Language Models: ... | Puspa et al. | 2025 15th International Conference on... | 10.1109/icts67612.2025.11369619 | 12 | OPT | YES |
| 2025 | Understanding and Enhancing CS Students’ Interaction Experience wit... | Long et al. | ACM Transactions on Software Engineer... | 10.1145/3785479 | 24 | OPT | YES |
| 2026 | A Systematic Literature Review on Detecting Software Vulnerabilitie... | Kaniewski et al. | ACM Transactions on Software Engineer... | 10.1145/3815425 | 22 | YES | YES |
| 2026 | An audit of machine learning experiments on software defect prediction | Destefanis et al. | Empirical Software Engineering | 10.1007/s10664-025-10797-w | 7 | OPT | YES |
| 2026 | Enhancing Automated Unit Test Generation with Large Language Models... | Zhang et al. | ACM Transactions on Software Engineer... | 10.1145/3802827 | 22 | YES | YES |
| 2026 | Measuring the Impact of AI Coding Assistants (e.g., GitHub Copilot,... | Dua Nadeem et al. | Kashf Journal of Multidisciplinary Re... | 10.71146/kjmr877 | 26 | YES | YES |
| 2026 | OLAF: Towards Robust LLM-Based Annotation Framework in Empirical So... | Imran et al. | Proceedings of the 2026 IEEE/ACM Inte... | 10.1145/3786149.3788306 | 18,19 | OPT | YES |
| 2026 | Performance analysis of AI-generated code: A case study of Copilot,... | Li et al. | Empirical Software Engineering | 10.1007/s10664-025-10776-1 | 18 | OPT | YES |
| 2026 | Prompt Engineering in Software Engineering Education: An Empirical ... | Kassab, Mohamad | Proceedings of the 34th ACM Internati... | 10.1145/3803437.3805788 | 22,27 | YES | YES |
| 2026 | Promptware Engineering: Software Engineering for Prompt-Enabled Sys... | Chen et al. | ACM Transactions on Software Engineer... | 10.1145/3796535 | 22,27 | YES | YES |
| 2026 | Software refactoring research with large language models: A systema... | Martinez et al. | Journal of Systems and Software | 10.1016/j.jss.2025.112762 | 22 | YES | YES |

## 5. Must-cite shortlist (for IST Related Work rewrite)

Count: **74**

- 1960 — **A Coefficient of Agreement for Nominal Scales** — `10.1177/001316446002000104`
- 1977 — **The Measurement of Observer Agreement for Categorical Data** — `10.2307/2529310`
- 1991 — **A Coefficient of Agreement for Nominal Scales: An Asymmetric Version of Kappa** — `10.1177/0013164491511008`
- 2004 — **The perils and pitfalls of mining SourceForge** — `10.1049/ic:20040467`
- 2005 — **Reporting guidelines for controlled experiments in software engineering** — `10.1109/isese.2005.1541818`
- 2008 — **Guidelines for conducting and reporting case study research in software engineering** — `10.1007/s10664-008-9102-8`
- 2008 — **The road ahead for Mining Software Repositories** — `10.1109/fosm.2008.4659248`
- 2009 — **Cross-project defect prediction** — `10.1145/1595696.1595713`
- 2011 — **Evaluating defect prediction approaches: a benchmark and an extensive comparison** — `10.1007/s10664-011-9173-9`
- 2011 — **On the reproducibility of empirical software engineering studies based on data retrieved from development repositories** — `10.1007/s10664-011-9181-9`
- 2012 — **A unifying view on dataset shift in classification** — `10.1016/j.patcog.2011.06.019`
- 2012 — **Experimentation in Software Engineering** — `10.1007/978-3-642-29044-2`
- 2012 — **GHTorrent: Github's data from a firehose** — `10.1109/msr.2012.6224294`
- 2012 — **Leakage in data mining** — `10.1145/2382577.2382579`
- 2013 — **Data Quality: Some Comments on the NASA Software Defect Datasets** — `10.1109/tse.2013.11`
- 2013 — **The impact of tangled code changes** — `10.1109/msr.2013.6624018`
- 2014 — **Influence of social and technical factors for evaluating contribution in GitHub** — `10.1145/2568225.2568315`
- 2014 — **Lean GHTorrent: GitHub data on demand** — `10.1145/2597073.2597126`
- 2014 — **Researcher Bias: The Use of Machine Learning in Software Defect Prediction** — `10.1109/tse.2014.2322358`
- 2014 — **The promises and perils of mining GitHub** — `10.1145/2597073.2597074`
- 2015 — **An in-depth study of the promises and perils of mining GitHub** — `10.1007/s10664-015-9393-5`
- 2015 — **Guidelines for conducting systematic mapping studies in software engineering: An update** — `10.1016/j.infsof.2015.03.007`
- 2015 — **The impact of tangled code changes on defect prediction models** — `10.1007/s10664-015-9376-6`
- 2015 — **Views on Internal and External Validity in Empirical Software Engineering** — `10.1109/icse.2015.24`
- 2016 — **A Map of Threats to Validity of Systematic Literature Reviews in Software Engineering** — `10.1109/apsec.2016.031`
- 2016 — **Comments on “Researcher Bias: The Use of Machine Learning in Software Defect Prediction”** — `10.1109/tse.2016.2553030`
- 2016 — **Understanding the Factors That Impact the Popularity of GitHub Repositories** — `10.1109/icsme.2016.31`
- 2017 — **A Systematic Mapping Study of Software Development With GitHub** — `10.1109/access.2017.2682323`
- 2017 — **An Empirical Comparison of Model Validation Techniques for Defect Prediction Models** — `10.1109/tse.2016.2584050`
- 2017 — **Comments on ScottKnottESD in response to "An empirical comparison of model validation techniques for defect prediction models"** — `10.1109/tse.2017.2748129`
- 2017 — **Curating GitHub for engineered software projects** — `10.1007/s10664-017-9512-6`
- 2017 — **DéjàVu: a map of code duplicates on GitHub** — `10.1145/3133908`
- 2018 — **A Comparative Study to Benchmark Cross-Project Defect Prediction Approaches** — `10.1109/tse.2017.2724538`
- 2018 — **A comparative study to benchmark cross-project defect prediction approaches** — `10.1145/3180155.3182542`
- 2018 — **Authors’ Reply to “Comments on ‘Researcher Bias: The Use of Machine Learning in Software Defect Prediction’”** — `10.1109/tse.2017.2731308`
- 2018 — **Building the universal archive of source code** — `10.1145/3183558`
- 2018 — **PyDriller: Python framework for mining software repositories** — `10.1145/3236024.3264598`
- 2018 — **There is no random sampling in software engineering research** — `10.1145/3183440.3195001`
- 2018 — **Threats to validity in search‐based predictive modelling for software engineering** — `10.1049/iet-sen.2018.5143`
- 2019 — **Correction of “A Comparative Study to Benchmark Cross-Project Defect Prediction Approaches”** — `10.1109/tse.2018.2790413`
- 2019 — **Identifying, categorizing and mitigating threats to validity in software engineering secondary studies** — `10.1016/j.infsof.2018.10.006`
- 2019 — **Mitigating Threats to Validity in Empirical Software Engineering: A Traceability Case Study** — `10.1109/compsac.2019.10227`
- 2019 — **The Software Heritage Graph Dataset: Public Software Development Under One Roof** — `10.1109/msr.2019.00030`
- 2019 — **The adverse effects of code duplication in machine learning models of code** — `10.1145/3359591.3359735`
- 2019 — **World of Code: An Infrastructure for Mining the Universe of Open Source VCS Data** — `10.1109/msr.2019.00031`
- 2020 — **PHANTOM: Curating GitHub for engineered software projects using time-series clustering** — `10.1007/s10664-020-09825-8`
- 2020 — **Publish or perish, but do not forget your software artifacts** — `10.1007/s10664-020-09851-6`
- 2020 — **The Software Heritage Graph Dataset** — `10.1145/3379597.3387510`
- 2021 — **A ground-truth dataset and classification model for detecting bots in GitHub issue and PR comments** — `10.1016/j.jss.2021.110911`
- 2021 — **ACM SIGSOFT Empirical Standards Released** — `10.1145/3437479.3437483`
- 2021 — **Sampling Projects in GitHub for MSR Studies** — `10.1109/msr52588.2021.00074`
- 2021 — **World of code: enabling a research workflow for mining and analyzing the universe of open source VCS data** — `10.1007/s10664-020-09905-9`
- 2022 — **A retrospective study of one decade of artifact evaluations** — `10.1145/3540250.3549172`
- 2022 — **Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models** — `10.1145/3491101.3519665`
- 2022 — **Problems with SZZ and features: An empirical study of the state of practice of defect prediction data collection** — `10.1007/s10664-021-10092-4`
- 2022 — **Sampling in software engineering research: a critical review and guidelines** — `10.1007/s10664-021-10072-8`
- 2023 — **ChatGPT outperforms crowd workers for text-annotation tasks** — `10.1073/pnas.2305016120`
- 2023 — **Grounded Copilot: How Programmers Interact with Code-Generating Models** — `10.1145/3586030`
- 2023 — **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** — `10.52202/075280-2020`
- 2023 — **Leakage and the reproducibility crisis in machine-learning-based science** — `10.1016/j.patter.2023.100804`
- 2023 — **Revisiting the reproducibility of empirical software engineering studies based on data retrieved from development repositories** — `10.1016/j.infsof.2023.107318`
- 2023 — **Threats to validity in software engineering research: A critical reflection** — `10.1016/j.infsof.2023.107329`
- 2024 — **Adding repository custom instructions for GitHub Copilot** — `https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot`
- 2024 — **Claude Code: Memory and project configuration** — `https://docs.anthropic.com/en/docs/claude-code/memory`
- 2024 — **Introducing the Model Context Protocol** — `https://www.anthropic.com/news/model-context-protocol`
- 2024 — **Large Language Models for Software Engineering: A Systematic Literature Review** — `10.1145/3695988`
- 2024 — **Measuring GitHub Copilot's Impact on Productivity** — `10.1145/3633453`
- 2024 — **Research artifacts in software engineering publications: Status and trends** — `10.1016/j.jss.2024.112032`
- 2024 — **Rules for AI: Project rules in Cursor** — `https://cursor.com/docs/rules`
- 2024 — **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** — `https://openreview.net/forum?id=VTF8yNQM66`
- 2025 — **AGENTS.md: Open format for repository agent context** — `https://agents.md/`
- 2025 — **Can LLMs Replace Manual Annotation of Software Engineering Artifacts?** — `10.1109/msr66628.2025.00086`
- 2025 — **Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Based Code Models** — `10.1109/icse-companion66252.2025.00075`
- 2026 — **Promptware Engineering: Software Engineering for Prompt-Enabled Systems** — `10.1145/3796535`

## 6. Grey literature note (Topics 23–28)

For `AGENTS.md`, Cursor Rules, Claude project memory, Copilot custom instructions, and MCP, peer-reviewed methodological papers are still thin. Verified primary documentation is included because these filenames/protocols are the discovery predicates of the target study. They must be labeled as grey/primary sources, not as empirical method papers.

## 7. Discard / quality filter summary

Rejected or demoted during curation (non-exhaustive categories):
- Crossref keyword false positives (medicine, genomics, oil-leakage, dating apps, etc.).
- Publisher tutorial/book-chapter noise around “GitHub Copilot”.
- PeerJ table/figure DOIs, SSRN-only duplicates of later journal versions, TOC/cover pages.
- Entries whose DOI did not resolve in Crossref (earlier pipeline stages).

Pipeline discarded DOI attempts recorded: **0** (see `verified_records.json`).

## 8. Files in this package

| File | Role |
|---|---|
| `SOTA_INVESTIGATION_REPORT.md` | This report |
| `curated_enriched.json` | Machine-readable curated records + analytical fields |
| `verified_records.json` | Pre-curation verified Crossref set |
| `search_by_topic.json` | Raw topic search dump |

---

_End of report. Manuscript not modified._