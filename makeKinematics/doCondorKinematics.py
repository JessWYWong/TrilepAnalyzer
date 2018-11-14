import os,sys,datetime

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/user_data/rsyarif/'


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

pfix=''

if len(sys.argv)>1: pfix=str(sys.argv[1])

cutType=''
if len(sys.argv)>2: cutType=str(sys.argv[2])

# if cutType=='FRCR2' or cutType=='FRCR1'or cutType=='CR2' or cutType=='SR' or 'fSR' in cutType or cutType=='CR1' or cutType=='ALLR': pfix+='_'+cutType+'_'+date
if cutType!='': pfix+='_'+cutType+'_'+date
else: pfix+='_'+date

#pfix+='_'+date+'_'+time
# pfix+='_no_jsf'


plotList = [#distribution name as defined in "doHists.py"
# 	'ElDxy',
# 	'ElDz',
# 	'MuDxy',
# 	'MuDz',

# 	'AK4JetFlavor', #only for MC
# 
# 	'NPV',
	'lepPt',
	'lepPtRebinned',
# 	'ElPt',
# 	'MuPt',
# 
# 	'lep1Pt',
# 	'lep2Pt',
# 	'lep3Pt',
# 
# 	'lepEta',
# # 	'ElEta',
# # 	'MuEta',
# 
# 	'lep1Eta',
# 	'lep2Eta',
# 	'lep3Eta',
# 	
# 	'Nlep',
# 	'Nel',
# 	'Nmu',
# 
 	'JetEta',
# 
	'JetPt' ,
# 
# 	'HT',
# 	'HTrebinned',
	'ST',
# # 	'STrebinned',
	'STrebinnedv2',
# # 	'STrebinnedv3',
# # 	'MET',
# 	'METrebinned',
	'NJets' ,
# 	'NBJets',
# # 	'NBJetsCorr',
# 
# # 	'minMlB',
# # 	'minMlBv2', #
# # 	'minMlllB',
# 	'minMlllBv2',
# # 	'minMlllBv3', #
# 	'minMlllBv4', #
# 
# # 	'minDPhiMETJet',
# # 	'DRlep1Jet1',
# # 	'minDRlep1Jets',
# # 	'minDRlep2Jets',
# # 	'minDRlep3Jets',
# # 	'minDRlepsJets',
# 
# # 	'mindeltaRlepJets',
# # 	'mindeltaRlep1Jets',
# # 	'mindeltaRlep2Jets',
# # 	'mindeltaRlep3Jets',
# # 	'mindeltaRB',
# # 	'mindeltaR1',
# # 	'mindeltaR2',
# # 	'mindeltaR3',
# # 	'lepCharge',
# 
# # 	'lepIso',
# # 	'ElIso',
# # 	'MuIso',
# 
# # 	'PtRel1',
# # 	'PtRel2',
# # 	'PtRel3',
# # 	'PtRel',
# 
# # 	'MllsameFlavorOS',
# # 	'MllOSall',
# # 	'MllOSallmin',
# # 	'MllOSallmax',
# # 	'Mlll',
	]

catList = ['EEE','EEM','EMM','MMM','All']

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.chdir(outDir)

count = 0
for distribution in plotList:
	print 'Process condor jobs for:',cutType, distribution
	if ('noWeight' in cutType):
		if not ('ST' in distribution): continue
	for cat in catList:
		print cat
		if not os.path.exists(outDir+'/'+cat): os.system('mkdir '+cat)
		os.chdir(cat)
		
# 		dict={'dir':outputDir,'dist':distribution,'cat':cat}
# 		dict={'dir':thisDir,'dist':distribution,'cat':cat}
# 		dict={'CMSSWBASE':relbase,'dir':outputDir,'dist':distribution,'cat':cat}
# 		dict={'CMSSWBASE':relbase,'thisDir':thisDir,'dist':distribution,'cat':cat}
		dict={'CMSSWBASE':relbase,'thisDir':thisDir,'dist':distribution,'cat':cat,'cutType':cutType}


		jdf=open('condor_'+distribution+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorKinematics.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor_%(dist)s.out
Error = condor_%(dist)s.err
Log = condor_%(dist)s.log
Notification = Error
Arguments = %(CMSSWBASE)s %(dist)s %(cat)s %(cutType)s

Queue 1"""%dict)
		jdf.close()

		os.system('condor_submit condor_'+distribution+'.job')
		os.chdir('..')
		count+=1
									
print "Total jobs submitted:", count



                  
