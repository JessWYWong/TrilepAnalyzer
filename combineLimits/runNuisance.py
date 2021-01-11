import os,sys
from ROOT import TFile, TObject, RooArgSet

## Arguments: limit directory name; mass point; signal amount to inject; number of toys

## Make a datacard first with datacard.py!

limitdir = sys.argv[1]
mass = sys.argv[2]

BR = 'bW0p5_tZ0p25_tH0p25'
if 'BB' in mass: BR = 'tW0p5_bZ0p25_bH0p25'
mass = mass.replace('BB','')

path = limitdir+'/'+BR+'/cmb/'+mass

os.chdir(path)

print "Running Fit Diagnostics for background-only Asimov toy and fits it"
print 'Command = combine -M FitDiagnostics workspace.root --bypassFrequentistFit -t -1 --expectSignal 1'
os.system('combine -M FitDiagnostics workspace.root --bypassFrequentistFit -t -1 --expectSignal 1')

#print "Running Fit Diagnostics for Nuisance Pulls"
#print 'Command = combine -M FitDiagnostics -d workspace.root --bypassFrequentistFit -t -1 --expectSignal 1 --saveWorkspace --saveShapes --plots'
#os.system('combine -M FitDiagnostics -d workspace.root --bypassFrequentistFit -t -1 --expectSignal 1 --saveWorkspace --saveShapes --plots')

print "Done!"
