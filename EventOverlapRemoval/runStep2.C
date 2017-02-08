#include "step2.C"

void runStep2(){
  
  
  std::vector<TString> inputFiles;
  std::vector<TString> outputFiles;

  TString inputFile;
  TString outputFile;
  TString bruxDir;
  TString inputDir;
  TString subDir;
  TString outputDir;  
  
  bruxDir ="/user_data/rsyarif";

  std::vector<TString> fileNames;
  
//   fileNames.push_back("DoubleEG_PRB_hadd.root");
//   fileNames.push_back("DoubleEG_PRC_hadd.root");
//   fileNames.push_back("DoubleEG_PRD_hadd.root");
// 
//   fileNames.push_back("DoubleMuon_PRB_hadd.root");
//   fileNames.push_back("DoubleMuon_PRC_hadd.root");
//   fileNames.push_back("DoubleMuon_PRD_hadd.root");
// 
//   fileNames.push_back("MuonEG_PRB_hadd.root");
//   fileNames.push_back("MuonEG_PRC_hadd.root");
//   fileNames.push_back("MuonEG_PRD_hadd.root");

//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_ddbkgscan";
//   inputDir="LJMet80x_3lepTT_SUSYID_2016_10_31_rizki_step1hadds";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_ddbkgscan_FRv4_varyElFR";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_FRv5";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_FRv5_v2";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_ddbkgscan_muFR0p261bTag_varyElFR";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_ddbkgscan_2DFRscan";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_FRv6";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_FRv7_PRv2";
//   inputDir="LJMet80x_3lepTT_2016_10_13_rizki_withNonIsoTrig_fixedST_step1hadds";


   fileNames.push_back("DoubleEG_RRB_hadd.root");
   fileNames.push_back("DoubleMuon_RRB_hadd.root");
   fileNames.push_back("MuonEG_RRB_hadd.root");
   fileNames.push_back("DoubleEG_RRC_hadd.root");
   fileNames.push_back("DoubleMuon_RRC_hadd.root");
   fileNames.push_back("MuonEG_RRC_hadd.root");
   fileNames.push_back("DoubleEG_RRD_hadd.root");
   fileNames.push_back("DoubleMuon_RRD_hadd.root");
   fileNames.push_back("MuonEG_RRD_hadd.root");
   fileNames.push_back("DoubleEG_RRE_hadd.root");
   fileNames.push_back("DoubleMuon_RRE_hadd.root");
   fileNames.push_back("MuonEG_RRE_hadd.root");
   fileNames.push_back("DoubleEG_RRF_hadd.root");
   fileNames.push_back("DoubleMuon_RRF_hadd.root");
   fileNames.push_back("MuonEG_RRF_hadd.root");
   fileNames.push_back("DoubleEG_RRG_hadd.root");
   fileNames.push_back("DoubleMuon_RRG_hadd.root");
   fileNames.push_back("MuonEG_RRG_hadd.root");
   fileNames.push_back("DoubleEG_PRH_hadd.root");
   fileNames.push_back("DoubleMuon_PRH_hadd.root");
   fileNames.push_back("MuonEG_PRH_hadd.root");
//    
// //   inputDir="LJMet80x_3lepTT_Full2016_2016_12_15_rizki_withNonIsoTrig_step1hadds";
// //   inputDir="LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_mcICHEP_2016_12_15_rizki_withNonIsoTrig_addDZforRunH_fixedST_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_PRv2_FRv8_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_PRv2_FRv9_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_PRv2_FRv10_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_2016_12_19_rizki_withNonIsoTrig_fixedST_looseLepjetClean_PRv3_FRv11_ClintsAN16-242_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv9_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv12_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv13_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv2_FRv12_muMinIso0p1_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv3_FRv14_muMinIso0p1_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv14a_muMinIso0p1_20Jan2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv14a_muMinIso0p2_20Jan2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv15_20Jan2017_updatedbtagWP_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv15b_20Jan2017_updatedbtagWP_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv4_FRv15b_26Jan2017_lepPt30_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_HLTupdate_2017_1_11_rizki_PRv5test_FRv15b_26Jan2017_lepPt30_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv17b_2Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv18b_3Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv18b_6Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv18bSys_6Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv18bSys_6Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv19test_6Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv7test_FRv18bSys_7Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv19test_7Feb2017_step1hadds";
//   inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv6_FRv19testV2_7Feb2017_step1hadds";
  inputDir="LJMet80x_3lepTT_Full2016_Moriond17_newJEC_newElMVA_2017_1_30_rizki_PRv8test_FRv18bSys_7Feb2017_step1hadds";

  subDir="nominal";

  outputDir=inputDir+"_step2";
  
  //copy input to output folder
//   system("cp -r "+bruxDir+"/"+inputDir+" "+bruxDir+"/"+outputDir);
  
  //create folder to save original overlapping datasets
//   system("mkdir -pv "+bruxDir+"/"+outputDir+"/"+subDir+"/overlappingSets");
    
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  for(int i=0; i< fileNames.size() ; i++){
  	
  	inputFile = bruxDir+"/"+inputDir+"/"+subDir+"/"+fileNames.at(i);
  	outputFile = bruxDir+"/"+outputDir+"/"+subDir+"/"+fileNames.at(i);
  	
//   	std::cout << "Moving original overlapping datasets to new folder:" << std::endl;
//   	system("mv -v "+bruxDir+"/"+outputDir+"/"+subDir+"/"+fileNames.at(i)+" "+bruxDir+"/"+outputDir+"/"+subDir+"/overlappingSets/");
  	std::cout << "" << std::endl;
  	
  	step2 t(inputFile,outputFile);
  	t.Loop();
  
  }
  
  system("mv -v CheckOverlap.txt "+bruxDir+"/"+outputDir);
  
  gApplication->Terminate();

}


