#!/usr/bin/python

import os,sys,time,math,pickle,itertools
from ROOT import *
from weights import *

gROOT.SetBatch(1)
start_time = time.time()

lumi=35.9 #for plot
lumiInTemplates=str(targetlumi/1000).replace('.','p') # 1/fb

discriminant = 'STrebinned'

saveKey = ''#'_topPtSystOnly'

# m1 = '800'
# sig1='X53X53M'+m1+'left' # choose the 1st signal to plot
# sig1leg='X_{5/3}#bar{X}_{5/3} LH (0.8 TeV)'
# m2 = '800'
# sig2='X53X53M'+m1+'right' # choose the 2nd signal to plot
# sig2leg='X_{5/3}#bar{X}_{5/3} RH (0.8 TeV)'
m1 = '800'
sig1='TTM'+m1 # choose the 1st signal to plot
sig1leg='TT (0.8 TeV)'
m2 = '1200'
sig2='TTM'+m2 # choose the 2nd signal to plot
sig2leg='TT (1.2 TeV)'
scaleSignals = True

# systematicList = ['pileup','btag','mistag','jec','jer','pdfNew','muRFcorrdNew','elPR','elFR','muPR','muFR']
systematicList = ['pileup','btag','mistag','pdfNew','muRFcorrdNewTop','muRFcorrdNewEwk','muRFcorrdNewSig','jec','jer','elPR','elFR','muPR','muFR']

normSystematics = {
					'elIdSys':{'EEE':0.06,'EEM':0.04,'EMM':0.02,'MMM':0.00},
					'muIdSys':{'EEE':0.00,'EEM':0.02,'EMM':0.04,'MMM':0.06},
					'elIsoSys':{'EEE':0.03,'EEM':0.02,'EMM':0.01,'MMM':0.00},
					'muIsoSys':{'EEE':0.00,'EEM':0.01,'EMM':0.02,'MMM':0.03},
					'elelelTrigSys':{'EEE':0.03,'EEM':0.00,'EMM':0.00,'MMM':0.00},
					'elelmuTrigSys':{'EEE':0.00,'EEM':0.03,'EMM':0.00,'MMM':0.00},
					'elmumuTrigSys':{'EEE':0.00,'EEM':0.00,'EMM':0.03,'MMM':0.00},
					'mumumuTrigSys':{'EEE':0.00,'EEM':0.00,'EMM':0.00,'MMM':0.03},
					}

# ddbkgSystematics = {
# 					'elPRsys':{'EEE':0.38,'EEM':0.12,'EMM':0.07,'MMM':0.00},
# 					'muPRsys':{'EEE':0.00,'EEM':0.02,'EMM':0.04,'MMM':0.09},
# 					'muFReta':{'EEE':0.00,'EEM':0.22,'EMM':0.11,'MMM':0.48}
# 					}

ddbkgSystematics = {
					'elPRsys':{'EEE':0.09,'EEM':0.15,'EMM':0.08,'MMM':0.00},
					'muPRsys':{'EEE':0.00,'EEM':0.04,'EMM':0.08,'MMM':0.17},
					'muFReta':{'EEE':0.00,'EEM':0.13,'EMM':0.10,'MMM':0.24}
					}


doAllSys = True

isRebinned=''#'_rebinned'#post fix for file names if the name changed b/c of rebinning or some other process
doNormByBinWidth=False # not tested, may not work out of the box
doOneBand = False
if not doAllSys: doOneBand = True # Don't change this!
blind = True
yLog  = False
doRealPull = False
if doRealPull: doOneBand=False


# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST600_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST700_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST800_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST900_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1000_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1100_mllOS20'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/'+cutString+'/'

# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20'
cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST800_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST900_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1000_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1100_mllOS20'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/'+cutString+'/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/'+cutString+'/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_6Feb2017_step2_2017_2_6/'+cutString+'/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_step2_2017_2_7/'+cutString+'/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_step2_2017_2_8/'+cutString+'/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_ALLsys_step2_addmistag_addMoreSignal_2017_2_17/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/4binsCount_updatedLumi_updatedLepIdUnc_addmistag_normRENORMPDF/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_newMllOScut_fixedAllSYS_step2_addmistag_addMoreSignal_2017_2_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/4binsCount_newMllOScut/'

# templateDir='/user_data/rsyarif/optimization_condor_PRv6_FRv20b_newMllOSV2_Allsys_2017_3_1/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/4binsCount/'
# templateDir='/user_data/rsyarif/optimization_condor_PRv6_FRv20b_newMllOSV2_Allsys_2017_3_1/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/4binsCount/'

# templateDir='/user_data/rsyarif/optimization_reMiniAOD_PRv6_FRv24_newMuTrkSF_AllSys_2017_3_5/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1100_mllOS20/4binsCount/'

# templateDir='/user_data/rsyarif/optimization_reMiniAOD_PRv9_FRv24_newFRsys_AllSys_2017_3_10/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/4binsCount/'

templateDir='/user_data/rsyarif/optimization_reMiniAOD_PRv9_FRv24_newFRsys_AllSys_2017_3_10/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/4binsCount_accurateLHEsys/'

BRconfStr='_bW0p5_tZ0p25_tH0p25'
# BRconfStr='_bW0p0_tZ0p5_tH0p5'
# BRconfStr='_bW0p0_tZ1p0_tH0p0'

