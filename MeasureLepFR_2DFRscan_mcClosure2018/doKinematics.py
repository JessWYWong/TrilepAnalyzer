#!/usr/bin/python

import os,sys,time,math,datetime,fnmatch,pickle
from numpy import linspace
from weights import *
from analyze import *
from samples import *
from cutList import *
import ROOT as R

R.gROOT.SetBatch(1)
start_time = time.time()

###########################################################
#################### CUTS & OUTPUT ########################
###########################################################

#obtain cutList and cutString from cutList.py

doAllSys= False
doDDBKGscan=True
printProcess=True
ptScan = False

# muFRtoPrint = 40	
# elFRtoPrint = 98
# 
#All region ttbar
# muFRtoPrint = 14	
# elFRtoPrint = 21
# 
# #SR ttbar
# muFRtoPrint = 12	
# elFRtoPrint = 24

#CR2 ttbar
# muFRtoPrint = 12	
# elFRtoPrint = 18

#CR1 ttbar
# muFRtoPrint = 16	
# elFRtoPrint = 22

# #All region DY
# muFRtoPrint = 7	
# elFRtoPrint = 44

#SR DY
# muFRtoPrint = 5	
# elFRtoPrint = 46

# muFRtoPrint = 13	
# elFRtoPrint = 21

########### elMVAvalueFix #########

#SR ttbar
muFRtoPrint = 13	
elFRtoPrint = 8

#CR2 ttbar
#muFRtoPrint = 8
#elFRtoPrint = 15

#SRHT400 ttbar
# muFRtoPrint = 12	
# elFRtoPrint = 26

#SRHT400low ttbar
# muFRtoPrint = 11	
# elFRtoPrint = 14

#All region ttbar
#muFRtoPrint = 9	
#elFRtoPrint = 21

#CR1 ttbar
# muFRtoPrint = 9	
# elFRtoPrint = 21

###################################



if printProcess and doDDBKGscan: print ''
if printProcess and doDDBKGscan: print ' -- printing: muFR = ', muFRtoPrint, ', elFR = ', elFRtoPrint, '--'
if printProcess and doDDBKGscan: print ''

# pfix='kinematics_condor_ddbkgscan_PRv6_ttbarClosure_2017_3_6'
# pfix='kinematics_condor_ddbkgscan_PRv6_FRv25ttbar_ttbarClosure_2017_3_6'
# pfix='kinematics_condor_ddbkgscan_PRv6_FRv28ttbar_ttbarClosure_2017_3_6'
# pfix='kinematics_condor_ddbkgscan_PRv6_FRv26ttbar_ttbarClosure_2017_3_6'
# pfix='kinematics_condor_ddbkgscan_PRv6_FRv28ttbar_ttbarClosure_saveVeryLoose_2017_3_8'
# pfix='kinematics_condor_ddbkgscan_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_ttbarClosure_2017_3_9'
# pfix='LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds'

dataList = []

#ATTENTION: different lepPt binnings for ttbar and DY!

# pfix='kinematics_condor_ddbkgscan_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_ttbarClosure_2017_3_9/'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_2017_3_16'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_fixedBug_2017_4_30'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_fixedBug_2017_5_1'
# pfix='kinematics_condor_NOddbkgscan_ttbarClosure_fixedBug_2017_5_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_2017_5_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_SR_2017_5_12'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_CR2_2017_5_13'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_CR1_2017_5_16'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35_2017_6_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv36_2017_6_1'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv37_2017_6_2'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv36_2017_6_2' #has more plots
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35_2017_6_2' #has more plots
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_2017_6_1' #ElPt MuPt
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv38_2017_6_5'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35a_2017_6_5' #--> double checking but also with muFR=.14instead of .13 in FRv35

# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SR_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_CR2_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400_2017_9_18'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400low_2017_9_18'
pfix='kinematics_ttbarClosure_uFRv2_FWLJMET102X_3lep2017_062019_wywong_step1_FRv1_hadds_step2_2019_10_11'
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_CR1_2017_9_25'
dataList = ['TTTo2L2Nu']


# 
# # pfix='kinematics_condor_ddbkgscan_zjetsClosure_2017_3_15'
# # pfix='kinematics_condor_FULLddbkgscan_DYClosure_2017_5_14'
# # pfix='kinematics_condor_FULLddbkgscan_DYClosure_SR_2017_5_14'
# # pfix='kinematics_condor_FULLddbkgscan_DYClosure_CR2_2017_5_14'
# pfix='kinematics_condor_FULLddbkgscan_DYClosure_SR_2017_6_22'
# # pfix='kinematics_condor_FULLddbkgscan_DYClosure_CR2_2017_6_22'
# # pfix='kinematics_condor_FULLddbkgscan_DYClosure_2017_6_22'
# dataList = ['DY50']

