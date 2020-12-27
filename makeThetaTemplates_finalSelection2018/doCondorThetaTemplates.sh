#!/bin/bash

condorDir=$PWD
relbase=$1
outdir=${15}

cd $relbase
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd -

echo $outdir

python -u doHists.py $outdir \
						  --lep1PtCut=${2} \
						  --jetPtCut=${3} \
						  --metCut=${4} \
						  --njetsCut=${5} \
                                                  --bJet1PtCut=${6} \
						  --nbjetsCut=${7} \
						  --htCut=${8} \
						  --stCut=${9} \
						  --mllOSCut=${10} \
						  --isPassTriLepton=${11} \
						  --isPassTrig_dilep=${12} \
						  --ptRelCut=${13}\
						  --minDRlepJetCut=${14}\
