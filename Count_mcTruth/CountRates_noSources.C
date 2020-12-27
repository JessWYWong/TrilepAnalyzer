
using namespace std;

void CountRates_noSources(){

	bool PrintMixedChannels = false;
	cout << "PrintMixedChannels = " << PrintMixedChannels << endl;	
	bool printSource = false;
	
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V3_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V4_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V6_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V7_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V8_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V9_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";

//	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
//	TString f_str = "/mnt/data/users/wwong/FWLJMET102X_3lep2017_062019_wywong_step1_FRv1_hadds_step2/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root";
	//TString f_str = "/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv4_uFR_hadds_step2/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root";
	TString f_str = "/mnt/data/users/wwong/FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv2_prefiring_hadds_step2/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_newTT_2017_3_21_rizki_mcClosure_step1hadds/nominal/TT_Mtt-700to1000_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_newTT_2017_3_21_rizki_mcClosure_step1hadds/nominal/TT_Mtt-1000toInf_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";

// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root";



	TFile *f = TFile::Open(f_str, "READ");
	
	cout << "Opening file:" << f_str << endl;

	TTree *t = (TTree*) f->Get("ljmet");

	TH1D *h = new TH1D();
	

// 	TString observ = "AllLeptonPt_PtOrdered";
	TString observ = "AK4HTpMETpLepPt";
	TString trig = " && MCPastTrigger_dilep == 1";
	TString trilep = " && isPassTrilepton==1";
	TString lepPt = " && (AllLeptonPt_PtOrdered[0]>30 && AllLeptonPt_PtOrdered[1]>30 && AllLeptonPt_PtOrdered[2]>0)";
	TString exactly3Lep = " && AllLeptonCount_PtOrdered==3";

	TString njet = " && 1";
// 	TString njet = " && (NJets_MultiLepCalc ==1)";
// 	TString njet = " && (NJets_MultiLepCalc ==2)";
// 	TString njet = " && (NJets_MultiLepCalc > 2)";

// 	TString bjet = " && 1";
	TString bjet = " && (NJetsBTagwithSF_MultiLepCalc >=1)";


// 	TString basic_cut = "1 "+trig+trilep+lepPt+exactly3Lep+njet+bjet;
// 	TString basic_cut = "1 "+trig+lepPt+exactly3Lep+njet+bjet;

	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_MultiLepCalc >= 0) && (NJets_MultiLepCalc >= 0) && (NJetsBTagwithSF_MultiLepCalc >= 0) && DataPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";
// 	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_MultiLepCalc >= 0) && (NJets_MultiLepCalc >= 0) && (NJetsBTagwithSF_MultiLepCalc >= 0) && MCPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";

	cout << "Counting with basic cuts: " << basic_cut << endl;	
	
	TString isTTT = " && isTTT"; 
	TString isTTL = " && isTTL"; 
	TString isTLT = " && isTLT"; 
	TString isLTT = " && isLTT"; 
	
	TString isEEE = " && isEEE";
	TString isEEM = " && isEEM";
	TString isEMM = " && isEMM";
	TString isMMM = " && isMMM"; 

	TString isEEM_ = " && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)";
	TString isEME_ = " && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0)";
	TString isMEE_ = " && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==0)";
	TString isEMM_ = " && (AllLeptonFlavor_PtOrdered[0]==0 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==1)";
	TString isMEM_ = " && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==0 && AllLeptonFlavor_PtOrdered[2]==1)";
	TString isMME_ = " && (AllLeptonFlavor_PtOrdered[0]==1 && AllLeptonFlavor_PtOrdered[1]==1 && AllLeptonFlavor_PtOrdered[2]==0)";


	TString isPPP = " && ( ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==1 ) )";
	
	TString isPPF = " ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isPFP = " ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";
	TString isFPP = " ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";

	TString isPFF = " ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isFPF = " ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isFFP = " ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";

	TString isFFF = " && ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==0 )  ";

	/////////////