tempsig='templates_'+discriminant+'_'+sig1+BRconfStr+'_'+lumiInTemplates+'fb'+isRebinned+'.root'	


isEMlist =['EEE','EEM','EMM','MMM']
nttaglist=['']
nWtaglist=['']
nbtaglist=['']
# catList = list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist))
catList = ['EEE','EEM','EMM','MMM']
tagList = list(itertools.product(nttaglist,nWtaglist,nbtaglist))

lumiSys = 0.026 #https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
lepIdSys = math.sqrt(3.*0.02**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty


#ATTENTION!!! THESE NEED TO BE UPDATED AND SYS NEED TO BE APPLED!

def getNormUnc(hist,ibin):
	contentsquared = hist.GetBinContent(ibin)**2
	#print 'catList[ibin-1]:', catList[ibin-1]
	corrdSysSq = lumiSys**2 + trigSys**2 + normSystematics['elIdSys'][catList[ibin-1]]**2 + normSystematics['muIdSys'][catList[ibin-1]]**2 + normSystematics['elIsoSys'][catList[ibin-1]]**2 + normSystematics['muIsoSys'][catList[ibin-1]]**2 
	error = corrdSysSq * contentsquared  #correlated uncertainties
	if 'top' in hist.GetName(): error += topXsecSys*topXsecSys*contentsquared # cross section
	if 'ewk' in hist.GetName(): error += ewkXsecSys*ewkXsecSys*contentsquared # cross section
	if 'qcd' in hist.GetName(): error += qcdXsecSys*qcdXsecSys*contentsquared # cross section
	return error

def getDDBKGNormUnc(hist,ibin):
	contentsquared = hist.GetBinContent(ibin)**2
	error = (ddbkgSystematics['elPRsys'][catList[ibin-1]]**2 + ddbkgSystematics['muPRsys'][catList[ibin-1]]**2 + ddbkgSystematics['muFReta'][catList[ibin-1]]**2) * contentsquared  #correlated uncertainties
	return error

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
		histogram.GetYaxis().SetLabelSize(0.07)
		histogram.GetYaxis().SetTitleSize(0.08)
		histogram.GetYaxis().SetTitleOffset(.71)

	if 'nB0' in histogram.GetName() and 'minMlb' in histogram.GetName(): histogram.GetXaxis().SetTitle("min[M(l,jets)] (GeV)")
	histogram.GetYaxis().CenterTitle()
	histogram.SetMinimum(0.00101)
	if not yLog: 
		histogram.SetMinimum(0.25)
	if yLog:
		uPad.SetLogy()
		if not doNormByBinWidth: histogram.SetMaximum(200*histogram.GetMaximum())
		
def formatLowerHist(histogram):
	histogram.GetXaxis().SetLabelSize(.12)
	histogram.GetXaxis().SetTitleSize(0.15)
	histogram.GetXaxis().SetTitleOffset(0.95)
	histogram.GetXaxis().SetNdivisions(506)
	#histogram.GetXaxis().SetTitle("S_{T} (GeV)")

	histogram.GetYaxis().SetLabelSize(0.12)
	histogram.GetYaxis().SetTitleSize(0.14)
	histogram.GetYaxis().SetTitleOffset(.37)
	histogram.GetYaxis().SetTitle('Data/Bkg')
	histogram.GetYaxis().SetNdivisions(5)
	if doRealPull: histogram.GetYaxis().SetRangeUser(min(-2.99,0.8*histogram.GetBinContent(histogram.GetMaximumBin())),max(2.99,1.2*histogram.GetBinContent(histogram.GetMaximumBin())))
	else: histogram.GetYaxis().SetRangeUser(0,2.99)
	histogram.GetYaxis().CenterTitle()

def negBinCorrection(hist): #set negative bin contents to zero and adjust the normalization
	norm0=hist.Integral()
	for iBin in range(0,hist.GetNbinsX()+2):
		if hist.GetBinContent(iBin)<0: hist.SetBinContent(iBin,0)
	if hist.Integral()!=0: hist.Scale(norm0/hist.Integral())

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

print 'Attempting to open:',templateDir+tempsig.replace(sig1,sig1)
RFile1 = TFile(templateDir+tempsig.replace(sig1,sig1))
RFile2 = TFile(templateDir+tempsig.replace(sig1,sig2))
systHists = {}
totBkgTemp1 = {}
totBkgTemp2 = {}
totBkgTemp3 = {}
# for cat in catList:
for cat in ['']: # you dont really need to loop.
	histPrefix='triLep'
# 	histPrefix=discriminant+'_'+lumiInTemplates+'fb_'
# 	tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
# 	catStr='is'+cat[0]+'_'+tagStr
# 	isEM=cat[0]
	catStr=cat
	isEM=cat
# 	histPrefix+=catStr
	print 'histPrefix:', histPrefix
	hTOP = RFile1.Get(histPrefix+'__top').Clone()
	try: hEWK = RFile1.Get(histPrefix+'__ewk').Clone()
	except:
		print "There is no EWK!!!!!!!!"
		print "Skipping EWK....."
		pass
	try: hQCD = RFile1.Get(histPrefix+'__qcd').Clone()
	except:
		print "There is no QCD!!!!!!!!"
		print "Skipping QCD....."
		pass
	try: hDDBKG = RFile1.Get(histPrefix+'__ddbkg').Clone()
	except:
		print "There is no DDBKG!!!!!!!!"
		print "Skipping DDBKG....."
		pass
	hData = RFile1.Get(histPrefix+'__DATA').Clone()
	hsig1 = RFile1.Get(histPrefix+'__sig').Clone(histPrefix+'__sig1')
	hsig2 = RFile2.Get(histPrefix+'__sig').Clone(histPrefix+'__sig2')
	hsig1.Scale(xsec[sig1])
	hsig2.Scale(xsec[sig2])
	if doNormByBinWidth:
		normByBinWidth(hTOP)
		normByBinWidth(hEWK)
		normByBinWidth(hQCD)
		normByBinWidth(hsig1)
		normByBinWidth(hsig2)
		normByBinWidth(hData)

	if doAllSys:
		for sys in systematicList:
			for ud in ['minus','plus']:
				try: systHists['top'+catStr+sys+ud] = RFile1.Get(histPrefix+'__top__'+sys+'__'+ud).Clone()
				#systHists['top'+catStr+sys+ud] = systHists['top'+catStr+sys+ud].Clone()
				except: 
					print "Skipping",sys,"for TOP"
					pass
				try: systHists['ewk'+catStr+sys+ud] = RFile1.Get(histPrefix+'__ewk__'+sys+'__'+ud).Clone()
				except: 
					print "Skipping",sys,"for EWK"
					pass
				try: systHists['qcd'+catStr+sys+ud] = RFile1.Get(histPrefix+'__qcd__'+sys+'__'+ud).Clone()
				except: 
					print "Skipping",sys,"for QCD"
					pass
				try: systHists['ddbkg'+catStr+sys+ud] = RFile1.Get(histPrefix+'__ddbkg__'+sys+'__'+ud).Clone()
				except: 
					print "Skipping",sys,"for DDBKG"
					pass

	bkgHT = hTOP.Clone()
	try: bkgHT.Add(hEWK)
	except: pass
	try: bkgHT.Add(hQCD)
	except: pass
	try: bkgHT.Add(hDDBKG)
	except: pass
	
	print 'hTOP.Integral():',hTOP.Integral(),
	print ', EEE:',hTOP.GetBinContent(1),
	print ', EEM:',hTOP.GetBinContent(2),
	print ', EMM:',hTOP.GetBinContent(3),
	print ', MMM:',hTOP.GetBinContent(4)
	print 'hEWK.Integral():',hEWK.Integral(),
	print ', EEE:',hEWK.GetBinContent(1),
	print ', EEM:',hEWK.GetBinContent(2),
	print ', EMM:',hEWK.GetBinContent(3),
	print ', MMM:',hEWK.GetBinContent(4)
	print 'hDDBKG.Integral():',hDDBKG.Integral(),
	print ', EEE:',hDDBKG.GetBinContent(1),
	print ', EEM:',hDDBKG.GetBinContent(2),
	print ', EMM:',hDDBKG.GetBinContent(3),
	print ', MMM:',hDDBKG.GetBinContent(4)

	print 'bkgHT.Integral():',bkgHT.Integral(),
	print ', EEE:',bkgHT.GetBinContent(1),
	print ', EEM:',bkgHT.GetBinContent(2),
	print ', EMM:',bkgHT.GetBinContent(3),
	print ', MMM:',bkgHT.GetBinContent(4)
	
# 	totBkgTemp1[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
# 	totBkgTemp2[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
# 	totBkgTemp3[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))

	totBkgTemp1 = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
	totBkgTemp2 = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
	totBkgTemp3 = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))
	

