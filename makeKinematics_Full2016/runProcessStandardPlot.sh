#!/bin/bash

# source switchToNew.sh 
###doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR2_2017_3_2 1
# python doKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR1_2017_3_2 1
# python doKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_CR2_2017_3_2 3 #2 --> Missing METrebinned.
# python doKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 2
# python doKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_fSR_2017_3_2 2
# python doKinematics.py kinematics_FRv21test_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 2

###plotKinematics.py <folder> <blind?> <log?>
# yLog=1
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR2_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR1_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_CR2_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_fSR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv21test_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv21test_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 0 $yLog
 
# yLog=0
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR2_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_FRCR1_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_CR2_2017_3_2 0 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv20b_PRv6_step2_newMllOScutV2_AllSYS_take2_fSR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv21test_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 1 $yLog
# python plotKinematics.py kinematics_FRv21test_PRv6_step2_newMllOScutV2_AllSYS_take2_SR_2017_3_2 0 $yLog

################################################################################################################

# source switchToNoDDBKGfinal.sh 
# python doKinematics.py kinematics_LJMet24Feb2017_noDDBKG_ALLR_2017_3_2
# python doKinematics.py kinematics_LJMet24Feb2017_noDDBKG_SR_2017_3_2
# python doKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR1_2017_3_2
# python doKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR2_2017_3_2
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_ALLR_2017_3_2 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_SR_2017_3_2 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR1_2017_3_2 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR2_2017_3_2 0 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_ALLR_2017_3_2 0 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_SR_2017_3_2 0 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR1_2017_3_2 0 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR2_2017_3_2 0 1

# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_ALLR_2017_3_2 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_SR_2017_3_2 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR1_2017_3_2 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR2_2017_3_2 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_ALLR_2017_3_2 1 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_SR_2017_3_2 1 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR1_2017_3_2 1 1
# python plotKinematics.py kinematics_LJMet24Feb2017_noDDBKG_CR2_2017_3_2 1 1

###########################################################################################################

# source switchToNoDDBKG.sh  
# python doKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_ALLR_2017_3_3
# python doKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_SR_2017_3_3
# python doKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR1_2017_3_3
# python doKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR2_2017_3_3
# 
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_ALLR_2017_3_3 0 0
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_SR_2017_3_3 0 0 
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR1_2017_3_3 0 0
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR2_2017_3_3 0 0
# 
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_ALLR_2017_3_3 1 0
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_SR_2017_3_3 1 0 
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR1_2017_3_3 1 0
# python plotKinematics.py kinematics_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_nuDYxsec_noDDBKG_CR2_2017_3_3 1 0

# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_ALLR_2017_3_3
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_SR_2017_3_3
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR1_2017_3_3
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR2_2017_3_3
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_ALLR_2017_3_3 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_SR_2017_3_3 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR1_2017_3_3 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR2_2017_3_3 0 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_ALLR_2017_3_3 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_SR_2017_3_3 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR1_2017_3_3 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_noDDBKG_CR2_2017_3_3 1 0

#####################################################################################################
# source switchToFinal.sh  
# 
# python doKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR2_2017_3_3 1
# python doKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR1_2017_3_3 1
# python doKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_CR2_2017_3_3 2
# python doKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_SR_2017_3_3 2
# python doKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_fSR_2017_3_3 2

# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR2_2017_3_3 0 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR1_2017_3_3 0 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_CR2_2017_3_3 0 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_SR_2017_3_3 1 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_fSR_2017_3_3 1 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_SR_2017_3_3 0 0
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_fSR_2017_3_3 0 0
# 
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR2_2017_3_3 0 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_FRCR1_2017_3_3 0 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_CR2_2017_3_3 0 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_SR_2017_3_3 1 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_fSR_2017_3_3 1 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_SR_2017_3_3 0 1
# python plotKinematics.py kinematics_FRv22_PRv6_step2_LJMet24Feb2017_AllSYS_fSR_2017_3_3 0 1

######################################################################################################
# source switchToNew.sh 
##doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv23test_PRv6_step2_newMllOScutV2_AllSYS_SR_2017_3_3 2