// 	TString isPPF_isMatched = " && ( AllLeptonIsMatched_PtOrdered[0]==1 && AllLeptonIsMatched_PtOrdered[1]==1 && AllLeptonIsMatched_PtOrdered[2]==0 )  ";
// 	TString isPFP_isMatched = " && ( AllLeptonIsMatched_PtOrdered[0]==1 && AllLeptonIsMatched_PtOrdered[1]==0 && AllLeptonIsMatched_PtOrdered[2]==1 )  " ;
// 	TString isFPP_isMatched = " && ( AllLeptonIsMatched_PtOrdered[0]==0 && AllLeptonIsMatched_PtOrdered[1]==1 && AllLeptonIsMatched_PtOrdered[2]==1 ) ";
// 
// 	TString isPPF_isFromB = " && ( AllLeptonIsFromB_PtOrdered[0]==0 && AllLeptonIsFromB_PtOrdered[1]==0 && AllLeptonIsFromB_PtOrdered[2]==1 )  ";
// 	TString isPFP_isFromB = " && ( AllLeptonIsFromB_PtOrdered[0]==0 && AllLeptonIsFromB_PtOrdered[1]==1 && AllLeptonIsFromB_PtOrdered[2]==0 )  " ;
// 	TString isFPP_isFromB = " && ( AllLeptonIsFromB_PtOrdered[0]==1 && AllLeptonIsFromB_PtOrdered[1]==0 && AllLeptonIsFromB_PtOrdered[2]==0 ) ";
// 
// 	TString isPPF_isFromC = " && ( AllLeptonIsFromC_PtOrdered[0]==0 && AllLeptonIsFromC_PtOrdered[1]==0 && AllLeptonIsFromC_PtOrdered[2]==1 )  ";
// 	TString isPFP_isFromC = " && ( AllLeptonIsFromC_PtOrdered[0]==0 && AllLeptonIsFromC_PtOrdered[1]==1 && AllLeptonIsFromC_PtOrdered[2]==0 )  " ;
// 	TString isFPP_isFromC = " && ( AllLeptonIsFromC_PtOrdered[0]==1 && AllLeptonIsFromC_PtOrdered[1]==0 && AllLeptonIsFromC_PtOrdered[2]==0 ) ";
// 
// 	TString isPPF_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[0]==0 && AllLeptonIsFromHL_PtOrdered[1]==0 && AllLeptonIsFromHL_PtOrdered[2]==1 )  ";
// 	TString isPFP_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[0]==0 && AllLeptonIsFromHL_PtOrdered[1]==1 && AllLeptonIsFromHL_PtOrdered[2]==0 )  " ;
// 	TString isFPP_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[0]==1 && AllLeptonIsFromHL_PtOrdered[1]==0 && AllLeptonIsFromHL_PtOrdered[2]==0 ) ";
// 
// 	TString isPPF_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[0]==0 && AllLeptonIsFromPh_PtOrdered[1]==0 && AllLeptonIsFromPh_PtOrdered[2]==1 )  ";
// 	TString isPFP_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[0]==0 && AllLeptonIsFromPh_PtOrdered[1]==1 && AllLeptonIsFromPh_PtOrdered[2]==0 )  " ;
// 	TString isFPP_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[0]==1 && AllLeptonIsFromPh_PtOrdered[1]==0 && AllLeptonIsFromPh_PtOrdered[2]==0 ) ";
// 
// 	TString isPPF_isFromL = " && ( AllLeptonIsFromL_PtOrdered[0]==0 && AllLeptonIsFromL_PtOrdered[1]==0 && AllLeptonIsFromL_PtOrdered[2]==1 )  ";
// 	TString isPFP_isFromL = " && ( AllLeptonIsFromL_PtOrdered[0]==0 && AllLeptonIsFromL_PtOrdered[1]==1 && AllLeptonIsFromL_PtOrdered[2]==0 )  " ;
// 	TString isFPP_isFromL = " && ( AllLeptonIsFromL_PtOrdered[0]==1 && AllLeptonIsFromL_PtOrdered[1]==0 && AllLeptonIsFromL_PtOrdered[2]==0 ) ";

	TString isPPF_isMatched = " && ( AllLeptonIsMatched_PtOrdered[2]==0 ) ";
	TString isPFP_isMatched = " && ( AllLeptonIsMatched_PtOrdered[1]==0 ) " ;

	TString isPPF_isFromB = " && ( AllLeptonIsFromB_PtOrdered[2]==1 )  ";
	TString isPFP_isFromB = " && ( AllLeptonIsFromB_PtOrdered[1]==1 )  " ;
	TString isFPP_isFromB = " && ( AllLeptonIsFromB_PtOrdered[0]==1 ) ";

	TString isPPF_isFromC = " && ( AllLeptonIsFromC_PtOrdered[2]==1 && AllLeptonIsFromB_PtOrdered[2]==0)  ";
	TString isPFP_isFromC = " && ( AllLeptonIsFromC_PtOrdered[1]==1 && AllLeptonIsFromB_PtOrdered[1]==0)  " ;
	TString isFPP_isFromC = " && ( AllLeptonIsFromC_PtOrdered[0]==1 && AllLeptonIsFromB_PtOrdered[0]==0) ";

	TString isPPF_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[2]==1 )  ";
	TString isPFP_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[1]==1 )  " ;
	TString isFPP_isFromHL = " && ( AllLeptonIsFromHL_PtOrdered[0]==1 ) ";

	TString isPPF_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[2]==1 )  ";
	TString isPFP_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[1]==1 )  " ;
	TString isFPP_isFromPh = " && ( AllLeptonIsFromPh_PtOrdered[0]==1 ) ";

	TString isPPF_isFromL = " && ( AllLeptonIsFromL_PtOrdered[2]==1 && AllLeptonIsFromB_PtOrdered[2]==0 && AllLeptonIsFromC_PtOrdered[2]==0)  ";
	TString isPFP_isFromL = " && ( AllLeptonIsFromL_PtOrdered[1]==1 && AllLeptonIsFromB_PtOrdered[1]==0 && AllLeptonIsFromC_PtOrdered[1]==0)  " ;
	TString isFPP_isFromL = " && ( AllLeptonIsFromL_PtOrdered[0]==1 && AllLeptonIsFromB_PtOrdered[0]==0 && AllLeptonIsFromC_PtOrdered[0]==0) ";


	int TTT_PPF = 0;		
	int TTT_PFP = 0;		
	int TTT_FPP = 0;		
	int TTL_PPF = 0;		
	int TLT_PFP = 0;		
	int LTT_FPP = 0;		

	int PFF = 0;
	int FPF = 0;
	int FFP = 0;

	int EEE = 0;
	int EEM = 0;
	int EMM = 0;
	int MMM = 0;
	int ALL = 0;

	int EEE_ppp = 0;
	int EEM_ppp = 0;
	int EMM_ppp = 0;
	int MMM_ppp = 0;
	int ALL_ppp = 0;

	int EEE_ppf = 0;
	int EEM_ppf = 0;
	int EMM_ppf = 0;
	int MMM_ppf = 0;
	int ALL_ppf = 0;

	int EEE_pff = 0;
	int EEM_pff = 0;
	int EMM_pff = 0;
	int MMM_pff = 0;
	int ALL_pff = 0;
	
	int EEE_fff = 0;
	int EEM_fff = 0;
	int EMM_fff = 0;
	int MMM_fff = 0;
	int ALL_fff = 0;


        

	//===========EEE==============
	
	int EEE_ttt = t->Draw(observ,basic_cut+isEEE+" &&  isTTT " );

	//1prompt
	EEE_pff = t->Draw(observ,basic_cut+isEEE+" &&  "+isPFF );
	int EEE_fpf = t->Draw(observ,basic_cut+isEEE+" &&  "+isFPF );
	int EEE_ffp = t->Draw(observ,basic_cut+isEEE+" &&  "+isFFP );

	//2 prompts (1 fake)
	EEE_ppf = t->Draw(observ,basic_cut+isEEE+" && "+isPPF );
	int EEE_pfp = t->Draw(observ,basic_cut+isEEE+" && "+isPFP  );
	int EEE_fpp = t->Draw(observ,basic_cut+isEEE+" && "+isFPP  );

	int EEE_ppf_ttl = t->Draw(observ,basic_cut+isEEE+" && ( "+isPPF+" && isTTL)" );
	int EEE_pfp_tlt = t->Draw(observ,basic_cut+isEEE+" && ( "+isPFP+" && isTLT)" );
	int EEE_fpp_ltt = t->Draw(observ,basic_cut+isEEE+" && ( "+isFPP+" && isLTT)" );

	int EEE_ppf_ttt = t->Draw(observ,basic_cut+isEEE+" && ( "+isPPF+" || "+isPFP+" || "+isFPP+" ) && isTTT " );

	//3 prompts , 3 fakes
	EEE_ppp = t->Draw(observ,basic_cut+isEEE+isPPP);
	EEE_fff = t->Draw(observ,basic_cut+isEEE+isFFF);

	//All
	EEE = t->Draw(observ,basic_cut+isEEE);

	//

	//
	cout << " ========= EEE ========= " << endl;
	cout << "Counts of EEE: FFF(" << EEE_fff<< "), PFF(" <<EEE_pff+EEE_fpf+EEE_ffp <<"), PPF("<< EEE_ppf+EEE_pfp+EEE_fpp<<"), PPP("<< EEE_ppp <<") : "<< EEE<<", TTT("<< EEE_ttt << ")"<<endl; 
	cout << "	--1 fake /2 prompts:   "<< endl;
	cout << "       IsTTT f(T) : " << EEE_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       IsTTL f(L) : " << EEE_ppf_ttl+EEE_pfp_tlt+EEE_fpp_ltt << endl;
	if(printSource){
	}
	float eee_fT = EEE_ppf_ttt*1.0;
	float eee_fL = (EEE_ppf_ttl+EEE_pfp_tlt+EEE_fpp_ltt )*1.0;
	float eee_FR = eee_fT / ( eee_fT  + eee_fL ) ;
	cout << "       		el fake rate  : " << eee_FR << endl;