# 	for ibin in range(1,hTOP.GetNbinsX()+1):
	for ibin in range(1,hTOP.GetNbinsX()+1): #here the bins are bin1:EEE,bin2:EEM,bin3:EMM,bin4:MMM
		print ''
		print '----- ibin:', ibin, '(',catList[ibin-1],') ----'
		print ''
		print 'hEWK.GetBinError(',catList[ibin-1],'):',hEWK.GetBinError(ibin)
		print 'hTOP.GetBinError(',catList[ibin-1],'):',hTOP.GetBinError(ibin)
		print 'hDDBKG.GetBinError(',catList[ibin-1],'):',hDDBKG.GetBinError(ibin)
		print 'bkgHT.GetBinError(',catList[ibin-1],'):',bkgHT.GetBinError(ibin)
		print 'math.sqrt( getNormUnc(hEWK,',catList[ibin-1],') ):',math.sqrt(getNormUnc(hEWK,ibin))
		print 'math.sqrt( getNormUnc(hTOP,',catList[ibin-1],') ):',math.sqrt(getNormUnc(hTOP,ibin))
		print 'math.sqrt( getDDBKGNormUnc(hDDBKG,',catList[ibin-1],') ):',math.sqrt(getDDBKGNormUnc(hDDBKG,ibin))
		errorUp = 0.
		errorDn = 0.
		errorStatOnly = bkgHT.GetBinError(ibin)**2
		errorNorm = getNormUnc(hTOP,ibin)
		try: errorNorm += getNormUnc(hEWK,ibin)
		except: pass
		try: errorNorm += getNormUnc(hQCD,ibin)
		except: pass
		try: errorNorm += getDDBKGNormUnc(hDDBKG,ibin)
		except: pass

		if doAllSys:
			topTotErrUp = 0.0
			topTotErrDn = 0.0
			topTotErrSym = 0.0
			ewkTotErrUp = 0.0
			ewkTotErrDn = 0.0
			ewkTotErrSym = 0.0
			ddbkgTotErrUp = 0.0
			ddbkgTotErrDn = 0.0
			ddbkgTotErrSym = 0.0
			for sys in systematicList:
				print '	sys:',sys
				if not ('PR' in sys or 'FR' in sys or 'Ewk' in sys or 'Sig' in sys):
					try:
						errorPlus = systHists['top'+catStr+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin)
						errorMinus = hTOP.GetBinContent(ibin)-systHists['top'+catStr+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
# 						print '		top',sys,'Up  :',  systHists['top'+catStr+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin)
# 						print '		top',sys,'Dn  :',  hTOP.GetBinContent(ibin)-systHists['top'+catStr+sys+'minus'].GetBinContent(ibin)
						print '		top',sys,'sym :',  0.5*(math.fabs(systHists['top'+catStr+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin)) + math.fabs(hTOP.GetBinContent(ibin)-systHists['top'+catStr+sys+'minus'].GetBinContent(ibin)))
						topTotErrUp+= (systHists['top'+catStr+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin))**2
						topTotErrDn+= (hTOP.GetBinContent(ibin)-systHists['top'+catStr+sys+'minus'].GetBinContent(ibin))**2						
						topTotErrSym +=  ( 0.5*(math.fabs(errorPlus)+math.fabs(errorMinus)) ) **2
						print '				top (sys) after adding',sys,' :',math.sqrt( (0.5*(math.sqrt(math.fabs(topTotErrUp))+math.sqrt(math.fabs(topTotErrDn))))**2 + (getNormUnc(hTOP,ibin)))
						print '				top (sys Sym) after adding',sys,' :',math.sqrt( topTotErrSym + (getNormUnc(hTOP,ibin) ) )
					except: pass
				if not ('PR' in sys or 'FR' in sys or 'Top' in sys or 'Sig' in sys):
					try:
						errorPlus = systHists['ewk'+catStr+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin)
						errorMinus = hEWK.GetBinContent(ibin)-systHists['ewk'+catStr+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
# 						print '		ewk',sys,'Up  :',  systHists['ewk'+catStr+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin)
# 						print '		ewk',sys,'Dn  :',  hEWK.GetBinContent(ibin)-systHists['ewk'+catStr+sys+'minus'].GetBinContent(ibin)
						print '		ewk',sys,'sym :',  0.5*(math.fabs(systHists['ewk'+catStr+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin)) + math.fabs(hEWK.GetBinContent(ibin)-systHists['ewk'+catStr+sys+'minus'].GetBinContent(ibin)))
						ewkTotErrUp+=(systHists['ewk'+catStr+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin))**2
						ewkTotErrDn+=(hEWK.GetBinContent(ibin)-systHists['ewk'+catStr+sys+'minus'].GetBinContent(ibin))**2						
						ewkTotErrSym +=  ( 0.5*(math.fabs(errorPlus)+math.fabs(errorMinus)) ) **2
						print '				ewk (sys) after adding',sys,' :',math.sqrt( (0.5*(math.sqrt(math.fabs(ewkTotErrUp))+math.sqrt(math.fabs(ewkTotErrDn))))**2 + (getNormUnc(hEWK,ibin)))
						print '				ewk (sys Sym) after adding',sys,' :',math.sqrt( ewkTotErrSym + (getNormUnc(hEWK,ibin) ) )
					except: pass
					try:
						errorPlus = systHists['qcd'+catStr+sys+'plus'].GetBinContent(ibin)-hQCD.GetBinContent(ibin)
						errorMinus = hQCD.GetBinContent(ibin)-systHists['qcd'+catStr+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
					except: pass													
				if 'PR' in sys or 'FR' in sys:
					try: errorSym += (0.5*abs(systHists['ddbkg'+catStr+sys+'plus'].GetBinContent(ibin)-systHists['ddbkg'+catStr+sys+'minus'].GetBinContent(ibin)))**2				
					except: pass
					try: errorPlus = systHists['ddbkg'+catStr+sys+'plus'].GetBinContent(ibin)-hDDBKG.GetBinContent(ibin)
					except: pass
					try: errorMinus = hDDBKG.GetBinContent(ibin)-systHists['ddbkg'+catStr+sys+'minus'].GetBinContent(ibin)
					except: pass
					if errorPlus > 0: errorUp += errorPlus**2
					else: errorDn += errorPlus**2
					if errorMinus > 0: errorDn += errorMinus**2
					else: errorUp += errorMinus**2
					ddbkgTotErrUp+= (systHists['ddbkg'+catStr+sys+'plus'].GetBinContent(ibin)-hDDBKG.GetBinContent(ibin) )**2
					ddbkgTotErrDn+= (hDDBKG.GetBinContent(ibin)-systHists['ddbkg'+catStr+sys+'minus'].GetBinContent(ibin) )**2
					ddbkgTotErrSym +=  ( 0.5*( math.fabs(errorPlus)+math.fabs(errorMinus) ) ) **2
# 					print '		ddbkg',sys,'Up  :',  systHists['ddbkg'+catStr+sys+'plus'].GetBinContent(ibin)-hDDBKG.GetBinContent(ibin)
# 					print '		ddbkg',sys,'Dn  :',  hDDBKG.GetBinContent(ibin)-systHists['ddbkg'+catStr+sys+'minus'].GetBinContent(ibin)
					print '		ddbkg',sys,'sym :',  0.5*(math.fabs(errorPlus) + math.fabs(errorMinus))


# 		print '			ddbkgTotErrUp:',math.sqrt(ddbkgTotErrUp+getDDBKGNormUnc(hDDBKG,ibin))
# 		print '			ddbkgTotErrDn:',math.sqrt(ddbkgTotErrDn+getDDBKGNormUnc(hDDBKG,ibin))
		
		print ''
		print '			top(stat) 				:', hTOP.GetBinError(ibin)
		print '			top math.sqrt(getNormUnc) 		:', math.sqrt(getNormUnc(hTOP,ibin)) 
		print '			top (stat+math.sqrt(getNormUnc)) 	:', math.sqrt(hTOP.GetBinError(ibin)**2 + getNormUnc(hTOP,ibin)) 
		print '			top (sys) 				:', math.sqrt( ( 0.5*(math.sqrt(math.fabs(topTotErrUp))+math.sqrt(math.fabs(topTotErrDn))) )**2 + getNormUnc(hTOP,ibin) )
		print '			top (sys Sym) 				:', math.sqrt( topTotErrSym  + getNormUnc(hTOP,ibin) )
		print '		-->	top (stat+sys) 				:', math.sqrt( ( 0.5*(math.sqrt(math.fabs(topTotErrUp))+math.sqrt(math.fabs(topTotErrDn))) )**2 + getNormUnc(hTOP,ibin) + hTOP.GetBinError(ibin)**2 ),'<--'
		print ''
		print '			ewk(stat) 				:', hEWK.GetBinError(ibin)
		print '			ewk math.sqrt(getNormUnc) 		:', math.sqrt(getNormUnc(hEWK,ibin)) 
		print '			ewk (stat+math.sqrt(getNormUnc)) 	:', math.sqrt(hEWK.GetBinError(ibin)**2 + getNormUnc(hEWK,ibin)) 
		print '			ewk (sys) 				:', math.sqrt( ( 0.5*(math.sqrt(math.fabs(ewkTotErrUp))+math.sqrt(math.fabs(ewkTotErrDn))) )**2 + getNormUnc(hEWK,ibin) )
		print '			ewk (sys Sym) 				:', math.sqrt( ewkTotErrSym  + getNormUnc(hEWK,ibin) )
		print '		-->	ewk (stat+sys) 				:', math.sqrt( ( 0.5*(math.sqrt(math.fabs(ewkTotErrUp))+math.sqrt(math.fabs(ewkTotErrDn))) )**2 + getNormUnc(hEWK,ibin) + hEWK.GetBinError(ibin)**2 ),'<--'
		print ''
		print '			ddbkgTotSym (stat) 			:', hDDBKG.GetBinError(ibin)
# 		print '			ddbkgTotSym (stat) ** 2 		:', hDDBKG.GetBinError(ibin) ** 2
		print '			ddbkgTotSym math.sqrt(getDDBKGNormUnc) 	:', math.sqrt(getDDBKGNormUnc(hDDBKG,ibin)) 
# 		print '			ddbkgTotSym (getDDBKGNormUnc) 		:', getDDBKGNormUnc(hDDBKG,ibin) 
		print '			ddbkgTotSym (stat+getDDBKGNormUnc) 	:', math.sqrt( hDDBKG.GetBinError(ibin)**2 + getDDBKGNormUnc(hDDBKG,ibin) )
		print '			ddbkgTotSym (sys) 			:', math.sqrt(( 0.5*(math.sqrt(math.fabs(ddbkgTotErrUp))+math.sqrt(math.fabs(ddbkgTotErrDn))) )**2 + getDDBKGNormUnc(hDDBKG,ibin) )
		print '			ddbkgTotSym (sys Sym) 			:', math.sqrt( ddbkgTotErrSym  + getDDBKGNormUnc(hDDBKG,ibin) )
		print '		-->	ddbkgTotSym (stat+sys) 			:', math.sqrt( ( 0.5*(math.sqrt(math.fabs(ddbkgTotErrUp))+math.sqrt(math.fabs(ddbkgTotErrDn))) )**2 + getDDBKGNormUnc(hDDBKG,ibin) + hDDBKG.GetBinError(ibin)**2 ),'<--'

# 		totBkgTemp1[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp))
# 		totBkgTemp1[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn))
# 		totBkgTemp2[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
# 		totBkgTemp2[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm))
# 		totBkgTemp3[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatOnly))
# 		totBkgTemp3[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm+errorStatOnly))

		totBkgTemp1.SetPointEYhigh(ibin-1,math.sqrt(errorUp))
		totBkgTemp1.SetPointEYlow(ibin-1, math.sqrt(errorDn))
		totBkgTemp2.SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
		totBkgTemp2.SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm))
		totBkgTemp3.SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatOnly))
		totBkgTemp3.SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm+errorStatOnly))

