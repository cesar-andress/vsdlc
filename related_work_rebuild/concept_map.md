# Concept map — literature clusters for the Related Work rebuild

```mermaid
flowchart TB
  subgraph P["Our problem"]
    C["Target-conditional contamination<br/>of AI-instruction discovery frames"]
    S["Consensus-protocol sensitivity"]
    F["Predicate-family structure"]
  end

  subgraph A["A. MSR methodology & discovery"]
    A1["Hassan 2008"]
    A2["GHTorrent / Lean GHTorrent"]
    A3["PyDriller"]
    A4["World of Code"]
    A5["Software Heritage"]
    A6["Cosentino mapping 2017"]
  end

  subgraph B["B. Sampling bias & GitHub perils"]
    B1["Howison 2004"]
    B2["Kalliamvakou 2014/2015"]
    B3["Baltes & Ralph 2022"]
    B4["Dabic 2021"]
    B5["Borges / Tsay metadata"]
  end

  subgraph D["D. Curation ≠ our construct"]
    D1["Munaiah RepoReapers 2017"]
    D2["PHANTOM 2020"]
    D3["Golzadeh bots 2021"]
  end

  subgraph E["E. Construct validity & ToV"]
    E1["Wohlin / Runeson"]
    E2["Siegmund 2015"]
    E3["Ampatzoglou 2019"]
    E4["Verdecchia 2023"]
    E5["Jedlitschka / Petersen / Ralph"]
  end

  subgraph G["G. Dataset contamination senses"]
    G1["Kaufman leakage"]
    G2["Moreno dataset shift"]
    G3["Lopes DéjàVu / Allamanis"]
    G4["Kapoor 2023"]
    G5["Zimmermann cross-project"]
  end

  subgraph H["H. Dataset & label validation"]
    H1["D'Ambros benchmark"]
    H2["Shepperd data quality / bias"]
    H3["Herzig tangled"]
    H4["Herbold SZZ 2022"]
    H5["Tantithamthavorn 2017"]
  end

  subgraph I["I. Reproducibility & artifacts"]
    I1["González-Barahona 2011/2023"]
    I2["Heumüller / Liu / Winter"]
    I3["da Silva replication map"]
  end

  subgraph J["J. Annotation & agreement"]
    J1["Cohen / Landis"]
    J2["Gilardi / Zheng LLM judges"]
    J3["Ahmed MSR 2025"]
    J4["Fantechi / Amershi"]
  end

  subgraph K["K. AI instruction / promptware"]
    K1["Chen Promptware 2026"]
    K2["Hou / Fan LLM4SE"]
    K3["Copilot studies"]
    K4["Grey docs: AGENTS.md, Cursor, MCP"]
  end

  A -->|"retrieval solved; membership not"| C
  B -->|"perils known; no instruction-frame audit"| C
  D -->|"engineered/bot filters ≠ analytic population"| C
  E -->|"ToV discourse; no worksheet protocol"| S
  G -->|"different contamination sense"| C
  H -->|"label validation cousins"| S
  I -->|"replay norms"| C
  J -->|"agreement tools; LLM annotators"| S
  K -->|"phenomenon without mining audit"| F

  C --- S
  C --- F
```

## Cluster reading order (for section structure)

1. **Perils & sampling** (B) → establish that path hits ≠ population membership.  
2. **Curation cousins** (D) → show engineered filters are insufficient.  
3. **Contamination senses** (G+H) → disambiguate our contamination from leakage/duplication.  
4. **Validity & reporting** (E+I) → justify protocol sensitivity and replication packages.  
5. **Annotation** (J) → situate multi-coder consensus and LLM adjudication limits.  
6. **Instruction artifacts** (K) → show phenomenon growth without methodological audit.  
7. **Gap statement** → contribution begins at the intersection of C∩S∩F.
