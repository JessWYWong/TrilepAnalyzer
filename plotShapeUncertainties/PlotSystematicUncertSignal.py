import ROOT as R
import os,sys,math
from array import array

from tdrStyle import *
setTDRStyle()
R.gROOT.SetBatch(1)
outDir = os.getcwd()+'/'

lumi = 2.2
discriminant = 'ST'
rfilePostFix = ''
tempVersion = 'templates_ST_2016_4_26/'
cutString = '/lep0_MET0_1jet0_2jet0_NJets0_NBJets0_3jet0_4jet0_5jet0_DR0_1Wjet0_1bjet0_HT0_ST0_minMlb0'
templateFile = '/home/rsyarif/LJMet/TprimeAnalysis/CMSSW_7_6_3/src/TrilepAnalyzer/makeThetaTemplates/'+tempVersion+cutString+'/templates_'+discriminant+'_TTM900_2p215fb'+rfilePostFix+'.root'
if not os.path.exists(outDir+tempVersion): os.system('mkdir '+outDir+tempVersion)
if not os.path.exists(outDir+tempVersion+'/signals'): os.system('mkdir '+outDir+tempVersion+'/signals')

systematics = ['pileup','jec','jer','btag','jsf','muRFcorrdNew','pdfNew']
systematics+= ['elIdSys','muIdSys','elIsoSys','muIsoSys','elelelTrigSys','elelmuTrigSys','elmumuTrigSys','mumumuTrigSys']

signameList = [
		   'TTM700',
           'TTM800',
           'TTM900',
           'TTM1000',
           'TTM1100',
           'TTM1200',
           'TTM1300',
#            'TTM1400',
#            'TTM1500',
#            'TTM1600',
#            'TTM1700',
#            'TTM1800',
		       ]

