#!/usr/bin/python

import os,sys,time,math,pickle
from ROOT import *
from weights import *
from tdrStyle import *


gROOT.SetBatch(1)
start_time = time.time()

lumi=41.6 #for plots
lumiInTemplates='41p557'
scaleFact1 = 10
scaleFact2 = 50

sig='ttm1000' # choose the 1st signal to plot
sigleg='T#bar{T}(1 TeV)'
sigM1500='ttm1500' 
siglegM1500='T#bar{T}(1.5 TeV)'

DEBUG=False
scaleSignals = True
dontShowSignalScaling = False
CutLessThan = False

mainDir='/mnt/data/users/wwong/'
templateDir=mainDir
templateDir+='kinematics_LJMet94x_3lepTT_2017datasets_2018_11_7_rizki_NoSYS_2016SFs_FRv3'
if len(sys.argv)>1: templateDir = mainDir+sys.argv[1] 

plotList = [#distribution name as defined in "doHists.py"
    'NPV',
 
    'lepPt',
    'lepPtRebinned',
    'ElPt',
    'MuPt',
    'lep1Pt',
    'lep2Pt',
    'lep3Pt',
    'lepEta',
    'ElEta',
    'MuEta',
    'lep1Eta',
    'lep2Eta',
    'lep3Eta',
    'Nlep',
    'Nel',
    'Nmu',

    'JetEta',
    'Jet1Eta',
    'Jet2Eta',
    'JetPt' ,
    'Jet1Pt' ,
    'Jet2Pt' ,

    'HT',
    'MET',
    'HTrebinned',

    'STrebinnedv2',

    'METrebinned',

    'NJets' ,
    'NBJets',
    ]


plotList = ['lepPtRebinned', 'STrebinnedv2', 'NJets', 'NBJets', 'JetEta','JetPt', 'lep1Eta','METrebinned', 'HTrebinned', 'minMlllBv4']
isEMlist = ['EEE','EEM','EMM','MMM','All']

def formatUpperHist_v2(histogram, th1hist):
	histogram.GetXaxis().SetLabelSize(0)
	lowside = th1hist.GetBinLowEdge(1)
	highside = th1hist.GetBinLowEdge(th1hist.GetNbinsX()+1)
	#histogram.GetXaxis().SetRangeUser(lowside,highside)
	print 'Name being formatted:',histogram.GetName()

	histogram.GetYaxis().SetLabelSize(0.05)
	histogram.GetYaxis().SetTitleSize(0.06)
	histogram.GetYaxis().SetTitleOffset(.78)

	if 'JetPt' in histogram.GetName() or 'JetEta' in histogram.GetName() or 'JetPhi' in histogram.GetName() or 'Pruned' in histogram.GetName() or 'Tau' in histogram.GetName(): histogram.GetYaxis().SetTitle("Jets")
# 	histogram.GetYaxis().CenterTitle()
	#histogram.SetMinimum(2.01e-4)
# 	histogram.SetMinimum(0.001)
	#histogram.SetMinimum(0.25)

def formatLowerHist(histogram):
	histogram.GetXaxis().SetLabelSize(.15)
	histogram.GetXaxis().SetTitleSize(0.15)
	histogram.GetXaxis().SetTitleOffset(0.9)
	histogram.GetXaxis().SetNdivisions(506)
	#histogram.GetXaxis().SetTitle("S_{T} (GeV)")

	histogram.GetYaxis().SetLabelSize(0.1)
	histogram.GetYaxis().SetTitleSize(0.13)
	histogram.GetYaxis().SetTitleOffset(.3)

	histogram.GetYaxis().SetNdivisions(5)
	#histogram.GetYaxis().SetRangeUser(0,2.99)
	#histogram.GetYaxis().CenterTitle()


