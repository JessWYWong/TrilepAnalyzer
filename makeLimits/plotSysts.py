import ROOT as R
from array import array
import math
import os,sys,itertools
from tdrStyle import *
setTDRStyle()
R.gROOT.SetBatch(1)

blind = True #stay blind to data when optimizing selections!
lumiPlot = '41.557'
lumiStr = '41p557'

distribution = 'STrebinnedv2'
signal = 'TTM1000'
Br = 'bW0p5_tZ0p25_tH0p25'
channelPrefix = 'triLep2017'

pfix = "optimization_FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv2_prefire_elIdSys_TrigEffWeight_pdf4LHC_hadds_step2_FIXelIdSys"
cutString = "NJets3_mllOS20_met20_isPassTrig_di1_nbjets1_ptRel8_bJet1Pt50_isPassTrilep1"
subDir = "thetaTemplates_rootfiles"
fileName = "templates_"+distribution+"_"+signal+"_"+Br+"_"+lumiStr+"fb.root"

if len(sys.argv)>1: pfix=sys.argv[1]

limitDir='/mnt/data/users/wwong/'+pfix+'/'+cutString+'/'+subDir+'/'

systematicList = ['pileup','prefire','btag','mistag','pdfNew','muRFcorrdNew','jec','jer','TrigEffWeight', 'elIdSys','elIsoSys','muIsoSys','muIdSys','FRSys','elPRsys','muFReta','muPRsys']
if len(sys.argv)>2: systematicList = [sys.argv[2]]


channels = ['EEE','EEM','EMM','MMM']
if len(sys.argv)>3: channels = [sys.argv[3]]

samples = ['ewk','top','ddbkg','sig']
if len(sys.argv)>4: samples = [sys.argv[4]]

RFile = R.TFile(limitDir+fileName)

