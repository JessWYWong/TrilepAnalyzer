#!/usr/bin/python

import os,sys,time,math,pickle
from ROOT import *
from weights import *
from tdrStyle import *


gROOT.SetBatch(1)
start_time = time.time()


templateDir='/user_data/rsyarif/kinematics_80x_condor_BLA'

DEBUG=False

mainDir='/user_data/rsyarif/'
templateDir=mainDir

templateDir+='kinematics_80x_condor_BLA'


if len(sys.argv)>1: templateDir = mainDir+sys.argv[1] 


lumi=41.6 #for plots

lumiInTemplates='41p557'

# sig='ttm800' # choose the 1st signal to plot
# sigleg='TT(0.8 TeV)'

sig='ttm1200' # choose the 1st signal to plot
sigleg='T#bar{T}(1.2 TeV)'

sigM1500='ttm1500' 
siglegM1500='T#bar{T}(1.2 TeV)'

scaleSignals = True
dontShowSignalScaling = False

# scaleFact1 = 300
scaleFact1 = 10
scaleFact2 = 50
if 'Final' in templateDir: scaleFact1 = 40

systematicList = ['pileup','btag','mistag','pdfNew','muRFcorrdNew','elPR','elFR','muPR','muFR','jec','jer']

doAllSys = False
# doAllSys = True

isRebinned=''#post fix for file names if the name changed b/c of rebinning or some other process
doNormByBinWidth=False # not tested, may not work out of the box
doOneBand = False
if not doAllSys: doOneBand = True # Don't change this!
blind = True
yLog = True

if len(sys.argv)>2: blind = bool( int(sys.argv[2]) )  
if len(sys.argv)>3: yLog  = bool( int(sys.argv[3]) )
print 'bool(sys.argv[2]) =', bool(int(sys.argv[2])),  
print 'Blind = ', blind
print 'bool(sys.argv[3]) =', bool(int(sys.argv[3])),  
print 'yLog = ', yLog

# doRealPull = False
doRealPull = True
if doRealPull: doOneBand=False

totBkgTemp1 = {}
totBkgTemp2 = {}
totBkgTemp3 = {}

def formatUpperHist_v2(histogram,th1hist):
	histogram.GetXaxis().SetLabelSize(0)
	lowside = th1hist.GetBinLowEdge(1)
	highside = th1hist.GetBinLowEdge(th1hist.GetNbinsX()+1)
	histogram.GetXaxis().SetRangeUser(lowside,highside)
	print 'Name being formatted:',histogram.GetName()
	if blind == True:
		histogram.GetXaxis().SetLabelSize(0.08)
		histogram.GetXaxis().SetTitleSize(0.08)
		#histogram.GetXaxis().SetTitle(xTitle)
		histogram.GetYaxis().SetLabelSize(0.08)
		histogram.GetYaxis().SetTitleSize(0.08)
		histogram.GetYaxis().SetTitleOffset(1.2)
		histogram.GetXaxis().SetNdivisions(506)
	else:
		histogram.GetYaxis().SetLabelSize(0.05)
		histogram.GetYaxis().SetTitleSize(0.06)
		histogram.GetYaxis().SetTitleOffset(.78)

	if 'JetPt' in histogram.GetName() or 'JetEta' in histogram.GetName() or 'JetPhi' in histogram.GetName() or 'Pruned' in histogram.GetName() or 'Tau' in histogram.GetName(): histogram.GetYaxis().SetTitle("Jets")
# 	histogram.GetYaxis().CenterTitle()
	histogram.SetMinimum(2.01e-4)
# 	histogram.SetMinimum(0.001)
	if not yLog: 
		histogram.SetMinimum(0.25)
	if yLog:
		uPad.SetLogy()
		histogram.SetMinimum(0.101)
		#histogram.SetMinimum(0.0401) #for EEE STrebinnedv2 bin=3 has yield ~0.04
		if not doNormByBinWidth: histogram.SetMaximum(200*histogram.GetMaximum())
		else: histogram.SetMaximum(50*histogram.GetMaximum())

def formatUpperHist(histogram):
	histogram.GetXaxis().SetLabelSize(0)

	if blind == True:
		histogram.GetXaxis().SetLabelSize(0.08)
		histogram.GetXaxis().SetTitleSize(0.08)
		#histogram.GetXaxis().SetTitle(xTitle)
		histogram.GetYaxis().SetLabelSize(0.08)
		histogram.GetYaxis().SetTitleSize(0.08)
		histogram.GetYaxis().SetTitleOffset(1.2)
		histogram.GetXaxis().SetNdivisions(506)
	else:
		histogram.GetYaxis().SetLabelSize(0.05)
		histogram.GetYaxis().SetTitleSize(0.06)
		histogram.GetYaxis().SetTitleOffset(.78)

	if 'JetPt' in histogram.GetName() or 'JetEta' in histogram.GetName() or 'JetPhi' in histogram.GetName() or 'Pruned' in histogram.GetName() or 'Tau' in histogram.GetName(): histogram.GetYaxis().SetTitle("Jets")
	histogram.GetYaxis().CenterTitle()
	histogram.SetMinimum(2.01e-4)
