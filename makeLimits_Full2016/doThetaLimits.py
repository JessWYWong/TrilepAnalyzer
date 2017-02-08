import os,sys,fnmatch

# templateDir='/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer_80x/optimization_Full2016/optimization_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_withJECJER_2016_12_21/lep1Pt0_MET20_jetPt0_NJets3_NBJets0_HT0_ST600_mllOS20/'
# templateDir='/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer_80x/optimization_Full2016/optimization_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_withJECJER_2016_12_22/lep1Pt0_MET20_jetPt0_NJets3_NBJets0_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_2016_12_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST700_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_2016_12_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST800_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_2016_12_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST900_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_2016_12_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1000_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_2016_12_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1100_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST700_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST800_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST900_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1000_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets0_HT0_ST1100_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST800_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST900_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1000_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1100_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_moreThan2Jets_lepPt30_2017_1_30/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_moreThan2Jets_lepPt30_testing_2017_1_31/lep1Pt30_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST800_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST900_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1000_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_3Feb2017_step2_2017_2_3/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1100_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_6Feb2017_step2_2017_2_6/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_step2_2017_2_7/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST800_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_CorrectedLumiSYS_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_CorrectedLumiSYS_ALLsys_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/user_data/rsyarif/optimization_condor_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_CorrectedLumiSYS_ALLsys_ONEddbkgSYS_step2_2017_2_8/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'

# templateDir='/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer_80x/optimization_Full2016/optimization_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_CorrectedLumiSYS_ALLsys_step2_2017_2_8/lep1Pt0_MET20_jetPt0_NJets3_NBJets1_HT0_ST600_mllOS20/'

templateDir='/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer_80x/optimization_Full2016/optimization_80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_6Feb2017_newdbkgSys_CorrectedLumiSYS_ALLsys_oneDDBKGsys_step2_2017_2_8/lep1Pt0_MET20_jetPt0_NJets3_NBJets1_HT0_ST600_mllOS20/'


thetaConfigTemp = os.getcwd()+'/theta_config_template.py'

toFilter = ['pdf','muR','muF','muRFcorrd','muRFdecorrdNew','muRFenv','tau21','jmr','jms']
# toFilter = ['pdf','muR','muF','muRFcorrd','muRFdecorrdNew','muRFenv','tau21','jmr','jms','btag'] #filter btag!
# toFilter = []
# toFilter+= ['jec','jer']
toFilter = ['__'+item+'__' for item in toFilter]
toFilter += ['sig__pdfNew','sig__muRFcorrdNew']
print 'Filtering the following : ',toFilter

if not os.path.exists('/user_data/rsyarif/limits/'+templateDir.split('/')[-1]): os.system('mkdir /user_data/rsyarif/limits/'+templateDir.split('/')[-1]) #prevent writing these (they are large) to brux6 common area
# outputDir = '/user_data/rsyarif/limits/'+templateDir.split('/')[-1]+'/'
outputDir = '/user_data/rsyarif/limits/'
# limitType = '80x_noJEC_noJER_v3'
# limitType = '80x_withJECJER'
# limitType = '80x_withJECJER_condor'
# limitType = '80x_withJECJER_condor_FRv7_PRv2'
# limitType = '80x_Full2016_mcICHEP_fixedST_AllSYS'
# limitType = '80x_MultiLep_Full2016_mcICHEP_FRv15_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23_nobtagSys'
# limitType = '80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_20Jan2017_moreThan2Jets_muMinIso0p1_updatedbtagWP_2017_1_23'
# limitType = '80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_moreThan2Jets_lepPt30_2017_1_30'
# limitType = '80x_MultiLep_Full2016_mcICHEP_FRv15b_PRv4_step2_26Jan2017_moreThan2Jets_lepPt30_testing_2017_1_31'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_2017_2_3'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18b_2017_2_6'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_2017_2_7'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_newdbkgSys_2017_2_8'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_newdbkgSys_CorrectedLumiSYS_2017_2_8'
# limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_newdbkgSys_CorrectedLumiSYS_ALLsys_2017_2_8'
limitType = '80x_MultiLep_Full2016_Moriond17_newJEC_newElMVA_PRv6_FRv18bSys_newdbkgSys_CorrectedLumiSYS_ALLsys_oneDDBKGsys_2017_2_8'

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)
            
rootfilelist = []
i=0
for rootfile in findfiles(templateDir, '*.root'):
    #if 'TTM800' not in rootfile: continue
    #if 'TTM1800' in rootfile: continue
    #if 'TTM1700' in rootfile: continue
    #if 'TTM1600' in rootfile: continue
    #if 'TTM1500' in rootfile: continue
    #if 'TTM1400' in rootfile: continue
    rootfilelist.append(rootfile)
    i+=1

f = open(thetaConfigTemp, 'rU')
thetaConfigLines = f.readlines()
f.close()

def makeThetaConfig(rFile,outDir):
	rFileDir = rFile.split('/')[-2]
	with open(outDir+'/'+rFileDir+'/'+rFile.split('/')[-1][:-5]+'.py','w') as fout:
		for line in thetaConfigLines:
			if line.startswith('outDir ='): fout.write('outDir = \''+outDir+'/'+rFileDir+'\'')
			elif line.startswith('input ='): fout.write('input = \''+rFile+'\'')
			elif line.startswith('    model = build_model_from_rootfile('): 
				if len(toFilter)!=0:
					model='    model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s:  s.count(\''+toFilter[0]+'\')==0'
					for item in toFilter: 
						if item!=toFilter[0]: model+=' and s.count(\''+item+'\')==0'
					model+='))'
					fout.write(model)
				else: fout.write(line)
			else: fout.write(line)
	with open(outDir+'/'+rFileDir+'/'+rFile.split('/')[-1][:-5]+'.sh','w') as fout:
		fout.write('#!/bin/sh \n')
		fout.write('cd /home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/\n')
		fout.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
		fout.write('cmsenv\n')
		fout.write('cd '+outDir+'/'+rFileDir+'\n')
		fout.write('/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/theta/utils2/theta-auto.py ' + outDir+'/'+rFileDir+'/'+rFile.split('/')[-1][:-5]+'.py')

count=0
for file in rootfilelist:
	print file
	signal = file.split('/')[-1].split('_')[2]
	BRStr = file.split('/')[-1][file.split('/')[-1].find(signal)+len(signal):file.split('/')[-1].find('_36p814fb')]
	outDir = outputDir+limitType+BRStr+'/'
	print signal,BRStr
	if not os.path.exists(outDir): os.system('mkdir '+outDir)
	os.chdir(outDir)
	fileDir = file.split('/')[-2]
	#if os.path.exists(outDir+fileDir+'/'+file.split('/')[-1][:-5]+'.job'): continue
	if not os.path.exists(outDir+fileDir): os.system('mkdir '+fileDir)
	os.chdir(fileDir)
	makeThetaConfig(file,outDir)

	dict={'configdir':outDir+fileDir,'configfile':file.split('/')[-1][:-5]}

	jdf=open(file.split('/')[-1][:-5]+'.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(configfile)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Notification = Error
notify_user = rizki_syarif@brown.edu

arguments      = ""

Output = %(configfile)s.out
Error = %(configfile)s.err
Log = %(configfile)s.log

Queue 1"""%dict)
	jdf.close()

	os.system('chmod +x '+file.split('/')[-1][:-5]+'.sh')
	os.system('condor_submit '+file.split('/')[-1][:-5]+'.job')
	os.chdir('..')
	count+=1
print "Total number of jobs submitted:", count
                  
