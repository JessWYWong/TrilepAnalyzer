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

model = get_model()

##################################################################################################################

model_summary(model)

plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 5000, n_data = 500)
#plot_exp, plot_obs = bayesian_limits(model,'expected')
plot_exp.write_txt('limits_'+rFileName+'_expected.txt')
plot_obs.write_txt('limits_'+rFileName+'_observed.txt')

report.write_html('htmlout_'+rFileName)
