cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, 
		   'leadJetPtCut':0,
		   'subLeadJetPtCut':0, 
		   'thirdJetPtCut':0,
		   'metCut': 20,
		   'njetsCut': 2, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
                   #'MuEtaCut':0.4, #0.4,0.9,1.2,2.1,2.4
		   }

cutString = 'isPassTrig_All'+str(int(cutList['isPassTrig']))+'_'+'dilep'+str(int(cutList['isPassTrig_dilep']))+'_'+'dilepAnth'+str(int(cutList['isPassTrig_dilep_anth']))+'_'+'trilep'+str(int(cutList['isPassTrig_trilep']))+'_'+'isPassTrilepton'+str(int(cutList['isPassTrilepton']))+'_lepPt'+str(int(cutList['lepPtCut']))+'_NJets'+str(int(cutList['njetsCut']))+'_NBJets'+str(int(cutList['nbjetsCut']))+'_DR'+str(int(cutList['drCut']))+'_ST'+str(int(cutList['stCut']))+'_MllOS'+str(int(cutList['mllOSCut']))+'_HT'+str(int(cutList['htCut']))+'_Mlllb'+str(int(cutList['mlllbCut']))#+'_MuEta'+str(int(cutList['MuEtaCut']))
