#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,getopt
from numpy import linspace
from weights import *
from analyze import *
from samples import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
step1Dir = '/user_data/rsyarif/LJMet_3lep_122115_step1hadds/nominal/'
#step1Dir = '/user_data/ssagir/LJMet_1lepX53_021216hadds/nominal/' #x53
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
	'WW','WZ','ZZ',
	'WWZ','WZZ','ZZZ',
##	'TTJetsPH',
# 	'TTJetsPH0to700inc',
# 	'TTJetsPH700to1000inc',
# 	'TTJetsPH1000toINFinc',
# 	'TTJetsPH700mtt',
# 	'TTJetsPH1000mtt',
	'TTWl','TTWq',
	'TTZl','TTZq',
	'Tt','Ts',
	'TtW','TbtW',
	'QCDht100','QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
	'DataDrivenBkgEEPRD','DataDrivenBkgEERRD','DataDrivenBkgEERRC',
	'DataDrivenBkgMMPRD','DataDrivenBkgMMRRD','DataDrivenBkgMMRRC',
	'DataDrivenBkgMEPRD','DataDrivenBkgMERRD','DataDrivenBkgMERRC',
	]

dataList = ['DataEERRC','DataEERRD','DataEEPRD','DataMMRRC','DataMMRRD','DataMMPRD','DataMERRC','DataMERRD','DataMEPRD']
		       
bkgStackList = ['VV','VVV','TTV','QCD','ddbkg']
# wjetList  = ['WJetsMG100','WJetsMG200','WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500']
# zjetList  = ['DY50']
# vvList    = ['WW','WZ','ZZ']
vvList    = ['WZ','ZZ']
vvvList   = ['WWZ','WZZ','ZZZ']
ttvList   = ['TTWl','TTWq','TTZl','TTZq']
# ttjetList = ['TTJetsPH0to700inc','TTJetsPH700to1000inc','TTJetsPH1000toINFinc','TTJetsPH700mtt','TTJetsPH1000mtt']
#ttjetList = ['TTJetsPH']
# tList     = ['Tt','Ts','TtW','TbtW']

dataList = ['DataEERRC','DataEERRD','DataEEPRD','DataMMRRC','DataMMRRD','DataMMPRD','DataMERRC','DataMERRD','DataMEPRD']

whichSignal = 'TT' #TT, BB, or X53X53
signalMassRange = [700,1800]
sigList = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='X53X53': decays = [''] #decays to tWtW 100% of the time

doBRScan = False
BRs={}
BRs['BW']=[0.50,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,1.0]
BRs['TH']=[0.25,0.0,0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0]
BRs['TZ']=[0.25,1.0,0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.0]
nBRconf=len(BRs['BW'])
if not doBRScan: nBRconf=1

topList = ['TTWl','TTZl','TTWq','TTZq'] #NoTTJets, No singleT
# topList = ['TTJetsPH0to700inc','TTJetsPH700to1000inc','TTJetsPH1000toINFinc','TTJetsPH700mtt','TTJetsPH1000mtt','TTWl','TTZl','TTWq','TTZq','Tt','Ts','TtW','TbtW']
#ewkList = ['DY50','WJets','WW','WZ','ZZ']
ewkList = ['WZ','ZZ','WWZ','WZZ','ZZZ'] #No DY, WJets, WW
# ewkList = ['DY50','WJetsMG100','WJetsMG200','WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500','WW','WZ','ZZ']
qcdList = ['QCDht100','QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000']
ddbkgList = ['DataDrivenBkgEEPRD','DataDrivenBkgEERRD','DataDrivenBkgEERRC','DataDrivenBkgMMPRD','DataDrivenBkgMMRRD','DataDrivenBkgMMRRC','DataDrivenBkgMEPRD','DataDrivenBkgMERRD','DataDrivenBkgMERRC']

scaleSignalXsecTo1pb = True # this has to be "True" if you are making templates for limit calculation!!!!!!!!
scaleLumi = False
lumiScaleCoeff = 2215./2215.
doAllSys = True
systematicList = ['pileup','jec','jer','jmr','jms','btag','tau21','muR','muF','muRFcorrd','jsf','PR','FR']
normalizeRENORM_PDF = False #normalize the renormalization/pdf uncertainties to nominal templates --> normalizes both the background and signal processes !!!!

try: 
	opts, args = getopt.getopt(sys.argv[2:], "", ["lepPtCut=",
	                                              "jet1PtCut=",
	                                              "jet2PtCut=",
	                                              "jet3PtCut=",
	                                              "jet4PtCut=",
	                                              "jet5PtCut=",
	                                              "metCut=",
	                                              "njetsCut=",
	                                              "nbjetsCut=",
	                                              "drCut=",
	                                              "Wjet1PtCut=",
	                                              "bjet1PtCut=",
	                                              "htCut=",
	                                              "stCut=",
	                                              "minMlbCut=",
	                                              ])
	print opts,args
except getopt.GetoptError as err:
	print str(err)
	sys.exit(1)

lepPtCut=0#40
jet1PtCut=0#300
jet2PtCut=0#150
metCut=0#75
njetsCut=0#3
nbjetsCut=0
jet3PtCut=0#100
jet4PtCut=0
jet5PtCut=0
drCut=0#1
Wjet1PtCut=0
bjet1PtCut=0
htCut=0
stCut=0
minMlbCut=0
catList  =['EEE','EEM','EMM','MMM']
nttaglist=['0p']
nWtaglist=['0p']#,'1p']
nbtaglist=['0p']#,'1','2','3p']
catList = list(itertools.product(catList,nttaglist,nWtaglist,nbtaglist))
tagList = list(itertools.product(nttaglist,nWtaglist,nbtaglist))

