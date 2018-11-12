import os,sys,datetime

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)


# pfix='kinematics_80x_condor_Exactly3Lep_no2Dcut_dilepTrigReady_fixedSF_mllOSmin20_FRv3_step2_v2'

# pfix='kinematics_80x_condor_Exactly3Lep_no2Dcut_dilepTrigReady_fixedSF_mllOSmin20_FRv3_step2_v2_moreThan2Jets'

# pfix='kinematics_80x_condor_Exactly3Lep_no2Dcut_dilepTrigReady_fixedSF_mllOSmin20_FRv3_step2_v2_exactly2Jets'

# pfix='kinematics_80x_condor_Exactly3Lep_no2Dcut_dilepTrigReady_fixedSF_mllOSmin20_FRv3_step2_v2_exactly1Jet'

# pfix='kinematics_80x_condor_Exactly3Lep_no2Dcut_dilepTrigReady_fixedSF_mllOSmin20_FRv3_step2_v2_1or2Jets'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta1p2'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta1p2to2p1'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_eta2p1to2p4'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2to2p1'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta2p1to2p4'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta1p2to2p1'
# 
# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_eta2p1to2p4'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv5test_muMinIso0p1_Full2016_26Jan2017_updatedbtagWP_1bjet_lepPt30'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv7test_1bjet'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv8test_1bjet'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet_newMllOS_fixedlumi'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet_newMllOS_fixedlumi'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet_newMllOS_fixedlumi_oriBin'

# pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet_newMllOS_fixedlumi'

# pfix='kinematics_condor_ddbkgscan_PRv6_1Mar2017_scaleFRforCR1_step1hadds_step2_FRCR1'

# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_FRCR2'

# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_FRCR1'

# pfix='kinematics_condor_ddbkgscan_PRv6_2Mar2017_take2_scaleFRforCR1_step1hadds_step2_FRCR1'
# pfix='kinematics_condor_ddbkgscan_PRv6_3Mar2017_scaleFR_CR2CR1_step1hadds_step2_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv6_3Mar2017_scaleFR_CR2SR_step1hadds_step2_FRCR2'

# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR1'

# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR2_nobjet'
# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR1_nobjet'

# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR1CR2'
# pfix='kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR1CR2_nobjet'

# pfix='kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR1'
# pfix='kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR1CR2'

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR1'
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR1CR2'

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1'
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1CR2'

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRST1000low'

# pfix='kinematics_condor_ddbkgscan_PRv10_newRunH_correctedMuTrSF_FRCR2'
# pfix='kinematics_condor_ddbkgscan_PRv10_newRunH_correctedMuTrSF_FRCR1'

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT600low' #remember to modify analyse.py for low hT
'''
cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, #40, #0, #
		   'leadJetPtCut':0,#150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 20,#60, #75, #0, #
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':600,
		   }
'''
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2HT600low' #remember to modify analyse.py for low hT
'''
cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, #40, #0, #
		   'leadJetPtCut':0,#150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 20,#60, #75, #0, #
		   'njetsCut': 2, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':600,
		   }
'''
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1HT600low' #remember to modify analyse.py for low hT
'''
cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, #40, #0, #
		   'leadJetPtCut':0,#150, #300, #0, #
		   'subLeadJetPtCut':0, #75, #150, #0, #
		   'thirdJetPtCut':0, #30, #100, #0, #
		   'metCut': 20,#60, #75, #0, #
		   'njetsCut': 1, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':600,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRmlllb400low' #remember to modify analyse.py for SR, ST HT set to defaults, mlllb low
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':400,
		   }
'''
# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2mlllb400low' #remember to modify analyse.py for SR, ST HT set to defaults, mlllb low
'''
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
	   	   'mlllbCut':400,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_2Dcut' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_2Dcut_extend' #scan FR 0.01 to 1.0 #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2HT400low_2Dcut_extend' #scan FR 0.01 to 1.0 #remember to modify analyse.py for low hT, njets and cutList.py!
'''
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
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1HT400low_2Dcut_extend' #scan FR 0.01 to 1.0 #remember to modify analyse.py for low hT, njets and cutList.py!
'''
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
		   'njetsCut': 1, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2_2Dcut_extend' #scan FR 0.01 to 1.0 #remember to modify analyse.py for low hT, njets and cutList.py!
'''
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
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1_2Dcut_extend' #scan FR 0.01 to 1.0 #remember to modify analyse.py for low hT, njets and cutList.py!
'''
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
		   'njetsCut': 1, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0.2,
	   	   'ptRelCut':10,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRSRHT400low' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR2' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRSRHT400' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
'''

# pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRSR' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 3, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
'''

pfix='kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR1' #remember to modify analyse.py for low hT and cutList.py!
'''
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
		   'njetsCut': 1, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
'''


pfix+='_'+date
#pfix+='_'+date+'_'+time
# pfix+='_no_jsf'

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
#  	'JetEta',
#  	'Jet1Eta',
#  	'Jet2Eta',
# 	'JetPt' ,
# 	'Jet1Pt',
# 	'Jet2Pt',
# 	'HT',
# 	'HTrebinned',
# 	'ST',
# 	'STrebinned',
# 	'MET',
# 	'METrebinned',
# 	'NJets' ,
# 	'NBJets',
# 	'NBJetsCorr',
# 	'mindeltaRlepJets',
# 	'mindeltaRlep1Jets',
# 	'mindeltaRlep2Jets',
# 	'mindeltaRlep3Jets',
# 	'mindeltaRB',
# 	'mindeltaR1',
# 	'mindeltaR2',
# 	'mindeltaR3',
# 	'lepCharge',
# 	'lepIso',
# 	'ElIso',
# 	'MuIso',
# 	'PtRel1',
# 	'PtRel2',
# 	'PtRel3',
# 	'MllsameFlavorOS',
# 	'MllOSall',
# 	'MllOSallmin',
# 	'Mlll',
	]

catList = ['EEE','EEM','EMM','MMM','All']

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.chdir(outDir)

count = 0
for distribution in plotList:
	for cat in catList:
		print cat
		if not os.path.exists(outDir+'/'+cat): os.system('mkdir '+cat)
		os.chdir(cat)
		
# 		dict={'dir':outputDir,'dist':distribution,'cat':cat}
# 		dict={'dir':thisDir,'dist':distribution,'cat':cat}
# 		dict={'CMSSWBASE':relbase,'dir':outputDir,'dist':distribution,'cat':cat}
		dict={'CMSSWBASE':relbase,'thisDir':thisDir,'dist':distribution,'cat':cat}


		jdf=open('condor_'+distribution+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorKinematics.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py,%(thisDir)s/cutList.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor_%(dist)s.out
Error = condor_%(dist)s.err
Log = condor_%(dist)s.log
Notification = Error
Arguments = %(CMSSWBASE)s %(dist)s %(cat)s

Queue 1"""%dict)
		jdf.close()

		os.system('condor_submit condor_'+distribution+'.job')
		os.chdir('..')
		count+=1
									
print "Total jobs submitted:", count



                  
