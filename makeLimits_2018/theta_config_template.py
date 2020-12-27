import os,sys
from operator import itemgetter,attrgetter

# outDir = os.environ['CMSSW_BASE']+'/src/theta/utils/optimization/limits/dummy'
#outDir = '/mnt/data/users/wwong/limits/'+'optimization_reMiniAOD_dummy'+'bW0p5_tZ0p25_tH0p25_41p557fb'+'/'+'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20'+'thetaTemplates_rootfiles'
#DirName='optimization_FWLJMET102X_3lep2017_wywong_102019_step1_FRv2_hadds_step2'
DirName='optimization_FWLJMET102X_3lep2017_wywong_012020_step1_flatFRv4_TrigEff_uFR_hadds_step2'
outDir = '/mnt/data/users/wwong/limits/'+DirName+'bW0p5_tZ0p25_tH0p25_41p557fb'+'/'+'lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20'+'/'+'thetaTemplates_rootfiles'

#input = 'dummy.root'
#input = '/mnt/data/users/wwong/optimization_reMiniAOD_dummy/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20/thetaTemplates_rootfiles/templates_STrebinnedv2_TTM1300_bW0p5_tZ0p25_tH0p25_41p557fb.root'
input = '/mnt/data/users/wwong/'+DirName+'/lep1Pt0_jetPt0_MET20_NJets3_NBJets1_HT0_ST0_mllOS20/thetaTemplates_rootfiles/templates_STrebinnedv2_TTM1300_bW0p5_tZ0p25_tH0p25_41p557fb.root'

rFileName = input.split('/')[-1][:-5]
                                                                                                                                          
def get_model():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True)#,histogram_filter = (lambda s: s.count('jec')==0 and s.count('jer')==0)

    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')
    
    procs = model.processes
    
    for proc in procs:
		if(proc!="ddbkg"):
# 			try: model.add_lognormal_uncertainty('lumiSys', math.log(1.062), proc)
			try: model.add_lognormal_uncertainty('lumiSys', math.log(1.023), proc) #https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM #https://hypernews.cern.ch/HyperNews/CMS/get/physics-announcements/4495.html
			except: pass


    return model

#defining all norm sys as lognormal here and not use histos
#fromJulie's /user_data/jhogan/CMSSW_7_4_14/src/tptp_2016/thetaLimits/theta_combined_template.py May-11-2017
def get_model3L():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True)
#    model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('muR__')==0 and s.count('muF__')==0 and s.count('muRFcorrd__')==0 and s.count('TrigEffWeight')==0 and s.count('elIsoSys')==0 and s.count('elIdSys')==0 and s.count('muIsoSys')==0 and s.count('muIdSys')==0 and s.count('PR__')==0))
#    model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('muR__')==0 and s.count('muF__')==0 and s.count('muRFcorrd__')==0 and s.count('elelelTrigSys')==0 and s.count('elelmuTrigSys')==0 and s.count('elmumuTrigSys')==0 and s.count('mumumuTrigSys')==0 and s.count('elIsoSys')==0 and s.count('elIdSys')==0 and s.count('muIsoSys')==0 and s.count('muIdSys')==0 and s.count('PR__')==0)) #for PRv9
#     model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('muR__')==0 and s.count('muF__')==0 and s.count('muRFcorrd__')==0 and s.count('elelelTrigSys')==0 and s.count('elelmuTrigSys')==0 and s.count('elmumuTrigSys')==0 and s.count('mumumuTrigSys')==0 and s.count('elIsoSys')==0 and s.count('elIdSys')==0 and s.count('muIsoSys')==0 and s.count('muIdSys')==0 and s.count('PRsys__')==0)) #for PRv10

    #                                                                                                                                                                                                                                    
    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')

    procs = model.processes
    obsvs = model.observables.keys()

    for proc in procs:
        if(proc != 'ddbkg'):
#            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.03), proc, 'triLepEEE')
#            except RuntimeError: pass
#            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.02), proc, 'triLepEEM')
#            except RuntimeError: pass
#            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.02), proc, 'triLepEMM')
#            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.045), proc, 'triLep2018EEE')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.030), proc, 'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.015), proc, 'triLep2018EMM')
            except RuntimeError: pass

            try: model.add_lognormal_uncertainty('elRecoSys', math.log(1.03), proc, 'triLep2018EEE')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elRecoSys', math.log(1.02), proc, 'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('elRecoSys', math.log(1.01), proc, 'triLep2018EMM')
            except RuntimeError: pass

            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.02), proc, 'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.04), proc, 'triLep2018EMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.06), proc, 'triLep2018MMM')
            except RuntimeError: pass

            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.015), proc, 'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.030), proc, 'triLep2018EMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.045), proc, 'triLep2018MMM')
            except RuntimeError: pass
 #           try: model.add_lognormal_uncertainty('TrigEffWeight', math.log(1.03), proc, 'triLepEEE')
 #           except RuntimeError: pass
 #           try: model.add_lognormal_uncertainty('TrigEffWeight', math.log(1.03), proc, 'triLepEEM')
 #           except RuntimeError: pass
 #           try: model.add_lognormal_uncertainty('TrigEffWeight', math.log(1.03), proc, 'triLepEMM')
 #           except RuntimeError: pass
 #           try: model.add_lognormal_uncertainty('TrigEffWeight', math.log(1.03), proc, 'triLepMMM')
 #           except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('eeeTrigSys', math.log(1.03), proc, 'triLepEEE')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('eemTrigSys', math.log(1.03), proc, 'triLepEEM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('emmTrigSys', math.log(1.03), proc, 'triLepEMM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('mmmTrigSys', math.log(1.03), proc, 'triLepMMM')
            #except RuntimeError: pass

            try: model.add_lognormal_uncertainty('lumiSys', math.log(1.025), proc, '*')
            except RuntimeError: pass

