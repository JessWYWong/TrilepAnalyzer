#!/usr/bin/python

import os,sys,time,math,pickle
from ROOT import *
from weights import *
from cutList import *
from samples import *
from array import array

gROOT.SetBatch(1)
start_time = time.time()

# pfix='kinematics_80x_MultiLep_ddbkgscan_step2_exactly2Jets_2DFRscan_2016_12_8'+'/'+cutString
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_2017_1_23/'
# pfix='kinematics_condor_ddbkgscan_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_ttbarClosure_2017_3_9'
# pfix='LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_2017_3_16'
# pfix='kinematics_condor_ddbkgscan_zjetsClosure_2017_3_15'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_fixedBug_2017_4_30'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_fixedBug_2017_5_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_2017_5_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_SR_2017_5_12'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_CR2_2017_5_13'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35_2017_6_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv36_2017_6_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_2017_6_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv37_2017_6_2'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv36_2017_6_2' #has more plots
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35_2017_6_2' #has more plots
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_2017_6_1' #Elpt MuPt
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv38_2017_6_5'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35a_2017_6_5' #--> double checking but also with muFR=.14instead of .13 in FRv35

# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SR_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_CR2_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400low_2017_9_18'
pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_2017_9_20'
if(len(sys.argv)>1):
  pfix = sys.argv[1]


doDDBKGscan=True

# muFRtoPlot = 12
# elFRtoPlot = 18

# muFRtoPlot = 14
# elFRtoPlot = 21

# #SR ttbar
# muFRtoPlot = 12	
# elFRtoPlot = 24

#CR2 ttbar
# muFRtoPlot = 12	
# elFRtoPlot = 18

# muFRtoPlot = 12
# elFRtoPlot = 24


# muFRtoPlot = 28
# elFRtoPlot = 35

# muFRtoPlot = 40
# elFRtoPlot = 98

########### elMVAvalueFix #########

#SR ttbar
# muFRtoPlot = 11	
# elFRtoPlot = 17

#CR2 ttbar
muFRtoPlot = 14	
elFRtoPlot = 8

#SRHT400 ttbar
# muFRtoPlot = 12	
# elFRtoPlot = 26

#SRHT400low ttbar
# muFRtoPlot = 11	
# elFRtoPlot = 14

#All region ttbar
#muFRtoPlot = 9
#elFRtoPlot = 21

###################################


if(doDDBKGscan):print ''
if(doDDBKGscan):print ' -- plotting: muFR = ', muFRtoPlot, ', elFR = ', elFRtoPlot, '--'
if(doDDBKGscan):print ''


#if len(sys.argv)>2:
#	muFRtoPlot=int(sys.argv[1])
#	elFRtoPlot=int(sys.argv[2])
# 
# print 'sys.argv:', sys.argv
# print 'muFRtoPlot:', str(muFRtoPlot)
# print 'elFRtoPlot:', str(elFRtoPlot)
# 
muFRindex = muFRtoPlot
elFRindex = elFRtoPlot

#outDir = '/user_data/rsyarif/'
outDir = '/mnt/data/users/wwong/'
templateDir=outDir+pfix+'/'

#lumi=35.9 #for plots
lumi=41.6
lumiInTemplates='41p557'
#lumiInTemplates='35p867'

sig='ttm1000' # choose the 1st signal to plot
sigleg='TT(1 TeV)'
scaleSignals = True

scaleFact1 = 300
if 'Final' in templateDir: scaleFact1 = 40

# systematicList = ['pileup','jec','jer','jsf','jmr','jms','btag','tau21','pdfNew','muRFcorrdNew','toppt','PR','FR']
# systematicList = ['pileup','jec','jer','jsf','btag','pdfNew','muRFcorrdNew','PR','FR']

# systematicList = ['pileup','jec','jer','btag','pdfNew','muRFcorrdNew','PR','FR'] # no jsf

# systematicList = ['PR','FR']

systematicList = ['pileup','btag','pdfNew','muRFcorrdNew','PR','FR']


doAllSys = False

isRebinned=''#post fix for file names if the name changed b/c of rebinning or some other process
doNormByBinWidth=False # not tested, may not work out of the box
doOneBand = False
if not doAllSys: doOneBand = True # Don't change this!
blind = False
yLog = True

