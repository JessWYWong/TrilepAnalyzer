
using namespace std;

void CountRates(){

	bool PrintMixedChannels = false;
	cout << "PrintMixedChannels = " << PrintMixedChannels << endl;	
	bool printSource = true;
	
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V3_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V4_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V6_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V7_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V8_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv6_FRv28ttbar_newMuTrkSF_PromptCount_V9_DEBUGGED_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined_hadd.root";

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

// 	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_singleLepCalc >= 0) && (NJets_singleLepCalc >= 0) && (NJetsBTagwithSF_singleLepCalc >= 0) && DataPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";
	TString basic_cut = "1 && (AllLeptonPt_PtOrdered[0] >= 30) && (AllLeptonPt_PtOrdered[1] >= 30) && (AllLeptonPt_PtOrdered[2] >= 30) && (corr_met_singleLepCalc >= 0) && (NJets_singleLepCalc >= 0) && (NJetsBTagwithSF_singleLepCalc >= 0) && MCPastTrigger_dilep == 1 && (AK4HTpMETpLepPt >= 0) && AllLeptonCount_PtOrdered == 3 && ( (MllOS_allComb[0] > 0 || MllOS_allComb[0] < 0) && (MllOS_allComb[1] > 0 || MllOS_allComb[1] < 0) && (MllOS_allComb[2] > 0 || MllOS_allComb[2] < 0) )";

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

	EEE_ppf_ttl_isB = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromB);
	EEE_pfp_tlt_isB = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromB );
	EEE_fpp_ltt_isB = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromB );

	EEE_ppf_ttl_isC = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromC);
	EEE_pfp_tlt_isC = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromC );
	EEE_fpp_ltt_isC = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromC );

	EEE_ppf_ttl_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromHL);
	EEE_pfp_tlt_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromHL );
	EEE_fpp_ltt_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromHL );

	EEE_ppf_ttl_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromPh);
	EEE_pfp_tlt_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromPh );
	EEE_fpp_ltt_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromPh );

	EEE_ppf_ttl_isL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTL)"+isPPF_isFromL);
	EEE_pfp_tlt_isL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTLT)"+isPFP_isFromL );
	EEE_fpp_ltt_isL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isLTT)"+isFPP_isFromL );

	//

	EEE_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isMatched);
	EEE_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isMatched );
	EEE_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isMatched );

	EEE_ppf_ttt_isB = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromB);
	EEE_pfp_ttt_isB = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromB );
	EEE_fpp_ttt_isB = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromB );

	EEE_ppf_ttt_isC = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromC);
	EEE_pfp_ttt_isC = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromC );
	EEE_fpp_ttt_isC = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromC );

	EEE_ppf_ttt_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromHL);
	EEE_pfp_ttt_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromHL );
	EEE_fpp_ttt_isHL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromHL );

	EEE_ppf_ttt_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromPh);
	EEE_pfp_ttt_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromPh );
	EEE_fpp_ttt_isPh = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromPh );

	EEE_ppf_ttt_isL = t->Draw(observ,basic_cut+isEEE+" && ( isPPF & isTTT)"+isPPF_isFromL);
	EEE_pfp_ttt_isL = t->Draw(observ,basic_cut+isEEE+" && ( isPFP & isTTT)"+isPFP_isFromL );
	EEE_fpp_ttt_isL = t->Draw(observ,basic_cut+isEEE+" && ( isFPP & isTTT)"+isFPP_isFromL );


	//
	cout << " ========= EEE ========= " << endl;
	cout << "Counts of EEE: FFF(" << EEE_fff<< "), PFF(" <<EEE_pff+EEE_fpf+EEE_ffp <<"), PPF("<< EEE_ppf+EEE_pfp+EEE_fpp<<"), PPP("<< EEE_ppp <<") : "<< EEE<<", TTT("<< EEE_ttt << ")"<<endl; 
	cout << "	--1 fake /2 prompts:   "<< endl;
	cout << "       IsTTT f(T)  : " << EEE_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEE_ppf_ttt_isMatched+EEE_pfp_ttt_isMatched+EEE_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << EEE_ppf_ttt_isB+EEE_pfp_ttt_isB+EEE_fpp_ttt_isB << endl;
	cout << "               IsFromC          : " << EEE_ppf_ttt_isC+EEE_pfp_ttt_isC+EEE_fpp_ttt_isC << endl;
	cout << "               IsFromHL         : " << EEE_ppf_ttt_isHL+EEE_pfp_ttt_isHL+EEE_fpp_ttt_isHL << endl;
	cout << "               IsFromPh         : " << EEE_ppf_ttt_isPh+EEE_pfp_ttt_isPh+EEE_fpp_ttt_isPh << endl;
	cout << "               IsFromL          : " << EEE_ppf_ttt_isL+EEE_pfp_ttt_isL+EEE_fpp_ttt_isL << endl;
	}
	cout << "       IsTTL f(L) : " << EEE_ppf_ttl+EEE_pfp_tlt+EEE_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << EEE_ppf_ttl_isMatched+EEE_pfp_tlt_isMatched+EEE_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << EEE_ppf_ttl_isB+EEE_pfp_tlt_isB+EEE_fpp_ltt_isB << endl;
	cout << "               IsFromC          : " << EEE_ppf_ttl_isC+EEE_pfp_tlt_isC+EEE_fpp_ltt_isC << endl;
	cout << "               IsFromHL         : " << EEE_ppf_ttl_isHL+EEE_pfp_tlt_isHL+EEE_fpp_ltt_isHL << endl;
	cout << "               IsFromPh         : " << EEE_ppf_ttl_isPh+EEE_pfp_tlt_isPh+EEE_fpp_ltt_isPh << endl;
	cout << "               IsFromL          : " << EEE_ppf_ttl_isL+EEE_pfp_tlt_isL+EEE_fpp_ltt_isL << endl;
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

	EEM_ppf_ttl = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTL);
	EEM_pfp_tlt = t->Draw(observ,basic_cut+isEEM_+isPFP+isTLT);
	EEM_fpp_ltt = t->Draw(observ,basic_cut+isEEM_+isFPP+isLTT);

	EEM_ppf_ttt = t->Draw(observ,basic_cut+isEEM_+isPPF+isTTT);
	EEM_pfp_ttt = t->Draw(observ,basic_cut+isEEM_+isPFP+isTTT);
	EEM_fpp_ttt = t->Draw(observ,basic_cut+isEEM_+isFPP+isTTT);

	//EME - 2prompts
	EME_ppf = t->Draw(observ,basic_cut+isEME_+isPPF);
	EME_pfp = t->Draw(observ,basic_cut+isEME_+isPFP);
	EME_fpp = t->Draw(observ,basic_cut+isEME_+isFPP);

	EME_ppf_ttl = t->Draw(observ,basic_cut+isEME_+isPPF+isTTL);
	EME_pfp_tlt = t->Draw(observ,basic_cut+isEME_+isPFP+isTLT);
	EME_fpp_ltt = t->Draw(observ,basic_cut+isEME_+isFPP+isLTT);

	EME_ppf_ttt = t->Draw(observ,basic_cut+isEME_+isPPF+isTTT);
	EME_pfp_ttt = t->Draw(observ,basic_cut+isEME_+isPFP+isTTT);
	EME_fpp_ttt = t->Draw(observ,basic_cut+isEME_+isFPP+isTTT);

	//MEE - 2prompts
	MEE_ppf = t->Draw(observ,basic_cut+isMEE_+isPPF);
	MEE_pfp = t->Draw(observ,basic_cut+isMEE_+isPFP);
	MEE_fpp = t->Draw(observ,basic_cut+isMEE_+isFPP);

	MEE_ppf_ttl = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTL);
	MEE_pfp_tlt = t->Draw(observ,basic_cut+isMEE_+isPFP+isTLT);
	MEE_fpp_ltt = t->Draw(observ,basic_cut+isMEE_+isFPP+isLTT);

	MEE_ppf_ttt = t->Draw(observ,basic_cut+isMEE_+isPPF+isTTT);
	MEE_pfp_ttt = t->Draw(observ,basic_cut+isMEE_+isPFP+isTTT);
	MEE_fpp_ttt = t->Draw(observ,basic_cut+isMEE_+isFPP+isTTT);

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
	cout << "       EEM PPF TTT (fake mu) : " << EEM_ppf_ttt << endl;
	cout << "       EEM PFP TTT (fake el) : " << EEM_pfp_ttt << endl;
	cout << "       EEM FPP TTT (fake el) : " << EEM_fpp_ttt << endl;
	cout << "-" << endl;
	cout << "       EME PPF TTT (fake el) : " << EME_ppf_ttt << endl;
	cout << "       EME PFP TTT (fake mu) : " << EME_pfp_ttt << endl;
	cout << "       EME FPP TTT (fake el) : " << EME_fpp_ttt << endl;
	cout << "-" << endl;
	cout << "       MEE PPF TTT (fake el) : " << MEE_ppf_ttt << endl;
	cout << "       MEE PFP TTT (fake el) : " << MEE_pfp_ttt << endl;
	cout << "       MEE FPP TTT (fake mu) : " << MEE_fpp_ttt << endl;
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EEM PPF TTL (fake mu) : " << EEM_ppf_ttl << endl;
	cout << "       EEM PFP TLT (fake el) : " << EEM_pfp_tlt << endl;
	cout << "       EEM FPP LTT (fake el) : " << EEM_fpp_ltt << endl;
	cout << "-" << endl;
	cout << "       EME PPF TTL (fake el) : " << EME_ppf_ttl << endl;
	cout << "       EME PFP TLT (fake mu) : " << EME_pfp_tlt << endl;
	cout << "       EME FPP LTT (fake el) : " << EME_fpp_ltt << endl;
	cout << "-" << endl;
	cout << "       MEE PPF TTL (fake el) : " << MEE_ppf_ttl << endl;
	cout << "       MEE PFP TLT (fake el) : " << MEE_pfp_tlt << endl;
	cout << "       MEE FPP LTT (fake mu) : " << MEE_fpp_ltt << endl;
	cout << "       ---------------------  " << endl;
	float eem_e_fT = EEM_pfp_ttt+EEM_fpp_ttt+EME_ppf_ttt+EME_fpp_ttt+MEE_ppf_ttt+MEE_pfp_ttt;
	float eem_e_fL = EEM_pfp_tlt+EEM_fpp_ltt+EME_ppf_ttl+EME_fpp_ltt+MEE_ppf_ttl+MEE_pfp_tlt;
	float eem_e_FR = eem_e_fT / ( eem_e_fT + eem_e_fL );
	cout << "       fake el f(T)          : " << eem_e_fT << endl;
	cout << "       fake el f(L)          : " << eem_e_fL << endl;
	cout << "       		el fake rate  : " << eem_e_fT / ( eem_e_fT + eem_e_fL ) << endl;

	float eem_m_fT = EEM_ppf_ttt+EME_pfp_ttt+MEE_fpp_ttt;
	float eem_m_fL = EEM_ppf_ttl+EME_pfp_tlt+MEE_fpp_ltt;
	float eem_m_FR = eem_m_fT / ( eem_m_fT + eem_m_fL );
	cout << "       fake mu f(T)          : " << eem_m_fT<<endl;
	cout << "       fake mu f(L)          : " << eem_m_fL<<endl;
	cout << "       		mu fake rate  : " << eem_m_fT / ( eem_m_fT + eem_m_fL ) << endl;
	//===========EMM==============
	
	EMM_ttt = t->Draw(observ,basic_cut+isEMM_+isTTT);
	MEM_ttt = t->Draw(observ,basic_cut+isMEM_+isTTT);
	MME_ttt = t->Draw(observ,basic_cut+isMME_+isTTT);

	//1 fake / 2 prompts
	EMM_ppf = t->Draw(observ,basic_cut+isEMM_+isPPF);
	EMM_pfp = t->Draw(observ,basic_cut+isEMM_+isPFP);
	EMM_fpp = t->Draw(observ,basic_cut+isEMM_+isFPP);

	MEM_ppf = t->Draw(observ,basic_cut+isMEM_+isPPF);
	MEM_pfp = t->Draw(observ,basic_cut+isMEM_+isPFP);
	MEM_fpp = t->Draw(observ,basic_cut+isMEM_+isFPP);

	MME_ppf = t->Draw(observ,basic_cut+isMME_+isPPF);
	MME_pfp = t->Draw(observ,basic_cut+isMME_+isPFP);
	MME_fpp = t->Draw(observ,basic_cut+isMME_+isFPP);

	EMM_ppf_ttt = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTT);
	EMM_pfp_ttt = t->Draw(observ,basic_cut+isEMM_+isPFP+isTTT);
	EMM_fpp_ttt = t->Draw(observ,basic_cut+isEMM_+isFPP+isTTT);

	MEM_ppf_ttt = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTT);
	MEM_pfp_ttt = t->Draw(observ,basic_cut+isMEM_+isPFP+isTTT);
	MEM_fpp_ttt = t->Draw(observ,basic_cut+isMEM_+isFPP+isTTT);

	MME_ppf_ttt = t->Draw(observ,basic_cut+isMME_+isPPF+isTTT);
	MME_pfp_ttt = t->Draw(observ,basic_cut+isMME_+isPFP+isTTT);
	MME_fpp_ttt = t->Draw(observ,basic_cut+isMME_+isFPP+isTTT);

	EMM_ppf_ttl = t->Draw(observ,basic_cut+isEMM_+isPPF+isTTL);
	EMM_pfp_tlt = t->Draw(observ,basic_cut+isEMM_+isPFP+isTLT);
	EMM_fpp_ltt = t->Draw(observ,basic_cut+isEMM_+isFPP+isLTT);

	MEM_ppf_ttl = t->Draw(observ,basic_cut+isMEM_+isPPF+isTTL);
	MEM_pfp_tlt = t->Draw(observ,basic_cut+isMEM_+isPFP+isTLT);
	MEM_fpp_ltt = t->Draw(observ,basic_cut+isMEM_+isFPP+isLTT);

	MME_ppf_ttl = t->Draw(observ,basic_cut+isMME_+isPPF+isTTL);
	MME_pfp_tlt = t->Draw(observ,basic_cut+isMME_+isPFP+isTLT);
	MME_fpp_ltt = t->Draw(observ,basic_cut+isMME_+isFPP+isLTT);

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
	cout << "       EMM PPF TTT (fake mu) : " << EMM_ppf_ttt << endl;
	cout << "       EMM PFP TTT (fake mu) : " << EMM_pfp_ttt << endl;
	cout << "       EMM FPP TTT (fake el) : " << EMM_fpp_ttt << endl;
	cout << "-" << endl;
	cout << "       MEM PPF TTT (fake mu) : " << MEM_ppf_ttt << endl;
	cout << "       MEM PFP TTT (fake el) : " << MEM_pfp_ttt << endl;
	cout << "       MEM FPP TTT (fake mu) : " << MEM_fpp_ttt << endl;
	cout << "-" << endl;
	cout << "       MME PPF TTT (fake el) : " << MME_ppf_ttt << endl;
	cout << "       MME PFP TTT (fake mu) : " << MME_pfp_ttt << endl;
	cout << "       MME FPP TTT (fake mu) : " << MME_fpp_ttt << endl;
	cout << "" << endl;
	cout << "	f(L):   "<< endl;
	cout << "       EMM PPF TTL (fake mu) : " << EMM_ppf_ttl << endl;
	cout << "       EMM PFP TLT (fake mu) : " << EMM_pfp_tlt << endl;
	cout << "       EMM FPP LTT (fake el) : " << EMM_fpp_ltt << endl;
	cout << "-" << endl;
	cout << "       MEM PPF TTL (fake mu) : " << MEM_ppf_ttl << endl;
	cout << "       MEM PFP TLT (fake el) : " << MEM_pfp_tlt << endl;
	cout << "       MEM FPP LTT (fake mu) : " << MEM_fpp_ltt << endl;
	cout << "-" << endl;
	cout << "       MME PPF TTL (fake el) : " << MME_ppf_ttl << endl;
	cout << "       MME PFP TLT (fake mu) : " << MME_pfp_tlt << endl;
	cout << "       MME FPP LTT (fake mu) : " << MME_fpp_ltt << endl;
	cout << "       ---------------------  " << endl;

	float emm_e_fT = EMM_fpp_ttt+MEM_pfp_ttt+MME_ppf_ttt;
	float emm_e_fL = EMM_fpp_ltt+MEM_pfp_tlt+MME_ppf_ttl;
	float emm_e_FR = emm_e_fT / ( emm_e_fT + emm_e_fL );
	cout << "       fake el f(T)          : " << emm_e_fT << endl;
	cout << "       fake el f(L)          : " << emm_e_fL << endl;
	cout << "       		el fake rate  : " << emm_e_fT / ( emm_e_fT + emm_e_fL ) << endl;

	float emm_m_fT = EMM_ppf_ttt+EMM_pfp_ttt+ MEM_ppf_ttt+ MEM_fpp_ttt+ MME_pfp_ttt+ MME_fpp_ttt;
	float emm_m_fL = EMM_ppf_ttl+EMM_pfp_tlt+ MEM_ppf_ttl+ MEM_fpp_ltt+ MME_pfp_tlt+ MME_fpp_ltt;
	float emm_m_FR = emm_m_fT / ( emm_m_fT + emm_m_fL );
	cout << "       fake mu f(T)          : " << emm_m_fT <<endl;
	cout << "       fake mu f(L)          : " << emm_m_fL <<endl;
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

	MMM_ppf_ttl_isB = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromB);
	MMM_pfp_tlt_isB = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromB );
	MMM_fpp_ltt_isB = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromB );

	MMM_ppf_ttl_isC = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromC);
	MMM_pfp_tlt_isC = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromC );
	MMM_fpp_ltt_isC = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromC );

	MMM_ppf_ttl_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromHL);
	MMM_pfp_tlt_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromHL );
	MMM_fpp_ltt_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromHL );

	MMM_ppf_ttl_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromPh);
	MMM_pfp_tlt_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromPh );
	MMM_fpp_ltt_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromPh );

	MMM_ppf_ttl_isL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTL)"+isPPF_isFromL);
	MMM_pfp_tlt_isL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTLT)"+isPFP_isFromL );
	MMM_fpp_ltt_isL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isLTT)"+isFPP_isFromL );

	//

	MMM_ppf_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isMatched);
	MMM_pfp_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isMatched );
	MMM_fpp_ttt_isMatched = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isMatched );

	MMM_ppf_ttt_isB = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromB);
	MMM_pfp_ttt_isB = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromB );
	MMM_fpp_ttt_isB = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromB );

	MMM_ppf_ttt_isC = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromC);
	MMM_pfp_ttt_isC = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromC );
	MMM_fpp_ttt_isC = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromC );

	MMM_ppf_ttt_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromHL);
	MMM_pfp_ttt_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromHL );
	MMM_fpp_ttt_isHL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromHL );

	MMM_ppf_ttt_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromPh);
	MMM_pfp_ttt_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromPh );
	MMM_fpp_ttt_isPh = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromPh );

	MMM_ppf_ttt_isL = t->Draw(observ,basic_cut+isMMM+" && ( isPPF & isTTT)"+isPPF_isFromL);
	MMM_pfp_ttt_isL = t->Draw(observ,basic_cut+isMMM+" && ( isPFP & isTTT)"+isPFP_isFromL );
	MMM_fpp_ttt_isL = t->Draw(observ,basic_cut+isMMM+" && ( isFPP & isTTT)"+isFPP_isFromL );


	//


	cout << " ========= MMM ========= " << endl;
	cout << "Counts of MMM: FFF(" << MMM_fff<< "), PFF(" <<MMM_pff+MMM_fpf+MMM_ffp <<"), PPF("<< MMM_ppf+MMM_pfp+MMM_fpp<<"), PPP("<< MMM_ppp <<") : "<< MMM<< ", TTT(" <<MMM_ttt  << ")"<<endl; 
	cout << "	1 fake / 2 prompts:   "<< endl;
	cout << "       IsTTT f(T)  : " << MMM_ppf_ttt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MMM_ppf_ttt_isMatched+MMM_pfp_ttt_isMatched+MMM_fpp_ttt_isMatched << endl;
	cout << "               IsFromB          : " << MMM_ppf_ttt_isB+MMM_pfp_ttt_isB+MMM_fpp_ttt_isB << endl;
	cout << "               IsFromC          : " << MMM_ppf_ttt_isC+MMM_pfp_ttt_isC+MMM_fpp_ttt_isC << endl;
	cout << "               IsFromHL         : " << MMM_ppf_ttt_isHL+MMM_pfp_ttt_isHL+MMM_fpp_ttt_isHL << endl;
	cout << "               IsFromPh         : " << MMM_ppf_ttt_isPh+MMM_pfp_ttt_isPh+MMM_fpp_ttt_isPh << endl;
	cout << "               IsFromL          : " << MMM_ppf_ttt_isL+MMM_pfp_ttt_isL+MMM_fpp_ttt_isL << endl;
	}
	cout << "       IsTTL f(L) : " << MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt << endl;
	if(printSource){
	cout << "               Is(not)Matched   : " << MMM_ppf_ttl_isMatched+MMM_pfp_tlt_isMatched+MMM_fpp_ltt_isMatched << endl;
	cout << "               IsFromB          : " << MMM_ppf_ttl_isB+MMM_pfp_tlt_isB+MMM_fpp_ltt_isB << endl;
	cout << "               IsFromC          : " << MMM_ppf_ttl_isC+MMM_pfp_tlt_isC+MMM_fpp_ltt_isC << endl;
	cout << "               IsFromHL         : " << MMM_ppf_ttl_isHL+MMM_pfp_tlt_isHL+MMM_fpp_ltt_isHL << endl;
	cout << "               IsFromPh         : " << MMM_ppf_ttl_isPh+MMM_pfp_tlt_isPh+MMM_fpp_ltt_isPh << endl;
	cout << "               IsFromL          : " << MMM_ppf_ttl_isL+MMM_pfp_tlt_isL+MMM_fpp_ltt_isL << endl;
	}
	float mmm_fT = MMM_ppf_ttt*1.0;
	float mmm_fL = (MMM_ppf_ttl+MMM_pfp_tlt+MMM_fpp_ltt )*1.0;
	float mmm_FR = mmm_fT / ( mmm_fT  + mmm_fL ) ;
	cout << "       		mu fake rate  : " << mmm_FR << endl;
	
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
	
	gApplication->Terminate();
	
}
