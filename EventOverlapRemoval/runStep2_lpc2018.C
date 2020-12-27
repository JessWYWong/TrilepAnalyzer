#include "step2.C"

void runStep2_lpc2018(){
  
  
  std::vector<TString> inputFiles;
  std::vector<TString> outputFiles;

  TString inputFile;
  TString outputFile;
  TString bruxDir;
  TString BaseDir;
  TString inputDir;
  TString subDir;
  TString outputDir;
  TString outputbruxDir;  
  
  //bruxDir ="/user_data/rsyarif";
  BaseDir = "root://cmseos.fnal.gov//store/user/wiwong/";

  std::vector<TString> fileNames;

   /*
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
   fileNames.push_back("DoubleEG_RRF_v2_hadd.root");
   fileNames.push_back("DoubleMuon_RRF_v2_hadd.root");
   fileNames.push_back("MuonEG_RRF_v2_hadd.root");
   */
   /*
   fileNames.push_back("DoubleEGRun2017B_hadd.root");
   fileNames.push_back("DoubleEGRun2017C_hadd.root");
   fileNames.push_back("DoubleEGRun2017D_hadd.root");
   fileNames.push_back("DoubleEGRun2017E_hadd.root");
   fileNames.push_back("DoubleEGRun2017F_hadd.root");
   fileNames.push_back("MuonEGRun2017B_hadd.root");
   fileNames.push_back("MuonEGRun2017C_hadd.root");
   fileNames.push_back("MuonEGRun2017D_hadd.root");
   fileNames.push_back("MuonEGRun2017E_hadd.root");
   fileNames.push_back("MuonEGRun2017F_hadd.root");
   fileNames.push_back("DoubleMuonRun2017B_hadd.root");
   fileNames.push_back("DoubleMuonRun2017C_hadd.root");
   fileNames.push_back("DoubleMuonRun2017D_hadd.root");
   fileNames.push_back("DoubleMuonRun2017E_hadd.root");
   fileNames.push_back("DoubleMuonRun2017F_hadd.root");
   */

   fileNames.push_back("EGammaRun2018A_hadd.root");
   fileNames.push_back("EGammaRun2018B_hadd.root");
   fileNames.push_back("EGammaRun2018C_hadd.root");
   fileNames.push_back("EGammaRun2018D_hadd.root");
   fileNames.push_back("MuonEGRun2018A_hadd.root");
   fileNames.push_back("MuonEGRun2018B_hadd.root");
   fileNames.push_back("MuonEGRun2018C_hadd.root");
   fileNames.push_back("MuonEGRun2018D_hadd.root");
   fileNames.push_back("DoubleMuonRun2018A_hadd.root");
   fileNames.push_back("DoubleMuonRun2018B_hadd.root");
   fileNames.push_back("DoubleMuonRun2018C_hadd.root");
   fileNames.push_back("DoubleMuonRun2018D_hadd.root");

  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds";
  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv1hadds";  
  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv2hadds";  
  //inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds";  
  //inputDir="FWLJMET102X_3lep2017_062019_wywong_step1_FRv1_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_UnityMuPR_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_012020_step1_FRv3_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_012020_step1_FRv3_UnityMuPR_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_MuFREta_hadds";
  //inputDir="FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_uFR_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_FRv1_TrigEff_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_etaFR_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_etaFRv2_DeepCSV_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_muPR_hadds";
  //inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_elIdSys_TrigEffWeight_pdfNew_hadds";
  inputDir="FWLJMET102X_3lep2018_wywong_052020_step1_FRv2_PRv2_elIdSys_TrigEffWeight_pdf4LHC_hadds";
  //subDir="nominal";
  //subDir="";

  outputbruxDir="/mnt/data/users/wwong";
  outputDir=inputDir+"_step2";
  
  // create output directory if not already exist 
  system("if [ ! -d \""+outputbruxDir+"/"+outputDir+"\" ]; then mkdir -p "+outputbruxDir+"/"+outputDir+"; fi");

  // do it with a separte script! copy input to output folder --> this is currently unnecessarily wastes space since it copies the same exact MC files to "_step2" folder. But convenient in terms of organization.
  //system("xrdcp -r "+BaseDir+"/"+inputDir+"/ "+outputbruxDir+"/"+outputDir);

  //system("bash movefiles_fromlpc.sh "+outputbruxDir+" "+outputDir+" "+inputDir);
  //system("bash moveTTfiles_fromlpc.sh "+outputbruxDir+" "+outputDir+" "+inputDir);
  
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  for(int i=0; i< fileNames.size() ; i++){
  	
  	inputFile = BaseDir+"/"+inputDir+"/"+subDir+fileNames.at(i);
  	outputFile = outputbruxDir+"/"+outputDir+"/"+fileNames.at(i);
  	
  	std::cout << "" << std::endl;
  	
  	step2 t(inputFile,outputFile);
  	t.Loop();
  
  }
  
  system("mv -v CheckOverlap.txt "+outputbruxDir+"/"+outputDir);
  
  gApplication->Terminate();

}


