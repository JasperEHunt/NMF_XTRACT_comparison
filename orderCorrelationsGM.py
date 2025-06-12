#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 13:49:46 2022
Updated on Wed Jun 11 15:19:00 2025 -- restructured comments, improved readability

@author: Jasper Hunt

Script to assemble a matrix of maximal correlations for each atlas-derived tract, at each number of NMF components.

orderCorrelationsGM requires the following libraries:
    sys, pandas, numpy, matplotlib, seaborn

Usage:
    python orderCorrelationsGM.py <NMFpath>

Compulsory argument:
	<NMFpath> - Path to directory containing outputs of correlateGM.py.

Required directory structure:
.
└── Analysis Path/
    ├── 10_NMF_GM_correlation.csv
    ├── 50_NMF_GM_correlation.csv
    ├── 60_NMF_GM_correlation.csv
    ├── 100_NMF_GM_correlation.csv
    └── 200_NMF_GM_correlation.csv

Example run:
    > python orderCorrelationsGM.py 'My/analysis/path/'

orderCorrelationsGM outputs two files:
	- A .csv file containing the final correlation matrix. Each column represents a tract identified via atlas-based tractography.
      Each row represents an NMF component number. Each cell identifies the maximal correlation among NMF components for a given tract.
	- A .png file containing a graphical representation of the correlation matrix.
"""

# Load required libraries, output error if libraries are missing.
try:
    import sys
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("Required libraries are installed.")
except:
    print("One or more libraries is missing. This script requires 'sys', 'pandas', 'numpy', 'matplotlib', and 'seaborn'.")

# User argument 
NMFpath = sys.argv[1] # user-entered path to NMF analysis files

# Function to identify each atlas tract's maximal correlation with NMF components
def max_corr(compNumb):
    compMax = []
    for column in compNumb:
        print(compNumb[column].max())
        compMax.append(compNumb[column].max())
    return compMax

# Populate an empty array for final correlation matrix
# Array size refers to 42 atlas-based tracts, 5 NMF component numbers
finalCorrMat = np.empty([0,42])

# Loop to identify max correlations for 10, 50, 60, 100, and 200 NMF components
for components in ["10", "50", "60", "100", "200"]:
    GM_comps = np.transpose(pd.DataFrame(np.loadtxt(open(NMFpath + components + "_NMF_GM_correlation.csv", "rb"), delimiter=",")))
    finalCorrMat = np.vstack((finalCorrMat, np.array(max_corr(GM_comps))))

# Save output as .csv and graphical plot
print("Saving correlation matrix in .csv format")
np.savetxt(NMFpath + "finalCompare_GM.csv", finalCorrMat, delimiter=",")

print("Saving matrix graphic")
# Generate a plot using Seaborn
plt.figure(figsize=(30, 4))
graphicOut = sns.heatmap(finalCorrMat, linewidth=0.25, cmap='plasma', xticklabels=True, yticklabels=True,)
graphicOut.set_xlabel('Atlas tract')
graphicOut.xaxis.tick_top()
graphicOut.xaxis.set_label_position('top')
graphicOut.set_ylabel('NMF component number')
plt.savefig(NMFpath + "finalCompare_GM.png")
