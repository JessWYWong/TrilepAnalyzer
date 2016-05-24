#!/usr/bin/python

targetlumi = 2320. #1/pb --> https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2015Analysis - Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt

BR={}
BR['BW'] = 0.5
BR['TZ'] = 0.25
BR['TH'] = 0.25
BR['TTBWBW'] = BR['BW']*BR['BW']
BR['TTTHBW'] = 2*BR['TH']*BR['BW']
BR['TTTZBW'] = 2*BR['TZ']*BR['BW']
BR['TTTZTZ'] = BR['TZ']*BR['TZ']
BR['TTTZTH'] = 2*BR['TZ']*BR['TH']
BR['TTTHTH'] = BR['TH']*BR['TH']

# Number of processed MC events (before selections)
nRun={}
nRun['DY10to50'] = 55716097 # from 76558711
nRun['DY'] = 81236727. # from 121212419

# nRun['TTJets'] = . # from 

nRun['WJets'] = 16521036. # from 24156124

nRun['TTJetsPH'] = 97994442. 
# nRun['TTJetsPH0to700inc'] = nRun['TTJetsPH']
# nRun['TTJetsPH700to1000inc'] = nRun['TTJetsPH']*0.0921 + 3877762. #filtering efficiency coeff.
# nRun['TTJetsPH1000toINFinc'] = nRun['TTJetsPH']*0.02474 + 2360497. #filtering efficiency coeff.
# nRun['TTJetsPH700mtt'] = nRun['TTJetsPH']*0.0921 + 3877762.
# nRun['TTJetsPH1000mtt'] = nRun['TTJetsPH']*0.02474 + 2360497.

nRun['WW'] = 988418. 
nRun['WZ'] = 1000000.
nRun['ZZ'] = 985600.

nRun['WWW'] = 210538 # from 240000 # N_eff=N_gen(1-2*frac_negW)? 
nRun['WWZ'] = 220044 # from 248400 # N_eff=N_gen(1-2*frac_negW)? 
nRun['WZZ'] = 218986 # from 249800 # N_eff=N_gen(1-2*frac_negW)?
nRun['ZZZ'] = 213850 # from 250000 # N_eff=N_gen(1-2*frac_negW)?
nRun['TTWl'] =  129001 #from 250307 
nRun['TTWq'] =  429599 #from 831847
nRun['TTZl'] =  183200 #from 394200 
nRun['TTZq'] =  350106 #from 747000 

nRun['WJetsMG'] = 47161328.

nRun['WJetsMG100'] = 10205377.
nRun['WJetsMG200'] = 4949568.
nRun['WJetsMG400'] = 1943664.
nRun['WJetsMG600'] = 3767766.
nRun['WJetsMG800'] = 1568277.
nRun['WJetsMG1200'] = 246239.
nRun['WJetsMG2500'] = 251982.
nRun['Ts'] = 621946. #from 998400 
nRun['Tt'] = 6294303. #from 29206391 
nRun['TtW'] = 1000000.
nRun['TbtW'] = 999400.

TTM700events =  805000.0
TTM800events =  788200.0
TTM900events =  830400.0
TTM1000events =  818600.0
TTM1100events =  808800.0
TTM1200events =  817800.0
TTM1300events =  828000.0
TTM1400events =  826800.0
TTM1500events =  832000.0
TTM1600events =  809200.0
TTM1700events =  795600.0
TTM1800events =  825800.0

