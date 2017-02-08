#!/usr/bin/python

import os,sys,time,math,datetime,fnmatch,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
from cutList import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

###########################################################
#################### CUTS & OUTPUT ########################
###########################################################

#obtain cutList and cutString from cutList.py

doAllSys= False

#pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_2016_12_19'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_2016_12_21'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_2017_1_9'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_1bjet_2017_1_9'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_ClintsAN16-242_2017_1_10'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_2017_1_13'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_1bjet_2017_1_13'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_2017_1_16'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate_2017_1_17'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate_1bjet_2017_1_17'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_muMinIso0p1_Full2016_IsoTrig_HLTupdate_2017_1_17'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv3_muMinIso0p1_Full2016_IsoTrig_HLTupdate_1bjet_2017_1_19'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_2017_1_20'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_LepPt_2017_1_21'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_1bjet_2017_1_21'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_LepPt_1bjet_2017_1_22'+'/'+cutString
# pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_2017_1_23'+'/'+cutString
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_2017_1_23/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_25/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2_2017_1_26/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2to2p1_2017_1_26/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta2p1to2p4_2017_1_26/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_26/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_30/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2_2017_1_30/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2to2p1_2017_1_30/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta2p1to2p4_2017_1_30/'
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv5test_muMinIso0p1_Full2016_26Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_31/'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet_2017_2_3/'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet_2017_2_3/'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv7test_1bjet_2017_2_7/'

pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv8test_1bjet_2017_2_7/'

# outDir = os.getcwd()+'/'
outDir = '/user_data/rsyarif/'
outDir+=pfix+'/'


category = ['EEE','EEM','EMM','MMM','All']

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

whichSignal = 'TT' #TT, BB, or T53T53
signalMassRange = [800,1800]
signals = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='T53T53': signals = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='T53T53': decays = [''] #decays to tWtW 100% of the time
sigList = {signal+decay:(signal+decay).lower() for signal in signals for decay in decays}

# bkgStackList = ['WJets','VV','TTV','TTJets','T','QCD','ddbkg']
# bkgStackList = ['VV','VVV','TTV','ddbkg']
bkgStackList = ['WZ','ZZ','VV','VVV','TTV','ddbkg']
# wjetList  = ['WJetsMG100','WJetsMG200','WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500']
# zjetList  = ['DY50']
# vvList    = ['WW','WZ','ZZ']
vvList    = ['WZ','ZZ']
wzList    = ['WZ']
zzList    = ['ZZ']
vvvList   = ['WWW','WWZ','WZZ','ZZZ']
# ttvList   = ['TTWl','TTWq','TTZl','TTZq']
ttvList   = ['TTWl','TTZl']
# ttjetList = ['TTJetsPH0to700inc','TTJetsPH700to1000inc','TTJetsPH1000toINFinc','TTJetsPH700mtt','TTJetsPH1000mtt']
# ttjetList = ['TTJetsPH']
tList     = ['Tt','Ts','TtW','TbtW']

signalList = [signal+decay for signal in signals for decay in decays]
topList = ['TTWl','TTZl'] #NoTTJets, No singleT
ewkList = ['WZ','ZZ','WWW','WWZ','WZZ','ZZZ'] #No DY, WJets, WW


dataList = []
ddbkgList = []
ddbkgTTTList = []
ddbkgTTLList = []
ddbkgTLTList = []
ddbkgLTTList = []
ddbkgTLLList = []
ddbkgLTLList = []
ddbkgLLTList = []
ddbkgLLLList = []

#run,dilep, --> set in samples
dataList = []
for run_ in run:
	for dilep_ in dilep:
		dataList.append('Data'+dilep_+run_)
		ddbkgList.append('DataDrivenBkg'+dilep_+run_)
		ddbkgTTTList.append('DataDrivenBkg'+ddbkgCat[0]+dilep_+run_)
		ddbkgTTLList.append('DataDrivenBkg'+ddbkgCat[1]+dilep_+run_)
		ddbkgTLTList.append('DataDrivenBkg'+ddbkgCat[2]+dilep_+run_)
		ddbkgLTTList.append('DataDrivenBkg'+ddbkgCat[3]+dilep_+run_)
		ddbkgTLLList.append('DataDrivenBkg'+ddbkgCat[4]+dilep_+run_)
		ddbkgLTLList.append('DataDrivenBkg'+ddbkgCat[5]+dilep_+run_)
		ddbkgLLTList.append('DataDrivenBkg'+ddbkgCat[6]+dilep_+run_)
		ddbkgLLLList.append('DataDrivenBkg'+ddbkgCat[7]+dilep_+run_)

#adding  muFR scans as ddbkgList -start
ddbkgList_scan = []
index = 0
FRscanIndex = 0
for muFRindex in xrange(loop): #loop, run, dilep --> set in samples.py
	for elFRindex in xrange(loop): #loop, run, dilep --> set in samples.py
		ddbkgList_temp = []
		for i in xrange(len(run)):
			for j in xrange(len(dilep)):
				ddbkgList_temp.append('DataDrivenBkg'+dilep[j]+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex))
				index+=1
		ddbkgList_scan.append(ddbkgList_temp)
		#print 'ddbkgList_scan[',FRscanIndex,'] = ',ddbkgList_scan[FRscanIndex]
		FRscanIndex+=1
#adding  muFR scans as ddbkgList -end


# systematicList = ['pileup','jec','jer','jsf','jmr','jms','btag','tau21','pdfNew','muR','muF',
# 				  'muRFcorrd','toppt','muRFcorrdNew','muRFdecorrdNew','PR','FR']
# systematicList = ['pileup','jec','jer','jsf','btag','pdfNew','muR','muF',
# 				  'muRFcorrd','muRFcorrdNew','muRFdecorrdNew','PR','FR']
# systematicList = ['PR','FR']
systematicList = ['pileup','btag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','PR','FR']


###########################################################
#################### NORMALIZATIONS #######################
###########################################################

lumiSys = 0.062 #6.2% https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM - 20Sep2016 - ATTENTION!! NEEDS to be checked again!
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
lepIdSys = math.sqrt(3.*0.01**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty
corrdSys = math.sqrt(lumiSys**2+trigSys**2+lepIdSys**2+lepIsoSys**2)

def round_sig(x,sig=2):
	try:
		return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
	except:
		return round(x,5)

###########################################################
######### GROUP SAMPLES AND PRINT YIELDS/UNCERTS ##########
###########################################################
def makeCats(datahists,sighists,bkghists,discriminant):
	## Input  histograms (datahists,sighists,bkghists) must have corresponding histograms returned from analyze.py##
	
	## INITIALIZE DICTIONARIES FOR YIELDS AND STATISTICAL UNCERTAINTIES ##
	yieldTable = {}
	yieldErrTable = {} #what is actually stored here is the square of the yield error
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		yieldTable[histoPrefix]={}
		yieldErrTable[histoPrefix]={}
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+systematic+ud]={}
	
	## WRITING HISTOGRAMS IN ROOT FILE ##
	outputRfile = R.TFile(outDir+'/templates_'+discriminant+'_'+lumiStr+'fb.root','RECREATE')
	hsig,htop,hewk,hqcd,hdata={},{},{},{},{}
	hwjets,hzjets,httjets,ht,httv,hvv,hwz,hzz,hvvv={},{},{},{},{},{},{},{},{}
	hddbkg,hddbkgTTT,hddbkgTTL,hddbkgTLT,hddbkgLTT,hddbkgTLL,hddbkgLTL,hddbkgLLT,hddbkgLLL={},{},{},{},{},{},{},{},{}
	
	hddbkg_scan = [{}]
	for FRindex in xrange(len(ddbkgList_scan)-1):hddbkg_scan.append({})
	#print hddbkg_scan
	#print 'there are', len(hddbkg_scan), "{}'s" 
	
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat

		#Group processes
