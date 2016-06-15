#!/bin/bash

condorDir=$PWD
relbase=$1
plotIndex=$2
category=$3

cd $relbase
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd -

python doHists.py $condorDir $plotIndex $category