doRealPull = False
if doRealPull: doOneBand=False

totBkgTemp1 = {}
totBkgTemp2 = {}
totBkgTemp3 = {}

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

	if 'JetPt' in histogram.GetName() or 'JetEta' in histogram.GetName() or 'JetPhi' in histogram.GetName() or 'Pruned' in histogram.GetName() or 'Tau' in histogram.GetName(): histogram.GetYaxis().SetTitle("Jets")
	histogram.GetYaxis().CenterTitle()
	histogram.SetMinimum(0.0001)
# 	histogram.SetMinimum(0.001)
	if not yLog: 
		histogram.SetMinimum(0.25)
	if yLog:
		uPad.SetLogy()
		histogram.SetMinimum(0.1)
		if not doNormByBinWidth: histogram.SetMaximum(100*histogram.GetMaximum())
		
def formatLowerHist(histogram):
	histogram.GetXaxis().SetLabelSize(.12)
	histogram.GetXaxis().SetTitleSize(0.15)
	histogram.GetXaxis().SetTitleOffset(0.95)
	histogram.GetXaxis().SetNdivisions(506)
# 	histogram.GetXaxis().SetTitle("Leptons p_{T} (GeV)")

	histogram.GetYaxis().SetLabelSize(0.12)
	histogram.GetYaxis().SetTitleSize(0.14)
	histogram.GetYaxis().SetTitleOffset(.37)
	histogram.GetYaxis().SetTitle('Data/Bkg')
	histogram.GetYaxis().SetNdivisions(5)
	if doRealPull: histogram.GetYaxis().SetRangeUser(min(-2.99,0.8*histogram.GetBinContent(histogram.GetMaximumBin())),max(2.99,1.2*histogram.GetBinContent(histogram.GetMaximumBin())))
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


### only if doAllSys ###
lumiSys = 0.026 #6.2% https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM - 20Sep2016
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

plotList = [#distribution name as defined in "doHists.py"
# 	'NPV',
	'lepPt',
# 	'ElPt',
# 	'MuPt',
# 	'lep1Pt',
# 	'lep2Pt',
# 	'lep3Pt',
# 	'lepEta',
# 	'ElEta',
# 	'MuEta',
# 	'lep1Eta',
# 	'lep2Eta',
# 	'lep3Eta',
# 	'JetEta',
# 	'Jet1Eta',
# 	'Jet2Eta',
# 	'JetPt' ,
# 	'Jet1Pt' ,
# 	'Jet2Pt' ,
# 	'HT',
# 	'ST',
# 	'MET',
# 	'HTrebinned',
# 	'STrebinned',
# 	'METrebinned',
# 
# 	'NJets' ,
# 	'NBJets',
	#'NBJetsCorr',
# 	'mindeltaRlepJets',
# 	'mindeltaRlep1Jets',
# 	'mindeltaRlep2Jets',
# 	'mindeltaRlep3Jets',

# 	'mindeltaR',
# 	'mindeltaRB',
# 
# 	'mindeltaR1',
# 	'mindeltaR2',
# 	'mindeltaR3',
# 	'PtRel1',
# 	'PtRel2',
# 	'PtRel3',
# 	'lepCharge',
# 	'lepIso',
# 	'ElIso',
# 	'MuIso',
# 	'MllsameFlavorOS',
# 	'MllOSall',
# 	'MllOSallmin',
# 	'Mlll'
	]

# lepPtbins = [0,10,30,40,60,80,100,120,140,160,180,220,260,300,400,500]
lepPtbins = [0,10,30,40,60,80,100,120,140,160,180,220,300,400,500]
rebinLepPt = False
checkUncBand = True

fit  = False
fit2 = False
fit3 = False
fit4 = False
catList=['EEE','EEM','EMM','MMM','All']
for discriminant in plotList:	
	fileTemp='templates_'+discriminant+'_'+lumiInTemplates+'fb'+isRebinned+'.root'
	print templateDir+'/'+fileTemp
	if not os.path.exists(templateDir+'/'+fileTemp): 
		print 'not found, skipping'
		continue
	RFile = TFile(templateDir+'/'+fileTemp)

	systHists={}

# 	for muFRindex in xrange(loop):
	for cat in catList:
		histPrefix=discriminant+'_'+lumiInTemplates+'fb_'+cat
	
