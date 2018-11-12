#!/usr/bin/python

import ROOT as R
from array import array
from weights import *
from samples import *

"""
--This function will make kinematic plots for a given distribution for electron, muon channels and their combination
--Check the cuts below to make sure those are the desired full set of cuts!
--The applied weights are defined in "weights.py". Also, the additional weights (SFs, 
negative MC weights, ets) applied below should be checked!
"""

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb

def analyze(tTree,process,cutList,doAllSys,discriminantName,discriminantDetails,category):
# 	print "*****"*20
# 	print "*****"*20
# 	print "DISTRIBUTION:", discriminantName
# 	print "            -name in ljmet trees:", discriminantDetails[0]
# 	print "            -x-axis label is set to:", discriminantDetails[2]
# 	print "            -using the binning as:", discriminantDetails[1]
	discriminantLJMETName=discriminantDetails[0]
	xbins=array('d', discriminantDetails[1])
	xAxisLabel=discriminantDetails[2]
	
# 	print "/////"*5
	print "PROCESSING: ", process, " CATEGORY: ", category
# 	print "/////"*5
	cut = '1'

	cut += ' && (AllLeptonPt_PtOrdered[0] >= '+str(cutList['lepPtCut'])+')'
	cut += ' && (AllLeptonPt_PtOrdered[1] >= '+str(cutList['lepPtCut'])+')'
	cut += ' && (AllLeptonPt_PtOrdered[2] >= '+str(cutList['lepPtCut'])+')'

# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[0]) < 1.2)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[1]) < 1.2)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[2]) < 1.2)'

# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[0]) >= 1.2)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[1]) >= 1.2)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[2]) >= 1.2)'
# 
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[0]) < 2.1)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[1]) < 2.1)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[2]) < 2.1)'
# 
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[0]) >= 2.1)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[1]) >= 2.1)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[2]) >= 2.1)'
# 
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[0]) < 2.4)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[1]) < 2.4)'
# 	cut += ' && (fabs(AllLeptonEta_PtOrdered[2]) < 2.4)'


	cut += ' && (corr_met_singleLepCalc >= '+str(cutList['metCut'])+')'

# 	cut += ' && (NJets_singleLepCalc >= '+str(cutList['njetsCut'])+')' #SR
	cut += ' && (NJets_singleLepCalc == '+str(cutList['njetsCut'])+')' #FRCR1, FRCR2
# 	cut += ' && (NJets_singleLepCalc == 2 || NJets_singleLepCalc == 1)' #FRCR1CR2

# 	cut += ' && (NJets_JetSubCalc >= '+str(cutList['njetsCut'])+')'
	cut += ' && (NJetsBTagwithSF_singleLepCalc >= '+str(cutList['nbjetsCut'])+')'
# 	cut += ' && (NJetsCSVwithSF_JetSubCalc_noLepCorr >= '+str(cutList['nbjetsCut'])+')'
	if ('Data' in process and 'Bkg' not in process): 
		if 'RRH' in process: #for runH use DZ version of HLT
			if cutList['isPassTrig_dilep']==1:cut += ' && DataPastTrigger_dilepDZ4runH == 1'
			if cutList['isPassTrilepton']==1 :  cut += ' && isPassTrilepton == 1'
		else:
			if cutList['isPassTrig']==1:        cut += ' && DataPastTrigger == 1'
			if cutList['isPassTrig_dilep']==1:  cut += ' && DataPastTrigger_dilep == 1'
			if cutList['isPassTrig_dilep_anth']==1:cut += ' && DataPastTrigger_dilep_anth == 1'
			if cutList['isPassTrig_trilep']==1: cut += ' && DataPastTrigger_trilep == 1'
			if cutList['isPassTrilepton']==1 :  cut += ' && isPassTrilepton == 1'
	elif ('DataDrivenBkg' in process): 
		if 'RRH' in process: #for runH use DZ version of HLT
			if cutList['isPassTrig_dilep']==1:cut += ' && DataPastTrigger_dilepDZ4runH == 1'
		else:
			if cutList['isPassTrig']==1:        cut += ' && DataPastTrigger == 1'
			if cutList['isPassTrig_dilep']==1:  cut += ' && DataPastTrigger_dilep == 1'
			if cutList['isPassTrig_dilep_anth']==1:cut += ' && DataPastTrigger_dilep_anth == 1'
			if cutList['isPassTrig_trilep']==1: cut += ' && DataPastTrigger_trilep == 1'
	elif ('Data' not in process): 
		if cutList['isPassTrig']==1:        cut += ' && MCPastTrigger == 1'
		if cutList['isPassTrig_dilep']==1:  cut += ' && MCPastTrigger_dilep == 1'
		if cutList['isPassTrig_dilep_anth']==1:cut += ' && MCPastTrigger_dilep_anth == 1'
		if cutList['isPassTrig_trilep']==1: cut += ' && MCPastTrigger_trilep == 1'
		if cutList['isPassTrilepton']==1 :  cut += ' && isPassTrilepton == 1'	
