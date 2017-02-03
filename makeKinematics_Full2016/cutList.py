#!/usr/bin/python

cutList_ = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 0,
		   'isPassTrig_dilepHT': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 0,
		   'lepPtCut': 0, #40, #0, #
		   'leadJetPtCut':0, #150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 0,#60, #75, #0, #
		   'njetsCut': 0, 
		   'nbjetsCut':0, #1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,#1100,
		   }

cutString_ = 'isPassTrig'+str(int(cutList_['isPassTrig']))+'_'+'isPassTrig_dilep'+str(int(cutList_['isPassTrig_dilep']))+'_'+'isPassTrig_dilepHT'+str(int(cutList_['isPassTrig_dilepHT']))+'_'+'isPassTrig_trilep'+str(int(cutList_['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList_['isPassTrilepton']))+'_'+'lep'+str(int(cutList_['lepPtCut']))+'_NJets'+str(int(cutList_['njetsCut']))+'_NBJets'+str(int(cutList_['nbjetsCut']))+'_DR'+str(int(cutList_['drCut']))+'_ST'+str(int(cutList_['stCut']))
