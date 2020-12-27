#!/usr/bin/env python

import os,sys,time,math,datetime,itertools
from ROOT import gROOT,TFile,TH1F

if 'CMSSW_10_2_10' in os.environ['CMSSW_BASE']:
        print "Go CMSENV inside CMSSW_10_2_13!"
        exit(1)

parent = os.path.dirname(os.getcwd())
thisdir= os.path.dirname(os.getcwd()+'/')
sys.path.append(parent)
from utils import *
import CombineHarvester.CombineTools.ch as ch

gROOT.SetBatch(1)

tag = '_FRv5_PRv2_prefiring' ##Tag and saveKey are used for output directory names

fileDir = '/mnt/data/users/wwong/'
templateDir17 = 'optimization_FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2'
templateDir18 = 'optimization_FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_elIdSys_TrigEffWeight_pdf4LHC_hadds_step2_FIX'
BRconfStr= 'bW0p0_tZ0p5_tH0p5'
subDir = 'thetaTemplates_rootfiles_Combine'
if len(sys.argv)>1 : templateDir17 = sys.argv[1]
if len(sys.argv)>2 : templateDir18 = sys.argv[2]
if len(sys.argv)>3 : BRconfStr = sys.argv[3]
if len(sys.argv)>4 : subDir = sys.argv[4]
if len(sys.argv)>5 : tag = sys.argv[5]

cutStr17 = templateDir17.split("/")[-1]
cutStr18 = templateDir18.split("/")[-1]

saveKey = tag

fileDir17 = fileDir+templateDir17+'/'+subDir+'/'
fileDir18 = fileDir+templateDir18+'/'+subDir+'/'

template = 'templates'+'_'#+'SR'/'CR'

whichsignal = 'TT'
if 'tW' in BRconfStr: whichsignal = 'BB'

print'Tag = ',tag,', BR string = ',BRconfStr

def add_processes_and_observations(cb, prefix=whichsignal):
        print '------------------------------------------------------------------------'
	print '>> Creating processes and observations...'
	for chn in chns:
                print '>>>> \t Creating proc/obs for channel:',chn
		cats_chn = cats[chn]
		cb.AddObservations(  ['*'],  [prefix], [era], [chn],                 cats_chn      )
		cb.AddProcesses(     ['*'],  [prefix], [era], [chn], bkg_procs[chn], cats_chn, False  )
		cb.AddProcesses(     masses, [prefix], [era], [chn], sig_procs,      cats_chn, True   )


def add_shapes(cb, prefix=whichsignal):
        print '------------------------------------------------------------------------'
	print '>> Extracting histograms from input root files...'
	for chn in chns:
                print '>>>> \t Extracting histos for channel:',chn
		#CRbkg_pattern = 'HTNtag_'+lumiStr+'_%s$BIN__$PROCESS' % chn
		#SRbkg_pattern = discrim+'_'+lumiStr+'_%s$BIN__$PROCESS' % chn
		#CRsig_pattern = 'HTNtag_'+lumiStr+'_%s$BIN__$PROCESS$MASS' % chn
		#SRsig_pattern = discrim+'_'+lumiStr+'_%s$BIN__$PROCESS$MASS' % chn
		bkg_pattern = '%s$BIN__$PROCESS' % chn
		sig_pattern = '%s$BIN__$PROCESS$MASS' % chn
		print("pattern", bkg_pattern, sig_pattern)
		#if prefix=='BB': SRbkg_pattern = SRbkg_pattern.replace('Tprime','Bprime')
		#if prefix=='BB': SRsig_pattern = SRsig_pattern.replace('TTM','BBM').replace('Tprime','Bprime')
		if prefix=='BB': bkg_pattern = bkg_pattern.replace('Tprime','Bprime')
		if prefix=='BB': sig_pattern = sig_pattern.replace('TTM','BBM').replace('Tprime','Bprime')

		#if 'isCR' in chn: 
		#	cb.cp().channel([chn]).era([era]).backgrounds().ExtractShapes(rfile, CRbkg_pattern, CRbkg_pattern + '__$SYSTEMATIC')
		#	cb.cp().channel([chn]).era([era]).signals().ExtractShapes(rfile, CRsig_pattern, CRsig_pattern + '__$SYSTEMATIC')
		#elif 'isSR' in chn:
		#	cb.cp().channel([chn]).era([era]).backgrounds().ExtractShapes(rfile, SRbkg_pattern, SRbkg_pattern + '__$SYSTEMATIC')
		#	cb.cp().channel([chn]).era([era]).signals().ExtractShapes(rfile, SRsig_pattern, SRsig_pattern + '__$SYSTEMATIC')
		#else:
		cb.cp().channel([chn]).era([era]).backgrounds().ExtractShapes(rfile, bkg_pattern, bkg_pattern + '__$SYSTEMATIC')
		cb.cp().channel([chn]).era([era]).signals().ExtractShapes(rfile, sig_pattern, sig_pattern + '__$SYSTEMATIC')


