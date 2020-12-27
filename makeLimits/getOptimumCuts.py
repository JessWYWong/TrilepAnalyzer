from array import array
from math import *
import os,sys,itertools

blind = True #stay blind to data when optimizing selections!
lumiPlot = '41.557'
lumiStr = '41p557'
distribution = 'STrebinnedv2'
pfix = "optimization_FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2_2020_6_24"
if len(sys.argv)>1: pfix=sys.argv[1]
limitDir='/mnt/data/users/wwong/limits/'+pfix
#limitDir='/mnt/data/users/wwong/limits/optimization_FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2_2020_7_7'
postfix = 'Limit' # for plot names in order to save them as different files
isRebinned=''#'_rebinned_modified'+str(stat).replace('.','p')
whichSignal='TT'
if('_BB' in sys.argv[1]): whichSignal = 'BB'

if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays

doBRScan = False
BRs={}
nBRconf=[0]
if whichSignal=='TT':
        BRs['BW']=[0.50,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,1.0]
        BRs['TH']=[0.25,0.0,0.5,0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0]
        BRs['TZ']=[0.25,1.0,0.5,0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.0]
        nBRconf=range(len(BRs['BW']))
if whichSignal=='BB':
        BRs['TW']=[0.50,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,0.0]
        BRs['BH']=[0.25,0.0,0.5,0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0]
        BRs['BZ']=[0.25,0.0,0.5,0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,1.0]
        nBRconf=range(len(BRs['TW']))
if not doBRScan: nBRconf=[0]

BRind = 1
if len(sys.argv)>2: BRind = int(sys.argv[2])
BRconfStr=''
if whichSignal=='TT': BRconfStr='_bW'+str(BRs['BW'][BRind]).replace('.','p')+'_tZ'+str(BRs['TZ'][BRind]).replace('.','p')+'_tH'+str(BRs['TH'][BRind]).replace('.','p')
if whichSignal=='BB': BRconfStr='_tW'+str(BRs['TW'][BRind]).replace('.','p')+'_bZ'+str(BRs['BZ'][BRind]).replace('.','p')+'_bH'+str(BRs['BH'][BRind]).replace('.','p')
print "********************************************************************************"
print(BRconfStr)
print "********************************************************************************"


lep1PtCutList = [0]
#lep1PtCutList = [30,50,100]
jetPtCutList  = [0]
#jetPtCutList  = [30,50,100]
#metCutList    = [20,40,60,80,100,200]
metCutList    = [20]
njetsCutList  = [3]
#njetsCutList  = [3,4,5]
bJet1PtCutList = [0]
bJet1PtCutList = [30,38,40,42,45,48,50,52,55,58,60,62,65,68,70,72,75,78,80]
#bJet1PtCutList = [30,50,100,200]
#bJet1PtCutList = [30,35,40,45,50,75,100]
nbjetsCutList = [1]
htCutList     = [0]
stCutList     = [0]
#stCutList     = [0,200,400,600,700,800,900,1000,1100]
#stCutList     = [0,200,400]
mllOSCutList  = [20] #,25,30,50,100]
isPassTriLeptonList= [1]
isPassTrig_dilepList= [1]
ptRelCutList = [0]#,4,6,8,10,12,14,16,20] #,10,20,30,50,60,70]
minDRlepJetCutList = [0.0] #,0.25,0.5,0.75,1.0]

cutConfigs = list(itertools.product(lep1PtCutList,jetPtCutList,metCutList,njetsCutList,bJet1PtCutList,nbjetsCutList,htCutList,stCutList,mllOSCutList,isPassTriLeptonList,isPassTrig_dilepList,ptRelCutList,minDRlepJetCutList))