if len(sys.argv)>1: pfix=str(sys.argv[1])

# outDir = os.getcwd()+'/'
outDir = '/mnt/data/users/wwong/'
outDir+=pfix+'/'


category = ['EEE','EEM','EMM','MMM','All']

###########################################################
#################### SAMPLE GROUPS ########################
###########################################################

bkgStackList = ['ddbkg']

ddbkgList = []
ddbkgTTTList = []
ddbkgTTLList = []
ddbkgTLTList = []
ddbkgLTTList = []
ddbkgTLLList = []
ddbkgLTLList = []
ddbkgLLTList = []
ddbkgLLLList = []

#Set in samples!
# if 'TT' in useWhichSampleForMatrix: dataList = ['TTJetsPH']
# if 'DY' in useWhichSampleForMatrix: dataList = ['DY50']

ddbkgList.append('MatrixBkg')
ddbkgTTTList.append('MatrixBkg'+ddbkgCat[0])
ddbkgTTLList.append('MatrixBkg'+ddbkgCat[1])
ddbkgTLTList.append('MatrixBkg'+ddbkgCat[2])
ddbkgLTTList.append('MatrixBkg'+ddbkgCat[3])
ddbkgTLLList.append('MatrixBkg'+ddbkgCat[4])
ddbkgLTLList.append('MatrixBkg'+ddbkgCat[5])
ddbkgLLTList.append('MatrixBkg'+ddbkgCat[6])
ddbkgLLLList.append('MatrixBkg'+ddbkgCat[7])

#adding  muFR scans as ddbkgList -start
ddbkgList_scan = []
index = 0
FRscanIndex = 0
for muFRindex in xrange(loop): #loop, run, dilep --> set in samples.py
	for elFRindex in xrange(loop): #loop, run, dilep --> set in samples.py
		if not doDDBKGscan:continue
		ddbkgList_temp = []
		ddbkgList_temp.append('MatrixBkg_muFR'+str(muFRindex+((int)(initial*100)))+'elFR'+str(elFRindex++((int)(initial*100))))
		index+=1
		ddbkgList_scan.append(ddbkgList_temp)
		FRscanIndex+=1
#adding  muFR scans as ddbkgList -end

systematicList = ['pileup','btag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','PR','FR']


###########################################################
#################### NORMALIZATIONS #######################
###########################################################

lumiSys = 0.023 #https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM
trigSys = 0.03 #3% trigger uncertainty - AN 2016 229
# lepIdSys = math.sqrt(3.*0.02**2) #1% lepton id uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
# lepIsoSys = math.sqrt(3.*0.01**2) #1% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons! - ATTENTION! NEED UPDATING!
lepIdSys = 0.02 #1.02% lepton id uncertainty ## NEED to add in quadrature for 3 leptons!
lepIsoSys = 0.03 #2% lepton isolation uncertainty ## NEED to add in quadrature for 3 leptons!
topXsecSys = 0.0 #55 #5.5% top x-sec uncertainty
ewkXsecSys = 0.0 #5 #5% ewk x-sec uncertainty
qcdXsecSys = 0.0 #50 #50% qcd x-sec uncertainty
corrdSys = math.sqrt(lumiSys**2+trigSys**2+lepIdSys**2+lepIsoSys**2)

def round_sig(x,sig=2):
	try:
		return round(x, sig-int(math.floor(math.log10(abs(x))))-1)
	except:
		return round(x,5)

