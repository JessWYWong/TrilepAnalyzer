#!/usr/bin/python

import os,sys,time,math,datetime,fnmatch,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

DEBUG = False
DEBUG_normalizeRENORM_PDF = False
if(DEBUG or DEBUG_normalizeRENORM_PDF): print ''
if(DEBUG or DEBUG_normalizeRENORM_PDF): print ''
if(DEBUG or DEBUG_normalizeRENORM_PDF): print ' --------- IN DEBUGGING MODE ------------ '
if(DEBUG or DEBUG_normalizeRENORM_PDF): print ''
if(DEBUG or DEBUG_normalizeRENORM_PDF): print ''


###########################################################
#################### CUTS & OUTPUT ########################
###########################################################

lumiStr = '41p557'
print 'lumiStr =',lumiStr
# doAllSys= True
doAllSys= False
print 'doAllSys =', doAllSys
normalizeRENORM_PDF = True 
print 'normalizeRENORM_PDF =', normalizeRENORM_PDF


pfix=''

whichPlots=1

if len(sys.argv)>1: pfix = sys.argv[1] 
if len(sys.argv)>2: whichPlots = int(sys.argv[2]) 
print 'whichPlots =', whichPlots,' --> ',
if whichPlots==0:print 'Processing all observables'
if whichPlots==1:print 'Processing ST and mainly lep kinematic plots'
if whichPlots==2:print 'Processing essential plots but not all'
if whichPlots==3:print 'Processing ST and NJets only'
if whichPlots==4:print 'Processing HT, lepPt, ST only'
if whichPlots==5:print 'Processing Electron and Muon kinematics only'
if whichPlots==6:print 'Processing some selection of variables'
if whichPlots==7:print 'Processing DR variables'
if whichPlots==8:print 'Processing lepPt,ST,minMlllbv4'
if whichPlots==9:print 'Processing HT,minMlllb, angles, PtRel, lepPt'
if whichPlots==10:print 'Processing PtRel'
if whichPlots==11:print 'Processing minMlllBv4, lepPt, HT'
if whichPlots==12:print 'Processing lep1,2,3 Pt,Eta'

# outDir = os.getcwd()+'/'
outDir = '/user_data/rsyarif/'
outDir+=pfix+'/'
# outDir+=pfix+'/'+cutString


isEMlist = ['EEE','EEM','EMM','MMM','All']

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

whichSignal = 'TT' #TT, BB, or T53T53
# whichSignal = 'BB'
signalMassRange = [1000,1800]
signals = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='T53T53': signals = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='T53T53': decays = [''] #decays to tWtW 100% of the time
sigList = {signal+decay:(signal+decay).lower() for signal in signals for decay in decays}

# bkgStackList = ['WJets','VV','TTV','TTJets','T','QCD','ddbkg']
# bkgStackList = ['VV','VVV','TTV','ddbkg']
bkgStackList = ['VV','WZ','ZZ','VVV','TTV','ddbkg']
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

sigOverSqrtBkgList = [signal+'OverSqrtBkg' for signal in signals]


systematicList = ['pileup','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','elPR','elFR','muPR','muFR','jec','jer']
# systematicList = ['pileup','btag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','PR','FR','jec','jer']

#how to incorporate this?

normSystematics = { #The All category was obtained by quad sum of the cats! its approximate!
					'elIdSys':{'EEE':0.06,'EEM':0.04,'EMM':0.02,'MMM':0.00,'All':0.075},
					'muIdSys':{'EEE':0.00,'EEM':0.02,'EMM':0.04,'MMM':0.06,'All':0.075},
					'elIsoSys':{'EEE':0.03,'EEM':0.02,'EMM':0.01,'MMM':0.00,'All':0.037},
					'muIsoSys':{'EEE':0.00,'EEM':0.01,'EMM':0.02,'MMM':0.03,'All':0.037},
					'elelelTrigSys':{'EEE':0.03,'EEM':0.00,'EMM':0.00,'MMM':0.00,'All':0.03},
					'elelmuTrigSys':{'EEE':0.00,'EEM':0.03,'EMM':0.00,'MMM':0.00,'All':0.03},
					'elmumuTrigSys':{'EEE':0.00,'EEM':0.00,'EMM':0.03,'MMM':0.00,'All':0.03},
					'mumumuTrigSys':{'EEE':0.00,'EEM':0.00,'EMM':0.00,'MMM':0.03,'All':0.03},
					}

ddbkgSystematics = {}

if 'FRv48sys' in pfix:
	ddbkgSystematics = { #based on elMVAvalueFix Sep20-Sep21 No ST cut - FOR FRv48sys
						'elPRsys':{'EEE':0.09,'EEM':0.05,'EMM':0.02,'MMM':0.00,'All':0.04},
						'muPRsys':{'EEE':0.00,'EEM':0.01,'EMM':0.02,'MMM':0.07,'All':0.02},
						'muFReta':{'EEE':0.00,'EEM':0.12,'EMM':0.16,'MMM':0.33,'All':0.15},
						'FRsys'  :{'EEE':0.34,'EEM':0.31,'EMM':0.19,'MMM':0.24,'All':0.24}, #FRSTHT400low (data-MC)/ddbkg and ttbar MC closure
						}
	print 'Using ddbkgSystematics for FRv48sys'
else:
	ddbkgSystematics = { #based on elMVAvalueFix Sep20-Sep21 No ST cut - FOR FRv49sys
						'elPRsys':{'EEE':0.09,'EEM':0.05,'EMM':0.02,'MMM':0.00,'All':0.04},
						'muPRsys':{'EEE':0.00,'EEM':0.01,'EMM':0.02,'MMM':0.07,'All':0.02},
						'muFReta':{'EEE':0.00,'EEM':0.12,'EMM':0.16,'MMM':0.33,'All':0.15},
						'FRsys'  :{'EEE':0.45,'EEM':0.38,'EMM':0.18,'MMM':0.20,'All':0.24}, #FRCR2 (data-MC)/ddbkg and ttbar MC closure
						}
	print 'Using ddbkgSystematics for FRv49sys'


###########################################################
#################### NORMALIZATIONS #######################
###########################################################

lumiSys = 0.026 #https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
lepIdSys = math.sqrt(3.*0.02**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty	



def getCorrdSysMC(cat): #this is approximate!?
	corrdSys = math.sqrt(lumiSys**2 + trigSys**2 + normSystematics['elIdSys'][cat]**2 + normSystematics['muIdSys'][cat]**2 + normSystematics['elIsoSys'][cat]**2 + normSystematics['muIsoSys'][cat]**2 )
	return corrdSys

	
def getCorrdSysDDBKG(cat):
	ddbkgSys = math.sqrt( ddbkgSystematics['elPRsys'][cat]**2 + ddbkgSystematics['muPRsys'][cat]**2 + ddbkgSystematics['muFReta'][cat]**2 + ddbkgSystematics['FRsys'][cat]**2 )
	return ddbkgSys


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
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		yieldTable[histoPrefix]={}
		yieldErrTable[histoPrefix]={}
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+systematic+ud]={}
	
	## WRITING HISTOGRAMS IN ROOT FILE ##
# 	outputRfile = R.TFile(outDir+'/templates_'+discriminant+'_'+lumiStr+'fb.root','RECREATE')
	savePATH = outDir+'/templates_'+discriminant+'_'+lumiStr+'fb.root'
	if(DEBUG):savePATH = '/user_data/rsyarif/TESSST/templates_'+discriminant+'_'+lumiStr+'fb.root'
	outputRfile = R.TFile(savePATH,'RECREATE')
	print 'Creating ', savePATH
	hsig,htop,hewk,hqcd,hdata={},{},{},{},{}
	hwjets,hzjets,httjets,ht,httv,hvv,hwz,hzz,hvvv={},{},{},{},{},{},{},{},{}
	hddbkg,hddbkgTTT,hddbkgTTL,hddbkgTLT,hddbkgLTT,hddbkgTLL,hddbkgLTL,hddbkgLLT,hddbkgLLL={},{},{},{},{},{},{},{},{}
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		if(DEBUG): print ''
		if(DEBUG): print '--- histoPrefix:',histoPrefix,': ---'
		if(DEBUG): print ''

		#Group processes
# 		hwjets[isEM] = bkghists[histoPrefix+'_'+wjetList[0]].Clone(histoPrefix+'_WJets')
# 		hzjets[isEM] = bkghists[histoPrefix+'_'+zjetList[0]].Clone(histoPrefix+'_ZJets')
# 		httjets[isEM] = bkghists[histoPrefix+'_'+ttjetList[0]].Clone(histoPrefix+'_TTJets')
# 		ht[isEM] = bkghists[histoPrefix+'_'+tList[0]].Clone(histoPrefix+'_T')
		httv[isEM] = bkghists[histoPrefix+'_'+ttvList[0]].Clone(histoPrefix+'_TTV')
		hvv[isEM] = bkghists[histoPrefix+'_'+vvList[0]].Clone(histoPrefix+'_VV')
		hwz[isEM] = bkghists[histoPrefix+'_'+wzList[0]].Clone(histoPrefix+'_WZ')
		hzz[isEM] = bkghists[histoPrefix+'_'+zzList[0]].Clone(histoPrefix+'_ZZ')
		hvvv[isEM] = bkghists[histoPrefix+'_'+vvvList[0]].Clone(histoPrefix+'_VVV')
		hddbkg[isEM] = bkghists[histoPrefix+'_'+ddbkgList[0]].Clone(histoPrefix+'_ddbkg')
		hddbkgTTT[isEM] = bkghists[histoPrefix+'_'+ddbkgTTTList[0]].Clone(histoPrefix+'_ddbkgTTT')

		hddbkgTTL[isEM] = bkghists[histoPrefix+'_'+ddbkgTTLList[0]].Clone(histoPrefix+'_ddbkgTTL')
		hddbkgTLT[isEM] = bkghists[histoPrefix+'_'+ddbkgTLTList[0]].Clone(histoPrefix+'_ddbkgTLT')
		hddbkgLTT[isEM] = bkghists[histoPrefix+'_'+ddbkgLTTList[0]].Clone(histoPrefix+'_ddbkgLTT')

		hddbkgTLL[isEM] = bkghists[histoPrefix+'_'+ddbkgTLLList[0]].Clone(histoPrefix+'_ddbkgTLL')
		hddbkgLTL[isEM] = bkghists[histoPrefix+'_'+ddbkgLTLList[0]].Clone(histoPrefix+'_ddbkgLTL')
		hddbkgLLT[isEM] = bkghists[histoPrefix+'_'+ddbkgLLTList[0]].Clone(histoPrefix+'_ddbkgLLT')

		hddbkgLLL[isEM] = bkghists[histoPrefix+'_'+ddbkgLLLList[0]].Clone(histoPrefix+'_ddbkgLLL')


