
using namespace std;

void CountRates(){

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

	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";

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
// 	TString njet = " && (NJets_singleLepCalc ==1)";
// 	TString njet = " && (NJets_singleLepCalc ==2)";
// 	TString njet = " && (NJets_singleLepCalc > 2)";

// 	TString bjet = " && 1";
	TString bjet = " && (NJetsBTagwithSF_singleLepCalc >=1)";


// 	TString basic_cut = "1 "+trig+trilep+lepPt+exactly3Lep+njet+bjet;
// 	TString basic_cut = "1 "+trig+lepPt+exactly3Lep+njet+bjet;

	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_singleLepCalc >= 0) && (NJets_singleLepCalc >= 0) && (NJetsBTagwithSF_singleLepCalc >= 0) && DataPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";
// 	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_singleLepCalc >= 0) && (NJets_singleLepCalc >= 0) && (NJetsBTagwithSF_singleLepCalc >= 0) && MCPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";

	cout << "Counting with basic cuts: " << basic_cut << endl;	
	
	TString isTTT = " && isTTT"; 
	TString isTTL = " && isTTL"; 
	TString isTLT = " && isTLT"; 
	TString isLTT = " && isLTT"; 
	
	TString isEEE = " && isEEE";
	TString isEEM = " && isEEM";
	TString isEMM = " && isEMM";
	TString isMMM = " && isMMM"; 

	TString isEEM_ = " && isEEM_";
	TString isEME_ = " && isEME_";
	TString isMEE_ = " && isMEE_";
	TString isEMM_ = " && isEMM_";
	TString isMEM_ = " && isMEM_";
	TString isMME_ = " && isMME_";


	TString isPPP = " && ( ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==1 ) )";
	
	TString isPPF = " && ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isPFP = " && ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";
	TString isFPP = " && ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";

	TString isPFF = " && ( AllLeptonIsPrompt_PtOrdered[0]==1 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isFPF = " && ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==1 && AllLeptonIsPrompt_PtOrdered[2]==0 ) ";
	TString isFFP = " && ( AllLeptonIsPrompt_PtOrdered[0]==0 && AllLeptonIsPrompt_PtOrdered[1]==0 && AllLeptonIsPrompt_PtOrdered[2]==1 ) ";

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
	TString isFPP_isMatched = " && ( AllLeptonIsMatched_PtOrdered[0]==0 ) ";

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
	
	EEE_ttt = t->Draw(observ,basic_cut+isEEE+" &&  isTTT " );

	//1prompt
	EEE_pff = t->Draw(observ,basic_cut+isEEE+" &&  isPFF " );
	EEE_fpf = t->Draw(observ,basic_cut+isEEE+" &&  isFPF " );
	EEE_ffp = t->Draw(observ,basic_cut+isEEE+" &&  isFFP " );

	//2 prompts (1 fake)
	EEE_ppf = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )" );
	EEE_pfp = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )" );
	EEE_fpp = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )" );

		EEE_ppf_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isMatched );
		EEE_pfp_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isMatched );
		EEE_fpp_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isMatched );

		EEE_ppf_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isFromB );
		EEE_pfp_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isFromB );
		EEE_fpp_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isFromB );

		EEE_ppf_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isFromC );
		EEE_pfp_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isFromC );
		EEE_fpp_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isFromC );

		EEE_ppf_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isFromHL );
		EEE_pfp_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isFromHL );
		EEE_fpp_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isFromHL );

		EEE_ppf_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isFromPh );
		EEE_pfp_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isFromPh );
		EEE_fpp_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isFromPh );

		EEE_ppf_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )"+isPPF_isFromL );
		EEE_pfp_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )"+isPFP_isFromL );
		EEE_fpp_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )"+isFPP_isFromL );
	
	EEE_ppf_ttl = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)" );
	EEE_pfp_tlt = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)" );
	EEE_fpp_ltt = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)" );

	EEE_ppf_ttt = t->Draw(observ,basic_cut+isEEE+" && ( isPPF || isPFP || isFPP ) && isTTT " );

	//3 prompts , 3 fakes
	EEE_ppp = t->Draw(observ,basic_cut+isEEE+isPPP);
	EEE_fff = t->Draw(observ,basic_cut+isEEE+isFFF);

	//All
	EEE = t->Draw(observ,basic_cut+isEEE);

	EEE_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isMatched);
	EEE_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isMatched );
	EEE_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isMatched );

	EEE_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromB);
	EEE_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromB );
	EEE_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromB );

	EEE_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromC);
	EEE_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromC );
	EEE_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromC );

	EEE_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromHL);
	EEE_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromHL );
	EEE_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromHL );

	EEE_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromPh);
	EEE_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromPh );
	EEE_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromPh );

	EEE_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromL);
	EEE_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromL );
	EEE_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromL );

	//

	EEE_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isMatched);
	EEE_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isMatched );
	EEE_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isMatched );

	EEE_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromB);
	EEE_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromB );
	EEE_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromB );

	EEE_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromC);
	EEE_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromC );
	EEE_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromC );

	EEE_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromHL);
	EEE_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromHL );
	EEE_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromHL );

	EEE_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromPh);
	EEE_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromPh );
	EEE_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromPh );

	EEE_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromL);
	EEE_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromL );
	EEE_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromL );


	//
	cout << " ========= EEE ========= " << endl;
	cout << "Counts of EEE: FFF(" << EEE_fff<< "), PFF(" <<EEE_pff+EEE_fpf+EEE_ffp <<"), PPF("<< EEE_ppf+EEE_pfp+EEE_fpp<<"), PPP("<< EEE_ppp <<") : "<< EEE<<", TTT("<< EEE_ttt << ")"<<endl; 
	cout << "	--1 fake /2 prompts:   "<< endl;
	cout << "       IsTTT f(T) : " << EEE_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEE_ppf_ttt_isMatched+EEE_pfp_ttt_isMatched+EEE_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EEE_ppf_ttt_isFromB+EEE_pfp_ttt_isFromB+EEE_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EEE_ppf_ttt_isFromC+EEE_pfp_ttt_isFromC+EEE_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EEE_ppf_ttt_isFromHL+EEE_pfp_ttt_isFromHL+EEE_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEE_ppf_ttt_isFromPh+EEE_pfp_ttt_isFromPh+EEE_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EEE_ppf_ttt_isFromL+EEE_pfp_ttt_isFromL+EEE_fpp_ttt_isFromL << endl;
	}
	cout << "       IsTTL f(L) : " << EEE_ppf_ttl+EEE_pfp_tlt+EEE_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEE_ppf_ttl_isMatched+EEE_pfp_tlt_isMatched+EEE_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << EEE_ppf_ttl_isFromB+EEE_pfp_tlt_isFromB+EEE_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << EEE_ppf_ttl_isFromC+EEE_pfp_tlt_isFromC+EEE_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << EEE_ppf_ttl_isFromHL+EEE_pfp_tlt_isFromHL+EEE_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEE_ppf_ttl_isFromPh+EEE_pfp_tlt_isFromPh+EEE_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << EEE_ppf_ttl_isFromL+EEE_pfp_tlt_isFromL+EEE_fpp_ltt_isFromL << endl;
	}
	float eee_fT = EEE_ppf_ttt*1.0;
	float eee_fL = (EEE_ppf_ttl+EEE_pfp_tlt+EEE_fpp_ltt )*1.0;
	float eee_FR = eee_fT / ( eee_fT  + eee_fL ) ;
	cout << "       		el fake rate  : " << eee_FR << endl;