# 	histogram.SetMinimum(0.001)
	if not yLog: 
		histogram.SetMinimum(0.25)
	if yLog:
		uPad.SetLogy()
		histogram.SetMinimum(0.1)
		if not doNormByBinWidth: histogram.SetMaximum(200*histogram.GetMaximum())
		else: histogram.SetMaximum(50*histogram.GetMaximum())
		
def formatLowerHist(histogram):
	histogram.GetXaxis().SetLabelSize(.15)
	histogram.GetXaxis().SetTitleSize(0.18)
	histogram.GetXaxis().SetTitleOffset(0.95)
	histogram.GetXaxis().SetNdivisions(506)
	#histogram.GetXaxis().SetTitle("S_{T} (GeV)")

	histogram.GetYaxis().SetLabelSize(0.15)
	histogram.GetYaxis().SetTitleSize(0.145)
	histogram.GetYaxis().SetTitleOffset(.3)
	if not doRealPull: histogram.GetYaxis().SetTitle('Data/Bkg')
	else: histogram.GetYaxis().SetTitle('#frac{(data-bkg)}{std. dev.}')
	histogram.GetYaxis().SetNdivisions(5)
# 	if doRealPull: histogram.GetYaxis().SetRangeUser(min(-2.99,0.8*histogram.GetBinContent(histogram.GetMaximumBin())),max(2.99,1.2*histogram.GetBinContent(histogram.GetMaximumBin())))
	if doRealPull: histogram.GetYaxis().SetRangeUser(-1.99,1.99)
#	else: histogram.GetYaxis().SetRangeUser(0,1.99)
	else: histogram.GetYaxis().SetRangeUser(0,2.99)
	histogram.GetYaxis().CenterTitle()

def normByBinWidth(result):
	result.SetBinContent(0,0)
	result.SetBinContent(result.GetNbinsX()+1,0)
	result.SetBinError(0,0)
	result.SetBinError(result.GetNbinsX()+1,0)
	
	for bin in range(1,result.GetNbinsX()+1):
		width=result.GetBinWidth(bin)
		content=result.GetBinContent(bin)
		error=result.GetBinError(bin)
		
		result.SetBinContent(bin, content/width)
		result.SetBinError(bin, error/width)

lumiSys = 0.026 #6.2% https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html - 11Feb2017
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
# lepIdSys = math.sqrt(3.*0.01**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
# lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIdSys = 0.03 #ATTENTION: is this right? add 1% linearly per lepton??
lepIsoSys = 0.03 #ATTENTION: is this right? add 1% linearly per lepton??
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty


#how to incorporate these?
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

ddbkgSystematics = { #based on newRunH Mar28 ST700
					'elPRsys':{'EEE':0.21,'EEM':0.12,'EMM':0.06,'MMM':0.00,'All':0.09},
					'muPRsys':{'EEE':0.00,'EEM':0.03,'EMM':0.07,'MMM':0.15,'All':0.06},
					'muFReta':{'EEE':0.00,'EEM':0.11,'EMM':0.10,'MMM':0.26,'All':0.12}
					}


def getNormUnc(hist,ibin,cat):
	contentsquared = hist.GetBinContent(ibin)**2
	corrdSysSq = lumiSys**2 + trigSys**2 + normSystematics['elIdSys'][cat]**2 + normSystematics['muIdSys'][cat]**2 + normSystematics['elIsoSys'][cat]**2 + normSystematics['muIsoSys'][cat]**2 
	error = corrdSysSq * contentsquared  #correlated uncertainties
	if 'top' in hist.GetName(): error += topXsecSys*topXsecSys*contentsquared # cross section
	if 'ewk' in hist.GetName(): error += ewkXsecSys*ewkXsecSys*contentsquared # cross section
	if 'qcd' in hist.GetName(): error += qcdXsecSys*qcdXsecSys*contentsquared # cross section
	return error

def getDDBKGNormUnc(hist,ibin,cat):
	contentsquared = hist.GetBinContent(ibin)**2
	error = (ddbkgSystematics['elPRsys'][cat]**2 + ddbkgSystematics['muPRsys'][cat]**2 + ddbkgSystematics['muFReta'][cat]**2) * contentsquared  #correlated uncertainties
	return error

def poissonNormByBinWidth(tgae,hist):
	alpha = 1. - 0.6827
	for ibin in range(0,tgae.GetN()):
		width = float(hist.GetBinWidth(ibin+1))
		X = tgae.GetX()[ibin]
		N = tgae.GetY()[ibin]
		L = 0
		if N != 0: L = Math.gamma_quantile(alpha/2.,N,1.)
		U = Math.gamma_quantile_c(alpha/2.,N+1,1)
		tgae.SetPoint(ibin,X,N/width)
		tgae.SetPointEYlow(ibin,(N-L)/width)
		tgae.SetPointEYhigh(ibin,(U-N)/width)

def poissonErrors(tgae,discriminant):
	alpha = 1. - 0.6827
	for ibin in range(0,tgae.GetN()):
		N = tgae.GetY()[ibin]
		L = 0
		if N != 0: L = Math.gamma_quantile(alpha/2.,N,1.)
		U = Math.gamma_quantile_c(alpha/2.,N+1,1)
		tgae.SetPointEYlow(ibin,N-L)
		tgae.SetPointEYhigh(ibin,U-N)

		if (discriminant=="lepPt" or discriminant=="STrebinnedv2") and (ibin==0 or ibin==1): #manually kill unc in first two bins.
			tgae.SetPointEYlow(ibin,0)
			tgae.SetPointEYhigh(ibin,0)


