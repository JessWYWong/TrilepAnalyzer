import os,sys,datetime,itertools

lep1PtCutList = [0]
jetPtCutList  = [0]
metCutList    = [20]
njetsCutList  = [3]
nbjetsCutList = [0,1]
htCutList     = [0]
stCutList     = [0,500,600,700,800,900,1000,1100]
mllOSCutList  = [20]
isPassTriLeptonList= [1]
isPassTrig_dilepList= [1]

cutConfigs = list(itertools.product(lep1PtCutList,jetPtCutList,metCutList,njetsCutList,nbjetsCutList,htCutList,stCutList,mllOSCutList,isPassTriLeptonList,isPassTrig_dilepList))

thisDir = os.getcwd()
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
# pfix='optimization_80x_noJECnoJER'
# pfix='optimization_80x_withJECJER_condor'
pfix='optimization_80x_withJECJER_condor_FRv7_PRv2'

pfix+='_'+date#+'_'+time

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lep1PtCut,jetPtCut,metCut,njetsCut,nbjetsCut,htCut,stCut,mllOSCut,isPassTriLepton,isPassTrig_dilep=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9]
	cutString = 'lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(htCut)+'_ST'+str(stCut)+'_mllOS'+str(mllOSCut)
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'CMSSWBASE':relbase,'thisDir':thisDir,'lep1PtCut':lep1PtCut,'jetPtCut':jetPtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'nbjetsCut':nbjetsCut,
		  'htCut':htCut,'stCut':stCut,'mllOSCut':mllOSCut,'isPassTriLepton':isPassTriLepton,'isPassTrig_dilep':isPassTrig_dilep}

	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorThetaTemplates.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doThetaTemplates.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(CMSSWBASE)s %(lep1PtCut)s %(jetPtCut)s %(metCut)s %(njetsCut)s %(nbjetsCut)s %(htCut)s %(stCut)s %(mllOSCut)s %(isPassTriLepton)s %(isPassTrig_dilep)s 

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
