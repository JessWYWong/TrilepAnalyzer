#!/bin/bash


###REMEMBER to CHECK step1Dir in doHists AND analyze.py_final before submitting!#############################
# source switchToFinal.sh  
# python doCondorKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs FRCR2
python doCondorKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs SR
python doCondorKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs CR2


####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
# source switchToNoDDBKGfinal.sh  
# 
# python doCondorKinematics.py kinematics_LJMet80x_extra_wGammas_noDDBKG SR