# 		try: hTOP = RFile.Get(histPrefix+'__top').Clone()
# 		except: 
# 			print "There is no TOP!!!!!!!!"
# 			print "Skipping TOP....."
# 			pass
# 		try: hEWK = RFile.Get(histPrefix+'__ewk').Clone()
# 		except: 
# 			print "There is no EWK!!!!!!!!"
# 			print "Skipping EWK....."
# 			pass
# 		try: hQCD = RFile.Get(histPrefix+'__qcd').Clone()
# 		except: 
# 			print "There is no QCD!!!!!!!!"
# 			print "Skipping QCD....."
# 			pass
		try: 
			hDDBKG = RFile.Get(histPrefix+'_ddbkg').Clone()
			if(doDDBKGscan): hDDBKG = RFile.Get(histPrefix+'_ddbkgMuFR'+str(muFRindex)+'_ElFR'+str(elFRindex)).Clone()
			if(rebinLepPt): 
				hTemp = RFile.Get(histPrefix+'_ddbkg').Clone()
				#for bin in xrange(hDDBKG.GetSize()): print 'DDBKG bin',bin,' : ',hDDBKG.GetBinContent(bin)
				hDDBKG = TH1D(hDDBKG.GetName(),hDDBKG.GetTitle(),len(lepPtbins)-1,array('d',lepPtbins))
				for bin in xrange(hTemp.GetSize()): 
					if (bin<11): hDDBKG.SetBinContent(bin,hTemp.GetBinContent(bin))
					elif (bin==11):
						content = 0.
						for bin in [11,12]: content += hTemp.GetBinContent(bin)
						hDDBKG.SetBinContent(11,content)
					elif (bin==13):
						content = 0.
						for bin in [13,14,15,16]: content += hTemp.GetBinContent(bin)
						hDDBKG.SetBinContent(12,content)
# 					elif (bin==15):
# 						content = 0.
# 						for bin in [15,16]: content += hTemp.GetBinContent(bin)
# 						hDDBKG.SetBinContent(13,content)
					elif (bin==17):
						content = 0.
						for bin in [17,18]: content += hTemp.GetBinContent(bin)
						hDDBKG.SetBinContent(13,content)
					elif (bin==19):
						content = 0.
						for bin in [19,20]: content += hTemp.GetBinContent(bin)
						hDDBKG.SetBinContent(14,content)
					elif (bin==21): hDDBKG.SetBinContent(16,hTemp.GetBinContent(bin))
				#for bin in xrange(hDDBKG.GetSize()): print 'bin',bin,' : ',hDDBKG.GetBinContent(bin)
		except: 
			if(doDDBKGscan):
				print "There is no DDBKG MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+"!!!!!!!!"
				print "Skipping DDBKG MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+"....."
			else:
				print "There is no DDBKG !!!!!!!!"
				print "Skipping DDBKG....."
			print "Skipping to draw for", cat
			continue
				
		try: print discriminant,cat, "TOP", hTOP.Integral()
		except: pass
		try: print discriminant,cat, "EWK", hEWK.Integral()
		except: pass
		try: print discriminant,cat, "QCD", hQCD.Integral()
		except: pass
		try: 
			if(doDDBKGscan):
				print discriminant,cat, "DDBKG MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+"", hDDBKG.Integral()
			else:
				print discriminant,cat, "DDBKG"+"", hDDBKG.Integral()
		except: pass
	
		hData = RFile.Get(histPrefix+'__DATA').Clone()
		if(rebinLepPt): 
			hTemp = RFile.Get(histPrefix+'__DATA').Clone()
			#for bin in xrange(hData.GetSize()): print 'DATA bin',bin,' : ',hData.GetBinContent(bin)
			hData = TH1D(hData.GetName(),hData.GetTitle(),len(lepPtbins)-1,array('d',lepPtbins))
			for bin in xrange(hTemp.GetSize()): 
				if (bin<11): hData.SetBinContent(bin,hTemp.GetBinContent(bin))
				elif (bin==11):
					content = 0.
					for bin in [11,12]: content += hTemp.GetBinContent(bin)
					hData.SetBinContent(11,content)
				elif (bin==13):
					content = 0.
					for bin in [13,14,15,16]: content += hTemp.GetBinContent(bin)
					hData.SetBinContent(12,content)
				elif (bin==17):
					content = 0.
					for bin in [17,18]: content += hTemp.GetBinContent(bin)
					hData.SetBinContent(13,content)
				elif (bin==19):
					content = 0.
					for bin in [19,20]: content += hTemp.GetBinContent(bin)
					hData.SetBinContent(14,content)
				elif (bin==21): hData.SetBinContent(16,hTemp.GetBinContent(bin))
			#for bin in xrange(hData.GetSize()): print 'DATA rebin',bin,' : ',hData.GetBinContent(bin)
