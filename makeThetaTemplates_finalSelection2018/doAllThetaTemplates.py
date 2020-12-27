import os,sys

inputDir='/mnt/data/users/wwong/optimization_FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_TrigEff_hadds_step2/'

if len(sys.argv)>1: inputDir=str(sys.argv[1])

dirList = os.listdir(inputDir)

for path in dirList:
    print('executing python doThetaTemplates.py '+inputDir+path+' /thetaTemplates_rootfiles')
    os.system('python doThetaTemplates.py '+inputDir+path+' /thetaTemplates_rootfiles')
 
