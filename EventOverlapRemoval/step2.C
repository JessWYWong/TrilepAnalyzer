#define step2_cxx
#include "step2.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>
#include <fstream>

void step2::Loop()
{
//   In a ROOT session, you can do:
//      root> .L step2.C
//      root> step2 t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    inputTree->SetBranchStatus("*",0);  // disable all branches
//    inputTree->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    inputTree->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (inputTree == 0) return;
   
   // OUTPUT FILE
   outputFile->cd();
   TTree *outputTree = new TTree("ljmet","ljmet");
   outputTree = inputTree->CloneTree(0);

   int duplicates=0;
   int uniques=0;

   //read CheckOverlap event filter file                                                                                                                                                                         
   vector <int> CheckOverlap_run;
   vector <int> CheckOverlap_ls;
   vector <int> CheckOverlap_event;

   //creates empty file if it doesn exist and //ios::app = All output operations are performed at the end of the file, appending the content to the current content of the file.
   ofstream outfileCheckOverlapm( "CheckOverlap.txt", ios::app);    
   
   cout << "Reading CheckOverlap.txt file and saving unique events" << std::endl;
   ifstream infileCheckOverlapm( "CheckOverlap.txt" ); 
   while (infileCheckOverlapm)
   {
     string s;
     if (!getline( infileCheckOverlapm, s ))break;

     istringstream ss( s );
     vector <string> line;
     while (ss)
     {
       string s;
       if (!getline( ss, s, ':' ))break;
       line.push_back( s );
     }
     CheckOverlap_run.push_back( std::atoi(line[0].c_str()) );
     CheckOverlap_ls.push_back( std::atoi(line[1].c_str()) );
     CheckOverlap_event.push_back( std::atoi(line[2].c_str()) );
   }
   if (!infileCheckOverlapm.eof())
   {
     cerr << "Error while reading CheckOverlap.txt file!\n";
   }
   infileCheckOverlapm.close();  
   cout << "Done reading CheckOverlap.txt file, testing vector size" << std::endl;
   cout << "Nevents = " << CheckOverlap_run.size() << ", " << CheckOverlap_ls.size() << ", " << CheckOverlap_event.size() << std::endl;
   
   Long64_t nentries = inputTree->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = inputTree->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      
//       if(jentry>10) break;
      
      std::cout << "run / lumi / event : " << run_CommonCalc << " / " << lumi_CommonCalc << " / "<< event_CommonCalc ;

      //CheckOverlap filter                                                                                                 
      bool filterEvent = false;
      for(unsigned int i=0; i < CheckOverlap_run.size(); i++){
        if(CheckOverlap_run[i]==run_CommonCalc && CheckOverlap_ls[i]==lumi_CommonCalc && CheckOverlap_event[i]==event_CommonCalc) filterEvent = true;
      }
      if(filterEvent){
		  std::cout << " ----> Skipping overlap" << std:: endl;
		  duplicates++;
		  continue;
      }
      else{
		  std::cout << " ----> Writing" << std::endl ; 
		  outfileCheckOverlapm << run_CommonCalc << ":" << lumi_CommonCalc << ":"<< event_CommonCalc << "\n"; 
      }
      
      uniques++;
      outputTree->Fill();

   }
   
   std::cout << "" << std::endl;
   std::cout << "Total Events     : " << nentries << std::endl;
   std::cout << "Total duplicates : " << duplicates << std::endl;
   std::cout << "Total uniques    : " << uniques << std::endl;
   std::cout << "" << std::endl;
   std::cout << "DONE!" << std::endl;
   
   outfileCheckOverlapm.close();
   
   outputTree->Write();
   
}