# 		hsig1 = RFile.Get(histPrefix+'__'+sig+'bwbw').Clone()
# 		hsig2 = RFile.Get(histPrefix+'__'+sig+'tztz').Clone()
# 		hsig3 = RFile.Get(histPrefix+'__'+sig+'thth').Clone()

# 		hsig = RFile.Get(histPrefix+'__'+sig+'bwbw').Clone(histPrefix+'__'+sig+'nominal')
# 		decays = ['tztz','thth','tzbw','thbw','tzth']
# 		for decay in decays:
# 			htemp = RFile.Get(histPrefix+'__'+sig+decay).Clone()
# 			hsig.Add(htemp)

		# original scale = lumi * xsec * BR(50/25/25) / N(33/33/33)
# 		hsig1.Scale(1.0/BR['TTBWBW'])
# 		hsig2.Scale(1.0/BR['TTTZTZ'])
# 		hsig3.Scale(1.0/BR['TTTHTH'])
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
					try: systHists['top'+sys+ud] = RFile.Get(histPrefix+'__top__'+sys+'__'+ud).Clone()
					except: 
						print "Skipping",sys,"for TOP"
						pass
					try: systHists['ewk'+sys+ud] = RFile.Get(histPrefix+'__ewk__'+sys+'__'+ud).Clone()
					except: 
						print "Skipping",sys,"for EWK"
						pass
					try: systHists['qcd'+sys+ud] = RFile.Get(histPrefix+'__qcd__'+sys+'__'+ud).Clone()
					except: 
						print "Skipping",sys,"for QCD"
						pass
					try: systHists['ddbkg'+sys+ud] = RFile.Get(histPrefix+'__ddbkg__'+sys+'__'+ud).Clone()
					except: 
						if(doDDBKGscan):print "Skipping",sys,"for DDBKG MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)
						else: print "Skipping",sys,"for DDBKG"
						pass

		try: hTOPstatOnly = hTOP.Clone(hTOP.GetName()+'statOnly')
		except: pass
		try: hEWKstatOnly= hEWK.Clone(hEWK.GetName()+'statOnly')
		except: pass
		try: hQCDstatOnly = hQCD.Clone(hQCD.GetName()+'statOnly')
		except: pass
		try: hDDBKGstatOnly = hDDBKG.Clone(hDDBKG.GetName()+'statOnly')
		except: pass

# 		try: bkgHT = hTOP.Clone()
# 		except: pass
# 		try: bkgHT.Add(hEWK)
# 		except: pass
# 		try: bkgHT.Add(hQCD)
# 		except: pass
		try: bkgHT = hDDBKG.Clone()
		except: pass

		try:
			totBkgTemp1[cat] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
			totBkgTemp2[cat] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
			totBkgTemp3[cat] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))
		except: pass
		
		try:
			BINS_temp = hData.GetNbinsX()
		except:
			BINS_temp = 0
					
		if(checkUncBand):print "Setting uncertainties:"
		errorNorm = 0.
		for ibin in range(1,BINS_temp+1):
			errorUp = 0.
			errorDn = 0.
			errorSym = 0.

			try: 
				errorStatOnly = bkgHT.GetBinError(ibin)**2
				if(checkUncBand):print "Bin",ibin,"errorStatOnly : ",errorStatOnly 
			except:
				if(checkUncBand):print "Bin",ibin,"Skipping errorStatOnly!!" 
				pass
				continue
			try: errorNorm = getNormUnc(hTOPstatOnly,ibin)
			except: pass
			try: errorNorm += getNormUnc(hEWKstatOnly,ibin)
			except: pass
			try: errorNorm += getNormUnc(hQCDstatOnly,ibin)
			except: pass

			if doAllSys:
				for sys in systematicList:
					if not (sys=='PR' or sys=='FR'):
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
					if sys=='PR' or sys=='FR':
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
						
			totBkgTemp1[cat].SetPointEYhigh(ibin-1,math.sqrt(errorUp))
			totBkgTemp1[cat].SetPointEYlow(ibin-1,math.sqrt(errorDn))
			totBkgTemp2[cat].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
			totBkgTemp2[cat].SetPointEYlow(ibin-1,math.sqrt(errorDn+errorNorm))
			totBkgTemp3[cat].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatOnly))
			totBkgTemp3[cat].SetPointEYlow(ibin-1,math.sqrt(errorDn+errorNorm+errorStatOnly))
		
		try:bkgHTgerr = totBkgTemp3[cat].Clone()
		except:pass

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
# 		hsig1.Scale(scaleFact1)
# 		hsig2.Scale(scaleFact1)
# 		hsig3.Scale(scaleFact1)
# 		hsig.Scale(scaleFact1)
	
		stackbkgHT = THStack("stackbkgHT","")
