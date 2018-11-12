import os,sys,datetime

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

# pfix='kinematics_condor_ddbkgscan_PRv6_FRv28ttbar_ttbarClosure_saveVeryLoose'
# pfix='kinematics_condor_ddbkgscan_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_ttbarClosure'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure'
# pfix='kinematics_condor_ddbkgscan_zjetsClosure'
# pfix='kinematics_condor_ddbkgscan_ttbarClosure_fixedBug'
# pfix='kinematics_condor_NOddbkgscan_ttbarClosure_fixedBug'

# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug' 
"""
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

"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_SR'
""" 
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
		   'njetsCut': 3, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_CR2'
"""
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
		   'njetsCut': 2, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_CR1'
"""
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
		   'njetsCut': 1, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
		   }
"""

# pfix='kinematics_condor_FULLddbkgscan_DYClosure' 
"""
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
"""
# pfix='kinematics_condor_FULLddbkgscan_DYClosure_SR' 
""" 
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
		   'njetsCut': 3, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_DYClosure_CR2' 
"""
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
		   'njetsCut': 2, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
		   }
"""

# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35' 
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv36' 
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv37' 
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv38' 
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_fixedBug_PRv9_FRv35a' #--> double checking but also with muFR=.14instead of .13 in FRv35
"""
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

"""

# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SR' #remember to modify analyse.py for low hT and cutList.py and samples.py!
""" 
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
		   'njetsCut': 3, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_CR2' #remember to modify analyse.py for Njets==2 and for low hT and cutList.py  and samples.py!
"""
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
		   'njetsCut': 2, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400' #remember to modify analyse.py for low hT and cutList.py and samples.py!
"""
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
		   'njetsCut': 3, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_SRHT400low' #remember to modify analyse.py for low hT and cutList.py and samples.py!
"""
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
		   'njetsCut': 3, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':400,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""
# pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix' #remember to modify analyse.py for low hT and cutList.py and samples.py!
"""
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
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""
pfix='kinematics_condor_FULLddbkgscan_ttbarClosure_PRv9_FRv48_elMVAvalueFix_CR1' #remember to modify analyse.py for Njets==1 and for low hT and cutList.py  and samples.py!
"""
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
		   'njetsCut': 1, 
		   'nbjetsCut':1,
		   'drCut':0, #1.0, #
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
"""


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



                  
