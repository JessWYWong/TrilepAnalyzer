#!/bin/bash

indir=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRv9_FRv24_postPreapproval_step1hadds_step2

outdir1=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRvElPRtest_FRv24_postPreapproval_step1hadds_step2
outdir2=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRvMuPRtest_FRv24_postPreapproval_step1hadds_step2
outdir3=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_PRv9_FRvMuEtatest_postPreapproval_step1hadds_step2

cp -vr $indir/JE* $outdir1/
cp -vr $indir/JE* $outdir2/
cp -vr $indir/JE* $outdir3/

cp -v $indir/nominal/DY* $outdir1/nominal/
cp -v $indir/nominal/DY* $outdir2/nominal/
cp -v $indir/nominal/DY* $outdir3/nominal/

cp -v $indir/nominal/T* $outdir1/nominal/
cp -v $indir/nominal/T* $outdir2/nominal/
cp -v $indir/nominal/T* $outdir3/nominal/

cp -v $indir/nominal/W* $outdir1/nominal/
cp -v $indir/nominal/W* $outdir2/nominal/
cp -v $indir/nominal/W* $outdir3/nominal/

cp -v $indir/nominal/Z* $outdir1/nominal/
cp -v $indir/nominal/Z* $outdir2/nominal/
cp -v $indir/nominal/Z* $outdir3/nominal/


# dir=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv18bSys_6Feb2017_step1hadds_step2
# dir=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv20b_1Mar2017_step1hadds_step2
# hadd -f $dir/ALLdata.root \
# $dir/nominal/DoubleEG_RRB_hadd.root \
# $dir/nominal/DoubleEG_RRC_hadd.root \
# $dir/nominal/DoubleEG_RRD_hadd.root \
# $dir/nominal/DoubleEG_RRE_hadd.root \
# $dir/nominal/DoubleEG_RRF_hadd.root \
# $dir/nominal/DoubleEG_RRG_hadd.root \
# $dir/nominal/DoubleEG_PRH_hadd.root \
# $dir/nominal/DoubleMuon_RRB_hadd.root \
# $dir/nominal/DoubleMuon_RRC_hadd.root \
# $dir/nominal/DoubleMuon_RRD_hadd.root \
# $dir/nominal/DoubleMuon_RRE_hadd.root \
# $dir/nominal/DoubleMuon_RRF_hadd.root \
# $dir/nominal/DoubleMuon_RRG_hadd.root \
# $dir/nominal/DoubleMuon_PRH_hadd.root \
# $dir/nominal/MuonEG_RRB_hadd.root \
# $dir/nominal/MuonEG_RRC_hadd.root \
# $dir/nominal/MuonEG_RRD_hadd.root \
# $dir/nominal/MuonEG_RRE_hadd.root \
# $dir/nominal/MuonEG_RRF_hadd.root \
# $dir/nominal/MuonEG_RRG_hadd.root \
# $dir/nominal/MuonEG_PRH_hadd.root \

# dir=/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_2017_2_24_rizki_step1hadds_step2/
# hadd -f $dir/ALLdata.root \
# $dir/nominal/DoubleEG_RRB_hadd.root \
# $dir/nominal/DoubleEG_RRC_hadd.root \
# $dir/nominal/DoubleEG_RRD_hadd.root \
# $dir/nominal/DoubleEG_RRE_hadd.root \
# $dir/nominal/DoubleEG_RRF_hadd.root \
# $dir/nominal/DoubleEG_RRG_hadd.root \
# $dir/nominal/DoubleEG_RRH_hadd.root \
# $dir/nominal/DoubleMuon_RRB_hadd.root \
# $dir/nominal/DoubleMuon_RRC_hadd.root \
# $dir/nominal/DoubleMuon_RRD_hadd.root \
# $dir/nominal/DoubleMuon_RRE_hadd.root \
# $dir/nominal/DoubleMuon_RRF_hadd.root \
# $dir/nominal/DoubleMuon_RRG_hadd.root \
# $dir/nominal/DoubleMuon_RRH_hadd.root \
# $dir/nominal/MuonEG_RRB_hadd.root \
# $dir/nominal/MuonEG_RRC_hadd.root \
# $dir/nominal/MuonEG_RRD_hadd.root \
# $dir/nominal/MuonEG_RRE_hadd.root \
# $dir/nominal/MuonEG_RRF_hadd.root \
# $dir/nominal/MuonEG_RRG_hadd.root \
# $dir/nominal/MuonEG_RRH_hadd.root \
# 