# 		try: stackbkgHT.Add(hTOP)
# 		except: pass
# 		try: stackbkgHT.Add(hEWK)
# 		except: pass
# 		try: 
# 			if hQCD.Integral()/bkgHT.Integral()>.005: stackbkgHT.Add(hQCD) #don't plot QCD if it is less than 0.5%
# 		except: pass
		try: stackbkgHT.Add(hDDBKG)
		except: pass

		try:
			hTOP.SetLineColor(kAzure-6)
			hTOP.SetFillColor(kAzure-6)
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
	
# 		hsig.SetLineColor(kBlack)
# 		hsig.SetLineWidth(3)
# 		hsig1.SetLineColor(kRed)
# 		hsig1.SetLineStyle(2)
# 		hsig1.SetLineWidth(3)
# 		hsig2.SetLineColor(kOrange-2)
# 		hsig2.SetLineStyle(5)
# 		hsig2.SetLineWidth(3)
# 		hsig3.SetLineColor(kGreen+1)
# 		hsig3.SetLineStyle(7)
# 		hsig3.SetLineWidth(3)
	
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
		try: 
			if not doNormByBinWidth: hData.SetMaximum(1.2*max(hData.GetMaximum(),bkgHT.GetMaximum()))
		except: 
			pass
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
			hsig1.SetMaximum(hData.GetMaximum())
			hsig1.Draw("HIST")

		stackbkgHT.Draw("SAME HIST")
# 		hsig.Draw("SAME HIST")
# 		hsig1.Draw("SAME HIST")
# 		hsig2.Draw("SAME HIST")
# 		hsig3.Draw("SAME HIST")
		if not blind: hData.Draw("SAME E1 X0") #redraw data so its not hidden
		uPad.RedrawAxis()
		bkgHTgerr.Draw("SAME E2")

		leg = {}
		if 'Tau21' in discriminant:
			leg = TLegend(0.15,0.53,0.45,0.90)
		elif 'Eta' in discriminant or 'deltaRjet2' in discriminant:
			leg = TLegend(0.72,0.43,0.95,0.90)
		else:
			leg = TLegend(0.65,0.53,0.95,0.90)
		leg.SetShadowColor(0)
		leg.SetFillColor(0)
		leg.SetFillStyle(0)
		leg.SetLineColor(0)
		leg.SetLineStyle(0)
		leg.SetBorderSize(0) 
		leg.SetTextFont(42)
# 		if not blind: leg.AddEntry(hData,"ttbar 'DATA' ")
		if not blind: leg.AddEntry(hData,"t#bar{t}  Observed ")
	
		scaleFact1Str = ' x'+str(scaleFact1)
		if not scaleSignals:
			scaleFact1Str = ''
	
# 		leg.AddEntry(hsig,sigleg+' nominal BRs'+scaleFact1Str,"l")
# 		leg.AddEntry(hsig1,sigleg+' #rightarrow bWbW'+scaleFact1Str,"l")
# 		leg.AddEntry(hsig2,sigleg+' #rightarrow tZtZ'+scaleFact1Str,"l")
# 		leg.AddEntry(hsig3,sigleg+' #rightarrow tHtH'+scaleFact1Str,"l")
		try: 
			if hQCD.Integral()/bkgHT.Integral()>.005: leg.AddEntry(hQCD,"QCD","f") #don't plot QCD if it is less than 0.5%
		except: pass