###########################################################
######### GROUP SAMPLES AND PRINT YIELDS/UNCERTS ##########
###########################################################
def makeCats(datahists,sighists,bkghists,discriminant):
	## Input  histograms (datahists,sighists,bkghists) must have corresponding histograms returned from analyze.py##
	
	## INITIALIZE DICTIONARIES FOR YIELDS AND STATISTICAL UNCERTAINTIES ##
	yieldTable = {}
	yieldErrTable = {} #what is actually stored here is the square of the yield error
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		yieldTable[histoPrefix]={}
		yieldErrTable[histoPrefix]={}
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+systematic+ud]={}
	
	## WRITING HISTOGRAMS IN ROOT FILE ##
	outputRfile = R.TFile(outDir+'/templates_'+discriminant+'_'+lumiStr+'fb.root','RECREATE')
	hdata={}
	hddbkg,hddbkgTTT,hddbkgTTL,hddbkgTLT,hddbkgLTT,hddbkgTLL,hddbkgLTL,hddbkgLLT,hddbkgLLL={},{},{},{},{},{},{},{},{}
	
	hddbkg_scan = [{}]
	for FRindex in xrange(len(ddbkgList_scan)-1):hddbkg_scan.append({})
	#print hddbkg_scan
	#print 'there are', len(hddbkg_scan), "{}'s" 
	
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat

		#Group data processes
		hdata[cat] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
		for dat in dataList:
			if dat!=dataList[0]: hdata[cat].Add(datahists[histoPrefix+'_'+dat])

		#Group processes
		hddbkg[cat] = bkghists[histoPrefix+'_'+ddbkgList[0]].Clone(histoPrefix+'_ddbkg')
		#print 'Cloning ', histoPrefix+'_'+ddbkgList[0], 'and naming it', histoPrefix+'_ddbkg'
		#print hddbkg
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			hddbkg_scan[FRindex][cat] = bkghists[histoPrefix+'_'+ddbkgList_scan[FRindex][0]].Clone(histoPrefix+'_ddbkg'+ddbkgIndexing)
			#print 'Cloning ',histoPrefix+'_'+ddbkgList_scan[FRindex][0],'and naming it',histoPrefix+'_ddbkg'+ddbkgIndexing
			#print hddbkg_scan[FRindex]

		hddbkgTTT[cat] = bkghists[histoPrefix+'_'+ddbkgTTTList[0]].Clone(histoPrefix+'_ddbkgTTT')
		hddbkgTTL[cat] = bkghists[histoPrefix+'_'+ddbkgTTLList[0]].Clone(histoPrefix+'_ddbkgTTL')
		hddbkgTLT[cat] = bkghists[histoPrefix+'_'+ddbkgTLTList[0]].Clone(histoPrefix+'_ddbkgTLT')
		hddbkgLTT[cat] = bkghists[histoPrefix+'_'+ddbkgLTTList[0]].Clone(histoPrefix+'_ddbkgLTT')
		hddbkgTLL[cat] = bkghists[histoPrefix+'_'+ddbkgTLLList[0]].Clone(histoPrefix+'_ddbkgTLL')
		hddbkgLTL[cat] = bkghists[histoPrefix+'_'+ddbkgLTLList[0]].Clone(histoPrefix+'_ddbkgLTL')
		hddbkgLLT[cat] = bkghists[histoPrefix+'_'+ddbkgLLTList[0]].Clone(histoPrefix+'_ddbkgLLT')
		hddbkgLLL[cat] = bkghists[histoPrefix+'_'+ddbkgLLLList[0]].Clone(histoPrefix+'_ddbkgLLL')

		for bkg in ddbkgList:
			if bkg!=ddbkgList[0]: 
				hddbkg[cat].Add(bkghists[histoPrefix+'_'+bkg])
				#print 'Adding', bkghists[histoPrefix+'_'+bkg], 'to', hddbkg[cat]
		#print hddbkg
		
		for FRindex in xrange(len(ddbkgList_scan)):
			for bkg in ddbkgList_scan[FRindex]:
				if bkg!=ddbkgList_scan[FRindex][0]: 
					hddbkg_scan[FRindex][cat].Add(bkghists[histoPrefix+'_'+bkg])
					#print 'Adding', bkghists[histoPrefix+'_'+bkg], 'to', hddbkg_scan[FRindex][cat]
			#print hddbkg_scan[FRindex]


		for bkg in ddbkgTTTList:
			if bkg!=ddbkgTTTList[0]: hddbkgTTT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTTLList:
			if bkg!=ddbkgTTLList[0]: hddbkgTTL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTLTList:
			if bkg!=ddbkgTLTList[0]: hddbkgTLT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTTList:
			if bkg!=ddbkgLTTList[0]: hddbkgLTT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgTLLList:
			if bkg!=ddbkgTLLList[0]: hddbkgTLL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLTLList:
			if bkg!=ddbkgLTLList[0]: hddbkgLTL[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLLTList:
			if bkg!=ddbkgLLTList[0]: hddbkgLLT[cat].Add(bkghists[histoPrefix+'_'+bkg])
		for bkg in ddbkgLLLList:
			if bkg!=ddbkgLLLList[0]: hddbkgLLL[cat].Add(bkghists[histoPrefix+'_'+bkg])

		#systematics
		if doAllSys:
			for systematic in systematicList:
					if systematic=='PR' or systematic=='FR': # PR and FR is only on the ddbkg sample, so it needs special treatment!
						hddbkg[cat+systematic+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+ddbkgList[0]].Clone(histoPrefix+'__ddbkg__'+systematic+'__'+ud.replace('Up','plus').replace('Down','minus'))
						for bkg in ddbkgList: 
							if bkg!=ddbkgList[0]: hddbkg[cat+systematic+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+systematic+ud)+'_'+bkg])

		
		#Group data processes
		hdata[cat] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
		for dat in dataList:
			if dat!=dataList[0]: hdata[cat].Add(datahists[histoPrefix+'_'+dat])

		#prepare yield table
		yieldTable[histoPrefix]['totBkg'] = hddbkg[cat].Integral()

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
# 			yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] = htop[cat].Integral()+hewk[cat].Integral()+hddbkg_scan[FRindex][cat].Integral()
			yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] = hddbkg_scan[FRindex][cat].Integral()
			#print histoPrefix+' totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)+' =', yieldTable[histoPrefix]['totBkg_ddbkgMuFR'+str(FRindex/loop)+'_ElFR'+str(FRindex%loop)] 

		yieldTable[histoPrefix]['data']   = hdata[cat].Integral()
		if yieldTable[histoPrefix]['totBkg']!=0:
			yieldTable[histoPrefix]['dataOverBkg']= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
		else:
			yieldTable[histoPrefix]['dataOverBkg']= 0.

		#look here
		upperCeiling = 50000. # for protection against extraordinarily large chiSq:
		if doDDBKGscan and printProcess==True: print ''
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			if yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing]!=0:
				yieldTable[histoPrefix]['dataOverBkg_ddbkg'+ddbkgIndexing]= yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing]
			else:
				yieldTable[histoPrefix]['dataOverBkg_ddbkg'+ddbkgIndexing]= 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing] = 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt30to60'] = 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt60to100'] = 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt100to140'] = 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt140to180'] = 0.
			yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt180to500'] = 0.
			if 'lepPt' in discriminant: 
				for ibin in [3,4,5,6,7,8,9,10,11,13]: #rebin for ttbar MC