// if(PrintMixedChannels){
	//===========EEM==============

	EEM_ttt = t->Draw(observ,basic_cut+isEEM_+isTTT);
	EME_ttt = t->Draw(observ,basic_cut+isEME_+isTTT);
	MEE_ttt = t->Draw(observ,basic_cut+isMEE_+isTTT);

	//1prompt
	EEM_pff = t->Draw(observ,basic_cut+isEEM_+isPFF);
	EEM_fpf = t->Draw(observ,basic_cut+isEEM_+isFPF);
	EEM_ffp = t->Draw(observ,basic_cut+isEEM_+isFFP);

	EME_pff = t->Draw(observ,basic_cut+isEME_+isPFF);
	EME_fpf = t->Draw(observ,basic_cut+isEME_+isFPF);
	EME_ffp = t->Draw(observ,basic_cut+isEME_+isFFP);

	MEE_pff = t->Draw(observ,basic_cut+isMEE_+isPFF);
	MEE_fpf = t->Draw(observ,basic_cut+isMEE_+isFPF);
	MEE_ffp = t->Draw(observ,basic_cut+isMEE_+isFFP);

	//EEM - 2prompts
	EEM_ppf = t->Draw(observ,basic_cut+isEEM_+isPPF);
	EEM_pfp = t->Draw(observ,basic_cut+isEEM_+isPFP);
	EEM_fpp = t->Draw(observ,basic_cut+isEEM_+isFPP);

		EEM_ppf_isMatched = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isMatched);
		EEM_pfp_isMatched = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isMatched);
		EEM_fpp_isMatched = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isMatched);

		EEM_ppf_isFromB = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isFromB);
		EEM_pfp_isFromB = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isFromB);
		EEM_fpp_isFromB = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isFromB);

		EEM_ppf_isFromC = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isFromC);
		EEM_pfp_isFromC = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isFromC);
		EEM_fpp_isFromC = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isFromC);

		EEM_ppf_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isFromHL);
		EEM_pfp_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isFromHL);
		EEM_fpp_isFromHL = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isFromHL);

		EEM_ppf_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isFromPh);
		EEM_pfp_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isFromPh);
		EEM_fpp_isFromPh = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isFromPh);

		EEM_ppf_isFromL = t->Draw(observ,basic_cut+isEEM_+isPPF+isPPF_isFromL);
		EEM_pfp_isFromL = t->Draw(observ,basic_cut+isEEM_+isPFP+isPFP_isFromL);
		EEM_fpp_isFromL = t->Draw(observ,basic_cut+isEEM_+isFPP+isFPP_isFromL);

	EEM_ppf_ttl = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL);
	EEM_pfp_tlt = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT);
	EEM_fpp_ltt = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT);

	EEM_ppf_ttt = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT);
	EEM_pfp_ttt = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT);
	EEM_fpp_ttt = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT);

		//sources - isMatched
		EEM_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isMatched);
		EEM_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isMatched);
		EEM_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isMatched);

		EEM_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isMatched);
		EEM_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isMatched);
		EEM_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isMatched);

		//sources - isFromB
		EEM_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromB);
		EEM_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromB);
		EEM_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromB);

		EEM_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromB);
		EEM_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromB);
		EEM_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromB);

		//sources - isFromB
		EEM_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromB);
		EEM_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromB);
		EEM_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromB);

		EEM_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromB);
		EEM_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromB);
		EEM_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromB);

		//sources - isFromC
		EEM_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromC);
		EEM_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromC);
		EEM_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromC);

		EEM_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromC);
		EEM_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromC);
		EEM_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromC);

		//sources - isFromHL
		EEM_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromHL);
		EEM_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromHL);
		EEM_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromHL);

		EEM_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromHL);
		EEM_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromHL);
		EEM_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromHL);

		//sources - isFromPh
		EEM_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromPh);
		EEM_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromPh);
		EEM_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromPh);

		EEM_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromPh);
		EEM_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromPh);
		EEM_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromPh);

		//sources - isFromL
		EEM_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL+isPPF_isFromL);
		EEM_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT+isPFP_isFromL);
		EEM_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT+isFPP_isFromL);

		EEM_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT+isPPF_isFromL);
		EEM_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT+isPFP_isFromL);
		EEM_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT+isFPP_isFromL);

	//EME - 2prompts
	EME_ppf = t->Draw(observ,basic_cut+isEME_+isPPF);
	EME_pfp = t->Draw(observ,basic_cut+isEME_+isPFP);
	EME_fpp = t->Draw(observ,basic_cut+isEME_+isFPP);

		EME_ppf_isMatched = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isMatched);
		EME_pfp_isMatched = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isMatched);
		EME_fpp_isMatched = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isMatched);

		EME_ppf_isFromB = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isFromB);
		EME_pfp_isFromB = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isFromB);
		EME_fpp_isFromB = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isFromB);

		EME_ppf_isFromC = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isFromC);
		EME_pfp_isFromC = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isFromC);
		EME_fpp_isFromC = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isFromC);

		EME_ppf_isFromHL = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isFromHL);
		EME_pfp_isFromHL = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isFromHL);
		EME_fpp_isFromHL = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isFromHL);

		EME_ppf_isFromPh = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isFromPh);
		EME_pfp_isFromPh = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isFromPh);
		EME_fpp_isFromPh = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isFromPh);

		EME_ppf_isFromL = t->Draw(observ,basic_cut+isEME_+isPPF+isPPF_isFromL);
		EME_pfp_isFromL = t->Draw(observ,basic_cut+isEME_+isPFP+isPFP_isFromL);
		EME_fpp_isFromL = t->Draw(observ,basic_cut+isEME_+isFPP+isFPP_isFromL);

	EME_ppf_ttl = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL);
	EME_pfp_tlt = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT);
	EME_fpp_ltt = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT);

	EME_ppf_ttt = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT);
	EME_pfp_ttt = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT);
	EME_fpp_ttt = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT);

		//sources - isMatched
		EME_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isMatched);
		EME_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isMatched);
		EME_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isMatched);

		EME_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isMatched);
		EME_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isMatched);
		EME_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isMatched);

		//sources - isFromB
		EME_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isFromB);
		EME_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isFromB);
		EME_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isFromB);

		EME_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isFromB);
		EME_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isFromB);
		EME_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isFromB);

		//sources - isFromC
		EME_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isFromC);
		EME_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isFromC);
		EME_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isFromC);

		EME_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isFromC);
		EME_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isFromC);
		EME_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isFromC);

		//sources - isFromHL
		EME_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isFromHL);
		EME_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isFromHL);
		EME_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isFromHL);

		EME_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isFromHL);
		EME_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isFromHL);
		EME_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isFromHL);

		//sources - isFromPh
		EME_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isFromPh);
		EME_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isFromPh);
		EME_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isFromPh);

		EME_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isFromPh);
		EME_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isFromPh);
		EME_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isFromPh);

		//sources - isFromL
		EME_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL+isPPF_isFromL);
		EME_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT+isPFP_isFromL);
		EME_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT+isFPP_isFromL);

		EME_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT+isPPF_isFromL);
		EME_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT+isPFP_isFromL);
		EME_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT+isFPP_isFromL);


	//MEE - 2prompts
	MEE_ppf = t->Draw(observ,basic_cut+isMEE_+isPPF);
	MEE_pfp = t->Draw(observ,basic_cut+isMEE_+isPFP);
	MEE_fpp = t->Draw(observ,basic_cut+isMEE_+isFPP);

		MEE_ppf_isMatched = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isMatched);
		MEE_pfp_isMatched = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isMatched);
		MEE_fpp_isMatched = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isMatched);

		MEE_ppf_isFromB = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isFromB);
		MEE_pfp_isFromB = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isFromB);
		MEE_fpp_isFromB = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isFromB);

		MEE_ppf_isFromC = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isFromC);
		MEE_pfp_isFromC = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isFromC);
		MEE_fpp_isFromC = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isFromC);

		MEE_ppf_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isFromHL);
		MEE_pfp_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isFromHL);
		MEE_fpp_isFromHL = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isFromHL);

		MEE_ppf_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isFromPh);
		MEE_pfp_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isFromPh);
		MEE_fpp_isFromPh = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isFromPh);

		MEE_ppf_isFromL = t->Draw(observ,basic_cut+isMEE_+isPPF+isPPF_isFromL);
		MEE_pfp_isFromL = t->Draw(observ,basic_cut+isMEE_+isPFP+isPFP_isFromL);
		MEE_fpp_isFromL = t->Draw(observ,basic_cut+isMEE_+isFPP+isFPP_isFromL);

	MEE_ppf_ttl = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL);
	MEE_pfp_tlt = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT);
	MEE_fpp_ltt = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT);

	MEE_ppf_ttt = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT);
	MEE_pfp_ttt = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT);
	MEE_fpp_ttt = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT);

		//source isMatched		
		MEE_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isMatched);
		MEE_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isMatched);
		MEE_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isMatched);

		MEE_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isMatched);
		MEE_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isMatched);
		MEE_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isMatched);

		//source isFromB		
		MEE_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isFromB);
		MEE_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isFromB);
		MEE_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isFromB);

		MEE_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isFromB);
		MEE_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isFromB);
		MEE_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isFromB);

		//source isFromC		
		MEE_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isFromC);
		MEE_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isFromC);
		MEE_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isFromC);

		MEE_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isFromC);
		MEE_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isFromC);
		MEE_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isFromC);

		//source isFromHL		
		MEE_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isFromHL);
		MEE_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isFromHL);
		MEE_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isFromHL);

		MEE_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isFromHL);
		MEE_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isFromHL);
		MEE_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isFromHL);

		//source isFromPh		
		MEE_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isFromPh);
		MEE_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isFromPh);
		MEE_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isFromPh);

		MEE_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isFromPh);
		MEE_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isFromPh);
		MEE_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isFromPh);

		//source isFromL		
		MEE_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL+isPPF_isFromL);
		MEE_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT+isPFP_isFromL);
		MEE_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT+isFPP_isFromL);

		MEE_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT+isPPF_isFromL);
		MEE_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT+isPFP_isFromL);
		MEE_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT+isFPP_isFromL);

		
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
	cout << "               Is(not)Matched   : " << EEM_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EEM_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EEM_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_ppf_ttt_isFromL<< endl;
	}
	cout << "       E(E)M PFP TTT (fake el) : " << EEM_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEM_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EEM_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EEM_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_pfp_ttt_isFromL<< endl;
	}
	cout << "       (E)EM FPP TTT (fake el) : " << EEM_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEM_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EEM_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EEM_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_fpp_ttt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       EM(E) PPF TTT (fake el) : " << EME_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EME_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EME_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EME_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EME_ppf_ttt_isFromL<< endl;
	}
	cout << "       E(M)E PFP TTT (fake mu) : " << EME_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EME_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EME_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EME_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EME_pfp_ttt_isFromL<< endl;
	}
	cout << "       (E)ME FPP TTT (fake el) : " << EME_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EME_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EME_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EME_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EME_fpp_ttt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       ME(E) PPF TTT (fake el) : " << MEE_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEE_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEE_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_ppf_ttt_isFromL<< endl;
	}
	cout << "       M(E)E PFP TTT (fake el) : " << MEE_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEE_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEE_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_pfp_ttt_isFromL<< endl;
	}
	cout << "       (M)EE FPP TTT (fake mu) : " << MEE_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEE_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEE_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_fpp_ttt_isFromL<< endl;
	}
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EE(M) PPF TTL (fake mu) : " << EEM_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEM_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << EEM_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << EEM_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_ppf_ttl_isFromL<< endl;
	}
	cout << "       E(E)M PFP TLT (fake el) : " << EEM_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEM_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << EEM_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << EEM_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_pfp_tlt_isFromL<< endl;
	}
	cout << "       (E)EM FPP LTT (fake el) : " << EEM_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEM_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << EEM_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << EEM_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << EEM_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << EEM_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << EEM_fpp_ltt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       EM(E) PPF TTL (fake el) : " << EME_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << EME_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << EME_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << EME_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << EME_ppf_ttl_isFromL<< endl;
	}
	cout << "       E(M)E PFP TLT (fake mu) : " << EME_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << EME_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << EME_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << EME_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << EME_pfp_tlt_isFromL<< endl;
	}
	cout << "       (E)ME FPP LTT (fake el) : " << EME_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EME_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << EME_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << EME_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << EME_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << EME_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << EME_fpp_ltt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       ME(E) PPF TTL (fake el) : " << MEE_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << MEE_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << MEE_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_ppf_ttl_isFromL<< endl;
	}
	cout << "       M(E)E PFP TLT (fake el) : " << MEE_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << MEE_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << MEE_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_pfp_tlt_isFromL<< endl;
	}
	cout << "       (M)EE FPP LTT (fake mu) : " << MEE_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEE_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << MEE_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << MEE_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << MEE_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEE_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << MEE_fpp_ltt_isFromL<< endl;
	}
	cout << "       ---------------------  " << endl;
