#!/usr/bin/python

import os,sys,time,math,datetime,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
from cutList_SR import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv24_newMuTrkSF_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv25ttbar_newMuTrkSF_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv26ttbar_newMuTrkSF_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveVeryLooseMC_2017_3_6_rizki_PRv6_FRv28ttbar_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/' #--> PRv9
# step1Dir = '/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_newTT_2017_3_21_rizki_mcClosure_step1hadds/nominal/' #--> PRv9

# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_step1hadds/nominal/' #-->PRv9
# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_PRv9_FRv35_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_PRv9_FRv36_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_PRv9_FRv37_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_PRv9_FRv38_step1hadds/nominal/'
# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_mcFakeRate_saveLooseMC_2017_4_20_rizki_PRv9_FRv35_step1hadds/nominal/' #--> double checking but also with muFR=.14instead of .13 in FRv35

# step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_ttbarFakeRate_saveLooseMC_2017_4_17_dR0p01_PRv9_FRv45_elMVAaltFix_rizki_step1hadds/nominal'
#step1Dir = '/user_data/rsyarif/LJMet80x_3lep_Moriond17_ttbarFakeRate_saveLooseMC_2017_4_17_dR0p01_PRv9_FRv48_elMVAaltFix_rizki_step1hadds/nominal'
#step1Dir = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_062019_wywong_step1_FRv1_hadds_step2/'
#step1Dir = '/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_hadds_step2/'
#step1Dir = '/mnt/data/users/wwong/FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_newPR_hadds_step2/'
step1Dir = '/mnt/data/users/wwong/FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_PRv2_hadds_step2/'

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
doDDBKGscan= True

# cutString = 'isPassTrig'+str(int(cutList['isPassTrig']))+'_'+'isPassTrig_dilep'+str(int(cutList['isPassTrig_dilep']))+'_'+'isPassTrig_dilepHT'+str(int(cutList['isPassTrig_dilepHT']))+'_'+'isPassTrig_trilep'+str(int(cutList['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList['isPassTrilepton']))+'_'+'lep'+str(int(cutList['lepPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))
# cutString = 'lep'+str(int(cutList['lepPtCut']))+'_MET'+str(int(cutList['metCut']))+'_leadJet'+str(int(cutList['leadJetPtCut']))+'_subLeadJet'+str(int(cutList['subLeadJetPtCut']))+'_thirdJet'+str(int(cutList['thirdJetPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)


pfix='kinematics_80x_Exactly3Lep_ddbkgscan_step2_PRv6_ttbarClosure_TESTTTTING'
# pfix=''
pfix='FR_FWLJMET102X_3lep2017_062019_wiwong_step1hadds_step2_ttbarClosure'

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
pTbinsV2 = [0,30,40,60,80,100,120,140,160,180,500]
pTbinsV3 = [0,10,30,40,60,80,100,120,140,160,180,200,220,500]
Mbins = [-10.0, 0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 300.0]
# jetPtbins =  [0.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
jetPtbins =  [0.0, 30, 60.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 450.0, 550.0, 650.0, 750.0]
etaBins = [-4.0,-3.0,-2.4,-2.1,-1.2,0,1.2,2.1,2.4,3.0,4.0]

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)

	'lepPt' :('AllLeptonPt_PtOrdered',pTbins,';Leptons p_{T} (GeV);'),
	'ElPt' :('AllLeptonElPt_PtOrdered',pTbins,';Electron p_{T} (GeV);'),
	'MuPt' :('AllLeptonMuPt_PtOrdered',pTbins,';Muon p_{T} (GeV);'),

# 	'lep1Pt' :('AllLeptonPt_PtOrdered[0]',linspace(0, 500, 26).tolist(),';Lepton 1 p_{T} (GeV);'),
# 	'lep2Pt' :('AllLeptonPt_PtOrdered[1]',linspace(0, 300, 16).tolist(),';Lepton 2 p_{T} (GeV);'),
# 	'lep3Pt' :('AllLeptonPt_PtOrdered[2]',linspace(0, 300, 16).tolist(),';Lepton 3 p_{T} (GeV);'),

	'lep1Pt' :('AllLeptonPt_PtOrdered[0]',pTbins,';Lepton 1 p_{T} (GeV);'),
	'lep2Pt' :('AllLeptonPt_PtOrdered[1]',pTbins,';Lepton 2 p_{T} (GeV);'),
	'lep3Pt' :('AllLeptonPt_PtOrdered[2]',pTbins,';Lepton 3 p_{T} (GeV);'),

        'lepPtRebinned' :('AllLeptonPt_PtOrdered',pTbinsV2,';Leptons p_{T} (GeV);'),
        'lepPtRebinnedv1' :('AllLeptonPt_PtOrdered',linspace(0, 500, 2).tolist(),';Leptons p_{T} (GeV);'),
        'lepPtRebinnedv3' :('AllLeptonPt_PtOrdered',pTbinsV3,';Leptons p_{T} (GeV);'),

	'lepEta':('AllLeptonEta_PtOrdered',etaBins,';Lepton 1 #eta;'),
# 	'ElEta':('AllLeptonElEta_PtOrdered',etaBins,';Electron 1 #eta;'),
# 	'MuEta':('AllLeptonMuEta_PtOrdered',etaBins,';Mu 1 #eta;'),

# 	'lep1Eta':('AllLeptonEta_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';Lepton 1 #eta;'),
# 	'lep2Eta':('AllLeptonEta_PtOrdered[1]',linspace(-4, 4, 41).tolist(),';Lepton 2 #eta;'),
# 	'lep3Eta':('AllLeptonEta_PtOrdered[2]',linspace(-4, 4, 41).tolist(),';Lepton 3 #eta;'),