for o, a in opts:
	print o, a
	if o == '--lepPtCut': lepPtCut = float(a)
	if o == '--jet1PtCut': jet1PtCut = float(a)
	if o == '--jet2PtCut': jet2PtCut = float(a)
	if o == '--jet3PtCut': jet3PtCut = float(a)
	if o == '--jet4PtCut': jet4PtCut = float(a)
	if o == '--jet5PtCut': jet5PtCut = float(a)
	if o == '--metCut': metCut = float(a)
	if o == '--njetsCut': njetsCut = float(a)
	if o == '--nbjetsCut': nbjetsCut = float(a)
	if o == '--drCut': drCut = float(a)
	if o == '--Wjet1PtCut': Wjet1PtCut = float(a)
	if o == '--bjet1PtCut': bjet1PtCut = float(a)
	if o == '--htCut': htCut = float(a)
	if o == '--stCut': stCut = float(a)
	if o == '--minMlbCut': minMlbCut = float(a)
	if o == '--isEM': catList = [str(a)]
	if o == '--nttag': nttaglist = [str(a)]
	if o == '--nWtag': nWtaglist = [str(a)]
	if o == '--nbtag': nbtaglist = [str(a)]

cutList = {'lepPtCut':lepPtCut,
		   'jet1PtCut':jet1PtCut,
		   'jet2PtCut':jet2PtCut,
		   'jet3PtCut':jet3PtCut,
		   'jet4PtCut':jet4PtCut,
		   'jet5PtCut':jet5PtCut,
		   'metCut':metCut,
		   'njetsCut':njetsCut,
		   'nbjetsCut':nbjetsCut,
		   'drCut':drCut,
		   'Wjet1PtCut':Wjet1PtCut,
		   'bjet1PtCut':bjet1PtCut,
		   'htCut':htCut,
		   'stCut':stCut,
		   'minMlbCut':minMlbCut,
		   }

cutString  = 'lep'+str(int(cutList['lepPtCut']))+'_MET'+str(int(cutList['metCut']))
cutString += '_1jet'+str(int(cutList['jet1PtCut']))+'_2jet'+str(int(cutList['jet2PtCut']))
cutString += '_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))
cutString += '_3jet'+str(int(cutList['jet3PtCut']))+'_4jet'+str(int(cutList['jet4PtCut']))
cutString += '_5jet'+str(int(cutList['jet5PtCut']))+'_DR'+str(cutList['drCut'])
cutString += '_1Wjet'+str(cutList['Wjet1PtCut'])+'_1bjet'+str(cutList['bjet1PtCut'])
cutString += '_HT'+str(cutList['htCut'])+'_ST'+str(cutList['stCut'])+'_minMlb'+str(cutList['minMlbCut'])

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templates_ST'
pfix+=datestr+'_'+timestr

normSystematics = {
					'elIdSys':{'EEE':1.03,'EEM':1.02,'EMM':1.01,'MMM':1.00},
					'muIdSys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.03},
					'elIsoSys':{'EEE':1.03,'EEM':1.02,'EMM':1.01,'MMM':1.00},
					'muIsoSys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.03},
					'elelelTrigSys':{'EEE':1.03,'EEM':1.00,'EMM':1.00,'MMM':1.00},
					'elelmuTrigSys':{'EEE':1.00,'EEM':1.03,'EMM':1.00,'MMM':1.00},
					'elmumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.03,'MMM':1.00},
					'mumumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.00,'MMM':1.03},
					}

if len(sys.argv)>1: outDir=sys.argv[1]
else: 
	outDir = os.getcwd()+'/'
	outDir+=pfix
	if not os.path.exists(outDir): os.system('mkdir '+outDir)
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
	outDir+='/'+cutString

lumiSys = 0.027 #2.7% lumi uncertainty
trigSys = 0.03 #3% trigger uncertainty
lepIdSys = 0.01 #1% lepton id uncertainty
lepIsoSys = 0.01 #1% lepton isolation uncertainty
topXsecSys = 0.#0.055 #5.5% top x-sec uncertainty
ewkXsecSys = 0.#0.05 #5% ewk x-sec uncertainty
qcdXsecSys = 0.#0.50 #50% qcd x-sec uncertainty
corrdSys = math.sqrt(lumiSys**2+trigSys**2+lepIdSys**2+lepIsoSys**2)

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
	
