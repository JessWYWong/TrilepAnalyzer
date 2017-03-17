
using namespace std;

void CountRates_prompt(){

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
	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_4_rizki_PRv9_FRv24_postPreapprovalF_PromptCount_V9_extScan_step1hadds/nominal/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_hadd.root";
// 	TString f_str = "/user_data/rsyarif/LJMet80x_3lepTT_Full2016_Moriond17_reMiniAOD_nuBTVSF_modMETfilt_saveLooseMC_2017_3_7_rizki_mcClosure_step1hadds/nominal/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_combined_hadd.root";

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

	TString isTLL = " && isTLL"; 
	TString isLTL = " && isLTL"; 
	TString isLLT = " && isLLT"; 
	TString isLLL = " && isLLL"; 
	
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
	EEE_lll = t->Draw(observ,basic_cut+isEEE+" &&  isLLL " );

	//1prompt
	EEE_pff = t->Draw(observ,basic_cut+isEEE+" &&  isPFF " );
	EEE_fpf = t->Draw(observ,basic_cut+isEEE+" &&  isFPF " );
	EEE_ffp = t->Draw(observ,basic_cut+isEEE+" &&  isFFP " );

	EEE_pff_tll = t->Draw(observ,basic_cut+isEEE+" &&  isPFF && isTLL " );
	EEE_fpf_ltl = t->Draw(observ,basic_cut+isEEE+" &&  isFPF && isLTL " );
	EEE_ffp_llt = t->Draw(observ,basic_cut+isEEE+" &&  isFFP && isLLT " );

	EEE_pff_lll = t->Draw(observ,basic_cut+isEEE+" &&  isPFF && isLLL " );
	EEE_fpf_lll = t->Draw(observ,basic_cut+isEEE+" &&  isFPF && isLLL " );
	EEE_ffp_lll = t->Draw(observ,basic_cut+isEEE+" &&  isFFP && isLLL " );

	//2 prompts (1 fake)
	EEE_ppf = t->Draw(observ,basic_cut+isEEE+" && ( isPPF )" );
	EEE_pfp = t->Draw(observ,basic_cut+isEEE+" && ( isPFP )" );
	EEE_fpp = t->Draw(observ,basic_cut+isEEE+" && ( isFPP )" );
	
	//3 prompts , 3 fakes
	EEE_ppp = t->Draw(observ,basic_cut+isEEE+isPPP);
	EEE_fff = t->Draw(observ,basic_cut+isEEE+isFFF);

	//All
	EEE = t->Draw(observ,basic_cut+isEEE);

	//
	cout << " ========= EEE ========= " << endl;
	cout << "Counts of EEE: FFF(" << EEE_fff<< "), PFF(" <<EEE_pff+EEE_fpf+EEE_ffp <<"), PPF("<< EEE_ppf+EEE_pfp+EEE_fpp<<"), PPP("<< EEE_ppp <<") : "<< EEE<<", TTT("<< EEE_ttt << ")"<<endl; 
	cout << "	--1 prompt /2 fakes:   "<< endl;
	cout << "       IsLLL f(L)  : " << EEE_pff_lll+EEE_fpf_lll+EEE_ffp_lll << endl;
	cout << "       IsTLL f(T) : " << EEE_pff_tll+EEE_fpf_ltl+EEE_ffp_llt << endl;
	float eee_pT = (EEE_pff_tll+EEE_fpf_ltl+EEE_ffp_llt)*1.0;
	float eee_pL = (EEE_pff_lll+EEE_fpf_lll+EEE_ffp_lll )*1.0;
	float eee_PR = eee_pT / ( eee_pT  + eee_pL ) ;
	cout << "       		el prompt rate  : " << eee_PR << endl;

// if(PrintMixedChannels){
	//===========EEM==============

	EEM_lll = t->Draw(observ,basic_cut+isEEM_+isLLL);
	EME_lll = t->Draw(observ,basic_cut+isEME_+isLLL);
	MEE_lll = t->Draw(observ,basic_cut+isMEE_+isLLL);

	//1prompt
	EEM_pff = t->Draw(observ,basic_cut+isEEM_+isPFF);
	EEM_fpf = t->Draw(observ,basic_cut+isEEM_+isFPF);
	EEM_ffp = t->Draw(observ,basic_cut+isEEM_+isFFP);

	EEM_pff_tll = t->Draw(observ,basic_cut+isEEM_+isPFF+isTLL);
	EEM_fpf_ltl = t->Draw(observ,basic_cut+isEEM_+isFPF+isLTL);
	EEM_ffp_llt = t->Draw(observ,basic_cut+isEEM_+isFFP+isLLT);

	EEM_pff_lll = t->Draw(observ,basic_cut+isEEM_+isPFF+isLLL);
	EEM_fpf_lll = t->Draw(observ,basic_cut+isEEM_+isFPF+isLLL);
	EEM_ffp_lll = t->Draw(observ,basic_cut+isEEM_+isFFP+isLLL);

	EME_pff = t->Draw(observ,basic_cut+isEME_+isPFF);
	EME_fpf = t->Draw(observ,basic_cut+isEME_+isFPF);
	EME_ffp = t->Draw(observ,basic_cut+isEME_+isFFP);

	EME_pff_tll = t->Draw(observ,basic_cut+isEME_+isPFF+isTLL);
	EME_fpf_ltl = t->Draw(observ,basic_cut+isEME_+isFPF+isLTL);
	EME_ffp_llt = t->Draw(observ,basic_cut+isEME_+isFFP+isLLT);

	EME_pff_lll = t->Draw(observ,basic_cut+isEME_+isPFF+isLLL);
	EME_fpf_lll = t->Draw(observ,basic_cut+isEME_+isFPF+isLLL);
	EME_ffp_lll = t->Draw(observ,basic_cut+isEME_+isFFP+isLLL);

	MEE_pff = t->Draw(observ,basic_cut+isMEE_+isPFF);
	MEE_fpf = t->Draw(observ,basic_cut+isMEE_+isFPF);
	MEE_ffp = t->Draw(observ,basic_cut+isMEE_+isFFP);

	MEE_pff_tll = t->Draw(observ,basic_cut+isMEE_+isPFF+isTLL);
	MEE_fpf_ltl = t->Draw(observ,basic_cut+isMEE_+isFPF+isLTL);
	MEE_ffp_llt = t->Draw(observ,basic_cut+isMEE_+isFFP+isLLT);

	MEE_pff_lll = t->Draw(observ,basic_cut+isMEE_+isPFF+isLLL);
	MEE_fpf_lll = t->Draw(observ,basic_cut+isMEE_+isFPF+isLLL);
	MEE_ffp_lll = t->Draw(observ,basic_cut+isMEE_+isFFP+isLLL);

	//EEM - 2prompts
	EEM_ppf = t->Draw(observ,basic_cut+isEEM_+isPPF);
	EEM_pfp = t->Draw(observ,basic_cut+isEEM_+isPFP);
	EEM_fpp = t->Draw(observ,basic_cut+isEEM_+isFPP);

	//EME - 2prompts
	EME_ppf = t->Draw(observ,basic_cut+isEME_+isPPF);
	EME_pfp = t->Draw(observ,basic_cut+isEME_+isPFP);
	EME_fpp = t->Draw(observ,basic_cut+isEME_+isFPP);

	//MEE - 2prompts
	MEE_ppf = t->Draw(observ,basic_cut+isMEE_+isPPF);
	MEE_pfp = t->Draw(observ,basic_cut+isMEE_+isPFP);
	MEE_fpp = t->Draw(observ,basic_cut+isMEE_+isFPP);

	//no prompt/fake
	EEM_ppp = t->Draw(observ,basic_cut+isEEM+isPPP);
	EEM_fff = t->Draw(observ,basic_cut+isEEM+isFFF);

	//all
	EEM = t->Draw(observ,basic_cut+isEEM);

	cout << " ========= EEM ========= " << endl;
	float eem_pff = EEM_pff+EEM_fpf+EEM_ffp + EME_pff+EME_fpf+EME_ffp + MEE_pff+MEE_fpf+MEE_ffp ;  
	float eem_ppf = EEM_ppf+EEM_pfp+EEM_fpp + EME_ppf+EME_pfp+EME_fpp + MEE_ppf+MEE_pfp+MEE_fpp ;  
	float eem_lll = EEM_lll+EME_lll+MEE_lll;
	cout << "Counts of EEM: FFF(" << EEM_fff<< "), PFF(" <<eem_pff <<"), PFF("<< eem_pff <<"), PPP("<<EEM_ppp <<") : "<< EEM<< ", LLL(" << eem_lll <<")" << endl; 
	cout << "	--1 prompt-- :  "<< endl;
	cout << "	p(L):   "<< endl;
	cout << "       EEM PFF LLL (prompt mu) : " << EEM_pff_lll << endl;
	cout << "       EEM FPF LLL (prompt el) : " << EEM_fpf_lll << endl;
	cout << "       EEM FFP LLL (prompt el) : " << EEM_ffp_lll << endl;
	cout << "-" << endl;
	cout << "       EME PFF LLL (prompt el) : " << EME_pff_lll << endl;
	cout << "       EME FPF LLL (prompt mu) : " << EME_fpf_lll << endl;
	cout << "       EME FFP LLL (prompt el) : " << EME_ffp_lll << endl;
	cout << "-" << endl;
	cout << "       MEE PFF LLL (prompt el) : " << MEE_pff_lll << endl;
	cout << "       MEE FPF LLL (prompt el) : " << MEE_fpf_lll << endl;
	cout << "       MEE FFP LLL (prompt mu) : " << MEE_ffp_lll << endl;
	cout << "" << endl;
	cout << "	p(T):   "<< endl;
	cout << "       EEM PFF TLL (prompt mu) : " << EEM_pff_tll << endl;
	cout << "       EEM FPF LTL (prompt el) : " << EEM_fpf_ltl << endl;
	cout << "       EEM FFP LLT (prompt el) : " << EEM_ffp_llt << endl;
	cout << "-" << endl;
	cout << "       EME PFF TLL (prompt el) : " << EME_pff_tll << endl;
	cout << "       EME FPF LTL (prompt mu) : " << EME_fpf_ltl << endl;
	cout << "       EME FFP LLT (prompt el) : " << EME_ffp_llt << endl;
	cout << "-" << endl;
	cout << "       MEE PFF TLL (prompt el) : " << MEE_pff_tll << endl;
	cout << "       MEE FPF LTL (prompt el) : " << MEE_fpf_ltl << endl;
	cout << "       MEE FFP LLT (prompt mu) : " << MEE_ffp_llt << endl;
	cout << "       ---------------------  " << endl;
	float eem_e_pL = EEM_fpf_lll+EEM_ffp_lll+EME_pff_lll+EME_ffp_lll+MEE_pff_lll+MEE_fpf_lll;
	float eem_e_pT = EEM_fpf_ltl+EEM_ffp_llt+EME_pff_tll+EME_ffp_llt+MEE_pff_tll+MEE_fpf_ltl;
	float eem_e_PR = eem_e_pT / ( eem_e_pT + eem_e_pL );
	cout << "       prompt el p(T)          : " << eem_e_pT << endl;
	cout << "       prompt el p(L)          : " << eem_e_pL << endl;
	cout << "       		el prompt rate  : " << eem_e_pT / ( eem_e_pT + eem_e_pL ) << endl;

	float eem_m_pL = EEM_pff_lll+EME_fpf_lll+MEE_ffp_lll;
	float eem_m_pT = EEM_pff_tll+EME_fpf_ltl+MEE_ffp_llt;
	float eem_m_PR = eem_m_pT / ( eem_m_pT + eem_m_pL );
	cout << "       prompt mu p(T)          : " << eem_m_pT<<endl;
	cout << "       prompt mu p(L)          : " << eem_m_pL<<endl;
	cout << "       		mu prompt rate  : " << eem_m_pT / ( eem_m_pT + eem_m_pL ) << endl;
	//===========EMM==============

	EMM_lll = t->Draw(observ,basic_cut+isEMM_+isLLL);
	MEM_lll = t->Draw(observ,basic_cut+isMEM_+isLLL);
	MME_lll = t->Draw(observ,basic_cut+isMME_+isLLL);

	//1prompt
	EMM_pff = t->Draw(observ,basic_cut+isEMM_+isPFF);
	EMM_fpf = t->Draw(observ,basic_cut+isEMM_+isFPF);
	EMM_ffp = t->Draw(observ,basic_cut+isEMM_+isFFP);

	EMM_pff_tll = t->Draw(observ,basic_cut+isEMM_+isPFF+isTLL);
	EMM_fpf_ltl = t->Draw(observ,basic_cut+isEMM_+isFPF+isLTL);
	EMM_ffp_llt = t->Draw(observ,basic_cut+isEMM_+isFFP+isLLT);

	EMM_pff_lll = t->Draw(observ,basic_cut+isEMM_+isPFF+isLLL);
	EMM_fpf_lll = t->Draw(observ,basic_cut+isEMM_+isFPF+isLLL);
	EMM_ffp_lll = t->Draw(observ,basic_cut+isEMM_+isFFP+isLLL);

	MEM_pff = t->Draw(observ,basic_cut+isMEM_+isPFF);
	MEM_fpf = t->Draw(observ,basic_cut+isMEM_+isFPF);
	MEM_ffp = t->Draw(observ,basic_cut+isMEM_+isFFP);

	MEM_pff_tll = t->Draw(observ,basic_cut+isMEM_+isPFF+isTLL);
	MEM_fpf_ltl = t->Draw(observ,basic_cut+isMEM_+isFPF+isLTL);
	MEM_ffp_llt = t->Draw(observ,basic_cut+isMEM_+isFFP+isLLT);

	MEM_pff_lll = t->Draw(observ,basic_cut+isMEM_+isPFF+isLLL);
	MEM_fpf_lll = t->Draw(observ,basic_cut+isMEM_+isFPF+isLLL);
	MEM_ffp_lll = t->Draw(observ,basic_cut+isMEM_+isFFP+isLLL);

	MME_pff = t->Draw(observ,basic_cut+isMME_+isPFF);
	MME_fpf = t->Draw(observ,basic_cut+isMME_+isFPF);
	MME_ffp = t->Draw(observ,basic_cut+isMME_+isFFP);

	MME_pff_tll = t->Draw(observ,basic_cut+isMME_+isPFF+isTLL);
	MME_fpf_ltl = t->Draw(observ,basic_cut+isMME_+isFPF+isLTL);
	MME_ffp_llt = t->Draw(observ,basic_cut+isMME_+isFFP+isLLT);

	MME_pff_lll = t->Draw(observ,basic_cut+isMME_+isPFF+isLLL);
	MME_fpf_lll = t->Draw(observ,basic_cut+isMME_+isFPF+isLLL);
	MME_ffp_lll = t->Draw(observ,basic_cut+isMME_+isFFP+isLLL);

	//EMM - 2prompts
	EMM_ppf = t->Draw(observ,basic_cut+isEMM_+isPPF);
	EMM_pfp = t->Draw(observ,basic_cut+isEMM_+isPFP);
	EMM_fpp = t->Draw(observ,basic_cut+isEMM_+isFPP);

	//MEM - 2prompts
	MEM_ppf = t->Draw(observ,basic_cut+isMEM_+isPPF);
	MEM_pfp = t->Draw(observ,basic_cut+isMEM_+isPFP);
	MEM_fpp = t->Draw(observ,basic_cut+isMEM_+isFPP);

	//MME - 2prompts
	MME_ppf = t->Draw(observ,basic_cut+isMME_+isPPF);
	MME_pfp = t->Draw(observ,basic_cut+isMME_+isPFP);
	MME_fpp = t->Draw(observ,basic_cut+isMME_+isFPP);

	//no prompt/fake
	EMM_ppp = t->Draw(observ,basic_cut+isEMM+isPPP);
	EMM_fff = t->Draw(observ,basic_cut+isEMM+isFFF);

	//all
	EMM = t->Draw(observ,basic_cut+isEMM);

	cout << " ========= EMM ========= " << endl;
	float emm_pff = EMM_pff+EMM_fpf+EMM_ffp + MEM_pff+MEM_fpf+MEM_ffp + MME_pff+MME_fpf+MME_ffp ;  
	float emm_ppf = EMM_ppf+EMM_pfp+EMM_fpp + MEM_ppf+MEM_pfp+MEM_fpp + MME_ppf+MME_pfp+MME_fpp ;  
	float emm_lll = EMM_lll+MEM_lll+MME_lll;
	cout << "Counts of EMM: FFF(" << EMM_fff<< "), PFF(" <<emm_pff <<"), PFF("<< emm_pff <<"), PPP("<<EMM_ppp <<") : "<< EMM<< ", LLL(" << emm_lll <<")" << endl; 
	cout << "	--1 prompt-- :  "<< endl;
	cout << "	p(L):   "<< endl;
	cout << "       EMM PFF LLL (prompt mu) : " << EMM_pff_lll << endl;
	cout << "       EMM FPF LLL (prompt el) : " << EMM_fpf_lll << endl;
	cout << "       EMM FFP LLL (prompt el) : " << EMM_ffp_lll << endl;
	cout << "-" << endl;
	cout << "       MEM PFF LLL (prompt el) : " << MEM_pff_lll << endl;
	cout << "       MEM FPF LLL (prompt mu) : " << MEM_fpf_lll << endl;
	cout << "       MEM FFP LLL (prompt el) : " << MEM_ffp_lll << endl;
	cout << "-" << endl;
	cout << "       MME PFF LLL (prompt el) : " << MME_pff_lll << endl;
	cout << "       MME FPF LLL (prompt el) : " << MME_fpf_lll << endl;
	cout << "       MME FFP LLL (prompt mu) : " << MME_ffp_lll << endl;
	cout << "" << endl;
	cout << "	p(T):   "<< endl;
	cout << "       EMM PFF TLL (prompt mu) : " << EMM_pff_tll << endl;
	cout << "       EMM FPF LTL (prompt el) : " << EMM_fpf_ltl << endl;
	cout << "       EMM FFP LLT (prompt el) : " << EMM_ffp_llt << endl;
	cout << "-" << endl;
	cout << "       MEM PFF TLL (prompt el) : " << MEM_pff_tll << endl;
	cout << "       MEM FPF LTL (prompt mu) : " << MEM_fpf_ltl << endl;
	cout << "       MEM FFP LLT (prompt el) : " << MEM_ffp_llt << endl;
	cout << "-" << endl;
	cout << "       MME PFF TLL (prompt el) : " << MME_pff_tll << endl;
	cout << "       MME FPF LTL (prompt el) : " << MME_fpf_ltl << endl;
	cout << "       MME FFP LLT (prompt mu) : " << MME_ffp_llt << endl;
	cout << "       ---------------------  " << endl;
	float emm_e_pL = EMM_fpf_lll+EMM_ffp_lll+MEM_pff_lll+MEM_ffp_lll+MME_pff_lll+MME_fpf_lll;
	float emm_e_pT = EMM_fpf_ltl+EMM_ffp_llt+MEM_pff_tll+MEM_ffp_llt+MME_pff_tll+MME_fpf_ltl;
	float emm_e_PR = emm_e_pT / ( emm_e_pT + emm_e_pL );
	cout << "       prompt el p(T)          : " << emm_e_pT << endl;
	cout << "       prompt el p(L)          : " << emm_e_pL << endl;
	cout << "       		el prompt rate  : " << emm_e_pT / ( emm_e_pT + emm_e_pL ) << endl;

	float emm_m_pL = EMM_pff_lll+MEM_fpf_lll+MME_ffp_lll;
	float emm_m_pT = EMM_pff_tll+MEM_fpf_ltl+MME_ffp_llt;
	float emm_m_PR = emm_m_pT / ( emm_m_pT + emm_m_pL );
	cout << "       prompt mu p(T)          : " << emm_m_pT<<endl;
	cout << "       prompt mu p(L)          : " << emm_m_pL<<endl;
	cout << "       		mu prompt rate  : " << emm_m_pT / ( emm_m_pT + emm_m_pL ) << endl;

// }
	//===========MMM==============
	
	MMM_ttt = t->Draw(observ,basic_cut+isMMM+" &&  isTTT " );
	MMM_lll = t->Draw(observ,basic_cut+isMMM+" &&  isLLL " );

	//1prompt
	MMM_pff = t->Draw(observ,basic_cut+isMMM+" &&  isPFF " );
	MMM_fpf = t->Draw(observ,basic_cut+isMMM+" &&  isFPF " );
	MMM_ffp = t->Draw(observ,basic_cut+isMMM+" &&  isFFP " );

	MMM_pff_tll = t->Draw(observ,basic_cut+isMMM+" &&  isPFF && isTLL " );
	MMM_fpf_ltl = t->Draw(observ,basic_cut+isMMM+" &&  isFPF && isLTL " );
	MMM_ffp_llt = t->Draw(observ,basic_cut+isMMM+" &&  isFFP && isLLT " );

	MMM_pff_lll = t->Draw(observ,basic_cut+isMMM+" &&  isPFF && isLLL " );
	MMM_fpf_lll = t->Draw(observ,basic_cut+isMMM+" &&  isFPF && isLLL " );
	MMM_ffp_lll = t->Draw(observ,basic_cut+isMMM+" &&  isFFP && isLLL " );

	//2 prompts (1 fake)
	MMM_ppf = t->Draw(observ,basic_cut+isMMM+" && ( isPPF )" );
	MMM_pfp = t->Draw(observ,basic_cut+isMMM+" && ( isPFP )" );
	MMM_fpp = t->Draw(observ,basic_cut+isMMM+" && ( isFPP )" );
	
	//3 prompts , 3 fakes
	MMM_ppp = t->Draw(observ,basic_cut+isMMM+isPPP);
	MMM_fff = t->Draw(observ,basic_cut+isMMM+isFFF);

	//All
	MMM = t->Draw(observ,basic_cut+isMMM);

	//
	cout << " ========= MMM ========= " << endl;
	cout << "Counts of MMM: FFF(" << MMM_fff<< "), PFF(" <<MMM_pff+MMM_fpf+MMM_ffp <<"), PPF("<< MMM_ppf+MMM_pfp+MMM_fpp<<"), PPP("<< MMM_ppp <<") : "<< MMM<<", TTT("<< MMM_ttt << ")"<<endl; 
	cout << "	--1 prompt /2 fakes:   "<< endl;
	cout << "       IsLLL p(L)  : " << MMM_pff_lll+MMM_fpf_lll+MMM_ffp_lll << endl;
	cout << "       IsTLL p(T) : " << MMM_pff_tll+MMM_fpf_ltl+MMM_ffp_llt << endl;
	float mmm_pT = (MMM_pff_tll+MMM_fpf_ltl+MMM_ffp_llt)*1.0;
	float mmm_pL = (MMM_pff_lll+MMM_fpf_lll+MMM_ffp_lll )*1.0;
	float mmm_PR = mmm_pT / ( mmm_pT  + mmm_pL ) ;
	cout << "       		mu prompt rate  : " << mmm_PR << endl;
	
	//===========ALL==============
	
	cout << " ========= ALL ========= " << endl;

	ALL_pff = t->Draw(observ,basic_cut+" && ( isPFF || isFPF || isFFP)" );
	ALL_ppf = t->Draw(observ,basic_cut+" && ( isPPF || isPFP || isFPP)" );
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
	cout << "el prompt rate (EEE): " << eee_PR << endl;
	cout << "el prompt rate (EEM): " << eem_e_PR << endl;
	cout << "el prompt rate (EMM): " << emm_e_PR << endl;
	cout << "-" << endl;
	cout << "		el prompt rate (EEE+EEM+EMM) : " << (eee_pT +  eem_e_pT +  emm_e_pT) / ( eee_pT  + eee_pL + eem_e_pT + eem_e_pL + emm_e_pT + emm_e_pL ) <<endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << "mu prompt rate (EEM): " << eem_m_PR << endl;
	cout << "mu prompt rate (EMM): " << emm_m_PR << endl;
	cout << "mu prompt rate (MMM): " << mmm_PR << endl;
	cout << "-" << endl;
	cout << "		mu prompt rate (MMM+EMM+EEM) : " << (mmm_pT +  eem_m_pT +  emm_m_pT) / ( mmm_pT  + mmm_pL + eem_m_pT + eem_m_pL + emm_m_pT + emm_m_pL ) <<endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << "NOTE: prompt rate = p(T) / [p(T)+p(L)] " << endl;
	cout << "" << endl;
	
	gApplication->Terminate();
	
}
