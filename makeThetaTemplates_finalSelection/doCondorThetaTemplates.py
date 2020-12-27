import os,sys,datetime,itertools

lep1PtCutList = [0]
#lep1PtCutList = [30,50,100,200]
jetPtCutList  = [0]
#jetPtCutList  = [30,50,100,150,200,250,300]
metCutList    = [20]
#metCutList    = [20,40,60,80,100,200]
njetsCutList  = [3]
bJet1PtCutList = [0]
bJet1PtCutList = [0,30,38,40,42,45,48,50,52,55,58,60,62,65,68,70,72,75,78,80]
nbjetsCutList = [1]
htCutList     = [0]#,100,200]
#htCutList     = [0,100,200]
stCutList     = [0] #,600,700,800,900,1000,1100]
#stCutList     = [200,400,600,700,800,900,1000,1100]
mllOSCutList  = [20]#,25,30,50,100]
#mllOSCutList  = [20,25,30,50,100]
isPassTriLeptonList= [1]
isPassTrig_dilepList= [1]
ptRelCutList = [0]
#ptRelCutList = [0,4,6,8,10,12,14,16,20]
minDRlepJetCutList = [0.0]#,0.25,0.5,0.75,1.0]
#minDRlepJetCutList = [0.0,0.25,0.5,0.75,1.0]

cutConfigs = list(itertools.product(lep1PtCutList,jetPtCutList,metCutList,njetsCutList,bJet1PtCutList,nbjetsCutList,htCutList,stCutList,mllOSCutList,isPassTriLeptonList,isPassTrig_dilepList,ptRelCutList,minDRlepJetCutList))

thisDir = os.getcwd()
#relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
#outputDir = '/user_data/rsyarif/'
relbase = '/home/wwong/VLQ/CMSSW_10_2_10/src/'
outputDir = '/mnt/data/users/wwong/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)


# pfix='LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds_step2_templates'
#pfix='LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds_step2_templates'
pfix='FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_hadds_step2_templates'


if len(sys.argv)>1: pfix=str(sys.argv[1])

pfix+='_'+date#+'_'+time


outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lep1PtCut,jetPtCut,metCut,njetsCut,bJet1PtCut,nbjetsCut,htCut,stCut,mllOSCut,isPassTriLepton,isPassTrig_dilep,ptRelCut,minDRlepJetCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12]
        if njetsCut>=3:
            cutString = 'lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_bJet1Pt'+str(int(bJet1PtCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(htCut)+'_ST'+str(stCut)+'_mllOS'+str(mllOSCut)+'_ptRel'+str(int(ptRelCut))+'_minDRlJ'+str(minDRlepJetCut).replace('.','p')
        else:
	    cutString = 'lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(htCut)+'_ST'+str(stCut)+'_mllOS'+str(mllOSCut)+'_ptRel'+str(int(ptRelCut))+'_minDRlJ'+str(minDRlepJetCut).replace('.','p')
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'CMSSWBASE':relbase,'outDir':outDir,'thisDir':thisDir,'lep1PtCut':lep1PtCut,'jetPtCut':jetPtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'bJet1PtCut':bJet1PtCut,'nbjetsCut':nbjetsCut,
		  'htCut':htCut,'stCut':stCut,'mllOSCut':mllOSCut,'isPassTriLepton':isPassTriLepton,'isPassTrig_dilep':isPassTrig_dilep,
		  'ptRelCut':ptRelCut,'minDRlepJetCut':minDRlepJetCut}

	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorThetaTemplates.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(CMSSWBASE)s %(lep1PtCut)s %(jetPtCut)s %(metCut)s %(njetsCut)s %(bJet1PtCut)s %(nbjetsCut)s %(htCut)s %(stCut)s %(mllOSCut)s %(isPassTriLepton)s %(isPassTrig_dilep)s %(ptRelCut)s %(minDRlepJetCut)s %(outDir)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
