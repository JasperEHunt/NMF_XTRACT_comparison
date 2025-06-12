# NMF_XTRACT_comparison

## General information

This repository contains analysis scripts from "An anthropoid/strepsirrhine divergence in ventral visual stream connectivity" by Hunt et al. (2025). These scripts enable the user to quantitatively compare NMF output with XTRACT output, to benchmark the performance of NMF at reconstructing known white matter tracts.

All materials herein are protected under a [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.

## Explanation of files
`analyse_GM.sh` is a shell script which calls `correlateGM.py` and `orderCorrelationsGM.py` to analyse several NMF-generated data files.

`correlateGM.py` generates a correlation matrix between an NMF dataset and an XTRACT dataset.

`orderCorrelationsGM.py` uses the output of correlateGM.py to generate a matrix of maximum correlations between XTRACT data and NMF output with different component numbers. This allows the user to determine, at a glance, which NMF decomposition has the best performance.
