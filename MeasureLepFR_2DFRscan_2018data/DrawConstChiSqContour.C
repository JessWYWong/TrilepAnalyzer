
#include "SetTDRStyle.cc"

void DrawConstChiSqContour(TFile *f,TString outname,Double_t xp, Double_t yp){

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
  c->SetBottomMargin(0.10);

  TH2D *h = (TH2D*) f->Get("chiSq_sum");

  h->GetXaxis()->SetTitle("#mu misidentification rate");
  h->GetYaxis()->SetTitle("#it{e} misidentification rate");
//   h->GetZaxis()->SetTitle("#bar{#chi^{2}}");

  h->Draw("colzcont2");

  double minRange = 0.01;
  double maxRange = 0.5;
  
  //bin = 1 is x = 0.0

  Double_t x = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(xp) );
  Double_t y = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(yp) );
  
  Double_t minChiSq = h->GetBinContent(h->GetXaxis()->FindBin(xp),h->GetYaxis()->FindBin(yp));
  std::cout << "minChiSq = " << minChiSq << std::endl;
  Double_t chiSq = 0;
  std::vector<int> x_cont;
  std::vector<int> y_cont;
  TMarker *cont; 
  for(int xbin=0; xbin <= h->GetNbinsX(); xbin++){
  	for(int ybin=0; ybin <= h->GetNbinsY(); ybin++){
  		chiSq = h->GetBinContent(xbin,ybin);
  		if(fabs(minChiSq-chiSq) <= 2.30 && minChiSq!=chiSq){
  			std::cout << "chiSq (" << xbin-1<<", "<< ybin-1<< ") = " << chiSq << " --> |chiSq-minChiSq| = " << fabs(minChiSq-chiSq) <<" < 2.30"<<std::endl;	
  			x_cont.push_back(xbin);
  			y_cont.push_back(ybin);
  			cont = new TMarker(h->GetXaxis()->GetBinCenter(xbin),h->GetYaxis()->GetBinCenter(ybin),7);
  			cont->Draw("same");
  			//h->SetBinContent(xbin,ybin,2000);
  		}
  	}
  }
  
  Double_t xmin = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(minRange) );
  Double_t ymin = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(minRange) );
  Double_t xmax = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(maxRange) );
  Double_t ymax = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(maxRange) );

  TMarker *m = new TMarker(x,y,5);
  m->Draw("same");

  TLine *l_hor = new TLine(xmin,y,xmax,y);
  TLine *l_ver = new TLine(x,ymin,x,ymax);

  l_hor->Draw("same");
  l_ver->Draw("same");
  
  h->GetXaxis()->SetRangeUser(minRange,maxRange);
  h->GetYaxis()->SetRangeUser(minRange,maxRange);
  
  h->SetTitle("");
  float_t labelSize = 0.04;
  
  h->GetYaxis()->SetTitleOffset(1.3);
  h->GetYaxis()->SetLabelSize(labelSize);
  h->GetYaxis()->SetTitleSize(labelSize);
  h->GetYaxis()->SetNdivisions(5);

  h->GetXaxis()->SetTitleOffset(1.1);
  h->GetXaxis()->SetLabelSize(labelSize);
  h->GetXaxis()->SetTitleSize(labelSize);
  h->GetXaxis()->SetNdivisions(5);

  h->GetZaxis()->SetLabelSize(labelSize);


  TLatex* prelimTex = new TLatex();
  prelimTex->SetNDC();
  prelimTex->SetTextAlign(31); // align right                                           
  prelimTex->SetTextFont(42);
//   prelimTex->SetTextSize(0.07);
  prelimTex->SetTextSize(labelSize);
  prelimTex->SetLineWidth(2);
//   prelimTex->DrawLatex(0.95,0.94,"#bar{#chi^{2}}");

  TLatex* prelimTex2= new TLatex();
  prelimTex2->SetNDC();
  prelimTex2->SetTextFont(61);
  prelimTex2->SetLineWidth(2);
  prelimTex2->SetTextSize(0.07);
  prelimTex2->DrawLatex(0.1,0.93,"CMS");


