#!/usr/bin/python

import os,sys,time,math,datetime,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

scaleSignalXsecTo1pb = False # this has to be "True" if you are making templates for limit calculation!!!!!!!!
doAllSys= True #False

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb


#step1Dir_mc = '/mnt/data/users/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds_step2/nominal' # uses PR v9 FR v49
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_hadds_step2' #PR v0 FR v0 
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_UnityMuPR_hadds_step2'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_UnityMuPR_hadds_step2'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_etaFRv5_hadds_step2'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv2_prefiring_hadds_step2'
step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv2_prefire_elIdSys_TrigEffWeight_pdf4LHC_hadds_step2'
step1Dir_data = step1Dir_mc
#step1Dir_data = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv2_prefiring_elPR_hadds_step2'
#step1Dir_data = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_hadds_step2' #step1Dir_mc
# step1Dir_data = '/user_data/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv1hadds_step2/nominal' # uses PR v9 FR v1 
# step1Dir_data = '/user_data/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv2hadds_step2/nominal' # uses PR v9 FR v2 
#step1Dir_data = '/mnt/data/users/wwong/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds_step2/nominal' # uses PR v9 FR v3 


print 'grabbing data files from ', step1Dir_data
print 'grabbing mc files from ', step1Dir_mc
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

cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lep1PtCut': 0, #40, #0, #
		   'leadJetPtCut':0, #150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 20,#60, #75, #0, #
		   'njetsCut': 3, #njet >= njetsCut
		   'nbjetsCut':1, #3, #
		   'drCut':0, #1.0, #
	   	   'stCut':600,
	   	   'mllOSCut':20,
                   'htCut':0,
		   }

print 'sys.argv', sys.argv

cutType='ALLR'
if len(sys.argv)>3: cutType=str(sys.argv[3])

if cutType=='ALLR':
	print 'Not applying any Njets criteria'
	cutList = {'isPassTrig': 0, 
			   'isPassTrig_dilep': 1,
			   'isPassTrig_dilep_anth': 0,
			   'isPassTrig_trilep': 0, 
			   'isPassTrilepton': 1,
			   'lep1PtCut': 0,
			   'leadJetPtCut':0,
			   'subLeadJetPtCut':0, 
			   'thirdJetPtCut':0, 
			   'metCut': 20,
			   'njetsCut': 0,
			   'nbjetsCut':1,
			   'drCut':0,
			   'stCut':0,
			   'mllOSCut':20,
			   'htCut':0,
			   }

if 'CR2' in cutType:
	print 'Applying exactly2jets criteria'
	cutList = {'isPassTrig': 0, 
			   'isPassTrig_dilep': 1,
			   'isPassTrig_dilep_anth': 0,
			   'isPassTrig_trilep': 0, 
			   'isPassTrilepton': 1,
			   'lep1PtCut': 0,
			   'leadJetPtCut':0,
			   'subLeadJetPtCut':0, 
			   'thirdJetPtCut':0, 
			   'metCut': 20,
			   'njetsCut': 2, #njet == njetsCut
			   'nbjetsCut':1,
			   'drCut':0,
			   'stCut':0,
			   'mllOSCut':20,
			   'htCut':0,
			   }


if 'CR1' in cutType:
	print 'Applying exactly1jet criteria'
	cutList = {'isPassTrig': 0, 
			   'isPassTrig_dilep': 1,
			   'isPassTrig_dilep_anth': 0,
			   'isPassTrig_trilep': 0, 
			   'isPassTrilepton': 1,
			   'lep1PtCut': 0,
			   'leadJetPtCut':0,
			   'subLeadJetPtCut':0, 
			   'thirdJetPtCut':0, 
			   'metCut': 20,
			   'njetsCut': 1, #njet == njetsCut
			   'nbjetsCut':1,
			   'drCut':0,
			   'stCut':0,
			   'mllOSCut':20,
			   'htCut':0,
			   }


if 'CR1' in cutType and 'CR2' in cutType:
	print 'Applying 1 or 2 jets criteria'
	cutList = {'isPassTrig': 0, 
			   'isPassTrig_dilep': 1,
			   'isPassTrig_dilep_anth': 0,
			   'isPassTrig_trilep': 0, 
			   'isPassTrilepton': 1,
			   'lep1PtCut': 0,
			   'leadJetPtCut':0,
			   'subLeadJetPtCut':0, 
			   'thirdJetPtCut':0, 
			   'metCut': 20,
			   'njetsCut': 2, # --> 1 <= njet <= njetsCut
			   'nbjetsCut':1,
			   'drCut':0,
			   'stCut':0,
			   'mllOSCut':20,
			   }

