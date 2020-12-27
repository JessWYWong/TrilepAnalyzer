import os,sys,datetime,itertools

thisDir = os.getcwd()
relbase = '/home/wwong/VLQ/CMSSW_10_2_10/src/'
inputDir = '/mnt/data/users/wwong/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

pfix='FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_TrigEff_hadds_step2_templates/'
if len(sys.argv)>1: pfix=sys.argv[1]

inDir=inputDir+pfix

cutStr=os.listdir(inDir)

count = 0

for cut in cutStr:
    os.system('python PlotLimits.py '+pfix+' '+cut)

