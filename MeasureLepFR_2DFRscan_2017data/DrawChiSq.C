
#include "SetTDRStyle.cc"

void DrawChiSq(TFile *f,TString outname,Double_t xp, Double_t yp){

  //set TDRStyle
  setTDRStyle();   

  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);


  TCanvas *c = new TCanvas("chiSq","chiSq",900,800);
//   TCanvas *c = new TCanvas("chiSq","chiSq",600,500);
  c->SetRightMargin(0.125);
  c->SetTopMargin(0.10);
  c->SetLeftMargin(0.10);
  c->SetRightMargin(0.15);
  //c->SetRightMargin(0.20);
  c->SetBottomMargin(0.10);

  TH2D *h = (TH2D*) f->Get("chiSq_average");

  h->GetXaxis()->SetTitle("#mu misidentification rate");
  h->GetYaxis()->SetTitle("#it{e} misidentification rate");
  //h->GetZaxis()->SetTitle("#bar{#chi^{2}}");
  //h->GetZaxis()->SetTitle("#chi^{2}");
  //h->GetZaxis()->RotateTitle();
  //h->GetZaxis()->SetTitleOffset(1.4);

  h->Draw("colzcont2");

  double minRange = 0.01;
  double maxRange = 0.5;

  Double_t x = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(xp) );
  Double_t y = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(yp) );
  
  Double_t xmin = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(minRange) );
  Double_t ymin = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(minRange) );
  Double_t xmax = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(maxRange) );
  Double_t ymax = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(maxRange) );

  //TMarker *m = new TMarker(x,y,7);//dot
//   TMarker *m = new TMarker(x,y,5); //x
//   m->Draw("same");

  TLine *l_hor = new TLine(xmin,y,xmax,y);
  TLine *l_ver = new TLine(x,ymin,x,ymax);

  l_hor->Draw("same");
  l_ver->Draw("same");
  
  h->GetXaxis()->SetRangeUser(minRange,maxRange);
  h->GetYaxis()->SetRangeUser(minRange,maxRange);
  
  h->SetTitle("");
  float_t labelSize = 0.04;
  
  h->GetYaxis()->SetTitleOffset(1.3);
  h->GetYaxis()->SetLabelSize(labelSize*1.2);
  h->GetYaxis()->SetTitleSize(labelSize);
  h->GetYaxis()->SetNdivisions(5);

  h->GetXaxis()->SetTitleOffset(1.1);
  h->GetXaxis()->SetLabelSize(labelSize*1.2);
  h->GetXaxis()->SetTitleSize(labelSize);
  h->GetXaxis()->SetNdivisions(5);

  h->GetZaxis()->SetLabelSize(labelSize*1.2);


  TLatex* prelimTex = new TLatex();
  prelimTex->SetNDC();
  prelimTex->SetTextAlign(31); // align right                                           
  prelimTex->SetTextFont(42);
//   prelimTex->SetTextSize(0.07);
  prelimTex->SetTextSize(labelSize);
  prelimTex->SetLineWidth(2);
  //prelimTex->DrawLatex(0.95,0.94,"#bar{#chi^{2}}");
  prelimTex->DrawLatex(0.95,0.94,"#chi^{2}");

  TLatex* prelimTex2= new TLatex();
  prelimTex2->SetNDC();
  prelimTex2->SetTextFont(61);
  prelimTex2->SetLineWidth(2);
  prelimTex2->SetTextSize(0.07);
  prelimTex2->DrawLatex(0.1,0.93,"CMS");

  TLatex* prelimTex3= new TLatex();
  prelimTex3->SetNDC();
  prelimTex3->SetTextAlign(13);
  prelimTex3->SetTextFont(52);
  prelimTex3->SetTextSize(0.055);
  prelimTex3->SetLineWidth(2);
//   prelimTex3->DrawLatex(0.24,0.97,"Preliminary");


//   c->SaveAs(outname+".png");
  c->SaveAs(outname+".pdf");
  c->SaveAs(outname+".C");
  c->SaveAs(outname+".root");

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

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR2_2017_3_9/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet24Feb2017_postPreapproval_FRCR2_35p867fb",0.15,0.23);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_postPreapproval_FRCR1_2017_3_9/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet24Feb2017_postPreapproval_FRCR1_35p867fb",0.13,0.29);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR2_2017_3_25/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet21Mar2017_newRunH_FRCR2_35p867fb",0.16,0.23);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR1_2017_3_25/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet21Mar2017_newRunH_FRCR1_35p867fb",0.16,0.29);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_FRCR1CR2_2017_3_25/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_1bjet_LJMet21Mar2017_newRunH_FRCR1CR2_35p867fb",0.15,0.26);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2_2017_4_4/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRCR2_35p867fb_2017_4_4",0.16,0.23);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1_2017_4_4/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRCR1_35p867fb_2017_4_4",0.16,0.29);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1CR2_2017_4_4/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRCR1CR2_35p867fb_2017_4_4",0.15,0.26);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRST1000low_2017_6_21/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRST1000low_35p867fb_2017_6_21",0.17,0.38);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv10_newRunH_correctedMuTrSF_FRCR2_2017_7_4/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv10_newRunH_correctedMuTrSF_FRCR2_35p867fb_2017_7_4",0.16,0.24);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv10_newRunH_correctedMuTrSF_FRCR1_2017_7_4/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv10_newRunH_correctedMuTrSF_FRCR1_35p867fb_2017_7_4",0.16,0.29);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT600low_2017_7_19/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRHT600low_35p867fb_2017_7_19",0.18,0.38);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRmlllb400low_2017_7_21/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRmlllb400low_35p867fb_2017_7_19",0.17,0.34);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_2017_7_24/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_35p867fb_2017_7_24",0.16,0.36);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_2Dcut_2017_7_26/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRHT400low2D_35p867fb_2017_7_26",0.36,0.50);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRSRHT400low_2Dcut_extend_2017_7_27/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRSRHT400low2Dext_35p867fb_2017_7_27",0.35,0.52);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR2HT400low_2Dcut_extend_2017_7_27/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRCR2HT400low2Dext_35p867fb_2017_7_27",0.26,0.28);
//   f->Close();
// 
//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_correctedMuTrSF_FRCR1HT400low_2Dcut_extend_2017_7_27/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_correctedMuTrSF_FRCR1HT400low2Dext_35p867fb_2017_7_27",0.2,0.3);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRSRHT400low_2017_9_12/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_elMVAaltFix_FRSRHT400low_35p867fb_2017_9_12",0.18,0.25);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR2_2017_9_12/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_elMVAaltFix_FRCR2_35p867fb_2017_9_12",0.14,0.20);
//   f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR1_2017_9_13/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_average_lepPt_PRv9_newRunH_elMVAaltFix_FRCR1_35p867fb_2017_9_13",0.15,0.23);
//   f->Close();

  filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR2_2017_9_12/chiSq_lepPt_35p867fb.root";
  f = TFile::Open(filename);
  DrawChiSq(f,"chiSq_NOTaverage_lepPt_PRv9_newRunH_elMVAaltFix_FRCR2_35p867fb_2017_9_12",0.14,0.20);
  f->Close();

//   filename = "/user_data/rsyarif/kinematics_condor_ddbkgscan_PRv9_newRunH_elMVAaltFix_FRCR1_2017_9_13/chiSq_lepPt_35p867fb.root";
//   f = TFile::Open(filename);
//   DrawChiSq(f,"chiSq_NOTaverage_lepPt_PRv9_newRunH_elMVAaltFix_FRCR1_35p867fb_2017_9_13",0.15,0.23);
//   f->Close();


  gApplication->Terminate();

}