nRun['TTM700BWBW'] = TTM700events*0.333*0.333
nRun['TTM800BWBW'] = TTM800events*0.333*0.333
nRun['TTM900BWBW'] = TTM900events*0.333*0.333
nRun['TTM1000BWBW'] = TTM1000events*0.333*0.333
nRun['TTM1100BWBW'] = TTM1100events*0.333*0.333
nRun['TTM1200BWBW'] = TTM1200events*0.333*0.333
nRun['TTM1300BWBW'] = TTM1300events*0.333*0.333
nRun['TTM1400BWBW'] = TTM1400events*0.333*0.333
nRun['TTM1500BWBW'] = TTM1500events*0.333*0.333
nRun['TTM1600BWBW'] = TTM1500events*0.333*0.333
nRun['TTM1700BWBW'] = TTM1500events*0.333*0.333
nRun['TTM1800BWBW'] = TTM1500events*0.333*0.333
nRun['TTM700THBW'] = TTM700events*0.333*0.333*2
nRun['TTM800THBW'] = TTM800events*0.333*0.333*2
nRun['TTM900THBW'] = TTM900events*0.333*0.333*2
nRun['TTM1000THBW'] = TTM1000events*0.333*0.333*2
nRun['TTM1100THBW'] = TTM1100events*0.333*0.333*2
nRun['TTM1200THBW'] = TTM1200events*0.333*0.333*2
nRun['TTM1300THBW'] = TTM1300events*0.333*0.333*2
nRun['TTM1400THBW'] = TTM1400events*0.333*0.333*2
nRun['TTM1500THBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1600THBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1700THBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1800THBW'] = TTM1500events*0.333*0.333*2
nRun['TTM700TZBW'] = TTM700events*0.333*0.333*2
nRun['TTM800TZBW'] = TTM800events*0.333*0.333*2
nRun['TTM900TZBW'] = TTM900events*0.333*0.333*2
nRun['TTM1000TZBW'] = TTM1000events*0.333*0.333*2
nRun['TTM1100TZBW'] = TTM1100events*0.333*0.333*2
nRun['TTM1200TZBW'] = TTM1200events*0.333*0.333*2
nRun['TTM1300TZBW'] = TTM1300events*0.333*0.333*2
nRun['TTM1400TZBW'] = TTM1400events*0.333*0.333*2
nRun['TTM1500TZBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1600TZBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1700TZBW'] = TTM1500events*0.333*0.333*2
nRun['TTM1800TZBW'] = TTM1500events*0.333*0.333*2
nRun['TTM700TZTZ'] = TTM700events*0.333*0.333
nRun['TTM800TZTZ'] = TTM800events*0.333*0.333
nRun['TTM900TZTZ'] = TTM900events*0.333*0.333
nRun['TTM1000TZTZ'] = TTM1000events*0.333*0.333
nRun['TTM1100TZTZ'] = TTM1100events*0.333*0.333
nRun['TTM1200TZTZ'] = TTM1200events*0.333*0.333
nRun['TTM1300TZTZ'] = TTM1300events*0.333*0.333
nRun['TTM1400TZTZ'] = TTM1400events*0.333*0.333
nRun['TTM1500TZTZ'] = TTM1500events*0.333*0.333
nRun['TTM1600TZTZ'] = TTM1500events*0.333*0.333
nRun['TTM1700TZTZ'] = TTM1500events*0.333*0.333
nRun['TTM1800TZTZ'] = TTM1500events*0.333*0.333
nRun['TTM700TZTH'] = TTM700events*0.333*0.333*2
nRun['TTM800TZTH'] = TTM800events*0.333*0.333*2
nRun['TTM900TZTH'] = TTM900events*0.333*0.333*2
nRun['TTM1000TZTH'] = TTM1000events*0.333*0.333*2
nRun['TTM1100TZTH'] = TTM1100events*0.333*0.333*2
nRun['TTM1200TZTH'] = TTM1200events*0.333*0.333*2
nRun['TTM1300TZTH'] = TTM1300events*0.333*0.333*2
nRun['TTM1400TZTH'] = TTM1400events*0.333*0.333*2
nRun['TTM1500TZTH'] = TTM1500events*0.333*0.333*2
nRun['TTM1600TZTH'] = TTM1500events*0.333*0.333*2
nRun['TTM1700TZTH'] = TTM1500events*0.333*0.333*2
nRun['TTM1800TZTH'] = TTM1500events*0.333*0.333*2
nRun['TTM700THTH'] = TTM700events*0.333*0.333
nRun['TTM800THTH'] = TTM800events*0.333*0.333
nRun['TTM900THTH'] = TTM900events*0.333*0.333
nRun['TTM1000THTH'] = TTM1000events*0.333*0.333
nRun['TTM1100THTH'] = TTM1100events*0.333*0.333
nRun['TTM1200THTH'] = TTM1200events*0.333*0.333
nRun['TTM1300THTH'] = TTM1300events*0.333*0.333
nRun['TTM1400THTH'] = TTM1400events*0.333*0.333
nRun['TTM1500THTH'] = TTM1500events*0.333*0.333
nRun['TTM1600THTH'] = TTM1500events*0.333*0.333
nRun['TTM1700THTH'] = TTM1500events*0.333*0.333
nRun['TTM1800THTH'] = TTM1500events*0.333*0.333

nRun['QCDht100'] = 82095800.
nRun['QCDht200'] = 18784379.
nRun['QCDht300'] = 16909004.
nRun['QCDht500'] = 19665695.
nRun['QCDht700'] = 15547962.
nRun['QCDht1000'] = 5049267.
nRun['QCDht1500'] = 3939077.
nRun['QCDht2000'] = 1981228.