# 		for bkg in ttjetList:
# 			if bkg!=ttjetList[0]: httjets[isEM].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in wjetList:
# 			if bkg!=wjetList[0]: hwjets[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ttvList:
			if bkg!=ttvList[0]: httv[isEM].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in tList:
# 			if bkg!=tList[0]: ht[isEM].Add(bkghists[histoPrefix+'_'+bkg])
# 		for bkg in zjetList:
# 			if bkg!=zjetList[0]: hzjets[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in vvList:
			if bkg!=vvList[0]: hvv[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in wzList:
			if bkg!=wzList[0]: hwz[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in zzList:
			if bkg!=zzList[0]: hzz[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in vvvList:
			if bkg!=vvvList[0]: hvvv[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgList:
			if bkg!=ddbkgList[0]: hddbkg[isEM].Add(bkghists[histoPrefix+'_'+bkg])

		for bkg in ddbkgTTTList:
			if bkg!=ddbkgTTTList[0]: hddbkgTTT[isEM].Add(bkghists[histoPrefix+'_'+bkg])

		for bkg in ddbkgTTLList:
			if bkg!=ddbkgTTLList[0]: hddbkgTTL[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTLTList:
			if bkg!=ddbkgTLTList[0]: hddbkgTLT[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTTList:
			if bkg!=ddbkgLTTList[0]: hddbkgLTT[isEM].Add(bkghists[histoPrefix+'_'+bkg])

		for bkg in ddbkgTLLList:
			if bkg!=ddbkgTLLList[0]: hddbkgTLL[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTLList:
			if bkg!=ddbkgLTLList[0]: hddbkgLTL[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLLTList:
			if bkg!=ddbkgLLTList[0]: hddbkgLLT[isEM].Add(bkghists[histoPrefix+'_'+bkg])

		for bkg in ddbkgLLLList:
			if bkg!=ddbkgLLLList[0]: hddbkgLLL[isEM].Add(bkghists[histoPrefix+'_'+bkg])

		
		#Group QCD processes
# 		hqcd[isEM] = bkghists[histoPrefix+'_'+qcdList[0]].Clone(histoPrefix+'__qcd')
# 		for bkg in qcdList: 
# 			if bkg!=qcdList[0]: hqcd[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		
		#Group EWK processes
		hewk[isEM] = bkghists[histoPrefix+'_'+ewkList[0]].Clone(histoPrefix+'__ewk')
		for bkg in ewkList:
			if bkg!=ewkList[0]: hewk[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		
		#Group TOP processes
		htop[isEM] = bkghists[histoPrefix+'_'+topList[0]].Clone(histoPrefix+'__top')
		for bkg in topList:
			if bkg!=topList[0]: htop[isEM].Add(bkghists[histoPrefix+'_'+bkg])
		
		#get signal
		for signal in sigList.keys(): hsig[isEM+signal] = sighists[histoPrefix+'_'+signal].Clone(histoPrefix+'__'+sigList[signal])
		#get total signal
		for signal in signals: 
			hsig[isEM+signal] = sighists[histoPrefix+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal)
			for decay in decays: 
				if decay!=decays[0]: hsig[isEM+signal].Add(sighists[histoPrefix+'_'+signal+decay])

		#systematics
		if doAllSys:
			for systematic in systematicList:
				if systematic=='pdfNew' or systematic=='muRFcorrdNew' or systematic=='muRFdecorrdNew': continue
				for ud in ['Up','Down']:
					if not(systematic=='toppt' or 'PR' in systematic or 'FR' in systematic):
# 						hqcd[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hewk[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hvv[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+vvList[0]].Clone(histoPrefix+'__VV__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hwz[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+wzList[0]].Clone(histoPrefix+'__WZ__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hzz[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+zzList[0]].Clone(histoPrefix+'__ZZ__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						hvvv[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+vvvList[0]].Clone(histoPrefix+'__VVV__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						httv[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ttvList[0]].Clone(histoPrefix+'__TTV__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						htop[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+topList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for signal in sigList.keys(): hsig[isEM+signal+systematic+ud] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal].Clone(histoPrefix+'__'+sigList[signal]+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for signal in signals: 
							hsig[isEM+signal+systematic+ud] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
							for decay in decays: 
								if decay!=decays[0]: hsig[isEM+signal+systematic+ud].Add(sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decay])
# 						for bkg in qcdList: 
# 							if bkg!=qcdList[0]: hqcd[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in ewkList: 
							if bkg!=ewkList[0]: hewk[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in vvList: 
							if bkg!=vvList[0]: hvv[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in wzList: 
							if bkg!=wzList[0]: hwz[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in zzList: 
							if bkg!=zzList[0]: hzz[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in vvvList: 
							if bkg!=vvvList[0]: hvvv[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in ttvList: 
							if bkg!=ttvList[0]: httv[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in topList: 
							if bkg!=topList[0]: htop[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
					if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
						htop[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ttjetList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for bkg in ttjetList: 
							if bkg!=ttjetList[0]: htop[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
						for bkg in topList: 
							if bkg not in ttjetList: htop[isEM+systematic+ud].Add(bkghists[histoPrefix+'_'+bkg])
					if 'PR' in systematic or 'FR' in systematic: # PR and FR is only on the ddbkg sample, so it needs special treatment!
						hddbkg[isEM+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ddbkgList[0]].Clone(histoPrefix+'__ddbkg__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for bkg in ddbkgList: 
							if bkg!=ddbkgList[0]: hddbkg[isEM+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])

			htop[isEM+'muRFcorrdNewUp'] = htop[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFcorrdNew__plus')
			htop[isEM+'muRFcorrdNewDown'] = htop[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFcorrdNew__minus')
			hewk[isEM+'muRFcorrdNewUp'] = hewk[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFcorrdNew__plus')
			hewk[isEM+'muRFcorrdNewDown'] = hewk[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFcorrdNew__minus')
			hvv[isEM+'muRFcorrdNewUp'] = hvv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__VV__muRFcorrdNew__plus')
			hvv[isEM+'muRFcorrdNewDown'] = hvv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__VV__muRFcorrdNew__minus')
			hwz[isEM+'muRFcorrdNewUp'] = hwz[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__WZ__muRFcorrdNew__plus')
			hwz[isEM+'muRFcorrdNewDown'] = hwz[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__WZ__muRFcorrdNew__minus')
			hzz[isEM+'muRFcorrdNewUp'] = hzz[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ZZ__muRFcorrdNew__plus')
			hzz[isEM+'muRFcorrdNewDown'] = hzz[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ZZ__muRFcorrdNew__minus')
			hvvv[isEM+'muRFcorrdNewUp'] = hvvv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__VVV__muRFcorrdNew__plus')
			hvvv[isEM+'muRFcorrdNewDown'] = hvvv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__VVV__muRFcorrdNew__minus')
			httv[isEM+'muRFcorrdNewUp'] = httv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__TTV__muRFcorrdNew__plus')
			httv[isEM+'muRFcorrdNewDown'] = httv[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__TTV__muRFcorrdNew__minus')
			for signal in sigList.keys(): hsig[isEM+signal+'muRFcorrdNewUp'] = hsig[isEM+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFcorrdNew__plus')
			for signal in sigList.keys(): hsig[isEM+signal+'muRFcorrdNewDown'] = hsig[isEM+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFcorrdNew__minus')
			for signal in signals: 
				hsig[isEM+signal+'muRFcorrdNewUp'] = hsig[isEM+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFcorrdNew__plus')
				hsig[isEM+signal+'muRFcorrdNewDown'] = hsig[isEM+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFcorrdNew__minus')

			htop[isEM+'muRFdecorrdNewUp'] = htop[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFdecorrdNew__plus')
			htop[isEM+'muRFdecorrdNewDown'] = htop[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__top__muRFdecorrdNew__minus')
			hewk[isEM+'muRFdecorrdNewUp'] = hewk[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFdecorrdNew__plus')
			hewk[isEM+'muRFdecorrdNewDown'] = hewk[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__ewk__muRFdecorrdNew__minus')
# 			hqcd[isEM+'muRFdecorrdNewUp'] = hqcd[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFdecorrdNew__plus')
# 			hqcd[isEM+'muRFdecorrdNewDown'] = hqcd[isEM+'muRFcorrdUp'].Clone(histoPrefix+'__qcd__muRFdecorrdNew__minus')
			for signal in sigList.keys(): hsig[isEM+signal+'muRFdecorrdNewUp'] = hsig[isEM+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFdecorrdNew__plus')
			for signal in sigList.keys(): hsig[isEM+signal+'muRFdecorrdNewDown'] = hsig[isEM+signal+'muRFcorrdUp'].Clone(histoPrefix+'__'+sigList[signal]+'__muRFdecorrdNew__minus')
			for signal in signals: 
				hsig[isEM+signal+'muRFdecorrdNewUp'] = hsig[isEM+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFdecorrdNew__plus')
				hsig[isEM+signal+'muRFdecorrdNewDown'] = hsig[isEM+signal+decays[0]+'muRFcorrdUp'].Clone(histoPrefix+'__'+signal+'__muRFdecorrdNew__minus')

			# nominal,renormWeights[4],renormWeights[2],renormWeights[1],renormWeights[0],renormWeights[5],renormWeights[3]
			histPrefixList = ['','muRUp','muRDown','muFUp','muFDown','muRFcorrdUp','muRFcorrdDown']
			for ibin in range(1,htop[isEM].GetNbinsX()+1):
				weightListTop = [htop[isEM+item].GetBinContent(ibin) for item in histPrefixList]	
				#for item in histPrefixList:print 'htop[', isEM, item, '].GetBinContent(', ibin, ')', htop[isEM+item].GetBinContent(ibin)
				weightListEwk = [hewk[isEM+item].GetBinContent(ibin) for item in histPrefixList]	
				weightListTTV = [httv[isEM+item].GetBinContent(ibin) for item in histPrefixList]	
# 				weightListQcd = [hqcd[isEM+item].GetBinContent(ibin) for item in histPrefixList]	
				weightListSig = {}
				for signal in sigList.keys()+signals: weightListSig[signal] = [hsig[isEM+signal+item].GetBinContent(ibin) for item in histPrefixList]
				indTopRFcorrdUp = weightListTop.index(max(weightListTop))
				#print '----> ibin:,',ibin,'max(weightListTop):',max(weightListTop) #CONTINUE HERE MARCH17-2017!!
				indTopRFcorrdDn = weightListTop.index(min(weightListTop))
				indEwkRFcorrdUp = weightListEwk.index(max(weightListEwk))
				indEwkRFcorrdDn = weightListEwk.index(min(weightListEwk))
				indTTVRFcorrdUp = weightListTTV.index(max(weightListTTV))
				indTTVRFcorrdDn = weightListTTV.index(min(weightListTTV))
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
				
				htop[isEM+'muRFcorrdNewUp'].SetBinContent(ibin,htop[isEM+histPrefixList[indTopRFcorrdUp]].GetBinContent(ibin))
				htop[isEM+'muRFcorrdNewDown'].SetBinContent(ibin,htop[isEM+histPrefixList[indTopRFcorrdDn]].GetBinContent(ibin))
				hewk[isEM+'muRFcorrdNewUp'].SetBinContent(ibin,hewk[isEM+histPrefixList[indEwkRFcorrdUp]].GetBinContent(ibin))
				hewk[isEM+'muRFcorrdNewDown'].SetBinContent(ibin,hewk[isEM+histPrefixList[indEwkRFcorrdDn]].GetBinContent(ibin))
				httv[isEM+'muRFcorrdNewUp'].SetBinContent(ibin,httv[isEM+histPrefixList[indTTVRFcorrdUp]].GetBinContent(ibin))
				httv[isEM+'muRFcorrdNewDown'].SetBinContent(ibin,httv[isEM+histPrefixList[indTTVRFcorrdDn]].GetBinContent(ibin))
# 				hqcd[isEM+'muRFcorrdNewUp'].SetBinContent(ibin,hqcd[isEM+histPrefixList[indQcdRFcorrdUp]].GetBinContent(ibin))
# 				hqcd[isEM+'muRFcorrdNewDown'].SetBinContent(ibin,hqcd[isEM+histPrefixList[indQcdRFcorrdDn]].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'muRFcorrdNewUp'].SetBinContent(ibin,hsig[isEM+signal+histPrefixList[indSigRFcorrdUp[signal]]].GetBinContent(ibin))
					hsig[isEM+signal+'muRFcorrdNewDown'].SetBinContent(ibin,hsig[isEM+signal+histPrefixList[indSigRFcorrdDn[signal]]].GetBinContent(ibin))
				htop[isEM+'muRFdecorrdNewUp'].SetBinContent(ibin,htop[isEM+histPrefixList[indTopRFdecorrdUp]].GetBinContent(ibin))
				htop[isEM+'muRFdecorrdNewDown'].SetBinContent(ibin,htop[isEM+histPrefixList[indTopRFdecorrdDn]].GetBinContent(ibin))
				hewk[isEM+'muRFdecorrdNewUp'].SetBinContent(ibin,hewk[isEM+histPrefixList[indEwkRFdecorrdUp]].GetBinContent(ibin))
				hewk[isEM+'muRFdecorrdNewDown'].SetBinContent(ibin,hewk[isEM+histPrefixList[indEwkRFdecorrdDn]].GetBinContent(ibin))
# 				hqcd[isEM+'muRFdecorrdNewUp'].SetBinContent(ibin,hqcd[isEM+histPrefixList[indQcdRFdecorrdUp]].GetBinContent(ibin))
# 				hqcd[isEM+'muRFdecorrdNewDown'].SetBinContent(ibin,hqcd[isEM+histPrefixList[indQcdRFdecorrdDn]].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'muRFdecorrdNewUp'].SetBinContent(ibin,hsig[isEM+signal+histPrefixList[indSigRFdecorrdUp[signal]]].GetBinContent(ibin))
					hsig[isEM+signal+'muRFdecorrdNewDown'].SetBinContent(ibin,hsig[isEM+signal+histPrefixList[indSigRFdecorrdDn[signal]]].GetBinContent(ibin))

				htop[isEM+'muRFcorrdNewUp'].SetBinError(ibin,htop[isEM+histPrefixList[indTopRFcorrdUp]].GetBinError(ibin))
				htop[isEM+'muRFcorrdNewDown'].SetBinError(ibin,htop[isEM+histPrefixList[indTopRFcorrdDn]].GetBinError(ibin))
				hewk[isEM+'muRFcorrdNewUp'].SetBinError(ibin,hewk[isEM+histPrefixList[indEwkRFcorrdUp]].GetBinError(ibin))
				hewk[isEM+'muRFcorrdNewDown'].SetBinError(ibin,hewk[isEM+histPrefixList[indEwkRFcorrdDn]].GetBinError(ibin))
				httv[isEM+'muRFcorrdNewUp'].SetBinError(ibin,httv[isEM+histPrefixList[indTTVRFcorrdUp]].GetBinError(ibin))
				httv[isEM+'muRFcorrdNewDown'].SetBinError(ibin,httv[isEM+histPrefixList[indTTVRFcorrdDn]].GetBinError(ibin))
# 				hqcd[isEM+'muRFcorrdNewUp'].SetBinError(ibin,hqcd[isEM+histPrefixList[indQcdRFcorrdUp]].GetBinError(ibin))
# 				hqcd[isEM+'muRFcorrdNewDown'].SetBinError(ibin,hqcd[isEM+histPrefixList[indQcdRFcorrdDn]].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'muRFcorrdNewUp'].SetBinError(ibin,hsig[isEM+signal+histPrefixList[indSigRFcorrdUp[signal]]].GetBinError(ibin))
					hsig[isEM+signal+'muRFcorrdNewDown'].SetBinError(ibin,hsig[isEM+signal+histPrefixList[indSigRFcorrdDn[signal]]].GetBinError(ibin))
				htop[isEM+'muRFdecorrdNewUp'].SetBinError(ibin,htop[isEM+histPrefixList[indTopRFdecorrdUp]].GetBinError(ibin))
				htop[isEM+'muRFdecorrdNewDown'].SetBinError(ibin,htop[isEM+histPrefixList[indTopRFdecorrdDn]].GetBinError(ibin))
				hewk[isEM+'muRFdecorrdNewUp'].SetBinError(ibin,hewk[isEM+histPrefixList[indEwkRFdecorrdUp]].GetBinError(ibin))
				hewk[isEM+'muRFdecorrdNewDown'].SetBinError(ibin,hewk[isEM+histPrefixList[indEwkRFdecorrdDn]].GetBinError(ibin))
# 				hqcd[isEM+'muRFdecorrdNewUp'].SetBinError(ibin,hqcd[isEM+histPrefixList[indQcdRFdecorrdUp]].GetBinError(ibin))
# 				hqcd[isEM+'muRFdecorrdNewDown'].SetBinError(ibin,hqcd[isEM+histPrefixList[indQcdRFdecorrdDn]].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'muRFdecorrdNewUp'].SetBinError(ibin,hsig[isEM+signal+histPrefixList[indSigRFdecorrdUp[signal]]].GetBinError(ibin))
					hsig[isEM+signal+'muRFdecorrdNewDown'].SetBinError(ibin,hsig[isEM+signal+histPrefixList[indSigRFdecorrdDn[signal]]].GetBinError(ibin))

			#SF from Julie /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/makeTemplates/modifyBinning.py (April 7, 2017)
			muSFsUp = {'TTM800':0.750,'TTM900':0.750,'TTM1000':0.749,'TTM1100':0.749,'TTM1200':0.748,'TTM1300':0.747,'TTM1400':0.746,'TTM1500':0.745,'TTM1600':0.744,'TTM1700':0.743,'TTM1800':0.741}
			muSFsDn = {'TTM800':1.303,'TTM900':1.303,'TTM1000':1.304,'TTM1100':1.305,'TTM1200':1.307,'TTM1300':1.309,'TTM1400':1.311,'TTM1500':1.313,'TTM1600':1.315,'TTM1700':1.317,'TTM1800':1.319}
			if whichSignal == 'BB':
				muSFsUp = {'BBM800':0.750,'BBM900':0.750,'BBM1000':0.749,'BBM1100':0.749,'BBM1200':0.748,'BBM1300':0.747,'BBM1400':0.746,'BBM1500':0.745,'BBM1600':0.744,'BBM1700':0.743,'BBM1800':0.741}
				muSFsDn = {'BBM800':1.303,'BBM900':1.303,'BBM1000':1.304,'BBM1100':1.305,'BBM1200':1.307,'BBM1300':1.309,'BBM1400':1.310,'BBM1500':1.313,'BBM1600':1.315,'BBM1700':1.317,'BBM1800':1.319}					
			for signal in sigList.keys()+signals: 
				if signal[-1]!='0':#exclude decay str
					scalefactorUp = muSFsUp[signal[:-4]]
					scalefactorDn = muSFsDn[signal[:-4]]
				else:
					scalefactorUp = muSFsUp[signal]
					scalefactorDn = muSFsDn[signal]				
				if(DEBUG): print 'pre SF : hsig[',isEM,signal,'muRFcorrdNewUp].Integral() =', hsig[isEM+signal+'muRFcorrdNewUp'].Integral()
				if(DEBUG): print 'pre SF : hsig[',isEM,signal,'muRFcorrdNewDown].Integral() =', hsig[isEM+signal+'muRFcorrdNewDown'].Integral()
				if(DEBUG): print 'Mass',signal,': assigning muRFcoordNew SFup =',scalefactorUp,', SFdn =',scalefactorDn                                                                                                                          
				hsig[isEM+signal+'muRFcorrdNewUp'].Scale(scalefactorUp)
				hsig[isEM+signal+'muRFcorrdNewDown'].Scale(scalefactorDn)
				if(DEBUG): print 'post SF : hsig[',isEM,signal,'muRFcorrdNewUp].Integral() =', hsig[isEM+signal+'muRFcorrdNewUp'].Integral()
				if(DEBUG): print 'post SF : hsig[',isEM,signal,'muRFcorrdNewDown].Integral() =', hsig[isEM+signal+'muRFcorrdNewDown'].Integral()

			for pdfInd in range(100):
# 				hqcd[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__pdf'+str(pdfInd))
				hewk[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__pdf'+str(pdfInd))
				hvv[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+vvList[0]].Clone(histoPrefix+'__VV__pdf'+str(pdfInd))
				hwz[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+wzList[0]].Clone(histoPrefix+'__WZ__pdf'+str(pdfInd))
				hzz[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+zzList[0]].Clone(histoPrefix+'__ZZ__pdf'+str(pdfInd))
				hvvv[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+vvvList[0]].Clone(histoPrefix+'__VVV__pdf'+str(pdfInd))
				httv[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+ttvList[0]].Clone(histoPrefix+'__TTV__pdf'+str(pdfInd))
				htop[isEM+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+topList[0]].Clone(histoPrefix+'__top__pdf'+str(pdfInd))
				for signal in sigList.keys(): hsig[isEM+signal+'pdf'+str(pdfInd)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal].Clone(histoPrefix+'__'+signal+'__pdf'+str(pdfInd))
				for signal in signals: 
					hsig[isEM+signal+'pdf'+str(pdfInd)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decays[0]].Clone(histoPrefix+'__'+signal+'__pdf'+str(pdfInd))
					for decay in decays: 
						if decay!=decays[0]: hsig[isEM+signal+'pdf'+str(pdfInd)].Add(sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decay])
# 				for bkg in qcdList: 
# 					if bkg!=qcdList[0]: hqcd[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in ewkList: 
					if bkg!=ewkList[0]: hewk[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in vvList: 
					if bkg!=vvList[0]: hvv[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in wzList: 
					if bkg!=wzList[0]: hwz[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in zzList: 
					if bkg!=zzList[0]: hzz[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in vvvList: 
					if bkg!=vvvList[0]: hvvv[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in ttvList: 
					if bkg!=ttvList[0]: httv[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
				for bkg in topList: 
					if bkg!=topList[0]: htop[isEM+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
			htop[isEM+'pdfNewUp'] = htop[isEM+'pdf0'].Clone(histoPrefix+'__top__pdfNew__plus')
			htop[isEM+'pdfNewDown'] = htop[isEM+'pdf0'].Clone(histoPrefix+'__top__pdfNew__minus')
			hewk[isEM+'pdfNewUp'] = hewk[isEM+'pdf0'].Clone(histoPrefix+'__ewk__pdfNew__plus')
			hewk[isEM+'pdfNewDown'] = hewk[isEM+'pdf0'].Clone(histoPrefix+'__ewk__pdfNew__minus')
			hvv[isEM+'pdfNewUp'] = hvv[isEM+'pdf0'].Clone(histoPrefix+'__VV__pdfNew__plus')
			hvv[isEM+'pdfNewDown'] = hvv[isEM+'pdf0'].Clone(histoPrefix+'__VV__pdfNew__minus')
			hwz[isEM+'pdfNewUp'] = hwz[isEM+'pdf0'].Clone(histoPrefix+'__WZ__pdfNew__plus')
			hwz[isEM+'pdfNewDown'] = hwz[isEM+'pdf0'].Clone(histoPrefix+'__WZ__pdfNew__minus')
			hzz[isEM+'pdfNewUp'] = hzz[isEM+'pdf0'].Clone(histoPrefix+'__ZZ__pdfNew__plus')
			hzz[isEM+'pdfNewDown'] = hzz[isEM+'pdf0'].Clone(histoPrefix+'__ZZ__pdfNew__minus')
			hvvv[isEM+'pdfNewUp'] = hvvv[isEM+'pdf0'].Clone(histoPrefix+'__VVV__pdfNew__plus')
			hvvv[isEM+'pdfNewDown'] = hvvv[isEM+'pdf0'].Clone(histoPrefix+'__VVV__pdfNew__minus')
			httv[isEM+'pdfNewUp'] = httv[isEM+'pdf0'].Clone(histoPrefix+'__TTV__pdfNew__plus')
			httv[isEM+'pdfNewDown'] = httv[isEM+'pdf0'].Clone(histoPrefix+'__TTV__pdfNew__minus')
# 			hqcd[isEM+'pdfNewUp'] = hqcd[isEM+'pdf0'].Clone(histoPrefix+'__qcd__pdfNew__plus')
# 			hqcd[isEM+'pdfNewDown'] = hqcd[isEM+'pdf0'].Clone(histoPrefix+'__qcd__pdfNew__minus')
			for signal in sigList.keys(): hsig[isEM+signal+'pdfNewUp'] = hsig[isEM+signal+'pdf0'].Clone(histoPrefix+'__'+sigList[signal]+'__pdfNew__plus')
			for signal in sigList.keys(): hsig[isEM+signal+'pdfNewDown'] = hsig[isEM+signal+'pdf0'].Clone(histoPrefix+'__'+sigList[signal]+'__pdfNew__minus')
			for signal in signals: 
				hsig[isEM+signal+'pdfNewUp'] = hsig[isEM+signal+decays[0]+'pdf0'].Clone(histoPrefix+'__'+signal+'__pdfNew__plus')
				hsig[isEM+signal+'pdfNewDown'] = hsig[isEM+signal+decays[0]+'pdf0'].Clone(histoPrefix+'__'+signal+'__pdfNew__minus')
			for ibin in range(1,htop[isEM+'pdfNewUp'].GetNbinsX()+1):
				weightListTop = [htop[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListEwk = [hewk[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListVV = [hvv[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListWZ = [hwz[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListZZ = [hzz[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListVVV = [hvvv[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListTTV = [httv[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
# 				weightListQcd = [hqcd[isEM+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				weightListSig = {}
				for signal in sigList.keys()+signals: weightListSig[signal] = [hsig[isEM+signal+'pdf'+str(pdfInd)].GetBinContent(ibin) for pdfInd in range(100)]
				indTopPDFUp = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[83]
				indTopPDFDn = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[15]
				indEwkPDFUp = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[83]
				indEwkPDFDn = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[15]
				indVVPDFUp = sorted(range(len(weightListVV)), key=lambda k: weightListVV[k])[83]
				indVVPDFDn = sorted(range(len(weightListVV)), key=lambda k: weightListVV[k])[15]
				indWZPDFUp = sorted(range(len(weightListWZ)), key=lambda k: weightListWZ[k])[83]
				indWZPDFDn = sorted(range(len(weightListWZ)), key=lambda k: weightListWZ[k])[15]
				indZZPDFUp = sorted(range(len(weightListZZ)), key=lambda k: weightListZZ[k])[83]
				indZZPDFDn = sorted(range(len(weightListZZ)), key=lambda k: weightListZZ[k])[15]
				indVVVPDFUp = sorted(range(len(weightListVVV)), key=lambda k: weightListVVV[k])[83]
				indVVVPDFDn = sorted(range(len(weightListVVV)), key=lambda k: weightListVVV[k])[15]
				indTTVPDFUp = sorted(range(len(weightListTTV)), key=lambda k: weightListTTV[k])[83]
				indTTVPDFDn = sorted(range(len(weightListTTV)), key=lambda k: weightListTTV[k])[15]
# 				indQcdPDFUp = sorted(range(len(weightListQcd)), key=lambda k: weightListQcd[k])[83]
# 				indQcdPDFDn = sorted(range(len(weightListQcd)), key=lambda k: weightListQcd[k])[15]
				indSigPDFUp = {}
				indSigPDFDn = {}
				for signal in sigList.keys()+signals: 
					indSigPDFUp[signal] = sorted(range(len(weightListSig[signal])), key=lambda k: weightListSig[signal][k])[83]
					indSigPDFDn[signal] = sorted(range(len(weightListSig[signal])), key=lambda k: weightListSig[signal][k])[15]
				
				htop[isEM+'pdfNewUp'].SetBinContent(ibin,htop[isEM+'pdf'+str(indTopPDFUp)].GetBinContent(ibin))
				htop[isEM+'pdfNewDown'].SetBinContent(ibin,htop[isEM+'pdf'+str(indTopPDFDn)].GetBinContent(ibin))
				hewk[isEM+'pdfNewUp'].SetBinContent(ibin,hewk[isEM+'pdf'+str(indEwkPDFUp)].GetBinContent(ibin))
				hewk[isEM+'pdfNewDown'].SetBinContent(ibin,hewk[isEM+'pdf'+str(indEwkPDFDn)].GetBinContent(ibin))
				hvv[isEM+'pdfNewUp'].SetBinContent(ibin,hvv[isEM+'pdf'+str(indVVPDFUp)].GetBinContent(ibin))
				hvv[isEM+'pdfNewDown'].SetBinContent(ibin,hvv[isEM+'pdf'+str(indVVPDFDn)].GetBinContent(ibin))
				hwz[isEM+'pdfNewUp'].SetBinContent(ibin,hwz[isEM+'pdf'+str(indWZPDFUp)].GetBinContent(ibin))
				hwz[isEM+'pdfNewDown'].SetBinContent(ibin,hwz[isEM+'pdf'+str(indWZPDFDn)].GetBinContent(ibin))
				hzz[isEM+'pdfNewUp'].SetBinContent(ibin,hzz[isEM+'pdf'+str(indZZPDFUp)].GetBinContent(ibin))
				hzz[isEM+'pdfNewDown'].SetBinContent(ibin,hzz[isEM+'pdf'+str(indZZPDFDn)].GetBinContent(ibin))
				hvvv[isEM+'pdfNewUp'].SetBinContent(ibin,hvvv[isEM+'pdf'+str(indVVVPDFUp)].GetBinContent(ibin))
				hvvv[isEM+'pdfNewDown'].SetBinContent(ibin,hvvv[isEM+'pdf'+str(indVVVPDFDn)].GetBinContent(ibin))
				httv[isEM+'pdfNewUp'].SetBinContent(ibin,httv[isEM+'pdf'+str(indTTVPDFUp)].GetBinContent(ibin))
				httv[isEM+'pdfNewDown'].SetBinContent(ibin,httv[isEM+'pdf'+str(indTTVPDFDn)].GetBinContent(ibin))
# 				hqcd[isEM+'pdfNewUp'].SetBinContent(ibin,hqcd[isEM+'pdf'+str(indQcdPDFUp)].GetBinContent(ibin))
# 				hqcd[isEM+'pdfNewDown'].SetBinContent(ibin,hqcd[isEM+'pdf'+str(indQcdPDFDn)].GetBinContent(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'pdfNewUp'].SetBinContent(ibin,hsig[isEM+signal+'pdf'+str(indSigPDFUp[signal])].GetBinContent(ibin))
					hsig[isEM+signal+'pdfNewDown'].SetBinContent(ibin,hsig[isEM+signal+'pdf'+str(indSigPDFDn[signal])].GetBinContent(ibin))

				htop[isEM+'pdfNewUp'].SetBinError(ibin,htop[isEM+'pdf'+str(indTopPDFUp)].GetBinError(ibin))
				htop[isEM+'pdfNewDown'].SetBinError(ibin,htop[isEM+'pdf'+str(indTopPDFDn)].GetBinError(ibin))
				hewk[isEM+'pdfNewUp'].SetBinError(ibin,hewk[isEM+'pdf'+str(indEwkPDFUp)].GetBinError(ibin))
				hewk[isEM+'pdfNewDown'].SetBinError(ibin,hewk[isEM+'pdf'+str(indEwkPDFDn)].GetBinError(ibin))
				hvv[isEM+'pdfNewUp'].SetBinError(ibin,hvv[isEM+'pdf'+str(indVVPDFUp)].GetBinError(ibin))
				hvv[isEM+'pdfNewDown'].SetBinError(ibin,hvv[isEM+'pdf'+str(indVVPDFDn)].GetBinError(ibin))
				hwz[isEM+'pdfNewUp'].SetBinError(ibin,hwz[isEM+'pdf'+str(indWZPDFUp)].GetBinError(ibin))
				hwz[isEM+'pdfNewDown'].SetBinError(ibin,hwz[isEM+'pdf'+str(indWZPDFDn)].GetBinError(ibin))
				hzz[isEM+'pdfNewUp'].SetBinError(ibin,hzz[isEM+'pdf'+str(indZZPDFUp)].GetBinError(ibin))
				hzz[isEM+'pdfNewDown'].SetBinError(ibin,hzz[isEM+'pdf'+str(indZZPDFDn)].GetBinError(ibin))
				hvvv[isEM+'pdfNewUp'].SetBinError(ibin,hvvv[isEM+'pdf'+str(indVVVPDFUp)].GetBinError(ibin))
				hvvv[isEM+'pdfNewDown'].SetBinError(ibin,hvvv[isEM+'pdf'+str(indVVVPDFDn)].GetBinError(ibin))
				httv[isEM+'pdfNewUp'].SetBinError(ibin,httv[isEM+'pdf'+str(indTTVPDFUp)].GetBinError(ibin))
				httv[isEM+'pdfNewDown'].SetBinError(ibin,httv[isEM+'pdf'+str(indTTVPDFDn)].GetBinError(ibin))
# 				hqcd[isEM+'pdfNewUp'].SetBinError(ibin,hqcd[isEM+'pdf'+str(indQcdPDFUp)].GetBinError(ibin))
# 				hqcd[isEM+'pdfNewDown'].SetBinError(ibin,hqcd[isEM+'pdf'+str(indQcdPDFDn)].GetBinError(ibin))
				for signal in sigList.keys()+signals: 
					hsig[isEM+signal+'pdfNewUp'].SetBinError(ibin,hsig[isEM+signal+'pdf'+str(indSigPDFUp[signal])].GetBinError(ibin))
					hsig[isEM+signal+'pdfNewDown'].SetBinError(ibin,hsig[isEM+signal+'pdf'+str(indSigPDFDn[signal])].GetBinError(ibin))

			#SF from Julie /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/makeTemplates/modifyBinning.py (April 7, 2017)
			pdfSFsUp = {'TTM800':0.908,'TTM900':0.902,'TTM1000':0.890,'TTM1100':0.889,'TTM1200':0.895,'TTM1300':0.895,'TTM1400':0.888,'TTM1500':0.897,'TTM1600':0.905,'TTM1700':0.885,'TTM1800':0.872}
			pdfSFsDn = {'TTM800':1.106,'TTM900':1.104,'TTM1000':1.099,'TTM1100':1.099,'TTM1200':1.093,'TTM1300':1.098,'TTM1400':1.102,'TTM1500':1.099,'TTM1600':1.122,'TTM1700':1.121,'TTM1800':1.133}
			if whichSignal == 'BB':
					pdfSFsUp = {'BBM800':0.909,'BBM900':0.903,'BBM1000':0.889,'BBM1100':0.889,'BBM1200':0.895,'BBM1300':0.895,'BBM1400':0.889,'BBM1500':0.897,'BBM1600':0.904,'BBM1700':0.884,'BBM1800':0.872}
					pdfSFsDn = {'BBM800':1.106,'BBM900':1.104,'BBM1000':1.100,'BBM1100':1.099,'BBM1200':1.093,'BBM1300':1.097,'BBM1400':1.102,'BBM1500':1.099,'BBM1600':1.121,'BBM1700':1.122,'BBM1800':1.132}
			for signal in sigList.keys()+signals: 
					if signal[-1]!='0': #exclude decay str
						scalefactorUp = pdfSFsUp[signal[:-4]]
						scalefactorDn = pdfSFsDn[signal[:-4]]
					else:
						scalefactorUp = pdfSFsUp[signal]
						scalefactorDn = pdfSFsDn[signal]					
					if(DEBUG): print 'pre SF : hsig[',isEM,signal,'pdfNewUp] =', hsig[isEM+signal+'pdfNewUp'].Integral()
					if(DEBUG): print 'pre SF : hsig[',isEM,signal,'pdfNewDown].Integral() =', hsig[isEM+signal+'pdfNewDown'].Integral()
					if(DEBUG): print 'Mass',signal,': assigning pdfNew SFup =',scalefactorUp,', SFdn =',scalefactorDn                                                                                                                          
					hsig[isEM+signal+'pdfNewUp'].Scale(scalefactorUp)
					hsig[isEM+signal+'pdfNewDown'].Scale(scalefactorDn)
					if(DEBUG): print 'post SF : hsig[',isEM,signal,'pdfNewUp].Integral() =', hsig[isEM+signal+'pdfNewUp'].Integral()
					if(DEBUG): print 'post SF : hsig[',isEM,signal,'pdfNewDown].Integral() =', hsig[isEM+signal+'pdfNewDown'].Integral()
		
		#Group data processes
		hdata[isEM] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
		for dat in dataList:
			if dat!=dataList[0]: hdata[isEM].Add(datahists[histoPrefix+'_'+dat])

		#prepare yield table

		yieldTable[histoPrefix]['top']    = htop[isEM].Integral()
		yieldTable[histoPrefix]['ewk']    = hewk[isEM].Integral()
# 		yieldTable[histoPrefix]['qcd']    = hqcd[isEM].Integral()
# 		yieldTable[histoPrefix]['totBkg'] = htop[isEM].Integral()+hewk[isEM].Integral()+hqcd[isEM].Integral()+hddbkg[isEM].Integral()
		yieldTable[histoPrefix]['totBkg'] = htop[isEM].Integral()+hewk[isEM].Integral()+hddbkg[isEM].Integral()
		yieldTable[histoPrefix]['data']   = hdata[isEM].Integral()
		for signal in sigList.keys(): yieldTable[histoPrefix][signal] = hsig[isEM+signal].Integral()
		for signal in signals: yieldTable[histoPrefix][signal] = hsig[isEM+signal].Integral()
		if yieldTable[histoPrefix]['totBkg']!=0:
			yieldTable[histoPrefix]['dataOverBkg']= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
			for signal in signals: yieldTable[histoPrefix][signal+'OverSqrtBkg'] = yieldTable[histoPrefix][signal]/math.sqrt(yieldTable[histoPrefix]['totBkg'])
		else:
			yieldTable[histoPrefix]['dataOverBkg']= 0.
			for signal in signals: yieldTable[histoPrefix][signal+'OverSqrtBkg'] = 0.
# 		yieldTable[histoPrefix]['WJets']  = hwjets[isEM].Integral()
# 		yieldTable[histoPrefix]['ZJets']  = hzjets[isEM].Integral()
		yieldTable[histoPrefix]['VV']     = hvv[isEM].Integral()
		yieldTable[histoPrefix]['WZ']     = hwz[isEM].Integral()
		yieldTable[histoPrefix]['ZZ']     = hzz[isEM].Integral()
		yieldTable[histoPrefix]['VVV']    = hvvv[isEM].Integral()
		yieldTable[histoPrefix]['TTV']    = httv[isEM].Integral()
# 		yieldTable[histoPrefix]['TTJets'] = httjets[isEM].Integral()
# 		yieldTable[histoPrefix]['T']      = ht[isEM].Integral()
# 		yieldTable[histoPrefix]['QCD']    = hqcd[isEM].Integral()
		yieldTable[histoPrefix]['ddbkg']  = hddbkg[isEM].Integral()

# 		print ''
# 		print '----------', isEM,'----------'

		yieldTable[histoPrefix]['ddbkgTTT']  = hddbkgTTT[isEM].Integral()
# 		print 'hddbkgTTT[isEM].Integral() = ', hddbkgTTT[isEM].Integral()
# 		print ''

		yieldTable[histoPrefix]['ddbkgTTL']  = hddbkgTTL[isEM].Integral()
# 		print 'hddbkgTTL[isEM].Integral() = ', hddbkgTTL[isEM].Integral()
		yieldTable[histoPrefix]['ddbkgTLT']  = hddbkgTLT[isEM].Integral()
# 		print 'hddbkgTLT[isEM].Integral() = ', hddbkgTLT[isEM].Integral()
		yieldTable[histoPrefix]['ddbkgLTT']  = hddbkgLTT[isEM].Integral()
# 		print 'hddbkgLTT[isEM].Integral() = ', hddbkgLTT[isEM].Integral()
# 		print ''

		yieldTable[histoPrefix]['ddbkgTLL']  = hddbkgTLL[isEM].Integral()
# 		print 'hddbkgTLL[isEM].Integral() = ', hddbkgTLL[isEM].Integral()
		yieldTable[histoPrefix]['ddbkgLTL']  = hddbkgLTL[isEM].Integral()
# 		print 'hddbkgLTL[isEM].Integral() = ', hddbkgLTL[isEM].Integral()
		yieldTable[histoPrefix]['ddbkgLLT']  = hddbkgLLT[isEM].Integral()
# 		print 'hddbkgLLT[isEM].Integral() = ', hddbkgLLT[isEM].Integral()
# 		print ''

		yieldTable[histoPrefix]['ddbkgLLL']  = hddbkgLLL[isEM].Integral()
# 		print 'hddbkgLLL[isEM].Integral() = ', hddbkgLLL[isEM].Integral()
		
		#+/- 1sigma variations of shape systematics
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					if not('PR' in systematic or 'FR' in systematic):
						yieldTable[histoPrefix+systematic+ud]['top'] = htop[isEM+systematic+ud].Integral()
						if systematic!='toppt':
							yieldTable[histoPrefix+systematic+ud]['ewk'] = hewk[isEM+systematic+ud].Integral()
							yieldTable[histoPrefix+systematic+ud]['VV'] = hvv[isEM+systematic+ud].Integral()
							yieldTable[histoPrefix+systematic+ud]['WZ'] = hwz[isEM+systematic+ud].Integral()
							yieldTable[histoPrefix+systematic+ud]['ZZ'] = hzz[isEM+systematic+ud].Integral()
							yieldTable[histoPrefix+systematic+ud]['VVV'] = hvvv[isEM+systematic+ud].Integral()
							yieldTable[histoPrefix+systematic+ud]['TTV'] = httv[isEM+systematic+ud].Integral()
# 							yieldTable[histoPrefix+systematic+ud]['qcd'] = hqcd[isEM+systematic+ud].Integral()
							for signal in sigList.keys(): 
								if normalizeRENORM_PDF and (systematic=='pdfNew' or systematic=='muRFcorrdNew') and hsig[isEM+signal].Integral()>0:
									if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print 'Normalizing',signal, systematic ,'sys yield'
									if (DEBUG_normalizeRENORM_PDF): print 'hsig[',isEM+signal+systematic+ud,'].Integral()',hsig[isEM+signal+systematic+ud].Integral() , 'hsig[',isEM+signal,'].Integral() =', hsig[isEM+signal].Integral()
									yieldTable[histoPrefix+systematic+ud][signal] = hsig[isEM+signal].Integral() ##ATTENTION: IS THIS CORRECT??
								else:
									if (DEBUG_normalizeRENORM_PDF): print 'hsig[',isEM+signal+systematic+ud,'].Integral()',hsig[isEM+signal+systematic+ud].Integral() , 'hsig[',isEM+signal,'].Integral() =', hsig[isEM+signal].Integral()
									yieldTable[histoPrefix+systematic+ud][signal] = hsig[isEM+signal+systematic+ud].Integral()
							for signal in signals: 
								if normalizeRENORM_PDF and (systematic=='pdfNew' or systematic=='muRFcorrdNew') and hsig[isEM+signal].Integral()>0:
									if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print 'Normalizing',signal, systematic ,'sys yield'
									yieldTable[histoPrefix+systematic+ud][signal] = hsig[isEM+signal].Integral()  ##ATTENTION: IS THIS CORRECT??
								else:
									yieldTable[histoPrefix+systematic+ud][signal] = hsig[isEM+signal+systematic+ud].Integral()
					if 'PR' in systematic or 'FR' in systematic:
						yieldTable[histoPrefix+systematic+ud]['ddbkg'] = hddbkg[isEM+systematic+ud].Integral()

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

		for ibin in range(1,hsig[isEM+signal].GetXaxis().GetNbins()+1):
			yieldErrTable[histoPrefix]['top']    += htop[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ewk']    += hewk[isEM].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['qcd']    += hqcd[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['data']   += hdata[isEM].GetBinError(ibin)**2
# 			print "hdata[isEM].GetBinError(ibin) = ", hdata[isEM].Get/BinError(ibin)
# 			print "hdata[isEM].GetBinError(ibin)*hdata[isEM].GetBinError(ibin) = ", hdata[isEM].GetBinError(ibin)*hdata[isEM].GetBinError(ibin)
# 			print "yieldErrTable[histoPrefix]['data'] = ", yieldErrTable[histoPrefix]['data']
# 			yieldErrTable[histoPrefix]['WJets']  += hwjets[isEM].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['ZJets']  += hzjets[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['VV']     += hvv[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['WZ']     += hwz[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ZZ']     += hzz[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['VVV']    += hvvv[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['TTV']    += httv[isEM].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['TTJets'] += httjets[isEM].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['T']      += ht[isEM].GetBinError(ibin)**2
# 			yieldErrTable[histoPrefix]['QCD']    += hqcd[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkg']  += hddbkg[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTTT']  += hddbkgTTT[isEM].GetBinError(ibin)**2

			yieldErrTable[histoPrefix]['ddbkgTTL']  += hddbkgTTL[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTLT']  += hddbkgTLT[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTT']  += hddbkgLTT[isEM].GetBinError(ibin)**2

			yieldErrTable[histoPrefix]['ddbkgTLL']  += hddbkgTLL[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTL']  += hddbkgLTL[isEM].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLLT']  += hddbkgLLT[isEM].GetBinError(ibin)**2

			yieldErrTable[histoPrefix]['ddbkgLLL']  += hddbkgLLL[isEM].GetBinError(ibin)**2
			for signal in sigList.keys(): yieldErrTable[histoPrefix][signal] += hsig[isEM+signal].GetBinError(ibin)**2
			for signal in signals: yieldErrTable[histoPrefix][signal] += hsig[isEM+signal].GetBinError(ibin)**2
			
		if doAllSys: #MC with ONLY normCorrdSys, ddbkg with all ddbkgSys.

			if(DEBUG):print 'math.sqrt(yieldErrTable[histoPrefix][top]) (stat only)		:',math.sqrt(yieldErrTable[histoPrefix]['top'])
			yieldErrTable[histoPrefix]['top']    += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['top'])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2
			if(DEBUG):print 'getCorrdSysMC (',isEM,')*yieldTable[histoPrefix][top])		:', (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['top'])
			if(DEBUG):print 'math.sqrt(yieldErrTable[histoPrefix][top]) (stat+getCorrdSysMC)	:',math.sqrt(yieldErrTable[histoPrefix]['top'])
			if(DEBUG):print''
			if(DEBUG):print 'math.sqrt(yieldErrTable[histoPrefix][ewk]) (stat only)		:',math.sqrt(yieldErrTable[histoPrefix]['ewk'])
			yieldErrTable[histoPrefix]['ewk']    += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ewk'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2
			if(DEBUG):print 'getCorrdSysMC (',isEM,')*yieldTable[histoPrefix][ewk])		:', (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ewk'])
			if(DEBUG):print 'math.sqrt(yieldErrTable[histoPrefix][ewk]) (stat+getCorrdSysMC)	:',math.sqrt(yieldErrTable[histoPrefix]['ewk'])


	# 		yieldErrTable[histoPrefix]['qcd']    += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['qcd'])**2+(qcdXsecSys*yieldTable[histoPrefix]['qcd'])**2
	# 		yieldErrTable[histoPrefix]['WJets']  += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['WJets'])**2+(ewkXsecSys*yieldTable[histoPrefix]['WJets'])**2
	# 		yieldErrTable[histoPrefix]['ZJets']  += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ZJets'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ZJets'])**2
			yieldErrTable[histoPrefix]['VV']     += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['VV'])**2+(ewkXsecSys*yieldTable[histoPrefix]['VV'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
			yieldErrTable[histoPrefix]['WZ']     += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['WZ'])**2+(ewkXsecSys*yieldTable[histoPrefix]['WZ'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
			yieldErrTable[histoPrefix]['ZZ']     += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ZZ'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ZZ'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
			yieldErrTable[histoPrefix]['VVV']    += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['VVV'])**2+(ewkXsecSys*yieldTable[histoPrefix]['VVV'])**2	#ATTENTION! CHECK IF CORRECT CALCULATION!
			yieldErrTable[histoPrefix]['TTV']    += (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['TTV'])**2+(topXsecSys*yieldTable[histoPrefix]['TTV'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
			#if(DEBUG):print 'For TTV', histoPrefix,'yield err, adding getCorrdSysMC (',isEM,'):', (getCorrdSysMC(isEM)*yieldTable[histoPrefix]['TTV'])
	# 		yieldErrTable[histoPrefix]['TTJets'] += (corrdSys*yieldTable[histoPrefix]['TTJets'])**2+(topXsecSys*yieldTable[histoPrefix]['TTJets'])**2
	# 		yieldErrTable[histoPrefix]['T']      += (corrdSys*yieldTable[histoPrefix]['T'])**2+(topXsecSys*yieldTable[histoPrefix]['T'])**2
	# 		yieldErrTable[histoPrefix]['QCD']    += (corrdSys*yieldTable[histoPrefix]['QCD'])**2+(qcdXsecSys*yieldTable[histoPrefix]['qcd'])**2

			topErrSys=0.0
			ewkErrSys=0.0
			for systematic in ['pileup','btag','mistag','pdfNew','muRFcorrdNew','jec','jer']:
# 			for systematic in ['pileup','btag','pdfNew','muRFcorrdNew','jec','jer']:
				if(DEBUG):print 'For MC bkg', histoPrefix,'yield err, adding sys:', systematic
				yieldErrTable[histoPrefix]['top'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['top'] - yieldTable[histoPrefix]['top'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['top'] - yieldTable[histoPrefix]['top'] ) ) ) **2
				topErrSys += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['top'] - yieldTable[histoPrefix]['top'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['top'] - yieldTable[histoPrefix]['top'] ) ) ) **2
				if(DEBUG): print '									top',histoPrefix,systematic,'				:',( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['top'] - yieldTable[histoPrefix]['top'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['top'] - yieldTable[histoPrefix]['top'] ) ) )  
				if(DEBUG): print '									yieldErrTable[histoPrefix][top]   (SYS) after adding ',systematic,' 	:', math.sqrt(topErrSys+(getCorrdSysMC(isEM)*yieldTable[histoPrefix]['top'])**2)
				yieldErrTable[histoPrefix]['ewk'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ewk'] - yieldTable[histoPrefix]['ewk'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ewk'] - yieldTable[histoPrefix]['ewk'] ) ) ) **2
				ewkErrSys += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ewk'] - yieldTable[histoPrefix]['ewk'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ewk'] - yieldTable[histoPrefix]['ewk'] ) ) ) **2
				if(DEBUG): print '									ewk',histoPrefix,systematic,'				:',( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ewk'] - yieldTable[histoPrefix]['ewk'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ewk'] - yieldTable[histoPrefix]['ewk'] ) ) )  
				if(DEBUG): print '									yieldErrTable[histoPrefix][ewk]   (SYS) after adding ',systematic,' 	:', math.sqrt(ewkErrSys+(getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ewk'])**2)
				yieldErrTable[histoPrefix]['VV'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['VV'] - yieldTable[histoPrefix]['VV'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['VV'] - yieldTable[histoPrefix]['VV'] ) ) ) **2
				yieldErrTable[histoPrefix]['WZ'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['WZ'] - yieldTable[histoPrefix]['WZ'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['WZ'] - yieldTable[histoPrefix]['WZ'] ) ) ) **2
				yieldErrTable[histoPrefix]['ZZ'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ZZ'] - yieldTable[histoPrefix]['ZZ'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ZZ'] - yieldTable[histoPrefix]['ZZ'] ) ) ) **2
				yieldErrTable[histoPrefix]['VVV'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['VVV'] - yieldTable[histoPrefix]['VVV'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['VVV'] - yieldTable[histoPrefix]['VVV'] ) ) ) **2
				yieldErrTable[histoPrefix]['TTV'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['TTV'] - yieldTable[histoPrefix]['TTV'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['TTV'] - yieldTable[histoPrefix]['TTV'] ) ) ) **2
				#if(DEBUG): print '									TTV',histoPrefix,systematic,':',( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['TTV'] - yieldTable[histoPrefix]['TTV'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['TTV'] - yieldTable[histoPrefix]['TTV'] ) ) )  
			
			if(DEBUG):print 'ddbkg:'
			ddbkgErrStat = 0.0 #delete me after debug
			if(DEBUG):print '	math.sqrt(yieldErrTable[histoPrefix][ddbkg]) (stat only)			: ',math.sqrt(yieldErrTable[histoPrefix]['ddbkg'])
			ddbkgErrStat = yieldErrTable[histoPrefix]['ddbkg'] #delete me after debug
			yieldErrTable[histoPrefix]['ddbkg']    += (getCorrdSysDDBKG(isEM)*yieldTable[histoPrefix]['ddbkg'])**2 #ATTENTION! CHECK IF CORRECT CALCULATION!
			if(DEBUG):print '	getCorrdSysDDBKG (',isEM,')*yieldTable[histoPrefix][ddbkg])			: ', (getCorrdSysDDBKG(isEM)*yieldTable[histoPrefix]['ddbkg'])
			if(DEBUG):print '	math.sqrt(yieldErrTable[histoPrefix][ddbkg]) (stat+getCorrdSysDDBKG)		: ',math.sqrt(yieldErrTable[histoPrefix]['ddbkg'])
			ddbkgErrSys = 0.0
			for systematic in ['elPR','elFR','muPR','muFR']:
				if(DEBUG):print 'For ddbkg', histoPrefix,'yield err, adding sys:', systematic
				#if(DEBUG):print '									nominal        =', yieldTable[histoPrefix]['ddbkg']
				#if(DEBUG):print '									up - nominal   =', math.fabs( yieldTable[histoPrefix+systematic+'Up']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) 
				#if(DEBUG):print '									down - nominal =', math.fabs( yieldTable[histoPrefix+systematic+'Down']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) 
				yieldErrTable[histoPrefix]['ddbkg'] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) ) ) **2
				if(DEBUG):print '									sym error =', ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) ) )
				ddbkgErrSys += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down']['ddbkg'] - yieldTable[histoPrefix]['ddbkg'] ) ) ) **2
					
			yieldErrTable[histoPrefix]['totBkg'] += yieldErrTable[histoPrefix]['top'] + yieldErrTable[histoPrefix]['ewk'] + yieldErrTable[histoPrefix]['ddbkg']

			if(DEBUG):print ''
			#if(DEBUG):print '											yieldErrTable[histoPrefix][TTV]   (STAT+SYS) =	', math.sqrt(yieldErrTable[histoPrefix]['TTV'])
			if(DEBUG):print '											yieldErrTable[histoPrefix][top]   (SYS) 			=	', math.sqrt(topErrSys+(getCorrdSysMC(isEM)*yieldTable[histoPrefix]['top'])**2)
			if(DEBUG):print '										-->	yieldErrTable[histoPrefix][top]   (STAT+SYS) 			=	', math.sqrt(yieldErrTable[histoPrefix]['top']),'<--'				
			if(DEBUG):print ''
			if(DEBUG):print '											yieldErrTable[histoPrefix][ewk]   (SYS) 			=	', math.sqrt(ewkErrSys+(getCorrdSysMC(isEM)*yieldTable[histoPrefix]['ewk'])**2)
			if(DEBUG):print '										-->	yieldErrTable[histoPrefix][ewk]   (STAT+SYS) 			=	', math.sqrt(yieldErrTable[histoPrefix]['ewk']),'<--'
			if(DEBUG):print ''
			if(DEBUG):print '											yieldErrTable[histoPrefix][ddbkg] (STAT) 			=	', math.sqrt(ddbkgErrStat)
			if(DEBUG):print '											yieldErrTable[histoPrefix][ddbkg] (getCorrdSysDDBKG) 		=	', (getCorrdSysDDBKG(isEM)*yieldTable[histoPrefix]['ddbkg'])
			if(DEBUG):print '											yieldErrTable[histoPrefix][ddbkg] (STAT+getCorrdSysDDBKG) 	=	', math.sqrt(ddbkgErrStat+(getCorrdSysDDBKG(isEM)*yieldTable[histoPrefix]['ddbkg'])**2)
			if(DEBUG):print '											yieldErrTable[histoPrefix][ddbkg] (SYS) 			=	', math.sqrt((getCorrdSysDDBKG(isEM)*yieldTable[histoPrefix]['ddbkg'])**2 + ddbkgErrSys )
			if(DEBUG):print '										-->	yieldErrTable[histoPrefix][ddbkg] (STAT+SYS) 			=	', math.sqrt(yieldErrTable[histoPrefix]['ddbkg']),'<--'
			if(DEBUG):print ''
			if(DEBUG):print '										-->	yieldErrTable[histoPrefix][totBkg] (STAT+SYS) 			=	', math.sqrt(yieldErrTable[histoPrefix]['totBkg']),'<--'
			if(DEBUG):print ''


			for signal in sigList.keys(): yieldErrTable[histoPrefix][signal] += (getCorrdSysMC(isEM)*yieldTable[histoPrefix][signal])**2
			for signal in signals: yieldErrTable[histoPrefix][signal] += (getCorrdSysMC(isEM)*yieldTable[histoPrefix][signal])**2

			for systematic in ['pileup','btag','mistag','pdfNew','muRFcorrdNew','jec','jer']:
				if(DEBUG):print 'For MC sig', histoPrefix,'yield err, adding sys:', systematic
				for signal in sigList.keys(): 
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'nominal        =', yieldTable[histoPrefix][signal]  
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'up - nominal   =', math.fabs( yieldTable[histoPrefix+systematic+'Up'][signal] - yieldTable[histoPrefix][signal] ) 
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'down - nominal =', math.fabs( yieldTable[histoPrefix+systematic+'Down'][signal] - yieldTable[histoPrefix][signal] ) 
					yieldErrTable[histoPrefix][signal] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up'][signal] - yieldTable[histoPrefix][signal] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down'][signal] - yieldTable[histoPrefix][signal] ) ) ) **2
				for signal in signals: 
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'nominal        =', yieldTable[histoPrefix][signal]  
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'up - nominal   =', math.fabs( yieldTable[histoPrefix+systematic+'Up'][signal] - yieldTable[histoPrefix][signal] ) 
					if 'M800' in signal and (DEBUG_normalizeRENORM_PDF): print '							',signal,'down - nominal =', math.fabs( yieldTable[histoPrefix+systematic+'Down'][signal] - yieldTable[histoPrefix][signal] ) 
					yieldErrTable[histoPrefix][signal] += ( 0.5 * ( math.fabs( yieldTable[histoPrefix+systematic+'Up'][signal] - yieldTable[histoPrefix][signal] ) + math.fabs( yieldTable[histoPrefix+systematic+'Down'][signal] - yieldTable[histoPrefix][signal] ) ) ) **2


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

		for signal in signals: yieldErrTable[histoPrefix][signal+'OverSqrtBkg'] = ( yieldTable[histoPrefix][signal+'OverSqrtBkg']**2 ) * ( ( math.sqrt( yieldErrTable[histoPrefix][signal] ) / ( yieldTable[histoPrefix][signal]+1e-20 ) )**2 + ( math.sqrt( math.sqrt(yieldErrTable[histoPrefix]['totBkg'] ) ) / ( math.sqrt(yieldTable[histoPrefix]['totBkg'])+1e-20) )**2 )
	
		hdata[isEM].Write()
		#write theta histograms in root file, avoid having processes with no event yield (to make theta happy) 
		for signal in sigList.keys()+signals: 
# 			if hsig[isEM+signal].Integral() > 0:  
				hsig[isEM+signal].Write()
				if doAllSys:
					for systematic in systematicList:
						if systematic=='toppt' or 'PR' in systematic or 'FR' in systematic: continue
						if normalizeRENORM_PDF and ( systematic=='muRFcorrdNew' or systematic=='pdfNew' ) and (hsig[isEM+signal+systematic+'Up'].Integral()!=0 or hsig[isEM+signal+systematic+'Down'].Integral()!=0) :
# 							if(DEBUG_normalizeRENORM_PDF):print 'normalize signal systematic:', systematic
							hsig[isEM+signal+systematic+'Up'].Scale(hsig[isEM+signal].Integral()/hsig[isEM+signal+systematic+'Up'].Integral())
							hsig[isEM+signal+systematic+'Down'].Scale(hsig[isEM+signal].Integral()/hsig[isEM+signal+systematic+'Down'].Integral())
						hsig[isEM+signal+systematic+'Up'].Write()
						hsig[isEM+signal+systematic+'Down'].Write()
		if htop[isEM].Integral() > 0:  
			htop[isEM].Write()
			if doAllSys:
				for systematic in systematicList:
					if 'PR' in systematic or 'FR' in systematic: continue
					htop[isEM+systematic+'Up'].Write()
					htop[isEM+systematic+'Down'].Write()
		if hewk[isEM].Integral() > 0:  
			hewk[isEM].Write()
			if doAllSys:
				for systematic in systematicList:
					if systematic=='toppt' or 'PR' in systematic or 'FR' in systematic: continue
					hewk[isEM+systematic+'Up'].Write()
					hewk[isEM+systematic+'Down'].Write()
# 		if hqcd[isEM].Integral() > 0:  
# 			hqcd[isEM].Write()
# 			if doAllSys:
# 				for systematic in systematicList:
# 					if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
# 					hqcd[isEM+systematic+'Up'].Write()
# 					hqcd[isEM+systematic+'Down'].Write()
# 		if hwjets[isEM].Integral() > 0: hwjets[isEM].Write()
# 		if hzjets[isEM].Integral() > 0: hzjets[isEM].Write()
# 		if httjets[isEM].Integral()> 0: httjets[isEM].Write()
# 		if ht[isEM].Integral() > 0    : ht[isEM].Write()
		if httv[isEM].Integral() > 0  : httv[isEM].Write()
		if hvv[isEM].Integral() > 0   : hvv[isEM].Write()
		if hwz[isEM].Integral() > 0   : hwz[isEM].Write()
		if hzz[isEM].Integral() > 0   : hzz[isEM].Write()
		if hvvv[isEM].Integral() > 0  : hvvv[isEM].Write()
		if hddbkg[isEM].Integral() > 0: 
			hddbkg[isEM].Write()
			if doAllSys:
				for systematic in systematicList:
					if not ('PR' in systematic or 'FR' in systematic): continue
					hddbkg[isEM+systematic+'Up'].Write()
					hddbkg[isEM+systematic+'Down'].Write()
		hddbkgTTT[isEM].Write()

		hddbkgTTL[isEM].Write()
		hddbkgTLT[isEM].Write()
		hddbkgLTT[isEM].Write()

		hddbkgTLL[isEM].Write()
		hddbkgLTL[isEM].Write()
		hddbkgLLT[isEM].Write()

		hddbkgLLL[isEM].Write()

	outputRfile.Close()

	stdout_old = sys.stdout
# 	logFile = open(outDir+'/yields_'+discriminant+'_'+lumiStr.replace('.','p')+'fb.txt','a')
	savelogPATH = outDir+'/yields_'+discriminant+'_'+lumiStr.replace('.','p')+'fb.txt'
	if(DEBUG):savelogPATH = '/user_data/rsyarif/TESSST//yields_'+discriminant+'_'+lumiStr.replace('.','p')+'fb.txt'
	logFile = open(savelogPATH,'a')
	print 'Creating ', savelogPATH
	sys.stdout = logFile

	## PRINTING YIELD TABLE WITH UNCERTAINTIES ##
	#first print table without background grouping
	ljust_i = 1
	print 'CUTS:',pfix
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for bkg in bkgStackList: print bkg.ljust(ljust_i),
	print 'data'.ljust(ljust_i),
	print
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
		for bkg in bkgStackList:
			print str(yieldTable[histoPrefix][bkg])+'\t',
		print str(yieldTable[histoPrefix]['data']),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
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
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
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
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
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
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
		for sig in signalList:
			print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
		for sig in signalList:
			print str(math.sqrt(yieldErrTable[histoPrefix][sig])).ljust(ljust_i),
		print

	#print yields for total signals
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for sig in signals: print sig.ljust(ljust_i),
	print
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
		for sig in signals:
			print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print (isEM).ljust(ljust_i),
		for sig in signals:
			print str(math.sqrt(yieldErrTable[histoPrefix][sig])).ljust(ljust_i),
		print
				
	#print for AN tables
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for isEM in isEMlist:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
		print histoPrefix.ljust(ljust_i),
	print
# 	for process in bkgStackList+['ewk','top','qcd','ddbkg','totBkg','data','dataOverBkg']+signals+signalList:
# 	for process in bkgStackList+['ewk','top','qcd','ddbkg','ddbkgTTT','ddbkgTTL','ddbkgTLL','ddbkgLLL','totBkg','data','dataOverBkg']+signals+signalList:
# 	for process in bkgStackList+['ewk','top','ddbkg','ddbkgTTT','ddbkgTTL','ddbkgTLL','ddbkgLLL','totBkg','data','dataOverBkg']+signals+signalList:
	for process in bkgStackList+['ewk','top','ddbkg','ddbkgTTT','ddbkgTTL','ddbkgTLT','ddbkgLTT','ddbkgTLL','ddbkgLTL','ddbkgLLT','ddbkgLLL','totBkg','data','dataOverBkg']+sigOverSqrtBkgList+signals+signalList:
		print process.ljust(ljust_i),
		for isEM in isEMlist:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+isEM
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4))+' $\pm$ '+str(round_sig(math.sqrt(yieldErrTable[histoPrefix][process]),2)),
		print '\\\\',
		print
				
	sys.stdout = stdout_old
	logFile.close()

###########################################################
###################### LOAD HISTS #########################
###########################################################

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

distList = []
print outDir
for file in findfiles(outDir+'/'+isEMlist[0]+'/', '*.p'):
    if 'bkghists' not in file: continue
    distList.append(file.split('_')[-1][:-2])
print distList
for dist in distList:
	print "DISTRIBUTION: ",dist
	datahists = {}
	bkghists  = {}
	sighists  = {}
	if whichPlots==1:
# 		if not ('STrebinned' in dist or 'lepPt' in dist) :continue
# 		if not ('ST' in dist or 'lepPt' in dist or 'lepEta' in dist or 'lep1Pt' in dist or 'lep1Eta' in dist or 'lep2Pt' in dist or 'lep2Eta' in dist or 'lep3Pt' in dist or 'lep3Eta' in dist or 'Nlep' in dist or 'Nel' in dist or 'Nmu' in dist) :continue
		if not ('NJets' in dist or 'NBJets' in dist or 'METrebinned' in dist or 'JetPt' in dist or 'JetEta' in dist or 'minMlllBv4' in dist or 'HT' in dist or 'ST' in dist or 'lepPt' in dist or 'lepPtRebinned' in dist or 'lepEta' in dist or 'lep1Pt' in dist or 'lep1Eta' in dist or 'lep2Pt' in dist or 'lep2Eta' in dist or 'lep3Pt' in dist or 'lep3Eta' in dist or 'Nlep' in dist or 'Nel' in dist or 'Nmu' in dist or 'ElPt' in dist or 'MuPt' in dist) :continue
	if whichPlots==2:
		if not ('JetPt' in dist or 'JetEta' in dist or 'NJets' in dist or 'NBJets' in dist or 'lepEta' in dist or 'ST' in dist or 'METrebinned' in dist or 'lepPt' in dist) :continue
# 	if not('STrebinnedv' in dist): continue
	if whichPlots==3:
		if not ('ST' in dist or 'NJets' in dist) :continue
	if whichPlots==4:
		if not ('HT' in dist or 'ST' in dist or 'lepPt' in dist) :continue
	if whichPlots==5:
		if not ('El' in dist or 'Mu' in dist) :continue
	if whichPlots==6:
		if not ('ElPt' in dist or 'MuPt' in dist or 'ST' in dist or 'HT' in dist or 'minMlB' in dist or 'minMlllBv2' in dist or 'lepPt' in dist or 'N' in dist or 'minDPhiMETJet' in dist or 'DRlep1Jet1' in dist or 'minDRlepsJets' or 'JetPt' in dist) :continue
	if whichPlots==7:
		if not ('DR' in dist) :continue
	if whichPlots==8:
		if not ('lepPt' in dist or 'minMlllBv4' in dist or 'ST' in dist) :continue
	if whichPlots==9:
		if not ('minMlllBv4' in dist or 'HT' in dist or 'DR' in dist or 'PtRel' in dist or 'lepPt' in dist) :continue
	if whichPlots==10:
		if not ('PtRel' in dist) :continue
	if whichPlots==11:
		if not ('minMlllBv4' in dist or 'lepPt' in dist) :continue
	if whichPlots==12:
		if not ('lep' in dist and ('1' in dist or '2' in dist or '3' in dist) and ('Pt' in dist or 'Eta' in dist) ):continue
	if(DEBUG):
		if dist!='ST': continue
	for isEM in isEMlist:
		print "LOADING: ",isEM
		datahists.update(pickle.load(open(outDir+'/'+isEM+'/datahists_'+dist+'.p','rb')))
		bkghists.update(pickle.load(open(outDir+'/'+isEM+'/bkghists_'+dist+'.p','rb')))
		sighists.update(pickle.load(open(outDir+'/'+isEM+'/sighists_'+dist+'.p','rb')))
	makeCats(datahists,sighists,bkghists,dist)

print 'AFTER YOU CHECK THE OUTPUT FILES, DELETE THE PICKLE FILES !!!!!!!'
print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
