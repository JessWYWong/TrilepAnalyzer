#!/usr/bin/python

samples = {

# 'DY10to50': 'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DY10to50':'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
# 'DY50':'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DY50':'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined',
# 'DY50':'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
# 'DY50':DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',

# 'DYMG100':'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG200':'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG400':'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG600':'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG800':'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG1200':'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 'DYMG2500':'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
# 
# 'TTJetsPH':'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8',

}

useWhichSampleForMatrix='TT_TuneCUETP8M2T4_13TeV-powheg-pythia8'
samples['TTJetsPH']='TT_TuneCUETP8M2T4_13TeV-powheg-pythia8'

# useWhichSampleForMatrix='DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined'
# samples['DY50']='DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined'

samples['MatrixBkg']=useWhichSampleForMatrix

ddbkgCat = ['TTT','TTL','TLT','LTT','TLL','LTL','LLT','LLL']
for ddbkgCat_ in ddbkgCat:
	samples['MatrixBkg'+ddbkgCat_]=useWhichSampleForMatrix


#adding scans of ddbkg
increment = 0.01;
initial = 0.0;
end = 1.0;
loop = (int) ( ( end - initial ) / increment ) + 1;
muFR=0.;
elFR=0.;
print 'scanning ddbkg using each muFR and elFR from ',  initial , ' to ' , end , ' with increment of ', increment ,'(' ,loop ,' loops) .'
for muFRindex in xrange(loop):
	for elFRindex in xrange(loop):
		samples['MatrixBkg_muFR'+str(muFRindex++((int)(initial*100)))+'elFR'+str(elFRindex++((int)(initial*100)))]=useWhichSampleForMatrix