massPoints = range(1000,1900,100)
if whichSignal=='BB': massPoints = range(900,1900,100)
mass_str = [str(item) for item in massPoints]

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
for i in range(len(massPoints)):
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
	lep1PtCut,jetPtCut,metCut,njetsCut,bJet1PtCut,nbjetsCut,htCut,stCut,mllOSCut,isPassTriLepton,isPassTrig_dilep,ptRelCut,minDRlepJetCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12]
	cutString  = 'lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_bJet1Pt'+str(int(bJet1PtCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(int(htCut))+'_ST'+str(int(stCut))+'_mllOS'+str(int(mllOSCut))+'_ptRel'+str(int(ptRelCut))+'_minDRlJ'+str(minDRlepJetCut).replace('.','p')
	#lepPtCut,jet1PtCut,bJet1PtCut,metCut,njetsCut,nbjetsCut,bJet1PtCut,jet4PtCut,jet5PtCut,drCut,Wjet1PtCut,bjet1PtCut,htCut,stCut,minMlbCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12],conf[13],conf[14]
	#cutString = 'lep'+str(int(lepPtCut))+'_MET'+str(int(metCut))+'_1jet'+str(int(jet1PtCut))+'_2jet'+str(int(bJet1PtCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_3jet'+str(int(bJet1PtCut))+'_4jet'+str(int(jet4PtCut))+'_5jet'+str(int(jet5PtCut))+'_DR'+str(drCut)+'_1Wjet'+str(Wjet1PtCut)+'_1bjet'+str(bjet1PtCut)+'_HT'+str(htCut)+'_ST'+str(stCut)+'_minMlb'+str(minMlbCut)
	haveLimits = True
	for i in range(len(massPoints)):
		try: 
			ftemp = open(limitDir+BRconfStr+'/'+cutString+'/thetaTemplates_rootfiles/limits_templates_'+distribution+'_'+whichSignal+'M'+mass_str[i]+BRconfStr+'_'+lumiStr+'fb'+isRebinned+'_expected.txt', 'rU')
		except: 
			haveLimits = False
			print('cannot find '+limitDir+BRconfStr+'/'+cutString+'/thetaTemplates_rootfiles/limits_templates_'+distribution+'_'+whichSignal+'M'+mass_str[i]+BRconfStr+'_'+lumiStr+'fb'+isRebinned+'_expected.txt')
	if not haveLimits: continue
	exp   =array('d',[0 for i in range(len(massPoints))])
	obs   =array('d',[0 for i in range(len(massPoints))])
	for i in range(len(massPoints)):
		lims = {}

		fobs = open(limitDir+BRconfStr+'/'+cutString+'/thetaTemplates_rootfiles/limits_templates_'+distribution+'_'+whichSignal+'M'+mass_str[i]+BRconfStr+'_'+lumiStr+'fb'+isRebinned+'_observed.txt', 'rU')
		linesObs = fobs.readlines()
		fobs.close()

		fexp = open(limitDir+BRconfStr+'/'+cutString+'/thetaTemplates_rootfiles/limits_templates_'+distribution+'_'+whichSignal+'M'+mass_str[i]+BRconfStr+'_'+lumiStr+'fb'+isRebinned+'_expected.txt', 'rU')
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
for i in range(len(massPoints)):
	print "Expected("+mass_str[i]+"GeV): "+expBestCutStr[mass_str[i]]+" with 95% CL: "+str(expBestLimit[mass_str[i]])
	if not blind: print "Observed("+mass_str[i]+"GeV): "+obsBestCutStr[mass_str[i]]+" with 95% CL: "+str(obsBestLimit[mass_str[i]])
print "********************************************************************************"
print "The worst set of cuts:"
for i in range(len(massPoints)):
	print "Expected("+mass_str[i]+"GeV): "+expWorstCutStr[mass_str[i]]+" with 95% CL: "+str(expWorstLimit[mass_str[i]])
	if not blind: print "Observed("+mass_str[i]+"GeV): "+obsWorstCutStr[mass_str[i]]+" with 95% CL: "+str(obsWorstLimit[mass_str[i]])
print "********************************************************************************"

#os._exit(1) # skip the plotting in the next lines!

#import matplotlib.pyplot as pl
#massPoint = '800'
from ROOT import *
from tdrStyle import *
setTDRStyle()
gROOT.SetBatch(1)

folder='.'
outDir = folder+'/'+(limitDir+BRconfStr).split('/')[-2]+'plots'
if not os.path.exists(outDir): os.system('mkdir '+outDir)
outDir += '/optimizationInIndividualCats'
if not os.path.exists(outDir): os.system('mkdir '+outDir)

bestCut = {}
allCuts = {}

for i in range(len(massPoints)):
    bestCut[whichSignal+'M'+mass_str[i]] = {}
    bestCutStr = expBestCutStr[mass_str[i]]
    for cut in bestCutStr.split('_'):
        ind = len(cut)-1
        while (cut[ind:].replace('p','.').isdigit() or cut[ind]=='p'):
            ind -= 1
        if ('p' not in cut[ind+1:]): bestCut[whichSignal+'M'+mass_str[i]].update({cut[:ind+1]: int(cut[ind+1:])})
        else : bestCut[whichSignal+'M'+mass_str[i]].update({cut[:ind+1]: float(cut[ind+1:].replace('p','.'))})
#print(bestCut)

allCuts = {}
for iCutStr in expLimits[mass_str[0]].keys():
    for cut in iCutStr.split('_'):
        ind = len(cut)-1
        while (cut[ind:].replace('p','.').isdigit() or cut[ind]=='p'):
            ind -= 1
        if cut[:ind+1] not in allCuts.keys(): allCuts.update({cut[:ind+1] : []})
        if ('p' not in cut[ind+1:]) and (int(cut[ind+1:]) not in allCuts[cut[:ind+1]]) : allCuts[cut[:ind+1]].append(int(cut[ind+1:]))
        if ('p' in cut[ind+1:]) and (float(cut[ind+1:].replace('p','.')) not in allCuts[cut[:ind+1]]) : allCuts[cut[:ind+1]].append(float(cut[ind+1:].replace('p','.')))
        allCuts[cut[:ind+1]].sort()
print(allCuts)

plotColor = [kBlack, kGray, kRed-7, kRed+2, kOrange, kViolet, kAzure, kCyan, kTeal-1, kSpring-4]

for cut in allCuts.keys():
    if len(allCuts[cut])<2 : continue
    xbin = sorted(allCuts[cut])

    c4 = TCanvas("c4","Limits", 1000, 800)
    c4.SetBottomMargin(0.15)
    c4.SetRightMargin(0.06)
    #c4.SetLogy()

    legend = TLegend(.62,.62,.92,.92) # top right
    legend.SetShadowColor(0)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetNColumns(2)

    expectedLim = {}
    for i in range(len(mass_str)): 
        expectedLim[mass_str[i]] = TGraph(len(xbin))
        maxValue = 0
        minValue = 999
        for j in range(len(xbin)):
            cutString = expBestCutStr[mass_str[0]].replace(cut+str(bestCut[whichSignal+'M'+mass_str[0]][cut]),cut+str(xbin[j]))
            expectedLim[mass_str[i]].SetPoint(j, xbin[j], expLimits[mass_str[i]][cutString])
            if expLimits[mass_str[i]][cutString] > maxValue : maxValue = expLimits[mass_str[i]][cutString]
            if expLimits[mass_str[i]][cutString] < minValue and expLimits[mass_str[i]][cutString] > 0 : minValue = expLimits[mass_str[i]][cutString]
        expectedLim[mass_str[i]].SetTitle("Expected Limits;"+cut+";#sigma [pb]")
        expectedLim[mass_str[i]].SetLineColor(plotColor[i])
        expectedLim[mass_str[i]].SetLineStyle(1)
        expectedLim[mass_str[i]].SetLineWidth(2)
        expectedLim[mass_str[i]].SetMaximum(maxValue*1.5)
        expectedLim[mass_str[i]].SetMinimum(minValue*0.5)
        if i == 0: expectedLim[mass_str[i]].Draw("alp")
        else: expectedLim[mass_str[i]].Draw("lp same")
        legend.AddEntry(expectedLim[mass_str[i]], whichSignal+"M"+mass_str[i], "l")

    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.03)
    latex2.SetTextAlign(11) # align right
    latex2.DrawLatex(0.58, 0.96, "CMS Preliminary, " + str(lumiPlot) + " fb^{-1} (13 TeV)")
    latex4 = TLatex()
    latex4.SetNDC()
    latex4.SetTextSize(0.06)
    latex4.SetTextAlign(31) # align right

    legend.Draw()
    c4.RedrawAxis()
    c4.SaveAs(outDir+'/ExpectedLimitPlot_'+limitDir.split('/')[-1]+BRconfStr+'_'+cut+'.pdf')

os._exit(1)

folder='.'
outDir = folder+'/'+(limitDir+BRconfStr).split('/')[-2]+'plots'
if not os.path.exists(outDir): os.system('mkdir '+outDir)
outDir += '/optimizationInIndividualCats'
if not os.path.exists(outDir): os.system('mkdir '+outDir)

bestLepPt  = expBestCutStr[massPoint][3:expBestCutStr[massPoint].find('_MET')]
bestMET    = expBestCutStr[massPoint][expBestCutStr[massPoint].find('MET')+3:expBestCutStr[massPoint].find('_1jet')]
bestJet1Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('1jet')+4:expBestCutStr[massPoint].find('_2jet')]
bestJet2Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('2jet')+4:expBestCutStr[massPoint].find('_NJets')]
bestJet3Pt = expBestCutStr[massPoint][expBestCutStr[massPoint].find('3jet')+4:expBestCutStr[massPoint].find('_4jet')]
bestNJets  = expBestCutStr[massPoint][expBestCutStr[massPoint].find('NJets')+5:expBestCutStr[massPoint].find('_NBJets')]
bestDR     = expBestCutStr[massPoint][expBestCutStr[massPoint].find('DR')+2:expBestCutStr[massPoint].find('_1Wjet')]
bestWJet1Pt= expBestCutStr[massPoint][expBestCutStr[massPoint].find('1Wjet')+5:expBestCutStr[massPoint].find('_1bjet')]
bestBJet1Pt= expBestCutStr[massPoint][expBestCutStr[massPoint].find('1bjet')+5:expBestCutStr[massPoint].find('_HT')]
bestST     = expBestCutStr[massPoint][expBestCutStr[massPoint].find('ST')+2:expBestCutStr[massPoint].find('_minMlb')]
bestminMlb = expBestCutStr[massPoint][expBestCutStr[massPoint].find('minMlb')+6:]