###########################################################
#################### CATEGORIZATION #######################
###########################################################
def makeThetaCats(datahists,sighists,bkghists,discriminant):

	## This function categorizes the events into electron/muon --> 0/1p W-tag! --> 1/2p b-tag (the same as Cat1, but there is no 4p/3p jets requirement here)
	## Input  histograms (datahists,sighists,bkghists) must have corresponding histograms returned from analyze.py##

	## INITIALIZE DICTIONARIES FOR YIELDS AND THEIR UNCERTAINTIES ##
	yieldTable = {}
	yieldStatErrTable = {} #what is actually stored in this is the square of the uncertainty
	for cat in catList:
		tagStr = 'nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
		catStr = 'is'+cat[0]+'_'+tagStr
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
		yieldTable[histoPrefix]={}
		yieldStatErrTable[histoPrefix]={}
		if doAllSys:
			for systematic in systematicList+['pdfNew','muRFcorrdNew']:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+systematic+ud]={}

	## WRITING HISTOGRAMS IN ROOT FILE ##
	i=0
	for BRind in range(nBRconf):
		BRconfStr=''
		if doBRScan: BRconfStr='_bW'+str(BRs['BW'][BRind]).replace('.','p')+'_tZ'+str(BRs['TZ'][BRind]).replace('.','p')+'_tH'+str(BRs['TH'][BRind]).replace('.','p')
		print "       BR Configuration:"+BRconfStr
		for signal in sigList:
			outputRfileName = outDir+'/templates_'+discriminant+'_'+signal+BRconfStr+'_'+lumiStr+'fb'+'.root'
			outputRfile = R.TFile(outputRfileName,'RECREATE')
			hsig,htop,hewk,hqcd,hddbkg,hdata={},{},{},{},{},{}
			hsigY,htopY,hewkY,hqcdY,hddbkgY,hdataY={},{},{},{},{},{}
			hwjets,hzjets,httjets,ht,httw,httz,httv,hvv,hvvv={},{},{},{},{},{},{},{},{}
			# Borrow histograms for yields to theta templates
			
			hqcdY[signal]  = R.TH1F('triLep__qcd','',len(catList),0,len(catList))
			hewkY[signal]  = R.TH1F('triLep__ewk','',len(catList),0,len(catList))
			htopY[signal]  = R.TH1F('triLep__top','',len(catList),0,len(catList))
			hddbkgY[signal]= R.TH1F('triLep__ddbkg','',len(catList),0,len(catList))
			hdataY[signal] = R.TH1F('triLep__DATA','',len(catList),0,len(catList))
			hsigY[signal]  = R.TH1F('triLep__sig','',len(catList),0,len(catList))
			
			#systematics
			if doAllSys:
				for systematic in systematicList+['pdfNew','muRFcorrdNew']+normSystematics.keys():
					for ud in ['Up','Down']:
						if systematic!='toppt' and systematic!='PR' and systematic!='FR':
							hqcdY[signal+systematic+ud] = R.TH1F('triLep__qcd__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))
							hewkY[signal+systematic+ud] = R.TH1F('triLep__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))
							htopY[signal+systematic+ud] = R.TH1F('triLep__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))
							hsigY[signal+systematic+ud] = R.TH1F('triLep__sig__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))
						if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
							htopY[signal+systematic+ud] = R.TH1F('triLep__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))
						if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
							hddbkgY[signal+systematic+ud] = R.TH1F('triLep__ddbkg__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(catList),0,len(catList))

			catInd = 1
			for cat in catList:
				tagStr = 'nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
				catStr = 'is'+cat[0]+'_'+tagStr
				histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr

				#Group processes
# 				hwjets[i] = bkghists[histoPrefix+'_'+wjetList[0]].Clone(histoPrefix+'_WJets')
# 				hzjets[i] = bkghists[histoPrefix+'_'+zjetList[0]].Clone(histoPrefix+'_ZJets')
# 				httjets[i] = bkghists[histoPrefix+'_'+ttjetList[0]].Clone(histoPrefix+'_TTJets')
# 				ht[i] = bkghists[histoPrefix+'_'+tList[0]].Clone(histoPrefix+'__T')
# 				httw[i] = bkghists[histoPrefix+'_'+ttwList[0]].Clone(histoPrefix+'__TTW')
# 				httz[i] = bkghists[histoPrefix+'_'+ttzList[0]].Clone(histoPrefix+'__TTZ')
				httv[i] = bkghists[histoPrefix+'_'+ttvList[0]].Clone(histoPrefix+'__TTV')
				hvv[i] = bkghists[histoPrefix+'_'+vvList[0]].Clone(histoPrefix+'__VV')
				hvvv[i] = bkghists[histoPrefix+'_'+vvvList[0]].Clone(histoPrefix+'__VVV')
				hddbkg[i] = bkghists[histoPrefix+'_'+ddbkgList[0]].Clone(histoPrefix+'__ddbkg')

# 				for bkg in ttjetList:
# 					if bkg!=ttjetList[0]: httjets[i].Add(bkghists[histoPrefix+'_'+bkg])
# 				for bkg in wjetList:
# 					if bkg!=wjetList[0]: hwjets[i].Add(bkghists[histoPrefix+'_'+bkg])
# 				for bkg in ttwList:
# 					if bkg!=ttwList[0]: httw[i].Add(bkghists[histoPrefix+'_'+bkg])
# 				for bkg in ttzList:
# 					if bkg!=ttzList[0]: httz[i].Add(bkghists[histoPrefix+'_'+bkg])
				for bkg in ttvList:
					if bkg!=ttvList[0]: httv[i].Add(bkghists[histoPrefix+'_'+bkg])
# 				for bkg in tList:
# 					if bkg!=tList[0]: ht[i].Add(bkghists[histoPrefix+'_'+bkg])
# 				for bkg in zjetList:
# 					if bkg!=zjetList[0]: hzjets[i].Add(bkghists[histoPrefix+'_'+bkg])
				for bkg in vvList:
					if bkg!=vvList[0]: hvv[i].Add(bkghists[histoPrefix+'_'+bkg])
				for bkg in vvvList:
					if bkg!=vvvList[0]: hvvv[i].Add(bkghists[histoPrefix+'_'+bkg])
				for bkg in ddbkgList:
					if bkg!=ddbkgList[0]: hddbkg[i].Add(bkghists[histoPrefix+'_'+bkg])
					
		
				#Group QCD processes
				hqcd[i] = bkghists[histoPrefix+'_'+qcdList[0]].Clone(histoPrefix+'__qcd')
				for bkg in qcdList: 
					if bkg!=qcdList[0]: 
						hqcd[i].Add(bkghists[histoPrefix+'_'+bkg])
		
				#Group EWK processes
				hewk[i] = bkghists[histoPrefix+'_'+ewkList[0]].Clone(histoPrefix+'__ewk')
				for bkg in ewkList:
					if bkg!=ewkList[0]: hewk[i].Add(bkghists[histoPrefix+'_'+bkg])
		
				#Group TOP processes
				htop[i] = bkghists[histoPrefix+'_'+topList[0]].Clone(histoPrefix+'__top')
				for bkg in topList:
					if bkg!=topList[0]: htop[i].Add(bkghists[histoPrefix+'_'+bkg])
		
				#get signal
				hsig[i] = sighists[histoPrefix+'_'+signal+decays[0]].Clone(histoPrefix+'__sig')
				if doBRScan: hsig[i].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
				for decay in decays:
					if decay!=decays[0]:
						htemp = sighists[histoPrefix+'_'+signal+decay].Clone()
						if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
						hsig[i].Add(htemp)

				#systematics
				if doAllSys:
					for systematic in systematicList:
						for ud in ['Up','Down']:
							if systematic!='toppt' and systematic!='PR' and systematic!='FR':
								hqcd[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								hewk[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								htop[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+topList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								hsig[systematic+ud+str(i)] = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decays[0]].Clone(histoPrefix+'__sig__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								if doBRScan: hsig[systematic+ud+str(i)].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
								for bkg in qcdList: 
									if bkg!=qcdList[0]: hqcd[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for bkg in ewkList: 
									if bkg!=ewkList[0]: hewk[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for bkg in topList: 
									if bkg!=topList[0]: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for decay in decays:
									htemp = sighists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+signal+decay].Clone()
									if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
									if decay!=decays[0]: hsig[systematic+ud+str(i)].Add(htemp)
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								htop[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ttjetList[0]].Clone(histoPrefix+'__top__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								for bkg in ttjetList: 
									if bkg!=ttjetList[0]: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])
								for bkg in topList: 
									if bkg not in ttjetList: htop[systematic+ud+str(i)].Add(bkghists[histoPrefix+'_'+bkg])
							if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
								hddbkg[systematic+ud+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ddbkgList[0]].Clone(histoPrefix+'__ddbkg'+'__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
								for bkg in ddbkgList: 
									if bkg!=ddbkgList[0]: hddbkg[systematic+ud+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])

					for pdfInd in range(100):
						hqcd['pdf'+str(pdfInd)+'_'+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+qcdList[0]].Clone(histoPrefix+'__qcd__pdf'+str(pdfInd))
						hewk['pdf'+str(pdfInd)+'_'+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+ewkList[0]].Clone(histoPrefix+'__ewk__pdf'+str(pdfInd))
						htop['pdf'+str(pdfInd)+'_'+str(i)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+topList[0]].Clone(histoPrefix+'__top__pdf'+str(pdfInd))
						hsig['pdf'+str(pdfInd)+'_'+str(i)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decays[0]].Clone(histoPrefix+'__sig__pdf'+str(pdfInd))
						if doBRScan: hsig['pdf'+str(pdfInd)+'_'+str(i)].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
						for bkg in qcdList: 
							if bkg!=qcdList[0]: hqcd['pdf'+str(pdfInd)+'_'+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
						for bkg in ewkList: 
							if bkg!=ewkList[0]: hewk['pdf'+str(pdfInd)+'_'+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
						for bkg in topList: 
							if bkg!=topList[0]: htop['pdf'+str(pdfInd)+'_'+str(i)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
						for decay in decays:
							htemp = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decay].Clone()
							if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
							if decay!=decays[0]:hsig['pdf'+str(pdfInd)+'_'+str(i)].Add(htemp)
		
				#Group data processes
				hdata[i] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
				for dat in dataList:
					if dat!=dataList[0]: hdata[i].Add(datahists[histoPrefix+'_'+dat])

				#prepare yield table
				yieldTable[histoPrefix]['top']    = htop[i].Integral()
				yieldTable[histoPrefix]['ewk']    = hewk[i].Integral()
				yieldTable[histoPrefix]['qcd']    = hqcd[i].Integral()
				yieldTable[histoPrefix]['totBkg'] = htop[i].Integral()+hewk[i].Integral()+hqcd[i].Integral()+hddbkg[i].Integral()
				yieldTable[histoPrefix]['data']   = hdata[i].Integral()
				yieldTable[histoPrefix]['dataOverBkg']= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
# 				yieldTable[histoPrefix]['WJets']  = hwjets[i].Integral()
# 				yieldTable[histoPrefix]['ZJets']  = hzjets[i].Integral()
				yieldTable[histoPrefix]['VV']     = hvv[i].Integral()
				yieldTable[histoPrefix]['VVV']    = hvvv[i].Integral()
# 				yieldTable[histoPrefix]['TTW']    = httw[i].Integral()
# 				yieldTable[histoPrefix]['TTZ']    = httz[i].Integral()
				yieldTable[histoPrefix]['TTV']    = httv[i].Integral()
# 				yieldTable[histoPrefix]['TTJets'] = httjets[i].Integral()
# 				yieldTable[histoPrefix]['T']      = ht[i].Integral()
				yieldTable[histoPrefix]['QCD']    = hqcd[i].Integral()
				yieldTable[histoPrefix]['ddbkg']  = hddbkg[i].Integral()
				yieldTable[histoPrefix][signal]   = hsig[i].Integral()
		
				#+/- 1sigma variations of shape systematics
				if doAllSys:
					for systematic in systematicList:
						for ud in ['Up','Down']:
							if systematic!='PR' and systematic!='FR':
								yieldTable[histoPrefix+systematic+ud]['top']    = htop[systematic+ud+str(i)].Integral()
								if systematic!='toppt':
									yieldTable[histoPrefix+systematic+ud]['ewk']   = hewk[systematic+ud+str(i)].Integral()
									yieldTable[histoPrefix+systematic+ud]['qcd']   = hqcd[systematic+ud+str(i)].Integral()
									yieldTable[histoPrefix+systematic+ud][signal]  = hsig[systematic+ud+str(i)].Integral()
							if systematic=='PR' or systematic=='FR':
								yieldTable[histoPrefix+systematic+ud]['ddbkg'] = hddbkg[systematic+ud+str(i)].Integral()
								
					#R/F
					yieldTable[histoPrefix+'muRFcorrdNewUp']['top']  = max(htop['muRUp'+str(i)].Integral(),htop['muFUp'+str(i)].Integral(),htop['muRFcorrdUp'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewDown']['top']= min(htop['muRDown'+str(i)].Integral(),htop['muFDown'+str(i)].Integral(),htop['muRFcorrdDown'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewUp']['ewk']  = max(hewk['muRUp'+str(i)].Integral(),hewk['muFUp'+str(i)].Integral(),hewk['muRFcorrdUp'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewDown']['ewk']= min(hewk['muRDown'+str(i)].Integral(),hewk['muFDown'+str(i)].Integral(),hewk['muRFcorrdDown'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewUp']['qcd']  = max(hqcd['muRUp'+str(i)].Integral(),hqcd['muFUp'+str(i)].Integral(),hqcd['muRFcorrdUp'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewDown']['qcd']= min(hqcd['muRDown'+str(i)].Integral(),hqcd['muFDown'+str(i)].Integral(),hqcd['muRFcorrdDown'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewUp'][signal]  = max(hsig['muRUp'+str(i)].Integral(),hsig['muFUp'+str(i)].Integral(),hsig['muRFcorrdUp'+str(i)].Integral())
					yieldTable[histoPrefix+'muRFcorrdNewDown'][signal]= min(hsig['muRDown'+str(i)].Integral(),hsig['muFDown'+str(i)].Integral(),hsig['muRFcorrdDown'+str(i)].Integral())
					
					#PDF
					topPDFweights = []
					ewkPDFweights = []
					qcdPDFweights = []
					sigPDFweights = []
					for pdfInd in range(100):
						topPDFweights.append(htop['pdf'+str(pdfInd)+'_'+str(i)].Integral())
						ewkPDFweights.append(hewk['pdf'+str(pdfInd)+'_'+str(i)].Integral())
						qcdPDFweights.append(hqcd['pdf'+str(pdfInd)+'_'+str(i)].Integral())
						sigPDFweights.append(hsig['pdf'+str(pdfInd)+'_'+str(i)].Integral())
					yieldTable[histoPrefix+'pdfNewUp']['top']  = htop['pdf'+str(sorted(range(len(topPDFweights)), key=lambda k: topPDFweights[k])[83])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown']['top']= htop['pdf'+str(sorted(range(len(topPDFweights)), key=lambda k: topPDFweights[k])[15])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewUp']['ewk']  = hewk['pdf'+str(sorted(range(len(ewkPDFweights)), key=lambda k: ewkPDFweights[k])[83])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown']['ewk']= hewk['pdf'+str(sorted(range(len(ewkPDFweights)), key=lambda k: ewkPDFweights[k])[15])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewUp']['qcd']  = hqcd['pdf'+str(sorted(range(len(qcdPDFweights)), key=lambda k: qcdPDFweights[k])[83])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown']['qcd']= hqcd['pdf'+str(sorted(range(len(qcdPDFweights)), key=lambda k: qcdPDFweights[k])[15])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewUp'][signal]  = hsig['pdf'+str(sorted(range(len(sigPDFweights)), key=lambda k: sigPDFweights[k])[83])+'_'+str(i)].Integral()
					yieldTable[histoPrefix+'pdfNewDown'][signal]= hsig['pdf'+str(sorted(range(len(sigPDFweights)), key=lambda k: sigPDFweights[k])[15])+'_'+str(i)].Integral()

				#prepare MC yield error table
				yieldStatErrTable[histoPrefix]['top']    = 0.
				yieldStatErrTable[histoPrefix]['ewk']    = 0.
				yieldStatErrTable[histoPrefix]['qcd']    = 0.
				yieldStatErrTable[histoPrefix]['totBkg'] = 0.
				yieldStatErrTable[histoPrefix]['data']   = 0.
				yieldStatErrTable[histoPrefix]['dataOverBkg']= 0.
				yieldStatErrTable[histoPrefix]['VV']     = 0.
				yieldStatErrTable[histoPrefix]['VVV']    = 0.
				yieldStatErrTable[histoPrefix]['TTV']    = 0.
				yieldStatErrTable[histoPrefix]['QCD']    = 0.
				yieldStatErrTable[histoPrefix]['ddbkg']  = 0.
				yieldStatErrTable[histoPrefix][signal]   = 0.

				for ibin in range(1,hsig[i].GetXaxis().GetNbins()+1):
					yieldStatErrTable[histoPrefix]['top']    += htop[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['ewk']    += hewk[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['qcd']    += hqcd[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['totBkg'] += htop[i].GetBinError(ibin)**2+hewk[i].GetBinError(ibin)**2+hqcd[i].GetBinError(ibin)**2+hddbkg[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['data']   += hdata[i].GetBinError(ibin)**2
# 					yieldStatErrTable[histoPrefix]['WJets']  += hwjets[i].GetBinError(ibin)**2
# 					yieldStatErrTable[histoPrefix]['ZJets']  += hzjets[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['VV']     += hvv[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['VVV']    += hvvv[i].GetBinError(ibin)**2
# 					yieldStatErrTable[histoPrefix]['TTW']    += httw[i].GetBinError(ibin)**2
# 					yieldStatErrTable[histoPrefix]['TTZ']    += httz[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['TTV']    += httv[i].GetBinError(ibin)**2					
# 					yieldStatErrTable[histoPrefix]['TTJets'] += httjets[i].GetBinError(ibin)**2
# 					yieldStatErrTable[histoPrefix]['T']      += ht[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['QCD']    += hqcd[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix]['ddbkg']  += hddbkg[i].GetBinError(ibin)**2
					yieldStatErrTable[histoPrefix][signal]   += hsig[i].GetBinError(ibin)**2
					
				hqcdY[signal].SetBinContent(catInd,yieldTable[histoPrefix]['qcd'])
				hewkY[signal].SetBinContent(catInd,yieldTable[histoPrefix]['ewk'])
				htopY[signal].SetBinContent(catInd,yieldTable[histoPrefix]['top'])
				hddbkgY[signal].SetBinContent(catInd,yieldTable[histoPrefix]['ddbkg'])
				hdataY[signal].SetBinContent(catInd,yieldTable[histoPrefix]['data'])
				hsigY[signal].SetBinContent(catInd,yieldTable[histoPrefix][signal])

				hqcdY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix]['qcd']))
				hewkY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix]['ewk']))
				htopY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix]['top']))
				hddbkgY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix]['ddbkg']))
				hdataY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix]['data']))
				hsigY[signal].SetBinError(catInd,math.sqrt(yieldStatErrTable[histoPrefix][signal]))
				
				#systematics
				if doAllSys:
					for systematic in systematicList+['pdfNew','muRFcorrdNew']:
						for ud in ['Up','Down']:
							if systematic!='toppt' and systematic!='PR' and systematic!='FR':
								hqcdY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud]['qcd'])
								hewkY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud]['ewk'])
								htopY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud]['top'])
								hsigY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud][signal])
							if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
								htopY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud]['top'])
							if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
								hddbkgY[signal+systematic+ud].SetBinContent(catInd,yieldTable[histoPrefix+systematic+ud]['ddbkg'])
					for systematic in normSystematics.keys():
						hqcdY[signal+systematic+'Up'].SetBinContent(catInd,yieldTable[histoPrefix]['qcd']*normSystematics[systematic][cat[0]])
						hewkY[signal+systematic+'Up'].SetBinContent(catInd,yieldTable[histoPrefix]['ewk']*normSystematics[systematic][cat[0]])
						htopY[signal+systematic+'Up'].SetBinContent(catInd,yieldTable[histoPrefix]['top']*normSystematics[systematic][cat[0]])
						hsigY[signal+systematic+'Up'].SetBinContent(catInd,yieldTable[histoPrefix][signal]*normSystematics[systematic][cat[0]])
						hqcdY[signal+systematic+'Down'].SetBinContent(catInd,yieldTable[histoPrefix]['qcd']*(2.-normSystematics[systematic][cat[0]]))
						hewkY[signal+systematic+'Down'].SetBinContent(catInd,yieldTable[histoPrefix]['ewk']*(2.-normSystematics[systematic][cat[0]]))
						htopY[signal+systematic+'Down'].SetBinContent(catInd,yieldTable[histoPrefix]['top']*(2.-normSystematics[systematic][cat[0]]))
						hsigY[signal+systematic+'Down'].SetBinContent(catInd,yieldTable[histoPrefix][signal]*(2.-normSystematics[systematic][cat[0]]))
				catInd+=1

				#scale signal cross section to 1pb
				#write theta histograms in root file, avoid having processes with no event yield (to make theta happy) 
# 				if hsig[i].Integral() > 0:  
# 					if scaleSignalXsecTo1pb: hsig[i].Scale(1./xsec[signal])
# 					hsig[i].Write()
# 					if doAllSys:
# 						for systematic in systematicList:
# 							if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
# 							if scaleSignalXsecTo1pb: 
# 								hsig[systematic+'Up'+str(i)].Scale(1./xsec[signal])
# 								hsig[systematic+'Down'+str(i)].Scale(1./xsec[signal])
# 							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
# 								hsig[systematic+'Up'+str(i)].Scale(hsig[i].Integral()/hsig[systematic+'Up'+str(i)].Integral())
# 								hsig[systematic+'Down'+str(i)].Scale(hsig[i].Integral()/hsig[systematic+'Down'+str(i)].Integral())
# 							hsig[systematic+'Up'+str(i)].Write()
# 							hsig[systematic+'Down'+str(i)].Write()
# 						for pdfInd in range(100): hsig['pdf'+str(pdfInd)+'_'+str(i)].Write()
# 				if htop[i].Integral() > 0:  
# 					htop[i].Write()
# 					if doAllSys:
# 						for systematic in systematicList:
# 							if systematic=='PR' or systematic=='FR': continue
# 							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
# 								htop[systematic+'Up'+str(i)].Scale(htop[i].Integral()/htop[systematic+'Up'+str(i)].Integral())
# 								htop[systematic+'Down'+str(i)].Scale(htop[i].Integral()/htop[systematic+'Down'+str(i)].Integral())  
# 							htop[systematic+'Up'+str(i)].Write()
# 							htop[systematic+'Down'+str(i)].Write()
# 						for pdfInd in range(100): htop['pdf'+str(pdfInd)+'_'+str(i)].Write()
# 				if hewk[i].Integral() > 0:  
# 					hewk[i].Write()
# 					if doAllSys:
# 						for systematic in systematicList:
# 							if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
# 							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
# 								hewk[systematic+'Up'+str(i)].Scale(hewk[i].Integral()/hewk[systematic+'Up'+str(i)].Integral())
# 								hewk[systematic+'Down'+str(i)].Scale(hewk[i].Integral()/hewk[systematic+'Down'+str(i)].Integral()) 
# 							hewk[systematic+'Up'+str(i)].Write()
# 							hewk[systematic+'Down'+str(i)].Write()
# 						for pdfInd in range(100): hewk['pdf'+str(pdfInd)+'_'+str(i)].Write()
# 				if hqcd[i].Integral() > 0:  
# 					hqcd[i].Write()
# 					if doAllSys:
# 						for systematic in systematicList:
# 							if systematic=='toppt' or systematic=='PR' or systematic=='FR': continue
# 							if normalizeRENORM_PDF and (systematic.startswith('mu') or systematic=='pdf'):
# 								hqcd[systematic+'Up'+str(i)].Scale(hqcd[i].Integral()/hqcd[systematic+'Up'+str(i)].Integral())
# 								hqcd[systematic+'Down'+str(i)].Scale(hqcd[i].Integral()/hqcd[systematic+'Down'+str(i)].Integral()) 
# 							hqcd[systematic+'Up'+str(i)].Write()
# 							hqcd[systematic+'Down'+str(i)].Write()
# 						for pdfInd in range(100): hqcd['pdf'+str(pdfInd)+'_'+str(i)].Write()
# 				if hddbkg[i].Integral() > 0:  
# 					hddbkg[i].Write()
# 					if doAllSys:
# 						for systematic in systematicList:
# 							if systematic!='PR' or systematic!='FR': continue
# 							hddbkg[systematic+'Up'+str(i)].Write()
# 							hddbkg[systematic+'Down'+str(i)].Write()
# 				hdata[i].Write()
				i+=1
			hdataY[signal].Write()
			if hsigY[signal].Integral() > 0:  
				if scaleSignalXsecTo1pb: hsigY[signal].Scale(1./xsec[signal])
				hsigY[signal].Write()
			if htopY[signal].Integral() > 0: htopY[signal].Write()
			if hewkY[signal].Integral() > 0: hewkY[signal].Write()
			if hqcdY[signal].Integral() > 0: hqcdY[signal].Write()
			if hddbkgY[signal].Integral() > 0: hddbkgY[signal].Write()
			#systematics
			if doAllSys:
				for systematic in systematicList+['pdfNew','muRFcorrdNew']+normSystematics.keys():
					for ud in ['Up','Down']:
						if systematic!='toppt' and systematic!='PR' and systematic!='FR':
							if hqcdY[signal+systematic+ud].Integral() > 0: hqcdY[signal+systematic+ud].Write()
							if hewkY[signal+systematic+ud].Integral() > 0: hewkY[signal+systematic+ud].Write()
							if htopY[signal+systematic+ud].Integral() > 0: htopY[signal+systematic+ud].Write()
							if hsigY[signal+systematic+ud].Integral() > 0:
								if scaleSignalXsecTo1pb: hsigY[signal+systematic+ud].Scale(1./xsec[signal])
								hsigY[signal+systematic+ud].Write()
						if systematic=='toppt': # top pt is only on the ttbar sample, so it needs special treatment!
							if htopY[signal+systematic+ud].Integral() > 0: htopY[signal+systematic+ud].Write()
						if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
							if hddbkgY[signal+systematic+ud].Integral() > 0: hddbkgY[signal+systematic+ud].Write()
			outputRfile.Close()
	
		stdout_old = sys.stdout
		logFile = open(outDir+'/yields_'+discriminant+BRconfStr+'_'+lumiStr+'fb'+'.txt','a')
		sys.stdout = logFile

		## PRINTING YIELD TABLE WITH STATISTICAL UNCERTAINTIES ##
		#first print table without background grouping
		ljust_i = 1
		print 'CUTS:',cutString
		print
		print 'YIELDS'.ljust(20*ljust_i), 
		for bkg in bkgStackList: print bkg.ljust(ljust_i),
		print 'data'.ljust(ljust_i),
		print
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for bkg in bkgStackList:
				print str(yieldTable[histoPrefix][bkg]).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
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
		print 'qcd'.ljust(ljust_i),
		print 'ddbkg'.ljust(ljust_i),
		print 'data'.ljust(ljust_i),
		print
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['ewk']).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['top']).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['qcd']).ljust(ljust_i),
			print str(yieldTable[histoPrefix]['ddbkg']).ljust(ljust_i),			
			print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['ewk'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['top'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['qcd'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['ddbkg'])).ljust(ljust_i),
			print str(math.sqrt(yieldStatErrTable[histoPrefix]['data'])).ljust(ljust_i),
			print

		#print yields for signals
		print
		print 'YIELDS'.ljust(20*ljust_i), 
		for sig in sigList: print sig.ljust(ljust_i),
		print
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
			print (catStr).ljust(ljust_i),
			for sig in sigList:
				print str(yieldTable[histoPrefix][sig]).ljust(ljust_i),
			print

		print 'YIELDS ERRORS'
		for cat in catList:
			tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
			catStr='is'+cat[0]+'_'+tagStr
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
				tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
				catStr='is'+cat[0]+'_'+tagStr
				print (catStr).ljust(ljust_i),
			print
			for process in ['qcd','ewk','top','ddbkg']+sigList:
				print process.ljust(ljust_i),
				print
				for ud in ['Up','Down']:
					for systematic in systematicList+['pdfNew','muRFcorrdNew']:
						if systematic=='toppt' and process!='top': continue
						if not (process=='ddbkg' or systematic=='PR' or systematic=='FR'):
							print (systematic+ud).ljust(ljust_i),
							for cat in catList:
								tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
								catStr='is'+cat[0]+'_'+tagStr
								histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
								print ' & '+str(round_sig(yieldTable[histoPrefix+systematic+ud][process]/(yieldTable[histoPrefix][process]+1e-20),2)),
							print '\\\\',
							print
						if process=='ddbkg' and (systematic=='PR' or systematic=='FR'):
							print (systematic+ud).ljust(ljust_i),
							for cat in catList:
								tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
								catStr='is'+cat[0]+'_'+tagStr
								histoPrefix=discriminant+'_'+lumiStr+'fb_'+catStr
								print ' & '+str(round_sig(yieldTable[histoPrefix+systematic+ud][process]/(yieldTable[histoPrefix][process]+1e-20),2)),
							print '\\\\',
							print
		
		sys.stdout = stdout_old
		logFile.close()

def readTree(file):
	if not os.path.exists(file): 
		print "Error: File does not exist! Aborting ...",file
		os._exit(1)
	tFile = R.TFile(file,'READ')
	tTree = tFile.Get('ljmet')
	return tFile, tTree

print "READING TREES"
shapesFiles = ['jec','jer','btag']#,'jsf']
tTreeData = {}
tFileData = {}
for data in dataList:
	print "READING:", data
	tFileData[data],tTreeData[data]=readTree(step1Dir+'/'+samples[data]+'_hadd.root')

tTreeSig = {}
tFileSig = {}
for sig in sigList:
	for decay in decays:
		print "READING:", sig+decay
		print "        nominal"
		tFileSig[sig+decay],tTreeSig[sig+decay]=readTree(step1Dir+'/'+samples[sig+decay]+'_hadd.root')
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					print "        "+syst+ud
					tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[sig+decay]+'_hadd.root')

tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList:
	print "READING:",bkg
	print "        nominal"
	tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root')
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if 'DataDriven' in bkg: continue
				else:
					print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[bkg]+'_hadd.root')
print "FINISHED READING"

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
			'HT':('AK4HT',linspace(0, 5000, 51).tolist(),';H_{T} (GeV);'),
			'ST':('AK4HTpMETpLepPt',linspace(0, 5000, 51).tolist(),';S_{T} (GeV);'),
			'minMlb':('minMleppBjet',linspace(0, 800, 51).tolist(),';min[M(l,b)] (GeV);'),
			'MallJetsPlusWleptonic':('M_AllJets_PlusWleptonic',linspace(0, 5000, 101).tolist(),';M (all jets + Wleptonic) (GeV);'),
			'x53Mass':('xftMass',linspace(0, 5000, 51).tolist(),';M (X_{5/3}) (GeV);'),
			}

iPlot='ST' #choose a discriminant from plotList!
print "PLOTTING:",iPlot
print "         LJMET Variable:",plotList[iPlot][0]
print "         X-AXIS TITLE  :",plotList[iPlot][2]
print "         BINNING USED  :",plotList[iPlot][1]

datahists = {}
bkghists  = {}
sighists  = {}
nCats  = len(catList)
catInd = 1
for cat in catList:
	category = {'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3]}
	for data in dataList: 
		datahists.update(analyze(tTreeData,data,cutList,False,iPlot,plotList[iPlot],category))
		if catInd==nCats: del tFileData[data]
	for bkg in bkgList: 
		bkghists.update(analyze(tTreeBkg,bkg,cutList,doAllSys,iPlot,plotList[iPlot],category))
		if catInd==nCats: del tFileBkg[bkg]
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
					if 'DataDriven' in bkg: continue			
					for ud in ['Up','Down']: del tFileSig[sig+decay+syst+ud]
	catInd+=1

#Negative Bin Correction
for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])

#OverFlow Correction
for data in datahists.keys(): overflow(datahists[data])
for bkg in bkghists.keys():   overflow(bkghists[bkg])
for sig in sighists.keys():   overflow(sighists[sig])

if scaleLumi:
	for key in bkghists.keys(): bkghists[key].Scale(lumiScaleCoeff)
	for key in sighists.keys(): sighists[key].Scale(lumiScaleCoeff)

print "MAKING CATEGORIES FOR TOTAL SIGNALS ..."
makeThetaCats(datahists,sighists,bkghists,iPlot)

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))