def add_bbb(cb):
        ## This function is not used! autoMCstats in the card instead
	print '>> Merging bin errors and generating bbb uncertainties...'
	bbb = ch.BinByBinFactory()
	bbb.SetAddThreshold(0.1).SetMergeThreshold(0.5).SetFixNorm(False)
	
	for chn in chns:
		cb_chn = cb.cp().channel([chn])
		if 'CR' in chn:
			bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0,1,2,3]).process(bkg_procs[chn]), cb)
			bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0,1,2,3]).process(sig_procs), cb)
		else:
			bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0]).process(bkg_procs[chn]), cb)
			bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0]).process(sig_procs), cb)


def rename_and_write(cb):
        print '------------------------------------------------------------------------'
	print '>> Setting standardised bin names...'
	ch.SetStandardBinNames(cb)
	
	writer = ch.CardWriter('limits_'+template+saveKey+'/'+BRconfStr+'/$TAG/$MASS/$ANALYSIS_$CHANNEL_$BINID_$ERA.txt',
						   'limits_'+template+saveKey+'/'+BRconfStr+'/$TAG/common/$ANALYSIS_$CHANNEL.input.root')
	writer.SetVerbosity(1)
	writer.WriteCards('cmb', cb)
	for chn in chns:
                print '>>>> \t WriteCards for channel:',chn
		writer.WriteCards(chn, cb.cp().channel([chn]))
	print '>> Done writing cards!'


def print_cb(cb):
	for s in ['Obs', 'Procs', 'Systs', 'Params']:
		print '* %s *' % s
		getattr(cb, 'Print%s' % s)()
		print


def add_systematics(cb):
        print '------------------------------------------------------------------------'
	print '>> Adding systematic uncertainties...'

	signal = cb.cp().signals().process_set()
        print ( signal, allbkgs, chns, chnsMMM, era)	
        ## Uncorrelated; Ex: B2G-19-001/AN2018_322_v7
        cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'lumi$ERA', 'lnN', ch.SystMap('era')(['2016'], 1.025)(['2017'], 1.023)(['2018'], 1.025)) 

        ## Taking lepton SFs as uncorrelated, new calculations each year
	#cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'elIdSys', 'shape', ch.SystMap()(1.0)) 
	cb.cp().process(signal + allbkgs).channel(chnsEEM).AddSyst(cb, 'muIdSys$ERA', 'lnN', ch.SystMap()(1.02))
	cb.cp().process(signal + allbkgs).channel(chnsEMM).AddSyst(cb, 'muIdSys$ERA', 'lnN', ch.SystMap()(1.04))
	cb.cp().process(signal + allbkgs).channel(chnsMMM).AddSyst(cb, 'muIdSys$ERA', 'lnN', ch.SystMap()(1.06))
	#cb.cp().process(signal + allbkgs).channel(chnsAll).AddSyst(cb, 'muIdSys', 'lnN', ch.SystMap()(1.049))
	cb.cp().process(signal + allbkgs).channel(chnsEEE).AddSyst(cb, 'elIsoSys$ERA', 'lnN', ch.SystMap()(1.045))
	cb.cp().process(signal + allbkgs).channel(chnsEEM).AddSyst(cb, 'elIsoSys$ERA', 'lnN', ch.SystMap()(1.030))
	cb.cp().process(signal + allbkgs).channel(chnsEMM).AddSyst(cb, 'elIsoSys$ERA', 'lnN', ch.SystMap()(1.015))
	#cb.cp().process(signal + allbkgs).channel(chnsAll).AddSyst(cb, 'elIsoSys', 'lnN', ch.SystMap()(1.036))
	cb.cp().process(signal + allbkgs).channel(chnsEEM).AddSyst(cb, 'muIsoSys$ERA', 'lnN', ch.SystMap()(1.015))
	cb.cp().process(signal + allbkgs).channel(chnsEMM).AddSyst(cb, 'muIsoSys$ERA', 'lnN', ch.SystMap()(1.030))
	cb.cp().process(signal + allbkgs).channel(chnsMMM).AddSyst(cb, 'muIsoSys$ERA', 'lnN', ch.SystMap()(1.045))
	#cb.cp().process(signal + allbkgs).channel(chnsAll).AddSyst(cb, 'muIsoSys', 'lnN', ch.SystMap()(1.036))
	cb.cp().process(signal + allbkgs).channel(chnsEEE).AddSyst(cb, 'elRecoSys$ERA', 'lnN', ch.SystMap()(1.03))
	cb.cp().process(signal + allbkgs).channel(chnsEEM).AddSyst(cb, 'elRecoSys$ERA', 'lnN', ch.SystMap()(1.02))
	cb.cp().process(signal + allbkgs).channel(chnsEMM).AddSyst(cb, 'elRecoSys$ERA', 'lnN', ch.SystMap()(1.01))

	cb.cp().process(ddbkg).channel(chnsEEE).AddSyst(cb, 'elPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.066))(['2018'],(1.00,1.074)))
	cb.cp().process(ddbkg).channel(chnsEEM).AddSyst(cb, 'elPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.028))(['2018'],(1.00,1.026)))
	cb.cp().process(ddbkg).channel(chnsEMM).AddSyst(cb, 'elPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.010))(['2018'],(1.00,1.008)))
	#cb.cp().process(ddbkg).channel(chnsAll).AddSyst(cb, 'elPRsys', 'lnN', ch.SystMap('era')(['2017'],1.02)(['2018'],1.02))
	cb.cp().process(ddbkg).channel(chnsEEM).AddSyst(cb, 'muPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.010))(['2018'],(1.00,1.012)))
	cb.cp().process(ddbkg).channel(chnsEMM).AddSyst(cb, 'muPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.015))(['2018'],(1.00,1.016)))
	cb.cp().process(ddbkg).channel(chnsMMM).AddSyst(cb, 'muPRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.066))(['2018'],(1.00,1.054)))
	#cb.cp().process(ddbkg).channel(chnsAll).AddSyst(cb, 'muPRsys', 'lnN', ch.SystMap('era')(['2017'],1.02)(['2018'],1.02))
	cb.cp().process(ddbkg).channel(chnsEEM).AddSyst(cb, 'muFReta$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.082))(['2018'],(1.00,1.018)))
	cb.cp().process(ddbkg).channel(chnsEMM).AddSyst(cb, 'muFReta$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.153))(['2018'],(1.00,1.030)))
	cb.cp().process(ddbkg).channel(chnsMMM).AddSyst(cb, 'muFReta$ERA', 'lnN', ch.SystMap('era')(['2017'],(1.00,1.328))(['2018'],(1.00,1.048)))
	#cb.cp().process(ddbkg).channel(chnsAll).AddSyst(cb, 'muFReta', 'lnN', ch.SystMap('era')(['2017'],1.17)(['2018'],1.03))

	cb.cp().process(ddbkg).channel(chnsEEE).AddSyst(cb, 'FRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],1.257)(['2018'],1.206))
	cb.cp().process(ddbkg).channel(chnsEEM).AddSyst(cb, 'FRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],1.144)(['2018'],1.076))
	cb.cp().process(ddbkg).channel(chnsEMM).AddSyst(cb, 'FRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],1.030)(['2018'],1.019))
	cb.cp().process(ddbkg).channel(chnsMMM).AddSyst(cb, 'FRsys$ERA', 'lnN', ch.SystMap('era')(['2017'],1.158)(['2018'],1.067))

        ## Taking uncorrelated -- example of B2G-19-001. Jec uncorrelated is more conservative than the various 0/50/100 scenarios that require source splitting
	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'jer$ERA', 'shape', ch.SystMap()(1.0))
	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'jec$ERA', 'shape', ch.SystMap()(1.0))

	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'pdfNew', 'shape', ch.SystMap()(1.0))

        ## Correlated: https://hypernews.cern.ch/HyperNews/CMS/get/b2g/1381.html
        cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'pileup', 'shape', ch.SystMap()(1.0)) 

	## Correlated in 2016 and 2017, doesn't exist in 2018
        if era=="2017": cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'prefire', 'shape', ch.SystMap()(1.0))

	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'btag' , 'shape', ch.SystMap()(1.0))
	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'mistag' , 'shape', ch.SystMap()(1.0))
	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'TrigEffWeight$ERA' , 'shape', ch.SystMap()(1.0))
	cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'elIdSys$ERA' , 'shape', ch.SystMap()(1.0))

	## Taking as correlated across years, but not processes -- no changes to this setting in MC
	cb.cp().process([allbkgs[0]]).channel(chns).AddSyst(cb, 'muRFcorrdNewTop', 'shape', ch.SystMap()(1.0))
	cb.cp().process([allbkgs[1]]).channel(chns).AddSyst(cb, 'muRFcorrdNewEwk', 'shape', ch.SystMap()(1.0))
	#cb.cp().process([allbkgs[2]]).channel(chns).AddSyst(cb, 'muRFcorrdNewQCD', 'shape', ch.SystMap()(1.0))
	cb.cp().process(signal).channel(chns).AddSyst(cb, 'muRFcorrdNewSig', 'shape', ch.SystMap()(1.0))



def add_autoMCstat(cb):
        print '------------------------------------------------------------------------'
	print '>> Adding autoMCstats...'
	
	thisDir = os.getcwd()
	mass=0
	massList = range(1000,1800+1,100)
	if whichsignal=='BB': massList = range(900,1800+1,100)

	for chn in chns+['cmb']:
                print '>>>> \t Adding autoMCstats for channel:',chn
		for mass in massList:
			chnDir = os.getcwd()+'/limits_'+template+saveKey+'/'+BRconfStr+'/'+chn+'/'+str(mass)+'/'
			print 'chnDir: ',chnDir
			os.chdir(chnDir)
			files = [x for x in os.listdir(chnDir) if '.txt' in x]
			for ifile in files:
				with open(chnDir+ifile, 'a') as chnfile: chnfile.write('* autoMCStats 1.')
			os.chdir(thisDir)

def create_workspace(cb):
        print '------------------------------------------------------------------------'
	print '>> Creating workspace...'

	#for chn in ['cmb']+chns:  ## do I really need individual workspaces? Not sure...
	for chn in ['cmb']:
                print '>>>> \t Creating workspace for channel:',chn
		chnDir = os.getcwd()+'/limits_'+template+saveKey+'/'+BRconfStr+'/'+chn+'/*'
		cmd = 'combineTool.py -M T2W -i '+chnDir+' -o workspace.root --parallel 4 --channel-masks'
		os.system(cmd)


def go(cb):
	add_processes_and_observations(cb)
	add_systematics(cb)
	add_shapes(cb)
	rename_and_write(cb)
	add_autoMCstat(cb)
	#create_workspace(cb)


if __name__ == '__main__':
	cb = ch.CombineHarvester()
	
	if not os.path.exists('./limits_'+template+saveKey+'/'+BRconfStr): os.system('mkdir -p ./limits_'+template+saveKey+'/'+BRconfStr+'/')
        discrim = 'STrebinnedv2'

        allbkgs = ['top','ewk']
        ddbkg = ['ddbkg']
	dataName = 'data_obs'

	if whichsignal=='TT': sig_procs = ['TTM']
        elif whichsignal=='BB': sig_procs = ['BBM']

	masses = ch.ValsFromRange('1000:1800|100')
        if whichsignal=='BB': masses = ch.ValsFromRange('900:1800|100')
        print 'Found this mass list: ',masses


	era = '2017'
	lumiStrDir = '41p557'
	lumiStr = lumiStrDir+'fb'

	rfile = fileDir17+'/templates_'+discrim+'_'+BRconfStr+'_'+lumiStrDir+'_Combine.root'
	print'File: ',rfile

	tfile17 = TFile(rfile)
	allHistNames = [k.GetName() for k in tfile17.GetListOfKeys() if not (k.GetName().endswith('Up') or k.GetName().endswith('Down'))]
	tfile17.Close()
	chns = [hist[:hist.find('__')] for hist in allHistNames if '__'+dataName in hist]

	chnsEEE = [chn for chn in chns if 'triLep2017EEE' in chn]
        chnsEEM = [chn for chn in chns if 'triLep2017EEM' in chn]
        chnsEMM = [chn for chn in chns if 'triLep2017EMM' in chn]
        chnsMMM = [chn for chn in chns if 'triLep2017MMM' in chn]

	bkg_procs = {chn:[hist.split('__')[-1] for hist in allHistNames if chn+'__' in hist and not (hist.endswith('Up') or hist.endswith('Down') or hist.endswith(dataName) or 'TTM' in hist or 'BBM' in hist)] for chn in chns}
	for cat in sorted(bkg_procs.keys()):
		print cat,bkg_procs[cat]
	if 'qcd' in bkg_procs[cat]:
		print '		Removing qcd ...'
		bkg_procs[cat]=bkg_procs[cat][:-1]
	
	cats = {}
	for chn in chns: cats[chn] = [(0, '')]
	
	go(cb)


	era = '2018'
	lumiStrDir = '59p74'
	lumiStr = lumiStrDir+'fb'

	rfile = fileDir18+'/templates_'+discrim+'_'+BRconfStr+'_'+lumiStrDir+'_Combine.root'
	print'File: ',rfile
	tfile18 = TFile(rfile)
	allHistNames = [k.GetName() for k in tfile18.GetListOfKeys() if not (k.GetName().endswith('Up') or k.GetName().endswith('Down'))]
	tfile18.Close()

	chns = [hist[:hist.find('__')] for hist in allHistNames if '__'+dataName in hist]

	chnsEEE = [chn for chn in chns if 'triLep2018EEE' in chn]
        chnsEEM = [chn for chn in chns if 'triLep2018EEM' in chn]
        chnsEMM = [chn for chn in chns if 'triLep2018EMM' in chn]
        chnsMMM = [chn for chn in chns if 'triLep2018MMM' in chn]

	bkg_procs = {chn:[hist.split('__')[-1] for hist in allHistNames if chn+'__' in hist and not (hist.endswith('Up') or hist.endswith('Down') or hist.endswith(dataName) or 'TTM' in hist or 'BBM' in hist)] for chn in chns}
        for cat in sorted(bkg_procs.keys()):
                print cat,bkg_procs[cat]
        if 'qcd' in bkg_procs[cat]:
                print '         Removing qcd ...'
                bkg_procs[cat]=bkg_procs[cat][:-1]

        cats = {}
        for chn in chns: cats[chn] = [(0, '')]

        go(cb)

	create_workspace(cb)
