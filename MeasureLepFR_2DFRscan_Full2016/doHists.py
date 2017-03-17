#!/usr/bin/python

import os,sys,time,math,datetime,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
from cutList import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_2016_12_15_rizki_withNonIsoTrig_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_PRv3_FRv11_ClintsAN16-242_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv9_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv12_muMinIso0p1_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv14a_muMinIso0p1_20Jan2017_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv15_20Jan2017_updatedbtagWP_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv5test_FRv15b_26Jan2017_lepPt30_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv17b_2Feb2017_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv7test_FRv18bSys_7Feb2017_step1hadds_step2/nominal'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv8test_FRv18bSys_7Feb2017_step1hadds_step2/nominal'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_scaleFRforCR1_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_2Mar2017_scaleFRforCR1_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_3Mar2017_scaleFR_CR2CR1_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_3Mar2017_scaleFR_CR2SR_step1hadds_step2/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRv6_FRv22_newMuTrkSF_step1hadds_step2/nominal/'
step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRv9_FRv24_postPreapproval_step1hadds_step2/nominal/'

print 'grabbing files from ', step1Dir
"""
Note: 
--Each process in step1 (or step2) directories should have the root files hadded! 
--The code will look for <step1Dir>/<process>_hadd.root for nominal trees.
The uncertainty shape shifted files will be taken from <step1Dir>/../<shape>/<process>_hadd.root,
where <shape> is for example "JECUp". hadder.py can be used to prepare input files this way! 
--Each process given in the lists below must have a definition in "samples.py"
--Check the set of cuts in "analyze.py"
"""
###########################################################
#################### CUTS & OUTPUT ########################
###########################################################

#obtain cutList and cutString from cutList.py

if len(sys.argv)>3: catList=[str(sys.argv[3])]
else: catList=['EEE','EEM','EMM','MMM','All']

scaleSignalXsecTo1pb = False # this has to be "True" if you are making templates for limit calculation!!!!!!!!
doAllSys= False

# cutString = 'isPassTrig'+str(int(cutList['isPassTrig']))+'_'+'isPassTrig_dilep'+str(int(cutList['isPassTrig_dilep']))+'_'+'isPassTrig_dilepHT'+str(int(cutList['isPassTrig_dilepHT']))+'_'+'isPassTrig_trilep'+str(int(cutList['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList['isPassTrilepton']))+'_'+'lep'+str(int(cutList['lepPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))
# cutString = 'lep'+str(int(cutList['lepPtCut']))+'_MET'+str(int(cutList['metCut']))+'_leadJet'+str(int(cutList['leadJetPtCut']))+'_subLeadJet'+str(int(cutList['subLeadJetPtCut']))+'_thirdJet'+str(int(cutList['thirdJetPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_ClintsAN16-242'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_muMinIso0p1_Full2016_IsoTrig_HLTupdate'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_muMinIso0p1_Full2016_IsoTrig_HLTupdate_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_LepPt'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_LepPt_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta1p2'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta1p2to2p1'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta2p1to2p4'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv7test_1bjet'
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv8test_1bjet'

pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_PRv6_1bjet_TESTTTTING'
pfix=''

pfix+='_'+datestr

#pfix+=datestr+'_'+timestr

###########################################################
#################### HISTOGRAM DEFS #######################
###########################################################

