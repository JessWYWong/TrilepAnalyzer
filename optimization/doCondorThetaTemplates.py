import os,sys,datetime,itertools

lepPtCutList  = [0]
jet1PtCutList = [0]
jet2PtCutList = [0]
metCutList    = [0]
njetsCutList  = [0,3]#1,2]
nbjetsCutList = [0,1]#,2,3]
jet3PtCutList = [0]
jet4PtCutList = [0]
jet5PtCutList = [0]
drCutList     = [0]
Wjet1PtCutList= [0]
bjet1PtCutList= [0]
htCutList     = [0]
stCutList     = [0,800,1100]#500,600,700,800,900,1000,1100]
minMlbCutList = [0]

cutConfigs = list(itertools.product(lepPtCutList,jet1PtCutList,jet2PtCutList,metCutList,njetsCutList,nbjetsCutList,jet3PtCutList,jet4PtCutList,jet5PtCutList,drCutList,Wjet1PtCutList,bjet1PtCutList,htCutList,stCutList,minMlbCutList))

thisDir = os.getcwd()
outputDir = thisDir+'/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templates_ST'
pfix+='_'+date#+'_'+time

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lepPtCut,jet1PtCut,jet2PtCut,metCut,njetsCut,nbjetsCut,jet3PtCut,jet4PtCut,jet5PtCut,drCut,Wjet1PtCut,bjet1PtCut,htCut,stCut,minMlbCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12],conf[13],conf[14]
	if not (len(jet1PtCutList)==1 and len(jet2PtCutList)==1 and len(jet3PtCutList)==1 and len(jet4PtCutList)==1 and len(jet5PtCutList)==1):
		if jet2PtCut >= jet1PtCut or jet3PtCut >= jet1PtCut or jet4PtCut >= jet1PtCut or jet5PtCut >= jet1PtCut: continue
		if jet3PtCut >= jet2PtCut or jet4PtCut >= jet2PtCut or jet5PtCut >= jet2PtCut: continue
		if (jet4PtCut >= jet3PtCut or jet5PtCut >= jet3PtCut) and jet3PtCut!=0: continue
		if jet5PtCut >= jet4PtCut and jet4PtCut!=0: continue
	cutString = 'lep'+str(int(lepPtCut))+'_MET'+str(int(metCut))+'_1jet'+str(int(jet1PtCut))+'_2jet'+str(int(jet2PtCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_3jet'+str(int(jet3PtCut))+'_4jet'+str(int(jet4PtCut))+'_5jet'+str(int(jet5PtCut))+'_DR'+str(drCut)+'_1Wjet'+str(Wjet1PtCut)+'_1bjet'+str(bjet1PtCut)+'_HT'+str(htCut)+'_ST'+str(stCut)+'_minMlb'+str(minMlbCut)
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'dir':outputDir,'lepPtCut':lepPtCut,'jet1PtCut':jet1PtCut,'jet2PtCut':jet2PtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'nbjetsCut':nbjetsCut,'jet3PtCut':jet3PtCut,
		  'jet4PtCut':jet4PtCut,'jet5PtCut':jet5PtCut,'drCut':drCut,'Wjet1PtCut':Wjet1PtCut,
		  'bjet1PtCut':bjet1PtCut,'htCut':htCut,'stCut':stCut,'minMlbCut':minMlbCut}

	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(dir)s/doCondorThetaTemplates.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(dir)s %(lepPtCut)s %(jet1PtCut)s %(jet2PtCut)s %(metCut)s %(njetsCut)s %(nbjetsCut)s %(jet3PtCut)s %(jet4PtCut)s %(jet5PtCut)s %(drCut)s %(Wjet1PtCut)s %(bjet1PtCut)s %(htCut)s %(stCut)s %(minMlbCut)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