# 	'JetEta':('theJetEta_JetSubCalc_PtOrdered',linspace(-4, 4, 41).tolist(),';AK4 Jet #eta;'),
# 	'Jet1Eta':('theJetEta_JetSubCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';1^{st} AK4 Jet #eta;'),
# 	'Jet2Eta':('theJetEta_JetSubCalc_PtOrdered[0]',linspace(-4, 4, 41).tolist(),';2^{nd} AK4 Jet #eta;'),

# 	'JetPt' :('theJetPt_JetSubCalc_PtOrdered',jetPtbins,';AK4 Jet p_{T} (GeV);'),
# 	'Jet1Pt':('theJetPt_JetSubCalc_PtOrdered[0]',jetPtbins,';1^{st} AK4 Jet p_{T} (GeV);'),
# 	'Jet2Pt':('theJetPt_JetSubCalc_PtOrdered[1]',jetPtbins,';2^{nd} AK4 Jet p_{T} (GeV);'),

# 	'HTrebinned'    :('AK4HT',HTbins,';H_{T} (GeV);'),
	'STrebinned'    :('AK4HTpMETpLepPt',STbins,';S_{T} (GeV);'),
# 	'METrebinned'   :('corr_met_MultiLepCalc',METbins,';#slash{E}_{T} (GeV);'),

# 	'NJets' :('NJets_JetSubCalc',linspace(0, 15, 16).tolist(),';AK4 Jet multiplicity;'),
# 	'NBJets':('NJetsCSVwithSF_JetSubCalc',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),
# 	'NBJetsCorr':('NJetsCSVwithSF_JetSubCalc_noLepCorr',linspace(0, 10, 11).tolist(),';CSVIVFv2 Medium tag multiplicity;'),
	
	}

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

bkgList = []

#adding scans of ddbkg
# loop,run,dilep --> set in samples
for muFRindex in xrange(loop):
	for elFRindex in xrange(loop):
		if(doDDBKGscan):bkgList.append('MatrixBkg_muFR'+str(muFRindex+((int)(initial*100)))+'elFR'+str(elFRindex+((int)(initial*100))))

dataList=[]
if 'TT' in useWhichSampleForMatrix:dataList.append('TTTo2L2Nu')
if 'DY' in useWhichSampleForMatrix:dataList.append('DY50')
bkgList.append('MatrixBkg')
for ddbkgCat_ in ddbkgCat:
	bkgList.append('MatrixBkg'+ddbkgCat_)

###########################################################
#################### NORMALIZATIONS #######################
###########################################################

def negBinCorrection(hist): #set negative bin contents to zero and adjust the normalization
	norm0=hist.Integral()
	for iBin in range(0,hist.GetNbinsX()+2):
		#print("bin",iBin," = ", hist.GetBinContent(iBin))
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
	print "READING:", data	
	print "samples[",data,"]:", samples[data]	
	tFileData[data],tTreeData[data]=readTree(step1Dir+'/'+samples[data]+'_hadd.root')

tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList:
	#print "READING:",bkg
	#print "        nominal"
	if 'Matrix' in bkg: continue #all the ddbkg uses the same files as data.
	tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root')
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if 'Matrix' in bkg: continue
				else:
					print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[bkg]+'_hadd.root')
print "FINISHED READING"

###########################################################
#################### RUN ANALYSE.PY #######################
###########################################################

if len(sys.argv)>2: iPlot=sys.argv[2]
# else: iPlot='minMlb'
# else: iPlot='STrebinned'
else: iPlot='lepPt'
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
        if len(sys.argv)>1:
                outDir=sys.argv[1]
                outDir+='_'+datestr #+=pfix
                if not os.path.exists(outDir): os.system('mkdir '+outDir)
        else:
                #outDir = '/user_data/rsyarif/'
                outDir = '/mnt/data/users/wwong/'
#               outDir = os.getcwd()+'/'
                outDir+=pfix
                if not os.path.exists(outDir): os.system('mkdir '+outDir)
                #if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+outDir+'/'+cutString)
                #outDir+='/'+cutString
        if not os.path.exists(outDir+'/'+category): os.system('mkdir '+outDir+'/'+category)
        outDir+='/'+category
	for data in dataList: 
# 		print '+++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>  data = ' , data 		
		datahists.update(analyze(tTreeData,data,cutList,False,iPlot,plotList[iPlot],category))
		if catInd==nCats: del tFileData[data]
	for bkg in bkgList: 
# 		print '+++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>  bkg = ' , bkg 
		tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root') #open file here because there too many files to open
		bkghists.update(analyze(tTreeBkg,bkg,cutList,doAllSys,iPlot,plotList[iPlot],category))
		del tFileBkg[bkg] #close file everytime because there too many files to open.
		#if catInd==nCats: del tFileBkg[bkg]
		if doAllSys and catInd==nCats:
			for syst in shapesFiles:
				if 'Matrix' in bkg: continue
				for ud in ['Up','Down']: del tFileBkg[bkg+syst+ud]
	
	#Negative Bin Correction
	for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])

	#OverFlow Correction
	for data in datahists.keys(): 
		#print(data)
		overflow(datahists[data])
	for bkg in bkghists.keys():   overflow(bkghists[bkg])

	pickle.dump(datahists,open(outDir+'/datahists_'+iPlot+'.p','wb'))
	pickle.dump(bkghists,open(outDir+'/bkghists_'+iPlot+'.p','wb'))
	catInd+=1
	print 'Saving pickle files at:',outDir

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