plotList = [#distribution name as defined in "doHists.py"
# # 	'ElDxy',
# # 	'ElDz',
# # 
# # 	'MuDxy',
# # 	'MuDz',
# 	
 	'NPV',
# 
	'lepPt',
	'lepPtRebinned',
	'ElPt',
	'MuPt',
	'lep1Pt',
	'lep2Pt',
	'lep3Pt',
	'lepEta',
	'ElEta',
	'MuEta',
	'lep1Eta',
	'lep2Eta',
	'lep3Eta',
	'Nlep',
	'Nel',
	'Nmu',

	'JetEta',
 	'Jet1Eta',
 	'Jet2Eta',
	'JetPt' ,
 	'Jet1Pt' ,
 	'Jet2Pt' ,
# 
# 
 	'HT',
# # 	'ST',
 	'MET',
 	'HTrebinned',
# 	'ST',
# # 	'STrebinned',
# 
	'STrebinnedv2',
# 
# # 	'STrebinnedv3',
 	'METrebinned',
# 
	'NJets' ,
 	'NBJets',
# 	#'NBJetsCorr',
# # 	'mindeltaRlepJets',
# # 	'mindeltaRlep1Jets',
# # 	'mindeltaRlep2Jets',
# # 	'mindeltaRlep3Jets',
# 
# # 	'minMlB',
# # 	'minMlBv2', #
# # 	'minMlllB',
# # 	'minMlllBv2',
# # 	'minMlllBv3', #
# # 	'minMlllBv4', #
# # 
# # 	'minDPhiMETJet',
# # 	'DRlep1Jet1',
# # 	'minDRlep1Jets',
# # 	'minDRlep2Jets',
# # 	'minDRlep3Jets',
# # 	'minDRlepsJets',	
# 	
# # 	'mindeltaR',
# # 	'mindeltaRB',
# # 
# # 	'mindeltaR1',
# # 	'mindeltaR2',
# # 	'mindeltaR3',
# 
# # 	'PtRel1',
# # 	'PtRel2',
# # 	'PtRel3',
# # 	'PtRel',
# 
# # 	'lepCharge',
# # 	'lepIso',
# # 	'ElIso',
# # 	'MuIso',
# # 	'MllsameFlavorOS',
# # 	'MllOSall',
# # 	'MllOSallmin',
# # 	'MllOSallmax',
# # 	'Mlll'
	]

fit  = False
fit2 = False
fit3 = False
fit4 = False
isEMlist=['EEE','EEM','EMM','MMM','All']
for discriminant in plotList:

