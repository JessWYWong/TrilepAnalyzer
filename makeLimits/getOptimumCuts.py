#from ROOT import *
from array import array
#from numpy import linspace
from math import *
import os,sys,itertools

#gROOT.SetBatch(1)

from tdrStyle import *
setTDRStyle()

lumiPlot = '2.3'
lumiStr = '2p318'
distribution = 'ST'
# limitDir='/user_data/rsyarif/limits/all/'
# limitDir='/user_data/rsyarif/limits/allSys/'
# limitDir='/user_data/rsyarif/limits/allSys_sig__muRFcorrdNew_sig__pdfNew_TrigSys/'
# limitDir='/user_data/rsyarif/limits/allSys_sig__muRFcorrdNew_sig__pdfNew_no_jec_no_jer/'
limitDir='/user_data/rsyarif/limits/76in74x_allSys_sig__muRFcorrdNew_sig__pdfNew/'

postfix = '' # for plot names in order to save them as different files
stat=''#0.75
isRebinned=''#'_rebinned_modified'+str(stat).replace('.','p')
print "CATEGORY",isRebinned

# lepPtCutList  = [0]
# jet1PtCutList = [0]
# jet2PtCutList = [0]
# metCutList    = [0]
# njetsCutList  = [0,1,2,3]
# nbjetsCutList = [0,1,2,3]
# jet3PtCutList = [0]
# jet4PtCutList = [0]
# jet5PtCutList = [0]
# drCutList     = [0]
# Wjet1PtCutList= [0]
# bjet1PtCutList= [0]
# htCutList     = [0]
# stCutList     = [0,500,600,700,800,900,1000,1100]
# minMlbCutList = [0]

lepPtCutList  = [20,25]
jet1PtCutList = [0]
jet2PtCutList = [0]
metCutList    = [20,30]
njetsCutList  = [0,1,2,3]
nbjetsCutList = [0,1,2,3]
jet3PtCutList = [0]
jet4PtCutList = [0]
jet5PtCutList = [0]
drCutList     = [0]
Wjet1PtCutList= [0]
bjet1PtCutList= [0]
htCutList     = [0]
stCutList     = [0,500,600,700,800,900,1000,1100,1200,1300]
minMlbCutList = [0]

cutConfigs = list(itertools.product(lepPtCutList,jet1PtCutList,jet2PtCutList,metCutList,njetsCutList,nbjetsCutList,jet3PtCutList,jet4PtCutList,jet5PtCutList,drCutList,Wjet1PtCutList,bjet1PtCutList,htCutList,stCutList,minMlbCutList))

massPoints = [800]
mass = array('d', massPoints)
masserr = array('d', [0]*len(massPoints))
mass_str = [str(item) for item in massPoints]

#theory_br = [.1285,.1285,.1285,.1285,.1285,.1285,.1285]
theory_xsec_dicts = {'700':0.455,'800':0.196,'900':0.0903,'1000':0.0440,'1100':0.0224,'1200':0.0118,'1300':0.00639}#,0.00354,0.00200,0.001148,0.000666,0.000391]
theory_xsec = [theory_xsec_dicts[item] for item in mass_str]

expBestCutStr = {}
expBestLimit  = {}
obsBestCutStr = {}
obsBestLimit  = {}
expWorstCutStr = {}
expWorstLimit  = {}
obsWorstCutStr = {}
obsWorstLimit  = {}
expLimits = {}
obsLimits = {}
for i in range(len(mass)):
	expLimits[mass_str[i]] = {}
	obsLimits[mass_str[i]] = {}
	expBestCutStr[mass_str[i]] = ''
	expBestLimit[mass_str[i]]  = 1e9
	obsBestCutStr[mass_str[i]] = ''
	obsBestLimit[mass_str[i]]  = 1e9
	expWorstCutStr[mass_str[i]] = ''
	expWorstLimit[mass_str[i]]  = -1.
	obsWorstCutStr[mass_str[i]] = ''
	obsWorstLimit[mass_str[i]]  = -1.
	