# 		print '	totBkgTemp3.GetErrorYhigh(',catList[ibin-1],'):',totBkgTemp3.GetErrorYhigh(ibin-1)
# 		print '	totBkgTemp3.GetErrorYlow(',catList[ibin-1],') :',totBkgTemp3.GetErrorYlow(ibin-1)

		print ''
		print '	total sqrt(errorUp) in ',catList[ibin-1],' :',math.sqrt(errorUp)
		print '	total sqrt(errorDn) in ',catList[ibin-1],' :',math.sqrt(errorDn)
		print '	total sqrt(errorNorm+errorStatOnly) in ',catList[ibin-1],' :',math.sqrt(errorNorm+errorStatOnly)
		print '	total sqrt(errorUp+errorNorm+errorStatOnly) in ',catList[ibin-1],' :',math.sqrt(errorUp+errorNorm+errorStatOnly)
		print '	total sqrt(errorDn+errorNorm+errorStatOnly) in ',catList[ibin-1],' :',math.sqrt(errorDn+errorNorm+errorStatOnly)
		print ''
		print '		--> total stat+sys error in ',catList[ibin-1],' :',(math.fabs(totBkgTemp3.GetErrorYhigh(ibin-1))+math.fabs(totBkgTemp3.GetErrorYlow(ibin-1)))*0.5,'<--'
		print ''