# 	if discriminant != 'ST': continue
	fileTemp='templates_'+discriminant+'_'+lumiInTemplates+'fb'+isRebinned+'.root'
	print templateDir+'/'+fileTemp
	if not os.path.exists(templateDir+'/'+fileTemp): 
		print 'not found, skipping'
		continue
	RFile = TFile(templateDir+'/'+fileTemp)

	systHists={}
	for isEM in isEMlist:

		gStyle.SetOptStat(0)
		gStyle.SetEndErrorSize(0);
		setTDRStyle()

		if 'El' in discriminant and  isEM=='MMM':continue	
		if 'Mu' in discriminant and  isEM=='EEE':continue	

		histPrefix=discriminant+'_'+lumiInTemplates+'fb_'+isEM
		
		try: hTOP = RFile.Get(histPrefix+'__top').Clone()
		except: 
			if(DEBUG): print "There is no TOP!!!!!!!!",
			if(DEBUG): print "Skipping TOP....."
			pass
		try: hEWK = RFile.Get(histPrefix+'__ewk').Clone()
		except: 
			if(DEBUG): print "There is no EWK!!!!!!!!",
			if(DEBUG): print "Skipping EWK....."
			pass
		try: hQCD = RFile.Get(histPrefix+'__qcd').Clone()
		except: 
			if(DEBUG): print "There is no QCD!!!!!!!!",
			if(DEBUG): print "Skipping QCD....."
			pass
		try: hDDBKG = RFile.Get(histPrefix+'_ddbkg').Clone()
		except: 
			if(DEBUG): print "There is no DDBKG!!!!!!!!",
			if(DEBUG): print "Skipping DDBKG....."
			pass
					
		try: print discriminant,isEM, "TOP", hTOP.Integral()
		except: pass
		try: print discriminant,isEM, "EWK", hEWK.Integral()
		except: pass
		try: print discriminant,isEM, "QCD", hQCD.Integral()
		except: pass
		try: print discriminant,isEM, "DDBKG", hDDBKG.Integral()
		except: pass
		
		hData = RFile.Get(histPrefix+'__DATA').Clone()
		gaeData = TGraphAsymmErrors(hData.Clone(hData.GetName()+'gaeData'))
		hsig1 = RFile.Get(histPrefix+'__'+sig+'bwbw').Clone()
		hsig2 = RFile.Get(histPrefix+'__'+sig+'tztz').Clone()
		hsig3 = RFile.Get(histPrefix+'__'+sig+'thth').Clone()

		hsig = RFile.Get(histPrefix+'__'+sig+'bwbw').Clone(histPrefix+'__'+sig+'nominal')
		hsigM1500 = RFile.Get(histPrefix+'__'+sigM1500+'bwbw').Clone(histPrefix+'__'+sigM1500+'nominal')
		decays = ['tztz','thth','tzbw','thbw','tzth']
		for decay in decays:
			htemp = RFile.Get(histPrefix+'__'+sig+decay).Clone()
			hsig.Add(htemp)
			htemp = RFile.Get(histPrefix+'__'+sigM1500+decay).Clone()
			hsigM1500.Add(htemp)

		# original scale = lumi * xsec * BR(50/25/25) / N(33/33/33)
		hsig1.Scale(1.0/BR['TTBWBW'])
		hsig2.Scale(1.0/BR['TTTZTZ'])
		hsig3.Scale(1.0/BR['TTTHTH'])
		if doNormByBinWidth:
			normByBinWidth(hTOP)
			normByBinWidth(hEWK)
			normByBinWidth(hQCD)
			normByBinWidth(hsig1)
			normByBinWidth(hsig2)
			normByBinWidth(hData)
		else: poissonErrors(gaeData,discriminant)
		
		if doAllSys:
			for sys in systematicList:
				for ud in ['minus','plus']:
					try: systHists['top'+sys+ud] = RFile.Get(histPrefix+'__top__'+sys+'__'+ud).Clone()
					except: 
						if(DEBUG): print "Skipping",sys,"for TOP"
						pass
					try: systHists['ewk'+sys+ud] = RFile.Get(histPrefix+'__ewk__'+sys+'__'+ud).Clone()
					except: 
						if(DEBUG): print "Skipping",sys,"for EWK"
						pass
					try: systHists['qcd'+sys+ud] = RFile.Get(histPrefix+'__qcd__'+sys+'__'+ud).Clone()
					except: 
						if(DEBUG): print "Skipping",sys,"for QCD"
						pass
					try: systHists['ddbkg'+sys+ud] = RFile.Get(histPrefix+'__ddbkg__'+sys+'__'+ud).Clone()
					except: 
						if(DEBUG): print "Skipping",sys,"for DDBKG"
						pass

		try: hTOPstatOnly = hTOP.Clone(hTOP.GetName()+'statOnly')
		except: pass
		try: hEWKstatOnly= hEWK.Clone(hEWK.GetName()+'statOnly')
		except: pass
		try: hQCDstatOnly = hQCD.Clone(hQCD.GetName()+'statOnly')
		except: pass
		try: hDDBKGstatOnly = hDDBKG.Clone(hDDBKG.GetName()+'statOnly')
		except: pass

		try: bkgHT = hTOP.Clone()
		except: pass
		try: bkgHT.Add(hEWK)
		except: pass
		try: bkgHT.Add(hQCD)
		except: pass
		try: bkgHT.Add(hDDBKG)
		except: pass
		gaeBkgHT = TGraphAsymmErrors(bkgHT.Clone("gaeBkgHT"))

		if doNormByBinWidth: poissonNormByBinWidth(gaeBkgHT,bkgHT)
		else: poissonErrors(gaeBkgHT,discriminant)

		try:
			totBkgTemp1[isEM] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
			totBkgTemp2[isEM] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
			totBkgTemp3[isEM] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))
		except: pass
			
		try:
			BINS_temp = hTOP.GetNbinsX()
		except:
			BINS_temp = 0
						
		for ibin in range(1,BINS_temp+1):
			errorUp = 0.
			errorDn = 0.
			errorSym = 0.
			errorNorm = 0.
			errorStatUp = gaeBkgHT.GetErrorYhigh(ibin-1)**2
			errorStatDn = gaeBkgHT.GetErrorYlow(ibin-1)**2

			errorStatOnly = bkgHT.GetBinError(ibin)**2