// 	cout << "			EE PP f(T): "<< EEM_ppf_ttt + EME_pfp_ttt + MEE_fpp_ttt<< endl;
// 	cout << "			EE PP f(L): "<< EEM_ppf_ttl + EME_pfp_tlt + MEE_fpp_ltt<< endl;
// 	cout << "			EM PP f(T): "<< EEM_pfp_ttt + EEM_fpp_ttt + EME_ppf_ttt + EME_fpp_ttt + MEE_ppf_ttt + MEE_pfp_ttt<< endl;
// 	cout << "			EM PP f(L): "<< EEM_pfp_tlt + EEM_fpp_ltt + EME_ppf_ttl + EME_fpp_ltt + MEE_ppf_ttl + MEE_pfp_tlt<< endl;
	cout << "       ---------------------  " << endl;
	float eem_e_fT = EEM_pfp_ttt+EEM_fpp_ttt+EME_ppf_ttt+EME_fpp_ttt+MEE_ppf_ttt+MEE_pfp_ttt;

		float eem_e_fT_isMatched = EEM_pfp_ttt_isMatched+EEM_fpp_ttt_isMatched+EME_ppf_ttt_isMatched+EME_fpp_ttt_isMatched+MEE_ppf_ttt_isMatched+MEE_pfp_ttt_isMatched;
		float eem_e_fT_isFromB = EEM_pfp_ttt_isFromB+EEM_fpp_ttt_isFromB+EME_ppf_ttt_isFromB+EME_fpp_ttt_isFromB+MEE_ppf_ttt_isFromB+MEE_pfp_ttt_isFromB;
		float eem_e_fT_isFromC = EEM_pfp_ttt_isFromC+EEM_fpp_ttt_isFromC+EME_ppf_ttt_isFromC+EME_fpp_ttt_isFromC+MEE_ppf_ttt_isFromC+MEE_pfp_ttt_isFromC;
		float eem_e_fT_isFromHL = EEM_pfp_ttt_isFromHL+EEM_fpp_ttt_isFromHL+EME_ppf_ttt_isFromHL+EME_fpp_ttt_isFromHL+MEE_ppf_ttt_isFromHL+MEE_pfp_ttt_isFromHL;
		float eem_e_fT_isFromPh = EEM_pfp_ttt_isFromPh+EEM_fpp_ttt_isFromPh+EME_ppf_ttt_isFromPh+EME_fpp_ttt_isFromPh+MEE_ppf_ttt_isFromPh+MEE_pfp_ttt_isFromPh;
		float eem_e_fT_isFromL = EEM_pfp_ttt_isFromL+EEM_fpp_ttt_isFromL+EME_ppf_ttt_isFromL+EME_fpp_ttt_isFromL+MEE_ppf_ttt_isFromL+MEE_pfp_ttt_isFromL;

	float eem_e_fL = EEM_pfp_tlt+EEM_fpp_ltt+EME_ppf_ttl+EME_fpp_ltt+MEE_ppf_ttl+MEE_pfp_tlt;

		float eem_e_fL_isMatched = EEM_pfp_tlt_isMatched+EEM_fpp_ltt_isMatched+EME_ppf_ttl_isMatched+EME_fpp_ltt_isMatched+MEE_ppf_ttl_isMatched+MEE_pfp_tlt_isMatched;
		float eem_e_fL_isFromB = EEM_pfp_tlt_isFromB+EEM_fpp_ltt_isFromB+EME_ppf_ttl_isFromB+EME_fpp_ltt_isFromB+MEE_ppf_ttl_isFromB+MEE_pfp_tlt_isFromB;
		float eem_e_fL_isFromC = EEM_pfp_tlt_isFromC+EEM_fpp_ltt_isFromC+EME_ppf_ttl_isFromC+EME_fpp_ltt_isFromC+MEE_ppf_ttl_isFromC+MEE_pfp_tlt_isFromC;
		float eem_e_fL_isFromHL = EEM_pfp_tlt_isFromHL+EEM_fpp_ltt_isFromHL+EME_ppf_ttl_isFromHL+EME_fpp_ltt_isFromHL+MEE_ppf_ttl_isFromHL+MEE_pfp_tlt_isFromHL;
		float eem_e_fL_isFromPh = EEM_pfp_tlt_isFromPh+EEM_fpp_ltt_isFromPh+EME_ppf_ttl_isFromPh+EME_fpp_ltt_isFromPh+MEE_ppf_ttl_isFromPh+MEE_pfp_tlt_isFromPh;
		float eem_e_fL_isFromL = EEM_pfp_tlt_isFromL+EEM_fpp_ltt_isFromL+EME_ppf_ttl_isFromL+EME_fpp_ltt_isFromL+MEE_ppf_ttl_isFromL+MEE_pfp_tlt_isFromL;


	float eem_e_FR = eem_e_fT / ( eem_e_fT + eem_e_fL );
	cout << "       fake el f(T)          : " << eem_e_fT << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << eem_e_fT_isMatched << endl;
	cout << "               IsFromB          : " << eem_e_fT_isFromB << endl;
	cout << "               IsFromC          : " << eem_e_fT_isFromC << endl;
	cout << "               IsFromHL         : " << eem_e_fT_isFromHL << endl;
	cout << "               IsFromPh         : " << eem_e_fT_isFromPh << endl;
	cout << "               IsFromL          : " << eem_e_fT_isFromL << endl;
	}
	cout << "       fake el f(L)          : " << eem_e_fL << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << eem_e_fL_isMatched << endl;
	cout << "               IsFromB          : " << eem_e_fL_isFromB << endl;
	cout << "               IsFromC          : " << eem_e_fL_isFromC << endl;
	cout << "               IsFromHL         : " << eem_e_fL_isFromHL << endl;
	cout << "               IsFromPh         : " << eem_e_fL_isFromPh << endl;
	cout << "               IsFromL          : " << eem_e_fL_isFromL << endl;
	}
	cout << "       		el fake rate  : " << eem_e_fT / ( eem_e_fT + eem_e_fL ) << endl;

	float eem_m_fT = EEM_ppf_ttt+EME_pfp_ttt+MEE_fpp_ttt;

		float eem_m_fT_isMatched = EEM_ppf_ttt_isMatched+EME_pfp_ttt_isMatched+MEE_fpp_ttt_isMatched;
		float eem_m_fT_isFromB = EEM_ppf_ttt_isFromB+EME_pfp_ttt_isFromB+MEE_fpp_ttt_isFromB;
		float eem_m_fT_isFromC = EEM_ppf_ttt_isFromC+EME_pfp_ttt_isFromC+MEE_fpp_ttt_isFromC;
		float eem_m_fT_isFromHL = EEM_ppf_ttt_isFromHL+EME_pfp_ttt_isFromHL+MEE_fpp_ttt_isFromHL;
		float eem_m_fT_isFromPh = EEM_ppf_ttt_isFromPh+EME_pfp_ttt_isFromPh+MEE_fpp_ttt_isFromPh;
		float eem_m_fT_isFromL = EEM_ppf_ttt_isFromL+EME_pfp_ttt_isFromL+MEE_fpp_ttt_isFromL;

	float eem_m_fL = EEM_ppf_ttl+EME_pfp_tlt+MEE_fpp_ltt;

		float eem_m_fL_isMatched = EEM_ppf_ttl_isMatched+EME_pfp_tlt_isMatched+MEE_fpp_ltt_isMatched;
		float eem_m_fL_isFromB = EEM_ppf_ttl_isFromB+EME_pfp_tlt_isFromB+MEE_fpp_ltt_isFromB;
		float eem_m_fL_isFromC = EEM_ppf_ttl_isFromC+EME_pfp_tlt_isFromC+MEE_fpp_ltt_isFromC;
		float eem_m_fL_isFromHL = EEM_ppf_ttl_isFromHL+EME_pfp_tlt_isFromHL+MEE_fpp_ltt_isFromHL;
		float eem_m_fL_isFromPh = EEM_ppf_ttl_isFromPh+EME_pfp_tlt_isFromPh+MEE_fpp_ltt_isFromPh;
		float eem_m_fL_isFromL = EEM_ppf_ttl_isFromL+EME_pfp_tlt_isFromL+MEE_fpp_ltt_isFromL;

	float eem_m_FR = eem_m_fT / ( eem_m_fT + eem_m_fL );
	cout << "       fake mu f(T)          : " << eem_m_fT<<endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << eem_m_fT_isMatched << endl;
	cout << "               IsFromB          : " << eem_m_fT_isFromB << endl;
	cout << "               IsFromC          : " << eem_m_fT_isFromC << endl;
	cout << "               IsFromHL         : " << eem_m_fT_isFromHL << endl;
	cout << "               IsFromPh         : " << eem_m_fT_isFromPh << endl;
	cout << "               IsFromL          : " << eem_m_fT_isFromL << endl;
	}
	cout << "       fake mu f(L)          : " << eem_m_fL<<endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << eem_m_fL_isMatched << endl;
	cout << "               IsFromB          : " << eem_m_fL_isFromB << endl;
	cout << "               IsFromC          : " << eem_m_fL_isFromC << endl;
	cout << "               IsFromHL         : " << eem_m_fL_isFromHL << endl;
	cout << "               IsFromPh         : " << eem_m_fL_isFromPh << endl;
	cout << "               IsFromL          : " << eem_m_fL_isFromL << endl;
	}
	cout << "       		mu fake rate  : " << eem_m_fT / ( eem_m_fT + eem_m_fL ) << endl;
	//===========EMM==============
	
	EMM_ttt = t->Draw(observ,basic_cut+isEMM_+isTTT);
	MEM_ttt = t->Draw(observ,basic_cut+isMEM_+isTTT);
	MME_ttt = t->Draw(observ,basic_cut+isMME_+isTTT);

	//1 fake / 2 prompts
	EMM_ppf = t->Draw(observ,basic_cut+isEMM_+isPPF);
	EMM_pfp = t->Draw(observ,basic_cut+isEMM_+isPFP);
	EMM_fpp = t->Draw(observ,basic_cut+isEMM_+isFPP);

		EMM_ppf_isMatched = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isMatched);
		EMM_pfp_isMatched = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isMatched);
		EMM_fpp_isMatched = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isMatched);

		EMM_ppf_isFromB = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isFromB);
		EMM_pfp_isFromB = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isFromB);
		EMM_fpp_isFromB = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isFromB);

		EMM_ppf_isFromC = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isFromC);
		EMM_pfp_isFromC = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isFromC);
		EMM_fpp_isFromC = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isFromC);

		EMM_ppf_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isFromHL);
		EMM_pfp_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isFromHL);
		EMM_fpp_isFromHL = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isFromHL);

		EMM_ppf_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isFromPh);
		EMM_pfp_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isFromPh);
		EMM_fpp_isFromPh = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isFromPh);

		EMM_ppf_isFromL = t->Draw(observ,basic_cut+isEMM_+isPPF+isPPF_isFromL);
		EMM_pfp_isFromL = t->Draw(observ,basic_cut+isEMM_+isPFP+isPFP_isFromL);
		EMM_fpp_isFromL = t->Draw(observ,basic_cut+isEMM_+isFPP+isFPP_isFromL);

	EMM_ppf_ttt = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT);
	EMM_pfp_ttt = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT);
	EMM_fpp_ttt = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT);

	EMM_ppf_ttl = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL);
	EMM_pfp_tlt = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT);
	EMM_fpp_ltt = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT);

		//sources - isMatched
		EMM_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isMatched);
		EMM_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isMatched);
		EMM_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isMatched);

		EMM_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isMatched);
		EMM_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isMatched);
		EMM_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isMatched);

		//sources - isFromB
		EMM_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isFromB);
		EMM_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isFromB);
		EMM_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isFromB);

		EMM_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isFromB);
		EMM_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isFromB);
		EMM_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isFromB);

		//sources - isFromC
		EMM_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isFromC);
		EMM_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isFromC);
		EMM_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isFromC);

		EMM_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isFromC);
		EMM_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isFromC);
		EMM_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isFromC);

		//sources - isFromHL
		EMM_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isFromHL);
		EMM_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isFromHL);
		EMM_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isFromHL);

		EMM_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isFromHL);
		EMM_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isFromHL);
		EMM_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isFromHL);

		//sources - isFromPh
		EMM_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isFromPh);
		EMM_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isFromPh);
		EMM_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isFromPh);

		EMM_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isFromPh);
		EMM_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isFromPh);
		EMM_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isFromPh);

		//sources - isFromL
		EMM_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT+isPPF_isFromL);
		EMM_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT+isPFP_isFromL);
		EMM_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT+isFPP_isFromL);

		EMM_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL+isPPF_isFromL);
		EMM_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT+isPFP_isFromL);
		EMM_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT+isFPP_isFromL);

	MEM_ppf = t->Draw(observ,basic_cut+isMEM_+isPPF);
	MEM_pfp = t->Draw(observ,basic_cut+isMEM_+isPFP);
	MEM_fpp = t->Draw(observ,basic_cut+isMEM_+isFPP);

	MEM_ppf_ttt = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT);
	MEM_pfp_ttt = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT);
	MEM_fpp_ttt = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT);

	MEM_ppf_ttl = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL);
	MEM_pfp_tlt = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT);
	MEM_fpp_ltt = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT);

		//source - isMatched
		MEM_ppf_isMatched = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isMatched);
		MEM_pfp_isMatched = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isMatched);
		MEM_fpp_isMatched = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isMatched);

		MEM_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isMatched);
		MEM_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isMatched);
		MEM_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isMatched);

		MEM_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isMatched);
		MEM_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isMatched);
		MEM_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isMatched);

		//source - isFromB
		MEM_ppf_isFromB = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isFromB);
		MEM_pfp_isFromB = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isFromB);
		MEM_fpp_isFromB = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isFromB);

		MEM_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isFromB);
		MEM_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isFromB);
		MEM_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isFromB);

		MEM_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isFromB);
		MEM_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isFromB);
		MEM_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isFromB);

		//source - isFromC
		MEM_ppf_isFromC = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isFromC);
		MEM_pfp_isFromC = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isFromC);
		MEM_fpp_isFromC = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isFromC);

		MEM_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isFromC);
		MEM_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isFromC);
		MEM_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isFromC);

		MEM_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isFromC);
		MEM_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isFromC);
		MEM_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isFromC);

		//source - isFromHL
		MEM_ppf_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isFromHL);
		MEM_pfp_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isFromHL);
		MEM_fpp_isFromHL = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isFromHL);

		MEM_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isFromHL);
		MEM_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isFromHL);
		MEM_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isFromHL);

		MEM_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isFromHL);
		MEM_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isFromHL);
		MEM_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isFromHL);

		//source - isFromPh
		MEM_ppf_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isFromPh);
		MEM_pfp_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isFromPh);
		MEM_fpp_isFromPh = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isFromPh);

		MEM_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isFromPh);
		MEM_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isFromPh);
		MEM_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isFromPh);

		MEM_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isFromPh);
		MEM_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isFromPh);
		MEM_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isFromPh);

		//source - isFromL
		MEM_ppf_isFromL = t->Draw(observ,basic_cut+isMEM_+isPPF+isPPF_isFromL);
		MEM_pfp_isFromL = t->Draw(observ,basic_cut+isMEM_+isPFP+isPFP_isFromL);
		MEM_fpp_isFromL = t->Draw(observ,basic_cut+isMEM_+isFPP+isFPP_isFromL);

		MEM_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT+isPPF_isFromL);
		MEM_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT+isPFP_isFromL);
		MEM_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT+isFPP_isFromL);

		MEM_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL+isPPF_isFromL);
		MEM_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT+isPFP_isFromL);
		MEM_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT+isFPP_isFromL);

	MME_ppf = t->Draw(observ,basic_cut+isMME_+isPPF);
	MME_pfp = t->Draw(observ,basic_cut+isMME_+isPFP);
	MME_fpp = t->Draw(observ,basic_cut+isMME_+isFPP);

		MME_ppf_isMatched = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isMatched);
		MME_pfp_isMatched = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isMatched);
		MME_fpp_isMatched = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isMatched);

		MME_ppf_isFromB = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isFromB);
		MME_pfp_isFromB = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isFromB);
		MME_fpp_isFromB = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isFromB);

		MME_ppf_isFromC = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isFromC);
		MME_pfp_isFromC = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isFromC);
		MME_fpp_isFromC = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isFromC);

		MME_ppf_isFromHL = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isFromHL);
		MME_pfp_isFromHL = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isFromHL);
		MME_fpp_isFromHL = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isFromHL);

		MME_ppf_isFromPh = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isFromPh);
		MME_pfp_isFromPh = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isFromPh);
		MME_fpp_isFromPh = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isFromPh);

		MME_ppf_isFromL = t->Draw(observ,basic_cut+isMME_+isPPF+isPPF_isFromL);
		MME_pfp_isFromL = t->Draw(observ,basic_cut+isMME_+isPFP+isPFP_isFromL);
		MME_fpp_isFromL = t->Draw(observ,basic_cut+isMME_+isFPP+isFPP_isFromL);

	MME_ppf_ttt = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT);
	MME_pfp_ttt = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT);
	MME_fpp_ttt = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT);

	MME_ppf_ttl = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL);
	MME_pfp_tlt = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT);
	MME_fpp_ltt = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT);

		//sources - isMatched
		MME_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isMatched);
		MME_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isMatched);
		MME_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isMatched);

		MME_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isMatched);
		MME_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isMatched);
		MME_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isMatched);

		//sources - isFromB
		MME_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isFromB);
		MME_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isFromB);
		MME_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isFromB);

		MME_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isFromB);
		MME_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isFromB);
		MME_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isFromB);

		//sources - isFromC
		MME_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isFromC);
		MME_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isFromC);
		MME_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isFromC);

		MME_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isFromC);
		MME_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isFromC);
		MME_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isFromC);

		//sources - isFromHL
		MME_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isFromHL);
		MME_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isFromHL);
		MME_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isFromHL);

		MME_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isFromHL);
		MME_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isFromHL);
		MME_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isFromHL);

		//sources - isFromPh
		MME_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isFromPh);
		MME_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isFromPh);
		MME_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isFromPh);

		MME_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isFromPh);
		MME_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isFromPh);
		MME_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isFromPh);

		//sources - isFromL
		MME_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT+isPPF_isFromL);
		MME_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT+isPFP_isFromL);
		MME_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT+isFPP_isFromL);

		MME_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL+isPPF_isFromL);
		MME_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT+isPFP_isFromL);
		MME_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT+isFPP_isFromL);


	//2fakes / 1 prompt
	
	EMM_pff = t->Draw(observ,basic_cut+isEMM_+isPFF);
	EMM_fpf = t->Draw(observ,basic_cut+isEMM_+isFPF);
	EMM_ffp = t->Draw(observ,basic_cut+isEMM_+isFFP);

	MEM_pff = t->Draw(observ,basic_cut+isMEM_+isPFF);
	MEM_fpf = t->Draw(observ,basic_cut+isMEM_+isFPF);
	MEM_ffp = t->Draw(observ,basic_cut+isMEM_+isFFP);

	MME_pff = t->Draw(observ,basic_cut+isMME_+isPFF);
	MME_fpf = t->Draw(observ,basic_cut+isMME_+isFPF);
	MME_ffp = t->Draw(observ,basic_cut+isMME_+isFFP);
	

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
	cout << "               Is(not)Matched   : " << EMM_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EMM_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EMM_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_ppf_ttt_isFromL<< endl;
	}
	cout << "       E(M)M PFP TTT (fake mu) : " << EMM_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EMM_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EMM_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EMM_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_pfp_ttt_isFromL<< endl;
	}
	cout << "       (E)MM FPP TTT (fake el) : " << EMM_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EMM_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EMM_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << EMM_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_fpp_ttt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       ME(M) PPF TTT (fake mu) : " << MEM_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEM_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEM_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_ppf_ttt_isFromL<< endl;
	}
	cout << "       M(E)M PFP TTT (fake el) : " << MEM_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEM_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEM_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_pfp_ttt_isFromL<< endl;
	}
	cout << "       (M)EM FPP TTT (fake mu) : " << MEM_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MEM_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MEM_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_fpp_ttt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       MM(E) PPF TTT (fake el) : " << MME_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_ppf_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MME_ppf_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MME_ppf_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MME_ppf_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_ppf_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MME_ppf_ttt_isFromL<< endl;
	}
	cout << "       M(M)E PFP TTT (fake mu) : " << MME_pfp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_pfp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MME_pfp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MME_pfp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MME_pfp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_pfp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MME_pfp_ttt_isFromL<< endl;
	}
	cout << "       (M)ME FPP TTT (fake mu) : " << MME_fpp_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MME_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MME_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MME_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MME_fpp_ttt_isFromL<< endl;
	}
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EM(M) PPF TTL (fake mu) : " << EMM_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EMM_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << EMM_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << EMM_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_ppf_ttl_isFromL<< endl;
	}
	cout << "       E(M)M PFP TLT (fake mu) : " << EMM_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EMM_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << EMM_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << EMM_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_pfp_tlt_isFromL<< endl;
	}
	cout << "       (E)MM FPP LTT (fake el) : " << EMM_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EMM_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << EMM_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << EMM_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << EMM_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << EMM_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << EMM_fpp_ltt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       ME(M) PPF TTL (fake mu) : " << MEM_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << MEM_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << MEM_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_ppf_ttl_isFromL<< endl;
	}
	cout << "       M(E)M PFP TLT (fake el) : " << MEM_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << MEM_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << MEM_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_pfp_tlt_isFromL<< endl;
	}
	cout << "       (M)EM FPP LTT (fake mu) : " << MEM_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MEM_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << MEM_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << MEM_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << MEM_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << MEM_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << MEM_fpp_ltt_isFromL<< endl;
	}
	cout << "-" << endl;
	cout << "       MM(E) PPF TTL (fake el) : " << MME_ppf_ttl << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_ppf_ttl_isMatched << endl;
	cout << "               IsFromB          : " << MME_ppf_ttl_isFromB << endl;
	cout << "               IsFromC          : " << MME_ppf_ttl_isFromC << endl;
	cout << "               IsFromHL         : " << MME_ppf_ttl_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_ppf_ttl_isFromPh << endl;
	cout << "               IsFromL          : " << MME_ppf_ttl_isFromL<< endl;
	}
	cout << "       M(M)E PFP TLT (fake mu) : " << MME_pfp_tlt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_pfp_tlt_isMatched << endl;
	cout << "               IsFromB          : " << MME_pfp_tlt_isFromB << endl;
	cout << "               IsFromC          : " << MME_pfp_tlt_isFromC << endl;
	cout << "               IsFromHL         : " << MME_pfp_tlt_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_pfp_tlt_isFromPh << endl;
	cout << "               IsFromL          : " << MME_pfp_tlt_isFromL<< endl;
	}
	cout << "       (M)ME FPP LTT (fake mu) : " << MME_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MME_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << MME_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << MME_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << MME_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << MME_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << MME_fpp_ltt_isFromL<< endl;
	}
	cout << "       ---------------------  " << endl;