// if(PrintMixedChannels){
	//===========EEM==============

	int EEM_ttt = t->Draw(observ,basic_cut+isEEM_+isTTT);
	int EME_ttt = t->Draw(observ,basic_cut+isEME_+isTTT);
	int MEE_ttt = t->Draw(observ,basic_cut+isMEE_+isTTT);

	//1prompt
	EEM_pff = t->Draw(observ,basic_cut+isEEM_+" && "+isPFF);
	int EEM_fpf = t->Draw(observ,basic_cut+isEEM_+" && "+isFPF);
	int EEM_ffp = t->Draw(observ,basic_cut+isEEM_+" && "+isFFP);

	int EME_pff = t->Draw(observ,basic_cut+isEME_+" && "+isPFF);
	int EME_fpf = t->Draw(observ,basic_cut+isEME_+" && "+isFPF);
	int EME_ffp = t->Draw(observ,basic_cut+isEME_+" && "+isFFP);

	int MEE_pff = t->Draw(observ,basic_cut+isMEE_+" && "+isPFF);
	int MEE_fpf = t->Draw(observ,basic_cut+isMEE_+" && "+isFPF);
	int MEE_ffp = t->Draw(observ,basic_cut+isMEE_+" && "+isFFP);

	//EEM - 2prompts
	EEM_ppf = t->Draw(observ,basic_cut+isEEM_+" && "+isPPF);
	int EEM_pfp = t->Draw(observ,basic_cut+isEEM_+" && "+isPFP);
	int EEM_fpp = t->Draw(observ,basic_cut+isEEM_+" && "+isFPP);


	int EEM_ppf_ttl = t->Draw(observ,basic_cut+isEEM_+" && "+isPPF+isTTL);
	int EEM_pfp_tlt = t->Draw(observ,basic_cut+isEEM_+" && "+isPFP+isTLT);
	int EEM_fpp_ltt = t->Draw(observ,basic_cut+isEEM_+" && "+isFPP+isLTT);

	int EEM_ppf_ttt = t->Draw(observ,basic_cut+isEEM_+" && "+isPPF+isTTT);
	int EEM_pfp_ttt = t->Draw(observ,basic_cut+isEEM_+" && "+isPFP+isTTT);
	int EEM_fpp_ttt = t->Draw(observ,basic_cut+isEEM_+" && "+isFPP+isTTT);


	//EME - 2prompts
	int EME_ppf = t->Draw(observ,basic_cut+isEME_+" && "+isPPF);
	int EME_pfp = t->Draw(observ,basic_cut+isEME_+" && "+isPFP);
	int EME_fpp = t->Draw(observ,basic_cut+isEME_+" && "+isFPP);


	int EME_ppf_ttl = t->Draw(observ,basic_cut+isEME_+" && "+isPPF+isTTL);
	int EME_pfp_tlt = t->Draw(observ,basic_cut+isEME_+" && "+isPFP+isTLT);
	int EME_fpp_ltt = t->Draw(observ,basic_cut+isEME_+" && "+isFPP+isLTT);

	int EME_ppf_ttt = t->Draw(observ,basic_cut+isEME_+" && "+isPPF+isTTT);
	int EME_pfp_ttt = t->Draw(observ,basic_cut+isEME_+" && "+isPFP+isTTT);
	int EME_fpp_ttt = t->Draw(observ,basic_cut+isEME_+" && "+isFPP+isTTT);


	//MEE - 2prompts
	int MEE_ppf = t->Draw(observ,basic_cut+isMEE_+" && "+isPPF);
	int MEE_pfp = t->Draw(observ,basic_cut+isMEE_+" && "+isPFP);
	int MEE_fpp = t->Draw(observ,basic_cut+isMEE_+" && "+isFPP);


	int MEE_ppf_ttl = t->Draw(observ,basic_cut+isMEE_+" && "+isPPF+isTTL);
	int MEE_pfp_tlt = t->Draw(observ,basic_cut+isMEE_+" && "+isPFP+isTLT);
	int MEE_fpp_ltt = t->Draw(observ,basic_cut+isMEE_+" && "+isFPP+isLTT);

	int MEE_ppf_ttt = t->Draw(observ,basic_cut+isMEE_+" && "+isPPF+isTTT);
	int MEE_pfp_ttt = t->Draw(observ,basic_cut+isMEE_+" && "+isPFP+isTTT);
	int MEE_fpp_ttt = t->Draw(observ,basic_cut+isMEE_+" && "+isFPP+isTTT);


	//no prompt/fake
	EEM_ppp = t->Draw(observ,basic_cut+isEEM+isPPP);
	EEM_fff = t->Draw(observ,basic_cut+isEEM+isFFF);

	//all
	EEM = t->Draw(observ,basic_cut+isEEM);
	

	cout << " ========= EEM ========= " << endl;
	float eem_pff = EEM_pff+EEM_fpf+EEM_ffp + EME_pff+EME_fpf+EME_ffp + MEE_pff+MEE_fpf+MEE_ffp ;  
	float eem_ppf = EEM_ppf+EEM_pfp+EEM_fpp + EME_ppf+EME_pfp+EME_fpp + MEE_ppf+MEE_pfp+MEE_fpp ;  
	float eem_ttt = EEM_ttt+EME_ttt+MEE_ttt;
	cout << "Counts of EEM: FFF(" << EEM_fff<< "), PFF(" <<eem_pff <<"), PPF("<< eem_ppf <<"), PPP("<<EEM_ppp <<") : "<< EEM<< ", TTT(" << eem_ttt <<")" << endl; 
	cout << "	--1 fake-- :  "<< endl;
	cout << "	f(T):   "<< endl;
	cout << "       EE(M) PPF TTT (fake mu) : " << EEM_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       E(E)M PFP TTT (fake el) : " << EEM_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (E)EM FPP TTT (fake el) : " << EEM_fpp_ttt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       EM(E) PPF TTT (fake el) : " << EME_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       E(M)E PFP TTT (fake mu) : " << EME_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (E)ME FPP TTT (fake el) : " << EME_fpp_ttt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       ME(E) PPF TTT (fake el) : " << MEE_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       M(E)E PFP TTT (fake el) : " << MEE_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (M)EE FPP TTT (fake mu) : " << MEE_fpp_ttt << endl;
	if(printSource){
	}
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EE(M) PPF TTL (fake mu) : " << EEM_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       E(E)M PFP TLT (fake el) : " << EEM_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (E)EM FPP LTT (fake el) : " << EEM_fpp_ltt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       EM(E) PPF TTL (fake el) : " << EME_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       E(M)E PFP TLT (fake mu) : " << EME_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (E)ME FPP LTT (fake el) : " << EME_fpp_ltt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       ME(E) PPF TTL (fake el) : " << MEE_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       M(E)E PFP TLT (fake el) : " << MEE_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (M)EE FPP LTT (fake mu) : " << MEE_fpp_ltt << endl;
	if(printSource){
	}
	cout << "       ---------------------  " << endl;
