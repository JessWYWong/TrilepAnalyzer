import os,sys,datetime,itertools

lepPtCutList  = [20]
lep1PtCutList = [50,75,100,150]
jetPtCutList  = [0]
jet1PtCutList = [0,50,100,150]
jet2PtCutList = [0,25,50]
metCutList    = [20,30]
njetsCutList  = [2,3]
nbjetsCutList = [0,1,2,3]
jet3PtCutList = [0]
jet4PtCutList = [0]
jet5PtCutList = [0]
drCutList     = [0]
Wjet1PtCutList= [0]
bjet1PtCutList= [0]
htCutList     = [200,300,400,500]
stCutList     = [0,500,800,1100,1150,1200,1250,1300]
minMlbCutList = [0]
mllOSCutList  = [20]

cutConfigs = list(itertools.product(lepPtCutList,lep1PtCutList,jetPtCutList,jet1PtCutList,jet2PtCutList,metCutList,njetsCutList,nbjetsCutList,jet3PtCutList,jet4PtCutList,jet5PtCutList,drCutList,Wjet1PtCutList,bjet1PtCutList,htCutList,stCutList,minMlbCutList,mllOSCutList))

thisDir = os.getcwd()
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
# pfix='optimization_76in74x_AllSys_trilep'
# pfix='optimization_76in74x_AllSys_dilep'
pfix='optimization_76in74x_AllSys_trilep_2Dcut_fixLepPt_mllOS'
# pfix='optimization_76in74x_AllSys_dilep_2Dcut_fixLepPt_mllOS'
pfix+='_'+date#+'_'+time

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lepPtCut,lep1PtCut,jetPtCut,jet1PtCut,jet2PtCut,metCut,njetsCut,nbjetsCut,jet3PtCut,jet4PtCut,jet5PtCut,drCut,Wjet1PtCut,bjet1PtCut,htCut,stCut,minMlbCut,mllOSCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12],conf[13],conf[14],conf[15],conf[16],conf[17]
	if not (len(jet1PtCutList)==1 and len(jet2PtCutList)==1 and len(jet3PtCutList)==1 and len(jet4PtCutList)==1 and len(jet5PtCutList)==1):
		if jet2PtCut >= jet1PtCut or jet3PtCut >= jet1PtCut or jet4PtCut >= jet1PtCut or jet5PtCut >= jet1PtCut: continue
		if jet3PtCut >= jet2PtCut or jet4PtCut >= jet2PtCut or jet5PtCut >= jet2PtCut: continue
		if (jet4PtCut >= jet3PtCut or jet5PtCut >= jet3PtCut) and jet3PtCut!=0: continue
		if jet5PtCut >= jet4PtCut and jet4PtCut!=0: continue
	cutString = 'lepPt'+str(int(lepPtCut))+'_lep1Pt'+str(int(lep1PtCut))+'_MET'+str(int(metCut))+'_jet1Pt'+str(int(jet1PtCut))+'_jet2Pt'+str(int(jet2PtCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_jet3Pt'+str(int(jet3PtCut))+'_jet4Pt'+str(int(jet4PtCut))+'_jet5Pt'+str(int(jet5PtCut))+'_DR'+str(drCut)+'_1Wjet'+str(Wjet1PtCut)+'_1bjet'+str(bjet1PtCut)+'_HT'+str(htCut)+'_ST'+str(stCut)+'_minMlb'+str(minMlbCut)+'_mllOS'+str(mllOSCut)
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'CMSSWBASE':relbase,'thisDir':thisDir,'lepPtCut':lepPtCut,'lep1PtCut':lep1PtCut,'jetPtCut':jetPtCut,'jet1PtCut':jet1PtCut,'jet2PtCut':jet2PtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'nbjetsCut':nbjetsCut,'jet3PtCut':jet3PtCut,
		  'jet4PtCut':jet4PtCut,'jet5PtCut':jet5PtCut,'drCut':drCut,'Wjet1PtCut':Wjet1PtCut,
		  'bjet1PtCut':bjet1PtCut,'htCut':htCut,'stCut':stCut,'minMlbCut':minMlbCut,'mllOSCut':mllOSCut}

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
Arguments = %(CMSSWBASE)s %(lepPtCut)s %(lep1PtCut)s %(jetPtCut)s %(jet1PtCut)s %(jet2PtCut)s %(metCut)s %(njetsCut)s %(nbjetsCut)s %(jet3PtCut)s %(jet4PtCut)s %(jet5PtCut)s %(drCut)s %(Wjet1PtCut)s %(bjet1PtCut)s %(htCut)s %(stCut)s %(minMlbCut)s %(mllOSCut)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
