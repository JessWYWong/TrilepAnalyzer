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

# day=2017_3_15
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_noDDBKG_CR2_$day 0 0

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with newRunH

# day=2017_3_25
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_noDDBKG_CR2_$day 0 0

#######################################################################################################

# day=2017_3_26
# source switchToFinal.sh  
##doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST700_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST700noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST800_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST800noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST900_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST900noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1000_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1000noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1100_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1100noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1200_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1200noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1300_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1300noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1400_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1400noWeight_$day 2

#plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST900_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1000_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1100_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1200_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1300_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1400_$day 1 0

# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST700_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST800_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST900_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1000_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1100_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1200_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1300_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_fSRST1400_$day 1 1

# day=2017_3_27
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 2
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_SR_$day 1 0

######################################################################################################

# day=2017_3_26
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR1_$day 0
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 0
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 0 0
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_AllSYS_FRCR2_$day 0 1

################################Check doKinematics AllSYS or noSYS!####################################

# day=2017_3_27
# day=2017_3_28
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3
#  
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3

# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0

#######################################################################################################

# day=2017_3_28
# source switchToFinal.sh  
#doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST700_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST700noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST800_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST800noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST900_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST900noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1000_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1000noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1100_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1100noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1200_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1200noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1300_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1300noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1400_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1400noWeight_$day 2

# plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST900_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1000_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1100_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1200_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1300_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1400_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST700_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST800_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST900_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1000_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1100_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1200_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1300_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_fSRST1400_$day 1 1

######################################################################################################

# day=2017_3_28
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR1_$day 0
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 0
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 0 0
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_FRsysMar28_AllSYS_FRCR2_$day 0 1

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with newRunH _correctedMuTrkSF

# day=2017_4_4
# source switchToNoDDBKGfinal.sh  
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_ALLR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SR_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR1_$day
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR2_$day
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_ALLR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SR_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR1_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR2_$day 1 0
# 
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_ALLR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SR_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR1_$day 0 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR2_$day 0 0

#######################################################################################################

# day=2017_4_5
# source switchToFinal.sh  
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1100_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1200_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1300_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1400_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1500_$day 2
# 
# day=2017_4_6
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1600_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1100noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1200noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1300noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1400noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1500noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1600noWeight_$day 2
# 
# 
# day=2017_4_5
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1100_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1200_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1300_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1400_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1500_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1100_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1200_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1300_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1400_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1500_$day 1 1
# 
# day=2017_4_6
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1600_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1600_$day 1 0

# day=2017_5_5
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRnoWeight_$day 2


#####################################################################################################

# day=2017_4_6
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 1
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# 
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1

################################Check doKinematics AllSYS or noSYS!####################################

# day=2017_?_?
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 3
# 
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 3

# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 3

# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 3
#  
# python doKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3
# python doKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3
# python doKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 3

# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_SR_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSR_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST700_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST800_$day 1 0

# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1000_$day 1 0

# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_fSRST1400_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRvEltest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRvMutest_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0
# python plotKinematics.py kinematics_FRvMuEtatest_PRv9_step2_LJMet21Mar2017_newRunH_noSYS_CR2_$day 1 0

#######################################################################################################

# day=2017_4_12
# source switchToFinal.sh  
#####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900noWeight_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 2
# python doKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000noWeight_$day 2

####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSR_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST700_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST800_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST900_$day 1 1
# python plotKinematics.py kinematics_FRv30CR2extSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 1 1
# 

#######################################################################################################
#Replacing earlier plots with FRsys Mar28 NoSTcut

# day=2017_4_5 
# source switchToFinal.sh  
# #####doKinematics.py <folder> <whichPlots?>
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 2
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 2
# 
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 4
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 4
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 4
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 5

####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0
# 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1

# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

# # 
# day=2017_4_6
# source switchToFinal.sh  
# # python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 1
# # python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# # 
# # python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# # 
# # python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 1
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# # 
#######################################################################################################

# day=2017_5_17
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv31CR1_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_5_18
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv33_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1
# python plotKinematics.py kinematics_FRv33_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv33_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_5_19
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv34_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1
# python plotKinematics.py kinematics_FRv34_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv34_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_5_25
# source switchToFinal.sh  
#####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_BB_SR_$day 2
####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_BB_SR_$day 1 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_BB_SR_$day 1 0

#######################################################################################################

# day=2017_6_6
# source switchToFinal.sh  
# python doKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1 #Typo should be FRv35bPtDep
# python doKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 1 #Typo should be FRv35bPtDep
# python doKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 #Typo should be FRv35bPtDep
# 
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0 #Typo should be FRv35bPtDep
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1 #Typo should be FRv35bPtDep
# 
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0 #Typo should be FRv35bPtDep
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1 #Typo should be FRv35bPtDep
# 
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0 #Typo should be FRv35bPtDep
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1 #Typo should be FRv35bPtDep

# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0 #Typo should be FRv35bPtDep
# python plotKinematics.py kinematics_FRv35PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1 #Typo should be FRv35bPtDep

# python doKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 1
# python doKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1
# 
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# 
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# 
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1

# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv39PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

# python doKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1
# python doKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 1
# python doKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1
# 
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# 
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# 
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 0
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 1 1

# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv40PtDep_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_6_20
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2ST1000low_$day 2
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2ST1000low_$day 1
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2ST1000low_$day 0 0 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2ST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 1
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2ST1000low_$day 0 1 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2ST1000low_$day 0 1

#######################################################################################################

# day=2017_6_22
# source switchToFinal.sh  

#####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 2
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 2
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 2
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 2
# python doKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 1

####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 0 0
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0 
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0

# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 0 1
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 1
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 0 1
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1 
# python plotKinematics.py kinematics_FRv41SRST1000low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1

#######################################################################################################

# day=2017_6_22
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 2
# python doKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 1
# python doKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 2
# python doKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 2
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 0
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 0 0
# 
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRST1000low_$day 0 1
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRST1000low_$day 0 1
# python plotKinematics.py kinematics_FRv41lessSys_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_fSRST1000_$day 0 1

#######################################################################################################

# day=2017_7_19
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0
# # python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1
# 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR2_$day 0 1
# 
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRCR1_$day 0 1

#######################################################################################################

# day=2017_7_19
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_elEta2p1_AllSYS_SR_$day 0
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_elEta2p1_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_elEta2p1_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_7_19
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 0
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 0 0
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 4
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 0 0
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 0 1

#######################################################################################################

# day=2017_7_20
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_7_21
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 7
# 
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_7_21
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 8
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 0 0
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 0 1

#####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 8
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 0 0
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 8
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 1

#######################################################################################################

# day=2017_7_24
# source switchToFinal.sh  
# 
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv43FRSRHT600low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 1

#######################################################################################################

# day=2017_7_24
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 10
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 10
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_minDRlepJet0p2_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_minDRlepJet0p2_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_minDRlepJet0p2_$day 0 1
# 
#######################################################################################################

# day=2017_7_24
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_minDRlepJet0p2_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_minDRlepJet0p2_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_minDRlepJet0p2_$day 0 1

#######################################################################################################

# day=2017_7_25
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 1

#######################################################################################################
# 
# day=2017_7_25
# source switchToFinal.sh  
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# # python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 9
# # ####plotKinematics.py <folder> <blind?> <log?>
# # python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 0 0
# # python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 9
# ###plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 0 1
# 
# # ####doKinematics.py <folder> <whichPlots?>
# # python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2Dlep1Jet_$day 11
# # ###plotKinematics.py <folder> <blind?> <log?>
# # python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2Dlep1Jet_$day 0 0
# # python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2Dlep1Jet_$day 0 1
# # 
# # ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 9
# ###plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 1
# 
# # ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 9
# ###plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600_$day 0 1
# 
# # ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 9
# ###plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT600low_$day 0 1
# 
#######################################################################################################

# day=2017_7_25
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2Dlep1Jet_$day 0 1
# 
# # ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 9
# ###plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv30CR2_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SR_2DlepJet_$day 0 1

#######################################################################################################

# day=2017_7_26 #SanityCheck
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 11
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 11
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 1

#######################################################################################################
# 
# day=2017_7_26 #SanityCheck
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 8
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 0 0
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_FRSRmlllb400low_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 8
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 0 0
# python plotKinematics.py kinematics_FRv44FRSRmlllb400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixlepOrder_AllSYS_SRmlllb400_$day 0 1

#######################################################################################################

# day=2017_7_27
# source switchToFinal.sh  
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 9
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 9
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv46FRSRHT400low2D_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 1
# 
#######################################################################################################
# 
# day=2017_7_28
# source switchToFinal.sh  
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 12
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 12
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_2DlepJet_$day 12
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1_2DlepJet_$day 12
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2HT400low_2DlepJet_$day 12
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2HT400low_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR2HT400low_2DlepJet_$day 0 1
# 
# ####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1HT400low_2DlepJet_$day 12
# #####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1HT400low_2DlepJet_$day 0 0
# python plotKinematics.py kinematics_FRv47FRSRHT400low2Dext_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_CR1HT400low_2DlepJet_$day 0 1
# 
#######################################################################################################
# _addMlllBUnc
# 
# day=2017_8_10
# source switchToFinal.sh  
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 0 1
# 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 1
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 1


#######################################################################################################
# reproduce

# day=2017_8_11
# source switchToFinal.sh  
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_FRSRHT400low_$day 0 1
# 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400_$day 0 1
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_AllSYS_SRHT400low_$day 0 1

#######################################################################################################

# day=2017_8_14
# source switchToFinal.sh  
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_FRSRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_FRSRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_FRSRHT400low_$day 0 1
# 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400_$day 0 1
# # 
# # #####doKinematics.py <folder> <whichPlots?>
# python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400low_$day 1
# ####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_AllSYS_SRHT400low_$day 0 1

