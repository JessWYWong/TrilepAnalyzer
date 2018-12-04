#!/bin/bash

# python doCondorThetaTemplates_new.py #Check output dir in doCondorThetaTemplates_new.py inputs in doHists.py_final and analyze.py_final before running!!


#############################
# 
day=2018_12_4  #2017data 1st try

python doThetaTemplates.py /user_data/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds_step2_templates_$day/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20/ /thetaTemplates_rootfiles


