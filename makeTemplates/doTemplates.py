#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,getopt,fnmatch
from numpy import linspace
from weights import *
from analyze import *
from samples import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

doCombineTemplates = True

DEBUG=False
if len(sys.argv)>3: DEBUG=sys.argv[3]
if DEBUG!=False: 
	print '' 
	print '==========================================' 
	print '================DEBUG MODE================' 
	print '==========================================' 
	print '' 

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

#outDir='/user_data/rsyarif/'
outDir='/mnt/data/users/wwong/'
outDir+='kinematics_80x_dummy/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets3_NBJets1_DR0_ST600_MllOS20/'
if len(sys.argv)>1: outDir=sys.argv[1]


newOutDir='/Shape_accurateLHEsys_FRsysMar28'
if len(sys.argv)>2: newOutDir=sys.argv[2]

if doCombineTemplates : newOutDir+='_Combine'


lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb

catList  =['EEE','EEM','EMM','MMM']

"""
Note: 
--Each process in step1 (or step2) directories should have the root files hadded! 
--The code will look for <step1Dir>/<process>_hadd.root for nominal trees.
The uncertainty shape shifted files will be taken from <step1Dir>/../<shape>/<process>_hadd.root,
where <shape> is for example "JECUp". hadder.py can be used to prepare input files this way! 
--Each process given in the lists below must have a definition in "samples.py"
--Check the set of cuts in "analyze.py"
"""

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

	'TTWl',#'TTWq',
	'TTZl',#'TTZq',

	]

#run,dilep,ddbkgCat --> set in samples
dataList = []
ddbkgList= []
for run_ in run:
	for dilep_ in dilep:
		dataList.append('Data'+dilep_+run_)
		bkgList.append('DataDrivenBkg'+dilep_+run_)
		ddbkgList.append('DataDrivenBkg'+dilep_+run_)

bkgStackList = ['VV','VVV','TTV','ddbkg']
vvList    = ['WZ','ZZ']
vvvList   = ['WWW','WWZ','WZZ','ZZZ']
ttvList   = ['TTWl','TTZl']
#ttjetList = ['TTJetsPH']
# tList     = ['Tt','Ts','TtW','TbtW']

whichSignal = 'TT' #TT, BB, or X53X53
if 'BB' in outDir: whichSignal = 'BB' #TT, BB, or X53X53

signalMassRange = [1000,1800]
if whichSignal=='BB' : signalMassRange = [900,1800]
sigList = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='X53X53': decays = [''] #decays to tWtW 100% of the time


doBRScan = True
if DEBUG!=False: doBRScan = False 
BRs={}
nBRconf=0
if whichSignal=='TT':
	BRs['BW']=[0.50,1.0,0.0,0.0] #0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,1.0,0.0]
	BRs['TH']=[0.25,0.0,0.5,0.0] #0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0,0.5]
	BRs['TZ']=[0.25,0.0,0.5,1.0] #0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.0,0.5]
	nBRconf=len(BRs['BW'])
if whichSignal=='BB':
	BRs['TW']=[0.50,1.0,0.0,0.0] #0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,0.0]
	BRs['BH']=[0.25,0.0,0.5,0.0] #0.0,0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.5]
	BRs['BZ']=[0.25,0.0,0.5,1.0] #1.0,0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.5]
	nBRconf=len(BRs['TW'])
if not doBRScan: nBRconf=1

topList = ['TTWl','TTZl'] #NoTTJets, No singleT
ewkList = ['WZ','ZZ','WWW','WWZ','WZZ','ZZZ'] #No DY, WJets, WW
# ewkList = ['WZ','WWW']#No DY, WJets, WW

scaleLumi = False
lumiScaleCoeff = 1.

scaleSignalXsecTo1pb = True # this has to be "True" if you are making templates for limit calculation!!!!!!!!
normalizeRENORM_PDF = True #normalize the renormalization/pdf uncertainties to nominal templates --> normalizes signal processes !!!!

doAllSys = True
#systematicList = ['pileup','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','elPR','elFR','muPR','muFR','jec','jer'] #ALL
#systematicList = ['pileup','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','elPR','elFR','muPR','muFR','jec','jer',"TrigEffWeight", "elIdSys"]
#systematicList = ['pileup','prefire','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','jec','jer',"TrigEffWeight", "elIdSys"]
#systematicList = ['pileup','prefire','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','elPR','elFR','muPR','muFR','jec','jer',"TrigEffWeight", "elIdSys"]
systematicList = ['pileup','prefire','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','jec','jer',"TrigEffWeight", "elIdSys"]

#normSystematics = {
#					'elIdSys':{'EEE':1.06,'EEM':1.04,'EMM':1.02,'MMM':1.00},
#					'muIdSys':{'EEE':1.00,'EEM':1.02,'EMM':1.04,'MMM':1.06},
#					'elIsoSys':{'EEE':1.03,'EEM':1.02,'EMM':1.01,'MMM':1.00},
#					'muIsoSys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.03},
#					'elelelTrigSys':{'EEE':1.03,'EEM':1.00,'EMM':1.00,'MMM':1.00},
#					'elelmuTrigSys':{'EEE':1.00,'EEM':1.03,'EMM':1.00,'MMM':1.00},
#					'elmumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.03,'MMM':1.00},
#					'mumumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.00,'MMM':1.03},
#					}


#ddbkgSystematics = { #based on elMVAvalueFix Sep20-2017 No ST cut --> Asymmetric Unc thats why its applied here, see below codes how asymmetry is applied
#						'elPRsys':{'EEE':1.09,'EEM':1.05,'EMM':1.02,'MMM':1.00},
#						'muPRsys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.07},
#						'muFReta':{'EEE':1.00,'EEM':1.12,'EMM':1.16,'MMM':1.33},
#					}

#normSystematics_hist = ['TrigEffWeight','elIdSys']
normSystematics = { #updated by Jess in Mar 2020
                                        #'muIdSys':{'EEE':0.00,'EEM':0.02,'EMM':0.028,'MMM':0.035,'All':0.049}, #flat rate of 2% 
                                        #'elIsoSys':{'EEE':0.026,'EEM':0.021,'EMM':0.015,'MMM':0.00,'All':0.036}, #flat rate of 1.5% for el
                                        #'muIsoSys':{'EEE':0.00,'EEM':0.015,'EMM':0.021,'MMM':0.026,'All':0.036}, #flat rate of 1.5% for mu
                                        }

ddbkgSystematics = { #updated by Jess on Jun 17,2020 based on yields in 2020 FRv6 files + eta updated Aug 2020
                                       #'elPRsys':{'EEE':0.07,'EEM':0.03,'EMM':0.01,'MMM':0.00,'All':0.02},
                                       #'muPRsys':{'EEE':0.00,'EEM':0.01,'EMM':0.02,'MMM':0.07,'All':0.02},
                                       ##'muFReta':{'EEE':0.00,'EEM':0.16,'EMM':0.22,'MMM':0.42,'All':0.21},
                                       #'muFReta':{'EEE':0.00,'EEM':0.08,'EMM':0.15,'MMM':0.33,'All':0.17},
                                       #'FRsys'  :{'EEE':0.25,'EEM':0.14,'EMM':0.03,'MMM':0.16,'All':0.04},
                                       }

def round_sig(x,sig=2):
	try:
		return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
	except:
		return round(x,5)
		 
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
	