fig_lep = pl.figure(0)
x = [item for item in range(len(lepPtCutList))]
xTicks = ['Pt(lep)>'+str(item) for item in lepPtCutList]
y = [expLimits[massPoint]['lep'+str(item)+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in lepPtCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryLepPt'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryLepPt'+isRebinned+postfix+'.pdf')

fig_met = pl.figure(1)
x = [item for item in range(len(metCutList))]
xTicks = ['MET>'+str(item) for item in metCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+str(item)+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in metCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryMET'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryMET'+isRebinned+postfix+'.pdf')

jet1Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('1jet')+4:expBestCutStr[massPoint].find('_2jet')])
bJet1Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('2jet')+4:expBestCutStr[massPoint].find('_NJets')])
bJet1Pt = int(expBestCutStr[massPoint][expBestCutStr[massPoint].find('3jet')+4:expBestCutStr[massPoint].find('_4jet')])
fig_jet1 = pl.figure(2)
x = [item for item in range(len(jet1PtCutList)) if jet1PtCutList[item] > bJet1Pt]
xTicks = ['Pt(j1)>'+str(item) for item in jet1PtCutList if item > bJet1Pt]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+str(item)+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in jet1PtCutList if item > bJet1Pt]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryJet1'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryJet1'+isRebinned+postfix+'.pdf')