colorList = [R.kRed, R.kBlack, R.kBlue] # up, nm, dn
def plotShift(hname, hNm, hUp, hDn):
	canv = R.TCanvas(hname, hname, 1000,700)
	yDiv = 0.3
	uPad=R.TPad('uPad','',0,yDiv,1,1)
	uPad.SetTopMargin(0.1)
	uPad.SetBottomMargin(0)
	uPad.SetRightMargin(.05)
	uPad.SetLeftMargin(.12)
	uPad.Draw()
	lPad=R.TPad("lPad","",0,0,1,yDiv) #for sigma runner
	lPad.SetTopMargin(0)
	lPad.SetBottomMargin(.4)
	lPad.SetRightMargin(.05)
	lPad.SetLeftMargin(.12)
	lPad.SetGridy()
	lPad.Draw()
	uPad.cd()
	R.gStyle.SetOptTitle(0)
	for i,h in enumerate([hUp,hNm,hDn]):
		#h.SetFillColor(R.kWhite)
		h.SetMarkerColor(colorList[i])
		h.SetLineColor(colorList[i])
		h.SetMarkerStyle(2)
		h.SetMarkerSize(4)
		h.SetLineWidth(2)
		h.SetLineStyle(1)
	hUp.GetYaxis().SetTitle('Events')
	hUp.GetYaxis().SetLabelSize(0.08)
	hUp.GetYaxis().SetTitleSize(0.08)
	hUp.GetYaxis().SetTitleOffset(.53)
	hUp.GetYaxis().SetRangeUser(0.0001,1.1*max(hUp.GetMaximum(),hNm.GetMaximum(),hDn.GetMaximum()))
	hUp.Draw()
	hNm.Draw('same')
	hDn.Draw('same')

	lPad.cd()
	R.gStyle.SetOptTitle(0)
	pulls = []
	maxD = 0.
	for h in [hUp, hDn]:
		pull = h.Clone()
		for iBin in range(0,pull.GetXaxis().GetNbins()+2):
			pull.SetBinContent(iBin,pull.GetBinContent(iBin)-hNm.GetBinContent(iBin))
			pull.SetBinError(iBin,math.sqrt(pull.GetBinError(iBin)**2+hNm.GetBinError(iBin)**2))
			if (not hNm.GetBinContent(iBin) == 0.0) and (math.fabs(pull.GetBinContent(iBin)-hNm.GetBinContent(iBin))/hNm.GetBinContent(iBin)) > maxD:
				maxD = math.fabs(pull.GetBinContent(iBin)-hNm.GetBinContent(iBin))/hNm.GetBinContent(iBin)
		pull.Divide(hNm)
		pull.SetTitle('')
		#pull.SetFillColor(2)
		#pull.SetLineColor(2)
		pull.SetMarkerSize(4)
		pull.SetMarkerStyle(2)
		pull.GetXaxis().SetLabelSize(.12)
		pull.GetXaxis().SetTitleSize(0.15)
		pull.GetXaxis().SetTitleOffset(0.95)
		pull.GetYaxis().SetTitle('#frac{Up/Down-Nom}{Nom}')#'Python-C++'
		pull.GetYaxis().CenterTitle(1)
		pull.GetYaxis().SetLabelSize(0.15)
		pull.GetYaxis().SetTitleSize(0.08)
		pull.GetYaxis().SetTitleOffset(.65)
		pull.GetYaxis().SetNdivisions(506)
		pulls.append(pull)
	pulls[0].GetYaxis().SetRangeUser(-maxD, maxD)
	pulls[0].SetMarkerColor(colorList[0])
	pulls[0].SetLineColor(colorList[0])
	pulls[1].SetMarkerColor(colorList[2])
	pulls[1].SetLineColor(colorList[2])
	pulls[0].Draw()
	pulls[1].Draw('same')
	lPad.RedrawAxis()

	uPad.cd()
	legend = R.TLegend(0.6,0.63,0.9,0.88)
	legend.SetShadowColor(0);
	legend.SetFillColor(0);
	legend.SetLineColor(0);
	legend.AddEntry(hNm,'Nominal','l')
	legend.AddEntry(hUp, hname.split("__")[-1]+' Up', 'l')
	legend.AddEntry(hDn, hname.split("__")[-1]+' Down', 'l')
	legend.Draw('same')
	prelimTex=R.TLatex()
	prelimTex.SetNDC()
	prelimTex.SetTextAlign(31) # align right
	prelimTex.SetTextFont(42)
	prelimTex.SetTextSize(0.05)
	prelimTex.SetLineWidth(2)
	prelimTex.DrawLatex(0.90,0.943,str(lumiPlot)+" fb^{-1} (13 TeV)")
	prelimTex2=R.TLatex()
	prelimTex2.SetNDC()
	prelimTex2.SetTextFont(61)
	prelimTex2.SetLineWidth(2)
	prelimTex2.SetTextSize(0.07)
	prelimTex2.DrawLatex(0.18,0.9364,"CMS")
	prelimTex3=R.TLatex()
	prelimTex3.SetNDC()
	prelimTex3.SetTextAlign(13)
	prelimTex3.SetTextFont(52)
	prelimTex3.SetTextSize(0.040)
	prelimTex3.SetLineWidth(2)
	prelimTex3.DrawLatex(0.25175,0.9664,"Preliminary")
	Tex1=R.TLatex()
	Tex1.SetNDC()
	Tex1.SetTextSize(0.05)
	Tex1.SetTextAlign(31) # align right
	textx = 0.5
	Tex2 = R.TLatex()
	Tex2.SetNDC()
	Tex2.SetTextSize(0.05)
	Tex2.SetTextAlign(21)
	channelTxt = hname.split("__")[0].replace('trilep','3+l')
	Tex2.DrawLatex(textx, 0.83, channelTxt)
	canv.SaveAs(limitDir+signal+'_'+hname+'.pdf')


for syst in systematicList:
	print "================= Ploting "+syst+" ================="
	for ch in channels:
		for sample in samples:
			hNm_name = channelPrefix+ch+"__"+sample
			print hNm_name
			hname = hNm_name+"__"+syst
			hNm = RFile.Get(hNm_name).Clone()
			hUp = RFile.Get(hname+"__plus").Clone()
			hDn = RFile.Get(hname+"__minus").Clone()
			plotShift(hname, hNm, hUp, hDn)

RFile.Close()