// 	cout << "			EE PP f(T): "<< EEM_ppf_ttt + EME_pfp_ttt + MEE_fpp_ttt<< endl;
// 	cout << "			EE PP f(L): "<< EEM_ppf_ttl + EME_pfp_tlt + MEE_fpp_ltt<< endl;
// 	cout << "			EM PP f(T): "<< EEM_pfp_ttt + EEM_fpp_ttt + EME_ppf_ttt + EME_fpp_ttt + MEE_ppf_ttt + MEE_pfp_ttt<< endl;
// 	cout << "			EM PP f(L): "<< EEM_pfp_tlt + EEM_fpp_ltt + EME_ppf_ttl + EME_fpp_ltt + MEE_ppf_ttl + MEE_pfp_tlt<< endl;
	cout << "       ---------------------  " << endl;
	float eem_e_fT = EEM_pfp_ttt+EEM_fpp_ttt+EME_ppf_ttt+EME_fpp_ttt+MEE_ppf_ttt+MEE_pfp_ttt;


	float eem_e_fL = EEM_pfp_tlt+EEM_fpp_ltt+EME_ppf_ttl+EME_fpp_ltt+MEE_ppf_ttl+MEE_pfp_tlt;



	float eem_e_FR = eem_e_fT / ( eem_e_fT + eem_e_fL );
	cout << "       fake el f(T)          : " << eem_e_fT << endl;
	if(printSource){
	}
	cout << "       fake el f(L)          : " << eem_e_fL << endl;
	if(printSource){
	}
	cout << "       		el fake rate  : " << eem_e_fT / ( eem_e_fT + eem_e_fL ) << endl;

	float eem_m_fT = EEM_ppf_ttt+EME_pfp_ttt+MEE_fpp_ttt;


	float eem_m_fL = EEM_ppf_ttl+EME_pfp_tlt+MEE_fpp_ltt;


	float eem_m_FR = eem_m_fT / ( eem_m_fT + eem_m_fL );
	cout << "       fake mu f(T)          : " << eem_m_fT<<endl;
	if(printSource){
	}
	cout << "       fake mu f(L)          : " << eem_m_fL<<endl;
	if(printSource){
	}
	cout << "       		mu fake rate  : " << eem_m_fT / ( eem_m_fT + eem_m_fL ) << endl;
	//===========EMM==============
	
	int EMM_ttt = t->Draw(observ,basic_cut+isEMM_+isTTT);
	int MEM_ttt = t->Draw(observ,basic_cut+isMEM_+isTTT);
	int MME_ttt = t->Draw(observ,basic_cut+isMME_+isTTT);

	//1 fake / 2 prompts
	EMM_ppf = t->Draw(observ,basic_cut+isEMM_+" && "+isPPF);
	int EMM_pfp = t->Draw(observ,basic_cut+isEMM_+" && "+isPFP);
	int EMM_fpp = t->Draw(observ,basic_cut+isEMM_+" && "+isFPP);







	int EMM_ppf_ttt = t->Draw(observ,basic_cut+isEMM_+" && "+isPPF+isTTT);
	int EMM_pfp_ttt = t->Draw(observ,basic_cut+isEMM_+" && "+isPFP+isTTT);
	int EMM_fpp_ttt = t->Draw(observ,basic_cut+isEMM_+" && "+isFPP+isTTT);

	int EMM_ppf_ttl = t->Draw(observ,basic_cut+isEMM_+" && "+isPPF+isTTL);
	int EMM_pfp_tlt = t->Draw(observ,basic_cut+isEMM_+" && "+isPFP+isTLT);
	int EMM_fpp_ltt = t->Draw(observ,basic_cut+isEMM_+" && "+isFPP+isLTT);












	int MEM_ppf = t->Draw(observ,basic_cut+isMEM_+" && "+isPPF);
	int MEM_pfp = t->Draw(observ,basic_cut+isMEM_+" && "+isPFP);
	int MEM_fpp = t->Draw(observ,basic_cut+isMEM_+" && "+isFPP);

	int MEM_ppf_ttt = t->Draw(observ,basic_cut+isMEM_+" && "+isPPF+isTTT);
	int MEM_pfp_ttt = t->Draw(observ,basic_cut+isMEM_+" && "+isPFP+isTTT);
	int MEM_fpp_ttt = t->Draw(observ,basic_cut+isMEM_+" && "+isFPP+isTTT);

	int MEM_ppf_ttl = t->Draw(observ,basic_cut+isMEM_+" && "+isPPF+isTTL);
	int MEM_pfp_tlt = t->Draw(observ,basic_cut+isMEM_+" && "+isPFP+isTLT);
	int MEM_fpp_ltt = t->Draw(observ,basic_cut+isMEM_+" && "+isFPP+isLTT);
















	int MME_ppf = t->Draw(observ,basic_cut+isMME_+" && "+isPPF);
	int MME_pfp = t->Draw(observ,basic_cut+isMME_+" && "+isPFP);
	int MME_fpp = t->Draw(observ,basic_cut+isMME_+" && "+isFPP);





	int MME_ppf_ttt = t->Draw(observ,basic_cut+isMME_+" && "+isPPF+isTTT);
	int MME_pfp_ttt = t->Draw(observ,basic_cut+isMME_+" && "+isPFP+isTTT);
	int MME_fpp_ttt = t->Draw(observ,basic_cut+isMME_+" && "+isFPP+isTTT);

	int MME_ppf_ttl = t->Draw(observ,basic_cut+isMME_+" && "+isPPF+isTTL);
	int MME_pfp_tlt = t->Draw(observ,basic_cut+isMME_+" && "+isPFP+isTLT);
	int MME_fpp_ltt = t->Draw(observ,basic_cut+isMME_+" && "+isFPP+isLTT);











	//2fakes / 1 prompt
	
	EMM_pff = t->Draw(observ,basic_cut+isEMM_+" && "+isPFF);
	int EMM_fpf = t->Draw(observ,basic_cut+isEMM_+" && "+isFPF);
	int EMM_ffp = t->Draw(observ,basic_cut+isEMM_+" && "+isFFP);

	int MEM_pff = t->Draw(observ,basic_cut+isMEM_+" && "+isPFF);
	int MEM_fpf = t->Draw(observ,basic_cut+isMEM_+" && "+isFPF);
	int MEM_ffp = t->Draw(observ,basic_cut+isMEM_+" && "+isFFP);

	int MME_pff = t->Draw(observ,basic_cut+isMME_+" && "+isPFF);
	int MME_fpf = t->Draw(observ,basic_cut+isMME_+" && "+isFPF);
	int MME_ffp = t->Draw(observ,basic_cut+isMME_+" && "+isFFP);
	

	//no prompt/fake
	EMM_ppp = t->Draw(observ,basic_cut+isEMM+isPPP);
	EMM_fff = t->Draw(observ,basic_cut+isEMM+isFFF);

	//all
	EMM = t->Draw(observ,basic_cut+isEMM);

	cout << " ========= EMM ========= " << endl;
	float emm_pff = EMM_pff+EMM_fpf+EMM_ffp + MEM_pff+MEM_fpf+MEM_ffp + MME_pff+MME_fpf+MME_ffp ;  
	float emm_ppf = EMM_ppf+EMM_pfp+EMM_fpp + MEM_ppf+MEM_pfp+MEM_fpp + MME_ppf+MME_pfp+MME_fpp ;  
	float emm_ttt = EMM_ttt+MEM_ttt+MME_ttt;  
	cout << "Counts of EMM: FFF(" << EMM_fff<< "), PFF(" <<emm_pff <<"), PPF("<< emm_ppf <<"), PPP("<<EMM_ppp <<") : "<< EMM<< ", TTT("<< emm_ttt<< ")"<<endl; 
	cout << "	--1 fake-- :  "<< endl;
	cout << "	f(T):   "<< endl;
	cout << "       EM(M) PPF TTT (fake mu) : " << EMM_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       E(M)M PFP TTT (fake mu) : " << EMM_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (E)MM FPP TTT (fake el) : " << EMM_fpp_ttt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       ME(M) PPF TTT (fake mu) : " << MEM_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       M(E)M PFP TTT (fake el) : " << MEM_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (M)EM FPP TTT (fake mu) : " << MEM_fpp_ttt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       MM(E) PPF TTT (fake el) : " << MME_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       M(M)E PFP TTT (fake mu) : " << MME_pfp_ttt << endl;
	if(printSource){
	}
	cout << "       (M)ME FPP TTT (fake mu) : " << MME_fpp_ttt << endl;
	if(printSource){
	}
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EM(M) PPF TTL (fake mu) : " << EMM_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       E(M)M PFP TLT (fake mu) : " << EMM_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (E)MM FPP LTT (fake el) : " << EMM_fpp_ltt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       ME(M) PPF TTL (fake mu) : " << MEM_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       M(E)M PFP TLT (fake el) : " << MEM_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (M)EM FPP LTT (fake mu) : " << MEM_fpp_ltt << endl;
	if(printSource){
	}
	cout << "-" << endl;
	cout << "       MM(E) PPF TTL (fake el) : " << MME_ppf_ttl << endl;
	if(printSource){
	}
	cout << "       M(M)E PFP TLT (fake mu) : " << MME_pfp_tlt << endl;
	if(printSource){
	}
	cout << "       (M)ME FPP LTT (fake mu) : " << MME_fpp_ltt << endl;
	if(printSource){
	}
	cout << "       ---------------------  " << endl;
