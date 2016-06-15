import os,sys,datetime

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
# pfix='kinematics_76in74x_condor_trilep_correctLumi'
# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi'
# pfix='kinematics_76in74x_condor_dilep_correctLumi'
# pfix='kinematics_76in74x_condor_dilep_2Dcut_correctLumi'

# pfix='kinematics_76in74x_condor_trilep_correctLumi_noJetSF_pTNbwflat'
# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat'
# pfix='kinematics_76in74x_condor_dilep_correctLumi_noJetSF_pTNbwflat'
# pfix='kinematics_76in74x_condor_dilep_2Dcut_correctLumi_noJetSF_pTNbwflat'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned'
# pfix='kinematics_76in74x_condor_dilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_OSsfl'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_mllOS20'
# pfix='kinematics_76in74x_condor_dilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_mllOS20'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_mllOS0'
# pfix='kinematics_76in74x_condor_dilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_mllOS0'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_OSsfl_TEST'

# pfix='kinematics_76in74x_condor_trilep_2Dcut_correctLumi_noJetSF_pTNbwflat_rebinned_OSsfl_TEST_2'

# pfix='kinematics_76in74x_condor_DEBUG_newMll_BJetCorr'
# pfix='kinematics_76in74x_condor_DEBUG_fixLooseLeps'
pfix='kinematics_76in74x_condor_DEBUG_fixLooseEl'


pfix+='_'+date
#pfix+='_'+date+'_'+time
# pfix+='_no_jsf'
# pfix+='_nbjets1_ST1100'

plotList = [#distribution name as defined in "doHists.py"
	'NPV',
	'lepPt',
	'lep1Pt',
	'lep2Pt',
	'lep3Pt',
	'lep1Eta',
	'lep2Eta',
	'lep3Eta',
 	'JetEta',
 	'Jet1Eta',
 	'Jet2Eta',
	'JetPt' ,
	'Jet1Pt',
	'Jet2Pt',
	'HT',
	'HTrebinned',
	'ST',
	'STrebinned',
	'MET',
	'METrebinned',
	'NJets' ,
	'NBJets',
	'NBJetsCorr',
	'mindeltaR',
	'mindeltaRB',
	'mindeltaR1',
	'mindeltaR2',
	'mindeltaR3',
	'lepCharge',
	'lepIso',
	'PtRel1',
	'PtRel2',
	'PtRel3',
	'MllsameFlavorOS',
	'MllOSall',
	'Mlll',
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
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py
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



                  