# 		hwjets[cat] = bkghists[histoPrefix+'_'+wjetList[0]].Clone(histoPrefix+'_WJets')
# 		hzjets[cat] = bkghists[histoPrefix+'_'+zjetList[0]].Clone(histoPrefix+'_ZJets')
# 		httjets[cat] = bkghists[histoPrefix+'_'+ttjetList[0]].Clone(histoPrefix+'_TTJets')
# 		ht[cat] = bkghists[histoPrefix+'_'+tList[0]].Clone(histoPrefix+'_T')
		httv[cat] = bkghists[histoPrefix+'_'+ttvList[0]].Clone(histoPrefix+'_TTV')
		hvv[cat] = bkghists[histoPrefix+'_'+vvList[0]].Clone(histoPrefix+'_VV')
		hwz[cat] = bkghists[histoPrefix+'_'+wzList[0]].Clone(histoPrefix+'_WZ')
		hzz[cat] = bkghists[histoPrefix+'_'+zzList[0]].Clone(histoPrefix+'_ZZ')
		hvvv[cat] = bkghists[histoPrefix+'_'+vvvList[0]].Clone(histoPrefix+'_VVV')
		hddbkg[cat] = bkghists[histoPrefix+'_'+ddbkgList[0]].Clone(histoPrefix+'_ddbkg')
		#print 'Cloning ', histoPrefix+'_'+ddbkgList[0], 'and naming it', histoPrefix+'_ddbkg'
		#print hddbkg
		for FRindex in xrange(len(ddbkgList_scan)):
			hddbkg_scan[FRindex][cat] = bkghists[histoPrefix+'_'+ddbkgList_scan[FRindex][0]].Clone(histoPrefix+'_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop))
			#print 'Cloning ',histoPrefix+'_'+ddbkgList_scan[FRindex][0],'and naming it',histoPrefix+'_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)
			#print hddbkg_scan[FRindex]

		hddbkgTTT[cat] = bkghists[histoPrefix+'_'+ddbkgTTTList[0]].Clone(histoPrefix+'_ddbkgTTT')
		hddbkgTTL[cat] = bkghists[histoPrefix+'_'+ddbkgTTLList[0]].Clone(histoPrefix+'_ddbkgTTL')
		hddbkgTLT[cat] = bkghists[histoPrefix+'_'+ddbkgTLTList[0]].Clone(histoPrefix+'_ddbkgTLT')
		hddbkgLTT[cat] = bkghists[histoPrefix+'_'+ddbkgLTTList[0]].Clone(histoPrefix+'_ddbkgLTT')
		hddbkgTLL[cat] = bkghists[histoPrefix+'_'+ddbkgTLLList[0]].Clone(histoPrefix+'_ddbkgTLL')
		hddbkgLTL[cat] = bkghists[histoPrefix+'_'+ddbkgLTLList[0]].Clone(histoPrefix+'_ddbkgLTL')
		hddbkgLLT[cat] = bkghists[histoPrefix+'_'+ddbkgLLTList[0]].Clone(histoPrefix+'_ddbkgLLT')
		hddbkgLLL[cat] = bkghists[histoPrefix+'_'+ddbkgLLLList[0]].Clone(histoPrefix+'_ddbkgLLL')



# 		for bkg in ttjetList:
# 			if bkg!=ttjetList[0]: httjets[cat].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in wjetList:
# 			if bkg!=wjetList[0]: hwjets[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ttvList:
			if bkg!=ttvList[0]: httv[cat].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in tList:
# 			if bkg!=tList[0]: ht[cat].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in zjetList:
# 			if bkg!=zjetList[0]: hzjets[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in vvList:
			if bkg!=vvList[0]: hvv[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in wzList:
			if bkg!=wzList[0]: hwz[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in zzList:
			if bkg!=zzList[0]: hzz[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in vvvList:
			if bkg!=vvvList[0]: hvvv[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgList:
			if bkg!=ddbkgList[0]: 
				hddbkg[cat].Add(bkghists[histoPrefix+'_'+bkg])
				#print 'Adding', bkghists[histoPrefix+'_'+bkg], 'to', hddbkg[cat]
		#print hddbkg
		
		for FRindex in xrange(len(ddbkgList_scan)):
			for bkg in ddbkgList_scan[FRindex]:
				if bkg!=ddbkgList_scan[FRindex][0]: 
					hddbkg_scan[FRindex][cat].Add(bkghists[histoPrefix+'_'+bkg])
					#print 'Adding', bkghists[histoPrefix+'_'+bkg], 'to', hddbkg_scan[FRindex][cat]
			#print hddbkg_scan[FRindex]


		for bkg in ddbkgTTTList:
			if bkg!=ddbkgTTTList[0]: hddbkgTTT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTTLList:
			if bkg!=ddbkgTTLList[0]: hddbkgTTL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTLTList:
			if bkg!=ddbkgTLTList[0]: hddbkgTLT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTTList:
			if bkg!=ddbkgLTTList[0]: hddbkgLTT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTLLList:
			if bkg!=ddbkgTLLList[0]: hddbkgTLL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTLList:
			if bkg!=ddbkgLTLList[0]: hddbkgLTL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLLTList:
			if bkg!=ddbkgLLTList[0]: hddbkgLLT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLLLList:
			if bkg!=ddbkgLLLList[0]: hddbkgLLL[cat].Add(bkghists[histoPrefix+'_'+bkg])

		
		#Group QCD processes
# 		hqcd[cat] = bkghists[histoPrefix+'_'+qcdList[0]].Clone(histoPrefix+'__qcd')
# 		for bkg in qcdList: 
# 			if bkg!=qcdList[0]: hqcd[cat].Add(bkghists[histoPrefix+'_'+bkg])
		
		#Group EWK processes
		hewk[cat] = bkghists[histoPrefix+'_'+ewkList[0]].Clone(histoPrefix+'__ewk')
		for bkg in ewkList:
			if bkg!=ewkList[0]: hewk[cat].Add(bkghists[histoPrefix+'_'+bkg])
		
		#Group TOP processes
		htop[cat] = bkghists[histoPrefix+'_'+topList[0]].Clone(histoPrefix+'__top')
		for bkg in topList:
			if bkg!=topList[0]: htop[cat].Add(bkghists[histoPrefix+'_'+bkg])
		
		#get signal
		for signal in sigList.keys(): hsig[cat+signal] = sighists[histoPrefix+'_'+signal].Clone(histoPrefix+'__'+sigList[signal])
		#get total signal
		for signal in signals: 
			hsig[cat+signal] = sighists[histoPrefix+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal)
			for decay in decays: 
				if decay!=decays[0]: hsig[cat+signal].Add(sighists[histoPrefix+'_'+signal+decay])

		#systematics
		if doAllSys:
			for systematic in systematicList:
				if systematic=='pdfNew' or systematic=='muRFcorrdNew' or systematic=='muRFdecorrdNew': continue
				for ud in ['Up','Down']:
					if systematic!='toppt' and systematic!='PR' and systematic!='FR':
# 						hqcd[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hewk[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						htop[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+topList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for signal in sigList.keys(): hsig[cat+signal+systematic+ud] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal].Clone(histoPrefix+'__'+sigList[signal]+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for signal in signals: 
							hsig[cat+signal+systematic+ud] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
							for decay in decays: 
								if decay!=decays[0]: hsig[cat+signal+systematic+ud].Add(sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decay])
# 						for bkg in qcdList: 
# 							if bkg!=qcdList[0]: hqcd[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in ewkList: 
							if bkg!=ewkList[0]: hewk[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in topList: 
							if bkg!=topList[0]: htop[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
					if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
						htop[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ttjetList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for bkg in ttjetList: 
							if bkg!=ttjetList[0]: htop[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in topList: 
							if bkg not in ttjetList: htop[cat+systematic+ud].Add(bkghists[histoPrefix+'_'+bkg])
					if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
						hddbkg[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ddbkgList[0]].Clone(histoPrefix+'__ddbkg__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for bkg in ddbkgList: 
							if bkg!=ddbkgList[0]: hddbkg[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])

			htop[cat+'muRFcorrdNewUp'] = htop[cat+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFcorrdNew__plus')
			htop[cat+'muRFcorrdNewDown'] = htop[cat+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFcorrdNew__minus')
			hewk[cat+'muRFcorrdNewUp'] = hewk[cat+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFcorrdNew__plus')
			hewk[cat+'muRFcorrdNewDown'] = hewk[cat+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFcorrdNew__minus')
# 			hqcd[cat+'muRFcorrdNewUp'] = hqcd[cat+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFcorrdNew__plus')
# 			hqcd[cat+'muRFcorrdNewDown'] = hqcd[cat+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFcorrdNew__minus')
			for signal in sigList.keys(): hsig[cat+signal+'muRFcorrdNewUp'] = hsig[cat+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFcorrdNew__plus')
			for signal in sigList.keys(): hsig[cat+signal+'muRFcorrdNewDown'] = hsig[cat+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFcorrdNew__minus')
			for signal in signals: 
				hsig[cat+signal+'muRFcorrdNewUp'] = hsig[cat+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFcorrdNew__plus')
				hsig[cat+signal+'muRFcorrdNewDown'] = hsig[cat+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFcorrdNew__minus')

			htop[cat+'muRFdecorrdNewUp'] = htop[cat+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFdecorrdNew__plus')
			htop[cat+'muRFdecorrdNewDown'] = htop[cat+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFdecorrdNew__minus')
			hewk[cat+'muRFdecorrdNewUp'] = hewk[cat+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFdecorrdNew__plus')
			hewk[cat+'muRFdecorrdNewDown'] = hewk[cat+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFdecorrdNew__minus')
# 			hqcd[cat+'muRFdecorrdNewUp'] = hqcd[cat+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFdecorrdNew__plus')
# 			hqcd[cat+'muRFdecorrdNewDown'] = hqcd[cat+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFdecorrdNew__minus')
			for signal in sigList.keys(): hsig[cat+signal+'muRFdecorrdNewUp'] = hsig[cat+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFdecorrdNew__plus')
			for signal in sigList.keys(): hsig[cat+signal+'muRFdecorrdNewDown'] = hsig[cat+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFdecorrdNew__minus')
			for signal in signals: 
				hsig[cat+signal+'muRFdecorrdNewUp'] = hsig[cat+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFdecorrdNew__plus')
				hsig[cat+signal+'muRFdecorrdNewDown'] = hsig[cat+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFdecorrdNew__minus')

			# nominal,renormWeights[4],renormWeights[2],renormWeights[1],renormWeights[0],renormWeights[5],renormWeights[3]
			histPrefixList = ['','muRUp','muRDown','muFUp','muFDown','muRFcorrdUp','muRFcorrdDown']
			for ibin in range(1,htop[cat].GetNbinsX()+1):
				weightListTop = [htop[cat+item].GetBinContent(ibin) for item in histPrefixList]	
				weightListEwk = [hewk[cat+item].GetBinContent(ibin) for item in histPrefixList]	
# 				weightListQcd = [hqcd[cat+item].GetBinContent(ibin) for item in histPrefixList]	
				weightListSig = {}
				for signal in sigList.keys()+signals: weightListSig[signal] = [hsig[cat+signal+item].GetBinContent(ibin) for item in histPrefixList]
				indTopRFcorrdUp = weightListTop.index(max(weightListTop))
				indTopRFcorrdDn = weightListTop.index(min(weightListTop))
				indEwkRFcorrdUp = weightListEwk.index(max(weightListEwk))
				indEwkRFcorrdDn = weightListEwk.index(min(weightListEwk))
# 				indQcdRFcorrdUp = weightListQcd.index(max(weightListQcd))
# 				indQcdRFcorrdDn = weightListQcd.index(min(weightListQcd))
				indSigRFcorrdUp = {}
				indSigRFcorrdDn = {}
				for signal in sigList.keys()+signals: 
					indSigRFcorrdUp[signal] = weightListSig[signal].index(max(weightListSig[signal]))
					indSigRFcorrdDn[signal] = weightListSig[signal].index(min(weightListSig[signal]))

				indTopRFdecorrdUp = weightListTop.index(max(weightListTop[:-2]))
				indTopRFdecorrdDn = weightListTop.index(min(weightListTop[:-2]))
				indEwkRFdecorrdUp = weightListEwk.index(max(weightListEwk[:-2]))
				indEwkRFdecorrdDn = weightListEwk.index(min(weightListEwk[:-2]))
# 				indQcdRFdecorrdUp = weightListQcd.index(max(weightListQcd[:-2]))
# 				indQcdRFdecorrdDn = weightListQcd.index(min(weightListQcd[:-2]))
				indSigRFdecorrdUp = {}
				indSigRFdecorrdDn = {}
				for signal in sigList.keys()+signals: 
					indSigRFdecorrdUp[signal] = weightListSig[signal].index(max(weightListSig[signal][:-2]))
					indSigRFdecorrdDn[signal] = weightListSig[signal].index(min(weightListSig[signal][:-2]))
				
				htop[cat+'muRFcorrdNewUp'].SetBinContent(ibin,htop[cat+histPrefixList[indTopRFcorrdUp]].GetBinContent(ibin))
				htop[cat+'muRFcorrdNewDown'].SetBinContent(ibin,htop[cat+histPrefixList[indTopRFcorrdDn]].GetBinContent(ibin))
				hewk[cat+'muRFcorrdNewUp'].SetBinContent(ibin,hewk[cat+histPrefixList[indEwkRFcorrdUp]].GetBinContent(ibin))
				hewk[cat+'muRFcorrdNewDown'].SetBinContent(ibin,hewk[cat+histPrefixList[indEwkRFcorrdDn]].GetBinContent(ibin))
# 				hqcd[cat+'muRFcorrdNewUp'].SetBinContent(ibin,hqcd[cat+histPrefixList[indQcdRFcorrdUp]].GetBinContent(ibin))
# 				hqcd[cat+'muRFcorrdNewDown'].SetBinContent(ibin,hqcd[cat+histPrefixList[indQcdRFcorrdDn]].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'muRFcorrdNewUp'].SetBinContent(ibin,hsig[cat+signal+histPrefixList[indSigRFcorrdUp[signal]]].GetBinContent(ibin))
					hsig[cat+signal+'muRFcorrdNewDown'].SetBinContent(ibin,hsig[cat+signal+histPrefixList[indSigRFcorrdDn[signal]]].GetBinContent(ibin))
				htop[cat+'muRFdecorrdNewUp'].SetBinContent(ibin,htop[cat+histPrefixList[indTopRFdecorrdUp]].GetBinContent(ibin))
				htop[cat+'muRFdecorrdNewDown'].SetBinContent(ibin,htop[cat+histPrefixList[indTopRFdecorrdDn]].GetBinContent(ibin))
				hewk[cat+'muRFdecorrdNewUp'].SetBinContent(ibin,hewk[cat+histPrefixList[indEwkRFdecorrdUp]].GetBinContent(ibin))
				hewk[cat+'muRFdecorrdNewDown'].SetBinContent(ibin,hewk[cat+histPrefixList[indEwkRFdecorrdDn]].GetBinContent(ibin))
# 				hqcd[cat+'muRFdecorrdNewUp'].SetBinContent(ibin,hqcd[cat+histPrefixList[indQcdRFdecorrdUp]].GetBinContent(ibin))
# 				hqcd[cat+'muRFdecorrdNewDown'].SetBinContent(ibin,hqcd[cat+histPrefixList[indQcdRFdecorrdDn]].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'muRFdecorrdNewUp'].SetBinContent(ibin,hsig[cat+signal+histPrefixList[indSigRFdecorrdUp[signal]]].GetBinContent(ibin))
					hsig[cat+signal+'muRFdecorrdNewDown'].SetBinContent(ibin,hsig[cat+signal+histPrefixList[indSigRFdecorrdDn[signal]]].GetBinContent(ibin))

				htop[cat+'muRFcorrdNewUp'].SetBinError(ibin,htop[cat+histPrefixList[indTopRFcorrdUp]].GetBinError(ibin))
				htop[cat+'muRFcorrdNewDown'].SetBinError(ibin,htop[cat+histPrefixList[indTopRFcorrdDn]].GetBinError(ibin))
				hewk[cat+'muRFcorrdNewUp'].SetBinError(ibin,hewk[cat+histPrefixList[indEwkRFcorrdUp]].GetBinError(ibin))
				hewk[cat+'muRFcorrdNewDown'].SetBinError(ibin,hewk[cat+histPrefixList[indEwkRFcorrdDn]].GetBinError(ibin))
# 				hqcd[cat+'muRFcorrdNewUp'].SetBinError(ibin,hqcd[cat+histPrefixList[indQcdRFcorrdUp]].GetBinError(ibin))
# 				hqcd[cat+'muRFcorrdNewDown'].SetBinError(ibin,hqcd[cat+histPrefixList[indQcdRFcorrdDn]].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'muRFcorrdNewUp'].SetBinError(ibin,hsig[cat+signal+histPrefixList[indSigRFcorrdUp[signal]]].GetBinError(ibin))
					hsig[cat+signal+'muRFcorrdNewDown'].SetBinError(ibin,hsig[cat+signal+histPrefixList[indSigRFcorrdDn[signal]]].GetBinError(ibin))
				htop[cat+'muRFdecorrdNewUp'].SetBinError(ibin,htop[cat+histPrefixList[indTopRFdecorrdUp]].GetBinError(ibin))
				htop[cat+'muRFdecorrdNewDown'].SetBinError(ibin,htop[cat+histPrefixList[indTopRFdecorrdDn]].GetBinError(ibin))
				hewk[cat+'muRFdecorrdNewUp'].SetBinError(ibin,hewk[cat+histPrefixList[indEwkRFdecorrdUp]].GetBinError(ibin))
				hewk[cat+'muRFdecorrdNewDown'].SetBinError(ibin,hewk[cat+histPrefixList[indEwkRFdecorrdDn]].GetBinError(ibin))
# 				hqcd[cat+'muRFdecorrdNewUp'].SetBinError(ibin,hqcd[cat+histPrefixList[indQcdRFdecorrdUp]].GetBinError(ibin))
# 				hqcd[cat+'muRFdecorrdNewDown'].SetBinError(ibin,hqcd[cat+histPrefixList[indQcdRFdecorrdDn]].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'muRFdecorrdNewUp'].SetBinError(ibin,hsig[cat+signal+histPrefixList[indSigRFdecorrdUp[signal]]].GetBinError(ibin))
					hsig[cat+signal+'muRFdecorrdNewDown'].SetBinError(ibin,hsig[cat+signal+histPrefixList[indSigRFdecorrdDn[signal]]].GetBinError(ibin))

			for pdfInd in range(100):
# 				hqcd[cat+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__pdf'+str(pdfInd))
				hewk[cat+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__pdf'+str(pdfInd))
				htop[cat+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+topList[0]].Clone(histoPrefix+'__top__pdf'+str(pdfInd))
				for signal in sigList.keys(): hsig[cat+signal+'pdf'+str(pdfInd)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal].Clone(histoPrefix+'__'+signal+'__pdf'+str(pdfInd))
				for signal in signals: 
					hsig[cat+signal+'pdf'+str(pdfInd)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal+'__pdf'+str(pdfInd))
					for decay in decays: 
						if decay!=decays[0]: hsig[cat+signal+'pdf'+str(pdfInd)].Add(sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decay])
# 				for bkg in qcdList: 
# 					if bkg!=qcdList[0]: hqcd[cat+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in ewkList: 
					if bkg!=ewkList[0]: hewk[cat+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in topList: 
					if bkg!=topList[0]: htop[cat+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
			htop[cat+'pdfNewUp'] = htop[cat+'pdf0'].Clone(histoPrefix+'__top__pdfNew__plus')
			htop[cat+'pdfNewDown'] = htop[cat+'pdf0'].Clone(histoPrefix+'__top__pdfNew__minus')
			hewk[cat+'pdfNewUp'] = hewk[cat+'pdf0'].Clone(histoPrefix+'__ewk__pdfNew__plus')
			hewk[cat+'pdfNewDown'] = hewk[cat+'pdf0'].Clone(histoPrefix+'__ewk__pdfNew__minus')
# 			hqcd[cat+'pdfNewUp'] = hqcd[cat+'pdf0'].Clone(histoPrefix+'__qcd__pdfNew__plus')
# 			hqcd[cat+'pdfNewDown'] = hqcd[cat+'pdf0'].Clone(histoPrefix+'__qcd__pdfNew__minus')
			for signal in sigList.keys(): hsig[cat+signal+'pdfNewUp'] = hsig[cat+signal+'pdf0'].Clone(histoPrefix+'__'+sigList[signal]+'__pdfNew__plus')
			for signal in sigList.keys(): hsig[cat+signal+'pdfNewDown'] = hsig[cat+signal+'pdf0'].Clone(histoPrefix+'__'+sigList[signal]+'__pdfNew__minus')
			for signal in signals: 
				hsig[cat+signal+'pdfNewUp'] = hsig[cat+signal+decays[0]+'pdf0'].Clone(histoPrefix+'__'+signal+'__pdfNew__plus')
				hsig[cat+signal+'pdfNewDown'] = hsig[cat+signal+decays[0]+'pdf0'].Clone(histoPrefix+'__'+signal+'__pdfNew__minus')
			for ibin in range(1,htop[cat+'pdfNewUp'].GetNbinsX()+1):
				weightListTop = [htop[cat+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListEwk = [hewk[cat+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
# 				weightListQcd = [hqcd[cat+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListSig = {}
				for signal in sigList.keys()+signals: weightListSig[signal] = [hsig[cat+signal+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				indTopPDFUp = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[83]
				indTopPDFDn = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[15]
				indEwkPDFUp = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[83]
				indEwkPDFDn = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[15]
# 				indQcdPDFUp = sorted(range(len(weightListQcd)), key=lambda k: weightListQcd[k])[83]
# 				indQcdPDFDn = sorted(range(len(weightListQcd)), key=lambda k: weightListQcd[k])[15]
				indSigPDFUp = {}
				indSigPDFDn = {}
				for signal in sigList.keys()+signals: 
					indSigPDFUp[signal] = sorted(range(len(weightListSig[signal])), key=lambda k: weightListSig[signal][k])[83]
					indSigPDFDn[signal] = sorted(range(len(weightListSig[signal])), key=lambda k: weightListSig[signal][k])[15]
				
				htop[cat+'pdfNewUp'].SetBinContent(ibin,htop[cat+'pdf'+str(indTopPDFUp)].GetBinContent(ibin))
				htop[cat+'pdfNewDown'].SetBinContent(ibin,htop[cat+'pdf'+str(indTopPDFDn)].GetBinContent(ibin))
				hewk[cat+'pdfNewUp'].SetBinContent(ibin,hewk[cat+'pdf'+str(indEwkPDFUp)].GetBinContent(ibin))
				hewk[cat+'pdfNewDown'].SetBinContent(ibin,hewk[cat+'pdf'+str(indEwkPDFDn)].GetBinContent(ibin))
# 				hqcd[cat+'pdfNewUp'].SetBinContent(ibin,hqcd[cat+'pdf'+str(indQcdPDFUp)].GetBinContent(ibin))
# 				hqcd[cat+'pdfNewDown'].SetBinContent(ibin,hqcd[cat+'pdf'+str(indQcdPDFDn)].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'pdfNewUp'].SetBinContent(ibin,hsig[cat+signal+'pdf'+str(indSigPDFUp[signal])].GetBinContent(ibin))
					hsig[cat+signal+'pdfNewDown'].SetBinContent(ibin,hsig[cat+signal+'pdf'+str(indSigPDFDn[signal])].GetBinContent(ibin))

				htop[cat+'pdfNewUp'].SetBinError(ibin,htop[cat+'pdf'+str(indTopPDFUp)].GetBinError(ibin))
				htop[cat+'pdfNewDown'].SetBinError(ibin,htop[cat+'pdf'+str(indTopPDFDn)].GetBinError(ibin))
				hewk[cat+'pdfNewUp'].SetBinError(ibin,hewk[cat+'pdf'+str(indEwkPDFUp)].GetBinError(ibin))
				hewk[cat+'pdfNewDown'].SetBinError(ibin,hewk[cat+'pdf'+str(indEwkPDFDn)].GetBinError(ibin))
# 				hqcd[cat+'pdfNewUp'].SetBinError(ibin,hqcd[cat+'pdf'+str(indQcdPDFUp)].GetBinError(ibin))
# 				hqcd[cat+'pdfNewDown'].SetBinError(ibin,hqcd[cat+'pdf'+str(indQcdPDFDn)].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[cat+signal+'pdfNewUp'].SetBinError(ibin,hsig[cat+signal+'pdf'+str(indSigPDFUp[signal])].GetBinError(ibin))
					hsig[cat+signal+'pdfNewDown'].SetBinError(ibin,hsig[cat+signal+'pdf'+str(indSigPDFDn[signal])].GetBinError(ibin))
		
		#Group data processes
		hdata[cat] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
		for dat in dataList:
			if dat!=dataList[0]: hdata[cat].Add(datahists[histoPrefix+'_'+dat])

		#prepare yield table

		yieldTable[histoPrefix]['top']    = htop[cat].Integral()
		yieldTable[histoPrefix]['ewk']    = hewk[cat].Integral()
# 		yieldTable[histoPrefix]['qcd']    = hqcd[cat].Integral()
# 		yieldTable[histoPrefix]['totBkg'] = htop[cat].Integral()+hewk[cat].Integral()+hqcd[cat].Integral()+hddbkg[cat].Integral()
		yieldTable[histoPrefix]['totBkg'] = htop[cat].Integral()+hewk[cat].Integral()+hddbkg[cat].Integral()

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] = htop[cat].Integral()+hewk[cat].Integral()+hddbkg_scan[FRindex][cat].Integral()
			#print histoPrefix+' totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)+' =', yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] 

		yieldTable[histoPrefix]['data']   = hdata[cat].Integral()
		if yieldTable[histoPrefix]['totBkg']!=0:
			yieldTable[histoPrefix]['dataOverBkg']= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
		else:
			yieldTable[histoPrefix]['dataOverBkg']= 0.

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			if yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]!=0:
				yieldTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]
			else:
				yieldTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]= 0.
			yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] = 0.
			for ibin in range(1,hsig[cat+signal].GetXaxis().GetNbins()+1):
				yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] += ( hdata[cat].GetBinContent(ibin) - 	( htop[cat].GetBinContent(ibin)+hewk[cat].GetBinContent(ibin)+hddbkg_scan[FRindex][cat].GetBinContent(ibin) ) )**2 / ( htop[cat].GetBinContent(ibin)+hewk[cat].GetBinContent(ibin)+hddbkg_scan[FRindex][cat].GetBinContent(ibin)+1e-100 ) 

# 		yieldTable[histoPrefix]['WJets']  = hwjets[cat].Integral()
# 		yieldTable[histoPrefix]['ZJets']  = hzjets[cat].Integral()
		yieldTable[histoPrefix]['VV']     = hvv[cat].Integral()
		yieldTable[histoPrefix]['WZ']     = hwz[cat].Integral()
		yieldTable[histoPrefix]['ZZ']     = hzz[cat].Integral()
		yieldTable[histoPrefix]['VVV']    = hvvv[cat].Integral()
		yieldTable[histoPrefix]['TTV']    = httv[cat].Integral()
# 		yieldTable[histoPrefix]['TTJets'] = httjets[cat].Integral()
# 		yieldTable[histoPrefix]['T']      = ht[cat].Integral()
# 		yieldTable[histoPrefix]['QCD']    = hqcd[cat].Integral()
		yieldTable[histoPrefix]['ddbkg']  = hddbkg[cat].Integral()
					
		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			yieldTable[histoPrefix]['ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]  = hddbkg_scan[FRindex][cat].Integral()
			#print 'yield '+histoPrefix+' ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop),'=',yieldTable[histoPrefix]['ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]

		yieldTable[histoPrefix]['ddbkgTTT']  = hddbkgTTT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTTL']  = hddbkgTTL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTLT']  = hddbkgTLT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLTT']  = hddbkgLTT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTLL']  = hddbkgTLL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLTL']  = hddbkgLTL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLLT']  = hddbkgLLT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLLL']  = hddbkgLLL[cat].Integral()

		for signal in sigList.keys(): yieldTable[histoPrefix][signal] = hsig[cat+signal].Integral()
		for signal in signals: yieldTable[histoPrefix][signal] = hsig[cat+signal].Integral()
		
		#+/- 1sigma variations of shape systematics
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					if systematic!='PR' and systematic!='FR':
						yieldTable[histoPrefix+systematic+ud]['top'] = htop[cat+systematic+ud].Integral()
						if systematic!='toppt':
							yieldTable[histoPrefix+systematic+ud]['ewk'] = hewk[cat+systematic+ud].Integral()
# 							yieldTable[histoPrefix+systematic+ud]['qcd'] = hqcd[cat+systematic+ud].Integral()
							for signal in sigList.keys(): yieldTable[histoPrefix+systematic+ud][signal] = hsig[cat+signal+systematic+ud].Integral()
							for signal in signals: yieldTable[histoPrefix+systematic+ud][signal] = hsig[cat+signal+systematic+ud].Integral()
					if systematic=='PR' or systematic=='FR':
						yieldTable[histoPrefix+systematic+ud]['ddbkg'] = hddbkg[cat+systematic+ud].Integral()

		#prepare MC yield error table
		yieldErrTable[histoPrefix]['top']    = 0.
		yieldErrTable[histoPrefix]['ewk']    = 0.
# 		yieldErrTable[histoPrefix]['qcd']    = 0.
		yieldErrTable[histoPrefix]['totBkg'] = 0.
		yieldErrTable[histoPrefix]['data']   = 0.
		yieldErrTable[histoPrefix]['dataOverBkg']= 0.
# 		yieldErrTable[histoPrefix]['WJets']  = 0.
# 		yieldErrTable[histoPrefix]['ZJets']  = 0.
		yieldErrTable[histoPrefix]['VV']     = 0.
		yieldErrTable[histoPrefix]['WZ']     = 0.
		yieldErrTable[histoPrefix]['ZZ']     = 0.
		yieldErrTable[histoPrefix]['VVV']    = 0.
		yieldErrTable[histoPrefix]['TTV']    = 0.
# 		yieldErrTable[histoPrefix]['TTJets'] = 0.
# 		yieldErrTable[histoPrefix]['T']      = 0.
# 		yieldErrTable[histoPrefix]['QCD']    = 0.

		yieldErrTable[histoPrefix]['ddbkg']  = 0.

		#look here
		for FRindex in xrange(len(ddbkgList_scan)): 
			yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] = 0.
			yieldErrTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]= 0.
			yieldErrTable[histoPrefix]['ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]  = 0.

		yieldErrTable[histoPrefix]['ddbkgTTT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTTL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTLT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLTT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTLL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLTL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLLT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLLL']  = 0.

		for signal in sigList.keys(): yieldErrTable[histoPrefix][signal] = 0.
		for signal in signals: yieldErrTable[histoPrefix][signal] = 0.

		for ibin in range(1,hsig[cat+signal].GetXaxis().GetNbins()+1):
			yieldErrTable[histoPrefix]['top']    += htop[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ewk']    += hewk[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['qcd']    += hqcd[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['totBkg'] += htop[cat].GetBinError(ibin)**2+hewk[cat].GetBinError(ibin)**2+hqcd[cat].GetBinError(ibin)**2+hddbkg[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['totBkg'] += htop[cat].GetBinError(ibin)**2+hewk[cat].GetBinError(ibin)**2+hddbkg[cat].GetBinError(ibin)**2
				
			yieldErrTable[histoPrefix]['data']   += hdata[cat].GetBinError(ibin)**2
# 			print "hdata[cat].GetBinError(ibin) = ", hdata[cat].GetBinError(ibin)
# 			print "hdata[cat].GetBinError(ibin)*hdata[cat].GetBinError(ibin) = ", hdata[cat].GetBinError(ibin)*hdata[cat].GetBinError(ibin)
# 			print "yieldErrTable[histoPrefix]['data'] = ", yieldErrTable[histoPrefix]['data']
# 			yieldErrTable[histoPrefix]['WJets']  += hwjets[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['ZJets']  += hzjets[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['VV']     += hvv[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['WZ']     += hwz[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ZZ']     += hzz[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['VVV']    += hvvv[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['TTV']    += httv[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['TTJets'] += httjets[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['T']      += ht[cat].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['QCD']    += hqcd[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkg']  += hddbkg[cat].GetBinError(ibin)**2

			yieldErrTable[histoPrefix]['ddbkgTTT']  += hddbkgTTT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTTL']  += hddbkgTTL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTLT']  += hddbkgTLT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTT']  += hddbkgLTT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTLL']  += hddbkgTLL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTL']  += hddbkgLTL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLLT']  += hddbkgLLT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLLL']  += hddbkgLLL[cat].GetBinError(ibin)**2

			for signal in sigList.keys(): yieldErrTable[histoPrefix][signal] += hsig[cat+signal].GetBinError(ibin)**2
			for signal in signals: yieldErrTable[histoPrefix][signal] += hsig[cat+signal].GetBinError(ibin)**2

		#look here , need to treat totbkg and ddbkg errors a bit differently to account for muFR scanning
		for FRindex in xrange(len(ddbkgList_scan)):
			for ibin in range(1,hsig[cat+signal].GetXaxis().GetNbins()+1):
				yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] += htop[cat].GetBinError(ibin)**2+hewk[cat].GetBinError(ibin)**2+hddbkg_scan[FRindex][cat].GetBinError(ibin)**2
				yieldErrTable[histoPrefix]['ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]  += hddbkg_scan[FRindex][cat].GetBinError(ibin)**2
			#print 'sqrt yieldErrTable ',histoPrefix,' totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop),'=',math.sqrt(yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)])
			#print 'sqrt yieldErrTable ',histoPrefix,' ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop),'=',math.sqrt(yieldErrTable[histoPrefix]['ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)])

			
		yieldErrTable[histoPrefix]['top']    += (corrdSys*yieldTable[histoPrefix]['top'])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2
		yieldErrTable[histoPrefix]['ewk']    += (corrdSys*yieldTable[histoPrefix]['ewk'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2
# 		yieldErrTable[histoPrefix]['qcd']    += (corrdSys*yieldTable[histoPrefix]['qcd'])**2+(qcdXsecSys*yieldTable[histoPrefix]['qcd'])**2
# 		yieldErrTable[histoPrefix]['totBkg'] += (corrdSys*yieldTable[histoPrefix]['totBkg'])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2+(qcdXsecSys*yieldTable[histoPrefix]['qcd'])**2
		yieldErrTable[histoPrefix]['totBkg'] += (corrdSys*yieldTable[histoPrefix]['totBkg'])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] += (corrdSys*yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2
			#print 'sqrt yieldErrTable ',histoPrefix,' totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop),'=',math.sqrt(yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)])


# 		yieldErrTable[histoPrefix]['WJets']  += (corrdSys*yieldTable[histoPrefix]['WJets'])**2+(ewkXsecSys*yieldTable[histoPrefix]['WJets'])**2
# 		yieldErrTable[histoPrefix]['ZJets']  += (corrdSys*yieldTable[histoPrefix]['ZJets'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ZJets'])**2
		yieldErrTable[histoPrefix]['VV']     += (corrdSys*yieldTable[histoPrefix]['VV'])**2+(ewkXsecSys*yieldTable[histoPrefix]['VV'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
		yieldErrTable[histoPrefix]['WZ']     += (corrdSys*yieldTable[histoPrefix]['WZ'])**2+(ewkXsecSys*yieldTable[histoPrefix]['WZ'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
		yieldErrTable[histoPrefix]['ZZ']     += (corrdSys*yieldTable[histoPrefix]['ZZ'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ZZ'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
		yieldErrTable[histoPrefix]['VVV']    += (corrdSys*yieldTable[histoPrefix]['VVV'])**2+(ewkXsecSys*yieldTable[histoPrefix]['VVV'])**2	#ATTENTION! CHECK IF CORRECT CALCULATION!
		yieldErrTable[histoPrefix]['TTV']    += (corrdSys*yieldTable[histoPrefix]['TTV'])**2+(topXsecSys*yieldTable[histoPrefix]['TTV'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
# 		yieldErrTable[histoPrefix]['TTJets'] += (corrdSys*yieldTable[histoPrefix]['TTJets'])**2+(topXsecSys*yieldTable[histoPrefix]['TTJets'])**2
# 		yieldErrTable[histoPrefix]['T']      += (corrdSys*yieldTable[histoPrefix]['T'])**2+(topXsecSys*yieldTable[histoPrefix]['T'])**2
# 		yieldErrTable[histoPrefix]['QCD']    += (corrdSys*yieldTable[histoPrefix]['QCD'])**2+(qcdXsecSys*yieldTable[histoPrefix]['qcd'])**2
		for signal in sigList.keys(): yieldErrTable[histoPrefix][signal] += (corrdSys*yieldTable[histoPrefix][signal])**2
		for signal in signals: yieldErrTable[histoPrefix][signal] += (corrdSys*yieldTable[histoPrefix][signal])**2

		if yieldTable[histoPrefix]['totBkg']!=0: 
			Ratio = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
		else:
			Ratio = 0.0			
# 		yieldErrTable[histoPrefix]['dataOverBkg'] = (Ratio**2) * ((yieldErrTable[histoPrefix]['data']/(yieldTable[histoPrefix]['data']+1e-20))**2 + (yieldErrTable[histoPrefix]['totBkg']/(yieldTable[histoPrefix]['totBkg']+1e-20))**2)
		yieldErrTable[histoPrefix]['dataOverBkg'] = (Ratio**2) * (        (math.sqrt(yieldErrTable[histoPrefix]['data'])      /(yieldTable[histoPrefix]['data']+1e-20))**2 + (math.sqrt(yieldErrTable[histoPrefix]['totBkg'])/(yieldTable[histoPrefix]['totBkg']+1e-20))**2)
# 		print 'Ratio**2 = ', (Ratio**2)
# 		print '(yieldErrTable[histoPrefix]["data"]) = ', (yieldErrTable[histoPrefix]['data'])
# 		print '(yieldTable[histoPrefix]["data"]+1e-20) = ', (yieldTable[histoPrefix]['data']+1e-20)
# 		print '(yieldErrTable[histoPrefix]["data"]/(yieldTable[histoPrefix]["data"]+1e-20))**2 = ', (yieldErrTable[histoPrefix]['data']/(yieldTable[histoPrefix]['data']+1e-20))**2
# 		print '(yieldErrTable[histoPrefix]["totBkg"]/(yieldTable[histoPrefix]["totBkg"]+1e-20))**2 = ', (yieldErrTable[histoPrefix]['totBkg']/(yieldTable[histoPrefix]['totBkg']+1e-20))**2

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			if yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]!=0: 
				Ratio = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]
			else:
				Ratio = 0.0			
			yieldErrTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] = (Ratio**2) * (        (math.sqrt(yieldErrTable[histoPrefix]['data'])      /(yieldTable[histoPrefix]['data']+1e-20))**2 + (math.sqrt(yieldErrTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)])/(yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)]+1e-20))**2)
			#print 'sqrt yieldErrTable '+histoPrefix+'dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)+' =',math.sqrt( yieldErrTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] )


		hdata[cat].Write()
		#write theta histograms in root file, avoid having processes with no event yield (to make theta happy) 
		for signal in sigList.keys()+signals: 
			#if hsig[cat+signal].Integral() > 0:  
				hsig[cat+signal].Write()
				if doAllSys:
					for systematic in systematicList:
						if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
						hsig[cat+signal+systematic+'Up'].Write()
						hsig[cat+signal+systematic+'Down'].Write()
		if htop[cat].Integral() > 0:  
			htop[cat].Write()
			if doAllSys:
				for systematic in systematicList:
					if systematic=='PR' or systematic=='FR': continue
					htop[cat+systematic+'Up'].Write()
					htop[cat+systematic+'Down'].Write()
		if hewk[cat].Integral() > 0:  
			hewk[cat].Write()
			if doAllSys:
				for systematic in systematicList:
					if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
					hewk[cat+systematic+'Up'].Write()
					hewk[cat+systematic+'Down'].Write()
# 		if hqcd[cat].Integral() > 0:  
# 			hqcd[cat].Write()
# 			if doAllSys:
# 				for systematic in systematicList:
# 					if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
# 					hqcd[cat+systematic+'Up'].Write()
# 					hqcd[cat+systematic+'Down'].Write()
# 		if hwjets[cat].Integral() > 0: hwjets[cat].Write()
# 		if hzjets[cat].Integral() > 0: hzjets[cat].Write()
# 		if httjets[cat].Integral()> 0: httjets[cat].Write()
# 		if ht[cat].Integral() > 0    : ht[cat].Write()
		if httv[cat].Integral() > 0  : httv[cat].Write()
		if hvv[cat].Integral() > 0   : hvv[cat].Write()
		if hwz[cat].Integral() > 0   : hwz[cat].Write()
		if hzz[cat].Integral() > 0   : hzz[cat].Write()
		if hvvv[cat].Integral() > 0  : hvvv[cat].Write()
		if hddbkg[cat].Integral() > 0: 
			hddbkg[cat].Write()
			if doAllSys:
				for systematic in systematicList:
					if systematic!='PR' and systematic!='FR': continue
					hddbkg[cat+systematic+'Up'].Write()
					hddbkg[cat+systematic+'Down'].Write()
		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			if hddbkg_scan[FRindex][cat].Integral() > 0: hddbkg_scan[FRindex][cat].Write()

		hddbkgTTT[cat].Write()

		hddbkgTTL[cat].Write()
		hddbkgTLT[cat].Write()
		hddbkgLTT[cat].Write()

		hddbkgTLL[cat].Write()
		hddbkgLTL[cat].Write()
		hddbkgLLT[cat].Write()

		hddbkgLLL[cat].Write()

	outputRfile.Close()

	stdout_old = sys.stdout
	logFile = open(outDir+'/yields_'+discriminant+'_'+lumiStr.replace('.','p')+'fb.txt','a')
	sys.stdout = logFile

	## PRINTING YIELD TABLE WITH UNCERTAINTIES ##
	#first print table without background grouping
	ljust_i = 1
	print 'CUTS:',cutString
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for bkg in bkgStackList: print bkg.ljust(ljust_i),
	print 'data'.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for bkg in bkgStackList:
			print str(yieldTable[histoPrefix][bkg])+'\t',
		print str(yieldTable[histoPrefix]['data']),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for bkg in bkgStackList:
			print str(math.sqrt(yieldErrTable[histoPrefix][bkg])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['data'])).ljust(ljust_i),
		print

	#now print with top,ewk,qcd grouping
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	print 'ewk'.ljust(ljust_i),
	print 'top'.ljust(ljust_i),
# 	print 'qcd'.ljust(ljust_i),
	print 'ddbkg'.ljust(ljust_i),

	print 'ddbkgTTT'.ljust(ljust_i),
	print 'ddbkgTTL'.ljust(ljust_i),
	print 'ddbkgTLT'.ljust(ljust_i),
	print 'ddbkgLTT'.ljust(ljust_i),
	print 'ddbkgTLL'.ljust(ljust_i),
	print 'ddbkgLTL'.ljust(ljust_i),
	print 'ddbkgLLT'.ljust(ljust_i),
	print 'ddbkgLLL'.ljust(ljust_i),

	print 'data'.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ewk']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['top']).ljust(ljust_i),
# 		print str(yieldTable[histoPrefix]['qcd']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkg']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgTTT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgTTL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgTLT']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLTT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgTLL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLTL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLLT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgLLL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ewk'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['top'])).ljust(ljust_i),
# 		print str(math.sqrt(yieldErrTable[histoPrefix]['qcd'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkg'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTTT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTTL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTLT'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLTT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTLL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLTL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLLT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLLL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['data'])).ljust(ljust_i),
		print

	#print yields for signals
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for sig in signalList: print sig.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for sig in signalList:
			print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for sig in signalList:
			print str(math.sqrt(yieldErrTable[histoPrefix][sig])).ljust(ljust_i),
		print

	#print yields for total signals
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for sig in signals: print sig.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for sig in signals:
			print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for sig in signals:
			print str(math.sqrt(yieldErrTable[histoPrefix][sig])).ljust(ljust_i),
		print
				
	#print for AN tables
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print histoPrefix.ljust(ljust_i),
	print
# 	for process in bkgStackList+['ewk','top','qcd','ddbkg','totBkg','data','dataOverBkg']+signals+signalList:
# 	for process in bkgStackList+['ewk','top','qcd','ddbkg','ddbkgTTT','ddbkgTTL','ddbkgTLL','ddbkgLLL','totBkg','data','dataOverBkg']+signals+signalList:
# 	for process in bkgStackList+['ewk','top','ddbkg','ddbkgTTT','ddbkgTTL','ddbkgTLL','ddbkgLLL','totBkg','data','dataOverBkg']+signals+signalList:
	for process in bkgStackList+['ewk','top','ddbkgTTT','ddbkgTTL','ddbkgTLT','ddbkgLTT','ddbkgTLL','ddbkgLTL','ddbkgLLT','ddbkgLLL','totBkg','data','dataOverBkg']+signals+signalList:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4))+' $\pm$ '+str(round_sig(math.sqrt(yieldErrTable[histoPrefix][process]),2)),
		print '\\\\',
		print

	#print for AN tables - ddbkg scan
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print histoPrefix.ljust(ljust_i),
	print

	#look here!!
	tempProcess = ['ewk','top']
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop))
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop))
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('dataOverBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop))
	for process in tempProcess:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4))+' $\pm$ '+str(round_sig(math.sqrt(yieldErrTable[histoPrefix][process]),2)),
		print '\\\\',
		print

	tempProcess = []
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('chiSq_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop))
	for process in tempProcess:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4)),
		print '\\\\',
		print
				
	sys.stdout = stdout_old
	logFile.close()

	## WRITING HISTOGRAMS IN ROOT FILE for ChiSq of 2DFRscan##
	print ''
	print 'Processing 2D Lep FR scan Chi Sq:'
	outputRfile_chiSq = R.TFile(outDir+'/chiSq_'+discriminant+'_'+lumiStr+'fb.root','RECREATE')
	h_chiSq={}
	min_chiSq={}
	min_process = {}		
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		min_chiSq[cat] = 100000.
		h_chiSq[cat] = R.TH2D('chiSq_'+cat,'chiSq_'+cat,loop,initial,end+increment,loop,initial,end+increment)
		for FRindex in xrange(len(ddbkgList_scan)):
			process ='chiSq_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop) 
			chiSq = round_sig(yieldTable[histoPrefix][process],4)
			bin_x = 1+(FRindex/loop)
			bin_y = 1+(FRindex%loop)
			h_chiSq[cat].SetBinContent(bin_x,bin_y,chiSq)
			#print cat, process, 'filling TH2D(', bin_x,bin_y,chiSq,')'
			if chiSq < min_chiSq[cat]:
				min_chiSq[cat] = chiSq
				min_process[cat] = process
		h_chiSq[cat].Write()

	#Calculate average chi_avr plot, and find global minimum.
	min_chiSq['average'] = 100000.
	h_chiSq['average'] = R.TH2D('chiSq_average','chiSq_average',loop,initial,end+increment,loop,initial,end+increment)
	for FRindex in xrange(len(ddbkgList_scan)):
		chiSq_avr = 0.0
		process ='chiSq_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop) 
		for cat in category: 
			if 'All' in cat: continue
			chiSq_avr += round_sig(yieldTable[discriminant+'_'+lumiStr+'fb_'+cat][process] / 4. ,4)
		if chiSq_avr < min_chiSq['average']:
			min_chiSq['average'] = chiSq_avr
			min_process['average'] = process
		bin_x = 1+(FRindex/loop)
		bin_y = 1+(FRindex%loop)
		h_chiSq['average'].SetBinContent(bin_x,bin_y,chiSq_avr)
		#print 'average', process, 'filling TH2D(',bin_x,bin_y,chiSq_avr,')'
	h_chiSq['average'].Write()

	for cat in category+['average']: 
		try:
			print 'Minimum ',cat,' chi sq = ', min_chiSq[cat], min_process[cat].replace('chiSq_ddbkg','').split('_')[0].replace('MuFR','MuFR = '),'% ',min_process[cat].replace('chiSq_ddbkg','').split('_')[1].replace('ElFR','ElFR = '),'%'
		except:
			print 'Something is wrong or empty. So check!'
			continue
	
	outputRfile_chiSq.Close()


###########################################################
###################### LOAD HISTS #########################
###########################################################

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

distList = []
print outDir
for file in findfiles(outDir+'/'+category[0]+'/', '*.p'):
    if 'bkghists' not in file: continue
    distList.append(file.split('_')[-1][:-2])
print distList
for dist in distList:
	print "DISTRIBUTION: ",dist
# 	if 'STrebinned' in dist:
# 		print 'Skipping',  dist
# 		continue
	datahists = {}
	bkghists  = {}
	sighists  = {}
	#if dist!='minMlb' and dist!='HT':continue
	for cat in category:
		print "LOADING: ",cat
		datahists.update(pickle.load(open(outDir+'/'+cat+'/datahists_'+dist+'.p','rb')))
		bkghists.update(pickle.load(open(outDir+'/'+cat+'/bkghists_'+dist+'.p','rb')))
		sighists.update(pickle.load(open(outDir+'/'+cat+'/sighists_'+dist+'.p','rb')))
	makeCats(datahists,sighists,bkghists,dist)

print 'AFTER YOU CHECK THE OUTPUT FILES, DELETE THE PICKLE FILES !!!!!!!'
print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
