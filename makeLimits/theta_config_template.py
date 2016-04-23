import os,sys
from operator import itemgetter,attrgetter

outDir = os.environ['CMSSW_BASE']+'/src/theta/utils/optimization/limits/lep40_MET80_leadJet450_subLeadJet75_leadbJet0_ST0_HT0'

input = '/uscms_data/d3/ssagir/ljmet/CMSSW_7_3_0/src/LJMet/macros/optimization_condor/templates_2015_8_3_4_23_24/lep40_MET80_leadJet450_subLeadJet75_leadbJet0_ST0_HT0/templates_HT_T53T53M900left_5fb_lep40_MET80_leadJet450_subLeadJet75_leadbJet0_ST0_HT0.root'

rFileName = input.split('/')[-1][:-5]
                                                                                                                                          
def get_model():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True)#,histogram_filter = (lambda s: s.count('jec')==0 and s.count('jer')==0)

    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')
    
    procs = model.processes
    obsvs = model.observables.keys()

    for obs in obsvs:
		if 'isEEE' in obs: ### CHECK TRIGGER SYST!!!!!!!!!!!!!!!!
			try: model.add_lognormal_uncertainty('elTrigSys', math.log(1.03), '*', obs)
			except: pass
		elif 'isEEM' in obs:
			try: model.add_lognormal_uncertainty('elTrigSys', math.log(1.03), '*', obs)
			except: pass
		elif 'isEMM' in obs:
			try: model.add_lognormal_uncertainty('muTrigSys', math.log(1.03), '*', obs)
			except: pass
		elif 'isMMM' in obs:
			try: model.add_lognormal_uncertainty('muTrigSys', math.log(1.03), '*', obs)
			except: pass
    try: model.add_lognormal_uncertainty('lumiSys', math.log(1.027), '*', '*')
    except: pass
#     try: model.add_lognormal_uncertainty('MC', math.log(1.50), 'qcd', '*')
#     except: pass
#     try: model.add_lognormal_uncertainty('MC', math.log(1.055), 'top', '*')
#     except: pass
#     try: model.add_lognormal_uncertainty('MC', math.log(1.05), 'ewk', '*')
#     except: pass

    return model

model = get_model()

##################################################################################################################

model_summary(model)

plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 5000, n_data = 500)
#plot_exp, plot_obs = bayesian_limits(model,'expected')
plot_exp.write_txt('limits_'+rFileName+'_expected.txt')
plot_obs.write_txt('limits_'+rFileName+'_observed.txt')

report.write_html('htmlout_'+rFileName)
