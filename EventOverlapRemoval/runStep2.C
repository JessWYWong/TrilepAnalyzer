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
  
  std::vector<TString> fileNames;
  
  fileNames.push_back("DoubleEG_PRB_hadd.root");
  fileNames.push_back("DoubleEG_PRC_hadd.root");
  fileNames.push_back("DoubleEG_PRD_hadd.root");

  fileNames.push_back("DoubleMuon_PRB_hadd.root");
  fileNames.push_back("DoubleMuon_PRC_hadd.root");
  fileNames.push_back("DoubleMuon_PRD_hadd.root");

  fileNames.push_back("MuonEG_PRB_hadd.root");
  fileNames.push_back("MuonEG_PRC_hadd.root");
  fileNames.push_back("MuonEG_PRD_hadd.root");

  bruxDir ="/user_data/rsyarif";
  inputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds";
  subDir="nominal";
  outputDir="LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_step2";
  
  //copy input to output folder
  system("cp -r "+bruxDir+"/"+inputDir+" "+bruxDir+"/"+outputDir);
  
  //create folder to save original overlapping datasets
  system("mkdir -pv "+bruxDir+"/"+outputDir+"/"+subDir+"/overlappingSets");
    
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  for(int i=0; i< fileNames.size() ; i++){
  	
  	inputFile = bruxDir+"/"+inputDir+"/"+subDir+"/"+fileNames.at(i);
  	outputFile = bruxDir+"/"+outputDir+"/"+subDir+"/"+fileNames.at(i);
  	
  	std::cout << "Moving original overlapping datasets to new folder:" << std::endl;
  	system("mv -v "+bruxDir+"/"+outputDir+"/"+subDir+"/"+fileNames.at(i)+" "+bruxDir+"/"+outputDir+"/"+subDir+"/overlappingSets/");
  	std::cout << "" << std::endl;
  	
  	step2 t(inputFile,outputFile);
  	t.Loop();
  
  }
  
  system("mv -v CheckOverlap.txt "+bruxDir+"/"+outputDir);
  
  gApplication->Terminate();

}