# 			errorStatOnly = hTOP.GetBinError(ibin)**2 + hEWK.GetBinError(ibin)**2 #since hDDBKG stat error is in its  "sys" error. #MMMM maybe this isn correct.
			try: errorNorm = getNormUnc(hTOPstatOnly,ibin,isEM)
			except: pass
			try: errorNorm += getNormUnc(hEWKstatOnly,ibin,isEM)
			except: pass
			try: errorNorm += getNormUnc(hQCDstatOnly,ibin,isEM)
			except: pass
			try: errorNorm += getDDBKGNormUnc(hDDBKGstatOnly,ibin,isEM)
			except: pass

			if doAllSys:
				for sys in systematicList:
					if not ('PR' in sys or 'FR' in sys):
						errorSym += (0.5*abs(systHists['top'+sys+'plus'].GetBinContent(ibin)-systHists['top'+sys+'minus'].GetBinContent(ibin)))**2				
						errorPlus = systHists['top'+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin)
						errorMinus = hTOP.GetBinContent(ibin)-systHists['top'+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
						if sys!='toppt':
							try:
								errorSym += (0.5*abs(systHists['ewk'+sys+'plus'].GetBinContent(ibin)-systHists['ewk'+sys+'minus'].GetBinContent(ibin)))**2				
								errorPlus = systHists['ewk'+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin)
								errorMinus = hEWK.GetBinContent(ibin)-systHists['ewk'+sys+'minus'].GetBinContent(ibin)
								if errorPlus > 0: errorUp += errorPlus**2
								else: errorDn += errorPlus**2
								if errorMinus > 0: errorDn += errorMinus**2
								else: errorUp += errorMinus**2
							except: pass
							try:
								errorSym += (0.5*abs(systHists['qcd'+sys+'plus'].GetBinContent(ibin)-systHists['qcd'+sys+'minus'].GetBinContent(ibin)))**2				
								errorPlus = systHists['qcd'+sys+'plus'].GetBinContent(ibin)-hQCD.GetBinContent(ibin)
								errorMinus = hQCD.GetBinContent(ibin)-systHists['qcd'+sys+'minus'].GetBinContent(ibin)
								if errorPlus > 0: errorUp += errorPlus**2
								else: errorDn += errorPlus**2
								if errorMinus > 0: errorDn += errorMinus**2
								else: errorUp += errorMinus**2
							except: pass
					if 'PR' in sys or 'FR' in sys:
						try: errorSym += (0.5*abs(systHists['ddbkg'+sys+'plus'].GetBinContent(ibin)-systHists['ddbkg'+sys+'minus'].GetBinContent(ibin)))**2				
						except: pass
						try: errorPlus = systHists['ddbkg'+sys+'plus'].GetBinContent(ibin)-hDDBKG.GetBinContent(ibin)
						except: pass
						try: errorMinus = hDDBKG.GetBinContent(ibin)-systHists['ddbkg'+sys+'minus'].GetBinContent(ibin)
						except: pass
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
							
			totBkgTemp1[isEM].SetPointEYhigh(ibin-1,math.sqrt(errorUp))
			totBkgTemp1[isEM].SetPointEYlow(ibin-1,math.sqrt(errorDn))
			totBkgTemp2[isEM].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
			totBkgTemp2[isEM].SetPointEYlow(ibin-1,math.sqrt(errorDn+errorNorm))
# 			totBkgTemp3[isEM].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatOnly))
# 			totBkgTemp3[isEM].SetPointEYlow(ibin-1,math.sqrt(errorDn+errorNorm+errorStatOnly))
			totBkgTemp3[isEM].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatUp))
			totBkgTemp3[isEM].SetPointEYlow(ibin-1,math.sqrt(errorDn+errorNorm+errorStatDn))
						
		bkgHTgerr = totBkgTemp3[isEM].Clone()

# 		if (isEM=='EEE' and discriminant=="STrebinnedv2"): 
# 			for ibin in range(1,hTOP.GetNbinsX()):
# 				print "gaeBkgHT  -- bin: ",ibin," yield: ",gaeBkgHT.GetY()[ibin-1],", + ",gaeBkgHT.GetErrorYhigh(ibin-1)," - ",gaeBkgHT.GetErrorYlow(ibin-1)
# 				print "bkgHTgerr -- bin: ",ibin," yield: ",bkgHTgerr.GetY()[ibin-1],", + ",bkgHTgerr.GetErrorYhigh(ibin-1)," - ",bkgHTgerr.GetErrorYlow(ibin-1)

		'''
		scaleFact1 = int(bkgHT.GetMaximum()/hsig1.GetMaximum()) - int(bkgHT.GetMaximum()/hsig1.GetMaximum()) % 10
		scaleFact1 *= 0.60
		if scaleFact1==0: scaleFact1=int(bkgHT.GetMaximum()/hsig1.GetMaximum())
		if scaleFact1==0: scaleFact1=1
		if not scaleSignals:
			scaleFact1=1
 		#else:
 		#	scaleFact1=25
                '''
		hsig1.Scale(scaleFact1)
		hsig2.Scale(scaleFact1)
		hsig3.Scale(scaleFact1)
		hsig.Scale(scaleFact1)
		hsigM1500.Scale(scaleFact2)
		
		stackbkgHT = THStack("stackbkgHT","")
		try: stackbkgHT.Add(hTOP)
		except: pass
		try: stackbkgHT.Add(hEWK)
		except: pass
		try: 
			if hQCD.Integral()/bkgHT.Integral()>.005: stackbkgHT.Add(hQCD) #don't plot QCD if it is less than 0.5%
		except: pass
		try: stackbkgHT.Add(hDDBKG)
		except: pass

		try:
			hTOP.SetLineColor(kCyan)
			hTOP.SetFillColor(kCyan)
			hTOP.SetLineWidth(2)
		except: pass
		try: 
			hEWK.SetLineColor(kMagenta-2)
			hEWK.SetFillColor(kMagenta-2)
			hEWK.SetLineWidth(2)
		except: pass
		try:
			hQCD.SetLineColor(kOrange+5)
			hQCD.SetFillColor(kOrange+5)
			hQCD.SetLineWidth(2)
		except: pass
		try:
			hDDBKG.SetLineColor(15)
			hDDBKG.SetFillColor(15)
			hDDBKG.SetLineWidth(2)
		except: pass
		
		hsig.SetLineColor(kBlack)
		hsig.SetLineStyle(1)
		hsig.SetLineWidth(3)
		hsigM1500.SetLineColor(kBlack)
		hsigM1500.SetLineStyle(2)
		hsigM1500.SetLineWidth(3)
		hsig1.SetLineColor(kRed)
		hsig1.SetLineStyle(2)
		hsig1.SetLineWidth(3)
		hsig2.SetLineColor(kOrange-2)
		hsig2.SetLineStyle(5)
		hsig2.SetLineWidth(3)
		hsig3.SetLineColor(kGreen+1)
		hsig3.SetLineStyle(7)
		hsig3.SetLineWidth(3)
		