if cutType=='SR':
	print 'Applying moreThan2jets criteria'
	cutList = {'isPassTrig': 0, 
			   'isPassTrig_dilep': 1,
			   'isPassTrig_dilep_anth': 0,
			   'isPassTrig_trilep': 0, 
			   'isPassTrilepton': 1,
			   'lep1PtCut': 0,
			   'leadJetPtCut':0,
			   'subLeadJetPtCut':0, 
			   'thirdJetPtCut':0, 
			   'metCut': 20,
			   'njetsCut': 3, #njet >= njetsCut
			   'nbjetsCut':1,
			   'drCut':0,
			   'stCut':0,
			   'mllOSCut':20,
			   'htCut':0,
			   }




if len(sys.argv)>4: catList=[str(sys.argv[4])]
else: catList=['EEE','EEM','EMM','MMM','All']

cutString = 'isPassTrig_All'+str(int(cutList['isPassTrig']))+'_'+'dilep'+str(int(cutList['isPassTrig_dilep']))+'_'+'dilepAnth'+str(int(cutList['isPassTrig_dilep_anth']))+'_'+'trilep'+str(int(cutList['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList['isPassTrilepton']))+'_'+cutType+'_lep1Pt'+str(int(cutList['lep1PtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))+'_MllOS'+str(int(cutList['mllOSCut']))

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

#pfix='kinematics_80x_dummy'
#pfix='kinematics_LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_NoSYS_2016SFs_FRv3'
#pfix='kinematics_FWLJMET102X_3lep2017_062019_wywong_step1_FRv1_hadds_step2'
pfix='kinematics_'+step1Dir_data.split('/')[-1]

#pfix+=datestr+'_'+timestr

###########################################################
#################### HISTOGRAM DEFS #######################
###########################################################

bigbins = [0,50,100,150,200,250,300,350,400,450,500,600,700,800,1000,1200,1500]
# HTbins = [0,100,200,300,400,500,600,800,1000,1200,1400,1600,2000]
HTbins = [0,100,200,300,400,500,600,800,1000,2000]
# STbins = [0,100,200,300,400,500,600,800,1000,1200,1400,1600,2000]
STbins = [0,100,200,300,400,500,600,800,1000,1400,2000]
STbinsv2 = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,2000]
STbinsv3 = [0,100,200,300,400,500,600,700,800,900,1000,1200,1400,1600,2000]
# METbins = [0,20,40,60,80,100,120,140,160,180,220,260,300,400,500]
METbins = [0,20,40,60,80,100,120,140,160,180,220,300,500]
# pTbins = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
# pTbins = [0,10,25,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
pTbins = [0,10,30,40,60,80,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500]
pTbinsV2 = [0,30,40,60,80,100,120,140,160,180,500]
Mbins = [-10.0, 0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 300.0]
MbinsV2 = [-10.0, 0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 300.0, 350.0, 400.00]
# jetPtbins =  [0.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
jetPtbins =  [0.0, 30, 60.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
Nlepbins=[0,1,2,3,4,5,6,7,8,9,10]
MlllBbins=[100,200,300,400,500,600,700,800,1000,1500]

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
# 	'ElDxy' :('AllLeptonElDxy_PtOrdered',linspace(-0.05, 0.05, 81).tolist(),';Electron IP_{xy} (cm);'),
# 	'ElDz' :('AllLeptonElDz_PtOrdered',linspace(-0.2, 0.2, 81).tolist(),';Electron IP_{z} (cm);'),
	'ElDxy' :('AllLeptonElDxy_PtOrdered',linspace(-0.1, 0.1, 21).tolist(),';Electron IP_{xy} (cm);'),
	'ElDz' :('AllLeptonElDz_PtOrdered',linspace(-0.2, 0.2, 21).tolist(),';Electron IP_{z} (cm);'),

	'MuDxy' :('AllLeptonMuDxy_PtOrdered',linspace(-0.1, 0.1, 21).tolist(),';Muon IP_{xy} (cm);'),
	'MuDz' :('AllLeptonMuDz_PtOrdered',linspace(-0.2, 0.2, 21).tolist(),';Muon IP_{z} (cm);'),

	'NPV'   :('nPV_MultiLepCalc',linspace(0, 30, 31).tolist(),';PV multiplicity;'),

# 	'lepPt' :('AllLeptonPt_PtOrdered',linspace(0, 500, 26).tolist(),';Leptons p_{T} (GeV);'),
# 	'ElPt' :('AllLeptonElPt_PtOrdered',linspace(0, 500, 26).tolist(),';Electron p_{T} (GeV);'),
# 	'MuPt' :('AllLeptonMuPt_PtOrdered',linspace(0, 500, 26).tolist(),';Muon p_{T} (GeV);'),

	'lepPt' :('AllLeptonPt_PtOrdered',pTbins,';Leptons p_{T} (GeV);'),
	'lepPtRebinned' :('AllLeptonPt_PtOrdered',pTbinsV2,';Leptons p_{T} (GeV);'),
	'ElPt' :('AllLeptonElPt_PtOrdered',pTbins,';Electron p_{T} (GeV);'),
	'MuPt' :('AllLeptonMuPt_PtOrdered',pTbins,';Muon p_{T} (GeV);'),

	'lep1Pt' :('AllLeptonPt_PtOrderedOnly_top3[0]',pTbins,';Lepton 1 p_{T} (GeV);'),
	'lep2Pt' :('AllLeptonPt_PtOrderedOnly_top3[1]',pTbins,';Lepton 2 p_{T} (GeV);'),
	'lep3Pt' :('AllLeptonPt_PtOrderedOnly_top3[2]',pTbins,';Lepton 3 p_{T} (GeV);'),

	'lepEta':('AllLeptonEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Lepton #eta;'),
	'ElEta':('AllLeptonElEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Electron #eta;'),
	'MuEta':('AllLeptonMuEta_PtOrdered',linspace(-4, 4, 41).tolist(),';Mu #eta;'),

	'lep1Eta':('AllLeptonEta_PtOrderedOnly_top3[0]',linspace(-4, 4, 41).tolist(),';Lepton 1 #eta;'),
	'lep2Eta':('AllLeptonEta_PtOrderedOnly_top3[1]',linspace(-4, 4, 41).tolist(),';Lepton 2 #eta;'),
	'lep3Eta':('AllLeptonEta_PtOrderedOnly_top3[2]',linspace(-4, 4, 41).tolist(),';Lepton 3 #eta;'),

	'Nlep':('AllLeptonCount_PtOrdered',Nlepbins,';Lepton Multiplicity;'),
	'Nel':('AllLeptonElCount_PtOrdered',Nlepbins,';electron Multiplicity;'),
	'Nmu':('AllLeptonMuCount_PtOrdered',Nlepbins,';#mu Multiplicity;'),

	'JetEta':('AK4JetEta_MultiLepCalc_PtOrdered',linspace(-4, 4, 41).tolist(),';AK4 Jet #eta;'),
# 	'Jet1Eta':('AK4JetEta_MultiLepCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';1^{st} AK4 Jet #eta;'),
# 	'Jet2Eta':('AK4JetEta_MultiLepCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';2^{nd} AK4 Jet #eta;'),

# 	'JetPt' :('AK4JetPt_MultiLepCalc_PtOrdered',linspace(0, 750, 16).tolist(),';AK4 Jet p_{T} (GeV);'),
# 	'Jet1Pt':('AK4JetPt_MultiLepCalc_PtOrdered[0]',linspace(0, 750, 16).tolist(),';1^{st} AK4 Jet p_{T} (GeV);'),
# 	'Jet2Pt':('AK4JetPt_MultiLepCalc_PtOrdered[1]',linspace(0, 750, 16).tolist(),';2^{nd} AK4 Jet p_{T} (GeV);'),

	'JetPt' :('AK4JetPt_MultiLepCalc_PtOrdered',jetPtbins,';AK4 Jet p_{T} (GeV);'),
# 	'Jet1Pt':('AK4JetPt_MultiLepCalc_PtOrdered[0]',jetPtbins,';1^{st} AK4 Jet p_{T} (GeV);'),
# 	'Jet2Pt':('AK4JetPt_MultiLepCalc_PtOrdered[1]',jetPtbins,';2^{nd} AK4 Jet p_{T} (GeV);'),


	'HT'    :('AK4HT',linspace(0, 4000, 41).tolist(),';H_{T} (GeV);'),
	'HTrebinned'    :('AK4HT',HTbins,';H_{T} (GeV);'),
	'ST'    :('AK4HTpMETpLepPt',linspace(0, 5000, 51).tolist(),';S_{T} (GeV);'),
	'STrebinned'    :('AK4HTpMETpLepPt',STbins,';S_{T} (GeV);'),
	'STrebinnedv2'    :('AK4HTpMETpLepPt',STbinsv2,';S_{T} (GeV);'),
# 	'STrebinnedv3'    :('AK4HTpMETpLepPt',STbinsv3,';S_{T} (GeV);'),
# 	'MET'   :('corr_met_MultiLepCalc',linspace(0, 500, 26).tolist(),';#slash{E}_{T} (GeV);'),
	'METrebinned'   :('corr_met_MultiLepCalc',METbins,';#slash{E}_{T} (GeV);'),

	'NJets' :('NJets_MultiLepCalc',linspace(0, 15, 16).tolist(),';AK4 Jet multiplicity;'),
	'NBJets':('NJetsBTagwithSF_MultiLepCalc',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),
# 	'NBJetsCorr':('NJetsBTagwithSF_MultiLepCalc_noLepCorr',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),

# 	'mindeltaRlepJets':('minDR_lepJet',linspace(0, 1, 26).tolist(),';min #DeltaR(leps, jets);'),
# 	'mindeltaRlep1Jets':('minDR_lep1Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_1, jets);'),
# 	'mindeltaRlep2Jets':('minDR_lep2Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_2, jets);'),
# 	'mindeltaRlep3Jets':('minDR_lep3Jet',linspace(0, 1, 26).tolist(),';min #DeltaR(lep_3, jets);'),

# 	'minMlB':('minMleppBjet',Mbins,';min[M(lep, b-jet)];'),
# 	'minMlBv2':('minMleppBjet',MbinsV2,';min[M(lep, b-jet)];'),
# 	'minMlllB':('minMlllBjet',linspace(0, 1500, 51).tolist(),';min[M(trilepton, b-jet)];'),
	'minMlllBv2':('minMlllBjet',linspace(0, 1500, 31).tolist(),';min[M(trilepton, b-jet)];'),
# 	'minMlllBv3':('minMlllBjet',linspace(0, 2000, 41).tolist(),';min[M(trilepton, b-jet)];'),
	'minMlllBv4':('minMlllBjet',MlllBbins,';min[M(trilepton, b-jet)];'),

	'minDPhiMETJet':('minDPhi_METJet',linspace(0, 3.15, 51).tolist(),';min #Delta#Phi(E_{miss}, jets);'),
	'DRlep1Jet1':('deltaR_lep1Jets[0]',linspace(0, 4, 51).tolist(),';#DeltaR(lep_{1},jet_{1});'),
	'minDRlep1Jets':('minDR_lep1Jet',linspace(0, 4, 51).tolist(),';min #DeltaR(lep_{1}, jets);'),
	'minDRlep2Jets':('minDR_lep2Jet',linspace(0, 4, 51).tolist(),';min #DeltaR(lep_{2}, jets);'),
	'minDRlep3Jets':('minDR_lep3Jet',linspace(0, 4, 51).tolist(),';min #DeltaR(lep_{3}, jets);'),
	'minDRlepsJets':('minDR_lepJet',linspace(0, 4, 51).tolist(),';min #DeltaR(leps, jets);'),

	'PtRel1':('ptRel_minDRlep1Jet',linspace(0,300,31).tolist(),';p_{T,rel}(lep_{1}, closest jet) [GeV]'),
	'PtRel2':('ptRel_minDRlep2Jet',linspace(0,300,31).tolist(),';p_{T,rel}(lep_{2}, closest jet) [GeV]'),
	'PtRel3':('ptRel_minDRlep3Jet',linspace(0,300,31).tolist(),';p_{T,rel}(lep_{3}, closest jet) [GeV]'),
	'PtRel':('ptRel_minDRlepJet',linspace(0,300,31).tolist(),';p_{T,rel}(min[#DeltaR(lep,jet)] [GeV]'),

# 	'mindeltaRB':('deltaR_lepBJets',linspace(0, 5, 51).tolist(),';min #DeltaR(l, bjet);'),
# 	'mindeltaR1':('deltaR_lepClosestJet[0]',linspace(0, 5, 51).tolist(),';min #DeltaR(l1, jet);'),
# 	'mindeltaR2':('deltaR_lepClosestJet[1]',linspace(0, 5, 51).tolist(),';min #DeltaR(l2, jet);'),
# 	'mindeltaR3':('deltaR_lepClosestJet[2]',linspace(0, 5, 51).tolist(),';min #DeltaR(l3, jet);'),

# 	'deltaRjet1':('deltaR_lepJets[0]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 1^{st} jet);'),
# 	'deltaRjet2':('deltaR_lepJets[1]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 2^{nd} jet);'),
# 	'deltaRjet3':('deltaR_lepJets[2]',linspace(0, 5, 51).tolist(),';#DeltaR(l, 3^{rd} jet);'),

# 	'lepCharge':('AllLeptonCharge_PtOrdered',linspace(-2,2,5).tolist(),';lepton charge'),

# 	'lepIso':('AllLeptonMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),';lepton mini isolation'),
# 	'ElIso':('AllLeptonElMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),';Electron mini isolation'),
# 	'MuIso':('AllLeptonMuMiniIso_PtOrdered',linspace(0,0.6,51).tolist(),'; Muon mini isolation'),

# 	'BjetPt':('AK4JetBTag_MultiLepCalc_PtOrdered',linspace(0,1500,51).tolist(),';b jet p_{T} [GeV]'),  ## B TAG
# 	'Bjet1Pt':('AK4JetBTag_MultiLepCalc_PtOrdered[0]',linspace(0,1500,51).tolist(),';1^{st} b jet p_{T} [GeV]'),  ## B TAG
# 	'Bjet1Pt':('AK4JetBTag_MultiLepCalc_PtOrdered[1]',linspace(0,1500,51).tolist(),';2^{nd} b jet p_{T} [GeV]'),  ## B TAG

# 	'PtRel1':('PtRelLepClosestJet[0]',linspace(0,500,51).tolist(),';p_{T,rel}(l1, closest jet) [GeV]'),
# 	'PtRel2':('PtRelLepClosestJet[1]',linspace(0,500,51).tolist(),';p_{T,rel}(l2, closest jet) [GeV]'),
# 	'PtRel3':('PtRelLepClosestJet[2]',linspace(0,500,51).tolist(),';p_{T,rel}(l3, closest jet) [GeV]'),
	
# 	'MllsameFlavorOS':('Mll_sameFlavorOS',linspace(-10,300,32).tolist(),'; M(ll_{OS}) [GeV]'),
# 	'MllOSall':('MllOS_allComb',linspace(-10,300,32).tolist(),'; M(ll_{OS}) all [GeV]'),
# 	'MllOSallmin':('MllOS_allComb_min',linspace(-10,300,32).tolist(),'; min ( M(ll_{OS}) ) [GeV]'),
# 	'Mlll':('Mlll',linspace(-10,300,32).tolist(),'; M(lll) [GeV]'),

# 	'MllsameFlavorOS':('Mll_sameFlavorOS',Mbins,'; M(ll_{OS}) [GeV]'),
# 	'MllOSall':('MllOS_allComb',Mbins,'; M(ll_{OS}) all [GeV]'),
# 	'MllOSallmin':('MllOS_allComb_min',Mbins,'; min ( M(ll_{OS}) ) [GeV]'),
# 	'MllOSallmax':('MllOS_allComb_max',Mbins,'; max ( M(ll_{OS}) ) [GeV]'),
# 	'Mlll':('Mlll',Mbins,'; M(lll) [GeV]'),
	
	}

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

