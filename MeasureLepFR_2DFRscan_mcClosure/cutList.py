
cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, #40, #0, #
		   'leadJetPtCut':0,#150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 0,#60, #75, #0, #
		   'njetsCut': 0, 
		   'nbjetsCut':0,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':0,
		   }

cutString = 'isPassTrig_All'+str(int(cutList['isPassTrig']))+'_'+'dilep'+str(int(cutList['isPassTrig_dilep']))+'_'+'dilepAnth'+str(int(cutList['isPassTrig_dilep_anth']))+'_'+'trilep'+str(int(cutList['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList['isPassTrilepton']))+'_lepPt'+str(int(cutList['lepPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))+'_MllOS'+str(int(cutList['mllOSCut']))
