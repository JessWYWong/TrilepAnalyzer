#!/bin/bash

#things to check: 
# - doHists.py for input file
# - sample.py for which dataset ttbar/DY
# - analyze.py for SR/CR low/high HT
# - cutList.py

source switchToFinal.sh
python doCondorKinematics.py
# python doKinematics.py
# root -l DrawChiSq.C