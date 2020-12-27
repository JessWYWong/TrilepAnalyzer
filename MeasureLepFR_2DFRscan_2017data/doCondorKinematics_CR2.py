import os,sys,datetime,shutil

thisDir = os.getcwd()
# outputDir = thisDir+'/'
relbase = '/home/wwong/VLQ/CMSSW_10_2_10/src/'#'/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/'
outputDir = '/mnt/data/users/wwong/'#'/user_data/rsyarif/'
if len(sys.argv)>1: outputDir=sys.argv[1]


cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)


#pfix='measureFR_LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_FRCR2' #remember to modify analyse.py for low hT and cutList.py!
'''
cutList = {'isPassTrig': 0, 
		   'isPassTrig_dilep': 1,
		   'isPassTrig_dilep_anth': 0,
		   'isPassTrig_trilep': 0, 
		   'isPassTrilepton': 1,
		   'lepPtCut': 30, 
		   'leadJetPtCut':0,
		   'subLeadJetPtCut':0, 
		   'thirdJetPtCut':0,
		   'metCut': 20,
		   'njetsCut': 2, #FRCR2:2, FRCR1:1, SR:3 
		   'nbjetsCut':1,
		   'drCut':0, 
	   	   'stCut':0,
	   	   'mllOSCut':20,
	   	   'htCut':0,
	   	   'mlllbCut':0,
	   	   'minDRlepJetCut': 0,
	   	   'ptRelCut':0,
		   }
'''



#pfix+='_'+date
#pfix+='_'+date+'_'+time
# pfix+='_no_jsf'

plotList = [#distribution name as defined in "doHists.py"
# 	'NPV',
	'lepPt',
# 	'ElPt',
# 	'MuPt',
# 	'lep1Pt',
# 	'lep2Pt',
# 	'lep3Pt',
# 	'lepEta',
# 	'ElEta',
# 	'MuEta',
# 	'lep1Eta',
# 	'lep2Eta',
# 	'lep3Eta',
#  	'JetEta',
#  	'Jet1Eta',
#  	'Jet2Eta',
# 	'JetPt' ,
# 	'Jet1Pt',
# 	'Jet2Pt',
# 	'HT',
# 	'HTrebinned',
# 	'ST',
# 	'STrebinned',
# 	'MET',
# 	'METrebinned',
# 	'NJets' ,
# 	'NBJets',
# 	'NBJetsCorr',
# 	'mindeltaRlepJets',
# 	'mindeltaRlep1Jets',
# 	'mindeltaRlep2Jets',
# 	'mindeltaRlep3Jets',
# 	'mindeltaRB',
# 	'mindeltaR1',
# 	'mindeltaR2',
# 	'mindeltaR3',
# 	'lepCharge',
# 	'lepIso',
# 	'ElIso',
# 	'MuIso',
# 	'PtRel1',
# 	'PtRel2',
# 	'PtRel3',
# 	'MllsameFlavorOS',
# 	'MllOSall',
# 	'MllOSallmin',
# 	'Mlll',
	]

if len(sys.argv)>2: plotList = [str(sys.argv[2])]


catList = ['EEE','EEM','EMM','MMM','All']
if len(sys.argv)>3: catList=[str(sys.argv[3])]

outDir = outputDir#+'_'+date#pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.chdir(outDir)

shutil.copyfile(thisDir+'/cutList_CR2.py', thisDir+'/cutList.py')
os.system('cat '+thisDir+'/cutList.py')

count = 0
for distribution in plotList:
	for cat in catList:
		print cat
		if not os.path.exists(outDir+'/'+cat): os.system('mkdir '+cat)
		os.chdir(cat)
		
# 		dict={'dir':outputDir,'dist':distribution,'cat':cat}
# 		dict={'dir':thisDir,'dist':distribution,'cat':cat}
 		dict={'CMSSWBASE':relbase,'dir':outDir,'dist':distribution,'cat':cat,'thisDir':thisDir}
#		dict={'CMSSWBASE':relbase,'thisDir':thisDir,'dist':distribution,'cat':cat}


		jdf=open('condor_'+distribution+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(thisDir)s/doCondorKinematics.sh
Should_Transfer_Files = YES
transfer_input_files = %(thisDir)s/doHists.py,%(thisDir)s/samples.py,%(thisDir)s/weights.py,%(thisDir)s/analyze.py,%(thisDir)s/cutList.py
WhenToTransferOutput = ON_EXIT

arguments      = ""

Output = condor_%(dist)s.out
Error = condor_%(dist)s.err
Log = condor_%(dist)s.log
Notification = Error
Arguments = %(CMSSWBASE)s %(dir)s %(dist)s %(cat)s

Queue 1"""%dict)
		jdf.close()

 		os.system('condor_submit condor_'+distribution+'.job')
		os.chdir('..')
		count+=1
									
print "Total jobs submitted:", count



                  