// 	cout << "       	EM PP f(T): "<< EMM_ppf_ttt+EMM_pfp_ttt+MEM_ppf_ttt+MEM_fpp_ttt+MME_pfp_ttt+MME_fpp_ttt<< endl;
// 	cout << "			EM PP f(L): "<< EMM_ppf_ttl+EMM_pfp_tlt+MEM_ppf_ttl+MEM_fpp_ltt+MME_pfp_tlt+MME_fpp_ltt<< endl;
// 	cout << "			MM PP f(T): "<< EMM_fpp_ttt+MEM_pfp_ttt+MME_ppf_ttt<< endl;
// 	cout << " 			MM PP f(L): "<< EMM_pfp_tlt+MEM_pfp_tlt+MME_ppf_ttl<< endl;

	float emm_e_fT = EMM_fpp_ttt+MEM_pfp_ttt+MME_ppf_ttt;


	float emm_e_fL = EMM_fpp_ltt+MEM_pfp_tlt+MME_ppf_ttl;


	float emm_e_FR = emm_e_fT / ( emm_e_fT + emm_e_fL );
	cout << "       fake el f(T)          : " << emm_e_fT << endl;
	if(printSource){
	}
	cout << "       fake el f(L)          : " << emm_e_fL << endl;
	if(printSource){
	}
	cout << "       		el fake rate  : " << emm_e_fT / ( emm_e_fT + emm_e_fL ) << endl;

	float emm_m_fT = EMM_ppf_ttt+EMM_pfp_ttt+ MEM_ppf_ttt+ MEM_fpp_ttt+ MME_pfp_ttt+ MME_fpp_ttt;


	float emm_m_fL = EMM_ppf_ttl+EMM_pfp_tlt+ MEM_ppf_ttl+ MEM_fpp_ltt+ MME_pfp_tlt+ MME_fpp_ltt;


	float emm_m_FR = emm_m_fT / ( emm_m_fT + emm_m_fL );
	cout << "       fake mu f(T)          : " << emm_m_fT <<endl;
	if(printSource){
	}
	cout << "       fake mu f(L)          : " << emm_m_fL <<endl;
	if(printSource){
	}
	cout << "       		mu fake rate  : " << emm_m_fT / ( emm_m_fT + emm_m_fL ) << endl;


