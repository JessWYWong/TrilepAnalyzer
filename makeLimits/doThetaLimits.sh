#!/bin/bash
theDir=$1
condorDir=$PWD
configfile=$2

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd $theDir
eval `scramv1 runtime -sh`

/hoem/wwong/VLQ/THETA/CMSSW_8_0_24/src/theta/utils2/theta-auto.py $configfile
#/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/theta/utils/theta-auto.py $configfile