# 	cut += ' && (deltaR_lepJets[1] >= '+str(cutList['drCut'])+')'

 	cut += ' && (AK4HTpMETpLepPt >= '+str(cutList['stCut'])+')' #remove low ST default
#  	cut += ' && (AK4HTpMETpLepPt < '+str(cutList['stCut'])+')' #remove high ST

 	cut += ' && (AK4HT >= '+str(cutList['htCut'])+')' #remove low HT default
#  	cut += ' && (AK4HT < '+str(cutList['htCut'])+')' #remove high HT

	cut += ' && (minMlllBjet >= '+str(cutList['mlllbCut'])+')' #remove low value default
# 	cut += ' && (minMlllBjet < '+str(cutList['mlllbCut'])+')' #remove high value

	#ATTENION, lines below might need to be commented!!
# 	cut += ' && ( ( ptRel_minDRlep1Jet > '+str(cutList['ptRelCut'])+'  || minDR_lep1Jet > '+str(cutList['minDRlepJetCut'])+' )' 
# 	cut += '   && ( ptRel_minDRlep2Jet > '+str(cutList['ptRelCut'])+'  || minDR_lep2Jet > '+str(cutList['minDRlepJetCut'])+' )' 
# 	cut += '   && ( ptRel_minDRlep3Jet > '+str(cutList['ptRelCut'])+'  || minDR_lep3Jet > '+str(cutList['minDRlepJetCut'])+' ) )' 

 	cut += ' && AllLeptonCount_PtOrdered == 3' #require exactly 3 leptons

	### cut only events where there is a OS lepton pair and that it has 0<MllOS<cutvalue 
	cut += ' && ( (MllOS_allComb[0] > '+str(cutList['mllOSCut'])+' || MllOS_allComb[0] < 0)' 
	cut += ' && (MllOS_allComb[1] > '+str(cutList['mllOSCut'])+' || MllOS_allComb[1] < 0)' 
	cut += ' && (MllOS_allComb[2] > '+str(cutList['mllOSCut'])+' || MllOS_allComb[2] < 0) )' 

# 	cut += ' && MllOS_allComb_min > '+str(cutList['mllOSCut']) #to make sure the OS pair are same sign cut above 0. 

	catCut=''
	if category=='EEE': catCut+=' && isEEE==1'
	if category=='EEM': catCut+=' && isEEM==1'
	if category=='EMM': catCut+=' && isEMM==1'
	if category=='MMM': catCut+=' && isMMM==1'
	


#Start -- Method if isTTT doesnt exist
# 	'''
	if 'DataDrivenBkgTTT' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==1 && AllLeptonIsTight_PtOrdered[2]==1)'

	if 'DataDrivenBkgTTL' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==1 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)'
		if category=='EMM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1) )'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
	if 'DataDrivenBkgTLT' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==1 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='EMM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1) )'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
	if 'DataDrivenBkgLTT' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==1 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='EMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'

	if 'DataDrivenBkgTLL' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==0 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='EMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
	if 'DataDrivenBkgLTL' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==0 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='EMM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'
	if 'DataDrivenBkgLLT' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==0 && AllLeptonIsTight_PtOrdered[2]==0)'
		if category=='EEE':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EEM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)'
		if category=='EMM':
			cut+=' &&  ( (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)'
			cut+=' ||    (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0) )'
		if category=='MMM':
			cut+=' && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)'

	if 'DataDrivenBkgLLL' in process: 
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==0 && AllLeptonIsTight_PtOrdered[1]==0 && AllLeptonIsTight_PtOrdered[2]==0)'
# 	'''
#End -- Method if isTTT doesnt exist