//   c->SaveAs(outname+".png");
 c->SaveAs(outname+"_1SigmaContour.pdf");
//   c->SaveAs(outname+".C");

}

void DrawProbChiSq(TFile *f,TString outname,Double_t xp, Double_t yp){

  //set TDRStyle
  setTDRStyle();   

  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);


  TCanvas *c = new TCanvas("prob_chiSq","prob_chiSq",900,800);
//   TCanvas *c = new TCanvas("chiSq","chiSq",600,500);
  c->SetRightMargin(0.125);
  c->SetTopMargin(0.10);
  c->SetLeftMargin(0.10);
  c->SetRightMargin(0.15);
  c->SetBottomMargin(0.10);
  c->SetLogz();

  TH2D *h = (TH2D*) f->Get("chiSq_sum");

  h->GetXaxis()->SetTitle("#mu misidentification rate");
  h->GetYaxis()->SetTitle("#it{e} misidentification rate");
//   h->GetZaxis()->SetTitle("#bar{#chi^{2}}");

  h->Draw("colzcont2");
  //h->Draw("Legocont2");

  double minRange = 0.01;
  double maxRange = 0.5;
  
  //bin = 1 is x = 0.0

  Double_t x = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(xp) );
  Double_t y = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(yp) );
  
  Double_t minChiSq = h->GetBinContent(h->GetXaxis()->FindBin(xp),h->GetYaxis()->FindBin(yp));
  std::cout << "minChiSq = " << minChiSq << std::endl;
  Double_t chiSq = 0;
  TMarker *cont; 
  for(int xbin=1; xbin < h->GetNbinsX(); xbin++){
  	for(int ybin=1; ybin < h->GetNbinsY(); ybin++){
  		chiSq = h->GetBinContent(xbin,ybin);
		double prob_chiSq  = exp( - (chiSq) / 2 );
		std::cout << "chiSq (" << xbin-1<<", "<< ybin-1<< ") = " << chiSq << " --> prob ~ " << prob_chiSq<<std::endl;	
		h->SetBinContent(xbin,ybin,prob_chiSq);
  	}
  }
  double norm = h->Integral();
  h->Scale(1/norm);
  std::cout << "h->Integral() = " << h->Integral() << std::endl;
    
  Double_t xmin = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(minRange) );
  Double_t ymin = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(minRange) );
  Double_t xmax = h->GetXaxis()->GetBinCenter( h->GetXaxis()->FindBin(maxRange) );
  Double_t ymax = h->GetYaxis()->GetBinCenter( h->GetYaxis()->FindBin(maxRange) );

  TMarker *m = new TMarker(x,y,5);
  m->Draw("same");

  TLine *l_hor = new TLine(xmin,y,xmax,y);
  TLine *l_ver = new TLine(x,ymin,x,ymax);

  l_hor->Draw("same");
  l_ver->Draw("same");
  
  h->GetXaxis()->SetRangeUser(minRange,maxRange);
  h->GetYaxis()->SetRangeUser(minRange,maxRange);
  
  h->SetTitle("");
  float_t labelSize = 0.04;
  
  h->GetYaxis()->SetTitleOffset(1.3);
  h->GetYaxis()->SetLabelSize(labelSize);
  h->GetYaxis()->SetTitleSize(labelSize);
  h->GetYaxis()->SetNdivisions(5);

  h->GetXaxis()->SetTitleOffset(1.1);
  h->GetXaxis()->SetLabelSize(labelSize);
  h->GetXaxis()->SetTitleSize(labelSize);
  h->GetXaxis()->SetNdivisions(5);

  h->GetZaxis()->SetLabelSize(labelSize);


  TLatex* prelimTex = new TLatex();
  prelimTex->SetNDC();
  prelimTex->SetTextAlign(31); // align right                                           
  prelimTex->SetTextFont(42);
