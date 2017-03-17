

void DrawChiSq(TFile *f,TString outname,Double_t xp, Double_t yp){

  gStyle->SetOptStat(0);

  TCanvas *c = new TCanvas("chiSq","chiSq",800,800);

  TH2D *h = (TH2D*) f->Get("chiSq_average");

  h->GetXaxis()->SetTitle("#mu FR");
  h->GetYaxis()->SetTitle("el FR");

  h->Draw("colzcont2");

  Double_t x = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(xp) );
  Double_t y = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(yp) );

  Double_t xmin = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(0.) );
  Double_t ymin = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(0.) );

  Double_t xmax = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(0.5) );
  Double_t ymax = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(0.5) );

  TMarker *m = new TMarker(x,y,7);
  m->Draw("same");

  TLine *l_hor = new TLine(xmin,y,xmax,y);
  TLine *l_ver = new TLine(x,ymin,x,ymax);

  l_hor->Draw("same");
  l_ver->Draw("same");

  c->SaveAs(outname+".png");
  c->SaveAs(outname+".C");

}


void DrawChiSq(){

  TString filename;
  TFile *f ;
  
//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_2016_12_19/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_36p46fb",0.06,0.29);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_2017_1_9/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_36p46fb",0.16,0.26);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_1bjet_2017_1_9/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets1_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_IsoTrig_addDZforRunH_fixedST_looseLepjetClean_1bjet_36p46fb",0.31,0.20);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_2017_1_13/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_IsoTrig_HLTupdate_36p46fb",0.19,0.24);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_1bjet_2017_1_13/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets1_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_IsoTrig_HLTupdate_1bjet_36p46fb",0.30,0.21);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv2_Full2016_IsoTrig_HLTupdate_2017_1_16/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets1_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly1Jet_PRv2_IsoTrig_HLTupdate_36p46fb",0.04,0.22);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate_2017_1_17/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_muMinIso0p1_IsoTrig_HLTupdate_36p46fb",0.12,0.21);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv2_muMinIso0p1_Full2016_IsoTrig_HLTupdate_1bjet_2017_1_17/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets1_DR0_ST0_MllOS20/chiSq_STrebinned_36p46fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv2_muMinIso0p1_IsoTrig_HLTupdate_1bjet_36p46fb",0.12,0.21);
//   f->Close();


//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_2017_1_20/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_STrebinned_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv4_muMinIso0p1_IsoTrig_HLTupdate_36p814fb",0.12,0.23);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_2017_1_23/chiSq_STrebinned_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_STrebinned_exactly2Jets_PRv4_muMinIso0p1_IsoTrig_HLTupdate_1bjet_36p814fb",0.16,0.20);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_LepPt_2017_1_21/isPassTrig_All0_dilep1_dilepAnth0_trilep0_isPassTrilepton1_lep1Pt0_NJets2_NBJets0_DR0_ST0_MllOS20/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv4_muMinIso0p1_IsoTrig_HLTupdate_36p814fb",0.6,0.28);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_2017_1_23/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv4_muMinIso0p1_IsoTrig_HLTupdate_1bjet_36p814fb",0.15,0.22);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly2Jets_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_25/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv4_muMinIso0p1_IsoTrig_HLTupdate_1bjet_lepPt30_36p814fb",0.13,0.22);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_exactly1Jet_2DFRscan_PRv4_muMinIso0p1_Full2016_20Jan2017_updatedbtagWP_1bjet_lepPt30_2017_1_30/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly1Jet_PRv4_muMinIso0p1_IsoTrig_HLTupdate_1bjet_lepPt30_36p814fb",0.10,0.27);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet_2017_2_3/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv6_1bjet_lepPt30_36p814fb",0.11,0.25);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet_2017_2_3/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly1Jet_PRv6_1bjet_lepPt30_36p814fb",0.07,0.30);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv7test_1bjet_2017_2_7/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv7test_1bjet_lepPt30_36p814fb",0.11,0.25);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_7Feb2017_exactly2Jets_PRv8test_1bjet_2017_2_7/chiSq_lepPt_36p814fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv8test_1bjet_lepPt30_36p814fb",0.11,0.25);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly2Jets_PRv6_1bjet_newMllOS_fixedlumi_2017_2_27/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly2Jets_PRv6_1bjet_newMllOS_fixedlumi_35p867fb",0.11,0.24);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_80x_condor_Exactly3Lep_ddbkgscan_step2_2Feb2017_exactly1Jet_PRv6_1bjet_newMllOS_fixedlumi_2017_2_27/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_exactly1Jet_PRv6_1bjet_newMllOS_fixedlumi_35p867fb",0.08,0.30);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_FRCR2_2017_3_2/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv6_1bjet_LJMet24Feb2017_FRCR2_35p867fb",0.15,0.22);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_FRCR1_2017_3_2/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv6_1bjet_LJMet24Feb2017_FRCR1_35p867fb",0.13,0.29);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR2_2017_3_3/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv6_1bjet_LJMet24Feb2017_newMuTrkSF_FRCR2_35p867fb",0.15,0.23);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv6_LJMet24Feb2017_newMuTrkSF_FRCR1_2017_3_3/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv6_1bjet_LJMet24Feb2017_newMuTrkSF_FRCR1_35p867fb",0.13,0.29);
//   f->Close();
  
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv6_3Mar2017_scaleFR_CR2CR1_step1hadds_step2_FRCR2_2017_3_3/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv6_1bjet_3Mar2017_scaleFR_CR2CR1_35p867fb",0.10,0.30);
//   f->Close();

  filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR2_2017_3_9/chiSq_lepPt_35p867fb.root";
  f = TFile::Open(filename);
  DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet24Feb2017_postPreapproval_FRCR2_35p867fb",0.15,0.23);
  f->Close();

  filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR1_2017_3_9/chiSq_lepPt_35p867fb.root";
  f = TFile::Open(filename);
  DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet24Feb2017_postPreapproval_FRCR1_35p867fb",0.13,0.29);
  f->Close();



  gApplication->Terminate();

}
