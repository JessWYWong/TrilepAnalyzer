#!/bin/bash

# python doCondorThetaTemplates.py #Check output dir in doCondorThetaTemplates_new.py inputs in doHists.py_final and analyze.py_final before running!!


#############################
# 
day=2018_12_12  

python doThetaTemplates.py /user_data/rsyarif/LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1_FRv3hadds_step2_templates_$day/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20/ /thetaTemplates_rootfiles

#############################
# 
# day=2018_12_4  #2018data 1st try
# 
# python doThetaTemplates.py /user_data/rsyarif/LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds_step2_templates_$day/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20/ /thetaTemplates_rootfiles


