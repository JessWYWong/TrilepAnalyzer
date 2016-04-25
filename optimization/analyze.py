#!/usr/bin/python

from array import array
from weights import *
import ROOT as R

"""
--This function will make theta templates for a given distribution and a category
--Check the cuts below to make sure those are the desired full set of cuts!
--The applied weights are defined in "weights.py". Also, the additional weights (SFs, 
negative MC weights, ets) applied below should be checked!
"""

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb

def analyze(tTree,process,cutList,doAllSys,discriminantName,discriminantDetails,category):
	print "*****"*20
	print "*****"*20
	print "DISTRIBUTION:", discriminantName
	print "            -name in ljmet trees:", discriminantDetails[0]
	print "            -x-axis label is set to:", discriminantDetails[2]
	print "            -using the binning as:", discriminantDetails[1]
	discriminantLJMETName=discriminantDetails[0]
	xbins=array('d', discriminantDetails[1])
	xAxisLabel=discriminantDetails[2]
	
	print "/////"*5
	print "PROCESSING: ", process
	print "/////"*5
        cut = '1'
#       cut += '(leptonPt_singleLepCalc > '+str(cutList['lepPtCut'])+')'                                                                                                                                                                    
#       cut += ' && (corr_met_singleLepCalc > '+str(cutList['metCut'])+')'                                                                                                                                                                 
#       cut += ' && (theJetPt_JetSubCalc_PtOrdered[0] > '+str(cutList['leadJetPtCut'])+')'                                                                                                                                                  
#       cut += ' && (theJetPt_JetSubCalc_PtOrdered[1] > '+str(cutList['subLeadJetPtCut'])+')'                                                                                                                                               
#       cut += ' && (theJetPt_JetSubCalc_PtOrdered[2] > '+str(cutList['thirdJetPtCut'])+')'                                                                                                                                                 
#       cut += ' && (NJetsHtagged == 0)'                                                                                                                                                                                                    
#       cut += ' && ('+wtagvar+' == 0)'                                                                                                                                                                                                     
        cut += ' && (deltaR_lepClosestJet[0] > 0.4 || PtRelLepClosestJet[0] > 40)'
        cut += ' && (deltaR_lepClosestJet[1] > 0.4 || PtRelLepClosestJet[1] > 40)'
        cut += ' && (deltaR_lepClosestJet[2] > 0.4 || PtRelLepClosestJet[2] > 40)'
        cut += ' && (NJets_JetSubCalc >= '+str(cutList['njetsCut'])+')'
#       cut += ' && (('+wtagvar+' > 0 && NJets_JetSubCalc >= '+str(cutList['njetsCut'])+') || ('+wtagvar+' == 0 && NJets_JetSubCalc >= '+str(cutList['njetsCut']+1)+'))'                                                                    
        cut += ' && (NJetsCSVwithSF_JetSubCalc >= '+str(cutList['nbjetsCut'])+')'
#       cut += ' && DataPastTrigger == 1 && MCPastTrigger == 1'                                                                                                                                                                             
        if 'Data' in process: cut += ' && DataPastTrigger == 1'
        else: cut += ' && MCPastTrigger == 1'