// 	cout << "       	EM PP f(T): "<< EMM_ppf_ttt+EMM_pfp_ttt+MEM_ppf_ttt+MEM_fpp_ttt+MME_pfp_ttt+MME_fpp_ttt<< endl;
// 	cout << "			EM PP f(L): "<< EMM_ppf_ttl+EMM_pfp_tlt+MEM_ppf_ttl+MEM_fpp_ltt+MME_pfp_tlt+MME_fpp_ltt<< endl;
// 	cout << "			MM PP f(T): "<< EMM_fpp_ttt+MEM_pfp_ttt+MME_ppf_ttt<< endl;
// 	cout << " 			MM PP f(L): "<< EMM_pfp_tlt+MEM_pfp_tlt+MME_ppf_ttl<< endl;

	float emm_e_fT = EMM_fpp_ttt+MEM_pfp_ttt+MME_ppf_ttt;

		float emm_e_fT_isMatched = EMM_fpp_ttt_isMatched+MEM_pfp_ttt_isMatched+MME_ppf_ttt_isMatched;
		float emm_e_fT_isFromB = EMM_fpp_ttt_isFromB+MEM_pfp_ttt_isFromB+MME_ppf_ttt_isFromB;
		float emm_e_fT_isFromC = EMM_fpp_ttt_isFromC+MEM_pfp_ttt_isFromC+MME_ppf_ttt_isFromC;
		float emm_e_fT_isFromHL = EMM_fpp_ttt_isFromHL+MEM_pfp_ttt_isFromHL+MME_ppf_ttt_isFromHL;
		float emm_e_fT_isFromPh = EMM_fpp_ttt_isFromPh+MEM_pfp_ttt_isFromPh+MME_ppf_ttt_isFromPh;
		float emm_e_fT_isFromL = EMM_fpp_ttt_isFromL+MEM_pfp_ttt_isFromL+MME_ppf_ttt_isFromL;

	float emm_e_fL = EMM_fpp_ltt+MEM_pfp_tlt+MME_ppf_ttl;

		float emm_e_fL_isMatched = EMM_fpp_ltt_isMatched+MEM_pfp_tlt_isMatched+MME_ppf_ttl_isMatched;
		float emm_e_fL_isFromB = EMM_fpp_ltt_isFromB+MEM_pfp_tlt_isFromB+MME_ppf_ttl_isFromB;
		float emm_e_fL_isFromC = EMM_fpp_ltt_isFromC+MEM_pfp_tlt_isFromC+MME_ppf_ttl_isFromC;
		float emm_e_fL_isFromHL = EMM_fpp_ltt_isFromHL+MEM_pfp_tlt_isFromHL+MME_ppf_ttl_isFromHL;
		float emm_e_fL_isFromPh = EMM_fpp_ltt_isFromPh+MEM_pfp_tlt_isFromPh+MME_ppf_ttl_isFromPh;
		float emm_e_fL_isFromL = EMM_fpp_ltt_isFromL+MEM_pfp_tlt_isFromL+MME_ppf_ttl_isFromL;

	float emm_e_FR = emm_e_fT / ( emm_e_fT + emm_e_fL );
	cout << "       fake el f(T)          : " << emm_e_fT << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << emm_e_fT_isMatched << endl;
	cout << "               IsFromB          : " << emm_e_fT_isFromB << endl;
	cout << "               IsFromC          : " << emm_e_fT_isFromC << endl;
	cout << "               IsFromHL         : " << emm_e_fT_isFromHL << endl;
	cout << "               IsFromPh         : " << emm_e_fT_isFromPh << endl;
	cout << "               IsFromL          : " << emm_e_fT_isFromL << endl;
	}
	cout << "       fake el f(L)          : " << emm_e_fL << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << emm_e_fL_isMatched << endl;
	cout << "               IsFromB          : " << emm_e_fL_isFromB << endl;
	cout << "               IsFromC          : " << emm_e_fL_isFromC << endl;
	cout << "               IsFromHL         : " << emm_e_fL_isFromHL << endl;
	cout << "               IsFromPh         : " << emm_e_fL_isFromPh << endl;
	cout << "               IsFromL          : " << emm_e_fL_isFromL << endl;
	}
	cout << "       		el fake rate  : " << emm_e_fT / ( emm_e_fT + emm_e_fL ) << endl;

	float emm_m_fT = EMM_ppf_ttt+EMM_pfp_ttt+ MEM_ppf_ttt+ MEM_fpp_ttt+ MME_pfp_ttt+ MME_fpp_ttt;

		float emm_m_fT_isMatched = EMM_ppf_ttt_isMatched+EMM_pfp_ttt_isMatched+ MEM_ppf_ttt_isMatched+ MEM_fpp_ttt_isMatched+ MME_pfp_ttt_isMatched+ MME_fpp_ttt_isMatched;
		float emm_m_fT_isFromB = EMM_ppf_ttt_isFromB+EMM_pfp_ttt_isFromB+ MEM_ppf_ttt_isFromB+ MEM_fpp_ttt_isFromB+ MME_pfp_ttt_isFromB+ MME_fpp_ttt_isFromB;
		float emm_m_fT_isFromC = EMM_ppf_ttt_isFromC+EMM_pfp_ttt_isFromC+ MEM_ppf_ttt_isFromC+ MEM_fpp_ttt_isFromC+ MME_pfp_ttt_isFromC+ MME_fpp_ttt_isFromC;
		float emm_m_fT_isFromHL = EMM_ppf_ttt_isFromHL+EMM_pfp_ttt_isFromHL+ MEM_ppf_ttt_isFromHL+ MEM_fpp_ttt_isFromHL+ MME_pfp_ttt_isFromHL+ MME_fpp_ttt_isFromHL;
		float emm_m_fT_isFromPh = EMM_ppf_ttt_isFromPh+EMM_pfp_ttt_isFromPh+ MEM_ppf_ttt_isFromPh+ MEM_fpp_ttt_isFromPh+ MME_pfp_ttt_isFromPh+ MME_fpp_ttt_isFromPh;
		float emm_m_fT_isFromL = EMM_ppf_ttt_isFromL+EMM_pfp_ttt_isFromL+ MEM_ppf_ttt_isFromL+ MEM_fpp_ttt_isFromL+ MME_pfp_ttt_isFromL+ MME_fpp_ttt_isFromL;

	float emm_m_fL = EMM_ppf_ttl+EMM_pfp_tlt+ MEM_ppf_ttl+ MEM_fpp_ltt+ MME_pfp_tlt+ MME_fpp_ltt;

		float emm_m_fL_isMatched = EMM_ppf_ttl_isMatched+EMM_pfp_tlt_isMatched+ MEM_ppf_ttl_isMatched+ MEM_fpp_ltt_isMatched+ MME_pfp_tlt_isMatched+ MME_fpp_ltt_isMatched;
		float emm_m_fL_isFromB = EMM_ppf_ttl_isFromB+EMM_pfp_tlt_isFromB+ MEM_ppf_ttl_isFromB+ MEM_fpp_ltt_isFromB+ MME_pfp_tlt_isFromB+ MME_fpp_ltt_isFromB;
		float emm_m_fL_isFromC = EMM_ppf_ttl_isFromC+EMM_pfp_tlt_isFromC+ MEM_ppf_ttl_isFromC+ MEM_fpp_ltt_isFromC+ MME_pfp_tlt_isFromC+ MME_fpp_ltt_isFromC;
		float emm_m_fL_isFromHL = EMM_ppf_ttl_isFromHL+EMM_pfp_tlt_isFromHL+ MEM_ppf_ttl_isFromHL+ MEM_fpp_ltt_isFromHL+ MME_pfp_tlt_isFromHL+ MME_fpp_ltt_isFromHL;
		float emm_m_fL_isFromPh = EMM_ppf_ttl_isFromPh+EMM_pfp_tlt_isFromPh+ MEM_ppf_ttl_isFromPh+ MEM_fpp_ltt_isFromPh+ MME_pfp_tlt_isFromPh+ MME_fpp_ltt_isFromPh;
		float emm_m_fL_isFromL = EMM_ppf_ttl_isFromL+EMM_pfp_tlt_isFromL+ MEM_ppf_ttl_isFromL+ MEM_fpp_ltt_isFromL+ MME_pfp_tlt_isFromL+ MME_fpp_ltt_isFromL;

	float emm_m_FR = emm_m_fT / ( emm_m_fT + emm_m_fL );
	cout << "       fake mu f(T)          : " << emm_m_fT <<endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << emm_m_fT_isMatched << endl;
	cout << "               IsFromB          : " << emm_m_fT_isFromB << endl;
	cout << "               IsFromC          : " << emm_m_fT_isFromC << endl;
	cout << "               IsFromHL         : " << emm_m_fT_isFromHL << endl;
	cout << "               IsFromPh         : " << emm_m_fT_isFromPh << endl;
	cout << "               IsFromL          : " << emm_m_fT_isFromL << endl;
	}
	cout << "       fake mu f(L)          : " << emm_m_fL <<endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << emm_m_fL_isMatched << endl;
	cout << "               IsFromB          : " << emm_m_fL_isFromB << endl;
	cout << "               IsFromC          : " << emm_m_fL_isFromC << endl;
	cout << "               IsFromHL         : " << emm_m_fL_isFromHL << endl;
	cout << "               IsFromPh         : " << emm_m_fL_isFromPh << endl;
	cout << "               IsFromL          : " << emm_m_fL_isFromL << endl;
	}
	cout << "       		mu fake rate  : " << emm_m_fT / ( emm_m_fT + emm_m_fL ) << endl;