fig_jet2 = pl.figure(3)
x = [item for item in range(len(bJet1PtCutList)) if bJet1PtCutList[item] > bJet1Pt and bJet1PtCutList[item] < jet1Pt]
xTicks = ['Pt(j2)>'+str(item) for item in bJet1PtCutList if item > bJet1Pt and item < jet1Pt]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+str(item)+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in bJet1PtCutList if item > bJet1Pt and item < jet1Pt]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryJet2'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryJet2'+isRebinned+postfix+'.pdf')

fig_jet3 = pl.figure(4)
x = [item for item in range(len(bJet1PtCutList)) if bJet1PtCutList[item] < bJet1Pt]
xTicks = ['Pt(j3)>'+str(item) for item in bJet1PtCutList if item < bJet1Pt]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+str(item)+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in bJet1PtCutList if item < bJet1Pt]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryJet3'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryJet3'+isRebinned+postfix+'.pdf')

fig_njets = pl.figure(5)
x = [item for item in range(len(njetsCutList))]
xTicks = ['#jets>='+str(item) for item in njetsCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+str(item)+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'] for item in njetsCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryNJets'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryNJets'+isRebinned+postfix+'.pdf')

# bestLepPt  = '40'
# bestMET    = '75'
# bestJet1Pt = '125'
# bestJet2Pt = '75'
# bestJet3Pt = '40'
# bestNJets  = '3'

bestLepPt  = '80'
bestMET    = '40'
bestJet1Pt = '300'
bestJet2Pt = '200'
bestJet3Pt = '100'
bestNJets  = '3'

fig_dr = pl.figure(6)
x = [item for item in range(len(drCutList))]
xTicks = ['DR>'+str(item) for item in drCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+str(item)+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in drCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryDRs'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryDRs'+isRebinned+postfix+'.pdf')

fig_wjet1 = pl.figure(7)
x = [item for item in range(len(Wjet1PtCutList))]
xTicks = ['Pt(W1)>'+str(item) for item in Wjet1PtCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+str(item)+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in Wjet1PtCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryWjet1'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryWjet1'+isRebinned+postfix+'.pdf')

fig_bjet1 = pl.figure(8)
x = [item for item in range(len(bjet1PtCutList))]
xTicks = ['Pt(b1)>'+str(item) for item in bjet1PtCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+str(item)+'_HT0_ST'+bestST+'_minMlb'+bestminMlb] for item in bjet1PtCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryBjet1'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryBjet1'+isRebinned+postfix+'.pdf')