# 	bkgHTgerr = totBkgTemp3[catStr].Clone()
	bkgHTgerr = totBkgTemp3.Clone()

	scaleFact1 = int(bkgHT.GetMaximum()/hsig1.GetMaximum()) - int(bkgHT.GetMaximum()/hsig1.GetMaximum()) % 10
	scaleFact2 = int(bkgHT.GetMaximum()/hsig2.GetMaximum()) - int(bkgHT.GetMaximum()/hsig2.GetMaximum()) % 10
	if scaleFact1==0: scaleFact1=int(bkgHT.GetMaximum()/hsig1.GetMaximum())
	if scaleFact2==0: scaleFact2=int(bkgHT.GetMaximum()/hsig2.GetMaximum())
	if scaleFact1==0: scaleFact1=1
	if scaleFact2==0: scaleFact2=1
	if not scaleSignals:
		scaleFact1=1
		scaleFact2=1
	else:
		scaleFact1=1.0
		scaleFact2=5.
	hsig1.Scale(scaleFact1)
	hsig2.Scale(scaleFact2)

	stackbkgHT = THStack("stackbkgHT","")#"CMS Preliminary, 5 fb^{-1} at #sqrt{s} = 13 TeV;H_{T} (GeV)")
	try: stackbkgHT.Add(hTOP)
	except: pass
	try: stackbkgHT.Add(hEWK)
	except: pass
	try: 
		if hQCD.Integral()/bkgHT.Integral()>.005: stackbkgHT.Add(hQCD) #don't plot QCD if it is less than 0.5%
	except: pass
	try: stackbkgHT.Add(hDDBKG)
	except: pass

	topColor = kAzure-6
	ewkColor = kMagenta-2
	qcdColor = kOrange+5
	sig1Color= kBlack
	sig2Color= kGreen
	if 'T53' in sig1: 
		topColor = kRed-9
		ewkColor = kBlue-7
		qcdColor = kOrange-5
		sig1Color= kBlack
		sig2Color= kBlack

	hTOP.SetLineColor(topColor)
	hTOP.SetFillColor(topColor)
	hTOP.SetLineWidth(2)
	try: 
		hEWK.SetLineColor(ewkColor)
		hEWK.SetFillColor(ewkColor)
		hEWK.SetLineWidth(2)
	except: pass
	try:
		hQCD.SetLineColor(qcdColor)
		hQCD.SetFillColor(qcdColor)
		hQCD.SetLineWidth(2)
	except: pass
	try:
		hDDBKG.SetLineColor(15)
		hDDBKG.SetFillColor(15)
		hDDBKG.SetLineWidth(2)
	except: pass
	hsig1.SetLineColor(sig1Color)
	hsig1.SetFillStyle(0)
	hsig1.SetLineWidth(3)
	hsig2.SetLineColor(sig2Color)
	hsig2.SetLineStyle(5)
	hsig2.SetFillStyle(0)
	hsig2.SetLineWidth(3)
	
	hData.SetMarkerStyle(20)
	hData.SetMarkerSize(1.2)
	hData.SetLineWidth(2)

	bkgHTgerr.SetFillStyle(3004)
	bkgHTgerr.SetFillColor(kBlack)

	gStyle.SetOptStat(0)
	c1 = TCanvas("c1","c1",1200,1000)
	gStyle.SetErrorX(0.5)
	yDiv=0.35
	if blind == True: yDiv=0.1
	uMargin = 0
	if blind == True: uMargin = 0.15
	rMargin=.04
	uPad=TPad("uPad","",0,yDiv,1,1) #for actual plots
	uPad.SetTopMargin(0.10)
	uPad.SetBottomMargin(uMargin)
	uPad.SetRightMargin(rMargin)
	uPad.SetLeftMargin(.12)
	uPad.Draw()
	if blind == False:
		lPad=TPad("lPad","",0,0,1,yDiv) #for sigma runner
		lPad.SetTopMargin(0)
		lPad.SetBottomMargin(.4)
		lPad.SetRightMargin(rMargin)
		lPad.SetLeftMargin(.12)
		lPad.SetGridy()
		lPad.Draw()
	if not doNormByBinWidth: hData.SetMaximum(1.2*max(hData.GetMaximum(),bkgHT.GetMaximum()))
	hData.SetMinimum(0.015)
	hData.SetTitle("")
	if doNormByBinWidth: hData.GetYaxis().SetTitle("Events / 1 GeV")
	else: hData.GetYaxis().SetTitle("Events")
	formatUpperHist(hData)
	uPad.cd()
	hData.SetTitle("")
	if not blind: hData.Draw("E1 X0")
	if blind: 
		hsig1.SetMinimum(0.015)
		if doNormByBinWidth: hsig1.GetYaxis().SetTitle("Events / 1 GeV")
		else: hsig1.GetYaxis().SetTitle("Events")
		formatUpperHist(hsig1)
		hsig1.SetMaximum(hData.GetMaximum()*2)
		hsig1.Draw("HIST")
	stackbkgHT.Draw("SAME HIST")
	hsig1.Draw("SAME HIST")
	hsig2.Draw("SAME HIST")
	if not blind: hData.Draw("SAME E1 X0") #redraw data so its not hidden
	uPad.RedrawAxis()
	bkgHTgerr.Draw("SAME E2")
	
	#add x labels - start
	hsig1.GetXaxis().SetLabelOffset(99)
	y = gPad.GetUymin() - 0.2*hsig1.GetYaxis().GetBinWidth(1)
	t = TText()
	t.SetTextAngle(60)
	t.SetTextSize(0.04)
	t.SetTextAlign(33)
	xEEE = hsig1.GetXaxis().GetBinCenter(1);
	xEEM = hsig1.GetXaxis().GetBinCenter(2);
	xEMM = hsig1.GetXaxis().GetBinCenter(3);
	xMMM = hsig1.GetXaxis().GetBinCenter(4);
	t.DrawText(xEEE,y,"EEE"); 	
	t.DrawText(xEEM,y,"EEM"); 	
	t.DrawText(xEMM,y,"EMM"); 	
	t.DrawText(xMMM,y,"MMM"); 	
	#add x labels - end
		
	chLatex = TLatex()
	chLatex.SetNDC()
	chLatex.SetTextSize(0.06)
	chLatex.SetTextAlign(11) # align right
	chString = ''
