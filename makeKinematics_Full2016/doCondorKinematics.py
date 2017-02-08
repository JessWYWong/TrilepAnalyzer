import os,sys,datetime

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_FRv7_PRv2_step2_moreThan2Jets_AllSYS'
# 
# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_mcICHEP_IsoTrig_FRv7_PRv2_step2_exactly2Jets_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv7_PRv2_step2_moreThan2Jets_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv7_PRv2_step2_moreThan2Jets_fixedST_AllSYS'

# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv7_PRv2_step2_exactly2Jets_fixedST_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv8_PRv2_step2_moreThan2Jets_fixedST_looseLepjetClean_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv9_PRv2_step2_moreThan2Jets_fixedST_looseLepjetClean_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv11_PRv3_ClintsAN16-242_step2_moreThan2Jets_fixedST_looseLepjetClean_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_addDZforRunH_FRv10_PRv2_step2_moreThan2Jets_fixedST_looseLepjetClean_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_HLTupdate_FRv9_PRv2_step2_moreThan2Jets_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_HLTupdate_FRv9_PRv2_step2_exactly2Jets_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_HLTupdate_FRv12_PRv2_step2_moreThan2Jets_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_HLTupdate_FRv13_PRv2_step2_moreThan2Jets_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_IsoTrig_HLTupdate_FRv12_PRv2_step2_exactly1Jet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv14a_PRv4_step2_20Jan2017_moreThan2Jets_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv14a_PRv4_step2_20Jan2017_exactly2Jets_AllSYS'

# pfix='kinematics_80x_condor_MoreThan3Lep_Full2016_mcICHEP_FRv14a_PRv4_step2_20Jan2017_moreThan2Jets_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv14a_PRv4_step2_20Jan2017_moreThan2Jets_noMllOScut_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv14a_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p2_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_exactly2Jets_muMinIso0p1_updatedbtagWP_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_exactly2Jets_muMinIso0p1_updatedbtagWP_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_1bjet_lepPt30_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_1bjet_lepPt30_altBinning_AllSYS'

# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_exactly2Jets_muMinIso0p1_updatedbtagWP_1bjet_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_mcICHEP_FRv15b_PRv5test_step2_26Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_1bjet_lepPt30_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv17b_PRv6_step2_moreThan2Jets_1bjet_noSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv17b_PRv6_step2_moreThan2Jets_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18b_PRv6_step2_moreThan2Jets_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18b_PRv6_step2_exactly2Jets_1bjet_AllSYS'

# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_Moriond17_FRv18b_PRv6_step2_exactly2Jets_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18b_PRv6_step2_moreThan2Jets_1bjet_AllSYS_ST600'

# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_Moriond17_FRv18b_PRv6_step2_exactly1Jet_1bjet_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18bSys_PRv6_step2_moreThan2Jets_1bjet_bTagSysFixed_addFRsys_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18bSys_PRv6_step2_exactly2Jets_1bjet_bTagSysFixed_addFRsys_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv19test_PRv6_step2_moreThan2Jets_1bjet_muFRetaDependence_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv19test_PRv6_step2_moreThan2Jets_1bjet_muFRetaDependence_noSYS_ST600'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18bSys_PRv6_step2_moreThan2Jets_1bjet_bTagSysFixed_addFRsys_AllSYS_ST600'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv19test_PRv6_step2_moreThan2Jets_1bjet_muFRetaDependence_noSYS_ST600'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv19test_PRv6_step2_moreThan2Jets_1bjet_muFRetaDependence_AllSYS'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_FRv18bSys_PRv7test_step2_moreThan2Jets_1bjet_noSYS_ST600'

# pfix='kinematics_80x_condor_MultiLep_Full2016_Moriond17_noSYS_noDDBKG'

# pfix='kinematics_80x_condor_Exactly3Lep_Full2016_Moriond17_FRv18bSys_PRv6_step2_exactly2Jets_1bjet_AllSYS'

pfix='kinematics_80x_condor_Exactly3Lep_Full2016_Moriond17_FRv18bSys_PRv6_step2_exactly1Jet_1bjet_AllSYS'

pfix+='_'+date
#pfix+='_'+date+'_'+time
# pfix+='_no_jsf'

plotList = [#distribution name as defined in "doHists.py"
	'NPV',
	'lepPt',
	'ElPt',
	'MuPt',

# 	'lep1Pt',
# 	'lep2Pt',
# 	'lep3Pt',

	'lepEta',
	'ElEta',
	'MuEta',

# 	'lep1Eta',
# 	'lep2Eta',
# 	'lep3Eta',

 	'JetEta',

#  	'Jet1Eta',
#  	'Jet2Eta',

	'JetPt' ,

# 	'Jet1Pt',
# 	'Jet2Pt',

	'HT',
	'HTrebinned',
	'ST',
	'STrebinned',
	'MET',
	'METrebinned',
	'NJets' ,
	'NBJets',
	'NBJetsCorr',

# 	'mindeltaRlepJets',
# 	'mindeltaRlep1Jets',
# 	'mindeltaRlep2Jets',
# 	'mindeltaRlep3Jets',
# 	'mindeltaRB',
# 	'mindeltaR1',
# 	'mindeltaR2',
# 	'mindeltaR3',
# 	'lepCharge',

	'lepIso',
	'ElIso',
	'MuIso',

# 	'PtRel1',
# 	'PtRel2',
# 	'PtRel3',

# 	'MllsameFlavorOS',
# 	'MllOSall',
	'MllOSallmin',
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



                  
