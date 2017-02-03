

void TEMP_rootMacro(){

  //TFile *f = TFile::Open("/user_data/rsyarif/LJMet80x_3lepTT_2016_8_31_rizki_step1hadds/nominal/DoubleMuon_PRB_hadd.root");
  TFile *f = TFile::Open("/user_data/rsyarif/LJMet80x_3lepTT_2016_8_31_rizki_step1hadds/nominal/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root");

  TTree *t = (TTree*) f->Get("ljmet");

  TString cut1 = "1 ";
  TString cut2 = "1 && (AllLeptonPt_PtOrdered[0] > 0) ";
  TString cut3 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) ";
  TString cut4 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) ";
  TString cut5 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) && (NJetsCSVwithSF_JetSubCalc >= 0) ";
  TString cut6 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) && (NJetsCSVwithSF_JetSubCalc >= 0) && MCPastTrigger_dilep == 1 ";
  TString cut7 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) && (NJetsCSVwithSF_JetSubCalc >= 0) && MCPastTrigger_dilep == 1 && isPassTrilepton == 1 ";
  TString cut8 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) && (NJetsCSVwithSF_JetSubCalc >= 0) && MCPastTrigger_dilep == 1 && isPassTrilepton == 1 && (AK4HTpMETpLepPt >= 0) ";
  TString cut9 = "1 && (AllLeptonPt_PtOrdered[0] > 0) && (corr_met_singleLepCalc > 0) && (NJets_JetSubCalc >= 2) && (NJetsCSVwithSF_JetSubCalc >= 0) && MCPastTrigger_dilep == 1 && isPassTrilepton == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3";
  
  std::cout << "cut1 = " << t->Draw("AllLeptonCount_PtOrdered",cut1)<< std::endl;
  std::cout << "cut2 = " << t->Draw("AllLeptonCount_PtOrdered",cut2)<< std::endl;
  std::cout << "cut3 = " << t->Draw("AllLeptonCount_PtOrdered",cut3)<< std::endl;
  std::cout << "cut4 = " << t->Draw("AllLeptonCount_PtOrdered",cut4)<< std::endl;
  std::cout << "cut5 = " << t->Draw("AllLeptonCount_PtOrdered",cut5)<< std::endl;
  std::cout << "cut6 = " << t->Draw("AllLeptonCount_PtOrdered",cut6)<< std::endl;
  std::cout << "cut7 = " << t->Draw("AllLeptonCount_PtOrdered",cut7)<< std::endl;
  std::cout << "cut8 = " << t->Draw("AllLeptonCount_PtOrdered",cut8)<< std::endl;
  std::cout << "cut9 = " << t->Draw("AllLeptonCount_PtOrdered",cut9)<< std::endl;

}