fig_st = pl.figure(9)
x = [item for item in range(len(stCutList))]
xTicks = ['ST>'+str(item) for item in stCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+str(item)+'_minMlb'+bestminMlb] for item in stCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryST'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryST'+isRebinned+postfix+'.pdf')

fig_minmlb = pl.figure(10)
x = [item for item in range(len(minMlbCutList))]
xTicks = ['minMlb>'+str(item) for item in minMlbCutList]
y = [expLimits[massPoint]['lep'+bestLepPt+'_MET'+bestMET+'_1jet'+bestJet1Pt+'_2jet'+bestJet2Pt+'_NJets'+bestNJets+'_NBJets0_3jet'+bestJet3Pt+'_4jet0_5jet0_DR'+bestDR+'_1Wjet'+bestWJet1Pt+'_1bjet'+bestBJet1Pt+'_HT0_ST'+bestST+'_minMlb'+str(item)] for item in minMlbCutList]
pl.xticks(x, xTicks)
pl.xticks(x, xTicks, rotation=25) #writes strings with 45 degree angle
pl.plot(x,y,'*-')
pl.ylabel(r'$\sigma$ ($T\bar T$)[pb]')
pl.title(expBestCutStr[massPoint].replace('_4jet0_5jet0','').replace('_NBJets0',''))
pl.savefig(outDir+'/VaryminMlb'+isRebinned+postfix+'.png')
pl.savefig(outDir+'/VaryminMlb'+isRebinned+postfix+'.pdf')