for signal in signameList:
	RFile = R.TFile(templateFile.replace('TTM900',signal))
	for syst in systematics:
		Prefix = 'triLep__sig'
		hMC = RFile.Get(Prefix).Clone()
		hMCUp = RFile.Get(Prefix+'__'+syst+'__plus').Clone()
		hMCDown = RFile.Get(Prefix+'__'+syst+'__minus').Clone()
		hMC.Draw()
		hMCUp.Draw()
		hMCDown.Draw()

		canv = R.TCanvas(Prefix+'__'+syst,Prefix+'__'+syst,1000,700)
		yDiv = 0.35
		uPad=R.TPad('uPad','',0,yDiv,1,1)
		uPad.SetTopMargin(0.07)
		uPad.SetBottomMargin(0)
		uPad.SetRightMargin(.05)
		uPad.SetLeftMargin(.18)
		#uPad.SetLogy()
		uPad.Draw()

		lPad=R.TPad("lPad","",0,0,1,yDiv) #for sigma runner
		lPad.SetTopMargin(0)
		lPad.SetBottomMargin(.4)
		lPad.SetRightMargin(.05)
		lPad.SetLeftMargin(.18)
		lPad.SetGridy()
		lPad.Draw()

		uPad.cd()

		R.gStyle.SetOptTitle(0)

		#canv.SetLogy()
		hMC.SetFillColor(R.kWhite)
		hMCUp.SetFillColor(R.kWhite)
		hMCDown.SetFillColor(R.kWhite)
		hMC.SetMarkerColor(R.kBlack)
		hMCUp.SetMarkerColor(R.kRed)
		hMCDown.SetMarkerColor(R.kBlue)
		hMC.SetLineColor(R.kBlack)
		hMCUp.SetLineColor(R.kRed)
		hMCDown.SetLineColor(R.kBlue)
		hMC.SetLineWidth(2)
		hMC.SetLineStyle(1)
		hMCUp.SetLineWidth(2)
		hMCUp.SetLineStyle(1)
		hMCDown.SetLineWidth(2)
		hMCDown.SetLineStyle(1)
		hMC.SetMarkerSize(.05)
		hMCUp.SetMarkerSize(.05)
		hMCDown.SetMarkerSize(.05)

		hMCUp.GetYaxis().SetTitle('Events')
		hMCUp.GetYaxis().SetLabelSize(0.10)
		hMCUp.GetYaxis().SetTitleSize(0.1)
		hMCUp.GetYaxis().SetTitleOffset(.6)
		
		hMCUp.GetYaxis().SetRangeUser(0.0001,1.1*max(hMCUp.GetMaximum(),hMC.GetMaximum(),hMCDown.GetMaximum()))

		hMCUp.Draw()
		hMC.Draw('same')
		hMCDown.Draw('same')
		#uPad.RedrawAxis()

		lPad.cd()
		R.gStyle.SetOptTitle(0)
		pullUp = hMCUp.Clone()
		for iBin in range(0,pullUp.GetXaxis().GetNbins()+2):
			pullUp.SetBinContent(iBin,pullUp.GetBinContent(iBin)-hMC.GetBinContent(iBin))
			pullUp.SetBinError(iBin,math.sqrt(pullUp.GetBinError(iBin)**2+hMC.GetBinError(iBin)**2))
		pullUp.Divide(hMC)
		pullUp.SetTitle('')
		pullUp.SetFillColor(2)
		pullUp.SetLineColor(2)

		#pullUp.GetXaxis().SetTitle(histName)
		pullUp.GetXaxis().SetLabelSize(.15)
		pullUp.GetXaxis().SetTitleSize(0.18)
		pullUp.GetXaxis().SetTitleOffset(0.95)

		pullUp.GetYaxis().SetTitle('#frac{Up/Down-Nom}{Nom}')
		pullUp.GetYaxis().CenterTitle(1)
		pullUp.GetYaxis().SetLabelSize(0.125)
		pullUp.GetYaxis().SetTitleSize(0.1)
		pullUp.GetYaxis().SetTitleOffset(.55)
		pullUp.GetYaxis().SetNdivisions(506)

		pullDown = hMCDown.Clone()
		for iBin in range(0,pullDown.GetXaxis().GetNbins()+2):
			pullDown.SetBinContent(iBin,pullDown.GetBinContent(iBin)-hMC.GetBinContent(iBin))
			pullDown.SetBinError(iBin,math.sqrt(pullDown.GetBinError(iBin)**2+hMC.GetBinError(iBin)**2))
		pullDown.Divide(hMC)
		pullDown.SetTitle('')
		pullDown.SetFillColor(4)
		pullDown.SetLineColor(4)

		#pullDown.GetXaxis().SetTitle(histName)
		pullDown.GetXaxis().SetLabelSize(.15)
		pullDown.GetXaxis().SetTitleSize(0.18)
		pullDown.GetXaxis().SetTitleOffset(0.95)

		pullDown.GetYaxis().SetTitle('#frac{Up/Down-Nom}{Nom}')#'Python-C++'
		pullDown.GetYaxis().CenterTitle(1)
		pullDown.GetYaxis().SetLabelSize(0.125)
		pullDown.GetYaxis().SetTitleSize(0.1)
		pullDown.GetYaxis().SetTitleOffset(.55)
		pullDown.GetYaxis().SetNdivisions(506)
		pullUp.SetMinimum(-0.5)
		pullUp.SetMaximum(0.5)
		pullUp.Draw()
		pullDown.Draw('same')
		lPad.RedrawAxis()

		uPad.cd()

		legend = R.TLegend(0.7,0.65,0.9,0.90)
		legend.SetShadowColor(0);
		legend.SetFillColor(0);
		legend.SetLineColor(0);
		legend.AddEntry(hMC,signal,'l')
		'muRFcorrd','muRFcorrdNew','muRFdecorrdNew'
		legend.AddEntry(hMCUp,syst.replace('muRFcorrdNew','muRF').replace('muRFdecorrdNew','muRF').replace('muRFcorrd','muRF').replace('muRFenv','muRF').replace('pdfNew','PDF').replace('toppt','Top Pt').replace('jsf','JSF').replace('jec','JEC').replace('q2','Q^{2}').replace('miniiso','miniIso').replace('pileup','Pileup').replace('jer','JER').replace('btag','b tag').replace('pdf','PDF').replace('jmr','JMR').replace('jms','JMS').replace('tau21','#tau_{2}/#tau_{1}')+' Up','l')
		legend.AddEntry(hMCDown,syst.replace('muRFcorrdNew','muRF').replace('muRFdecorrdNew','muRF').replace('muRFcorrd','muRF').replace('muRFenv','muRF').replace('pdfNew','PDF').replace('toppt','Top Pt').replace('jsf','JSF').replace('jec','JEC').replace('q2','Q^{2}').replace('miniiso','miniIso').replace('pileup','Pileup').replace('jer','JER').replace('btag','b tag').replace('pdf','PDF').replace('jmr','JMR').replace('jms','JMS').replace('tau21','#tau_{2}/#tau_{1}')+' Down','l')

		legend.Draw('same')
	
		prelimTex=R.TLatex()
		prelimTex.SetNDC()
		prelimTex.SetTextAlign(31) # align right
		prelimTex.SetTextFont(42)
		prelimTex.SetTextSize(0.05)
		prelimTex.SetLineWidth(2)
		prelimTex.DrawLatex(0.90,0.943,str(lumi)+" fb^{-1} (13 TeV)")

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

		#canv.SaveAs(tempVersion+'/signals/'+syst+'_'+signal+'.pdf')
		canv.SaveAs(tempVersion+'/signals/'+syst+'_'+signal+'.png')
		#canv.SaveAs(tempVersion+'/signals/'+syst+'_'+signal+'.root')
	RFile.Close()