# 		hData.SetMarkerStyle(20)
# 		hData.SetMarkerSize(1.2)
# 		hData.SetLineWidth(2)
		gaeData.SetMarkerStyle(20)
		gaeData.SetMarkerSize(1.2)
		gaeData.SetLineWidth(2)
		gaeData.SetMarkerColor(kBlack)
		gaeData.SetLineColor(kBlack)

		bkgHTgerr.SetFillStyle(3004)
		bkgHTgerr.SetFillColor(kBlack)


		c1 = TCanvas("c1","c1",600,500)
		yDiv=0.25
		if blind == True: yDiv=0.1
		# for some reason the markers at 0 don't show with this setting:
		uMargin = 0.00001
		if blind == True: uMargin = 0.15
		rMargin=.04
		# overlap the pads a little to hide the error bar gap:
		#uPad=TPad("uPad","",0,yDiv-0.009,1,1) #for actual plots
		uPad=TPad("uPad","",0,yDiv,1,1) #for actual plots
		uPad.SetTopMargin(0.08)
		uPad.SetBottomMargin(uMargin)
		uPad.SetRightMargin(rMargin)
		uPad.SetLeftMargin(.105)
		uPad.Draw()
		if blind == False:
			lPad=TPad("lPad","",0,0,1,yDiv) #for sigma runner
			lPad.SetTopMargin(0.05)
			lPad.SetBottomMargin(.4)
			lPad.SetRightMargin(rMargin)
			lPad.SetLeftMargin(.105)
			lPad.SetGridy()
			lPad.Draw()

# 		try: 
# 			if not doNormByBinWidth: hData.SetMaximum(1.2*max(hData.GetMaximum(),bkgHT.GetMaximum()))
# 		except: 
# 			pass
# 		hData.SetMinimum(0.015)
# 		hData.SetTitle("")
# 		if doNormByBinWidth: hData.GetYaxis().SetTitle("Events / 1 GeV")
# 		else: hData.GetYaxis().SetTitle("Events")
# 		formatUpperHist(hData)
# 		uPad.cd()
# 		hData.SetTitle("")
# 		if not blind: hData.Draw("E1 X0")

		# this is super important now!! gaeData has badly defined (negative) maximum
		gaeData.SetMaximum(1.25*max(gaeData.GetMaximum(),bkgHT.GetMaximum()))
		gaeData.SetMinimum(0.015)
		gaeData.SetTitle("")
		if doNormByBinWidth: gaeData.GetYaxis().SetTitle("< Events / GeV >")
		else: gaeData.GetYaxis().SetTitle("Events / bin")
		formatUpperHist_v2(gaeData,hData)
		gaeData.GetXaxis().SetTitle("TEST")
		uPad.cd()
		gaeData.SetTitle("")
		gStyle.SetErrorX(0.);
		if not blind: gaeData.Draw("ap")

		if blind: 

			hsig1.SetMinimum(0.015)
			if doNormByBinWidth: hsig1.GetYaxis().SetTitle("Events / 1 GeV")
			else: hsig1.GetYaxis().SetTitle("Events")
			formatUpperHist(hsig1)
			hsig1.SetMaximum(hData.GetMaximum())
			hsig1.Draw("HIST")

		stackbkgHT.Draw("SAME HIST")
		hsig.Draw("SAME HIST")
		hsigM1500.Draw("SAME HIST")
# 		hsig1.Draw("SAME HIST")
# 		hsig2.Draw("SAME HIST")
# 		hsig3.Draw("SAME HIST")
		if not blind: gaeData.Draw("p") #redraw data so its not hidden
		uPad.RedrawAxis()
		gStyle.SetErrorX(0.5);
		bkgHTgerr.Draw("SAME E2")

		leg = {}
		if 'Tau21' in discriminant:
			leg = TLegend(0.15,0.53,0.45,0.90)
		elif 'Eta' in discriminant or 'deltaRjet2' in discriminant:
			leg = TLegend(0.72,0.43,0.95,0.90)
		else:
			leg = TLegend(0.360,0.622,0.939,0.89)
		leg.SetShadowColor(0)
		leg.SetFillColor(0)
		leg.SetFillStyle(0)
		leg.SetLineColor(0)
		leg.SetLineStyle(0)
		leg.SetBorderSize(0)
		leg.SetNColumns(2)
		leg.SetTextFont(62)
		leg.SetTextSize(0.06)
		if not blind: leg.AddEntry(gaeData,"Data","pel")
