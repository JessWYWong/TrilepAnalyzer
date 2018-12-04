#!/usr/bin/python

samples = {


'TTM1000BWBW':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1100BWBW':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1200BWBW':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1300BWBW':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1400BWBW':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1500BWBW':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1600BWBW':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1700BWBW':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BWBW',
'TTM1800BWBW':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BWBW',

'TTM1000THBW':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1100THBW':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1200THBW':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1300THBW':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1400THBW':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1500THBW':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1600THBW':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1700THBW':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THBW',
'TTM1800THBW':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THBW',

'TTM1000TZBW':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1100TZBW':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1200TZBW':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1300TZBW':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1400TZBW':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1500TZBW':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1600TZBW':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1700TZBW':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZBW',
'TTM1800TZBW':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZBW',

'TTM1000TZTZ':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1100TZTZ':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1200TZTZ':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1300TZTZ':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1400TZTZ':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1500TZTZ':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1600TZTZ':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1700TZTZ':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTZ',
'TTM1800TZTZ':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTZ',

'TTM1000TZTH':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1100TZTH':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1200TZTH':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1300TZTH':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1400TZTH':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1500TZTH':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1600TZTH':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1700TZTH':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTH',
'TTM1800TZTH':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTH',

'TTM1000THTH':'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1100THTH':'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1200THTH':'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1300THTH':'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1400THTH':'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1500THTH':'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1600THTH':'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1700THTH':'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THTH',
'TTM1800THTH':'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THTH',

#BB
'BBM1000TWTW':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1100TWTW':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1200TWTW':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1300TWTW':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1400TWTW':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1500TWTW':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1600TWTW':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1700TWTW':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TWTW',
'BBM1800TWTW':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TWTW',

'BBM1000BHTW':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1100BHTW':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1200BHTW':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1300BHTW':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1400BHTW':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1500BHTW':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1600BHTW':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1700BHTW':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BHTW',
'BBM1800BHTW':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BHTW',

'BBM1000BZTW':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1100BZTW':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1200BZTW':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1300BZTW':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1400BZTW':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1500BZTW':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1600BZTW':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1700BZTW':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZTW',
'BBM1800BZTW':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZTW',

'BBM1000BZBZ':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1100BZBZ':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1200BZBZ':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1300BZBZ':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1400BZBZ':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1500BZBZ':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1600BZBZ':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1700BZBZ':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZBZ',
'BBM1800BZBZ':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZBZ',

'BBM1000BZBH':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1100BZBH':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1200BZBH':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1300BZBH':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1400BZBH':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1500BZBH':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1600BZBH':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1700BZBH':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZBH',
'BBM1800BZBH':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZBH',

'BBM1000BHBH':'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1100BHBH':'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1200BHBH':'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1300BHBH':'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1400BHBH':'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1500BHBH':'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1600BHBH':'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1700BHBH':'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BHBH',
'BBM1800BHBH':'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BHBH',
#


#'WW':'WW_TuneCUETP8M1_13TeV-pythia8',

'WZ':'WZTo3LNu_TuneCP5_13TeV-powheg-pythia8',
'ZZ':'ZZTo4L_TuneCP5_13TeV_powheg_pythia8',

'WWW':'WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8',
'WWZ':'WWZ_TuneCP5_13TeV-amcatnlo-pythia8',
'WZZ':'WZZ_TuneCP5_13TeV-amcatnlo-pythia8',
'ZZZ':'ZZZ_TuneCP5_13TeV-amcatnlo-pythia8',

'WJets':'',


'TTJetsPH':'',

'TTWl':'TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'TTWq':'',
'TTZl':'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
'TTZq':'',

#### As requested by Cristina Botta (ARC B2G-17-011).
'TTGJets':'',
'ZGTo2LG':'',
'TTZToLLM1to10':'',

}

dilep = ['EE','MM','ME']
dict_dilep = {dilep[0]:'EGamma',dilep[1]:'DoubleMuon',dilep[2]:'MuonEG'}
run = ['RunA','RunB','RunC','RunD']
ddbkgCat = ['TTT','TTL','TLT','LTT','TLL','LTL','LLT','LLL']

for run_ in run:
	for dilep_ in dilep:
		samples['Data'+dilep_+run_]=dict_dilep[dilep_]+'_'+run_
		samples['DataDrivenBkg'+dilep_+run_]=dict_dilep[dilep_]+'_'+run_
		for ddbkgCat_ in ddbkgCat:
			samples['DataDrivenBkg'+ddbkgCat_+dilep_+run_]=dict_dilep[dilep_]+'_'+run_