# 				for ibin in [3,4,5,6,7,9,11]: #for Zjets
					data_rebin = 0.
					ddbkg_rebin = 0.
# 					if ibin==7:
# 						for ibin_rebin in [7,8]: #for Zjets
# 							data_rebin += hdata[cat].GetBinContent(ibin_rebin)
# 							ddbkg_rebin += hddbkg_scan[FRindex][cat].GetBinContent(ibin_rebin)
# 					if ibin==9:
# 						for ibin_rebin in [9,10]: #for Zjets
# 							data_rebin += hdata[cat].GetBinContent(ibin_rebin)
# 							ddbkg_rebin += hddbkg_scan[FRindex][cat].GetBinContent(ibin_rebin)

					if ibin==11:
						for ibin_rebin in [11,12]: #rebin for ttbar MC
# 						for ibin_rebin in [11,12,13,14,15,16,17,18,19,20]: #for Zjets
							data_rebin += hdata[cat].GetBinContent(ibin_rebin)
							ddbkg_rebin += hddbkg_scan[FRindex][cat].GetBinContent(ibin_rebin)
					elif ibin==13: 
						for ibin_rebin in [13,14,15,16,17,18,19,20]: #rebin for ttbar MC
							data_rebin += hdata[cat].GetBinContent(ibin_rebin)
							ddbkg_rebin += hddbkg_scan[FRindex][cat].GetBinContent(ibin_rebin)			
					else:
						data_rebin += hdata[cat].GetBinContent(ibin)
						ddbkg_rebin += hddbkg_scan[FRindex][cat].GetBinContent(ibin)													

					yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 

					if(ptScan):
						if(ibin<5): # _pt30to60
							yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt30to60'] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 
						elif(ibin<7): # _pt60to100
							yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt60to100'] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 
						elif(ibin<9): # _pt100to140
							yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt100to140'] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 
						elif(ibin<11): # _pt140to180
							yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt140to180'] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 
						else: # _pt180to500
							yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt180to500'] += ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ) 

					if doDDBKGscan and printProcess==True and FRindex/loop+((int)(initial*100))==muFRtoPrint and FRindex%loop+((int)(initial*100))==elFRtoPrint:
						print cat,discriminant,'bin:', ibin, 'data =', data_rebin,
						print ',	ddbkg =', round_sig(ddbkg_rebin,4),
						print ',	( data - ddbkg )**2 / ddbkg=', round_sig( ( data_rebin - 	ddbkg_rebin )**2 / ( ddbkg_rebin+1e-10 ),4)

				#protect against extraordinarily large chiSq:
				if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
				if(ptScan):
					if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt30to60'] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
					if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt60to100'] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
					if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt100to140'] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
					if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt140to180'] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
					if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing+'_pt180to500'] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling
				continue			

			for ibin in range(1,hdata[cat].GetXaxis().GetNbins()+1):
				yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing] += ( hdata[cat].GetBinContent(ibin) - 	( hddbkg_scan[FRindex][cat].GetBinContent(ibin) ) )**2 / ( hddbkg_scan[FRindex][cat].GetBinContent(ibin)+1e-10 ) 
				if printProcess!=True or FRindex/loop+((int)(initial*100))!=muFRtoPrint or FRindex%loop+((int)(initial*100))!=elFRtoPrint:continue
				print cat,discriminant,'bin:', ibin, 'data =', ( hdata[cat].GetBinContent(ibin) ), 
				print ',	ddbkg:', round_sig( hddbkg_scan[FRindex][cat].GetBinContent(ibin), 4 ),  
				print ',	( data - ddbkg )**2 / ddbkg =', round_sig( ( hdata[cat].GetBinContent(ibin) - 	( hddbkg_scan[FRindex][cat].GetBinContent(ibin) ) )**2 / ( hddbkg_scan[FRindex][cat].GetBinContent(ibin)+1e-10 ) , 4 )

			#protect against extraordinarily large chiSq:
			if yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing] > upperCeiling: yieldTable[histoPrefix]['chiSq_ddbkg'+ddbkgIndexing]=upperCeiling

		if doDDBKGscan and printProcess==True and yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)]==upperCeiling:
			print cat, 'chiSq >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)]
			if(ptScan):
				print cat, 'chiSq _pt30to60 >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt30to60']
				print cat, 'chiSq _pt60to100 >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt60to100']
				print cat, 'chiSq _pt100to140 >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt100to140']
				print cat, 'chiSq _pt140to180 >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt140to180']
				print cat, 'chiSq _pt180to500 >=', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt180to500']
		elif doDDBKGscan and printProcess==True:
			print cat, 'chiSq =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)]
			if(ptScan):
				print cat, 'chiSq _pt30to60 =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt30to60']
				print cat, 'chiSq _pt60to100 =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt60to100']
				print cat, 'chiSq _pt100to140 =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt100to140']
				print cat, 'chiSq _pt140to180 =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt140to180']
				print cat, 'chiSq _pt180to500 =	', yieldTable[histoPrefix]['chiSq_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)+'_pt180to500']

		yieldTable[histoPrefix]['ddbkg']  = hddbkg[cat].Integral()
					
		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			yieldTable[histoPrefix]['ddbkg'+ddbkgIndexing]  = hddbkg_scan[FRindex][cat].Integral()
			#print 'yield '+histoPrefix+' ddbkg'+ddbkgIndexing,'=',yieldTable[histoPrefix]['ddbkg'+ddbkgIndexing]

		yieldTable[histoPrefix]['ddbkgTTT']  = hddbkgTTT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTTL']  = hddbkgTTL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTLT']  = hddbkgTLT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLTT']  = hddbkgLTT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgTLL']  = hddbkgTLL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLTL']  = hddbkgLTL[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLLT']  = hddbkgLLT[cat].Integral()
		yieldTable[histoPrefix]['ddbkgLLL']  = hddbkgLLL[cat].Integral()
		
		#+/- 1sigma variations of shape systematics
		if doAllSys:
			for systematic in systematicList:
				for ud in ['Up','Down']:
					if systematic=='PR' or systematic=='FR':
						yieldTable[histoPrefix+systematic+ud]['ddbkg'] = hddbkg[cat+systematic+ud].Integral()

		#prepare MC yield error table
		yieldErrTable[histoPrefix]['totBkg'] = 0.
		yieldErrTable[histoPrefix]['data']   = 0.
		yieldErrTable[histoPrefix]['dataOverBkg']= 0.

		yieldErrTable[histoPrefix]['ddbkg']  = 0.

		#look here
		for FRindex in xrange(len(ddbkgList_scan)): 
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] = 0.
			yieldErrTable[histoPrefix]['dataOverBkg_ddbkg'+ddbkgIndexing]= 0.
			yieldErrTable[histoPrefix]['ddbkg'+ddbkgIndexing]  = 0.

		yieldErrTable[histoPrefix]['ddbkgTTT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTTL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTLT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLTT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgTLL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLTL']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLLT']  = 0.
		yieldErrTable[histoPrefix]['ddbkgLLL']  = 0.


		for ibin in range(1,hdata[cat].GetXaxis().GetNbins()+1):
			yieldErrTable[histoPrefix]['totBkg'] += hddbkg[cat].GetBinError(ibin)**2
				
			yieldErrTable[histoPrefix]['data']   += hdata[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkg']  += hddbkg[cat].GetBinError(ibin)**2

			yieldErrTable[histoPrefix]['ddbkgTTT']  += hddbkgTTT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTTL']  += hddbkgTTL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTLT']  += hddbkgTLT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTT']  += hddbkgLTT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgTLL']  += hddbkgTLL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLTL']  += hddbkgLTL[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLLT']  += hddbkgLLT[cat].GetBinError(ibin)**2
			yieldErrTable[histoPrefix]['ddbkgLLL']  += hddbkgLLL[cat].GetBinError(ibin)**2

		#look here , need to treat totbkg and ddbkg errors a bit differently to account for muFR scanning
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			for ibin in range(1,hdata[cat].GetXaxis().GetNbins()+1):
				yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] += hddbkg_scan[FRindex][cat].GetBinError(ibin)**2
				yieldErrTable[histoPrefix]['ddbkg'+ddbkgIndexing]  += hddbkg_scan[FRindex][cat].GetBinError(ibin)**2

		#yieldErrTable[histoPrefix]['totBkg'] += (corrdSys*yieldTable[histoPrefix]['totBkg'])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			#yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] += (corrdSys*yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing])**2+(topXsecSys*yieldTable[histoPrefix]['top'])**2+(ewkXsecSys*yieldTable[histoPrefix]['ewk'])**2
			yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing] += (corrdSys*yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing])**2
			#print 'sqrt yieldErrTable ',histoPrefix,' totBkg_ddbkg'+ddbkgIndexing,'=',math.sqrt(yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing])


		if yieldTable[histoPrefix]['totBkg']!=0: 
			Ratio = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
		else:
			Ratio = 0.0			