# yLog=1
# python plotKinematics.py kinematics_FRv23test_PRv6_step2_newMllOScutV2_AllSYS_SR_2017_3_3 1 $yLog
# python plotKinematics.py kinematics_FRv23test_PRv6_step2_newMllOScutV2_AllSYS_SR_2017_3_3 0 $yLog 
# yLog=0
# python plotKinematics.py kinematics_FRv23test_PRv6_step2_newMllOScutV2_AllSYS_SR_2017_3_3 1 $yLog
# python plotKinematics.py kinematics_FRv23test_PRv6_step2_newMllOScutV2_AllSYS_SR_2017_3_3 0 $yLog

#######################################################################################################

# source switchToFinal.sh  
##doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_2017_3_4 1
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_2017_3_4 1
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_4 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_4 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_4 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1000_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1100_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1200_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1300_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1400_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1000noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1100noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1200noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1300noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1400noWeight_2017_3_5 2
# python doKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_2017_3_6 2

##plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_2017_3_4 0 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_2017_3_4 0 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_4 0 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_4 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_4 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_5 0 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1000_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1100_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1200_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1300_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1400_2017_3_5 1 0
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_2017_3_6 0 0

# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_2017_3_4 0 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_2017_3_4 0 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_4 0 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_4 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_4 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR2_2017_3_5 0 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1000_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1100_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1200_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1300_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST1400_2017_3_5 1 1
# python plotKinematics.py kinematics_FRv24_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_2017_3_6 0 1

######################################################################################################

# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_2017_3_4
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_2017_3_4
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_2017_3_4
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_2017_3_4
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_2017_3_4 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_2017_3_4 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_2017_3_4 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_2017_3_4 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_2017_3_4 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_2017_3_4 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_2017_3_4 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_2017_3_4 0 0


######################################################################################################

# day=2017_3_6
# source switchToFinal.sh  
# 
# python doKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_$day 0
# python doKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_$day 0
# 
# python plotKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_$day 0 0
# 
# python plotKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv29CR1_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR2_$day 0 1


######################################################################################################

# day=2017_3_6
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1CR2_$day 0
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_$day 1
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_$day 1
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_$day 1
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_$day 1
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRnoWeight_$day 1
# python doKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700noWeight_$day 1

# ylog=0
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1CR2_$day 0 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_$day 0 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRnoWeight_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700noWeight_$day 1 $ylog
# 
# ylog=1
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_FRCR1CR2_$day 0 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_CR1CR2_$day 0 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_SR_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSR_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRnoWeight_$day 1 $ylog
# python plotKinematics.py kinematics_FRv27_PRv6_step2_LJMet24Feb2017_newMuTrkS_AllSYS_fSRST700noWeight_$day 1 $ylog


######################################################################################################
##using new DY samples - amcatnlo M50 
# 
# day=2017_3_9
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_nuDYxsec_newMuTrkS_noDDBKG_CR2_$day 0 0

######################################################################################################
##using new DY samples - madgraph_combined M50 

# day=2017_3_9
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_mgDYcombined_newMuTrkS_noDDBKG_CR2_$day 0 0

#######################################################################################################

# day=2017_3_9
# source switchToFinal.sh  
# ##doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSRST700_$day 2
# python doKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSRST700noWeight_$day 2
# 
##plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSRST700_$day 1 0

# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv24_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_fSRST700_$day 1 1

######################################################################################################

# day=2017_3_10
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR1_$day 0
# python doKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 0
# 
# python plotKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 0 0
# 
# python plotKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv29CR1_PRv9_step2_LJMet24Feb2017_postPreapproval_AllSYS_FRCR2_$day 0 1

########################################################################################################
##using WZinc, ZZinc, TTWq, TTZq samples 

# day=2017_3_10
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_VVincTTVq_noDDBKG_CR2_$day 0 0

# python doKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_TTVq_noDDBKG_CR2_$day 0 0
# 

################################################################################################

# day=2017_3_10
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv24_PRvEltest_step2_LJMet24Feb2017_postPreapproval_noSYS_fSRST700_$day 1
# python doKinematics.py kinematics_FRv24_PRvMutest_step2_LJMet24Feb2017_postPreapproval_noSYS_fSRST700_$day 1
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet24Feb2017_postPreapproval_noSYS_fSRST700_$day 1

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples 

day=2017_3_15
source switchToNoDDBKGfinal.sh  
python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day
python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day
python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day
python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day

python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day 1 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day 1 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day 1 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day 1 0

python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day 0 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day 0 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day 0 0
python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day 0 0