# 		try: leg.AddEntry(hDDBKG,"DD BKG","f")
		try: leg.AddEntry(hDDBKG,"Nonprompt","f")
		except: pass
		
		scaleFact1Str = ' x'+str(scaleFact1)
		scaleFact2Str = ' x'+str(scaleFact2)
		if not scaleSignals or dontShowSignalScaling:
			scaleFact1Str = ''
			scaleFact2Str = ''
		leg.AddEntry(hsig,sigleg+scaleFact1Str,"l")
		try: leg.AddEntry(hEWK,"VV(V)","f")
		except: pass
		leg.AddEntry(hsigM1500,siglegM1500+scaleFact2Str,"l")
		try: leg.AddEntry(hTOP,"t#bar{t}+V","f")
		except: pass
		try: 
			if hQCD.Integral()/bkgHT.Integral()>.005: leg.AddEntry(hQCD,"QCD","f") #don't plot QCD if it is less than 0.5%
		except: pass
		leg.AddEntry(bkgHTgerr,"","")
		leg.AddEntry(bkgHTgerr,"Bkg uncert.","f")
		leg.Draw("same")

		prelimTex=TLatex()
		prelimTex.SetNDC()
		prelimTex.SetTextAlign(31) # align right
		prelimTex.SetTextFont(42)
		prelimTex.SetTextSize(0.07)
		prelimTex.SetLineWidth(2)
		prelimTex.DrawLatex(0.95,0.94,str(lumi)+" fb^{-1} (13 TeV)")

		prelimTex2=TLatex()
		prelimTex2.SetNDC()
		prelimTex2.SetTextFont(61)
		prelimTex2.SetLineWidth(2)
		prelimTex2.SetTextSize(0.10)
		prelimTex2.DrawLatex(0.16,0.81,"CMS")

		prelimTex3=TLatex()
		prelimTex3.SetNDC()
		prelimTex3.SetTextAlign(13)
		prelimTex3.SetTextFont(52)
		prelimTex3.SetTextSize(0.075)
		prelimTex3.SetLineWidth(2)
# 		if not blind: prelimTex3.DrawLatex(0.24,0.975,"Preliminary")
# 		#if blind: prelimTex3.DrawLatex(0.29175,0.9364,"Preliminary")
# 		if blind: prelimTex3.DrawLatex(0.29175,0.975,"Preliminary")
# 		prelimTex3.SetTextSize(0.06) #for Supplementary
# 		if not blind: prelimTex3.DrawLatex(0.14,0.78,"Supplementary")
# 		if not blind: prelimTex3.DrawLatex(0.14,0.78,"Preliminary")

		chLatex = TLatex()
		chLatex.SetNDC()
		chLatex.SetTextSize(0.08)
		chLatex.SetTextAlign(31) # align right
		chString = ''
		if isEM=='All': chString+='All channels'
		if isEM=='EEE': chString+='eee'
		if isEM=='EEM': chString+='ee#mu'
		if isEM=='EMM': chString+='e#mu#mu'
		if isEM=='MMM': chString+='#mu#mu#mu'
		chLatex.DrawLatex(0.92, 0.56, chString)

		flat = TF1("flat","pol1",30,250);

		line = TF1("line","pol1",250,1500);
		line2 = TF1("line2","pol1",30,1500);
		line3 = TF1("line3","pol1",30,1500);
		line4 = TF1("line4","pol1",30,1500);

		line.SetLineWidth(2);

		para = TF1("para","pol2",30,1500); para.SetLineColor(kBlue);
		para2 = TF1("para2","pol2",30,1500); para2.SetLineColor(kBlue);
		para3 = TF1("para3","pol2",30,1500); para3.SetLineColor(kBlue);

		cube = TF1("cube","pol3",30,1500); cube.SetLineColor(kGreen);
		cube2 = TF1("cube2","pol3",30,1500); cube2.SetLineColor(kGreen);
		cube3 = TF1("cube3","pol3",30,1500); cube3.SetLineColor(kGreen);

		if blind == False and not doRealPull:
			lPad.cd()
			pull=hData.Clone("pull")
