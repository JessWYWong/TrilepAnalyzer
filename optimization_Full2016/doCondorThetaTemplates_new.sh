#!/bin/bash

condorDir=$PWD
relbase=$1

cd $relbase
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd -

python -u doHists.py $condorDir \
						  --lep1PtCut=${2} \
						  --jetPtCut=${3} \
						  --metCut=${4} \
						  --njetsCut=${5} \
						  --nbjetsCut=${6} \
						  --htCut=${7} \
						  --stCut=${8} \
						  --mllOSCut=${9} \
						  --isPassTriLepton=${10} \
						  --isPassTrig_dilep=${11} \
						  --ptRelCut=${12}\
						  --minDRlepJetCut=${13}\
