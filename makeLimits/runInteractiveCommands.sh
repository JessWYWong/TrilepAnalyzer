#!/bin/bash

###########

# todayDec-4-2018

day=2018_12_4

#

python doThetaLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
thetaTemplates_rootfiles \
thetaTemplates_rootfiles

# python PlotLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles



