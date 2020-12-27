#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,getopt,fnmatch
from numpy import linspace
from weights import *
from analyze import *
from samples import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

#step1Dir_mc = '/user_data/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds_step2/nominal' # uses PR v9 FR v49
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_062019_wiwong_step1hadds_step2/'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_hadds_step2/'
#step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_TrigEff_hadds_step2/'
step1Dir_mc = '/mnt/data/users/wwong/FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_elIdSys_TrigEffWeight_pdf4LHC_hadds_step2/'
step1Dir_data = step1Dir_mc
#step1Dir_data = '/user_data/rsyarif/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds_step2/nominal' # uses PR v9 FR v3 
#step1Dir_data = step1Dir_mc #'/mnt/data/users/wwong/LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds_step2/nominal' # uses PR v9 FR v3 
#step1Dir_data = '/mnt/data/users/wwong/FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_hadds_step2/'


print 'grabbing data files from ', step1Dir_data
print 'grabbing mc files from ', step1Dir_mc

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

# pfix='optimization_PRv6_FRv24_newMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv24_newFRsys_AllSys_BB_TEST'
#pfix='optimization_reMiniAOD_dummy'
pfix='optimization_'+step1Dir_data.split('/')[-1]

pfix+='_'+datestr

if len(sys.argv)>1:
        outDir=sys.argv[1]
else:
        outDir = os.getcwd()+'/'
        outDir+=pfix

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

# bkgStackList = ['VV','VVV','TTV','ddbkg']
# vvList    = ['WZ','ZZ']
# vvvList   = ['WWW','WWZ','WZZ','ZZZ']
# ttvList   = ['TTWl','TTZl']
# #ttjetList = ['TTJetsPH']
# # tList     = ['Tt','Ts','TtW','TbtW']
# 
whichSignal = 'TT' #TT, BB, or X53X53
#whichSignal = 'BB' #TT, BB, or X53X53
if '_BB_' in outDir: whichSignal = 'BB'
if whichSignal == 'BB' and not ('_BB_' in outDir):
	print("ERROR!!!! outDir not matching whichSignal!!!!")
        exit()
print 'whichSignal = ', whichSignal

signalMassRange = [1000,1800]
if '_BB_' in outDir: signalMassRange = [900,1800]
sigList = [whichSignal+'M'+str(mass) for mass in range(signalMassRange[0],signalMassRange[1]+100,100)]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in range(signalMassRange[0],signalMassRange[1]+100,100) for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='X53X53': decays = [''] #decays to tWtW 100% of the time
 
# doBRScan = False
# BRs={}
# BRs['BW']=[0.50,0.0,0.0]#,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,1.0]
# BRs['TH']=[0.25,0.0,0.2]#,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0]
# BRs['TZ']=[0.25,1.0,0.8]#,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.0]
# nBRconf=len(BRs['BW'])
# if not doBRScan: nBRconf=1

# topList = ['TTWl','TTZl'] #NoTTJets, No singleT
# ewkList = ['WZ','ZZ','WWW','WWZ','WZZ','ZZZ'] #No DY, WJets, WW
# # ewkList = ['WZ','WWW']#No DY, WJets, WW
# 
# scaleSignalXsecTo1pb = True # this has to be "True" if you are making templates for limit calculation!!!!!!!!
scaleLumi = False
lumiScaleCoeff = 1.

doAllSys = True


try: 
	opts, args = getopt.getopt(sys.argv[2:], "", [
	                                              "lep1PtCut=",
	                                              "jetPtCut=",
						      "bJet1PtCut=",
	                                              "metCut=",
	                                              "njetsCut=",
	                                              "nbjetsCut=",
	                                              "htCut=",
	                                              "stCut=",
	                                              "mllOSCut=",
	                                              "isPassTrig_dilep=",
	                                              "isPassTriLepton=",
	                                              "ptRelCut=",
	                                              "minDRlepJetCut=",
	                                              ])
	print '[opts][args]:',opts,args
except getopt.GetoptError as err:
	print str(err)
	sys.exit(1)

lep1PtCut=0#40
jetPtCut=0#300
bJet1PtCut=0
metCut=20
njetsCut=3
nbjetsCut=1
htCut=0
stCut=0
mllOSCut=20
isPassTrig_dilep=1
isPassTrilepton=1
ptRelCut=0
minDRlepJetCut=0

catList  =['EEE','EEM','EMM','MMM']

for o, a in opts:
	print 'o, a in opts: ',o, a
	if o == '--lep1PtCut': lep1PtCut = float(a)
	if o == '--jetPtCut': jetPtCut = float(a)
        if o == '--bJet1PtCut': bJet1PtCut = float(a)
	if o == '--metCut': metCut = float(a)
	if o == '--njetsCut': njetsCut = float(a)
	if o == '--nbjetsCut': nbjetsCut = float(a)
	if o == '--htCut': htCut = float(a)
	if o == '--stCut': stCut = float(a)
	if o == '--mllOSCut': mllOSCut = float(a)
	if o == '--ptRelCut': ptRelCut = float(a)
	if o == '--minDRlepJetCut': minDRlepJetCut = float(a)
	if o == '--whichCat': catList = [str(a)]

cutList = {
		   'lep1PtCut':lep1PtCut,
		   'jetPtCut':jetPtCut,
                   'bJet1PtCut':bJet1PtCut,
		   'metCut':metCut,
		   'njetsCut':njetsCut,
		   'nbjetsCut':nbjetsCut,
		   'htCut':htCut,
		   'stCut':stCut,
		   'mllOSCut':mllOSCut,
		   'isPassTrig_dilep':isPassTrig_dilep,
		   'isPassTrilepton':isPassTrilepton,
		   'ptRelCut':ptRelCut,
		   'minDRlepJetCut':minDRlepJetCut,
		   }

cutString = 'NJets'+str(int(cutList['njetsCut']))
for ikey in cutList.keys():
	if ikey!='njetsCut' and cutList[ikey]>0:
		cutString += '_'+ikey[:-3]+str(int(cutList[ikey]))

#cutString  = 'lep1Pt'+str(int(cutList['lep1PtCut']))
#cutString += '_jetPt'+str(int(cutList['jetPtCut']))
#cutString += '_MET'+str(int(cutList['metCut']))
#cutString += '_NJets'+str(int(cutList['njetsCut']))
#cutString += '_NBJets'+str(int(cutList['nbjetsCut']))
#cutString += '_HT'+str(int(cutList['htCut']))
#cutString += '_ST'+str(int(cutList['stCut']))
#cutString += '_mllOS'+str(int(cutList['mllOSCut']))
#cutString += '_ptRel'+str(cutList['ptRelCut'])
#cutString += '_minDRlJ'+str(cutList['minDRlepJetCut']).replace('.','p')


# normSystematics = {
# # 					'elIdSys':{'EEE':1.017,'EEM':1.014,'EMM':1.01,'MMM':1.00},
# # 					'muIdSys':{'EEE':1.00,'EEM':1.01,'EMM':1.014,'MMM':1.017},
# # 					'elIsoSys':{'EEE':1.017,'EEM':1.014,'EMM':1.01,'MMM':1.00},
# # 					'muIsoSys':{'EEE':1.00,'EEM':1.01,'EMM':1.014,'MMM':1.017},
# 					'elIdSys':{'EEE':1.03,'EEM':1.02,'EMM':1.01,'MMM':1.00},
# 					'muIdSys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.03},
# 					'elIsoSys':{'EEE':1.03,'EEM':1.02,'EMM':1.01,'MMM':1.00},
# 					'muIsoSys':{'EEE':1.00,'EEM':1.01,'EMM':1.02,'MMM':1.03},
# 					'elelelTrigSys':{'EEE':1.03,'EEM':1.00,'EMM':1.00,'MMM':1.00},
# 					'elelmuTrigSys':{'EEE':1.00,'EEM':1.03,'EMM':1.00,'MMM':1.00},
# 					'elmumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.03,'MMM':1.00},
# 					'mumumuTrigSys':{'EEE':1.00,'EEM':1.00,'EMM':1.00,'MMM':1.03},
# 					}

# ddbkgSystematics = {
# 					'elPRsys':{'EEE':1.38,'EEM':1.12,'EMM':1.07,'MMM':1.00},
# 					'muPRsys':{'EEE':1.00,'EEM':1.02,'EMM':1.04,'MMM':1.09},
# 					'muFReta':{'EEE':1.00,'EEM':1.22,'EMM':1.11,'MMM':1.48}
# 					}

# ddbkgSystematics = {
# 					'elPRsys':{'EEE':1.09,'EEM':1.15,'EMM':1.08,'MMM':1.00},
# 					'muPRsys':{'EEE':1.00,'EEM':1.04,'EMM':1.08,'MMM':1.17},
# 					'muFReta':{'EEE':1.00,'EEM':1.13,'EMM':1.10,'MMM':1.24}
# 					}


if not os.path.exists(outDir): os.system('mkdir '+outDir)
if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
outDir+='/'+cutString

#if len(sys.argv)>1: 
#	outDir=sys.argv[1]
#        if not os.path.exists(outDir): os.system('mkdir '+outDir)
#        if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
#        outDir+='/'+cutString
#else: 
#	outDir = os.getcwd()+'/'
#	outDir+=pfix
#	if not os.path.exists(outDir): os.system('mkdir '+outDir)
#	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
#	outDir+='/'+cutString

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
#################### READING TREES #######################
###########################################################

#def readTree(file):
#	if not os.path.exists(file): 
#		print "Error: File does not exist! Aborting ...",file
#		os._exit(1)
#	tFile = R.TFile(file,'READ')
#	tTree = tFile.Get('ljmet')
#	return tFile, tTree

def readTree(file,tree):
	if not os.path.exists(file):
		print "Error: File does not exist! Aborting ...",file
		os._exit(1)
	tFile = R.TFile(file,'READ')
	tTree = tFile.Get(tree)
	return tFile, tTree

displayProcess=True
print "READING TREES"
shapesFiles = ['jec','jer']
# shapesFiles = []
tTreeData = {}
tFileData = {}
for data in dataList:
	if(displayProcess):print "READING:", data
	tFileData[data],tTreeData[data]=readTree(step1Dir_data+'/'+samples[data]+'_hadd.root','ljmet')

tTreeSig = {}
tFileSig = {}
for sig in sigList:
	for decay in decays:
		if(displayProcess):print "READING:", sig+decay
		if(displayProcess):print "        nominal"
		tFileSig[sig+decay],tTreeSig[sig+decay]=readTree(step1Dir_mc+'/'+samples[sig+decay]+'_hadd.root','ljmet')
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					if(displayProcess):print "        "+syst+ud
					tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readTree(step1Dir_mc+'/'+samples[sig+decay]+'_hadd.root','ljmet_'+syst.upper()+ud.lower())
					if(displayProcess):print(tTreeSig[sig+decay+syst+ud].GetEntriesFast())

tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList:
	if(displayProcess):print "READING:",bkg
	if(displayProcess):print "        nominal"
	if "DataDrivenBkg" in bkg:
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir_data+'/'+samples[bkg]+'_hadd.root','ljmet')
	else:
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir_mc+'/'+samples[bkg]+'_hadd.root','ljmet')
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if 'DataDriven' in bkg: continue
				else:
					if(displayProcess):print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir_mc+'/'+samples[bkg]+'_hadd.root','ljmet_'+syst.upper()+ud.lower())
				if(displayProcess):print(tTreeBkg[bkg+syst+ud].GetEntriesFast())
print "FINISHED READING"


###########################################################
######################## ANALYZE ##########################
###########################################################

HTbins = [0,100,200,300,400,500,600,800,1000,2000]
STbins = [0,100,200,300,400,500,600,800,1000,1400,2000]
STbinsv2 = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,2000]
MlllBbins=[100,200,300,400,500,600,700,800,1000,1500]
plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
			'HT':('AK4HT',linspace(0, 5000, 51).tolist(),';H_{T} (GeV);'),
			'HTrebinned'    :('AK4HT',HTbins,';H_{T} (GeV);'),
			'ST':('AK4HTpMETpLepPt',linspace(0, 5000, 51).tolist(),';S_{T} (GeV);'),
			'STrebinned'    :('AK4HTpMETpLepPt',STbins,';S_{T} (GeV);'),
			'STrebinnedv2'    :('AK4HTpMETpLepPt',STbinsv2,';S_{T} (GeV);'),
			'NJets' :('NJets_MultiLepCalc',linspace(0, 15, 16).tolist(),';AK4 Jet multiplicity;'),
			'minMlllBv2':('minMlllBjet',linspace(0, 1500, 31).tolist(),';min[M(trilepton, b-jet)];'),
			'minMlllBv4':('minMlllBjet',MlllBbins,';min[M(trilepton, b-jet)];'),
			}

# iPlot='ST' #choose a discriminant from plotList!
# iPlot='STrebinned' #choose a discriminant from plotList!
iPlot='STrebinnedv2' #choose a discriminant from plotList!
# iPlot='HTrebinned' #choose a discriminant from plotList!
# iPlot='NJets' #choose a discriminant from plotList! NJets can only be used with CutNCount!! Use STrebinned for shape!
if('FRv48sys' in step1Dir_data): iPlot='minMlllBv4' #choose a discriminant from plotList!
if(displayProcess):print "PLOTTING:",iPlot
if(displayProcess):print "         LJMET Variable:",plotList[iPlot][0]
if(displayProcess):print "         X-AXIS TITLE  :",plotList[iPlot][2]
if(displayProcess):print "         BINNING USED  :",plotList[iPlot][1]


print "START ANALYZE"

# outDir = '/user_data/rsyarif/'
# outDir+=pfix
# if not os.path.exists(outDir): os.system('mkdir '+outDir)
# if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
# outDir+='/'+cutString

datahists = {}
bkghists  = {}
sighists  = {}

nCats  = len(catList)
catInd = 1
for cat in catList:
	category = cat
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


	#Negative Bin Correction
	for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])

	#OverFlow Correction
	for data in datahists.keys(): overflow(datahists[data])
	for bkg in bkghists.keys():   overflow(bkghists[bkg])
	for sig in sighists.keys():   overflow(sighists[sig])

	if scaleLumi:
		for key in bkghists.keys(): bkghists[key].Scale(lumiScaleCoeff)
		for key in sighists.keys(): sighists[key].Scale(lumiScaleCoeff)

	pickle.dump(datahists,open(outDir+'/datahists_'+iPlot+'_'+cat+'.p','wb'))
	pickle.dump(bkghists,open(outDir+'/bkghists_'+iPlot+'_'+cat+'.p','wb'))
	pickle.dump(sighists,open(outDir+'/sighists_'+iPlot+'_'+cat+'.p','wb'))
	print 'Saving pickle files at:',outDir
	catInd+=1
print "FINISHED ANALYZE"


print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
