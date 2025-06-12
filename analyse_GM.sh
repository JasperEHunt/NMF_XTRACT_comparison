#! /bin/sh

myPath="/path/to/NMF/analysis/"

for compNumb in 10 50 60 100 200; do
    python ${myPath}analysis_scripts/correlateGM.py ${compNumb} ${myPath}NMF_GM_${compNumb}.LR.dscalar.nii ${myPath}merged_xtract.dscalar.nii ${myPath}
done

python orderCorrelationsGM.py ${myPath}
