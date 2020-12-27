import os,sys,fnmatch

templateDir = '/mnt/data/users/wwong/'

limitType = templateDir.split('/')[-2]

if len(sys.argv)>1: 
	templateDir+=sys.argv[1]+'/'
	limitType = sys.argv[1].split('/')[0]


if len(sys.argv)>2: 
	templateDir+=sys.argv[2]+'/'


#if len(sys.argv)>3: 
#	templateDir+=sys.argv[3]+'/'

print "Checking:", templateDir


outSubDir=''
if len(sys.argv)>3: 
	outSubDir=sys.argv[3]


outputDir = '/mnt/data/users/wwong/limits/'


lumiStr = '59p74'

thetaConfigTemp = os.getcwd()+'/theta_config_template.py'

########## unused syst ##########
toFilter = ['muR__','muF__','muRFcorrd__','elPR__','muPR__','elFR__','muFR__']
################################
########## filter rate ##########
toFilter += ['elIsoSys__','muIsoSys__','muIdSys__','FRSys__','elPRsys__','muFReta__','muPRsys__']
################################
########## filter shape ##########
#toFilter += ['pileup','btag','mistag','pdfNew','muR','muF','muRFcorrd','muRFcorrdNew','jec','jer',"TrigEffWeight", "elIdSys"]
################################

testFilter = []
#testFilter = ['FRSys__']
#testFilter = ['muFReta__']
#testFilter = ['muRFcorrdNew']
toFilter += testFilter
toFilter = [item for item in toFilter]
print 'Filtering the following : ',toFilter


def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)
            
rootfilelist = []
i=0
for rootfile in findfiles(templateDir, '*.root'):
    #if 'BBM900' not in rootfile: continue
    #if 'TTM1800' in rootfile: continue
    #if 'TTM1700' in rootfile: continue
    #if 'TTM1600' in rootfile: continue
    #if 'TTM1500' in rootfile: continue
    #if 'TTM1400' in rootfile: continue
    #if len(sys.argv)>4 and not sys.argv[4] in rootfile: continue
    rootfilelist.append(rootfile)
    i+=1

f = open(thetaConfigTemp, 'rU')
thetaConfigLines = f.readlines()
f.close()

def makeThetaConfig(rFile,outDir):
# 	rFileDir = rFile.split('/')[-2]
	rFileDir = outSubDir+"/"
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
		fout.write('cd /home/wwong/VLQ/THETA/CMSSW_7_6_3/src/\n')
#                fout.write('cd /home/wwong/VLQ/THETA/CMSSW_8_0_24/src/\n')
		fout.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
		fout.write('cmsenv\n')
		fout.write('cd '+outDir+'/'+rFileDir+'\n')
#                fout.write('/home/wwong/VLQ/THETA/CMSSW_8_0_24/src/theta/utils2/theta-auto.py ' + outDir+'/'+rFileDir+'/'+rFile.split('/')[-1][:-5]+'.py')
		fout.write('/home/wwong/VLQ/THETA/CMSSW_7_6_3/src/theta/utils2/theta-auto.py ' + outDir+'/'+rFileDir+'/'+rFile.split('/')[-1][:-5]+'.py')

if len(testFilter)> 0:
    for filtered in testFilter:
        outSubDir+="_"+filtered
outSubDir += "/"
count=0
for file in rootfilelist:
	print ''
	print 'file   : ',file
	signal = file.split('/')[-1].split('_')[2]
	BRStr = file.split('/')[-1][file.split('/')[-1].find(signal)+len(signal):file.split('/')[-1].find('_'+lumiStr+'fb')]
	if not('_BB' in sys.argv[1]):
		if not('_bW0p5_tZ0p25_tH0p25' in BRStr or '_bW0p0_tZ0p5_tH0p5' in BRStr or '_bW0p0_tZ1p0_tH0p0' in BRStr): 
			print '--> Skipping'
			continue
	if ('_BB' in sys.argv[1]):
		if not('_tW0p5_bZ0p25_bH0p25' in BRStr or '_tW0p0_bZ0p5_bH0p5' in BRStr or '_tW1p0_bZ0p0_bH0p0' in BRStr): 
			print '--> Skipping'
			continue
        outDir = outputDir
        if not os.path.exists(outDir): os.system('mkdir -v -p '+outDir)
	#outDir = outputDir+limitType+BRStr+'/'
        outDir +=limitType+BRStr+'/'
	print 'signal : ',signal,BRStr
# 	if not ('M800' in signal or 'M1000' in signal): continue
 	print 'outDir : ',outDir
	if not os.path.exists(outDir): os.system('mkdir -v -p '+outDir)
	outDir+='/'+templateDir.split('/')[-3]
	if not os.path.exists(outDir): os.system('mkdir -v -p '+outDir)
# 	print 'outDir : ',outDir
# 	print 'pwd:',os.getcwd()
	os.chdir(outDir)
# 	print 'pwd:',os.getcwd()
	fileDir = '/'+file.split('/')[-2]
# 	fileDir = '/'+outSubDir
	#if os.path.exists(outDir+fileDir+'/'+file.split('/')[-1][:-5]+'.job'): continue
# 	print 'outDir+fileDir:',outDir+fileDir
# 	if not os.path.exists(outDir+fileDir): os.system('mkdir -v '+outDir+fileDir)
# 	os.chdir(outDir+fileDir)
# 	print 'fileDir: ',fileDir
	print 'outDir : ',outDir+'/'+outSubDir
	if not os.path.exists(outDir+'/'+outSubDir): os.system('mkdir -v '+outDir+'/'+outSubDir)
	os.chdir(outDir+'/'+outSubDir)
	makeThetaConfig(file,outDir)

	dict={'configdir':outDir+fileDir,'configfile':file.split('/')[-1][:-5]}

	jdf=open(file.split('/')[-1][:-5]+'.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(configfile)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Notification = Error

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
                  
