import os,sys,datetime,itertools

lep1PtCutList = [0]
jetPtCutList  = [0]
metCutList    = [20]
njetsCutList  = [3]
nbjetsCutList = [1]
htCutList     = [400]
stCutList     = [0]#600,700,800,900,1000,1100]
mllOSCutList  = [20]
isPassTriLeptonList= [1]
isPassTrig_dilepList= [1]
ptRelCutList = [0]
minDRlepJetCutList = [0]

cutConfigs = list(itertools.product(lep1PtCutList,jetPtCutList,metCutList,njetsCutList,nbjetsCutList,htCutList,stCutList,mllOSCutList,isPassTriLeptonList,isPassTrig_dilepList,ptRelCutList,minDRlepJetCutList))

thisDir = os.getcwd()
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
# pfix='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumiSYS_fixedLepIdIsoSys_ALLsys_step2_TESTING'
# pfix='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_ALLsys_step2_addmistag_addMoreSignal'
# pfix='optimization_condor_80x_MultiLep_Full2016_Moriond17_PRv6_FRv18bSys_fixedLumi_newMllOScut_fixedAllSYS_step2_addmistag_addMoreSignal'
# pfix='optimization_condor_PRv6_FRv20b_newMllOSV2_Allsys'
# pfix='optimization_reMiniAOD_PRv6_FRv24_newMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv24_newFRsys_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv24_newFRsys_AllSys_BB'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2_newRunH_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2_newRunH_correctedMuTrkSF_AllSys_BB'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2extSys_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2extSys_newRunH_correctedMuTrkSF_AllSys_BB'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2statOnly_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2Sys2Only_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv30CR2Sys4Only_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv10_FRv42CR2_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv10_FRv42CR2_newRunH_correctedMuTrkSF_AllSys_BB'
# pfix='optimization_reMiniAOD_PRv9_FRv45FRSRHT400low_newRunH_correctedMuTrkSF_AllSys'
# pfix='optimization_reMiniAOD_PRv9_FRv45FRSRHT400low_newRunH_correctedMuTrkSF_AllSys_BB'

# pfix='optimization_reMiniAOD_PRv9_FRv47FRSRHT400low2Dext_newRunH_correctedMuTrkSF_AllSys'

# pfix='optimization_reMiniAOD_PRv9_FRv45FRSRHT400low_newRunH_correctedMuTrkSF_addMlllBUnc_AllSys'
pfix='optimization_reMiniAOD_PRv9_FRv45FRSRHT400low_newRunH_correctedMuTrkSF_addMlllBUnc_AllSys_BB'

pfix+='_'+date#+'_'+time

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lep1PtCut,jetPtCut,metCut,njetsCut,nbjetsCut,htCut,stCut,mllOSCut,isPassTriLepton,isPassTrig_dilep,ptRelCut,minDRlepJetCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11]
	cutString = 'lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(htCut)+'_ST'+str(stCut)+'_mllOS'+str(mllOSCut)#+'_ptRel'+str(ptRelCut)+'_minDRlJ'+str(minDRlepJetCut).replace('.','p')
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'CMSSWBASE':relbase,'thisDir':thisDir,'lep1PtCut':lep1PtCut,'jetPtCut':jetPtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'nbjetsCut':nbjetsCut,
		  'htCut':htCut,'stCut':stCut,'mllOSCut':mllOSCut,'isPassTriLepton':isPassTriLepton,'isPassTrig_dilep':isPassTrig_dilep,
		  'ptRelCut':ptRelCut,'minDRlepJetCut':minDRlepJetCut}

	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorThetaTemplates_new.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(CMSSWBASE)s %(lep1PtCut)s %(jetPtCut)s %(metCut)s %(njetsCut)s %(nbjetsCut)s %(htCut)s %(stCut)s %(mllOSCut)s %(isPassTriLepton)s %(isPassTrig_dilep)s %(ptRelCut)s %(minDRlepJetCut)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