#       cut += ' && (deltaR_lepJets[1] >= '+str(cutList['drCut'])+')'                                                                                                                                                                       
# 	cut += ' && (AK4HT > '+str(cutList['htCut'])+')'
# 	cut += ' && (AK4HTpMETpLepPt > '+str(cutList['stCut'])+')'

	if 'DataDrivenBkg' not in process:
		cut+=' && (AllLeptonIsTight_PtOrdered[0]==1 && AllLeptonIsTight_PtOrdered[1]==1 && AllLeptonIsTight_PtOrdered[2]==1)'
	print "Applying Cuts: ", cut
	
	isEM  = category['isEM']
	nttag = category['nttag']
	nWtag = category['nWtag']
	nbtag = category['nbtag']
	catStr = isEM+'_nT'+nttag+'_nW'+nWtag+'_nB'+nbtag
	
	hists = {}
	hists[discriminantName+'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	if doAllSys:
		if 'DataDrivenBkg' in process:
			hists[discriminantName+'PRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'PRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'PRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'PRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'FRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'FRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'FRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'FRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		else:
			hists[discriminantName+'pileupUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'pileupUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'pileupDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'pileupDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRFcorrdUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process]=R.TH1D(discriminantName+'muRFcorrdUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRFcorrdDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process]=R.TH1D(discriminantName+'muRFcorrdDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'muRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'muRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muFUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'muFUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'muFDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'muFDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'topptUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'topptUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'topptDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'topptDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jmrUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jmrUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jmrDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jmrDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jmsUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jmsUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jmsDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jmsDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'tau21Up'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'tau21Up'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'tau21Down' +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'tau21Down' +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jsfUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jsfUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[discriminantName+'jsfDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jsfDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)						
			if tTree[process+'jerUp']: 
				hists[discriminantName+'jerUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jerUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
				hists[discriminantName+'jerDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jerDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			if tTree[process+'jecUp']:
				hists[discriminantName+'jecUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jecUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
				hists[discriminantName+'jecDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'jecDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			if tTree[process+'btagUp']:
				hists[discriminantName+'btagUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'btagUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
				hists[discriminantName+'btagDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process]  = R.TH1D(discriminantName+'btagDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)						
			for i in range(100): hists[discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_is'+catStr+'_'+process] = R.TH1D(discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_is'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)				
	for key in hists.keys(): hists[key].Sumw2()
	
	jetSFstr = 'JetSF_pTNbwflat'
		
	if 'Data' in process: 
		if 'DataDrivenBkg' in process: 
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
		weightmuRUpStr      = '1'
		weightmuRDownStr    = '1'
		weightmuFUpStr      = '1'
		weightmuFDownStr    = '1'
		weighttopptUpStr    = '1'
		weighttopptDownStr  = '1'
		weightjsfUpStr      = '1'
		weightjsfDownStr    = '1'
	else: 
		weightStr           = jetSFstr+' * TrigEffWeight * pileupWeight * isoSF * lepIdSF * MCWeight_singleLepCalc/abs(MCWeight_singleLepCalc) * '+str(weight[process])
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
		weightjsfUpStr      = weightStr.replace('JetSF_pTNbwflat','JetSFupwide_pTNbwflat')
		weightjsfDownStr    = weightStr.replace('JetSF_pTNbwflat','JetSFdnwide_pTNbwflat')
		
# 	isEMCut=''
# 	if isEM=='E': isEMCut+=' && isElectron==1'
# 	elif isEM=='M': isEMCut+=' && isMuon==1'

	isLepCut=''
	if isEM=='EEE': isLepCut+=' && isEEE==1'
	if isEM=='EEM': isLepCut+=' && isEEM==1'
	if isEM=='EMM': isLepCut+=' && isEMM==1'
	if isEM=='MMM': isLepCut+=' && isMMM==1'

	
	nttagLJMETname = 'NJetsToptagged'
	nttagCut=''
	if 'p' in nttag: nttagCut+=' && '+nttagLJMETname+'>='+nttag[:-1]
	else: nttagCut+=' && '+nttagLJMETname+'=='+nttag
	if nttag=='0p': nttagCut=''
	
	nWtagLJMETname = 'NJetsWtagged_0p6'#'NJetsWtagged_JMR'
	if 'Data' in process: nWtagLJMETname = 'NJetsWtagged_0p6'#'NJetsWtagged'
	nWtagCut=''
	#nWtagCut+=' && (WJetLeadPt>'+str(cutList['Wjet1PtCut'])+' || '+nWtagLJMETname+'==0)'
	if 'p' in nWtag: nWtagCut+=' && '+nWtagLJMETname+'>='+nWtag[:-1]+' && NJets_JetSubCalc>='+str(cutList['njetsCut'])
	else: nWtagCut+=' && '+nWtagLJMETname+'=='+nWtag+' && NJets_JetSubCalc>='+str(cutList['njetsCut']+1)
	if nWtag=='0p': nWtagCut=''
	
	nbtagLJMETname = 'NJetsCSVwithSF_JetSubCalc'
	nbtagCut=''
	if 'p' in nbtag: nbtagCut+=' && '+nbtagLJMETname+'>='+nbtag[:-1]
	else: nbtagCut+=' && '+nbtagLJMETname+'=='+nbtag
	if nbtag=='0p': nbtagCut=''
	
	print 'Flavour: '+isEM+' #ttags: '+nttag+' #Wtags: '+nWtag+' #btags: '+nbtag
	print 'discriminantLJMETName: '+discriminantLJMETName
	print 'Cuts: '+cut+isLepCut+nttagCut+nWtagCut+nbtagCut
	
	tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
	if doAllSys:
		if 'DataDrivenBkg' in process: 
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'PRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightPRUpStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'PRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightPRDownStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'FRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightFRUpStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'FRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightFRDownStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
		else:
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pileupUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightPileupUpStr  +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pileupDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process, weightPileupDownStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRFcorrdUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuRFcorrdUpStr  +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRFcorrdDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuRFcorrdDownStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuRUpStr     +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muRDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuRDownStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muFUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuFUpStr     +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'muFDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightmuFDownStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'topptUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weighttopptUpStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'topptDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process, weighttopptDownStr +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jmrUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[0]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jmrDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[1]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jmsUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[2]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jmsDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[3]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'tau21Up'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[4]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'tau21Down' +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut.replace(nWtagLJMETname,'NJetsWtagged_0p6_shifts[5]')+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jsfUp'     +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightjsfUpStr     +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'jsfDown'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightjsfDownStr   +'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			if tTree[process+'jerUp']:
				tTree[process+'jerUp'].Draw(discriminantLJMETName   +' >> '+discriminantName+'jerUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
				tTree[process+'jerDown'].Draw(discriminantLJMETName +' >> '+discriminantName+'jerDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			if tTree[process+'jecUp']:
				tTree[process+'jecUp'].Draw(discriminantLJMETName   +' >> '+discriminantName+'jecUp'   +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
				tTree[process+'jecDown'].Draw(discriminantLJMETName +' >> '+discriminantName+'jecDown' +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			if tTree[process+'btagUp']:
				tTree[process+'btagUp'].Draw(discriminantLJMETName  +' >> '+discriminantName+'btagUp'  +'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
				tTree[process+'btagDown'].Draw(discriminantLJMETName+' >> '+discriminantName+'btagDown'+'_'+lumiStr+'fb_is'+catStr+'_'+process, weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')
			for i in range(100): tTree[process].Draw(discriminantLJMETName+' >> '+discriminantName+'pdf'+str(i)+'_'+lumiStr+'fb_is'+catStr+'_'+process, 'pdfWeights['+str(i)+'] * '+weightStr+'*('+cut+isLepCut+nttagCut+nWtagCut+nbtagCut+')', 'GOFF')

	if nbtag=='0' and discriminantName=='minMlb': discriminantLJMETName=originalLJMETName
			
	for key in hists.keys(): hists[key].SetDirectory(0)	
	return hists