#Start -- Method if isTTT  exist
	'''
	if 'DataDrivenBkgTTT' in process: cut+=' && isTTT==1'
	if 'DataDrivenBkgTTL' in process: cut+=' && isTTL==1'
	if 'DataDrivenBkgTLT' in process: cut+=' && isTLT==1'
	if 'DataDrivenBkgLTT' in process: cut+=' && isLTT==1'
	if 'DataDrivenBkgTLL' in process: cut+=' && isTLL==1'
	if 'DataDrivenBkgLTL' in process: cut+=' && isLTL==1'
	if 'DataDrivenBkgLLT' in process: cut+=' && isLLT==1'
	if 'DataDrivenBkgLLL' in process: cut+=' && isLLL==1'
	'''
#End -- Method if isTTT exist

	TrigEff = 'TrigEffWeight'
		
	if 'muFR0elFR0' in process and 'EEE' in category: print "Applying Cuts: ", cut
	
	doDDBKGsys = False

	#create and initialize histograms 
	hists = {}
	hists[discriminantName+'_'+lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'_'+lumiStr+'fb_'+category+'_' +process,xAxisLabel,len(xbins)-1,xbins)
	if doAllSys or doDDBKGsys:
		if doDDBKGsys and 'DataDrivenBkg' in process: 	
			hists[discriminantName+'PRUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'PRUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'PRDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'PRDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'FRUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'FRUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'FRDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'FRDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		elif doAllSys:			
			hists[discriminantName+'pileupUp_'  +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'pileupUp_'  +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'pileupDown_'+lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'pileupDown_'+lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRFcorrdUp_'  +lumiStr+'fb_'+category+'_'+process]=R.TH1D(discriminantName+'muRFcorrdUp_'  +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRFcorrdDown_'+lumiStr+'fb_'+category+'_'+process]=R.TH1D(discriminantName+'muRFcorrdDown_'+lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'muRUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'muRDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muFUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'muFUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muFDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'muFDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'topptUp_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'topptUp_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'topptDown_' +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'topptDown_' +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jmrUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jmrUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jmrDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jmrDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jmsUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jmsUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jmsDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jmsDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'tau21Up_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'tau21Up_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'tau21Down_' +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'tau21Down_' +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jsfUp_'     +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jsfUp_'     +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			hists[discriminantName+'jsfDown_'   +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'jsfDown_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)

			hists[discriminantName+'btagUp_'    +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'btagUp_'    +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'btagDown_'  +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'btagDown_'  +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'bmistagUp_'    +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'bmistagUp_'    +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'bmistagDown_'  +lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'bmistagDown_'  +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)


# 			if tTree[process+'jecUp']:		
# 				hists[discriminantName+'jecUp_'   +lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'jecUp_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 				hists[discriminantName+'jecDown_' +lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'jecDown_' +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			if tTree[process+'jerUp']:		
# 				hists[discriminantName+'jerUp_'   +lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'jerUp_'   +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 				hists[discriminantName+'jerDown_' +lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'jerDown_' +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 			if tTree[process+'btagUp']:		
# 				hists[discriminantName+'btagUp_'  +lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'btagUp_'  +lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
# 				hists[discriminantName+'btagDown_'+lumiStr+'fb_'+category+'_'+process]  = R.TH1D(discriminantName+'btagDown_'+lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			for i in range(100): hists[discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_'+category+'_'+process] = R.TH1D(discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_'+category+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	for key in hists.keys(): hists[key].Sumw2()
	
	#Determins weights	
	if 'Data' in process: 
		if ('DataDrivenBkg' in process):
			if ('TTT' in process or 'TTL' in process or 'TLT' in process or 'LTT' in process or 'TLL' in process or 'LTL' in process or 'LLT' in process or 'LLL' in process):  
				weightStr         ='1'
				weightPRUpStr     ='1'
				weightPRDownStr   ='1'
				weightFRUpStr     ='1'
				weightFRDownStr   ='1'
				#print 'weightStr-------------------------------------------------------->', weightStr
			elif('muFR'in process):
 				#print ''
 				#print '------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>  LOOK HERE. process: ',process
				#print 'weightStr = ddBkgWeights_scan['+str(int((process.split('muFR')[1]).split('elFR')[0])*loop + int((process.split('muFR')[1]).split('elFR')[1]) )+']' #loop set in samples
				weightStr         ='ddBkgWeights_scan['+str(int((process.split('muFR')[1]).split('elFR')[0])*loop + int((process.split('muFR')[1]).split('elFR')[1]))+']' #loop set in samples
				weightPRUpStr     ='1'
				weightPRDownStr   ='1'
				weightFRUpStr     ='1'
				weightFRDownStr   ='1'				
			else: 
				#print 'process----------------------------------------------------------> ', process
				weightStr         ='ddBkgWeights[0]'
				weightPRUpStr     ='ddBkgWeights[3]'
				weightPRDownStr   ='ddBkgWeights[4]'
				weightFRUpStr     ='ddBkgWeights[1]'
				weightFRDownStr   ='ddBkgWeights[2]'
		else: 
			weightStr         ='1'
			weightPRUpStr     ='1'
			weightPRDownStr   ='1'
			weightFRUpStr     ='1'
			weightFRDownStr   ='1'

		weightPileupUpStr   = '1'
		weightPileupDownStr = '1'
		weightmuRFcorrdUpStr   = '1'
		weightmuRFcorrdDownStr = '1'
		weightmuRUpStr   = '1'
		weightmuRDownStr = '1'
		weightmuFUpStr   = '1'
		weightmuFDownStr = '1'
		weighttopptUpStr    = '1'
		weighttopptDownStr  = '1'
		weightjsfUpStr    = '1'
		weightjsfDownStr  = '1'		
	else: 
		weightStr           = TrigEff+' * pileupWeight * 1 * isoSF * lepIdSF * EGammaGsfSF * MuTrkSF * MCWeight_singleLepCalc/abs(MCWeight_singleLepCalc) * '+str(weight[process])
		weightPileupUpStr   = weightStr.replace('pileupWeight','pileupWeightUp')
		weightPileupDownStr = weightStr.replace('pileupWeight','pileupWeightDown')
		weightmuRFcorrdUpStr   = 'renormWeights[5] * '+weightStr
		weightmuRFcorrdDownStr = 'renormWeights[3] * '+weightStr
		weightmuRUpStr      = 'renormWeights[4] * '+weightStr
		weightmuRDownStr    = 'renormWeights[2] * '+weightStr
		weightmuFUpStr      = 'renormWeights[1] * '+weightStr
		weightmuFDownStr    = 'renormWeights[0] * '+weightStr
		weighttopptUpStr    = weightStr
		weighttopptDownStr  = 'topPtWeight * '+weightStr
		weightjsfUpStr      = weightStr.replace('JetSF','JetSFupwide')
		weightjsfDownStr    = weightStr.replace('JetSF','JetSFdnwide')

	#Draw histograms
	try:
		tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+''+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')
# 		print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DRAW SUCCESSFULL!!!!!'
	except:
		print '--------------------------------------------------------------------------------------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>Skip DRAW'
	if doAllSys or doDDBKGsys:
		if doDDBKGsys and 'DataDrivenBkg' in process: 
# 			print 'Processing ddbkg sys !'
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'PRUp_'     +lumiStr+'fb_'+category+'_'+process, weightPRUpStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'PRDown_'   +lumiStr+'fb_'+category+'_'+process, weightPRDownStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'FRUp_'     +lumiStr+'fb_'+category+'_'+process, weightFRUpStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'FRDown_'   +lumiStr+'fb_'+category+'_'+process, weightFRDownStr+'*('+cut+catCut+')', 'GOFF')
		if doAllSys:
# 			print 'Processing ALL other sys !'
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pileupUp_'  +lumiStr+'fb_'+category+'_'+process, weightPileupUpStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pileupDown_'+lumiStr+'fb_'+category+'_'+process, weightPileupDownStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRFcorrdUp_'  +lumiStr+'fb_'+category+'_'+process, weightmuRFcorrdUpStr  +'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRFcorrdDown_'+lumiStr+'fb_'+category+'_'+process, weightmuRFcorrdDownStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRUp_'     +lumiStr+'fb_'+category+'_'+process, weightmuRUpStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRDown_'   +lumiStr+'fb_'+category+'_'+process, weightmuRDownStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muFUp_'     +lumiStr+'fb_'+category+'_'+process, weightmuFUpStr+'*('+cut+catCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muFDown_'   +lumiStr+'fb_'+category+'_'+process, weightmuFDownStr+'*('+cut+catCut+')', 'GOFF')
# 			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'topptUp_'   +lumiStr+'fb_'+category+'_'+process, weighttopptUpStr+'*('+cut+catCut+')', 'GOFF')
# 			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'topptDown_' +lumiStr+'fb_'+category+'_'+process, weighttopptDownStr+'*('+cut+catCut+')', 'GOFF')
# 			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jsfUp_'     +lumiStr+'fb_'+category+'_'+process, weightjsfUpStr+'*('+cut+catCut+')', 'GOFF')
# 			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jsfDown_'   +lumiStr+'fb_'+category+'_'+process, weightjsfDownStr+'*('+cut+catCut+')', 'GOFF')
			
			# replace cuts for shifts
			nbtagLJMETname = 'NJetsBTagwithSF_singleLepCalc'
			cut_btagUp = cut.replace(nbtagLJMETname,'NJetsBTagwithSF_singleLepCalc_shifts[0]')#nbtagLJMETname+'_shifts[0]')
			cut_btagDn = cut.replace(nbtagLJMETname,'NJetsBTagwithSF_singleLepCalc_shifts[1]')#nbtagLJMETname+'_shifts[1]')
			cut_mistagUp = cut.replace(nbtagLJMETname,'NJetsBTagwithSF_singleLepCalc_shifts[2]')#nbtagLJMETname+'_shifts[2]')
			cut_mistagDn = cut.replace(nbtagLJMETname,'NJetsBTagwithSF_singleLepCalc_shifts[3]')#nbtagLJMETname+'_shifts[3]')
			
			bTagSFshiftName = discriminantLJMETName
			if 'NJetsBTag' in discriminantLJMETName: 
				bTagSFshiftName = discriminantLJMETName+'_shifts[0]'
			print 'BTAGup LJMET NAME',bTagSFshiftName.replace('_shifts[0]','_shifts[0]')
			tTree[process].Draw(bTagSFshiftName.replace('_shifts[0]','_shifts[0]')+' >> '+discriminantName+'btagUp'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut_btagUp+catCut+')', 'GOFF')
			print 'BTAGdn LJMET NAME',bTagSFshiftName.replace('_shifts[0]','_shifts[1]')
			tTree[process].Draw(bTagSFshiftName.replace('_shifts[0]','_shifts[1]')+' >> '+discriminantName+'btagDown'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut_btagDn+catCut+')', 'GOFF')
			print 'MISTAGup LJMET NAME',bTagSFshiftName.replace('_shifts[0]','_shifts[2]')
			tTree[process].Draw(bTagSFshiftName.replace('_shifts[0]','_shifts[2]')+' >> '+discriminantName+'mistagUp'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut_mistagUp+catCut+')', 'GOFF')
			print 'MISTAGdn LJMET NAME',bTagSFshiftName.replace('_shifts[0]','_shifts[3]')
			tTree[process].Draw(bTagSFshiftName.replace('_shifts[0]','_shifts[3]')+' >> '+discriminantName+'mistagDown'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut_mistagDn+catCut+')', 'GOFF')

# 			if tTree[process+'jecUp']:
# 				tTree[process+'jecUp'].Draw(discriminantLJMETName   +' >> '+discriminantName+'jecUp'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')
# 				tTree[process+'jecDown'].Draw(discriminantLJMETName +' >> '+discriminantName+'jecDown'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')
# 			if tTree[process+'jerUp']:
# 				tTree[process+'jerUp'].Draw(discriminantLJMETName   +' >> '+discriminantName+'jerUp'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')
# 				tTree[process+'jerDown'].Draw(discriminantLJMETName +' >> '+discriminantName+'jerDown'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')

# # 			if tTree[process+'btagUp']:
# # 				tTree[process+'btagUp'].Draw(discriminantLJMETName  +' >> '+discriminantName+'btagUp'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')
# # 				tTree[process+'btagDown'].Draw(discriminantLJMETName+' >> '+discriminantName+'btagDown'+'_'+lumiStr+'fb_'+category+'_' +process, weightStr+'*('+cut+catCut+')', 'GOFF')

			for i in range(100): tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_'+category+'_'+process, 'pdfWeights['+str(i)+'] * '+weightStr+'*('+cut+catCut+')', 'GOFF')
	
	for key in hists.keys(): hists[key].SetDirectory(0)	
	
	return hists