# 	if isEM=='EEE': chString+='eee'
# 	if isEM=='EEM': chString+='ee#mu'
# 	if isEM=='EMM': chString+='e#mu#mu'
# 	if isEM=='MMM': chString+='#mu#mu#mu'
	chLatex.DrawLatex(0.16, 0.82, chString)

	leg = TLegend(0.65,0.53,0.95,0.90)
	leg.SetShadowColor(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetLineColor(0)
	leg.SetLineStyle(0)
	leg.SetBorderSize(0) 
	leg.SetTextFont(42)
	if not blind: leg.AddEntry(hData,"DATA")
	scaleFact1Str = ' x'+str(scaleFact1)
	scaleFact2Str = ' x'+str(scaleFact2)
	if not scaleSignals:
		scaleFact1Str = ''
		scaleFact2Str = ''
	leg.AddEntry(hsig1,sig1leg+scaleFact1Str,"l")
	leg.AddEntry(hsig2,sig2leg+scaleFact2Str,"l")
	try: 
		if hQCD.Integral()/bkgHT.Integral()>.005: leg.AddEntry(hQCD,"QCD","f") #don't plot QCD if it is less than 0.5%
	except: pass
	try: leg.AddEntry(hEWK,"VV+VVV","f")
	except: pass
	try: leg.AddEntry(hTOP,"TTV","f")
	except: pass
	try: leg.AddEntry(hDDBKG,"DD BKG","f")
	except: pass
	leg.AddEntry(bkgHTgerr,"Bkg uncert. (stat. #oplus syst.)","f")
	leg.Draw("same")

	prelimTex=TLatex()
	prelimTex.SetNDC()
	prelimTex.SetTextAlign(31) # align right
	prelimTex.SetTextFont(42)
	prelimTex.SetTextSize(0.07)
	prelimTex.SetLineWidth(2)
	prelimTex.DrawLatex(0.95,0.92,str(lumi)+" fb^{-1} (13 TeV)")

	prelimTex2=TLatex()
	prelimTex2.SetNDC()
	prelimTex2.SetTextFont(61)
	prelimTex2.SetLineWidth(2)
	prelimTex2.SetTextSize(0.10)
	prelimTex2.DrawLatex(0.12,0.92,"CMS")

	prelimTex3=TLatex()
	prelimTex3.SetNDC()
	prelimTex3.SetTextAlign(13)
	prelimTex3.SetTextFont(52)
	prelimTex3.SetTextSize(0.075)
	prelimTex3.SetLineWidth(2)
	if not blind: prelimTex3.DrawLatex(0.24,0.975,"Preliminary")
	if blind: prelimTex3.DrawLatex(0.29175,0.975,"Preliminary")
	#if blind: prelimTex3.DrawLatex(0.29175,0.9364,"Preliminary")

	if blind == False and not doRealPull:
		lPad.cd()
		pull=hData.Clone("pull")
		pull.Divide(hData, bkgHT)
		for binNo in range(0,hData.GetNbinsX()+2):
			if bkgHT.GetBinContent(binNo)!=0:
				pull.SetBinError(binNo,hData.GetBinError(binNo)/bkgHT.GetBinContent(binNo))
		pull.SetMaximum(3)
		pull.SetMinimum(0)
		pull.SetFillColor(1)
		pull.SetLineColor(1)
		formatLowerHist(pull)
		pull.Draw("E1")
		
		BkgOverBkg = pull.Clone("bkgOverbkg")
		BkgOverBkg.Divide(bkgHT, bkgHT)
		pullUncBandTot=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncTot"))
		for binNo in range(0,hData.GetNbinsX()+2):
			if bkgHT.GetBinContent(binNo)!=0:
				pullUncBandTot.SetPointEYhigh(binNo-1,totBkgTemp3[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
				pullUncBandTot.SetPointEYlow(binNo-1,totBkgTemp3[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
		if not doOneBand: pullUncBandTot.SetFillStyle(3001)
		else: pullUncBandTot.SetFillStyle(3344)
		pullUncBandTot.SetFillColor(1)
		pullUncBandTot.SetLineColor(1)
		pullUncBandTot.SetMarkerSize(0)
		gStyle.SetHatchesLineWidth(1)
		pullUncBandTot.Draw("SAME E2")
		
		pullUncBandNorm=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncNorm"))
		for binNo in range(0,hData.GetNbinsX()+2):
			if bkgHT.GetBinContent(binNo)!=0:
				pullUncBandNorm.SetPointEYhigh(binNo-1,totBkgTemp2[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
				pullUncBandNorm.SetPointEYlow(binNo-1,totBkgTemp2[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
		pullUncBandNorm.SetFillStyle(3001)
		pullUncBandNorm.SetFillColor(2)
		pullUncBandNorm.SetLineColor(2)
		pullUncBandNorm.SetMarkerSize(0)
		gStyle.SetHatchesLineWidth(1)
		if not doOneBand: pullUncBandNorm.Draw("SAME E2")
		
		pullUncBandStat=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncStat"))
		for binNo in range(0,hData.GetNbinsX()+2):
			if bkgHT.GetBinContent(binNo)!=0:
				pullUncBandStat.SetPointEYhigh(binNo-1,totBkgTemp1[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
				pullUncBandStat.SetPointEYlow(binNo-1,totBkgTemp1[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
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
		if not doOneBand: pullLegend.AddEntry(pullUncBandStat , "Bkg uncert. (shape syst.)" , "f")
		if not doOneBand: pullLegend.AddEntry(pullUncBandNorm , "Bkg uncert. (shape #oplus norm. syst.)" , "f")
		if not doOneBand: pullLegend.AddEntry(pullUncBandTot , "Bkg uncert. (stat. #oplus all syst.)" , "f")
		else: pullLegend.AddEntry(pullUncBandTot , "Bkg uncert. (stat. #oplus syst.)" , "f")
		#pullLegend.AddEntry(pullQ2up , "Q^{2} Up" , "l")
		#pullLegend.AddEntry(pullQ2dn , "Q^{2} Down" , "l")
		pullLegend.Draw("SAME")
		pull.Draw("SAME")
		lPad.RedrawAxis()

	if blind == False and doRealPull:
		lPad.cd()
		pull=hData.Clone("pull")
		for binNo in range(0,hData.GetNbinsX()+2):
			if hData.GetBinContent(binNo)!=0:
				MCerror = 0.5*(totBkgTemp3[catStr].GetErrorYhigh(binNo-1)+totBkgTemp3[catStr].GetErrorYlow(binNo-1))
				pull.SetBinContent(binNo,(hData.GetBinContent(binNo)-bkgHT.GetBinContent(binNo))/math.sqrt(MCerror**2+hData.GetBinError(binNo)**2))
				#pull.SetBinContent(binNo,(hData.GetBinContent(binNo)-bkgHT.GetBinContent(binNo))/math.sqrt(bkgHT.GetBinError(binNo)**2+hData.GetBinError(binNo)**2))
			else: pull.SetBinContent(binNo,0.)
		pull.SetMaximum(3)
		pull.SetMinimum(-3)
		pull.SetFillColor(2)
		pull.SetLineColor(2)
		formatLowerHist(pull)
		pull.GetYaxis().SetTitle('Pull')
		pull.Draw("HIST")

	#c1.Write()
	savePrefix = templateDir+'/'+'plots/'
	print 'Saving files at:', savePrefix
	if not os.path.exists(savePrefix): os.system('mkdir -v '+savePrefix)
	savePrefix+=histPrefix+isRebinned+saveKey
	print 'savePrefix :', savePrefix
	if doRealPull: savePrefix+='_pull'
	if yLog: savePrefix+='_logy'

	if doOneBand:
		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+"_totBand.pdf")
		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+"_totBand.png")
# 		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+"_totBand.root")
# 		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+"_totBand.C")
	else:
		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+".pdf")
		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+".png")
# 		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+".root")
# 		c1.SaveAs(savePrefix+"_"+cutString+'_'+discriminant+BRconfStr+".C")
	try: del hTOP
	except: pass
	try: del hEWK
	except: pass
	try: del hQCD
	except: pass
			
RFile1.Close()
RFile2.Close()

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))


