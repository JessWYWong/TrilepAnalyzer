import os,sys,datetime,itertools

thisDir = os.getcwd()
relbase = '/home/wwong/VLQ/CMSSW_10_2_10/src/'
inputDir = '/mnt/data/users/wwong/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

pfix='FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_TrigEff_hadds_step2'
if len(sys.argv)>1: pfix=sys.argv[1]

inDir=inputDir+pfix

subdir='thetaTemplates_rootfiles'
if len(sys.argv)>2: subdir=sys.argv[2]

cutStr=os.listdir(inDir)

print(cutStr)

count = 0

for cut in cutStr:
    dict={'CMSSWBASE':relbase,'thisDir':thisDir,'pfix': pfix ,'cut':cut, 'subdir':subdir}
    if not os.path.exists(inDir+cut+'/'+subdir): os.system('mkdir '+inDir+cut+'/'+subdir)

    os.system('python doThetaLimits.py '+pfix+cut+' '+subdir+' '+subdir)