################################################################
#################### TEMPLATE PRODUCTION #######################
################################################################
def makeThetaCats(datahists,sighists,bkghists,discriminant):

	## This function categorizes the events into electron/muon --> 0/1p W-tag! --> 1/2p b-tag (the same as Cat1, but there is no 4p/3p jets requirement here)
	## Input  histograms (datahists,sighists,bkghists) must have corresponding histograms returned from analyze.py##

	## INITIALIZE DICTIONARIES FOR YIELDS AND THEIR UNCERTAINTIES ##
	yieldTable = {}
	yieldStatErrTable = {} #what is actually stored in this is the square of the uncertainty
	for cat in catList:
		catStr = cat
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
		yieldTable[histoPrefix]={}
		yieldStatErrTable[histoPrefix]={}
		if doAllSys:
			for systematic in systematicList+normSystematics.keys()+ddbkgSystematics.keys():#+['pdfNew','muRFcorrdNew']:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+systematic+ud]={}

	## WRITING HISTOGRAMS IN ROOT FILE ##
	#i=0
	for BRind in range(nBRconf):
		BRconfStr=''
		#if doBRScan: 
		if whichSignal=='TT': BRconfStr='_bW'+str(BRs['BW'][BRind]).replace('.','p')+'_tZ'+str(BRs['TZ'][BRind]).replace('.','p')+'_tH'+str(BRs['TH'][BRind]).replace('.','p')
		if whichSignal=='BB': BRconfStr='_tW'+str(BRs['TW'][BRind]).replace('.','p')+'_bZ'+str(BRs['BZ'][BRind]).replace('.','p')+'_bH'+str(BRs['BH'][BRind]).replace('.','p')
		if(DEBUG):print ''
		print "--- BR Configuration: "+BRconfStr, "----"
		hists={}
		for signal in sigList:

			if not os.path.exists(outDir+newOutDir): os.system('mkdir -v '+outDir+newOutDir)
			outputRfileName = outDir+newOutDir+'/templates_'+discriminant+'_'+signal+BRconfStr+'_'+lumiStr+'fb'+'.root'
			outputRfile = R.TFile(outputRfileName,'RECREATE')

			catInd = 1
			for cat in catList:
				catStr = cat
				i=BRconfStr+cat
				histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			
				hsig,htop,hewk,hqcd,hddbkg,hdata={},{},{},{},{},{}
				hsigY,htopY,hewkY,hqcdY,hddbkgY,hdataY={},{},{},{},{},{}
				hwjets,hzjets,httjets,ht,httw,httz,httv,hvv,hvvv={},{},{},{},{},{},{},{},{}
				# Borrow histograms for yields to theta templates
			
				hewkY[signal]  = R.TH1F('triLep2017'+catStr+'__ewk','',1,0,1)
				htopY[signal]  = R.TH1F('triLep2017'+catStr+'__top','',1,0,1)
				hddbkgY[signal]= R.TH1F('triLep2017'+catStr+'__ddbkg','',1,0,1)
				hdataY[signal] = R.TH1F('triLep2017'+catStr+'__DATA','',1,0,1)
				hsigY[signal]  = R.TH1F('triLep2017'+catStr+'__sig','',1,0,1)

			
				#systematics
				if doAllSys:
					for systematic in systematicList+normSystematics.keys()+ddbkgSystematics.keys():
						for ud in ['Up','Down']:
							if 'muRFcorrdNew' in systematic: continue
							if not (systematic=='toppt' or 'PR' in systematic or 'FR' in systematic or 'ddbkgSys' in systematic):
								if(DEBUG):print 'for: ewk, top, sig, creating systematics:', systematic, ud
								hewkY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
								htopY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
								hsigY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__sig__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								htopY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
							if ('PR' in systematic or 'FR' in systematic or 'ddbkgSys' in systematic): # PR and FR is only on the ddbkg sample, so it needs special treatment!
								if(DEBUG):print 'for: ddbkg, creating systematics:', systematic,ud
								hddbkgY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__ddbkg__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
						for ud in ['Up','Down']:
							if 'muRFcorrdNew' in systematic:
								hewkY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__ewk__'+systematic+'Ewk__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
								htopY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__top__'+systematic+'Top__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)
								hsigY[signal+systematic+ud] = R.TH1F('triLep2017'+catStr+'__sig__'+systematic+'Sig__'+ud.replace('Up','plus').replace('Down','minus'),'',1,0,1)


				#Group ttv processes
				httv[i] = bkghists[histoPrefix+'_'+ttvList[0]].Clone('triLep2017'+catStr+'__TTV')
				for bkg in ttvList:
					if bkg!=ttvList[0]: httv[i].Add(bkghists[histoPrefix+'_'+bkg])

				#Group vv processes
				hvv[i] = bkghists[histoPrefix+'_'+vvList[0]].Clone('triLep2017'+catStr+'__VV')
				for bkg in vvList:
					if bkg!=vvList[0]: hvv[i].Add(bkghists[histoPrefix+'_'+bkg])

				#Group vvv processes
				hvvv[i] = bkghists[histoPrefix+'_'+vvvList[0]].Clone('triLep2017'+catStr+'__VVV')
				for bkg in vvvList:
					if bkg!=vvvList[0]: hvvv[i].Add(bkghists[histoPrefix+'_'+bkg])

				#Group ddbkg processes
				hddbkg[i] = bkghists[histoPrefix+'_'+ddbkgList[0]].Clone('triLep2017'+catStr+'__ddbkg')
				for bkg in ddbkgList:
					if bkg!=ddbkgList[0]: hddbkg[i].Add(bkghists[histoPrefix+'_'+bkg])
							
				#Group EWK processes
				hewk[i] = bkghists[histoPrefix+'_'+ewkList[0]].Clone('triLep2017'+catStr+'__ewk')
				for bkg in ewkList:
					if bkg!=ewkList[0]: hewk[i].Add(bkghists[histoPrefix+'_'+bkg])
		
				#Group TOP processes
				htop[i] = bkghists[histoPrefix+'_'+topList[0]].Clone('triLep2017'+catStr+'__top')
				for bkg in topList:
					if bkg!=topList[0]: htop[i].Add(bkghists[histoPrefix+'_'+bkg])
		
				#get signal
				hsig[i] = sighists[histoPrefix+'_'+signal+decays[0]].Clone('triLep2017'+catStr+'__sig')
				if doBRScan: hsig[i].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
				for decay in decays:
					if decay!=decays[0]:
						htemp = sighists[histoPrefix+'_'+signal+decay].Clone()
						if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
						hsig[i].Add(htemp)

				#systematics
				if doAllSys:
					for systematic in systematicList:
						if systematic=='pdfNew' or systematic=='muRFcorrdNew' or systematic=='muRFdecorrdNew': continue
						for ud in ['Up','Down']:
							if not (systematic=='toppt' or 'PR' in systematic or 'FR' in systematic):
								hewk[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ewkList[0]].Clone('triLep2017'+catStr+'__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								htop[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+topList[0]].Clone('triLep2017'+catStr+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								hsig[systematic+ud+str(i)] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decays[0]].Clone('triLep2017'+catStr+'__sig__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								if doBRScan: hsig[systematic+ud+str(i)].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
								for bkg in ewkList: 
									if bkg!=ewkList[0]: hewk[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for bkg in topList: 
									if bkg!=topList[0]: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for decay in decays:
									htemp = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decay].Clone()
									if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
									if decay!=decays[0]: hsig[systematic+ud+str(i)].Add(htemp)
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								htop[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ttjetList[0]].Clone('triLep2017'+catStr+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								for bkg in ttjetList: 
									if bkg!=ttjetList[0]: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for bkg in topList: 
									if bkg not in ttjetList: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix+'_'+bkg])
							if 'PR' in systematic or 'FR' in systematic: # PR and FR is only on the ddbkg sample, so it needs special treatment!
								hddbkg[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ddbkgList[0]].Clone('triLep2017'+catStr+'__ddbkg'+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								for bkg in ddbkgList: 
									if bkg!=ddbkgList[0]: hddbkg[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
					for systematic in normSystematics.keys():
						hewk[systematic+'Up'+str(i)] = hewk[i].Clone('triLep2017'+catStr+'__ewk__'+systematic+'__plus')
						hewk[systematic+'Up'+str(i)].Scale(normSystematics[systematic][cat])
						hewk[systematic+'Down'+str(i)] = hewk[i].Clone('triLep2017'+catStr+'__ewk__'+systematic+'__minus')
						hewk[systematic+'Down'+str(i)].Scale(2.-normSystematics[systematic][cat])

						htop[systematic+'Up'+str(i)] = htop[i].Clone('triLep2017'+catStr+'__top__'+systematic+'__plus')
						htop[systematic+'Up'+str(i)].Scale(normSystematics[systematic][cat])
						htop[systematic+'Down'+str(i)] = htop[i].Clone('triLep2017'+catStr+'__top__'+systematic+'__minus')
						htop[systematic+'Down'+str(i)].Scale(2.-normSystematics[systematic][cat])

						hsig[systematic+'Up'+str(i)] = hsig[i].Clone('triLep2017'+catStr+'__sig__'+systematic+'__plus')
						hsig[systematic+'Up'+str(i)].Scale(normSystematics[systematic][cat])
						hsig[systematic+'Down'+str(i)] = hsig[i].Clone('triLep2017'+catStr+'__sig__'+systematic+'__minus')
						hsig[systematic+'Down'+str(i)].Scale(2.-normSystematics[systematic][cat])

 
					for systematic in ddbkgSystematics.keys():
						if(DEBUG):print 'Attempting to incorporate', signal, systematic
						hddbkg[systematic+'Up'+str(i)] = hddbkg[i].Clone('triLep2017'+catStr+'__ddbkg__'+systematic+'__plus')
						hddbkg[systematic+'Up'+str(i)].Scale(ddbkgSystematics[systematic][cat])
						hddbkg[systematic+'Down'+str(i)] = hddbkg[i].Clone('triLep2017'+catStr+'__ddbkg__'+systematic+'__minus')
						#Set as Asymetric FRsystematics, comment out below.
						#hddbkg[systematic+'Down'+str(i)].Scale(2.-ddbkgSystematics[systematic][cat]) 

					for pdfInd in range(100):
						hewk['pdf'+str(pdfInd)+'_'+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+ewkList[0]].Clone('triLep2017'+catStr+'__ewk__pdf'+str(pdfInd))
						for bkg in ewkList:
                                                        if bkg!=ewkList[0]: hewk['pdf'+str(pdfInd)+'_'+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])

						htop['pdf'+str(pdfInd)+'_'+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+topList[0]].Clone('triLep2017'+catStr+'__top__pdf'+str(pdfInd))
						for bkg in topList:
                                                        if bkg!=topList[0]: htop['pdf'+str(pdfInd)+'_'+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])

						if not pdfInd<30: continue
						hsig['pdf'+str(pdfInd)+'_'+str(i)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decays[0]].Clone('triLep2017'+catStr+'__sig__pdf'+str(pdfInd))
						if doBRScan: hsig['pdf'+str(pdfInd)+'_'+str(i)].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
						for decay in decays:
							htemp = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decay].Clone()
							if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
							if decay!=decays[0]:hsig['pdf'+str(pdfInd)+'_'+str(i)].Add(htemp)
					if(DEBUG):print(htop['pdf0'+'_'+str(i)], htop['pdf0'+'_'+str(i)].GetNbinsX())	
				#Group data processes
				hdata[i] = datahists[histoPrefix+'_'+dataList[0]].Clone('triLep2017'+catStr+'__DATA')
				for dat in dataList:
					if dat!=dataList[0]: hdata[i].Add(datahists[histoPrefix+'_'+dat])

				#prepare yield table
				yieldTable[histoPrefix]['top']    = htop[i].Integral()
				yieldTable[histoPrefix]['ewk']    = hewk[i].Integral()
				yieldTable[histoPrefix]['totBkg'] = htop[i].Integral()+hewk[i].Integral()+hddbkg[i].Integral()
				yieldTable[histoPrefix]['data']   = hdata[i].Integral()
				yieldTable[histoPrefix]['dataOverBkg']= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
				yieldTable[histoPrefix]['VV']     = hvv[i].Integral()
				yieldTable[histoPrefix]['VVV']    = hvvv[i].Integral()
				yieldTable[histoPrefix]['TTV']    = httv[i].Integral()
				yieldTable[histoPrefix]['ddbkg']  = hddbkg[i].Integral()
				yieldTable[histoPrefix][signal]   = hsig[i].Integral()
		
				#+/- 1sigma variations of shape systematics
				if doAllSys:
					for systematic in systematicList:
						if systematic=='pdfNew' or systematic=='muRFcorrdNew' or systematic=='muRFdecorrdNew': continue
						for ud in ['Up','Down']:
							if not('PR' in systematic or 'FR' in systematic):
								yieldTable[histoPrefix+systematic+ud]['top']    = htop[systematic+ud+str(i)].Integral()
								if systematic!='toppt':
									yieldTable[histoPrefix+systematic+ud]['ewk']   = hewk[systematic+ud+str(i)].Integral()
									yieldTable[histoPrefix+systematic+ud][signal]  = hsig[systematic+ud+str(i)].Integral()
							if 'PR' in systematic or 'FR' in systematic:
								yieldTable[histoPrefix+systematic+ud]['ddbkg'] = hddbkg[systematic+ud+str(i)].Integral()
					#normalization systematics
					for systematic in normSystematics.keys():
						yieldTable[histoPrefix+systematic+'Up']['top'] = yieldTable[histoPrefix]['top']*normSystematics[systematic][cat]
						yieldTable[histoPrefix+systematic+'Up']['ewk'] = yieldTable[histoPrefix]['ewk']*normSystematics[systematic][cat]
						yieldTable[histoPrefix+systematic+'Up'][signal] = yieldTable[histoPrefix][signal]*normSystematics[systematic][cat]
						yieldTable[histoPrefix+systematic+'Down']['top'] = yieldTable[histoPrefix]['top']*(2.-normSystematics[systematic][cat])
						yieldTable[histoPrefix+systematic+'Down']['ewk'] = yieldTable[histoPrefix]['ewk']*(2.-normSystematics[systematic][cat])
						yieldTable[histoPrefix+systematic+'Down'][signal] = yieldTable[histoPrefix][signal]*(2.-normSystematics[systematic][cat])
					for systematic in ddbkgSystematics.keys():
						yieldTable[histoPrefix+systematic+'Up']['ddbkg'] = yieldTable[histoPrefix]['ddbkg']*ddbkgSystematics[systematic][cat]
						#Set as Asymetric FRsystematics:
						#yieldTable[histoPrefix+systematic+'Down']['ddbkg'] = yieldTable[histoPrefix]['ddbkg']*(2.-ddbkgSystematics[systematic][cat])
						yieldTable[histoPrefix+systematic+'Down']['ddbkg'] = yieldTable[histoPrefix]['ddbkg']
								
					#R/F
