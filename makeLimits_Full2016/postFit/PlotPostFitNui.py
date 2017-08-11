from ROOT import *
from array import array
from math import *
import os,sys,pickle

gROOT.SetBatch(1)

from tdrStyle import *
setTDRStyle()

blind=False
isBkgOnly=True
sigProc='sig'
if(isBkgOnly):sigProc=''
saveKey=''
lumiPlot = '35.9'
lumiStr = '35p867'
spin=''#'right'
# discriminant='STrebinnedv2'
# discriminant='HTrebinned'
discriminant='minMlllBv4'
histPrefix=discriminant+'_'+str(lumiStr)+'fb'+spin
stat=''#0.75
isRebinned='_rebinned'+str(stat).replace('.','p')
tempKey='all_forPostFitNuis'
limitDir='/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer_80x/makeLimits_Full2016/postFit/'
cutString='lep40_MET75_1jet300_2jet150_NJets3_NBJets0_3jet100_4jet0_5jet0_DR1_1Wjet0_1bjet0_HT0_ST0_minMlb0'
# file='/templates_STrebinnedv2_TTM1000_bW0p5_tZ0p25_tH0p25_35p867fb'
# file='/templates_HTrebinned_TTM1000_bW0p5_tZ0p25_tH0p25_35p867fb'
file='/templates_minMlllBv4_TTM1000_bW0p5_tZ0p25_tH0p25_35p867fb'
if(isBkgOnly):file=file+'_bkgonly'
file=file+'.p'

parVals=pickle.load(open(limitDir+file,'rb'))
#print parVals

nuisNam = []
nuisVal = []
nuisErr = []
for nuis in parVals[sigProc].keys():
	if nuis=='__cov' or nuis=='__nll': continue
	nuisNam.append(nuis)
	nuisVal.append(parVals[sigProc][nuis][0][0])
	nuisErr.append(parVals[sigProc][nuis][0][1])
	print nuis,"=",parVals[sigProc][nuis][0][0],"+/-",parVals[sigProc][nuis][0][1]

nuisNam = [
			'pdfNew',
			'muRFcorrdNewSig',
			'muRFcorrdNewEwk',
			'muRFcorrdNewTop',
			'btag',
			'mistag',
			'jer',
			'jec',
			'pileup',
			'mumumuTrigSys',
			'elmumuTrigSys',
			'elelmuTrigSys',
			'elelelTrigSys',
			'muIsoSys',
			'elIsoSys',
			'muIdSys',
			'elIdSys',
			'elFR',
			'muFR',
			'muFReta',
			'elPRsys',
			'muPRsys',
			'elPR',
			'muPR',
			'lumiSys',
			]
nuisNamPlot = [
			'PDF',
			'muRFsig',
			'muRFewk',
			'muRFtop',
			'Btag',
			'Bmistag',
			'JER',
			'JEC',
			'pileup',
			'mumumuTrig',
			'elmumuTrig',
			'elelmuTrig',
			'elelelTrig',
			'muIso',
			'elIso',
			'muId',
			'elId',
			'elFR',
			'muFR',
			'muFReta',
			'elPRsys',
			'muPRsys',
			'elFR',
			'muFR',
			'lumi',
			]

