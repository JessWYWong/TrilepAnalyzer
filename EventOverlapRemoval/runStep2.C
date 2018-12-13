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
    
  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1hadds";
  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv1hadds";  
  //  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv2hadds";  
  inputDir="LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_step1_FRv3hadds";  

  subDir="nominal";

  outputDir=inputDir+"_step2";
  
  //copy input to output folder --> this is currently unnecessarily wastes space since it copies the same exact MC files to "_step2" folder. But convenient in terms of organization.
  system("cp -vr "+bruxDir+"/"+inputDir+" "+bruxDir+"/"+outputDir);
      
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  for(int i=0; i< fileNames.size() ; i++){
  	
  	inputFile = bruxDir+"/"+inputDir+"/"+subDir+"/"+fileNames.at(i);
  	outputFile = bruxDir+"/"+outputDir+"/"+subDir+"/"+fileNames.at(i);
  	
  	std::cout << "" << std::endl;
  	
  	step2 t(inputFile,outputFile);
  	t.Loop();
  
  }
  
  system("mv -v CheckOverlap.txt "+bruxDir+"/"+outputDir);
  
  gApplication->Terminate();

}


