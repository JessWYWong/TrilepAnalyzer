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

   fileNames.push_back("DoubleMuon_RunA_hadd.root");
   fileNames.push_back("DoubleMuon_RunB_hadd.root");
   fileNames.push_back("DoubleMuon_RunC_hadd.root");
   fileNames.push_back("DoubleMuon_RunD_hadd.root");

   fileNames.push_back("MuonEG_RunA_hadd.root");
   fileNames.push_back("MuonEG_RunB_hadd.root");
   fileNames.push_back("MuonEG_RunC_hadd.root");
   fileNames.push_back("MuonEG_RunD_hadd.root");

   fileNames.push_back("EGamma_RunA_hadd.root");
   fileNames.push_back("EGamma_RunB_hadd.root");
   fileNames.push_back("EGamma_RunC_hadd.root");
   fileNames.push_back("EGamma_RunD_hadd.root");

//    
  inputDir="LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_step1hadds";
  
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