#			pull.Scale(1.0/pull.Integral())
#			pullDenom = bkgHT.Clone("pullDenom")
#			pullDenom.Scale(1.0/pullDenom.Integral())
#			pull.Divide(pullDenom)
			try: pull.Divide(hData, bkgHT)
			except: pass
			
			try:
				for binNo in range(0,hData.GetNbinsX()+2):
					if bkgHT.GetBinContent(binNo)!=0:
						pull.SetBinError(binNo,hData.GetBinError(binNo)/bkgHT.GetBinContent(binNo))
			except: pass

			pullData=TGraphAsymmErrors(pull.Clone("pullData"))
			for binNo in range(0,hData.GetNbinsX()+2):
				if bkgHT.GetBinContent(binNo)!=0:
					pullData.SetPointEYhigh(binNo-1,gaeData.GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
					pullData.SetPointEYlow(binNo-1,gaeData.GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))
			
			pull.SetMaximum(3)
			pull.SetMinimum(0)
			pull.SetFillColor(1)
			pull.SetLineColor(1)
			formatLowerHist(pull)

			pull.Draw("E0")
			pull.Draw("ap")

			if 'Bins' in discriminant:
				print '******************************'
				print 'Data/MC for',discriminant
				for binNo in range(0,pull.GetNbinsX()+2):
					print 'Bin',binNo,': content =',pull.GetBinContent(binNo),'; error =',pull.GetBinError(binNo),';'
		
			BkgOverBkg = pull.Clone("bkgOverbkg")
			try: BkgOverBkg.Divide(bkgHT, bkgHT)
			except: pass
			pullUncBandTot=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncTot"))
			
			try:
				for binNo in range(0,hData.GetNbinsX()+2):
					if bkgHT.GetBinContent(binNo)!=0:
						pullUncBandTot.SetPointEYhigh(binNo-1,totBkgTemp3[isEM].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandTot.SetPointEYlow(binNo-1,totBkgTemp3[isEM].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
			except: pass
						
			if not doOneBand: pullUncBandTot.SetFillStyle(3001)
			else: pullUncBandTot.SetFillStyle(3344)
			pullUncBandTot.SetFillColor(1)
			pullUncBandTot.SetLineColor(1)
			pullUncBandTot.SetMarkerSize(0)
			gStyle.SetHatchesLineWidth(1)
			pullUncBandTot.Draw("SAME E2")
				
			pullUncBandNorm=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncNorm"))

			try:
				for binNo in range(0,hData.GetNbinsX()+2):
					if bkgHT.GetBinContent(binNo)!=0:
						pullUncBandNorm.SetPointEYhigh(binNo-1,totBkgTemp2[isEM].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandNorm.SetPointEYlow(binNo-1,totBkgTemp2[isEM].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))
			except: pass			

			pullUncBandNorm.SetFillStyle(3001)
			pullUncBandNorm.SetFillColor(2)
			pullUncBandNorm.SetLineColor(2)
			pullUncBandNorm.SetMarkerSize(0)
			gStyle.SetHatchesLineWidth(1)
			if not doOneBand: pullUncBandNorm.Draw("SAME E2")
			
			pullUncBandStat=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncStat"))

			try:
				for binNo in range(0,hData.GetNbinsX()+2):
					if bkgHT.GetBinContent(binNo)!=0:
						pullUncBandStat.SetPointEYhigh(binNo-1,totBkgTemp1[isEM].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandStat.SetPointEYlow(binNo-1,totBkgTemp1[isEM].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
			except: pass
			
			pullUncBandStat.SetFillStyle(3001)
			pullUncBandStat.SetFillColor(3)
			pullUncBandStat.SetLineColor(3)
			pullUncBandStat.SetMarkerSize(0)
			gStyle.SetHatchesLineWidth(1)
			if not doOneBand: pullUncBandStat.Draw("SAME E2")

			pullLegend=TLegend(0.14,0.87,0.85,0.96)
			SetOwnership( pullLegend, 0 )   # 0 = release (not keep), 1 = keep
			pullLegend.SetShadowColor(0)
			pullLegend.SetNColumns(3)
			pullLegend.SetFillColor(0)
			pullLegend.SetFillStyle(0)
			pullLegend.SetLineColor(0)
			pullLegend.SetLineStyle(0)
			pullLegend.SetBorderSize(0)
			pullLegend.SetTextFont(42)
			if not doOneBand: pullLegend.AddEntry(pullUncBandStat , "Bkg shape syst." , "f")
			if not doOneBand: pullLegend.AddEntry(pullUncBandNorm , "Bkg shape #oplus norm. syst." , "f")
			if not doOneBand: pullLegend.AddEntry(pullUncBandTot , "Bkg stat. #oplus all syst." , "f")
#			else: pullLegend.AddEntry(pullUncBandTot , "Bkg stat. #oplus syst." , "f")
			else: 
				pullLegend.AddEntry(pullUncBandTot , "Bkg stat." , "f")
			#	pullLegend.AddEntry(jsf, "Fit","l")
			#	pullLegend.AddEntry(jsfup, "#pm 1#sigma","l")
			pullLegend.Draw("SAME")
			pull.Draw("SAME")
			lPad.RedrawAxis()

		if blind == False and doRealPull:
			lPad.cd()
			pull=hData.Clone(hData.GetName()+'pull')
			for binNo in range(1,hData.GetNbinsX()+1):
				# case for data < MC:
				dataerror = gaeData.GetErrorYhigh(binNo-1)
				MCerror = totBkgTemp3[isEM].GetErrorYlow(binNo-1)
				# case for data > MC: 
				if(hData.GetBinContent(binNo) > bkgHT.GetBinContent(binNo)):
					dataerror = gaeData.GetErrorYlow(binNo-1)
					MCerror = totBkgTemp3[isEM].GetErrorYhigh(binNo-1)
				if(dataerror+MCerror!=0):pull.SetBinContent(binNo,(hData.GetBinContent(binNo)-bkgHT.GetBinContent(binNo))/math.sqrt(MCerror**2+dataerror**2))
			pull.SetMaximum(3)
			pull.SetMinimum(-3)
			pull.SetFillColor(kGray+2)
			pull.SetLineColor(kGray+2)
			formatLowerHist(pull)
			pull.Draw("HIST")

		savePrefix = templateDir+'/plots/'
		if not os.path.exists(savePrefix): os.system('mkdir '+savePrefix)
		savePrefix+=histPrefix+isRebinned
		if doRealPull: savePrefix+='_pull'
		if yLog: savePrefix+='_logy'
		if blind: savePrefix+='_blinded'

		if doOneBand:
			c1.SaveAs(savePrefix+"_totBand.pdf")
			c1.SaveAs(savePrefix+"_totBand.png")
			c1.SaveAs(savePrefix+"_totBand.root")
			c1.SaveAs(savePrefix+"totBand.C")
		else:
			c1.SaveAs(savePrefix+".pdf")
			c1.SaveAs(savePrefix+".png")
			c1.SaveAs(savePrefix+".root")
			c1.SaveAs(savePrefix+".C")
			
	RFile.Close()

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))