bkgList = [
# 	'WW',
	'WZ','ZZ',

	'WWW','WWZ','WZZ','ZZZ',
	'TTWl',
	'TTZl',
	]

whichSignal = 'TT' #TT, BB, or T53T53
# whichSignal = 'BB'
signalMassRange = [1000,1800]
#sigList = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
sigList = [whichSignal+'M'+str(mass) for mass in [1000,1500]]
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
readDEBUG=False

#def readTree(file):
#	if not os.path.exists(file): 
#		print "Error: File does not exist! Aborting ...",file
#		os._exit(1)
#	if(readDEBUG):print 'READING file:',file
#	tFile = R.TFile(file,'READ')
#	tTree = tFile.Get('ljmet')
#	return tFile, tTree 
#def readUncTree(file,unc):
#        if not os.path.exists(file):
#                print "Error: File does not exist! Aborting ...",file
#                os._exit(1)
#        if(readDEBUG):print 'READING file:',file
#        tFile = R.TFile(file,'READ')
#        tTree = tFile.Get('ljmet'+unc)
#        return tFile, tTree

def readTree(file,tree):
        if not os.path.exists(file):
                print "Error: File does not exist! Aborting ...",file
                os._exit(1)
        tFile = R.TFile(file,'READ')
        tTree = tFile.Get(tree)
        return tFile, tTree

