#!/bin/bash

condorDir=$PWD
relbase=$1

cd $relbase
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd -

python -u doThetaTemplates.py $condorDir \
						  --lepPtCut=${2} \
						  --lep1PtCut=${3} \
						  --jetPtCut=${4} \
						  --jet1PtCut=${5} \
						  --jet2PtCut=${6} \
						  --metCut=${7} \
						  --njetsCut=${8} \
						  --nbjetsCut=${9} \
						  --jet3PtCut=${10} \
						  --jet4PtCut=${11} \
						  --jet5PtCut=${12} \
						  --drCut=${13} \
						  --Wjet1PtCut=${14} \
						  --bjet1PtCut=${15} \
						  --htCut=${16} \
						  --stCut=${17} \
						  --minMlbCut=${18} \
						  --mllOSCut=${19} \