#######################################################################################################

# day=2017_8_17
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
#python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_FRSRHT400low_$day 1
####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_FRSRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_FRSRHT400low_$day 0 1

# #####doKinematics.py <folder> <whichPlots?>
#python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400_$day 1
####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
#python doKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400low_$day 1
####plotKinematics.py <folder> <blind?> <log?>
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400low_$day 0 0
# python plotKinematics.py kinematics_FRv45FRSRHT400low_PRv9_step2_LJMet21Mar2017_newRunH_correctedMuTrkSF_FRsysMar28_fixedMinMlllBshifts_extraFRsys17Aug_AllSYS_SRHT400low_$day 0 1

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with newRunH _correctedMuTrkSF
# day=2017_9_11
# source switchToNoDDBKGfinal.sh  
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400_$day
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400_$day 0 0
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400low_$day
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400low_$day 1 0
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400low_$day 0 0

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with newRunH _correctedMuTrkSF - plotting AK4JetFlavor
# day=2017_9_11
# source switchToNoDDBKGfinal.sh  
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR2_$day 1
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_CR2_$day 1 0
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SR_$day 1
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SR_$day 1 0
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400low_$day 1
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400low_$day 1 0
# 
# python doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400_$day 1
# python plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_correctedMuTrkSF_noDDBKG_SRHT400_$day 1 0

#######################################################################################################

# day=2017_9_17
# source switchToFinal.sh
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 0 1

#######################################################################################################

# day=2017_9_17
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 1

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with elMVAvalueAlt - plotting AK4JetFlavor
# day=2017_9_17
# source switchToNoDDBKGfinal.sh  
# 
# # python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR2_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR2_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR2_$day 0 0
# 
# # python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SR_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SR_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SR_$day 0 0
# 
# # python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400low_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400low_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400low_$day 0 0
# 
# # python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_SRHT400_$day 0 0

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with elMVAvalueAlt - plotting AK4JetFlavor

# day=2017_9_18
# source switchToNoDDBKGfinal.sh  
# 
# python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_ALLR_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_ALLR_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_ALLR_$day 0 0

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##using binned DY samples with elMVAvalueAlt - plotting AK4JetFlavor

# day=2017_9_20
# source switchToNoDDBKGfinal.sh  
# 
# python -u doKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR1_$day 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR1_$day 1 0
# python -u plotKinematics.py kinematics_LJMet24Feb2017_binnedDY_newRunH_elMVAvalueAlt_noDDBKG_CR1_$day 0 0

#######################################################################################################
# 
# day=2017_9_20
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv48MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv48_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv49MuEtaTest_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9ElPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 8
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv49_PRv9MuPRtest_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_StatOnly_SRHT400_$day 0 1
# 
# #

#######################################################################################################

# day=2017_9_20
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv50_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 1

#######################################################################################################
# 
# day=2017_9_21
# source switchToFinal.sh
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 0 0
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRSRHT400low_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 0 0
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 0 0
# python -u plotKinematics.py kinematics_FRv48sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SRHT400low_$day 0 1
# 
# #######################################################################################################
# 
# day=2017_9_21
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 0
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 1
# 
#######################################################################################################
# 
# day=2017_9_25
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 1
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 1
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 0
# python -u plotKinematics.py kinematics_FRv50sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 1

#######################################################################################################
# 
# day=2017_10_3
# source switchToFinal.sh  
# 
# #####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_statSYS_SR_$day 0
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_statSYS_SR_$day 0 1

# #######################################################################################################
# Recreate using new plotter synced with Julie's code. 
day=2017_9_21
source switchToFinal.sh #plotKinematics.py_final_v2 
# 
# ##plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 0
python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_FRCR2_$day 0 1
# 
# ##plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 0
python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_SR_$day 0 1
# 
# ##plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 0
python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_elMVAvalueAlt_AllSYS_CR2_$day 0 1

#######################################################################################################
# 
# day=2017_11_29
# source switchToFinal.sh  

#####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_statSYS_SR_$day 0
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_statSYS_SR_$day 0 1

#####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_v2_statSYS_SR_$day 0
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_v2_statSYS_SR_$day 0 1

#####doKinematics.py <folder> <whichPlots?>
# python -u doKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_v3_statSYS_SR_$day 0
# ###plotKinematics.py <folder> <blind?> <log?>
# python -u plotKinematics.py kinematics_FRv49sys_PRv9_step2_LJMet21Mar2017_newRunH_addIP_v3_statSYS_SR_$day 0 1

####REMEMBER to CHECK step1Dir in doHists before submitting!#############################
##checking MCBKg Gamma samples
# 
# day=2017_12_1
# source switchToNoDDBKGfinal.sh  
# 
# python -u doKinematics.py kinematics_LJMet80x_extra_wGammas_noDDBKG_SR_$day 0