// }
// 	===========MMM==============

	int MMM_ttt = t->Draw(observ,basic_cut+isMMM+" &&  isTTT " );
	
	MMM_pff = t->Draw(observ,basic_cut+isMMM+" &&  "+isPFF );
	int MMM_fpf = t->Draw(observ,basic_cut+isMMM+" &&  "+isFPF );
	int MMM_ffp = t->Draw(observ,basic_cut+isMMM+" &&  "+isFFP );

	MMM_ppf = t->Draw(observ,basic_cut+isMMM+" && "+ isPPF  );
	int MMM_pfp = t->Draw(observ,basic_cut+isMMM+" && "+ isPFP );
	int MMM_fpp = t->Draw(observ,basic_cut+isMMM+" && "+ isFPP  );	





	int MMM_ppf_ttl = t->Draw(observ,basic_cut+isMMM+" && ( "+isPPF+" && isTTL)" );
	int MMM_pfp_tlt = t->Draw(observ,basic_cut+isMMM+" && ( "+isPFP+" && isTLT)" );
	int MMM_fpp_ltt = t->Draw(observ,basic_cut+isMMM+" && ( "+isFPP+" && isLTT)" );
	int MMM_ppf_ttt = t->Draw(observ,basic_cut+isMMM+" && ( "+isPPF+" || "+isPFP+" || "+isFPP+" ) && isTTT " );

	MMM_ppp = t->Draw(observ,basic_cut+isMMM+isPPP);
	MMM_fff = t->Draw(observ,basic_cut+isMMM+isFFF);

	MMM = t->Draw(observ,basic_cut+isMMM);

	//

	//


	cout << " ========= MMM ========= " << endl;
	cout << "Counts of MMM: FFF(" << MMM_fff<< "), PFF(" <<MMM_pff+MMM_fpf+MMM_ffp <<"), PPF("<< MMM_ppf+MMM_pfp+MMM_fpp<<"), PPP("<< MMM_ppp <<") : "<< MMM<< ", TTT(" <<MMM_ttt  << ")"<<endl; 
	cout << "	1 fake / 2 prompts:   "<< endl;
	cout << "       IsTTT f(T)  : " << MMM_ppf_ttt << endl;
	if(printSource){
	}
	cout << "       IsTTL f(L) : " << MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt << endl;
	if(printSource){
	}
	float mmm_fT = MMM_ppf_ttt*1.0;
	float mmm_fL = (MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt )*1.0;
	float mmm_FR = mmm_fT / ( mmm_fT  + mmm_fL ) ;
	cout << "       		mu fake rate  : " << mmm_FR << endl;
	cout << "       ---------------------  " << endl;
	cout << "			MMM PPF / MMM		: " << (MMM_ppf+MMM_pfp+MMM_fpp)<<" / "<<MMM <<" = "<< 1.0*(MMM_ppf+MMM_pfp+MMM_fpp)/MMM << endl; 
	
	//===========ALL==============
	
	cout << " ========= ALL ========= " << endl;

	ALL_pff = t->Draw(observ,basic_cut+" && ( "+isPFF+" || "+isFPF+" || "+isFFP+")" );
	ALL_ppf = t->Draw(observ,basic_cut+" && ( "+isPPF+" || "+isPFP+" || "+isFPP+")" );
	ALL_ppp = t->Draw(observ,basic_cut+isPPP);
	ALL_fff = t->Draw(observ,basic_cut+isFFF);
	ALL = t->Draw(observ,basic_cut);


   	printf("Counts of ALL: FFF(%i), PFF(%i), PPF(%i), PPP(%i) : %i \n", ALL_fff, ALL_pff, ALL_ppf, ALL_ppp,  ALL);


	cout<< ""<< endl;
	cout<< "Systematic uncertainty due to PPP count: "<< 1.0*ALL_ppp/ALL *100. << "%" <<endl; 	
	cout<< ""<< endl;
		
	cout << " ========= FINAL RESULT ========= " << endl;
	cout << "" << endl;
	cout << "TTbar MC truth with basic cuts: " << basic_cut << endl;	
	cout << "" << endl;
	cout << "el fake rate (EEE): " << eee_FR << endl;
	cout << "el fake rate (EEM): " << eem_e_FR << endl;
	cout << "el fake rate (EMM): " << emm_e_FR << endl;
	cout << "-" << endl;
	cout << "		el fake rate (EEE+EEM+EMM) : " << (eee_fT +  eem_e_fT +  emm_e_fT) / ( eee_fT  + eee_fL + eem_e_fT + eem_e_fL + emm_e_fT + emm_e_fL ) <<endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << "mu fake rate (EEM): " << eem_m_FR << endl;
	cout << "mu fake rate (EMM): " << emm_m_FR << endl;
	cout << "mu fake rate (MMM): " << mmm_FR << endl;
	cout << "-" << endl;
	cout << "		mu fake rate (MMM+EMM+EEM) : " << (mmm_fT +  eem_m_fT +  emm_m_fT) / ( mmm_fT  + mmm_fL + eem_m_fT + eem_m_fL + emm_m_fT + emm_m_fL ) <<endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << "NOTE: fake rate = f(T) / [f(T)+f(L)] " << endl;
	cout << "" << endl;
	
	cout << " ========= Some more RESULTs summary ========= " << endl;
	cout << "       EEE---------------------  " << endl;
	cout << "			EEE PPF / EEE 		: " << (EEE_ppf+EEE_pfp+EEE_fpp)<<" / "<<EEE <<" = "<< 1.0*(EEE_ppf+EEE_pfp+EEE_fpp)/EEE << endl; 
	cout << "       EEM---------------------  " << endl;
	cout << "			EE PP / PPF		: "<< (EEM_ppf + EME_pfp + MEE_fpp) <<" / "<< eem_ppf <<" = "<< 1.0*(EEM_ppf + EME_pfp + MEE_fpp) / eem_ppf << endl; 
	cout << "			EM PP / PPF		: "<<  (EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp) <<" / "<< eem_ppf <<" = "<<1.0*(EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp) / eem_ppf << endl; 
	cout << "       EMM---------------------  " << endl;
	cout << "			EM PP / PPF 		: "	<< EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp << " / " << emm_ppf <<" = "<<1.0*(EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp) / emm_ppf << endl; 
	cout << " 			MM PP / PPF 		: "<< EMM_fpp+MEM_pfp+MME_ppf << " / " << emm_ppf <<" = "<< 1.0*(EMM_fpp+MEM_pfp+MME_ppf) / emm_ppf << endl; 
	cout << "       MMM---------------------  " << endl;
	cout << "			MMM PPF / MMM 		: " << (MMM_ppf+MMM_pfp+MMM_fpp)<<" / "<<MMM <<" = "<< 1.0*(MMM_ppf+MMM_pfp+MMM_fpp)/MMM << endl; 

	cout << "" << endl;
	cout << " ========= Some more RESULTs summary ========= " << endl;
	float totalEEPP = (EEE_ppf+EEE_pfp+EEE_fpp)+(EEM_ppf + EME_pfp + MEE_fpp) ;
	float totalEMPP = (EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp)+EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp;
	float totalMMPP = EMM_fpp+MEM_pfp+MME_ppf + (MMM_ppf+MMM_pfp+MMM_fpp);
	float totalEvents = (EEE_ppf+EEE_pfp+EEE_fpp)+(EEM_ppf + EME_pfp + MEE_fpp) + (EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp)+EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp + EMM_fpp+MEM_pfp+MME_ppf + (MMM_ppf+MMM_pfp+MMM_fpp);
	cout << "			EE PP		: " << (EEE_ppf+EEE_pfp+EEE_fpp)+(EEM_ppf + EME_pfp + MEE_fpp)<< " ( "<< totalEEPP / totalEvents *100. << " % )"<<endl; 
	cout << "			EM PP 		: "<<  (EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp)+EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp << " ( "<< totalEMPP / totalEvents *100.<< " % )"<< endl; 
	cout << " 			MM PP  		: "<< EMM_fpp+MEM_pfp+MME_ppf + (MMM_ppf+MMM_pfp+MMM_fpp)<< " ( "<< totalMMPP / totalEvents *100.<< " % )"<< endl; 

	gApplication->Terminate();
	
}