bigbins = [0,50,100,150,200,250,300,350,400,450,500,600,700,800,1000,1200,1500]
# HTbins = [0,100,200,300,400,500,600,800,1000,1200,1400,1600,2000]
HTbins = [0,100,200,300,400,500,600,800,1000,2000]
# STbins = [0,100,200,300,400,500,600,800,1000,1200,1400,1600,2000]
STbins = [0,100,200,300,400,500,600,800,1000,1400,2000]
# METbins = [0,20,40,60,80,100,120,140,160,180,220,260,300,400,500]
METbins = [0,20,40,60,80,100,120,140,160,180,220,300,500]
# pTbins = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
# pTbins = [0,10,25,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
pTbins = [0,10,30,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
Mbins = [-10.0, 0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 300.0]
# jetPtbins =  [0.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
jetPtbins =  [0.0, 30, 60.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
etaBins= [-4.0,-3.0,-2.4,-2.1,-1.2,0,1.2,2.1,2.4,3.0,4.0]

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
	'NPV'   :('nPV_singleLepCalc',linspace(0, 30, 31).tolist(),';PV multiplicity;'),

# 	'lepPt' :('AllLeptonPt_PtOrdered',linspace(0, 500, 26).tolist(),';Leptons p_{T} (GeV);'),
# 	'ElPt' :('AllLeptonElPt_PtOrdered',linspace(0, 500, 26).tolist(),';Electron p_{T} (GeV);'),
# 	'MuPt' :('AllLeptonMuPt_PtOrdered',linspace(0, 500, 26).tolist(),';Muon p_{T} (GeV);'),

	'lepPt' :('AllLeptonPt_PtOrdered',pTbins,';Leptons p_{T} (GeV);'),
	'ElPt' :('AllLeptonElPt_PtOrdered',pTbins,';Electron p_{T} (GeV);'),
	'MuPt' :('AllLeptonMuPt_PtOrdered',pTbins,';Muon p_{T} (GeV);'),

	'lep1Pt' :('AllLeptonPt_PtOrdered[0]',linspace(0, 500, 26).tolist(),';Lepton 1 p_{T} (GeV);'),
	'lep2Pt' :('AllLeptonPt_PtOrdered[1]',linspace(0, 300, 16).tolist(),';Lepton 2 p_{T} (GeV);'),
	'lep3Pt' :('AllLeptonPt_PtOrdered[2]',linspace(0, 300, 16).tolist(),';Lepton 3 p_{T} (GeV);'),

# 	'lepEta':('AllLeptonEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Lepton 1 #eta;'),
# 	'ElEta':('AllLeptonElEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Electron 1 #eta;'),
# 	'MuEta':('AllLeptonMuEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Mu 1 #eta;'),

	'lepEta':('AllLeptonEta_PtOrdered',etaBins,';Lepton 1 #eta;'),
	'ElEta':('AllLeptonElEta_PtOrdered',etaBins,';Electron 1 #eta;'),
	'MuEta':('AllLeptonMuEta_PtOrdered',etaBins,';Mu 1 #eta;'),

	'lep1Eta':('AllLeptonEta_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';Lepton 1 #eta;'),
	'lep2Eta':('AllLeptonEta_PtOrdered[1]',linspace(-4, 4, 41).tolist(),';Lepton 2 #eta;'),
	'lep3Eta':('AllLeptonEta_PtOrdered[2]',linspace(-4, 4, 41).tolist(),';Lepton 3 #eta;'),

	'JetEta':('theJetEta_JetSubCalc_PtOrdered',linspace(-4, 4, 41).tolist(),';AK4 Jet #eta;'),
	'Jet1Eta':('theJetEta_JetSubCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';1^{st} AK4 Jet #eta;'),
	'Jet2Eta':('theJetEta_JetSubCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';2^{nd} AK4 Jet #eta;'),

# 	'JetPt' :('theJetPt_JetSubCalc_PtOrdered',linspace(0, 750, 16).tolist(),';AK4 Jet p_{T} (GeV);'),
# 	'Jet1Pt':('theJetPt_JetSubCalc_PtOrdered[0]',linspace(0, 750, 16).tolist(),';1^{st} AK4 Jet p_{T} (GeV);'),
# 	'Jet2Pt':('theJetPt_JetSubCalc_PtOrdered[1]',linspace(0, 750, 16).tolist(),';2^{nd} AK4 Jet p_{T} (GeV);'),

	'JetPt' :('theJetPt_JetSubCalc_PtOrdered',jetPtbins,';AK4 Jet p_{T} (GeV);'),
	'Jet1Pt':('theJetPt_JetSubCalc_PtOrdered[0]',jetPtbins,';1^{st} AK4 Jet p_{T} (GeV);'),
	'Jet2Pt':('theJetPt_JetSubCalc_PtOrdered[1]',jetPtbins,';2^{nd} AK4 Jet p_{T} (GeV);'),


	'HT'    :('AK4HT',linspace(0, 2000, 21).tolist(),';H_{T} (GeV);'),
	'HTrebinned'    :('AK4HT',HTbins,';H_{T} (GeV);'),
	'ST'    :('AK4HTpMETpLepPt',linspace(0, 2000, 21).tolist(),';S_{T} (GeV);'),
	'STrebinned'    :('AK4HTpMETpLepPt',STbins,';S_{T} (GeV);'),
	'MET'   :('corr_met_singleLepCalc',linspace(0, 500, 26).tolist(),';#slash{E}_{T} (GeV);'),
	'METrebinned'   :('corr_met_singleLepCalc',METbins,';#slash{E}_{T} (GeV);'),

	'NJets' :('NJets_JetSubCalc',linspace(0, 15, 16).tolist(),';AK4 Jet multiplicity;'),
	'NBJets':('NJetsCSVwithSF_JetSubCalc',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),
	'NBJetsCorr':('NJetsCSVwithSF_JetSubCalc_noLepCorr',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),

	'mindeltaRlepJets':('minDR_lepJet',linspace(0, 1, 26).tolist(),';min #DeltaR(leps, jets);'),
	'mindeltaRlep1Jets':('minDR_lep1Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_1, jets);'),
	'mindeltaRlep2Jets':('minDR_lep2Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_2, jets);'),
	'mindeltaRlep3Jets':('minDR_lep3Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_3, jets);'),

# 	'mindeltaRB':('deltaR_lepBJets',linspace(0, 5, 51).tolist(),';min #DeltaR(l, bjet);'),
# 	'mindeltaR1':('deltaR_lepClosestJet[0]',linspace(0, 5, 51).tolist(),';min #DeltaR(l1, jet);'),
# 	'mindeltaR2':('deltaR_lepClosestJet[1]',linspace(0, 5, 51).tolist(),';min #DeltaR(l2, jet);'),
# 	'mindeltaR3':('deltaR_lepClosestJet[2]',linspace(0, 5, 51).tolist(),';min #DeltaR(l3, jet);'),

# 	'deltaRjet1':('deltaR_lepJets[0]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 1^{st} jet);'),
# 	'deltaRjet2':('deltaR_lepJets[1]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 2^{nd} jet);'),
# 	'deltaRjet3':('deltaR_lepJets[2]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 3^{rd} jet);'),

	'lepCharge':('AllLeptonCharge_PtOrdered',linspace(-2,2,5).tolist(),';lepton charge'),

	'lepIso':('AllLeptonMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),';lepton mini isolation'),
	'ElIso':('AllLeptonElMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),';Electron mini isolation'),
	'MuIso':('AllLeptonMuMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),'; Muon mini isolation'),

	'BjetPt':('theJetBTag_JetSubCalc_PtOrdered',linspace(0,1500,51).tolist(),';b jet p_{T} [GeV]'),  ## B TAG
	'Bjet1Pt':('theJetBTag_JetSubCalc_PtOrdered[0]',linspace(0,1500,51).tolist(),';1^{st} b jet p_{T} [GeV]'),  ## B TAG
	'Bjet1Pt':('theJetBTag_JetSubCalc_PtOrdered[1]',linspace(0,1500,51).tolist(),';2^{nd} b jet p_{T} [GeV]'),  ## B TAG

	'PtRel1':('PtRelLepClosestJet[0]',linspace(0,500,51).tolist(),';p_{T,rel}(l1, closest jet) [GeV]'),
	'PtRel2':('PtRelLepClosestJet[1]',linspace(0,500,51).tolist(),';p_{T,rel}(l2, closest jet) [GeV]'),
	'PtRel3':('PtRelLepClosestJet[2]',linspace(0,500,51).tolist(),';p_{T,rel}(l3, closest jet) [GeV]'),
	
# 	'MllsameFlavorOS':('Mll_sameFlavorOS',linspace(-10,300,32).tolist(),'; M(ll_{OS}) [GeV]'),
# 	'MllOSall':('MllOS_allComb',linspace(-10,300,32).tolist(),'; M(ll_{OS}) all [GeV]'),
# 	'MllOSallmin':('MllOS_allComb_min',linspace(-10,300,32).tolist(),'; min ( M(ll_{OS}) ) [GeV]'),
# 	'Mlll':('Mlll',linspace(-10,300,32).tolist(),'; M(lll) [GeV]'),

	'MllsameFlavorOS':('Mll_sameFlavorOS',Mbins,'; M(ll_{OS}) [GeV]'),
	'MllOSall':('MllOS_allComb',Mbins,'; M(ll_{OS}) all [GeV]'),
	'MllOSallmin':('MllOS_allComb_min',Mbins,'; min ( M(ll_{OS}) ) [GeV]'),
	'Mlll':('Mlll',Mbins,'; M(lll) [GeV]'),
	
	}

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

bkgList = [
# 	'DY50',
# 	'WJetsMG100',
# 	'WJetsMG200',
# 	'WJetsMG400',
# 	'WJetsMG600',
# 	'WJetsMG800',
# 	'WJetsMG1200',
# 	'WJetsMG2500',
# 	'WW',
	'WZ','ZZ',

	'WWW','WWZ','WZZ','ZZZ',
# 	'TTJets',
# 	'TTJetsPH',
# 	'TTJetsPH0to700inc',
# 	'TTJetsPH700to1000inc',
# 	'TTJetsPH1000toINFinc',
# 	'TTJetsPH700mtt',
# 	'TTJetsPH1000mtt',
# 	'TTWl','TTWq',
	'TTWl',
# 	'TTZl','TTZq',
	'TTZl',
# 	'Tt','Ts',
# 	'TtW','TbtW',
# 	'QCDht100','QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
	]

#adding scans of ddbkg
# loop,run,dilep --> set in samples
for muFRindex in xrange(loop):
	for elFRindex in xrange(loop):
		for i in xrange(len(run)):
			for j in xrange(len(dilep)):
				bkgList.append('DataDrivenBkg'+dilep[j]+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex))

whichSignal = 'TT' #TT, BB, or T53T53
signalMassRange = [800,1800]
sigList = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='T53T53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='T53T53': decays = [''] #decays to tWtW 100% of the time

#run,dilep,ddbkgCat --> set in samples
dataList = []
for run_ in run:
	for dilep_ in dilep:
		dataList.append('Data'+dilep_+run_)
		bkgList.append('DataDrivenBkg'+dilep_+run_)
		for ddbkgCat_ in ddbkgCat:
			bkgList.append('DataDrivenBkg'+ddbkgCat_+dilep_+run_)

###########################################################
#################### NORMALIZATIONS #######################
###########################################################

def negBinCorrection(hist): #set negative bin contents to zero and adjust the normalization
	norm0=hist.Integral()
	for iBin in range(0,hist.GetNbinsX()+2):
		if hist.GetBinContent(iBin)<0: hist.SetBinContent(iBin,0)
		if hist.Integral()!=0 and norm0>0: hist.Scale(norm0/hist.Integral())
		
def overflow(hist):
	nBinsX=hist.GetXaxis().GetNbins()
	content=hist.GetBinContent(nBinsX)+hist.GetBinContent(nBinsX+1)
	error=math.sqrt(hist.GetBinError(nBinsX)**2+hist.GetBinError(nBinsX+1)**2)
	hist.SetBinContent(nBinsX,content)
	hist.SetBinError(nBinsX,error)
	hist.SetBinContent(nBinsX+1,0)
	hist.SetBinError(nBinsX+1,0)

###########################################################
################### READ INPUT FILES ######################
###########################################################

def readTree(file):
	if not os.path.exists(file): 
		print "Error: File does not exist! Aborting ...",file
		os._exit(1)
	tFile = R.TFile(file,'READ')
	tTree = tFile.Get('ljmet')
	return tFile, tTree 

print "READING TREES"
# shapesFiles = ['jec','jer']
shapesFiles = []
tTreeData = {}
tFileData = {}
for data in dataList:
	#print "READING:", data
	tFileData[data],tTreeData[data]=readTree(step1Dir+'/'+samples[data]+'_hadd.root')

tTreeSig = {}
tFileSig = {}
for sig in sigList:
	for decay in decays:
		#print "READING:", sig+decay
		#print "        nominal"
		tFileSig[sig+decay],tTreeSig[sig+decay]=readTree(step1Dir+'/'+samples[sig+decay]+'_hadd.root')
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					print "        "+syst+ud
					tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[sig+decay]+'_hadd.root')

tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList:
	#print "READING:",bkg
	#print "        nominal"
	if 'DataDriven' in bkg: continue #all the ddbkg uses the same files as data.
	tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root')
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if 'DataDriven' in bkg: continue
				else:
					print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[bkg]+'_hadd.root')
print "FINISHED READING"

###########################################################
#################### RUN ANALYSE.PY #######################
###########################################################

if len(sys.argv)>2: iPlot=sys.argv[2]
# else: iPlot='minMlb'
else: iPlot='STrebinned'
# else: iPlot='lepPt'
# else: iPlot='Mlll'
# else: iPlot='lepIso'
# else: iPlot='JetPt'
print "PLOTTING:",iPlot
print "         LJMET Variable:",plotList[iPlot][0]
print "         X-AXIS TITLE  :",plotList[iPlot][2]
print "         BINNING USED  :",plotList[iPlot][1]

nCats  = len(catList)
catInd = 1
for category in catList:
	print category
	datahists = {}
	bkghists  = {}
	sighists  = {}
	if len(sys.argv)>1: outDir=sys.argv[1]
	else: 
		outDir = '/user_data/rsyarif/'
# 		outDir = os.getcwd()+'/'
		outDir+=pfix
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
		outDir+='/'+cutString
		if not os.path.exists(outDir+'/'+category): os.system('mkdir '+outDir+'/'+category)
		outDir+='/'+category
	for data in dataList: 
		datahists.update(analyze(tTreeData,data,cutList,False,iPlot,plotList[iPlot],category))
		if catInd==nCats: del tFileData[data]
	for bkg in bkgList: 
		#print '+++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>  bkg = ' , bkg 
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root') #open file here because there too many files to open
		bkghists.update(analyze(tTreeBkg,bkg,cutList,doAllSys,iPlot,plotList[iPlot],category))
		del tFileBkg[bkg] #close file everytime because there too many files to open.
		#if catInd==nCats: del tFileBkg[bkg]
		if doAllSys and catInd==nCats:
			for syst in shapesFiles:
				if 'DataDriven' in bkg: continue
				for ud in ['Up','Down']: del tFileBkg[bkg+syst+ud]
	for sig in sigList: 
		for decay in decays: 
			sighists.update(analyze(tTreeSig,sig+decay,cutList,doAllSys,iPlot,plotList[iPlot],category))
			if catInd==nCats: del tFileSig[sig+decay]
			if doAllSys and catInd==nCats:
				for syst in shapesFiles:
					for ud in ['Up','Down']: del tFileSig[sig+decay+syst+ud]

	#Negative Bin Correction
	for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])

	#OverFlow Correction
	for data in datahists.keys(): overflow(datahists[data])
	for bkg in bkghists.keys():   overflow(bkghists[bkg])
	for sig in sighists.keys():   overflow(sighists[sig])

	pickle.dump(datahists,open(outDir+'/datahists_'+iPlot+'.p','wb'))
	pickle.dump(bkghists,open(outDir+'/bkghists_'+iPlot+'.p','wb'))
	pickle.dump(sighists,open(outDir+'/sighists_'+iPlot+'.p','wb'))
	catInd+=1

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
