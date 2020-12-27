#!/bin/bash
#file_list="TT_EOSList.txt"
file_list="MC_EOSList.txt_withSig"
#file_list="MC_EOSList.txt_Sig"
#file_list="MC_EOSList.txt_woutSig"
BruxBaseDir=$1 #"/mnt/data/users/wwong/" #$1
outputDir=$2

FNAL_eosBase="/store/user/wiwong/"
inDir=$3

while READLIST= read -r sample
do
  if [[ $sample == "#"* ]]; then
    echo "reading file ${file_list}"
    continue
  fi
  if [[ ! $sample == "/"* ]]; then
    continue
  fi

  if [[ $sample == *"DoubleEG"* ]] || [[ $sample == *"DoubleMuon"* ]] || [[ $sample == *"MuonEG"* ]] ; then
    echo "Data file ${sample} will not be copied"
  elif test -f "${BruxBaseDir}/${outputDir}/${sample}"; then
    echo "File ${sample} already exist. Not copying."
  else
    echo "copying ${sample} from lpc"
    eval "xrdcp root://cmseos.fnal.gov/${FNAL_eosBase}/${inDir}/${sample} ${BruxBaseDir}/${outputDir}"
  fi
done < "${file_list}"
echo "Finished copying files from lpc."
