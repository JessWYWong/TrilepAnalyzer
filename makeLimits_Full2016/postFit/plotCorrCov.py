from ROOT import *
from array import array
from math import *
import os,sys,pickle


gROOT.SetBatch(1)

from tdrStyle import *
setTDRStyle()

inputFile = "mle_covcorr_templates_minMlllBv4_TTM1000_bW0p5_tZ0p25_tH0p25_35p867fb_bkgonly"

file = ROOT.TFile(inputFile+'.root')

cov_plot = file.Get("covariance_matrix")
cor_plot = file.Get("correlation_matrix")


prelimTex2=TLatex()
prelimTex2.SetNDC()
prelimTex2.SetTextFont(61)
prelimTex2.SetLineWidth(2)
prelimTex2.SetTextSize(0.05)

prelimTex3=TLatex()
prelimTex3.SetNDC()
prelimTex3.SetTextAlign(13)
prelimTex3.SetTextFont(52)
prelimTex3.SetTextSize(0.05*0.7)
prelimTex3.SetLineWidth(2)


c_cov = TCanvas("canvas","canvas",1000,800)
c_cov.cd()
c_cov.SetRightMargin(0.1)
cov_plot.Draw("colz")
prelimTex2.DrawLatex(0.15,0.955,"CMS")
prelimTex3.DrawLatex(0.24,0.98,"Preliminary")

c_cov.SaveAs(inputFile+'_cov.pdf')

c_cor = TCanvas("canvas","canvas",1000,800)
c_cor.cd()
c_cor.SetRightMargin(0.1)
cor_plot.Draw("colz")
prelimTex2.DrawLatex(0.15,0.955,"CMS")
prelimTex3.DrawLatex(0.24,0.98,"Preliminary")
c_cor.SaveAs(inputFile+'_cor.pdf')
