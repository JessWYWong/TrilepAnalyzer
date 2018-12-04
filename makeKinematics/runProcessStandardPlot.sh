#!/bin/bash


####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
# #######################################################################################################
# 1st attempt dor 2018data
day=2018_11_30

# #####doKinematics.py <folder> <whichPlots?>
python -u doKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_SR_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
python -u plotKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_SR_$day 0 0
python -u plotKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_SR_$day 0 1


# #####doKinematics.py <folder> <whichPlots?>
python -u doKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_CR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
python -u plotKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_CR2_$day 0 0
python -u plotKinematics.py kinematics_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_NoSYS_2016SFs_CR2_$day 0 1


#######################################################################################################

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##checking MCBKg Gamma samples
# 
# day=2017_12_1
# source switchToNoDDBKGfinal.sh  
# 
# python -u doKinematics.py kinematics_LJMet80x_extra_wGammas_noDDBKG_SR_$day 0