if(readDEBUG):print "READING TREES"
shapesFiles = ['jec','jer']
# shapesFiles = []
tTreeData = {}
tFileData = {}
treeBaseName = 'ljmet'
for data in dataList:
	if(readDEBUG):print "READING:", data
	tFileData[data],tTreeData[data]=readTree(step1Dir_data+'/'+samples[data]+'_hadd.root',treeBaseName)

tTreeSig = {}
tFileSig = {}
for sig in sigList:
	for decay in decays:
		if(readDEBUG):print "READING:", sig+decay
		if(readDEBUG):print "        nominal"
		tFileSig[sig+decay],tTreeSig[sig+decay]=readTree(step1Dir_mc+'/'+samples[sig+decay]+'_hadd.root',treeBaseName)
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					if(readDEBUG):print "        "+syst+ud
					tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readTree(step1Dir_mc+'/'+samples[sig+decay]+'_hadd.root',treeBaseName+"_"+syst.upper()+ud.lower())
					#tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readUncTree(step1Dir_mc+'/'+samples[sig+decay]+'_hadd.root', syst+ud)
tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList:
	if(readDEBUG):print "READING:",bkg
	if(readDEBUG):print "        nominal"
	if "DataDrivenBkg" in bkg:
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir_data+'/'+samples[bkg]+'_hadd.root',treeBaseName)
	else:
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir_mc+'/'+samples[bkg]+'_hadd.root',treeBaseName)
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if 'DataDriven' in bkg: continue
				else:
					if(readDEBUG):print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir_mc+'/'+samples[bkg]+'_hadd.root',treeBaseName+"_"+syst.upper()+ud.lower())
					#tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readUncTree(step1Dir_mc+'/'+samples[bkg]+'_hadd.root',syst+ud)