for discriminant in plotList:

    ## read hist template root file from doKinematics
    fileTemp='templates_'+discriminant+'_'+lumiInTemplates+'fb'+'.root'
    print templateDir+'/'+fileTemp
    if not os.path.exists(templateDir+'/'+fileTemp): 
        print 'not found, skipping'
        continue
    RFile = TFile(templateDir+'/'+fileTemp)

    for isEM in isEMlist:

        ## set plot style
        gStyle.SetOptStat(0)
        gStyle.SetEndErrorSize(0)
        setTDRStyle()

        ## for checking
        if 'El' in discriminant and  isEM=='MMM': continue
        if 'Mu' in discriminant and  isEM=='EEE': continue

        histPrefix=discriminant+'_'+lumiInTemplates+'fb_'+isEM
        try: hTOP = RFile.Get(histPrefix+'__top').Clone()
        except: 
            if(DEBUG): print "There is no TOP!!!!!!!!",
            if(DEBUG): print "Skipping TOP....."
            pass
        try: hEWK = RFile.Get(histPrefix+'__ewk').Clone()
        except: 
            if(DEBUG): print "There is no EWK!!!!!!!!",
            if(DEBUG): print "Skipping EWK....."
            pass
        try: hQCD = RFile.Get(histPrefix+'__qcd').Clone()
        except: 
            if(DEBUG): print "There is no QCD!!!!!!!!",
            if(DEBUG): print "Skipping QCD....."
            pass
        try: hDDBKG = RFile.Get(histPrefix+'_ddbkg').Clone()
        except: 
            if(DEBUG): print "There is no DDBKG!!!!!!!!",
            if(DEBUG): print "Skipping DDBKG....."
            pass

        hsig = RFile.Get(histPrefix+'__'+sig+'bwbw').Clone(histPrefix+'__'+sig+'nominal')
        hsigM1500 = RFile.Get(histPrefix+'__'+sigM1500+'bwbw').Clone(histPrefix+'__'+sigM1500+'nominal')
        decays = ['tztz','thth','tzbw','thbw','tzth']
        for decay in decays:
            htemp = RFile.Get(histPrefix+'__'+sig+decay).Clone()
            hsig.Add(htemp)
            htemp = RFile.Get(histPrefix+'__'+sigM1500+decay).Clone()
            hsigM1500.Add(htemp)

        try: bkgHT = hTOP.Clone()
        except: pass
        try: bkgHT.Add(hEWK)
        except: pass
        try: bkgHT.Add(hQCD)
        except: pass
        try: bkgHT.Add(hDDBKG)
        except: pass


        def plotSignificance(hbkg, hsig):
            hSigni = hbkg.Clone(hbkg.GetName()+'_Significance')
            for i in range(hbkg.GetNbinsX()):
                nBkg = hbkg.GetBinContent(i+1)
                nSig = hsig.GetBinContent(i+1)
                if nBkg>0:
                    hSigni.SetBinContent(i+1,nSig/math.sqrt(nBkg))
                else:
                    hSigni.SetBinContent(i+1,0)
                hSigni.SetBinError(i+1,0)
            hSignificance = TGraphAsymmErrors( hSigni.Clone(hSigni.GetName()))
            return hSignificance

        print(bkgHT, hsig)
        hsigSignificance = plotSignificance(bkgHT, hsig)
        hsigM1500Significance = plotSignificance(bkgHT, hsigM1500)

        hsigSignificance.SetMarkerColor(kBlack)
        hsigSignificance.SetLineColor(kBlack)
        hsigSignificance.SetLineWidth(1)
        hsigSignificance.SetMarkerStyle(21)
        hsigSignificance.SetMarkerSize(1.0)

	hsigM1500Significance.SetMarkerColor(kBlue)
	hsigM1500Significance.SetLineColor(kBlue)
	hsigM1500Significance.SetLineWidth(1)
	hsigM1500Significance.SetMarkerStyle(21)
	hsigM1500Significance.SetMarkerSize(1.0)

        bkgHTCopy = bkgHT.Clone(bkgHT.GetName()+'_Cumu')
        bkgHTCumu = bkgHTCopy.GetCumulative((not CutLessThan))
        hsigCopy = hsig.Clone(hsig.GetName()+'_Cumu')
        hsigM1500Copy = hsigM1500.Clone(hsigM1500.GetName()+'_Cumu')
        hsigCumu = hsigCopy.GetCumulative(CutLessThan)
        hsigM1500Cumu = hsigM1500Copy.GetCumulative(CutLessThan)

        hsigCumuSignificance = plotSignificance(bkgHTCumu, hsigCumu)
        hsigM1500CumuSignificance = plotSignificance(bkgHTCumu, hsigM1500Cumu)

        c1 = TCanvas("c1","c1",600,500)
        yDiv=0.25
        uMargin = 0.00001
        rMargin=.04

        uPad=TPad("uPad","",0,yDiv,1,1) #for actual plots
        uPad.SetTopMargin(0.08)
        uPad.SetBottomMargin(uMargin)
        uPad.SetRightMargin(rMargin)
        uPad.SetLeftMargin(.105)
        uPad.Draw()
        lPad=TPad("lPad","",0,0,1,yDiv) #for sigma runner
        lPad.SetTopMargin(0.05)
        lPad.SetBottomMargin(.4)
        lPad.SetRightMargin(rMargin)
        lPad.SetLeftMargin(.105)
        lPad.SetGridy()
        lPad.Draw()

        hsigSignificance.SetMinimum(0.0)
        #hsigSignificance.SetMaximum(1.5)
        hsigSignificance.GetYaxis().SetTitle("S/#sqrt(B) per Bin")
        formatUpperHist_v2(hsigSignificance,hsigCopy)
        #bkgHTSig.GetXaxis().SetTitle("TEST")
        uPad.cd()
        hsigSignificance.SetTitle("")
        hsigSignificance.Draw("alp")
	hsigM1500Significance.Draw("SAME lp")

        uPad.RedrawAxis()

        leg = TLegend(0.360,0.822,0.939,0.89)
        leg.SetShadowColor(0)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetLineColor(0)
        leg.SetLineStyle(0)
        leg.SetBorderSize(0)
        leg.SetNColumns(2)
        leg.SetTextFont(62)
        leg.SetTextSize(0.06)

        leg.AddEntry(hsigSignificance, sigleg , "pel")
	leg.AddEntry(hsigM1500Significance, siglegM1500 , "pel")
        leg.Draw("same")

        prelimTex=TLatex()
        prelimTex.SetNDC()
        prelimTex.SetTextAlign(31) # align right
        prelimTex.SetTextFont(42)
        prelimTex.SetTextSize(0.07)
        prelimTex.SetLineWidth(2)
        prelimTex.DrawLatex(0.95,0.94,str(lumi)+" fb^{-1} (13 TeV)")

        prelimTex2=TLatex()
        prelimTex2.SetNDC()
        prelimTex2.SetTextFont(61)
        prelimTex2.SetLineWidth(2)
        prelimTex2.SetTextSize(0.10)
        prelimTex2.DrawLatex(0.16,0.81,"CMS")

        prelimTex3=TLatex()
        prelimTex3.SetNDC()
        prelimTex3.SetTextAlign(13)
        prelimTex3.SetTextFont(52)
        prelimTex3.SetTextSize(0.075)
        prelimTex3.SetLineWidth(2)

        chLatex = TLatex()
        chLatex.SetNDC()
        chLatex.SetTextSize(0.05)
        chLatex.SetTextAlign(31) # align right
        chString = ''
        if isEM=='All': chString+='All channels'
        if isEM=='EEE': chString+='eee'
        if isEM=='EEM': chString+='ee#mu'
        if isEM=='EMM': chString+='e#mu#mu'
        if isEM=='MMM': chString+='#mu#mu#mu'
        chLatex.DrawLatex(0.92, 0.7, chString)

        lPad.cd()

        hsigCumuSignificance.SetMarkerColor(kBlack)
        hsigCumuSignificance.SetLineColor(kBlack)
        hsigCumuSignificance.SetLineWidth(1)
        hsigCumuSignificance.SetMarkerStyle(21)
        hsigCumuSignificance.SetMarkerSize(0.5)

        hsigM1500CumuSignificance.SetMarkerColor(kBlue)
        hsigM1500CumuSignificance.SetLineColor(kBlue)
        hsigM1500CumuSignificance.SetLineWidth(1)
        hsigM1500CumuSignificance.SetMarkerStyle(21)
        hsigM1500CumuSignificance.SetMarkerSize(0.5)


        #hsigCumuSignificance.SetMaximum(math.ceil(10*1.2*bkgHTCopy.GetMaximum())*0.1)
        #hsigCumuSignificance.SetMinimum(0)
        hsigCumuSignificance.GetXaxis().SetTitle(bkgHT.GetXaxis().GetTitle())
        formatLowerHist(hsigCumuSignificance)
        hsigCumuSignificance.GetYaxis().SetTitle('Cumulative')
        hsigCumuSignificance.Draw("alp")
        hsigM1500CumuSignificance.Draw("SAME lp") 

        savePrefix = templateDir+'/Significance_plots/'
        if not os.path.exists(savePrefix): os.system('mkdir '+savePrefix)
        savePrefix+='Significance_'+histPrefix

        c1.SaveAs(savePrefix+".pdf")
        c1.SaveAs(savePrefix+".png")
        c1.SaveAs(savePrefix+".root")
        c1.SaveAs(savePrefix+".C")

    RFile.Close()
print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))





