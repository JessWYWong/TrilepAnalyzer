#!/usr/bin/python

import os,sys,time,math,pickle,itertools
from ROOT import *
from weights import *

gROOT.SetBatch(1)
start_time = time.time()

lumi=12.9 #for plots
lumiInTemplates=str(targetlumi/1000).replace('.','p') # 1/fb

discriminant = 'ST'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST0_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST600_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST700_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST800_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST900_mllOS20'
cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1000_mllOS20'
# cutString = 'lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1100_mllOS20'
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

# systematicList = ['pileup','jec','jer','jmr','jms','btag','tau21','muR','muF','muRFcorrd','toppt','jsf','PR','FR']
systematicList = ['pileup','jec','jer','btag','pdfNew','muRFcorrdNew','PR','FR']

doAllSys = True

isRebinned=''#'_rebinned'#post fix for file names if the name changed b/c of rebinning or some other process
doNormByBinWidth=False # not tested, may not work out of the box
doOneBand = False
if not doAllSys: doOneBand = True # Don't change this!
blind = False
yLog  = False
doRealPull = False
if doRealPull: doOneBand=False

# templateDir=os.getcwd()+'/templates_ST2016_4_22_15_29_7/'+cutString+'/'
# templateDir='/user_data/rsyarif/optimization_80x_withJECJER_condor_2016_11_30/'+cutString+'/'
templateDir='/user_data/rsyarif/optimization_80x_withJECJER_condor_FRv7_PRv2_2016_12_14/'+cutString+'/'

tempsig='templates_'+discriminant+'_'+sig1+'_'+lumiInTemplates+'fb'+isRebinned+'.root'	

isEMlist =['EEE','EEM','EMM','MMM']
nttaglist=['0p']
nWtaglist=['0p']
nbtaglist=['0p']
catList = list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist))
tagList = list(itertools.product(nttaglist,nWtaglist,nbtaglist))

lumiSys = 0.062 #6.2% https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM - 20Sep2016 - ATTENTION!! NEEDS to be checked again!
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
lepIdSys = math.sqrt(3.*0.01**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty
corrdSys = math.sqrt(lumiSys**2+trigSys**2+lepIdSys**2+lepIsoSys**2)

def getNormUnc(hist,ibin):
	contentsquared = hist.GetBinContent(ibin)**2
	error = corrdSys*corrdSys*contentsquared  #correlated uncertainties
	if 'top' in hist.GetName(): error += topXsecSys*topXsecSys*contentsquared # cross section
	if 'ewk' in hist.GetName(): error += ewkXsecSys*ewkXsecSys*contentsquared # cross section
	if 'qcd' in hist.GetName(): error += qcdXsecSys*qcdXsecSys*contentsquared # cross section
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

RFile1 = TFile(templateDir+tempsig.replace(sig1,sig1))
RFile2 = TFile(templateDir+tempsig.replace(sig1,sig2))
systHists = {}
totBkgTemp1 = {}
totBkgTemp2 = {}
totBkgTemp3 = {}
for cat in catList:
	histPrefix='triLep'
# 	histPrefix=discriminant+'_'+lumiInTemplates+'fb_'
	tagStr='nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]
	catStr='is'+cat[0]+'_'+tagStr
	isEM=cat[0]
# 	histPrefix+=catStr
	print histPrefix
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
	
	totBkgTemp1[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
	totBkgTemp2[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
	totBkgTemp3[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))
	
	for ibin in range(1,hTOP.GetNbinsX()+1):
		errorUp = 0.
		errorDn = 0.
		errorStatOnly = bkgHT.GetBinError(ibin)**2
		errorNorm = getNormUnc(hTOP,ibin)
		try: errorNorm += getNormUnc(hEWK,ibin)
		except: pass
		try: errorNorm += getNormUnc(hQCD,ibin)
		except: pass

		if doAllSys:
			for sys in systematicList:
				if sys=='PR' or sys=='FR': continue	
				errorPlus = systHists['top'+catStr+sys+'plus'].GetBinContent(ibin)-hTOP.GetBinContent(ibin)
				errorMinus = hTOP.GetBinContent(ibin)-systHists['top'+catStr+sys+'minus'].GetBinContent(ibin)
				if errorPlus > 0: errorUp += errorPlus**2
				else: errorDn += errorPlus**2
				if errorMinus > 0: errorDn += errorMinus**2
				else: errorUp += errorMinus**2
				if sys!='toppt':
					try:
						errorPlus = systHists['ewk'+catStr+sys+'plus'].GetBinContent(ibin)-hEWK.GetBinContent(ibin)
						errorMinus = hEWK.GetBinContent(ibin)-systHists['ewk'+catStr+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
					except: pass
					try:
						errorPlus = systHists['qcd'+catStr+sys+'plus'].GetBinContent(ibin)-hQCD.GetBinContent(ibin)
						errorMinus = hQCD.GetBinContent(ibin)-systHists['qcd'+catStr+sys+'minus'].GetBinContent(ibin)
						if errorPlus > 0: errorUp += errorPlus**2
						else: errorDn += errorPlus**2
						if errorMinus > 0: errorDn += errorMinus**2
						else: errorUp += errorMinus**2
					except: pass													

		totBkgTemp1[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp))
		totBkgTemp1[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn))
		totBkgTemp2[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
		totBkgTemp2[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm))
		totBkgTemp3[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatOnly))
		totBkgTemp3[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm+errorStatOnly))
	
	bkgHTgerr = totBkgTemp3[catStr].Clone()

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
	try: leg.AddEntry(hEWK,"EWK","f")
	except: pass
	try: leg.AddEntry(hTOP,"TOP","f")
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
# 	savePrefix = templateDir.replace(cutString,'')+templateDir.split('/')[-2]+cutString+'/'+'plots/'
	savePrefix = templateDir.replace(cutString,'')+templateDir.split('/')[-2]+'/'+'plots/'
	if not os.path.exists(savePrefix): os.system('mkdir '+savePrefix)
	savePrefix+=histPrefix+isRebinned+saveKey
	if doRealPull: savePrefix+='_pull'
	if yLog: savePrefix+='_logy'

	if doOneBand:
		c1.SaveAs(savePrefix+"totBand.pdf")
		c1.SaveAs(savePrefix+"totBand.png")
		c1.SaveAs(savePrefix+"totBand.root")
		c1.SaveAs(savePrefix+"totBand.C")
	else:
		c1.SaveAs(savePrefix+".pdf")
		c1.SaveAs(savePrefix+".png")
		c1.SaveAs(savePrefix+".root")
		c1.SaveAs(savePrefix+".C")
	try: del hTOP
	except: pass
	try: del hEWK
	except: pass
	try: del hQCD
	except: pass
			
RFile1.Close()
RFile2.Close()

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))