// }
// 	===========MMM==============

	MMM_ttt = t->Draw(observ,basic_cut+isMMM+" &&  isTTT " );
	
	MMM_pff = t->Draw(observ,basic_cut+isMMM+" &&  isPFF " );
	MMM_fpf = t->Draw(observ,basic_cut+isMMM+" &&  isFPF " );
	MMM_ffp = t->Draw(observ,basic_cut+isMMM+" &&  isFFP " );

	MMM_ppf = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )" );
	MMM_pfp = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )" );
	MMM_fpp = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )" );	

		MMM_ppf_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isMatched);
		MMM_pfp_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isMatched );
		MMM_fpp_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isMatched );	

		MMM_ppf_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isFromB);
		MMM_pfp_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isFromB );
		MMM_fpp_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isFromB );	

		MMM_ppf_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isFromC);
		MMM_pfp_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isFromC );
		MMM_fpp_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isFromC );	

		MMM_ppf_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isFromHL);
		MMM_pfp_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isFromHL );
		MMM_fpp_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isFromHL );	

		MMM_ppf_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isFromPh);
		MMM_pfp_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isFromPh );
		MMM_fpp_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isFromPh );	

		MMM_ppf_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )"+isPPF_isFromL);
		MMM_pfp_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )"+isPFP_isFromL );
		MMM_fpp_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )"+isFPP_isFromL );	

	MMM_ppf_ttl = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)" );
	MMM_pfp_tlt = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)" );
	MMM_fpp_ltt = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)" );
	MMM_ppf_ttt = t->Draw(observ,basic_cut+isMMM+" && ( isPPF || isPFP || isFPP ) && isTTT " );

	MMM_ppp = t->Draw(observ,basic_cut+isMMM+isPPP);
	MMM_fff = t->Draw(observ,basic_cut+isMMM+isFFF);

	MMM = t->Draw(observ,basic_cut+isMMM);

	MMM_ppf_ttl_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isMatched);
	MMM_pfp_tlt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isMatched );
	MMM_fpp_ltt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isMatched );

	MMM_ppf_ttl_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromB);
	MMM_pfp_tlt_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromB );
	MMM_fpp_ltt_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromB );

	MMM_ppf_ttl_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromC);
	MMM_pfp_tlt_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromC );
	MMM_fpp_ltt_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromC );

	MMM_ppf_ttl_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromHL);
	MMM_pfp_tlt_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromHL );
	MMM_fpp_ltt_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromHL );

	MMM_ppf_ttl_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromPh);
	MMM_pfp_tlt_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromPh );
	MMM_fpp_ltt_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromPh );

	MMM_ppf_ttl_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromL);
	MMM_pfp_tlt_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromL );
	MMM_fpp_ltt_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromL );

	//

	MMM_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isMatched);
	MMM_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isMatched );
	MMM_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isMatched );

	MMM_ppf_ttt_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromB);
	MMM_pfp_ttt_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromB );
	MMM_fpp_ttt_isFromB = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromB );

	MMM_ppf_ttt_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromC);
	MMM_pfp_ttt_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromC );
	MMM_fpp_ttt_isFromC = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromC );

	MMM_ppf_ttt_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromHL);
	MMM_pfp_ttt_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromHL );
	MMM_fpp_ttt_isFromHL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromHL );

	MMM_ppf_ttt_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromPh);
	MMM_pfp_ttt_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromPh );
	MMM_fpp_ttt_isFromPh = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromPh );

	MMM_ppf_ttt_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromL);
	MMM_pfp_ttt_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromL );
	MMM_fpp_ttt_isFromL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromL );


	//


	cout << " ========= MMM ========= " << endl;
	cout << "Counts of MMM: FFF(" << MMM_fff<< "), PFF(" <<MMM_pff+MMM_fpf+MMM_ffp <<"), PPF("<< MMM_ppf+MMM_pfp+MMM_fpp<<"), PPP("<< MMM_ppp <<") : "<< MMM<< ", TTT(" <<MMM_ttt  << ")"<<endl; 
	cout << "	1 fake / 2 prompts:   "<< endl;
	cout << "       IsTTT f(T)  : " << MMM_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MMM_ppf_ttt_isMatched+MMM_pfp_ttt_isMatched+MMM_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MMM_ppf_ttt_isFromB+MMM_pfp_ttt_isFromB+MMM_fpp_ttt_isFromB << endl;
	cout << "               IsFromC          : " << MMM_ppf_ttt_isFromC+MMM_pfp_ttt_isFromC+MMM_fpp_ttt_isFromC << endl;
	cout << "               IsFromHL         : " << MMM_ppf_ttt_isFromHL+MMM_pfp_ttt_isFromHL+MMM_fpp_ttt_isFromHL << endl;
	cout << "               IsFromPh         : " << MMM_ppf_ttt_isFromPh+MMM_pfp_ttt_isFromPh+MMM_fpp_ttt_isFromPh << endl;
	cout << "               IsFromL          : " << MMM_ppf_ttt_isFromL+MMM_pfp_ttt_isFromL+MMM_fpp_ttt_isFromL << endl;
	}
	cout << "       IsTTL f(L) : " << MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MMM_ppf_ttl_isMatched+MMM_pfp_tlt_isMatched+MMM_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << MMM_ppf_ttl_isFromB+MMM_pfp_tlt_isFromB+MMM_fpp_ltt_isFromB << endl;
	cout << "               IsFromC          : " << MMM_ppf_ttl_isFromC+MMM_pfp_tlt_isFromC+MMM_fpp_ltt_isFromC << endl;
	cout << "               IsFromHL         : " << MMM_ppf_ttl_isFromHL+MMM_pfp_tlt_isFromHL+MMM_fpp_ltt_isFromHL << endl;
	cout << "               IsFromPh         : " << MMM_ppf_ttl_isFromPh+MMM_pfp_tlt_isFromPh+MMM_fpp_ltt_isFromPh << endl;
	cout << "               IsFromL          : " << MMM_ppf_ttl_isFromL+MMM_pfp_tlt_isFromL+MMM_fpp_ltt_isFromL << endl;
	}
	float mmm_fT = MMM_ppf_ttt*1.0;
	float mmm_fL = (MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt )*1.0;
	float mmm_FR = mmm_fT / ( mmm_fT  + mmm_fL ) ;
	cout << "       		mu fake rate  : " << mmm_FR << endl;
	cout << "       ---------------------  " << endl;
	cout << "			MMM PPF / MMM		: " << (MMM_ppf+MMM_pfp+MMM_fpp)<<" / "<<MMM <<" = "<< 1.0*(MMM_ppf+MMM_pfp+MMM_fpp)/MMM << endl; 
	cout << "			MMM PPF (M)IsFromB / MMM	: " << (MMM_ppf_isFromB+MMM_pfp_isFromB+MMM_fpp_isFromB) <<" / "<< MMM <<" = "<< 1.0*(MMM_ppf_isFromB+MMM_pfp_isFromB+MMM_fpp_isFromB) / MMM << endl;
	
	//===========ALL==============
	
	cout << " ========= ALL ========= " << endl;

	ALL_pff = t->Draw(observ,basic_cut+" && ( isPFF || isFPF || isFFP)" );
	ALL_ppf = t->Draw(observ,basic_cut+" && ( isPPF || isPFP || isFPP)" );
	ALL_ppp = t->Draw(observ,basic_cut+isPPP);
	ALL_fff = t->Draw(observ,basic_cut+isFFF);
	ALL = t->Draw(observ,basic_cut);

	ALL_ppf_isMatched = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isMatched+isPFP_isMatched+isFPP_isMatched);
	ALL_ppf_isFromB = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isFromB+isPFP_isFromB+isFPP_isFromB);
	ALL_ppf_isFromC = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isFromC+isPFP_isFromC+isFPP_isFromC);
	ALL_ppf_isFromHL = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isFromHL+isPFP_isFromHL+isFPP_isFromHL);
	ALL_ppf_isFromPh = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isFromPh+isPFP_isFromPh+isFPP_isFromPh);
	ALL_ppf_isFromL = t->Draw(observ,basic_cut+isPPF+isPFP+isFPP+isPPF_isFromL+isPFP_isFromL+isFPP_isFromL);

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
	cout << "			EEE PPF	(E)IsFromB / EEE : " << (EEE_ppf_isFromB+EEE_pfp_isFromB+EEE_fpp_isFromB) <<" / "<< EEE <<" = "<< 1.0*(EEE_ppf_isFromB+EEE_pfp_isFromB+EEE_fpp_isFromB) / EEE << endl;
	cout << "       EEM---------------------  " << endl;
	cout << "			EE PP / PPF		: "<< (EEM_ppf + EME_pfp + MEE_fpp) <<" / "<< eem_ppf <<" = "<< 1.0*(EEM_ppf + EME_pfp + MEE_fpp) / eem_ppf << endl; 
	cout << "			EE PP (M)isFromB / PPF	: "<< (EEM_ppf_isFromB + EME_pfp_isFromB + MEE_fpp_isFromB) <<" / "<< eem_ppf <<" = "<< 1.0*(EEM_ppf_isFromB + EME_pfp_isFromB + MEE_fpp_isFromB) / eem_ppf << endl; 
	cout << "			EM PP / PPF		: "<<  (EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp) <<" / "<< eem_ppf <<" = "<<1.0*(EEM_pfp + EEM_fpp + EME_ppf + EME_fpp + MEE_ppf + MEE_pfp) / eem_ppf << endl; 
	cout << "			EM PP (E)isFromB / PPF	: "<< (EEM_pfp_isFromB + EEM_fpp_isFromB + EME_ppf_isFromB + EME_fpp_isFromB + MEE_ppf_isFromB + MEE_pfp_isFromB) <<" / "<< eem_ppf <<" = "<< 1.0*(EEM_pfp_isFromB + EEM_fpp_isFromB + EME_ppf_isFromB + EME_fpp_isFromB + MEE_ppf_isFromB + MEE_pfp_isFromB) / eem_ppf << endl; 
	cout << "       EMM---------------------  " << endl;
	cout << "			EM PP / PPF 		: "	<< EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp << " / " << emm_ppf <<" = "<<1.0*(EMM_ppf+EMM_pfp+MEM_ppf+MEM_fpp+MME_pfp+MME_fpp) / emm_ppf << endl; 
	cout << "			EM PP (M)isFromB / PPF	: "<< (EMM_ppf_isFromB+EMM_pfp_isFromB+MEM_ppf_isFromB+MEM_fpp_isFromB+MME_pfp_isFromB+MME_fpp_isFromB) << " / "<< emm_ppf <<" = "<< 1.0*(EMM_ppf_isFromB+EMM_pfp_isFromB+MEM_ppf_isFromB+MEM_fpp_isFromB+MME_pfp_isFromB+MME_fpp_isFromB) / emm_ppf << endl; 
	cout << " 			MM PP / PPF 		: "<< EMM_fpp+MEM_pfp+MME_ppf << " / " << emm_ppf <<" = "<< 1.0*(EMM_fpp+MEM_pfp+MME_ppf) / emm_ppf << endl; 
	cout << " 			MM PP (E)isFromB / PPF	: "<< EMM_fpp_isFromB+MEM_pfp_isFromB+MME_ppf_isFromB <<  " / " << emm_ppf <<" = "<< 1.0*(EMM_fpp_isFromB+MEM_pfp_isFromB+MME_ppf_isFromB) / emm_ppf << endl; 
	cout << "       MMM---------------------  " << endl;
	cout << "			MMM PPF / MMM 		: " << (MMM_ppf+MMM_pfp+MMM_fpp)<<" / "<<MMM <<" = "<< 1.0*(MMM_ppf+MMM_pfp+MMM_fpp)/MMM << endl; 
	cout << "			MMM PPF (M)IsFromB / MMM : " << (MMM_ppf_isFromB+MMM_pfp_isFromB+MMM_fpp_isFromB) <<" / "<< MMM <<" = "<< 1.0*(MMM_ppf_isFromB+MMM_pfp_isFromB+MMM_fpp_isFromB) / MMM << endl;

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