#energy scale samples (Q^2)
nRun['TTJetsPHQ2U'] = 38507969.
nRun['TTJetsPHQ2D'] = 39461147.
nRun['TtWQ2U'] = 499200.
nRun['TtWQ2D'] = 500000.
nRun['TbtWQ2U'] = 499600.
nRun['TbtWQ2D'] = 495200.

# Cross sections for MC samples (in pb)
xsec={}
xsec['DY10to50'] = 18610 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJetsPH0to700inc'] = 831.76
xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsPH700mtt'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000mtt'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['WWW'] = 0.1651 #cross section obtained from 20k events: 0.1651 +- 0.0002 pb fraction of negative weights ~5.6%",  (from DAS mcm,notes)
xsec['WWZ'] = 0.1651 #cs = 0.1651 pb at NLO, frac_negW = 0.0571 (from CMS AN-2015/148)	 
xsec['WZZ'] = 0.05565 #cs = 0.05565 pb at NLO, frac_negW = 0.0617 (from CMS AN-2015/148) 	
xsec['ZZZ'] = 0.01398 #cs = 0.01398 pb at NLO, frac_negW = 0.0723 (from CMS AN-2015/148)	
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 216.99/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Ts'] = 11.36/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

xsec['TTM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo


xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

#energy scale samples (Q^2)
xsec['TTJetsPHQ2U'] = xsec['TTJetsPH']
xsec['TTJetsPHQ2D'] = xsec['TTJetsPH']
xsec['TtWQ2U'] = xsec['TtW']
xsec['TtWQ2D'] = xsec['TtW']
xsec['TbtWQ2U'] = xsec['TbtW']
xsec['TbtWQ2D'] = xsec['TbtW']

# Calculate lumi normalization weights
weight = {}
weight['DY10to50'] = (targetlumi*xsec['DY10to50']) / (nRun['DY10to50'])
weight['DY50'] = (targetlumi*xsec['DY']) / (nRun['DY'])
# weight['TTJets'] = (targetlumi*xsec['TTJets']) / (nRun['TTJets'])
weight['WJets'] = (targetlumi*xsec['WJets']) / (nRun['WJets'])
# weight['TTJetsPH'] = (targetlumi*xsec['TTJetsPH']) / (nRun['TTJetsPH'])
# weight['TTJetsPH0to700inc'] = (targetlumi*xsec['TTJetsPH0to700inc']) / (nRun['TTJetsPH0to700inc'])
# weight['TTJetsPH700to1000inc'] = (targetlumi*xsec['TTJetsPH700to1000inc']) / (nRun['TTJetsPH700to1000inc'])
# weight['TTJetsPH1000toINFinc'] = (targetlumi*xsec['TTJetsPH1000toINFinc']) / (nRun['TTJetsPH1000toINFinc'])
# weight['TTJetsPH700mtt'] = (targetlumi*xsec['TTJetsPH700mtt']) / (nRun['TTJetsPH700mtt'])
# weight['TTJetsPH1000mtt'] = (targetlumi*xsec['TTJetsPH1000mtt']) / (nRun['TTJetsPH1000mtt'])
weight['WJetsMG'] = (targetlumi*xsec['WJetsMG']) / (nRun['WJetsMG'])
weight['WJetsMG100'] = (targetlumi*xsec['WJetsMG100']) / (nRun['WJetsMG100'])
weight['WJetsMG200'] = (targetlumi*xsec['WJetsMG200']) / (nRun['WJetsMG200'])
weight['WJetsMG400'] = (targetlumi*xsec['WJetsMG400']) / (nRun['WJetsMG400'])
weight['WJetsMG600'] = (targetlumi*xsec['WJetsMG600']) / (nRun['WJetsMG600'])
weight['WJetsMG800'] = (targetlumi*xsec['WJetsMG800']) / (nRun['WJetsMG800'])
weight['WJetsMG1200'] = (targetlumi*xsec['WJetsMG1200']) / (nRun['WJetsMG1200'])
weight['WJetsMG2500'] = (targetlumi*xsec['WJetsMG2500']) / (nRun['WJetsMG2500'])
weight['WW'] = (targetlumi*xsec['WW']) / (nRun['WW'])
weight['WZ'] = (targetlumi*xsec['WZ']) / (nRun['WZ'])
weight['ZZ'] = (targetlumi*xsec['ZZ']) / (nRun['ZZ'])
weight['WWW'] = (targetlumi*xsec['WWW']) / (nRun['WWW'])
weight['WWZ'] = (targetlumi*xsec['WWZ']) / (nRun['WWZ'])
weight['WZZ'] = (targetlumi*xsec['WZZ']) / (nRun['WZZ'])
weight['ZZZ'] = (targetlumi*xsec['ZZZ']) / (nRun['ZZZ'])
weight['TTWl'] = (targetlumi*xsec['TTWl']) / (nRun['TTWl'])
weight['TTWq'] = (targetlumi*xsec['TTWq']) / (nRun['TTWq'])
weight['TTZl'] = (targetlumi*xsec['TTZl']) / (nRun['TTZl'])
weight['TTZq'] = (targetlumi*xsec['TTZq']) / (nRun['TTZq'])
weight['Tt'] = (targetlumi*xsec['Tt']) / (nRun['Tt'])
weight['Ts'] = (targetlumi*xsec['Ts']) / (nRun['Ts'])
weight['TtW'] = (targetlumi*xsec['TtW']) / (nRun['TtW'])
weight['TbtW'] = (targetlumi*xsec['TbtW']) / (nRun['TbtW'])
weight['QCDht100'] = (targetlumi*xsec['QCDht100']) / (nRun['QCDht100'])
weight['QCDht200'] = (targetlumi*xsec['QCDht200']) / (nRun['QCDht200'])
weight['QCDht300'] = (targetlumi*xsec['QCDht300']) / (nRun['QCDht300'])
weight['QCDht500'] = (targetlumi*xsec['QCDht500']) / (nRun['QCDht500'])
weight['QCDht700'] = (targetlumi*xsec['QCDht700']) / (nRun['QCDht700'])
weight['QCDht1000'] = (targetlumi*xsec['QCDht1000']) / (nRun['QCDht1000'])
weight['QCDht1500'] = (targetlumi*xsec['QCDht1500']) / (nRun['QCDht1500'])
weight['QCDht2000'] = (targetlumi*xsec['QCDht2000']) / (nRun['QCDht2000'])
weight['TTM700BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM700']) / (nRun['TTM700BWBW'])
weight['TTM800BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM800']) / (nRun['TTM800BWBW'])
weight['TTM900BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM900']) / (nRun['TTM900BWBW'])
weight['TTM1000BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1000']) / (nRun['TTM1000BWBW'])
weight['TTM1100BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1100']) / (nRun['TTM1100BWBW'])
weight['TTM1200BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1200']) / (nRun['TTM1200BWBW'])
weight['TTM1300BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1300']) / (nRun['TTM1300BWBW'])
weight['TTM1400BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1400']) / (nRun['TTM1400BWBW'])
weight['TTM1500BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1500']) / (nRun['TTM1500BWBW'])
weight['TTM1600BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1600']) / (nRun['TTM1600BWBW'])
weight['TTM1700BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1700']) / (nRun['TTM1700BWBW'])
weight['TTM1800BWBW'] = (targetlumi*BR['TTBWBW']*xsec['TTM1800']) / (nRun['TTM1800BWBW'])
weight['TTM700THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM700']) / (nRun['TTM700THBW'])
weight['TTM800THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM800']) / (nRun['TTM800THBW'])
weight['TTM900THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM900']) / (nRun['TTM900THBW'])
weight['TTM1000THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1000']) / (nRun['TTM1000THBW'])
weight['TTM1100THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1100']) / (nRun['TTM1100THBW'])
weight['TTM1200THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1200']) / (nRun['TTM1200THBW'])
weight['TTM1300THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1300']) / (nRun['TTM1300THBW'])
weight['TTM1400THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1400']) / (nRun['TTM1400THBW'])
weight['TTM1500THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1500']) / (nRun['TTM1500THBW'])
weight['TTM1600THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1600']) / (nRun['TTM1600THBW'])
weight['TTM1700THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1700']) / (nRun['TTM1700THBW'])
weight['TTM1800THBW'] = (targetlumi*BR['TTTHBW']*xsec['TTM1800']) / (nRun['TTM1800THBW'])
weight['TTM700TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM700']) / (nRun['TTM700TZBW'])
weight['TTM800TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM800']) / (nRun['TTM800TZBW'])
weight['TTM900TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM900']) / (nRun['TTM900TZBW'])
weight['TTM1000TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1000']) / (nRun['TTM1000TZBW'])
weight['TTM1100TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1100']) / (nRun['TTM1100TZBW'])
weight['TTM1200TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1200']) / (nRun['TTM1200TZBW'])
weight['TTM1300TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1300']) / (nRun['TTM1300TZBW'])
weight['TTM1400TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1400']) / (nRun['TTM1400TZBW'])
weight['TTM1500TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1500']) / (nRun['TTM1500TZBW'])
weight['TTM1600TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1600']) / (nRun['TTM1600TZBW'])
weight['TTM1700TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1700']) / (nRun['TTM1700TZBW'])
weight['TTM1800TZBW'] = (targetlumi*BR['TTTZBW']*xsec['TTM1800']) / (nRun['TTM1800TZBW'])
weight['TTM700TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM700']) / (nRun['TTM700TZTZ'])
weight['TTM800TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM800']) / (nRun['TTM800TZTZ'])
weight['TTM900TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM900']) / (nRun['TTM900TZTZ'])
weight['TTM1000TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1000']) / (nRun['TTM1000TZTZ'])
weight['TTM1100TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1100']) / (nRun['TTM1100TZTZ'])
weight['TTM1200TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1200']) / (nRun['TTM1200TZTZ'])
weight['TTM1300TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1300']) / (nRun['TTM1300TZTZ'])
weight['TTM1400TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1400']) / (nRun['TTM1400TZTZ'])
weight['TTM1500TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1500']) / (nRun['TTM1500TZTZ'])
weight['TTM1600TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1600']) / (nRun['TTM1600TZTZ'])
weight['TTM1700TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1700']) / (nRun['TTM1700TZTZ'])
weight['TTM1800TZTZ'] = (targetlumi*BR['TTTZTZ']*xsec['TTM1800']) / (nRun['TTM1800TZTZ'])
weight['TTM700TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM700']) / (nRun['TTM700TZTH'])
weight['TTM800TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM800']) / (nRun['TTM800TZTH'])
weight['TTM900TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM900']) / (nRun['TTM900TZTH'])
weight['TTM1000TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1000']) / (nRun['TTM1000TZTH'])
weight['TTM1100TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1100']) / (nRun['TTM1100TZTH'])
weight['TTM1200TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1200']) / (nRun['TTM1200TZTH'])
weight['TTM1300TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1300']) / (nRun['TTM1300TZTH'])
weight['TTM1400TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1400']) / (nRun['TTM1400TZTH'])
weight['TTM1500TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1500']) / (nRun['TTM1500TZTH'])
weight['TTM1600TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1600']) / (nRun['TTM1600TZTH'])
weight['TTM1700TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1700']) / (nRun['TTM1700TZTH'])
weight['TTM1800TZTH'] = (targetlumi*BR['TTTZTH']*xsec['TTM1800']) / (nRun['TTM1800TZTH'])
weight['TTM700THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM700']) / (nRun['TTM700THTH'])
weight['TTM800THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM800']) / (nRun['TTM800THTH'])
weight['TTM900THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM900']) / (nRun['TTM900THTH'])
weight['TTM1000THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1000']) / (nRun['TTM1000THTH'])
weight['TTM1100THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1100']) / (nRun['TTM1100THTH'])
weight['TTM1200THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1200']) / (nRun['TTM1200THTH'])
weight['TTM1300THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1300']) / (nRun['TTM1300THTH'])
weight['TTM1400THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1400']) / (nRun['TTM1400THTH'])
weight['TTM1500THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1500']) / (nRun['TTM1500THTH'])
weight['TTM1600THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1600']) / (nRun['TTM1600THTH'])
weight['TTM1700THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1700']) / (nRun['TTM1700THTH'])
weight['TTM1800THTH'] = (targetlumi*BR['TTTHTH']*xsec['TTM1800']) / (nRun['TTM1800THTH'])

#energy scale samples (Q^2)
weight['TTJetsPHQ2U'] = (targetlumi*xsec['TTJetsPHQ2U']) / (nRun['TTJetsPHQ2U'])
weight['TTJetsPHQ2D'] = (targetlumi*xsec['TTJetsPHQ2D']) / (nRun['TTJetsPHQ2D'])
weight['TtWQ2U'] = (targetlumi*xsec['TtWQ2U']) / (nRun['TtWQ2U'])
weight['TtWQ2D'] = (targetlumi*xsec['TtWQ2D']) / (nRun['TtWQ2D'])
weight['TbtWQ2U'] = (targetlumi*xsec['TbtWQ2U']) / (nRun['TbtWQ2U'])
weight['TbtWQ2D'] = (targetlumi*xsec['TbtWQ2D']) / (nRun['TbtWQ2D'])


