import os,sys
from operator import itemgetter,attrgetter

# outDir = os.environ['CMSSW_BASE']+'/src/theta/utils/optimization/limits/dummy'

input = 'dummy.root'

rFileName = input.split('/')[-1][:-5]
                                                                                                                                          
def get_model():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True)#,histogram_filter = (lambda s: s.count('jec')==0 and s.count('jer')==0)

    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')
    
    procs = model.processes
    
    for proc in procs:
		if(proc!="ddbkg"):
# 			try: model.add_lognormal_uncertainty('lumiSys', math.log(1.062), proc)
			try: model.add_lognormal_uncertainty('lumiSys', math.log(1.026), proc) #https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html
			except: pass


    return model

#defining all norm sys as lognormal here and not use histos
#fromJulie's /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/thetaLimits/theta_combined_template.py May-11-2017
def get_model3L():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('muR__')==0 and s.count('muF__')==0 and s.count('muRFcorrd__')==0 and s.count('elelelTrigSys')==0 and s.count('elelmuTrigSys')==0 and s.count('elmumuTrigSys')==0 and s.count('mumumuTrigSys')==0 and s.count('elIsoSys')==0 and s.count('elIdSys')==0 and s.count('muIsoSys')==0 and s.count('muIdSys')==0 and s.count('PR__')==0)) #for PRv9
#     model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('muR__')==0 and s.count('muF__')==0 and s.count('muRFcorrd__')==0 and s.count('elelelTrigSys')==0 and s.count('elelmuTrigSys')==0 and s.count('elmumuTrigSys')==0 and s.count('mumumuTrigSys')==0 and s.count('elIsoSys')==0 and s.count('elIdSys')==0 and s.count('muIsoSys')==0 and s.count('muIdSys')==0 and s.count('PRsys__')==0)) #for PRv10

    #                                                                                                                                                                                                                                    
    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')

    procs = model.processes
    obsvs = model.observables.keys()

    for proc in procs:
        if(proc != 'ddbkg'):
            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.06), proc, 'triLepEEE')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.04), proc, 'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.02), proc, 'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.03), proc, 'triLepEEE')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.02), proc, 'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.01), proc, 'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.02), proc, 'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.04), proc, 'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.06), proc, 'triLepMMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.01), proc, 'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.02), proc, 'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.03), proc, 'triLepMMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('eeeTrigSys', math.log(1.03), proc, 'triLepEEE')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('eemTrigSys', math.log(1.03), proc, 'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('emmTrigSys', math.log(1.03), proc, 'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('mmmTrigSys', math.log(1.03), proc, 'triLepMMM')
            except RuntimeError: pass

            try: model.add_lognormal_uncertainty('lumiSys', math.log(1.026), proc, '*')
            except RuntimeError: pass

        else:
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.20),proc,'triLepMMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.12),proc,'triLepEMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.26),proc,'triLepEEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.24),proc,'triLepEEE')
            except RuntimeError: pass

#     flatpars = {'mean': 0.0, 
#                 'range': [float('-inf'), float('inf')], 
#                 'typ': 'gauss', 
#                 'width': float('inf')}
#     
#     model.distribution.distributions.update({'elFR': flatpars})
# #     model.distribution.distributions.update({'FRsys': flatpars})

    return model


##################################################################################################################

# model = get_model()
model = get_model3L() #defining all norm sys as lognormal here and not use histos

model_summary(model)

# plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 10, n_data = 10)
plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 5000, n_data = 500)
# plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 100000, n_data = 1000)
#plot_exp, plot_obs = bayesian_limits(model,'expected')
plot_exp.write_txt('limits_'+rFileName+'_expected.txt')
plot_obs.write_txt('limits_'+rFileName+'_observed.txt')

report.write_html('htmlout_'+rFileName)