# 		try: leg.AddEntry(hEWK,"EWK","f")
# 		try: leg.AddEntry(hEWK,"VV & VVV","f")
# 		except: pass
# 		try: leg.AddEntry(hTOP,"TOP","f")
# 		try: leg.AddEntry(hTOP,"TTV","f")
# 		except: pass
# 		try: leg.AddEntry(hDDBKG,"tt 'DD BKG' (fr_{#mu}:"+str(muFRtoPlot)+",fr_{el}:"+str(elFRtoPlot)+")","f")
		try: 
			if(doDDBKGscan):leg.AddEntry(hDDBKG,"t#bar{t}  Predicted (FR_{#mu}:"+str(muFRtoPlot)+",FR_{el}:"+str(elFRtoPlot)+")","f")
			else:leg.AddEntry(hDDBKG,"t#bar{t}  Predicted","f")
		except: pass
# 		leg.AddEntry(bkgHTgerr,"Bkg uncert. (stat. #oplus syst.)","f")
		leg.AddEntry(bkgHTgerr,"Bkg uncert. (stat.)","f")
		leg.Draw("same")

		prelimTex=TLatex()
		prelimTex.SetNDC()
		prelimTex.SetTextAlign(31) # align right
		prelimTex.SetTextFont(42)
		prelimTex.SetTextSize(0.07)
		prelimTex.SetLineWidth(2)
# 		prelimTex.DrawLatex(0.95,0.92,str(lumi)+" fb^{-1} (13 TeV)")

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
		if blind: prelimTex3.DrawLatex(0.29175,0.9364,"Preliminary")

		chLatex = TLatex()
		chLatex.SetNDC()
		chLatex.SetTextSize(0.06)
		chLatex.SetTextAlign(11) # align right                                                                                                                                                                                         
		chString = ''
		if cat=='EEE': chString+='eee'
		if cat=='EEM': chString+='ee#mu'
		if cat=='EMM': chString+='e#mu#mu'
		if cat=='MMM': chString+='#mu#mu#mu'
		chLatex.DrawLatex(0.16, 0.82, chString)

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
		
			pull.SetMaximum(3)
			pull.SetMinimum(0)
			pull.SetFillColor(1)
			pull.SetLineColor(1)
			formatLowerHist(pull)
			if fit:
#				pull.Fit("flat","R")
#				fitresult = pull.Fit("line","RS")
#				cov = fitresult.GetCovarianceMatrix()
#				p0p0cov = cov(0,0)
#				p0p1cov = cov(0,1)
#				p1p1cov = cov(1,1)
#				print 'covariance p0-p0 =',p0p0cov
#				print 'covariance p0-p1 =',p0p1cov
#				print 'covariance p1-p1 =',p1p1cov
				'''
				****************************************
				Minimizer is Linear
				Chi2                      =      9.97134
				NDf                       =            9
				p0                        =      1.09771   +/-   0.0384644   
				p1                        = -0.000517529   +/-   9.94895e-05 
				covariance p0-p0 = 0.0014795109823
				covariance p0-p1 = -3.6104869696e-06
				covariance p1-p1 = 9.89815635815e-09
				******************************
				'''				
				jsf = TF1("jsf","1.09771 - 0.000517529*x",200,1500)
				jsfup = TF1("jsfup","1.09771 - 0.000517529*x + sqrt(0.0014795109823 + x*x*9.89815635815e-09 - 2*x*3.6104869696e-06)",200,1500)
				jsfdn = TF1("jsfdn","1.09771 - 0.000517529*x - sqrt(0.0014795109823 + x*x*9.89815635815e-09 - 2*x*3.6104869696e-06)",200,1500)

				print 'JSFup at 250:',jsfup.Eval(250)
			
				jsf.SetLineColor(kRed)
				jsf.SetLineWidth(2)
				jsfup.SetLineColor(kBlue)
				jsfdn.SetLineColor(kBlue)
				jsfup.SetLineWidth(2)
				jsfdn.SetLineWidth(2)
