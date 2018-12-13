#!/bin/bash

###########

# todayDec-12-2018

day=2018_12_12

# python doThetaLimits_combine2017and2018.py \
# LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds_step2_templates_$day  \
# LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1_FRv3hadds_step2_templates_$day \
# lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles

python PlotLimits_2017and2018.py Combined2017and2018_$day \
lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
thetaTemplates_rootfiles


# python doThetaLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1_FRv3hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles \
# thetaTemplates_rootfiles

# python PlotLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1_FRv3hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles


###########

# todayDec-4-2018

# day=2018_12_4

#

# python doThetaLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles \
# thetaTemplates_rootfiles

# python PlotLimits.py LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds_step2_templates_$day lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20 \
# thetaTemplates_rootfiles



