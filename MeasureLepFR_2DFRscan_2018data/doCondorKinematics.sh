#!/bin/bash

condorDir=$2
relbase=$1
VarName=$3
category=$4

cd $relbase
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd -

python doHists.py $condorDir $VarName $category
