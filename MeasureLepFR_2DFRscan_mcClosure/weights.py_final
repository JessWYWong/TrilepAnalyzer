#!/usr/bin/python

# targetlumi = 36814. # 1/pb  https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/662.html   
targetlumi = 35867. # 1/pb  https://mail.google.com/mail/u/0/#label/eDRAWER%2FCERN-HyperNews/15a2f9a2bd29c798 https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html   

# Number of processed MC events (before selections)
nRun={}

# nRun['DY50'] = 1.95549e+07 # DYJetsToLL_M-50_TuneCUETHS1_13TeV-madgraphMLM-herwigpp - from WeightAnalyzer
# nRun['DY50'] = 8.17811e+07 # from 1.22055e+08 DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8  - from WeightAnalyzer
nRun['DY50'] = 1.45405e+08 # DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined  - from WeightAnalyzer
# 
# nRun['DY50'] = 96658943. # madgraph - ext2 - from DAS https://cmsweb.cern.ch/das/request?input=dataset%3D%2FDYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8%2FRunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1%2FMINIAODSIM&instance=prod%2Fglobal

# nRun['DYMG100'] = 10607207.
# nRun['DYMG200'] = 9653731.
# nRun['DYMG400'] = 10008776.
# nRun['DYMG600'] = 8292957.
# nRun['DYMG800'] = 2668730.
# nRun['DYMG1200']= 596079.
# nRun['DYMG2500']= 399492.

nRun['DY10to50'] = 29386500. # from 40381400. # calculated using WeightAnalyzer.
#nRun['DY50'] = 19403300. # from 28968300. # calculated using WeightAnalyzer. 
# nRun['DY50'] = 16912500. # from 25249500. # calculated using WeightAnalyzer few jobs failed!.

# nRun['TTJetsPH'] = 155119000. # calculated using WeightAnalyzer.

nRun['TTJetsPH'] = 155235652. # Sinans number https://github.com/sisagir/singleLepAnalyzer/blob/x53x53_2016/weights.py#L46-L50
nRun['TTJetsPH0to700inc'] = nRun['TTJetsPH']
nRun['TTJetsPH700to1000inc'] = nRun['TTJetsPH']*0.0921 + 38578334. # Sinans number https://github.com/sisagir/singleLepAnalyzer/blob/x53x53_2016/weights.py#L46-L50
nRun['TTJetsPH1000toINFinc'] = nRun['TTJetsPH']*0.02474 + 24561633.# Sinans number https://github.com/sisagir/singleLepAnalyzer/blob/x53x53_2016/weights.py#L46-L50
nRun['TTJetsPH700mtt'] = nRun['TTJetsPH700to1000inc']
nRun['TTJetsPH1000mtt'] = nRun['TTJetsPH1000toINFinc']

# Cross sections for MC samples (in pb)
xsec={}
xsec['DY10to50'] = 18610 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
# xsec['DY50'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DY50'] = 5765.4 #1921.8*3 +-0.6*3 (integration err) +- 33.2*3 pb (pdf+alpha_s err) : https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z 
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns

# Sinans number https://github.com/sisagir/singleLepAnalyzer/blob/x53x53_2016/weights.py#L300-L303
xsec['TTJetsPH0to700inc'] = 831.76
xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsPH700mtt'] = xsec['TTJetsPH700to1000inc']
xsec['TTJetsPH1000mtt'] = xsec['TTJetsPH1000toINFinc']

# Calculate lumi normalization weights
weight = {}
for sample in sorted(nRun.keys()): 
	weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])
	print sample, (xsec[sample]) / (nRun[sample])
