import os,sys,shutil,datetime,time
import itertools

inputDir='/mnt/data/users/wwong/optimization_FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2_2020_6_24/'
if len(sys.argv)>1: inputDir=sys.argv[1]

subdir='/thetaTemplates_rootfiles'
if len(sys.argv)>2: subdir=sys.argv[2]

lep1PtCutList = [0]
jetPtCutList  = [0]
metCutList    = [20]
njetsCutList  = [3]
nbjetsCutList = [1]
htCutList     = [0]
# htCutList     = [400]
stCutList     = [0]#600,700,800,900,1000,1100]
mllOSCutList  = [20]
isPassTriLeptonList= [1]
isPassTrig_dilepList= [1]
ptRelCutList = [0]
minDRlepJetCutList = [0]
cutConfigs = list(itertools.product(lep1PtCutList,jetPtCutList,metCutList,njetsCutList,nbjetsCutList,htCutList,stCutList,mllOSCutList,isPassTriLeptonList,isPassTrig_dilepList,ptRelCutList,minDRlepJetCutList))


allSubFiles = False
if len(sys.argv)>3: allSubFiles = sys.argv[3]
cutStr = []
if allSubFiles:
    for conf in cutConfigs:
        lep1PtCut,jetPtCut,metCut,njetsCut,nbjetsCut,htCut,stCut,mllOSCut,isPassTriLepton,isPassTrig_dilep,ptRelCut,minDRlepJetCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11]
        cutStr.append('lep1Pt'+str(int(lep1PtCut))+'_jetPt'+str(int(jetPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_HT'+str(htCut)+'_ST'+str(stCut)+'_mllOS'+str(mllOSCut))
else :
    cutStr=os.listdir(inDir)


count = 0

for cut in cutStr:
    print(inputDir,cut,subdir)
    os.system('python doThetaTemplates.py '+inputDir+cut+' '+subdir)