#				pull.Fit("para","R+")
#				pull.Fit("cube","R+")
#				pull.Draw("E1 same")
				pull.Draw("E1 same")
				jsf.Draw("same")
				jsfup.Draw("same")
				jsfdn.Draw("same")
			elif fit2:
				pull.Fit("line2","R")
#				pull.Fit("para2","R+")
#				pull.Fit("cube2","R+")
				pull.Draw("E1 same")
			elif fit3:
				pull.Fit("line3","R")
#				pull.Fit("para3","R+")
#				pull.Fit("cube3","R+")
				pull.Draw("E1 same")
			elif fit4:
				pull.Fit("line4","R")
				pull.Draw("E1 same")
			else:
# 				pull.Draw("E1")
				pull.Draw("E0")

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
				if(checkUncBand):print "CHECKING uncert bands:"
				for binNo in range(0,hData.GetNbinsX()+2):
					if(checkUncBand):print "		Bin: ",binNo," -- ",
					if(checkUncBand):print "	EYhigh: ",round(totBkgTemp3[cat].GetErrorYhigh(binNo-1),2), 
					if(checkUncBand):print "	EYlow : ",round(totBkgTemp3[cat].GetErrorYlow(binNo-1),2), 
					if(checkUncBand):print "	content: ",round(bkgHT.GetBinContent(binNo),2), 
					if bkgHT.GetBinContent(binNo)!=0:
						if(checkUncBand):print "	uncBand: ",round(totBkgTemp3[cat].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo),2)  
						pullUncBandTot.SetPointEYhigh(binNo-1,totBkgTemp3[cat].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandTot.SetPointEYlow(binNo-1,totBkgTemp3[cat].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
					else:
						if(checkUncBand):print "	","not computable" 						
			except: 
				if(checkUncBand):print "		Skipping bin ",binNo, "!!"					
				pass
					
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
						pullUncBandNorm.SetPointEYhigh(binNo-1,totBkgTemp2[cat].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandNorm.SetPointEYlow(binNo-1,totBkgTemp2[cat].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))
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
						pullUncBandStat.SetPointEYhigh(binNo-1,totBkgTemp1[cat].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
						pullUncBandStat.SetPointEYlow(binNo-1,totBkgTemp1[cat].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
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
			pull=hData.Clone("pull")
			for binNo in range(0,hData.GetNbinsX()+2):
				if hData.GetBinContent(binNo)!=0:
					MCerror = 0.5*(totBkgTemp3[cat].GetErrorYhigh(binNo-1)+totBkgTemp3[cat].GetErrorYlow(binNo-1))
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

		savePrefix = templateDir+'/plots/'
		if not os.path.exists(savePrefix): os.system('mkdir '+savePrefix)
		savePrefix+=histPrefix+isRebinned
		if doRealPull: savePrefix+='_pull'
		if yLog: savePrefix+='_logy'

		if doDDBKGscan:
			if doOneBand:
				c1.SaveAs(savePrefix+"_totBand"+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".pdf")
				c1.SaveAs(savePrefix+"_totBand"+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".png")
	# 			c1.SaveAs(savePrefix+"_totBand"+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".root")
	# 			c1.SaveAs(savePrefix+"totBand"+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".C")
			else:
				c1.SaveAs(savePrefix+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".pdf")
				c1.SaveAs(savePrefix+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".png")
	# 			c1.SaveAs(savePrefix+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".root")
	# 			c1.SaveAs(savePrefix+"_ddbkg_MuFR"+str(muFRindex)+"_ElFR"+str(elFRindex)+".C")
		else:
			if doOneBand:
				c1.SaveAs(savePrefix+"_totBand"+"_ddbkg.pdf")
				c1.SaveAs(savePrefix+"_totBand"+"_ddbkg.png")
	# 			c1.SaveAs(savePrefix+"_totBand"+"_ddbkg.root")
	# 			c1.SaveAs(savePrefix+"totBand"+"_ddbkg.C")
			else:
				c1.SaveAs(savePrefix+"_ddbkg.pdf")
				c1.SaveAs(savePrefix+"_ddbkg.png")
	# 			c1.SaveAs(savePrefix+"_ddbkg.root")
	# 			c1.SaveAs(savePrefix+"_ddbkg.C")
			
	RFile.Close()

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))