//   prelimTex->SetTextSize(0.07);
  prelimTex->SetTextSize(labelSize);
  prelimTex->SetLineWidth(2);
  prelimTex->DrawLatex(0.95,0.94,"P(#mu_{MR},#it{e}_{MR})");

  TLatex* prelimTex2= new TLatex();
  prelimTex2->SetNDC();
  prelimTex2->SetTextFont(61);
  prelimTex2->SetLineWidth(2);
  prelimTex2->SetTextSize(0.07);
  prelimTex2->DrawLatex(0.1,0.93,"CMS");
  

//   c->SaveAs(outname+".png");
 c->SaveAs(outname+"_Probability.pdf");
//   c->SaveAs(outname+".C");

  TCanvas *cx = new TCanvas("prob_chiSq_x","prob_chiSq_x",900,800);
  TH1D *hx = new TH1D("hx","hx",h->GetNbinsX(),0,h->GetNbinsX());

  //squash horizontally
  for(int xbin=0; xbin < h->GetNbinsX(); xbin++){
  	double tot_y=0;
  	for(int ybin=0; ybin < h->GetNbinsY(); ybin++){
  		tot_y += h->GetBinContent(xbin,ybin);
  	}
  	hx->SetBinContent(xbin,tot_y);
  	std::cout << "xbin = " << xbin << ", tot_y = " << tot_y <<std::endl;
  }
  hx->GetXaxis()->SetTitle("#mu misidentification rate");
  hx->Fit("gaus","R","",10,25); // pay attention to the init condition : range !
  //hx->Fit("gaus");
  hx->Draw();
  std::cout << "hx->Integral() = " << hx->Integral() << std::endl;
  cx->SaveAs(outname+"_x_Probability.pdf");
  cx->SaveAs(outname+"_x_Probability.root");

  TCanvas *cy = new TCanvas("prob_chiSq_y","prob_chiSq_y",900,800);
  TH1D *hy = new TH1D("hy","hy",h->GetNbinsY(),0,h->GetNbinsX());
  //squash vertically
  for(int ybin=0; ybin < h->GetNbinsY(); ybin++){
  	double tot_x=0;
  	for(int xbin=0; xbin < h->GetNbinsX(); xbin++){
  		tot_x += h->GetBinContent(xbin,ybin);
  	}
  	hy->SetBinContent(ybin,tot_x);
  	std::cout << "ybin = " << ybin << ", tot_x = " << tot_x <<std::endl;
  }
  hy->GetXaxis()->SetTitle("#it{e} misidentification rate");
  hy->Fit("gaus","R","",1,25); // pay attention to the init condition : range !!!
  //hy->Fit("gaus");
  hy->Draw();
  std::cout << "hy->Integral() = " << hy->Integral() << std::endl;
  cy->SaveAs(outname+"_y_Probability.pdf");
  cy->SaveAs(outname+"_y_Probability.root");


}


void DrawConstChiSqContour(){

  //enter fake rates here to draw
  float muFR = 0.17 ;
  float elFR = 0.09 ; 

  TString brux_dir ="/user_data/rsyarif";
  TString dir ="measureFR_LJMet102x_3lepTT_2018datasets_2018_11_22_rizki_FRCR2_2018_12_13";
  TString filename = "chiSq_lepPt_58p83fb.root";
  TString saveDir = "chiSq_plots";

  gSystem->Exec("mkdir -vp "+saveDir);
  f = TFile::Open(brux_dir+"/"+dir+"/"+filename);
  DrawConstChiSqContour(f,"chiSq_lepPt_"+dir,muFR,elFR);
  DrawProbChiSq(f,"chiSq_lepPt_"+dir,muFR,elFR);
  f->Close();

  gSystem->Exec("mv -v chiSq* "+saveDir);

  gApplication->Terminate();

}