#         else: #From ttbar closure
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.20),proc,'triLepMMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.12),proc,'triLepEMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.26),proc,'triLepEEM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.24),proc,'triLepEEE')
#             except RuntimeError: pass

#         else: #From ttbar closure + (data-MC)/ddbkg _extraFRsys17Aug
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.36),proc,'triLepMMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.18),proc,'triLepEMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.29),proc,'triLepEEM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.38),proc,'triLepEEE')
#             except RuntimeError: pass

#        else: #From ttbar closure + (data-MC)/ddbkg April 2020 for FRv5 (updated by Jess)
#            try: model.add_lognormal_uncertainty('FRsys',math.log(1.17),proc,'triLepMMM')
#            except RuntimeError: pass
#            try: model.add_lognormal_uncertainty('FRsys',math.log(1.19),proc,'triLepEMM')
#            except RuntimeError: pass
#            try: model.add_lognormal_uncertainty('FRsys',math.log(1.27),proc,'triLepEEM')
#            except RuntimeError: pass
#            try: model.add_lognormal_uncertainty('FRsys',math.log(1.42),proc,'triLepEEE')
#            except RuntimeError: pass

#         else: #From ttbar closure + (data-MC)/ddbkg Sep20-21 for FRv49sys
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.20),proc,'triLepMMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.18),proc,'triLepEMM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.38),proc,'triLepEEM')
#             except RuntimeError: pass
#             try: model.add_lognormal_uncertainty('FRsys',math.log(1.45),proc,'triLepEEE')
#             except RuntimeError: pass

        else: #From ttbcar closure + (data-MC)/ddbkg for FRv1_TrigEff Aug 2020  (updated by Jess)
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.067),proc,'triLep2018MMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.019),proc,'triLep2018EMM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.076),proc,'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_lognormal_uncertainty('FRsys',math.log(1.206),proc,'triLep2018EEE')
            except RuntimeError: pass

            try: model.add_asymmetric_lognormal_uncertainty('muFReta',math.log(0.952),math.log(1.00),proc,'triLep2018MMM')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('muFReta',math.log(0.970),math.log(1.00),proc,'triLep2018EMM')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('muFReta',math.log(0.982),math.log(1.00),proc,'triLep2018EEM')
            except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muFReta',math.log(1.05),proc,'triLepMMM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muFReta',math.log(1.03),proc,'triLepEMM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muFReta',math.log(1.02),proc,'triLepEEM')
            #except RuntimeError: pass

            try: model.add_asymmetric_lognormal_uncertainty('muPRsys',math.log(1.00),math.log(1.054),proc,'triLep2018MMM')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('muPRsys',math.log(1.00),math.log(1.016),proc,'triLep2018EMM')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('muPRsys',math.log(1.00),math.log(1.012),proc,'triLep2018EEM')
            except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muPRsys',math.log(1.05),proc,'triLepMMM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muPRsys',math.log(1.02),proc,'triLepEMM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('muPRsys',math.log(1.01),proc,'triLepEEM')
            #except RuntimeError: pass

            try: model.add_asymmetric_lognormal_uncertainty('elPRsys',math.log(1.00),math.log(1.074),proc,'triLep2018EEE')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('elPRsys',math.log(1.00),math.log(1.026),proc,'triLep2018EEM')
            except RuntimeError: pass
            try: model.add_asymmetric_lognormal_uncertainty('elPRsys',math.log(1.00),math.log(1.008),proc,'triLep2018EMM')
            except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('elPRsys',math.log(1.07),proc,'triLepEEE')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('elPRsys',math.log(1.03),proc,'triLepEEM')
            #except RuntimeError: pass
            #try: model.add_lognormal_uncertainty('elPRsys',math.log(1.01),proc,'triLepEMM')
            #except RuntimeError: pass
    return model

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
#plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 5000, n_data = 500)
plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 100000, n_data = 1000)
#plot_exp, plot_obs = bayesian_limits(model,'expected')
plot_exp.write_txt('limits_'+rFileName+'_expected.txt')
plot_obs.write_txt('limits_'+rFileName+'_observed.txt')

report.write_html('htmlout_'+rFileName)
