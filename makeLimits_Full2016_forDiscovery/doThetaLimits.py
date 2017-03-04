import os,sys,fnmatch

templateDir = '/user_data/rsyarif/'

# templateDir+='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumiSYS_fixedLepIdIsoSys_ALLsys_step2_TESTING_2017_2_15/'
# templateDir+='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_ALLsys_step2_addbMistag_addMoreSignal_2017_2_16/'
# templateDir+='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_ALLsys_step2_addmistag_addMoreSignal_2017_2_17/'
# templateDir+='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_newMllOScut_fixedAllSYS_step2_addmistag_addMoreSignal_2017_2_23/'
templateDir+='optimization_condor_PRv6_FRv20b_newMllOSV2_Allsys_2017_3_1/'

limitType = templateDir.split('/')[-2]

templateDir+='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST600_mllOS20/'
# templateDir='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST700_mllOS20/'
# templateDir='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST800_mllOS20/'
# templateDir='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST900_mllOS20/'
# templateDir='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1000_mllOS20/'
# templateDir='lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST1100_mllOS20/'

# templateDir+='4binsCount_updatedLumi_updatedLepIdUnc_addbmistag_normRENORMPDF/'
# templateDir+='4binsCount_updatedLumi_updatedLepIdUnc_addmistag_normRENORMPDF/'
# templateDir+='4binsCount_newMllOScut/'
templateDir+='4binsCount/'
print "Checking:", templateDir


outputDir = '/user_data/rsyarif/limits/'


lumiStr = '35p867'

# thetaConfigTemp = os.getcwd()+'/theta_config_template.py'
thetaConfigTemp = os.getcwd()+'/theta_discovery_optimization.py'

toFilter = ['pdf','muR','muF','muRFcorrd','muRFdecorrdNew','muRFenv','tau21','jmr','jms']
# toFilter = ['pdf','muR','muF','muRFcorrd','muRFdecorrdNew','muRFenv','tau21','jmr','jms','btag'] #filter btag!
# toFilter = []
# toFilter+= ['jec','jer']
toFilter = ['__'+item+'__' for item in toFilter]
# toFilter += ['sig__pdfNew','sig__muRFcorrdNew']
print 'Filtering the following : ',toFilter


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
	print ''
	print 'file   : ',file
	signal = file.split('/')[-1].split('_')[2]
	BRStr = file.split('/')[-1][file.split('/')[-1].find(signal)+len(signal):file.split('/')[-1].find('_'+lumiStr+'fb')]
	outDir = outputDir+limitType+BRStr+'/'
	print 'signal : ',signal,BRStr
# 	print 'outDir : ',outDir
	if not os.path.exists(outDir): os.system('mkdir -v '+outDir)
	outDir+='/'+templateDir.split('/')[-3]
	if not os.path.exists(outDir): os.system('mkdir -v '+outDir)
# 	print 'outDir : ',outDir
# 	print 'pwd:',os.getcwd()
	os.chdir(outDir)
# 	print 'pwd:',os.getcwd()
	fileDir = '/'+file.split('/')[-2]
	#if os.path.exists(outDir+fileDir+'/'+file.split('/')[-1][:-5]+'.job'): continue
# 	print 'outDir+fileDir:',outDir+fileDir
	if not os.path.exists(outDir+fileDir): os.system('mkdir -v '+outDir+fileDir)
	os.chdir(outDir+fileDir)
# 	print 'fileDir: ',fileDir
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
                  