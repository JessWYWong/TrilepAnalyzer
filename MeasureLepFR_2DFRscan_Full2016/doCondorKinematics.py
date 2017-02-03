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

pfix='kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet'


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
	'lepEta',
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
	'STrebinned',
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



                  