if isBkgOnly: 
	nuisNam = [
				'pdfNew',
	# 			'muRFcorrdNewSig',
				'muRFcorrdNewEwk',
				'muRFcorrdNewTop',
				'btag',
				'mistag',
				'jer',
				'jec',
				'pileup',
# 				'mumumuTrigSys',
# 				'elmumuTrigSys',
# 				'elelmuTrigSys',
# 				'elelelTrigSys',
				'mmmTrigSys',
				'emmTrigSys',
				'eemTrigSys',
				'eeeTrigSys',
				'muIsoSys',
				'elIsoSys',
				'muIdSys',
				'elIdSys',
				'FRsys', #closure in ttbar
				'muFReta',
				'muFR',
				'elFR',
				'muPRsys', #varying to 1.0
				'elPRsys', #varying to 1.0
# 				'muPR',
# 				'elPR',
				'lumiSys',
				]
	nuisNamPlot = [
				'PDF',
	# 			'muRFsig',
				'muRFewk',
				'muRFtop',
				'Btag',
				'Bmistag',
				'JER',
				'JEC',
				'pileup',
				'mumumuTrig',
				'elmumuTrig',
				'elelmuTrig',
				'elelelTrig',
				'muIso',
				'elIso',
				'muId',
				'elId',
				'FRsys', #closure in ttbar 
				'muFReta',
				'muFR',
				'elFR',
				'muPR', #varying to 1.0
				'elPR', #varying to 1.0
# 				'muPR',
# 				'elPR',
				'lumi',
				]


nuisVal = []
nuisErr = []
for i in range(len(nuisNam)):
	nuis = nuisNam[i]
	nuisVal.append(parVals[sigProc][nuis][0][0])
	nuisErr.append(parVals[sigProc][nuis][0][1])
nNuis = len(nuisNam)

g   = TGraphAsymmErrors(nNuis)
g68 = TGraph(2*nNuis+7)
g95 = TGraph(2*nNuis+7)
for i in range(nNuis):
	g.SetPoint(i, nuisVal[i], i+1.5)
	g.SetPointEXlow(i, nuisErr[i])
	g.SetPointEXhigh(i, nuisErr[i])
for a in xrange(0, nNuis+3):
	g68.SetPoint(a, -1, a)
	g95.SetPoint(a, -1.99, a)
	g68.SetPoint(a+1+nNuis+2, 1, nNuis+2-a)
	g95.SetPoint(a+1+nNuis+2, 1.99, nNuis+2-a)

g.SetLineStyle(1)
g.SetLineWidth(1)
g.SetLineColor(1)
g.SetMarkerStyle(21)
g.SetMarkerSize(1.25)
g68.SetFillColor(ROOT.kGreen)
g95.SetFillColor(ROOT.kYellow)

c = TCanvas('PostFit', 'PostFit', 1000, 1200)
c.SetTopMargin(0.06)
c.SetRightMargin(0.06)
c.SetBottomMargin(0.12)
c.SetLeftMargin(0.25)
c.SetTickx()
c.SetTicky()
	
g95.Draw('AF')
g68.Draw('F')
g.Draw('P')


prim_hist = g95.GetHistogram() 
ax_1 = prim_hist.GetYaxis()
ax_2 = prim_hist.GetXaxis()

g95.SetTitle('')
ax_2.SetTitle('post-fit values')
#ax_2.SetTitle('deviation in units of #sigma')
ax_1.SetTitleSize(0.050)
ax_2.SetTitleSize(0.050)
ax_1.SetTitleOffset(1.4)
ax_2.SetTitleOffset(1.0)
ax_1.SetLabelSize(0.05)
#ax_2.SetLabelSize(0.05)
ax_1.SetRangeUser(0, nNuis+2)
ax_2.SetRangeUser(-2.2, 2.2)

ax_1.Set(nNuis+2, 0, nNuis+2)
ax_1.SetNdivisions(-414)
#ax_2.SetNdivisions(-505)
for i in range(nNuis):
	ax_1.SetBinLabel(i+2, nuisNamPlot[i])

g95.GetHistogram().Draw('axis,same')
c.Modified()
c.Update()

if not isBkgOnly:
	c.SaveAs('postFitNuis.root')
	c.SaveAs('postFitNuis.pdf')
	c.SaveAs('postFitNuis.png')
	c.SaveAs('postFitNuis.C')
else:
	c.SaveAs('postFitNuis_bkgonly.root')
	c.SaveAs('postFitNuis_bkgonly.pdf')
	c.SaveAs('postFitNuis_bkgonly.png')
	c.SaveAs('postFitNuis_bkgonly.C')