# 		yieldErrTable[histoPrefix]['dataOverBkg'] = (Ratio**2) * ((yieldErrTable[histoPrefix]['data']/(yieldTable[histoPrefix]['data']+1e-20))**2 + (yieldErrTable[histoPrefix]['totBkg']/(yieldTable[histoPrefix]['totBkg']+1e-20))**2)
		yieldErrTable[histoPrefix]['dataOverBkg'] = (Ratio**2) * (        (math.sqrt(yieldErrTable[histoPrefix]['data'])      /(yieldTable[histoPrefix]['data']+1e-20))**2 + (math.sqrt(yieldErrTable[histoPrefix]['totBkg'])/(yieldTable[histoPrefix]['totBkg']+1e-20))**2)

		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			if yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing]!=0: 
				Ratio = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing]
			else:
				Ratio = 0.0			
			yieldErrTable[histoPrefix]['dataOverBkg_ddbkg'+ddbkgIndexing] = (Ratio**2) * (        (math.sqrt(yieldErrTable[histoPrefix]['data'])      /(yieldTable[histoPrefix]['data']+1e-20))**2 + (math.sqrt(yieldErrTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing])/(yieldTable[histoPrefix]['totBkg_ddbkg'+ddbkgIndexing]+1e-20))**2)
			#print 'sqrt yieldErrTable '+histoPrefix+'dataOverBkg_ddbkg'+ddbkgIndexing+' =',math.sqrt( yieldErrTable[histoPrefix]['dataOverBkg_ddbkg'+ddbkgIndexing] )

		#print interactive display output
		if doDDBKGscan and printProcess==True: print 'data      :',yieldTable[histoPrefix]['data'],'+-',round_sig(math.sqrt(yieldErrTable[histoPrefix]['data']),4)
		if doDDBKGscan and printProcess==True: print 'ddbkg     :',round_sig(yieldTable[histoPrefix]['ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)],4),'+-',round_sig(math.sqrt(yieldErrTable[histoPrefix]['ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)]),4)
		if doDDBKGscan and printProcess==True: print 'data/ddbkg:',round_sig(yieldTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)],4),'+-',round_sig(math.sqrt(yieldErrTable[histoPrefix]['dataOverBkg_ddbkgMuFR'+str(muFRtoPrint)+'_ElFR'+str(elFRtoPrint)]),4)

		hdata[cat].Write()
		#write theta histograms in root file, avoid having processes with no event yield (to make theta happy) 
		if hddbkg[cat].Integral() > 0: 
			hddbkg[cat].Write()
			if doAllSys:
				for systematic in systematicList:
					if systematic!='PR' and systematic!='FR': continue
					hddbkg[cat+systematic+'Up'].Write()
					hddbkg[cat+systematic+'Down'].Write()
		#look here
		for FRindex in xrange(len(ddbkgList_scan)):
			ddbkgIndexing = 'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100)))
			if hddbkg_scan[FRindex][cat].Integral() >= 0: hddbkg_scan[FRindex][cat].Write()
			else : print("FR scan with negative integral at muFR %s elFR %s" %(str(FRindex/loop+((int)(initial*100))), str(FRindex%loop+((int)(initial*100)))))
		hddbkgTTT[cat].Write()
		hddbkgTTL[cat].Write()
		hddbkgTLT[cat].Write()
		hddbkgLTT[cat].Write()
		hddbkgTLL[cat].Write()
		hddbkgLTL[cat].Write()
		hddbkgLLT[cat].Write()
		hddbkgLLL[cat].Write()

	outputRfile.Close()

	stdout_old = sys.stdout
	logFile = open(outDir+'/yields_'+discriminant+'_'+lumiStr.replace('.','p')+'fb.txt','a')
	sys.stdout = logFile

	## PRINTING YIELD TABLE WITH UNCERTAINTIES ##
	#first print table without background grouping
	ljust_i = 1
	print 'CUTS:',cutString
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for bkg in bkgStackList: print bkg.ljust(ljust_i),
	print 'data'.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for bkg in bkgStackList:
			print str(yieldTable[histoPrefix][bkg])+'\t',
		print str(yieldTable[histoPrefix]['data']),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		for bkg in bkgStackList:
			print str(math.sqrt(yieldErrTable[histoPrefix][bkg])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['data'])).ljust(ljust_i),
		print

	#now print with top,ewk,qcd grouping
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	print 'ddbkg'.ljust(ljust_i),

	print 'ddbkgTTT'.ljust(ljust_i),
	print 'ddbkgTTL'.ljust(ljust_i),
	print 'ddbkgTLT'.ljust(ljust_i),
	print 'ddbkgLTT'.ljust(ljust_i),
	print 'ddbkgTLL'.ljust(ljust_i),
	print 'ddbkgLTL'.ljust(ljust_i),
	print 'ddbkgLLT'.ljust(ljust_i),
	print 'ddbkgLLL'.ljust(ljust_i),

	print 'data'.ljust(ljust_i),
	print
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkg']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgTTT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgTTL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgTLT']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLTT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgTLL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLTL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['ddbkgLLT']).ljust(ljust_i),

		print str(yieldTable[histoPrefix]['ddbkgLLL']).ljust(ljust_i),
		print str(yieldTable[histoPrefix]['data']).ljust(ljust_i),
		print

	print 'YIELDS STATISTICAL + NORM. SYS. ERRORS'
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print (cat).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkg'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTTT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTTL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTLT'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLTT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgTLL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLTL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLLT'])).ljust(ljust_i),

		print str(math.sqrt(yieldErrTable[histoPrefix]['ddbkgLLL'])).ljust(ljust_i),
		print str(math.sqrt(yieldErrTable[histoPrefix]['data'])).ljust(ljust_i),
		print

				
	#print for AN tables
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print histoPrefix.ljust(ljust_i),
	print
	for process in bkgStackList+['ddbkgTTT','ddbkgTTL','ddbkgTLT','ddbkgLTT','ddbkgTLL','ddbkgLTL','ddbkgLLT','ddbkgLLL','totBkg','data','dataOverBkg']:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4))+' $\pm$ '+str(round_sig(math.sqrt(yieldErrTable[histoPrefix][process]),2)),
		print '\\\\',
		print

	#print for AN tables - ddbkg scan
	print
	print 'YIELDS'.ljust(20*ljust_i), 
	for cat in category:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		print histoPrefix.ljust(ljust_i),
	print

	#look here!!
	tempProcess = []
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('ddbkgMuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))))
# 	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('totBkg_ddbkgMuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))))
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('dataOverBkg_ddbkgMuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))))
	for process in tempProcess:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4))+' $\pm$ '+str(round_sig(math.sqrt(yieldErrTable[histoPrefix][process]),2)),
		print '\\\\',
		print
	
	print ''

	tempProcess = [] # Mu --> El loop
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('chiSq_ddbkgMuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))))
	for process in tempProcess:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4)),
		print '\\\\',
		print

	print ''
	
	tempProcess = [] #El --> Mu loop
	for FRindex in xrange(len(ddbkgList_scan)): tempProcess.append('chiSq_ddbkgMuFR'+str(FRindex%loop+((int)(initial*100)))+'_ElFR'+str(FRindex/loop+((int)(initial*100))))
	for process in tempProcess:
		print process.ljust(ljust_i),
		for cat in category:
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			print ' & '+str(round_sig(yieldTable[histoPrefix][process],4)),
		print '\\\\',
		print
				
	sys.stdout = stdout_old
	logFile.close()

	## WRITING HISTOGRAMS IN ROOT FILE for ChiSq of 2DFRscan##
	print ''
	print 'Processing 2D Lep FR scan Chi Sq:'
	outputRfile_chiSq = R.TFile(outDir+'/chiSq_'+discriminant+'_'+lumiStr+'fb.root','RECREATE')
	ptRanges = ['']
	if(ptScan):ptRanges = ['','_pt30to60','_pt60to100','_pt100to140','_pt140to180','_pt180to500']
	for postFix in ptRanges:
		print 'processing '+postFix+' ...'
		h_chiSq={}
		min_chiSq={}
		min_process = {}		
		for cat in category:
			h_chiSq[cat]={}
			min_chiSq[cat]={}
			min_process[cat]={}		
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			min_chiSq[cat][postFix] = 100000.
			h_chiSq[cat][postFix] = R.TH2D('chiSq_'+cat+postFix,'chiSq_'+cat+postFix,loop,initial,end+increment,loop,initial,end+increment)
			for FRindex in xrange(len(ddbkgList_scan)):
				process ='chiSq_ddbkg'+'MuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))) 
				chiSq = round_sig(yieldTable[histoPrefix][process+postFix],4)
				bin_x = 1+(FRindex/loop)
				bin_y = 1+(FRindex%loop)
				h_chiSq[cat][postFix].SetBinContent(bin_x,bin_y,chiSq)
				if chiSq < min_chiSq[cat][postFix] and chiSq!=0 : #protect against chiSq==0.0!
					min_chiSq[cat][postFix] = chiSq
					min_process[cat][postFix] = process
				#if doDDBKGscan and printProcess and FRindex/loop+((int)(initial*100))==muFRtoPrint and FRindex%loop+((int)(initial*100))==elFRtoPrint:print cat, process, 'filling TH2D(', bin_x-1,bin_y-1,chiSq,')'
				h_chiSq[cat][postFix].Write()

		#Calculate average chi_avr plot, and find global minimum.
		h_chiSq['average'] = {}
		min_chiSq['average'] = {}
		min_process['average']={}		
		min_chiSq['average'][postFix] = 100000.
		h_chiSq['average'][postFix] = R.TH2D('chiSq_average'+postFix,'chiSq_average'+postFix,loop,initial,end+increment,loop,initial,end+increment)
		for FRindex in xrange(len(ddbkgList_scan)):
			chiSq_avr = 0.0
			process ='chiSq_ddbkgMuFR'+str(FRindex/loop+((int)(initial*100)))+'_ElFR'+str(FRindex%loop+((int)(initial*100))) 
			for cat in category: 
				if 'All' in cat: continue
				#chiSq_avr += round_sig(yieldTable[discriminant+'_'+lumiStr+'fb_'+cat][process+postFix] / 4. ,4)
				chiSq_avr += round_sig(yieldTable[discriminant+'_'+lumiStr+'fb_'+cat][process+postFix] ,4) #based on recommendation by Roman, and also Meenakshi, she actually said it a while ago. Just sum al four categories and dont average, since these four categories are statistically independent.
			if chiSq_avr < min_chiSq['average'][postFix] and chiSq_avr!=0 : #protect against chiSq==0.0!
				min_chiSq['average'][postFix] = chiSq_avr
				min_process['average'][postFix] = process
			bin_x = 1+(FRindex/loop)
			bin_y = 1+(FRindex%loop)
			h_chiSq['average'][postFix].SetBinContent(bin_x,bin_y,chiSq_avr)
			#if doDDBKGscan and printProcess and FRindex/loop+((int)(initial*100))==muFRtoPrint and FRindex%loop+((int)(initial*100))==elFRtoPrint:print 'average', process, 'filling TH2D(',bin_x-1,bin_y-1,chiSq_avr,')'
		h_chiSq['average'][postFix].Write()

		for cat in category+['average']: 
			try:
				print 'Minimum ',cat,' chi sq '+postFix+' = ', min_chiSq[cat][postFix], min_process[cat][postFix].replace('chiSq_ddbkg','').split('_')[0].replace('MuFR','MuFR = '),'% ',min_process[cat][postFix].replace('chiSq_ddbkg','').split('_')[1].replace('ElFR','ElFR = '),'%'
			except:
				print 'Something is wrong or empty. So check!'
				continue
	
	outputRfile_chiSq.Close()


###########################################################
###################### LOAD HISTS #########################
###########################################################

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

distList = []
print outDir
for file in findfiles(outDir+'/'+category[0]+'/', '*.p'):
    if 'bkghists' not in file: continue
    distList.append(file.split('_')[-1][:-2])
print distList
for dist in distList:
	print "DISTRIBUTION: ",dist
	if 'lepPt' not in dist: continue
# 	if 'ElPt' not in dist and 'MuPt' not in dist: continue
# 	if 'ST' in dist: continue
# 	if 'lepEta' in dist: continue
	datahists = {}
	bkghists  = {}
	sighists  = {}
	for cat in category:
		print "LOADING: ",cat
		datahists.update(pickle.load(open(outDir+'/'+cat+'/datahists_'+dist+'.p','rb')))
		bkghists.update(pickle.load(open(outDir+'/'+cat+'/bkghists_'+dist+'.p','rb')))
	makeCats(datahists,sighists,bkghists,dist)

print 'AFTER YOU CHECK THE OUTPUT FILES, DELETE THE PICKLE FILES !!!!!!!'
print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
