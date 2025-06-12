# NMF_XTRACT_comparison

## General information

This repository contains analysis scripts from "An anthropoid/strepsirrhine divergence in ventral visual stream connectivity" by Hunt et al. (2025). These scripts enable the user to quantitatively compare NMF output with XTRACT output, to benchmark the performance of NMF at reconstructing known white matter tracts. The 'GM' stands for 'grey matter', as these scripts compare grey matter innervation patterns from each analysis.

All materials herein are protected under a [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.

## Explanation of files

I wrote four analysis scripts to assess and visualise the performance of NMF against XTRACT. Sorted in order of usage (first to last), they are:
```
.
├── analyse_GM.sh
│   ├── correlateGM.py
│   └── orderCorrelationsGM.py
└── GMcorr_boxplots.R
```

* `analyse_GM.sh` is a shell script which calls `correlateGM.py` and `orderCorrelationsGM.py` to generate NMF-XTRACT correlation matrices and associated data visualisations.
    * `correlateGM.py` generates a correlation matrix between two user-specified datasets: one from NMF and one from XTRACT.
    * `orderCorrelationsGM.py` uses the outputs of correlateGM.py to generate a matrix and a visualisation of the maximum correlations between NMF and XTRACT analyses. This allows the user to visualise NMF decomposition performance at a glance.
* `GMcorr_boxplots.R` uses the output of `orderCorrelationsGM.py` to generate box plots describing the distribution of maximal correlations at each number of NMF components. This allows the user to identify trends in NMF performance at different component numbers.

## Outcomes

Utilising this pipeline from start to finish will generate:
1. Correlation matrices identifying which NMF component is best-associated with a given XTRACT-derived tract.
2. A matrix of maximal correlations, allowing for quantitative comparison of NMF performance at different component numbers.
3. Visualisations of (1) and (2), as well as a series of box plots showing distributions of maximal correlations at different NMF component numbers.

These analyses and visualisations formed the basis of Figure 2 in [my paper](https://doi.org/10.1101/2025.05.19.653861) benchmarking the use of NMF to reconstruct white matter tracts in non-human brains.