print "FINISHED READING"

###########################################################
#################### RUN ANALYSE.PY #######################
###########################################################
DEBUG=False

if len(sys.argv)>2: iPlot=sys.argv[2]
# else: iPlot='minMlb'
#else: iPlot='STrebinned'
# else: iPlot='Mlll'
# else: iPlot='lepIso'
# else: iPlot='JetPt'
else: iPlot='lepPt'
if(DEBUG):print "PLOTTING:",iPlot
if(DEBUG):print "         LJMET Variable:",plotList[iPlot][0]
if(DEBUG):print "         X-AXIS TITLE  :",plotList[iPlot][2]
if(DEBUG):print "         BINNING USED  :",plotList[iPlot][1]

nCats  = len(catList)
catInd = 1
for category in catList:
	print category
	datahists = {}
	bkghists  = {}
	sighists  = {}
	if len(sys.argv)>1: 
                outDir=sys.argv[1]
	else: 
		outDir = '/mnt/data/users/wwong/'
# 		outDir = os.getcwd()+'/'
	outDir+=pfix
	if not os.path.exists(outDir): os.system('mkdir '+outDir)
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
	outDir+='/'+cutString #'/'+cutString
	if not os.path.exists(outDir+'/'+category): os.system('mkdir '+outDir+'/'+category)
	outDir+='/'+category
	print 'outDir', outDir
	for data in dataList: 
		datahists.update(analyze(tTreeData,data,cutList,False,iPlot,plotList[iPlot],category,cutType))
		if catInd==nCats: del tFileData[data]
	for bkg in bkgList: 
		print '+++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>  bkg = ' , bkg 
		bkghists.update(analyze(tTreeBkg,bkg,cutList,doAllSys,iPlot,plotList[iPlot],category,cutType))
		if catInd==nCats: del tFileBkg[bkg]
		if doAllSys and catInd==nCats:
			for syst in shapesFiles:
				if 'DataDriven' in bkg: continue
				for ud in ['Up','Down']: del tFileBkg[bkg+syst+ud]
	for sig in sigList: 
		for decay in decays: 
			sighists.update(analyze(tTreeSig,sig+decay,cutList,doAllSys,iPlot,plotList[iPlot],category,cutType))
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
	print 'Saving pickle files at:',outDir

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