ind=1                                                                                               
for conf in cutConfigs:
	lepPtCut,jet1PtCut,jet2PtCut,metCut,njetsCut,nbjetsCut,jet3PtCut,jet4PtCut,jet5PtCut,drCut,Wjet1PtCut,bjet1PtCut,htCut,stCut,minMlbCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12],conf[13],conf[14]
	cutString = 'lep'+str(int(lepPtCut))+'_MET'+str(int(metCut))+'_1jet'+str(int(jet1PtCut))+'_2jet'+str(int(jet2PtCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_3jet'+str(int(jet3PtCut))+'_4jet'+str(int(jet4PtCut))+'_5jet'+str(int(jet5PtCut))+'_DR'+str(drCut)+'_1Wjet'+str(Wjet1PtCut)+'_1bjet'+str(bjet1PtCut)+'_HT'+str(htCut)+'_ST'+str(stCut)+'_minMlb'+str(minMlbCut)
	plotLimits = True
	for i in range(len(mass)):
		try: 
			ftemp = open(limitDir+'/'+cutString+'/limits_templates_'+distribution+'_TTM'+mass_str[i]+'_'+lumiStr+'fb'+isRebinned+'_expected.txt', 'rU')
		except: plotLimits = False
	if not plotLimits: continue
	#if leadJetPtCut==1000: continue

	exp   =array('d',[0 for i in range(len(mass))])
	obs   =array('d',[0 for i in range(len(mass))])
	for i in range(len(mass)):
		lims = {}

		fobs = open(limitDir+'/'+cutString+'/limits_templates_'+distribution+'_TTM'+mass_str[i]+'_'+lumiStr+'fb'+isRebinned+'_observed.txt', 'rU')
		linesObs = fobs.readlines()
		fobs.close()

		fexp = open(limitDir+'/'+cutString+'/limits_templates_'+distribution+'_TTM'+mass_str[i]+'_'+lumiStr+'fb'+isRebinned+'_expected.txt', 'rU')
		linesExp = fexp.readlines()
		fexp.close()

		obs[i] = float(linesObs[1].strip().split()[1])
		exp[i] = float(linesExp[1].strip().split()[1])

		lims[-1] = float(linesObs[1].strip().split()[1])
		lims[.5] = float(linesExp[1].strip().split()[1])
		lims[.16] = float(linesExp[1].strip().split()[4])
		lims[.84] = float(linesExp[1].strip().split()[5])
		lims[.025] = float(linesExp[1].strip().split()[2])
		lims[.975] = float(linesExp[1].strip().split()[3])
		expLimits[mass_str[i]][cutString] = exp[i]
		obsLimits[mass_str[i]][cutString] = obs[i]
		if exp[i]<=expBestLimit[mass_str[i]]:
			expBestLimit[mass_str[i]] = exp[i]
			expBestCutStr[mass_str[i]] = cutString
		if obs[i]<=obsBestLimit[mass_str[i]]:
			obsBestLimit[mass_str[i]] = obs[i]
			obsBestCutStr[mass_str[i]] = cutString

		if exp[i]>expWorstLimit[mass_str[i]]:
			expWorstLimit[mass_str[i]] = exp[i]
			expWorstCutStr[mass_str[i]] = cutString
		if obs[i]>obsWorstLimit[mass_str[i]]:
			obsWorstLimit[mass_str[i]] = obs[i]
			obsWorstCutStr[mass_str[i]] = cutString		
	ind+=1

print "********************************************************************************"
print "Run over", ind-1, "sets of cuts"
print "********************************************************************************"
print "********************************************************************************"
print "The best set of cuts:"
for i in range(len(mass)):
	print "Expected("+mass_str[i]+"GeV): "+expBestCutStr[mass_str[i]]+" with 95% CL: "+str(expBestLimit[mass_str[i]])
	print "Observed("+mass_str[i]+"GeV): "+obsBestCutStr[mass_str[i]]+" with 95% CL: "+str(obsBestLimit[mass_str[i]])
print "********************************************************************************"
print "The worst set of cuts:"
for i in range(len(mass)):
	print "Expected("+mass_str[i]+"GeV): "+expWorstCutStr[mass_str[i]]+" with 95% CL: "+str(expWorstLimit[mass_str[i]])
	print "Observed("+mass_str[i]+"GeV): "+obsWorstCutStr[mass_str[i]]+" with 95% CL: "+str(obsWorstLimit[mass_str[i]])
print "********************************************************************************"

# import pylab as pl
# massPoint = '800'
# 
# folder='.'
# outDir = folder+'/'+limitDir.split('/')[-2]+'plots'
# if not os.path.exists(outDir): os.system('mkdir '+outDir)
# outDir += '/optimizationInIndividualCats'
# if not os.path.exists(outDir): os.system('mkdir '+outDir)
# 
# bestLepPt  = expBestCutStr[massPoint][3:expBestCutStr[massPoint].find('_MET')]
# bestMET    = expBestCutStr[massPoint][expBestCutStr[massPoint].find('MET')+3:expBestCutStr[massPoint].find('_1jet')]
# bestJet1Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('1jet')+4:expBestCutStr[massPoint].find('_2jet')]
# bestJet2Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('2jet')+4:expBestCutStr[massPoint].find('_NJets')]
# bestJet3Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('3jet')+4:expBestCutStr[massPoint].find('_4jet')]
# bestNJets  = expBestCutStr[massPoint][expBestCutStr[massPoint].find('NJets')+5:expBestCutStr[massPoint].find('_NBJets')]
# bestDR     = expBestCutStr[massPoint][expBestCutStr[massPoint].find('DR')+2:expBestCutStr[massPoint].find('_1Wjet')]
# bestWJet1Pt= expBestCutStr[massPoint][expBestCutStr[massPoint].find('1Wjet')+5:expBestCutStr[massPoint].find('_1bjet')]
# bestBJet1Pt= expBestCutStr[massPoint][expBestCutStr[massPoint].find('1bjet')+5:expBestCutStr[massPoint].find('_HT')]
# bestST     = expBestCutStr[massPoint][expBestCutStr[massPoint].find('ST')+2:expBestCutStr[massPoint].find('_minMlb')]
# bestminMlb = expBestCutStr[massPoint][expBestCutStr[massPoint].find('minMlb')+6:]
# 
# fig_lep = pl.figure(0)
# x = [item for item in range(len(lepPtCutList))]
# xTicks = ['Pt(lep)>'+str(item) for item in lepPtCutList]
# y = [expLimits[massPoint]['lep'+str(item)+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in lepPtCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryLepPt'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryLepPt'+isRebinned+postfix+'.pdf')
# 
# fig_met = pl.figure(1)
# x = [item for item in range(len(metCutList))]
# xTicks = ['MET>'+str(item) for item in metCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+str(item)+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in metCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryMET'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryMET'+isRebinned+postfix+'.pdf')
# 
# jet1Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('1jet')+4:expBestCutStr[massPoint].find('_2jet')])
# jet2Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('2jet')+4:expBestCutStr[massPoint].find('_NJets')])
# jet3Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('3jet')+4:expBestCutStr[massPoint].find('_4jet')])
# fig_jet1 = pl.figure(2)
# x = [item for item in range(len(jet1PtCutList)) if jet1PtCutList[item] > jet2Pt]
# xTicks = ['Pt(j1)>'+str(item) for item in jet1PtCutList if item > jet2Pt]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+str(item)+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in jet1PtCutList if item > jet2Pt]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryJet1'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryJet1'+isRebinned+postfix+'.pdf')
# 
# fig_jet2 = pl.figure(3)
# x = [item for item in range(len(jet2PtCutList)) if jet2PtCutList[item] > jet3Pt and jet2PtCutList[item] < jet1Pt]
# xTicks = ['Pt(j2)>'+str(item) for item in jet2PtCutList if item > jet3Pt and item < jet1Pt]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+str(item)+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in jet2PtCutList if item > jet3Pt and item < jet1Pt]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryJet2'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryJet2'+isRebinned+postfix+'.pdf')
# 
# fig_jet3 = pl.figure(4)
# x = [item for item in range(len(jet3PtCutList)) if jet3PtCutList[item] < jet2Pt]
# xTicks = ['Pt(j3)>'+str(item) for item in jet3PtCutList if item < jet2Pt]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+str(item)+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in jet3PtCutList if item < jet2Pt]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryJet3'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryJet3'+isRebinned+postfix+'.pdf')
# 
# fig_njets = pl.figure(5)
# x = [item for item in range(len(njetsCutList))]
# xTicks = ['#jets>='+str(item) for item in njetsCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+str(item)+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in njetsCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryNJets'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryNJets'+isRebinned+postfix+'.pdf')
# 
# # bestLepPt  = '40'
# # bestMET    = '75'
# # bestJet1Pt = '125'
# # bestJet2Pt = '75'
# # bestJet3Pt = '40'
# # bestNJets  = '3'
# 
# bestLepPt  = '80'
# bestMET    = '40'
# bestJet1Pt = '300'
# bestJet2Pt = '200'
# bestJet3Pt = '100'
# bestNJets  = '3'
# 
# fig_dr = pl.figure(6)
# x = [item for item in range(len(drCutList))]
# xTicks = ['DR>'+str(item) for item in drCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+str(item)+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in drCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryDRs'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryDRs'+isRebinned+postfix+'.pdf')
# 
# fig_wjet1 = pl.figure(7)
# x = [item for item in range(len(Wjet1PtCutList))]
# xTicks = ['Pt(W1)>'+str(item) for item in Wjet1PtCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+str(item)+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in Wjet1PtCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryWjet1'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryWjet1'+isRebinned+postfix+'.pdf')
# 
# fig_bjet1 = pl.figure(8)
# x = [item for item in range(len(bjet1PtCutList))]
# xTicks = ['Pt(b1)>'+str(item) for item in bjet1PtCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+str(item)+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in bjet1PtCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryBjet1'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryBjet1'+isRebinned+postfix+'.pdf')
# 
# fig_st = pl.figure(9)
# x = [item for item in range(len(stCutList))]
# xTicks = ['ST>'+str(item) for item in stCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+str(item)+'_minMlb'+bestminMlb] for item in stCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryST'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryST'+isRebinned+postfix+'.pdf')
# 
# fig_minmlb = pl.figure(10)
# x = [item for item in range(len(minMlbCutList))]
# xTicks = ['minMlb>'+str(item) for item in minMlbCutList]
# y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+str(item)] for item in minMlbCutList]
# pl.xticks(x, xTicks)
# pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
# pl.plot(x,y,'*-')
# pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
# pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
# pl.savefig(outDir+'/VaryminMlb'+isRebinned+postfix+'.png')
# pl.savefig(outDir+'/VaryminMlb'+isRebinned+postfix+'.pdf')
# 
# 