#start
					htop['muRFcorrdNewUp'+str(i)] = htop['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__top__muRFcorrdNewTop__plus')
					htop['muRFcorrdNewDown'+str(i)] = htop['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__top__muRFcorrdNewTop__minus')
					hewk['muRFcorrdNewUp'+str(i)] = hewk['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__ewk__muRFcorrdNewEwk__plus')
					hewk['muRFcorrdNewDown'+str(i)] = hewk['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__ewk__muRFcorrdNewEwk__minus')
					hsig['muRFcorrdNewUp'+str(i)] = hsig['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__sig__muRFcorrdNewSig__plus')
					hsig['muRFcorrdNewDown'+str(i)] = hsig['muRFcorrdUp'+str(i)].Clone('triLep2017'+catStr+'__sig__muRFcorrdNewSig__minus')

					muRFprefixList = ['','muRUp','muRDown','muFUp','muFDown','muRFcorrdUp','muRFcorrdDown']
					htop[''+str(i)] =  htop[i].Clone() #hack to be able to use loop over muRFprefixList as it is.
					hewk[''+str(i)] =  hewk[i].Clone()
					hsig[''+str(i)] =  hsig[i].Clone()
					for ibin in range(1,htop[i].GetNbinsX()+1):
						weightRFcoordListTop = [htop[muRFprefix+str(i)].GetBinContent(ibin) for muRFprefix in muRFprefixList]
						if DEBUG and signal=='TTM800': 
							print 'htop[',i,'].GetBinContent(',ibin,') =', htop[i].GetBinContent(ibin) 
							for muRFprefix in ['muRUp','muRDown','muFUp','muFDown','muRFcorrdUp','muRFcorrdDown']: print 'htop[',muRFprefix,str(i),'].GetBinContent(',ibin,') =', htop[muRFprefix+str(i)].GetBinContent(ibin) 
						weightRFcoordListEwk = [hewk[muRFprefix+str(i)].GetBinContent(ibin) for muRFprefix in muRFprefixList]
						weightRFcoordListSig = [hsig[muRFprefix+str(i)].GetBinContent(ibin) for muRFprefix in muRFprefixList]

						indTopRFcoordUp = weightRFcoordListTop.index(max(weightRFcoordListTop))
						if DEBUG and signal=='TTM800': print '----->',
						if DEBUG and signal=='TTM800': print signal,cat,'ibin:,',ibin,'max(weightRFcoordListTop):',max(weightRFcoordListTop) 
						indTopRFcoordDn = weightRFcoordListTop.index(min(weightRFcoordListTop))
						indEwkRFcoordUp = weightRFcoordListEwk.index(max(weightRFcoordListEwk))
						indEwkRFcoordDn = weightRFcoordListEwk.index(min(weightRFcoordListEwk))
						indSigRFcoordUp = weightRFcoordListSig.index(max(weightRFcoordListSig))
						indSigRFcoordDn = weightRFcoordListSig.index(min(weightRFcoordListSig))

						htop['muRFcorrdNewUp'+str(i)].SetBinContent(ibin,htop[muRFprefixList[indTopRFcoordUp]+str(i)].GetBinContent(ibin))
						htop['muRFcorrdNewDown'+str(i)].SetBinContent(ibin,htop[muRFprefixList[indTopRFcoordDn]+str(i)].GetBinContent(ibin))
						hewk['muRFcorrdNewUp'+str(i)].SetBinContent(ibin,hewk[muRFprefixList[indEwkRFcoordUp]+str(i)].GetBinContent(ibin))
						hewk['muRFcorrdNewDown'+str(i)].SetBinContent(ibin,hewk[muRFprefixList[indEwkRFcoordDn]+str(i)].GetBinContent(ibin))
						hsig['muRFcorrdNewUp'+str(i)].SetBinContent(ibin,hsig[muRFprefixList[indSigRFcoordUp]+str(i)].GetBinContent(ibin))
						hsig['muRFcorrdNewDown'+str(i)].SetBinContent(ibin,hsig[muRFprefixList[indSigRFcoordDn]+str(i)].GetBinContent(ibin))

						htop['muRFcorrdNewUp'+str(i)].SetBinError(ibin,htop[muRFprefixList[indTopRFcoordUp]+str(i)].GetBinError(ibin))
						htop['muRFcorrdNewDown'+str(i)].SetBinError(ibin,htop[muRFprefixList[indTopRFcoordDn]+str(i)].GetBinError(ibin))
						hewk['muRFcorrdNewUp'+str(i)].SetBinError(ibin,hewk[muRFprefixList[indEwkRFcoordUp]+str(i)].GetBinError(ibin))
						hewk['muRFcorrdNewDown'+str(i)].SetBinError(ibin,hewk[muRFprefixList[indEwkRFcoordDn]+str(i)].GetBinError(ibin))
						hsig['muRFcorrdNewUp'+str(i)].SetBinError(ibin,hsig[muRFprefixList[indSigRFcoordUp]+str(i)].GetBinError(ibin))
						hsig['muRFcorrdNewDown'+str(i)].SetBinError(ibin,hsig[muRFprefixList[indSigRFcoordDn]+str(i)].GetBinError(ibin))

					#SF from Julie /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/makeTemplates/modifyBinning.py (April 7, 2017)
					#muSFsUp = {'TTM800':0.750,'TTM900':0.750,'TTM1000':0.749,'TTM1100':0.749,'TTM1200':0.748,'TTM1300':0.747,'TTM1400':0.746,'TTM1500':0.745,'TTM1600':0.744,'TTM1700':0.743,'TTM1800':0.741}
					#muSFsDn = {'TTM800':1.303,'TTM900':1.303,'TTM1000':1.304,'TTM1100':1.305,'TTM1200':1.307,'TTM1300':1.309,'TTM1400':1.311,'TTM1500':1.313,'TTM1600':1.315,'TTM1700':1.317,'TTM1800':1.319}
					#if whichSignal == 'BB':
					#	muSFsUp = {'BBM800':0.750,'BBM900':0.750,'BBM1000':0.749,'BBM1100':0.749,'BBM1200':0.748,'BBM1300':0.747,'BBM1400':0.746,'BBM1500':0.745,'BBM1600':0.744,'BBM1700':0.743,'BBM1800':0.741}
					#	muSFsDn = {'BBM800':1.303,'BBM900':1.303,'BBM1000':1.304,'BBM1100':1.305,'BBM1200':1.307,'BBM1300':1.309,'BBM1400':1.310,'BBM1500':1.313,'BBM1600':1.315,'BBM1700':1.317,'BBM1800':1.319}

	
					#SF from Julie https://github.com/jmhogan/singleLepAnalyzer/blob/tptp_2018/makeTemplates/modifyBinning.py (Oct 15 2020)
					#muSFsUp = {'TTM900':0.744,'TTM1000':0.744,'TTM1100':0.747,'TTM1200':0.742,'TTM1300':0.741,'TTM1400':0.738,'TTM1500':0.740,'TTM1600':0.735,'TTM1700':0.721,'TTM1800':0.746}
					#muSFsDn = {'TTM900':1.312,'TTM1000':1.312,'TTM1100':1.306,'TTM1200':1.315,'TTM1300':1.316,'TTM1400':1.322,'TTM1500':1.319,'TTM1600':1.329,'TTM1700':1.354,'TTM1800':1.311}
					#pdfSFsUp = {'TTM900':0.997,'TTM1000':0.997,'TTM1100':0.996,'TTM1200':0.995,'TTM1300':0.994,'TTM1400':0.991,'TTM1500':0.986,'TTM1600':0.984,'TTM1700':0.980,'TTM1800':0.966}
					#pdfSFsDn = {'TTM900':1.005,'TTM1000':1.005,'TTM1100':1.007,'TTM1200':1.008,'TTM1300':1.011,'TTM1400':1.015,'TTM1500':1.022,'TTM1600':1.027,'TTM1700':1.031,'TTM1800':1.050}
					#if whichSignal == 'BB':
					#	muSFsUp = {'BBM900':0.742,'BBM1000':0.742,'BBM1100':0.743,'BBM1200':0.742,'BBM1300':0.741,'BBM1400':0.739,'BBM1500':0.735,'BBM1600':0.735,'BBM1700':0.733,'BBM1800':0.731}
					#	muSFsDn = {'BBM900':1.315,'BBM1000':1.315,'BBM1100':1.314,'BBM1200':1.316,'BBM1300':1.318,'BBM1400':1.321,'BBM1500':1.329,'BBM1600':1.329,'BBM1700':1.331,'BBM1800':1.337}
					#	pdfSFsUp = {'BBM900':0.997,'BBM1000':0.997,'BBM1100':0.997,'BBM1200':0.996,'BBM1300':0.994,'BBM1400':0.991,'BBM1500':0.987,'BBM1600':0.984,'BBM1700':0.979,'BBM1800':0.970}
					#	pdfSFsDn = {'BBM900':1.005,'BBM1000':1.005,'BBM1100':1.006,'BBM1200':1.008,'BBM1300':1.011,'BBM1400':1.015,'BBM1500':1.019,'BBM1600':1.027,'BBM1700':1.037,'BBM1800':1.049}

					#SF from Julie (updated by Jess 28 Dec 2020) https://github.com/jmhogan/singleLepAnalyzer/blob/tptp_2017/makeTemplates/modifyBinning_byyear.py
					muSFsUp = {'TTM1000':0.744,'TTM1100':0.747,'TTM1200':0.742,'TTM1300':0.741,'TTM1400':0.738,'TTM1500':0.740,'TTM1600':0.735,'TTM1700':0.721,'TTM1800':0.746}
					muSFsDn = {'TTM1000':1.312,'TTM1100':1.306,'TTM1200':1.315,'TTM1300':1.316,'TTM1400':1.322,'TTM1500':1.319,'TTM1600':1.329,'TTM1700':1.354,'TTM1800':1.311}
					pdfSFsUp = {'TTM1000':0.954,'TTM1100':0.951,'TTM1200':0.947,'TTM1300':0.942,'TTM1400':0.936,'TTM1500':0.929,'TTM1600':0.921,'TTM1700':0.911,'TTM1800':0.898}
					pdfSFsDn = {'TTM1000':1.050,'TTM1100':1.054,'TTM1200':1.060,'TTM1300':1.066,'TTM1400':1.073,'TTM1500':1.082,'TTM1600':1.094,'TTM1700':1.109,'TTM1800':1.128}
					pdfSFsSym = {'TTM1000':0.048,'TTM1100':0.051,'TTM1200':0.056,'TTM1300':0.062,'TTM1400':0.068,'TTM1500':0.076,'TTM1600':0.086,'TTM1700':0.098,'TTM1800':0.113}
					if whichSignal == 'BB':
						muSFsUp = {'BBM900':0.742,'BBM1000':0.742,'BBM1100':0.743,'BBM1200':0.742,'BBM1300':0.741,'BBM1400':0.739,'BBM1500':0.735,'BBM1600':0.735,'BBM1700':0.733,'BBM1800':0.731}
						muSFsDn = {'BBM900':1.315,'BBM1000':1.315,'BBM1100':1.314,'BBM1200':1.316,'BBM1300':1.318,'BBM1400':1.321,'BBM1500':1.329,'BBM1600':1.329,'BBM1700':1.331,'BBM1800':1.337}
						pdfSFsUp = {'BBM900':0.954,'BBM1000':0.954,'BBM1100':0.951,'BBM1200':0.947,'BBM1300':0.942,'BBM1400':0.936,'BBM1500':0.929,'BBM1600':0.921,'BBM1700':0.911,'BBM1800':0.897}
						pdfSFsDn = {'BBM900':1.050,'BBM1000':1.050,'BBM1100':1.055,'BBM1200':1.059,'BBM1300':1.066,'BBM1400':1.073,'BBM1500':1.082,'BBM1600':1.094,'BBM1700':1.108,'BBM1800':1.130}
						pdfSFsSym = {'BBM900':0.048,'BBM1000':0.048,'BBM1100':0.052,'BBM1200':0.056,'BBM1300':0.061,'BBM1400':0.068,'BBM1500':0.076,'BBM1600':0.086,'BBM1700':0.098,'BBM1800':0.115}

					if(DEBUG): print 'before extra SF hsig[\'muRFcorrdNewUp\'',i,')]\']',hsig['muRFcorrdNewUp'+str(i)].Integral()					
					if(DEBUG): print 'before extra SF hsig[\'muRFcorrdNewDown\'',i,')]\']',hsig['muRFcorrdNewDown'+str(i)].Integral()					
					scalefactorUp = muSFsUp[signal]
					scalefactorDn = muSFsDn[signal]
					if(DEBUG): print 'Mass',signal,': assigning muRFcorrdNew SFup =',scalefactorUp,', SFdn =',scalefactorDn                                                                                                                          
					hsig['muRFcorrdNewUp'+str(i)].Scale(scalefactorUp)   # shape-only: muRFcorrdNewUpHist.Scale(renormNomHist.Integral()/muRFcorrdNewUpHist.Integral())                                                                 
					hsig['muRFcorrdNewDown'+str(i)].Scale(scalefactorDn)
					if(DEBUG): print 'after extra SF hsig[\'muRFcorrdNewUp\'',i,')]\']',hsig['muRFcorrdNewUp'+str(i)].Integral()					
					if(DEBUG): print 'after extra SF hsig[\'muRFcorrdNewDown\'',i,')]\']',hsig['muRFcorrdNewDown'+str(i)].Integral()					

					yieldTable[histoPrefix+'muRFcorrdNewUp']['top']  = htop['muRFcorrdNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'muRFcorrdNewDown']['top']  = htop['muRFcorrdNewDown'+str(i)].Integral()
					yieldTable[histoPrefix+'muRFcorrdNewUp']['ewk']  = hewk['muRFcorrdNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'muRFcorrdNewDown']['ewk']  = hewk['muRFcorrdNewDown'+str(i)].Integral()
					yieldTable[histoPrefix+'muRFcorrdNewUp'][signal]  = hsig['muRFcorrdNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'muRFcorrdNewDown'][signal]  = hsig['muRFcorrdNewDown'+str(i)].Integral()
#end									


# 					yieldTable[histoPrefix+'muRFcorrdNewUp']['top']  = max(htop['muRUp'+str(i)].Integral(),htop['muFUp'+str(i)].Integral(),htop['muRFcorrdUp'+str(i)].Integral())
# 					yieldTable[histoPrefix+'muRFcorrdNewDown']['top']= min(htop['muRDown'+str(i)].Integral(),htop['muFDown'+str(i)].Integral(),htop['muRFcorrdDown'+str(i)].Integral())
# 					yieldTable[histoPrefix+'muRFcorrdNewUp']['ewk']  = max(hewk['muRUp'+str(i)].Integral(),hewk['muFUp'+str(i)].Integral(),hewk['muRFcorrdUp'+str(i)].Integral())
# 					yieldTable[histoPrefix+'muRFcorrdNewDown']['ewk']= min(hewk['muRDown'+str(i)].Integral(),hewk['muFDown'+str(i)].Integral(),hewk['muRFcorrdDown'+str(i)].Integral())
# 					yieldTable[histoPrefix+'muRFcorrdNewUp'][signal]  = max(hsig['muRUp'+str(i)].Integral(),hsig['muFUp'+str(i)].Integral(),hsig['muRFcorrdUp'+str(i)].Integral())
# 					yieldTable[histoPrefix+'muRFcorrdNewDown'][signal]= min(hsig['muRDown'+str(i)].Integral(),hsig['muFDown'+str(i)].Integral(),hsig['muRFcorrdDown'+str(i)].Integral())
					
					#PDF
#start
					#print("pdf0 for top !!!!!!!", htop['pdf0'+'_'+str(i)].Integral())
					htop['pdfNewUp'+str(i)] = htop['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__top__pdfNew__plus')
					htop['pdfNewDown'+str(i)] = htop['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__top__pdfNew__minus')
					hewk['pdfNewUp'+str(i)] = hewk['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__ewk__pdfNew__plus')
					hewk['pdfNewDown'+str(i)] = hewk['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__ewk__pdfNew__minus')
					hsig['pdfNewUp'+str(i)] = hsig['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__sig__pdfNew__plus')
					hsig['pdfNewDown'+str(i)] = hsig['pdf0'+'_'+str(i)].Clone('triLep2017'+catStr+'__sig__pdfNew__minus')

					for ibin in range(1,htop['pdf0_'+str(i)].GetNbinsX()+1):
						weightListTop = [htop['pdf'+str(pdfInd)+'_'+str(i)].GetBinContent(ibin) for pdfInd in range(100)]
						weightListEwk = [hewk['pdf'+str(pdfInd)+'_'+str(i)].GetBinContent(ibin) for pdfInd in range(100)]
						weightListSig = [hsig['pdf'+str(pdfInd)+'_'+str(i)].GetBinContent(ibin) for pdfInd in range(30)]
						#indTopPDFUp = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[83]
						#indTopPDFDn = sorted(range(len(weightListTop)), key=lambda k: weightListTop[k])[15]
						#indEwkPDFUp = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[83]
						#indEwkPDFDn = sorted(range(len(weightListEwk)), key=lambda k: weightListEwk[k])[15]
						#indSigPDFUp = sorted(range(len(weightListSig)), key=lambda k: weightListSig[k])[83]
						#indSigPDFDn = sorted(range(len(weightListSig)), key=lambda k: weightListSig[k])[15]

						## New syst by % of the quad. sum of error (from central value
						errsqTop = 0
                                                shiftpctTop = 0
                                                for weight in weightListTop:
                                                        errsqTop += (weight - htop[i].GetBinContent(ibin))**2
                                                if htop[i].GetBinContent(ibin) != 0: shiftpctTop = math.sqrt(errsqTop)/htop[i].GetBinContent(ibin)
                                                elif math.sqrt(errsqTop) != 0: print 'Weird: (Top) central is 0 but not PDF unc'

                                                errsqEwk = 0
                                                shiftpctEwk = 0
                                                for weight in weightListEwk:
                                                        errsqEwk += (weight - hewk[i].GetBinContent(ibin))**2
                                                if hewk[i].GetBinContent(ibin) != 0: shiftpctEwk = math.sqrt(errsqEwk)/hewk[i].GetBinContent(ibin)
                                                elif math.sqrt(errsqEwk) != 0: print 'Weird: (Ewk) central is 0 but not PDF unc'

                                                errsqSig = 0
                                                shiftpctSig = 0
                                                for weight in weightListSig:
                                                        errsqSig += (weight - hsig[i].GetBinContent(ibin))**2
                                                if hsig[i].GetBinContent(ibin) != 0: shiftpctSig = math.sqrt(errsqSig)/hsig[i].GetBinContent(ibin)
                                                elif math.sqrt(errsqSig) != 0: print 'Weird: (Sig) central is 0 but not PDF unc'

                                                ### FOR SIGNAL ONLY --- reduce shift by the no-selection value
                                                #if shiftpctSig != 0:
                                                #        shiftpctSig = shiftpctSig - pdfSFsSym[signal]
                                                #if abs(shiftpctSig) > 1: print 'WARNING: pdf shift is',shiftpctSig,', flooring down at 0 in bin',ibin,'of hist Sig', i

						#print("top bin ", ibin, " weight ", weightListTop, " content ", htop['pdf'+str(indTopPDFUp)+'_'+str(i)].GetBinContent(ibin), " contentDn ", htop['pdf'+str(indTopPDFDn)+'_'+str(i)].GetBinContent(ibin))
						#print("ewk bin ", ibin, " weight ", weightListEwk, " content ", hewk['pdf'+str(indEwkPDFUp)+'_'+str(i)].GetBinContent(ibin), " contentDn ", hewk['pdf'+str(indEwkPDFDn)+'_'+str(i)].GetBinContent(ibin))
						#htop['pdfNewUp'+str(i)].SetBinContent(ibin,htop['pdf'+str(indTopPDFUp)+'_'+str(i)].GetBinContent(ibin))
						#htop['pdfNewDown'+str(i)].SetBinContent(ibin,htop['pdf'+str(indTopPDFDn)+'_'+str(i)].GetBinContent(ibin))
						#hewk['pdfNewUp'+str(i)].SetBinContent(ibin,hewk['pdf'+str(indEwkPDFUp)+'_'+str(i)].GetBinContent(ibin))
						#hewk['pdfNewDown'+str(i)].SetBinContent(ibin,hewk['pdf'+str(indEwkPDFDn)+'_'+str(i)].GetBinContent(ibin))
						#hsig['pdfNewUp'+str(i)].SetBinContent(ibin,hsig['pdf'+str(indSigPDFUp)+'_'+str(i)].GetBinContent(ibin))
						#hsig['pdfNewDown'+str(i)].SetBinContent(ibin,hsig['pdf'+str(indSigPDFDn)+'_'+str(i)].GetBinContent(ibin))

						htop['pdfNewUp'+str(i)].SetBinContent(ibin, max(0,htop[i].GetBinContent(ibin)*(1 + shiftpctTop)))
                                                htop['pdfNewDown'+str(i)].SetBinContent(ibin, max(0,htop[i].GetBinContent(ibin)*(1 - shiftpctTop)))
                                                hewk['pdfNewUp'+str(i)].SetBinContent(ibin, max(0,hewk[i].GetBinContent(ibin)*(1 + shiftpctEwk)))
                                                hewk['pdfNewDown'+str(i)].SetBinContent(ibin, max(0,hewk[i].GetBinContent(ibin)*(1 - shiftpctEwk)))
                                                hsig['pdfNewUp'+str(i)].SetBinContent(ibin, max(0,hsig[i].GetBinContent(ibin)*(1 + shiftpctSig)))
                                                hsig['pdfNewDown'+str(i)].SetBinContent(ibin, max(0,hsig[i].GetBinContent(ibin)*(1 - shiftpctSig)))

						#htop['pdfNewUp'+str(i)].SetBinError(ibin,htop['pdf'+str(indTopPDFUp)+'_'+str(i)].GetBinError(ibin))
						#htop['pdfNewDown'+str(i)].SetBinError(ibin,htop['pdf'+str(indTopPDFDn)+'_'+str(i)].GetBinError(ibin))
						#hewk['pdfNewUp'+str(i)].SetBinError(ibin,hewk['pdf'+str(indEwkPDFUp)+'_'+str(i)].GetBinError(ibin))
						#hewk['pdfNewDown'+str(i)].SetBinError(ibin,hewk['pdf'+str(indEwkPDFDn)+'_'+str(i)].GetBinError(ibin))
						#hsig['pdfNewUp'+str(i)].SetBinError(ibin,hsig['pdf'+str(indSigPDFUp)+'_'+str(i)].GetBinError(ibin))
						#hsig['pdfNewDown'+str(i)].SetBinError(ibin,hsig['pdf'+str(indSigPDFDn)+'_'+str(i)].GetBinError(ibin))

#					#SF from Julie /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/makeTemplates/modifyBinning.py (April 7, 2017)
#					pdfSFsUp = {'TTM800':0.908,'TTM900':0.902,'TTM1000':0.890,'TTM1100':0.889,'TTM1200':0.895,'TTM1300':0.895,'TTM1400':0.888,'TTM1500':0.897,'TTM1600':0.905,'TTM1700':0.885,'TTM1800':0.872}
#					pdfSFsDn = {'TTM800':1.106,'TTM900':1.104,'TTM1000':1.099,'TTM1100':1.099,'TTM1200':1.093,'TTM1300':1.098,'TTM1400':1.102,'TTM1500':1.099,'TTM1600':1.122,'TTM1700':1.121,'TTM1800':1.133}
#					if whichSignal == 'BB':
#							pdfSFsUp = {'BBM800':0.909,'BBM900':0.903,'BBM1000':0.889,'BBM1100':0.889,'BBM1200':0.895,'BBM1300':0.895,'BBM1400':0.889,'BBM1500':0.897,'BBM1600':0.904,'BBM1700':0.884,'BBM1800':0.872}
#							pdfSFsDn = {'BBM800':1.106,'BBM900':1.104,'BBM1000':1.100,'BBM1100':1.099,'BBM1200':1.093,'BBM1300':1.097,'BBM1400':1.102,'BBM1500':1.099,'BBM1600':1.121,'BBM1700':1.122,'BBM1800':1.132}
					if(DEBUG): print 'before extra SF hsig[\'pdfNewUp\'',i,')]\']',hsig['pdfNewUp'+str(i)].Integral()					
					if(DEBUG): print 'before extra SF hsig[\'pdfNewDown\'',i,')]\']',hsig['pdfNewDown'+str(i)].Integral()					
					scalefactorUp = pdfSFsUp[signal]
					scalefactorDn = pdfSFsDn[signal]
					if(DEBUG): print 'Mass',signal,': assigning pdfNew SFup =',scalefactorUp,', SFdn =',scalefactorDn                                                                                                                          
					hsig['pdfNewUp'+str(i)].Scale(scalefactorUp)
					hsig['pdfNewDown'+str(i)].Scale(scalefactorDn)
					if(DEBUG): print 'after extra SF hsig[\'pdfNewUp\'',i,')]\']',hsig['pdfNewUp'+str(i)].Integral()					
					if(DEBUG): print 'after extra SF hsig[\'pdfNewDown\'',i,')]\']',hsig['pdfNewDown'+str(i)].Integral()					
					#print("Check yield top pdfNew !!!!!!!!!!! ", htop['pdfNewDown'+str(i)].Integral())
					yieldTable[histoPrefix+'pdfNewUp']['top']  = htop['pdfNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown']['top']  = htop['pdfNewDown'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewUp']['ewk']  = hewk['pdfNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown']['ewk']  = hewk['pdfNewDown'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewUp'][signal]  = hsig['pdfNewUp'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown'][signal]  = hsig['pdfNewDown'+str(i)].Integral()
#end

# 					topPDFweights = []
# 					ewkPDFweights = []
# 					sigPDFweights = []
# 					for pdfInd in range(100):
# 						topPDFweights.append(htop['pdf'+str(pdfInd)+'_'+str(i)].Integral())
# 						ewkPDFweights.append(hewk['pdf'+str(pdfInd)+'_'+str(i)].Integral())
# 						sigPDFweights.append(hsig['pdf'+str(pdfInd)+'_'+str(i)].Integral())
# 					yieldTable[histoPrefix+'pdfNewUp']['top']  = htop['pdf'+str(sorted(range(len(topPDFweights)), key=lambda k: topPDFweights[k])[83])+'_'+str(i)].Integral()
# 					yieldTable[histoPrefix+'pdfNewDown']['top']= htop['pdf'+str(sorted(range(len(topPDFweights)), key=lambda k: topPDFweights[k])[15])+'_'+str(i)].Integral()
# 					yieldTable[histoPrefix+'pdfNewUp']['ewk']  = hewk['pdf'+str(sorted(range(len(ewkPDFweights)), key=lambda k: ewkPDFweights[k])[83])+'_'+str(i)].Integral()
# 					yieldTable[histoPrefix+'pdfNewDown']['ewk']= hewk['pdf'+str(sorted(range(len(ewkPDFweights)), key=lambda k: ewkPDFweights[k])[15])+'_'+str(i)].Integral()
# 					yieldTable[histoPrefix+'pdfNewUp'][signal]  = hsig['pdf'+str(sorted(range(len(sigPDFweights)), key=lambda k: sigPDFweights[k])[83])+'_'+str(i)].Integral()
# 					yieldTable[histoPrefix+'pdfNewDown'][signal]= hsig['pdf'+str(sorted(range(len(sigPDFweights)), key=lambda k: sigPDFweights[k])[15])+'_'+str(i)].Integral()

				#prepare MC yield error table
				yieldStatErrTable[histoPrefix]['top']    = 0.
				yieldStatErrTable[histoPrefix]['ewk']    = 0.
				yieldStatErrTable[histoPrefix]['totBkg'] = 0.
				yieldStatErrTable[histoPrefix]['data']   = 0.
				yieldStatErrTable[histoPrefix]['dataOverBkg']= 0.
				yieldStatErrTable[histoPrefix]['VV']     = 0.
				yieldStatErrTable[histoPrefix]['VVV']    = 0.
				yieldStatErrTable[histoPrefix]['TTV']    = 0.
				yieldStatErrTable[histoPrefix]['ddbkg']  = 0.
				yieldStatErrTable[histoPrefix][signal]   = 0.

				for ibin in range(1,hsig[i].GetXaxis().GetNbins()+1):
					yieldStatErrTable[histoPrefix]['top']    += htop[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['ewk']    += hewk[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['totBkg'] += htop[i].GetBinError(ibin)**2+hewk[i].GetBinError(ibin)**2+hddbkg[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['data']   += hdata[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['VV']     += hvv[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['VVV']    += hvvv[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['TTV']    += httv[i].GetBinError(ibin)**2					
					yieldStatErrTable[histoPrefix]['ddbkg']  += hddbkg[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix][signal]   += hsig[i].GetBinError(ibin)**2
					
				hewkY[signal].SetBinContent(1,yieldTable[histoPrefix]['ewk'])
				htopY[signal].SetBinContent(1,yieldTable[histoPrefix]['top'])
				hddbkgY[signal].SetBinContent(1,yieldTable[histoPrefix]['ddbkg'])
				hdataY[signal].SetBinContent(1,yieldTable[histoPrefix]['data'])
				if(DEBUG):print 'hdataY = ', yieldTable[histoPrefix]['data']
				hsigY[signal].SetBinContent(1,yieldTable[histoPrefix][signal])
				if(DEBUG):print 'hsigY[',signal+cat,'] = ', yieldTable[histoPrefix][signal]

				hewkY[signal].SetBinError(1,math.sqrt(yieldStatErrTable[histoPrefix]['ewk']))
				htopY[signal].SetBinError(1,math.sqrt(yieldStatErrTable[histoPrefix]['top']))
				hddbkgY[signal].SetBinError(1,math.sqrt(yieldStatErrTable[histoPrefix]['ddbkg']))
				hdataY[signal].SetBinError(1,math.sqrt(yieldStatErrTable[histoPrefix]['data']))
				hsigY[signal].SetBinError(1,math.sqrt(yieldStatErrTable[histoPrefix][signal]))
				
				#systematics
				if doAllSys:
					for systematic in systematicList:
						if systematic=='pdfNew' or systematic=='muRFcorrdNew' or systematic=='muRFdecorrdNew': continue
						for ud in ['Up','Down']:
							if not (systematic=='toppt' or 'PR' in systematic or 'FR' in systematic) :
								hewkY[signal+systematic+ud].SetBinContent(1,yieldTable[histoPrefix+systematic+ud]['ewk'])
								htopY[signal+systematic+ud].SetBinContent(1,yieldTable[histoPrefix+systematic+ud]['top'])
								hsigY[signal+systematic+ud].SetBinContent(1,yieldTable[histoPrefix+systematic+ud][signal])
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								htopY[signal+systematic+ud].SetBinContent(1,yieldTable[histoPrefix+systematic+ud]['top'])
							if 'PR' in systematic or 'FR' in systematic: # PR and FR is only on the ddbkg sample, so it needs special treatment!
								hddbkgY[signal+systematic+ud].SetBinContent(1,yieldTable[histoPrefix+systematic+ud]['ddbkg'])
					for systematic in normSystematics.keys():
						hewkY[signal+systematic+'Up'].SetBinContent(1,yieldTable[histoPrefix]['ewk']*normSystematics[systematic][cat])
						htopY[signal+systematic+'Up'].SetBinContent(1,yieldTable[histoPrefix]['top']*normSystematics[systematic][cat])
						hsigY[signal+systematic+'Up'].SetBinContent(1,yieldTable[histoPrefix][signal]*normSystematics[systematic][cat])
						hewkY[signal+systematic+'Down'].SetBinContent(1,yieldTable[histoPrefix]['ewk']*(2.-normSystematics[systematic][cat]))
						htopY[signal+systematic+'Down'].SetBinContent(1,yieldTable[histoPrefix]['top']*(2.-normSystematics[systematic][cat]))
						hsigY[signal+systematic+'Down'].SetBinContent(1,yieldTable[histoPrefix][signal]*(2.-normSystematics[systematic][cat]))
					for systematic in ddbkgSystematics.keys():
						if(DEBUG):print 'Attempting to incorporate', signal, systematic
						hddbkgY[signal+systematic+'Up'].SetBinContent(1,yieldTable[histoPrefix]['ddbkg']*ddbkgSystematics[systematic][cat])
						#Set as Asymetric FRsystematics:
						#hddbkgY[signal+systematic+'Down'].SetBinContent(1,yieldTable[histoPrefix]['ddbkg']*(2.-ddbkgSystematics[systematic][cat]))
						hddbkgY[signal+systematic+'Down'].SetBinContent(1,yieldTable[histoPrefix]['ddbkg'])
				catInd+=1
				
				'''
				#scale signal cross section to 1pb
				#write theta histograms in root file, avoid having processes with no event yield (to make theta happy) 
				if hsig[i].Integral() > 0:  
					if scaleSignalXsecTo1pb: hsig[i].Scale(1./xsec[signal])
					hsig[i].Write()
					if doAllSys:
						for systematic in systematicList:
							if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
							if scaleSignalXsecTo1pb: 
								hsig[systematic+'Up'+str(i)].Scale(1./xsec[signal])
								hsig[systematic+'Down'+str(i)].Scale(1./xsec[signal])
							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
								hsig[systematic+'Up'+str(i)].Scale(hsig[i].Integral()/hsig[systematic+'Up'+str(i)].Integral())
								hsig[systematic+'Down'+str(i)].Scale(hsig[i].Integral()/hsig[systematic+'Down'+str(i)].Integral())
							hsig[systematic+'Up'+str(i)].Write()
							hsig[systematic+'Down'+str(i)].Write()
						for pdfInd in range(100): hsig['pdf'+str(pdfInd)+'_'+str(i)].Write()
				if htop[i].Integral() > 0:  
					htop[i].Write()
					if doAllSys:
						for systematic in systematicList:
							if systematic=='PR' or systematic=='FR': continue
							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
								htop[systematic+'Up'+str(i)].Scale(htop[i].Integral()/htop[systematic+'Up'+str(i)].Integral())
								htop[systematic+'Down'+str(i)].Scale(htop[i].Integral()/htop[systematic+'Down'+str(i)].Integral())  
							htop[systematic+'Up'+str(i)].Write()
							htop[systematic+'Down'+str(i)].Write()
						for pdfInd in range(100): htop['pdf'+str(pdfInd)+'_'+str(i)].Write()
				if hewk[i].Integral() > 0:  
					hewk[i].Write()
					if doAllSys:
						for systematic in systematicList:
							if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
								hewk[systematic+'Up'+str(i)].Scale(hewk[i].Integral()/hewk[systematic+'Up'+str(i)].Integral())
								hewk[systematic+'Down'+str(i)].Scale(hewk[i].Integral()/hewk[systematic+'Down'+str(i)].Integral()) 
							hewk[systematic+'Up'+str(i)].Write()
							hewk[systematic+'Down'+str(i)].Write()
						for pdfInd in range(100): hewk['pdf'+str(pdfInd)+'_'+str(i)].Write()
				if hddbkg[i].Integral() > 0:  
					hddbkg[i].Write()
					if doAllSys:
						for systematic in systematicList:
							if systematic!='PR' or systematic!='FR': continue
							hddbkg[systematic+'Up'+str(i)].Write()
							hddbkg[systematic+'Down'+str(i)].Write()
				hdata[i].Write()
				'''
				
				hdata[i].Write()
				hists['data'+i] = hdata[i].Clone()
				hists['data'+i].SetDirectory(0)
# 				if hsig[i].Integral() > 0:  
				if(DEBUG):print 'hsigY[',signal+cat,'] (post 1pb xsec norm) :',hsigY[signal].Integral()
				if(DEBUG):print 'hsig[',i,'] (post 1pb xsec norm) :',hsig[i].Integral()
				if scaleSignalXsecTo1pb: 
					hsigY[signal].Scale(1./xsec[signal])
					hsig[i].Scale(1./xsec[signal])
					if(DEBUG):print 'hsigY[',signal+cat,'] (pre 1pb xsec norm)  :',hsigY[signal].Integral()
					if(DEBUG):print 'hsig[',i,'] (pre 1pb xsec norm)  :',hsig[i].Integral()
				hsig[i].Write()
				hists[signal+i] = hsig[i].Clone()
				hists[signal+i].SetDirectory(0)

				if htop[i].Integral() >= 0: 
					htop[i].Write()
				hists['top'+i] = htop[i].Clone()
				hists['top'+i].SetDirectory(0)
				if hewk[i].Integral() >= 0: 
					hewk[i].Write()
                                hists['ewk'+i] = hewk[i].Clone()
				hists['ewk'+i].SetDirectory(0)
				if hddbkg[i].Integral() >= 0: 
					hddbkg[i].Write()
                                hists['ddbkg'+i] = hddbkg[i].Clone()
                                hists['ddbkg'+i].SetDirectory(0)
				#systematics
				if doAllSys:
					for systematic in systematicList+normSystematics.keys()+ddbkgSystematics.keys():
						#print 'Writing systematics for ewk, top, sig:',systematic 
						for ud in ['Up','Down']:
							if not (systematic=='toppt' or 'PR' in systematic or 'FR' in systematic or 'ddbkgSys' in systematic):
								if not hewk[systematic+ud+str(i)].Integral() < 0: hewk[systematic+ud+str(i)].Write()
								hists['ewk'+i+systematic+ud] = hewk[systematic+ud+str(i)].Clone()
                                                                hists['ewk'+i+systematic+ud].SetDirectory(0)
								if not htop[systematic+ud+str(i)].Integral() < 0: htop[systematic+ud+str(i)].Write()
								hists['top'+i+systematic+ud] = htop[systematic+ud+str(i)].Clone()
                                                                hists['top'+i+systematic+ud].SetDirectory(0)
								#if ('pdfNew' in systematic and ud == 'Down') : print("WARNING check top pdfNew!!!!!! ",htop[systematic+ud+str(i)].Integral())
								if hsig[systematic+ud+str(i)].Integral() > 0:
									if scaleSignalXsecTo1pb: 
										hsig[systematic+ud+str(i)].Scale(1./xsec[signal])
									if normalizeRENORM_PDF and ('muRF' in systematic or 'pdf' in systematic):
										#print 'normalize signal systematic:', systematic
										hsig[systematic+ud+str(i)].Scale(hsig[i].Integral()/hsig[systematic+ud+str(i)].Integral())
								if not hsig[systematic+ud+str(i)].Integral() < 0: hsig[systematic+ud+str(i)].Write()
								hists[signal+i+systematic+ud] = hsig[systematic+ud+str(i)].Clone()
                                                                hists[signal+i+systematic+ud].SetDirectory(0)
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								if not htop[systematic+ud+str(i)].Integral() < 0: htop[systematic+ud].Write()

							if 'PR' in systematic or 'FR' in systematic or 'ddbkgSys' in systematic: # PR and FR is only on the ddbkg sample, so it needs special treatment!
								#print 'Writing systematics for ddbkg:', systematic 
								if not hddbkg[systematic+ud+str(i)].Integral() < 0: hddbkg[systematic+ud+str(i)].Write()
								hists['ddbkg'+i+systematic+ud] = hddbkg[systematic+ud+str(i)].Clone()
                                                                hists['ddbkg'+i+systematic+ud].SetDirectory(0)
								#hists[signal+i+systematic+ud] = hddbkg[systematic+ud+str(i)].Clone()
								#hists[signal+i+systematic+ud].SetDirectory(0)
				#i+=1
			outputRfile.Close()

		for h in hists.keys():
			#if 'TTM' in h or 'BBM' in h:
			for iBin in range(1,hists[h].GetNbinsX()+1):
				binValue = hists[h].GetBinContent(iBin)
				if binValue == 0.0:
					hists[h].SetBinContent(iBin,1e-6)
					hists[h].SetBinError(iBin,math.sqrt(1e-6))

		#Combine templates:
		if doCombineTemplates:
			#if 'NJets3' not in outDir+newOutDir: postTag = 'isCR_'
			#else: postTag = 'isSR_'
			postTag = ''
			print "       WRITING COMBINE TEMPLATES: "
			combineRfileName = outDir+newOutDir+'/templates_'+discriminant+BRconfStr+'_'+lumiStr+'_Combine.root'
			combineRfile = R.TFile(combineRfileName,'RECREATE')
			#print(hists.keys())
			for cat in catList:
				print "              ... "+cat
				i=BRconfStr+cat
				for signal in sigList:
					mass = [str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100) if str(mass) in signal][0]
					hists[signal+i].SetName(hists[signal+i].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass))
					hists[signal+i].Write()
					if doAllSys:
						for syst in systematicList+normSystematics.keys()+ddbkgSystematics.keys():
							if syst=='toppt': continue
							if 'PR' in syst or 'FR' in syst or 'ddbkgSys' in syst: continue
							if signal+i+syst+'Up' not in hists.keys(): print(signal+i+syst+'Up not found')
							if signal+i+syst+'Down' not in hists.keys(): print(signal+i+syst+'Down not found')
							hists[signal+i+syst+'Up'].SetName(hists[signal+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('__plus','Up'))
							hists[signal+i+syst+'Down'].SetName(hists[signal+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('__minus','Down'))
							if 'jec' in syst or 'jer' in syst or 'Trig' in syst or 'IdSys' in syst:
								hists[signal+i+syst+'Up'].SetName(hists[signal+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('Up','2017Up'))
								hists[signal+i+syst+'Down'].SetName(hists[signal+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('Down','2017Down'))
							hists[signal+i+syst+'Up'].Write()
							hists[signal+i+syst+'Down'].Write()

				totBkg_ = sum([hists[proc+i].Integral() for proc in ['top','ewk','ddbkg']])
				for proc in ['top','ewk','ddbkg']:
					if hists[proc+i].Integral()/totBkg_ < 0.0:
						print proc+i,"IS EMPTY! SKIPPING ..."
						continue
					hists[proc+i].SetName(hists[proc+i].GetName().replace('fb_','fb_'+postTag))
					if hists[proc+i].Integral() == 0.0: hists[proc+i].SetBinContent(1,1e-12)
					hists[proc+i].Write()
					if doAllSys:
						for syst in systematicList+normSystematics.keys()+ddbkgSystematics.keys():
							if syst=='toppt': continue
                                                        if proc!='ddbkg' and ('PR' in syst or 'FR' in syst or 'ddbkgSys' in syst): continue
							if proc=='ddbkg' and not ('PR' in syst or 'FR' in syst or 'ddbkgSys' in syst): continue
                                                        if proc+i+syst+'Up' not in hists.keys(): print(proc+i+syst+'Up not found')
                                                        if proc+i+syst+'Down' not in hists.keys(): print(proc+i+syst+'Down not found')
							hists[proc+i+syst+'Up'].SetName(hists[proc+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('__plus','Up'))
							hists[proc+i+syst+'Down'].SetName(hists[proc+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('__minus','Down'))
							if 'jec' in syst or 'jer' in syst or 'Trig' in syst or 'IdSys' in syst:
								hists[proc+i+syst+'Up'].SetName(hists[proc+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('Up','2017Up'))
								hists[proc+i+syst+'Down'].SetName(hists[proc+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('Down','2017Down'))
							if not hists[proc+i+syst+'Up'].Integral() < 0: hists[proc+i+syst+'Up'].Write()
							if not hists[proc+i+syst+'Down'].Integral() < 0: hists[proc+i+syst+'Down'].Write()
				
				hists['data'+i].SetName(hists['data'+i].GetName().replace('fb_','fb_'+postTag).replace('DATA','data_obs'))
				if not hists['data'+i].Integral() < 0: hists['data'+i].Write()
			combineRfile.Close()


		stdout_old = sys.stdout
		logFile = open(outDir+newOutDir+'/'+'/yields_'+discriminant+BRconfStr+'_'+lumiStr+'fb'+'.txt','a')
		sys.stdout = logFile

		## PRINTING YIELD TABLE WITH STATISTICAL UNCERTAINTIES ##
		#first print table without background grouping
		ljust_i = 1
		print 'CUTS:',outDir.split('/')[-2]#cutString
		print
		print 'YIELDS'.ljust(20*ljust_i), 
		for bkg in bkgStackList: print bkg.ljust(ljust_i),
		print 'data'.ljust(ljust_i),
		print
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for bkg in bkgStackList:
				print str(yieldTable[histoPrefix][bkg]).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for bkg in bkgStackList:
				print str(math.sqrt(yieldStatErrTable[histoPrefix][bkg])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['data'])).ljust(ljust_i),
			print

		#now print with top,ewk,qcd grouping
		print
		print 'YIELDS'.ljust(20*ljust_i), 
		print 'ewk'.ljust(ljust_i),
		print 'top'.ljust(ljust_i),
		print 'ddbkg'.ljust(ljust_i),
		print 'data'.ljust(ljust_i),
		print
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['ewk']).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['top']).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['ddbkg']).ljust(ljust_i),			
			print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['ewk'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['top'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['ddbkg'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['data'])).ljust(ljust_i),
			print

		#print yields for signals
		print
		print 'YIELDS'.ljust(20*ljust_i), 
		for sig in sigList: print sig.ljust(ljust_i),
		print
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for sig in sigList:
				print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			catStr=cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for sig in sigList:
				print str(math.sqrt(yieldStatErrTable[histoPrefix][sig])).ljust(ljust_i),
			print
		
		#print for AN tables systematics
		if doAllSys:
			print
			print "FOR AN (shape systematic percentaces): "
			print
			print 'YIELDS'.ljust(20*ljust_i), 
			for cat in catList:
				catStr=cat
				print (catStr).ljust(ljust_i),
			print
			for process in ['ewk','top','ddbkg']+sigList:
				print process.ljust(ljust_i),
				print
				for ud in ['Up','Down']:
# 					for systematic in systematicList+['pdfNew','muRFcorrdNew']:
					for systematic in systematicList+normSystematics.keys()+ddbkgSystematics.keys():
						if systematic=='toppt' and process!='top': continue
						if not (process=='ddbkg' or 'PR' in systematic or 'FR' in systematic or systematic=='ddbkgSys'):
							print (systematic+ud).ljust(ljust_i),
							for cat in catList:
								catStr=cat
								histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
								print ' & '+str(round_sig(yieldTable[histoPrefix+systematic+ud][process]/(yieldTable[histoPrefix][process]+1e-20),3)),
							print '\\\\',
							print
						if process=='ddbkg' and ('PR' in systematic or 'FR' in systematic or systematic=='ddbkgSys'):
							print (systematic+ud).ljust(ljust_i),
							for cat in catList:
								catStr=cat
								histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
								print ' & '+str(round_sig(yieldTable[histoPrefix+systematic+ud][process]/(yieldTable[histoPrefix][process]+1e-20),3)),
							print '\\\\',
							print
		
		sys.stdout = stdout_old
		logFile.close()


###########################################################
###################### LOAD HISTS #########################
###########################################################

print 'Loading files in:',outDir

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

#Just to list out distributions available to process.
distList = []
for file in findfiles(outDir, '*.p'):
    if 'bkghists' not in file: continue
    if 'EEE' not in file: continue
    distList.append(file.split('_')[-2])
print distList
for dist in distList:
	print "DISTRIBUTION: ",dist
	datahists = {}
	bkghists  = {}
	sighists  = {}
# 	if 'Iso' in dist:continue
# 	if dist=='MET' not in dist: continue
# 	if 'NBJets' not in dist: continue 
# 	if 'NJets' not in dist :continue
# 	if 'STrebinned' not in dist :continue
# 	if 'HTrebinned' not in dist :continue
# 	if dist!='ST' :continue
	for cat in catList:
		print "LOADING: ",cat
		datahists.update(pickle.load(open(outDir+'/datahists_'+dist+'_'+cat+'.p','rb')))
		bkghists.update(pickle.load(open(outDir+'/bkghists_'+dist+'_'+cat+'.p','rb')))
		sighists.update(pickle.load(open(outDir+'/sighists_'+dist+'_'+cat+'.p','rb')))

	print "MAKING CATEGORIES FOR TOTAL SIGNALS ..."
	makeThetaCats(datahists,sighists,bkghists,dist)

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
