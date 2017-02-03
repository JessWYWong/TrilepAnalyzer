#define post_C

#include <TStyle.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TH2.h>
#include <TH3.h>
#include "TAxis.h"
#include "TF1.h"
#include "TLine.h"
#include "TColor.h"
#include <THStack.h>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TLatex.h"
#include <iostream>
#include <fstream>
#include "interface/DMCclass_list.h"
#include "interface/DMCblock.h"
#include "interface/stringmap.h"
#include "interface/controlpannel.h"
#include "interface/utilities.h"
#include "interface/CMSStyle.C"
#include "interface/KinematicVar.h"
#include <time.h> 
//#include <assert.h> //assert isn't sufficiently assertive. It doesn't actually stop the program. 

using namespace std;
using namespace controlpannel;
typedef stringmap<TH1F*> histmap;
typedef stringmap<histmap*> histtable;
typedef stringmap<TH2F*> histmap2D;
typedef stringmap<histmap2D*> histtable2D;

struct thetaSigFile{
	thetaSigFile(string _filename, double _bWbr, double _tHbr):filename(_filename),bWbr(_bWbr),tHbr(_tHbr){}
	string filename;
	double bWbr;
	double tHbr;
};

////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
TH1F* extrackBkg(TH2F* bkg_hist);
TH1F* make_ratio_uncertainty_hist(TH1F* data, TH1F* bkg);
void fix_negatives(TH1F* hist, bool verbose=false);
void fix_negativesX(TH2F* hist, bool verbose=false);
bool has_negatives(TH1F* hist);
bool has_negatives(TH2F* hist);
bool Check_binning(TH1F* A, TH1F* B, string complaint);
bool Check_binning(TH2F* A, TH2F* B, string complaint);
bool Check_binning(TAxis* A,TAxis* B,string complaint);//if one of the TAxis comes from a THStack, make sure to call Draw before calling this.
TH1F* patchYield(TH1F* yield, LabelKinVars allkinvar_stringmap); //NEEDS TEST
string ThetaFileNameSig(string directory, string classname, double bWbr, double tHbr);//makes filenames for signal br scan theta files..
string MakeThetaRootFile_Yield_nonsignal(histtable htable, histmap2D* histmapbkg, histtable2D htable2D, string dir, string dataClassName, 
	std::vector<DMCclass*> vBkgClasses,
	std::vector<DMCclass*> vBkgClassesUP, std::vector<DMCclass*> vBkgClassesDOWN, 
	std::vector<DMCclass*> vBkgClassesJERup, std::vector<DMCclass*> vBkgClassesJERdown, 
	std::vector<DMCclass*> vBkgClassesJECup, std::vector<DMCclass*> vBkgClassesJECdown,
	stringmap<KinematicVar*>* kinvar_stringmap);
string MakeThetaRootFile_Yield_simple_signal(histtable htable, histmap2D* histmapbkg, histtable2D htable2D, string dir, string dataClassName,stringmap<KinematicVar*>* kinvar_stringmap);
std::vector<thetaSigFile*> MakeThetaRootFile_Yield_signalScan(stringmap<std::vector<TH1F*>> Signal_yields,  std::vector<DMCclass*> vSigClassesAll,string dir, int nBRslices);
string MakeThetaCounts(histtable htable, histmap2D* histmapbkg, string SigClassToUse, std::vector<DMCclass*> vBkgClasses);
TH1F* brRescale( std::vector<TH1F*> hists, float bWbr, float tHbr, string outname);
float get_bZbr(float bWbr, float tHbr);
void Assert(bool truth_or_death);
string  Steralized_Class_Name(string dirty_class_name);
//void Fix_Yield_Binning(TH1F* yield, KinematicVar* kinvar, bool include_OSDL1=true, bool include_OSDL2=false, bool include_SSDL=true);
TH1F* Fix_Yield_Binning(TH1F* yield, KinematicVar* kinvar, bool include_OSDL1=true, bool include_OSDL2=false, bool include_SSDL=true);
void bump_em(TH1F* h_yield, float bump_term,bool include_OSDL1=true, bool include_OSDL2=false, bool include_SSDL=true);
void bump_ee(TH1F* h_yield, float bump_term,bool include_OSDL1=true, bool include_OSDL2=false, bool include_SSDL=true);
void bump_mm(TH1F* h_yield, float bump_term,bool include_OSDL1=true, bool include_OSDL2=false, bool include_SSDL=true);

////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
void Assert(bool truth_or_death){
    if(not truth_or_death){
	cout<<"Process euthanize by Assert"<<endl;
	std::terminate();
    }
}

void post(){
	CMSStyle();
	std::vector<string> SigtoInclude;
	std::vector<string> plotnames; 
	std::vector<string> plotnames2D; 
	std::vector<string> bkgplotnames; 
	LabelKinVars allkinvar_stringmap = setupAllKinematicVar(); //the entire universe of kinvars
	stringmap<KinematicVar*> chosenkinvar_stringmap; // map from plotname to the corresponding kinvar. 

	///////////////////////////// Switcehs //////////////////////////////////////
	//Most switches are on the control pannel. 
	bool saveImages = false;
	bool draw_ddbkg  = true;
	bool use_ddbkg_in_ratio = true;

	bool makeLimitFile = true;

	bool makeStackPlots_lin = false;
	bool makeStackPlots_lin_ratio = false;

	bool makeStackPlots_log = false;
	bool makeStackPlots_log_ratio = false;

	///////////////////////////// Lists  //////////////////////////////////////
	namedstring plotdirs;
	plotdirs.set("c", plotsdirC);
	plotdirs.set("root", plotsdirroot);
	plotdirs.set("jpg", plotsdirjpg );
	plotdirs.set("pdf", plotsdirpdf );
	plotdirs.set("png", plotsdirpng );
	plotdirs.set("gif", plotsdirgif );
	plotdirs.set("eps", plotsdireps );


	SigtoInclude.push_back(string("TpTp700")+(T50ns_F25ns?"s":"f"));
	SigtoInclude.push_back(string("TpTp900")+(T50ns_F25ns?"s":"f"));
	string dataClassName = string("Data2lep")+(T50ns_F25ns?"s":"f");

		//MAKE A LIST OF ALL THE PLOT NAMES TO LOAD IN: "plotnames", AND BKG PLOT NAMES "bkgplotnames"
		//Map the plotname or bkgplotname  to the kinvar in chosenkinvar_stringmap.set
	try{
	    //Special plots to load in
	    plotnames.push_back("h_HT_OSDL1sansH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_OSDL1sansHlb"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_OSDL1sansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_OSDL2sansH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_OSDL2sansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_SSDLsansH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    plotnames.push_back("h_HT_SSDLsansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("HT",1));

	    plotnames.push_back("h_STSSDL_sansST"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_OSDL1sansS"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_OSDL1sansSlb"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_OSDL1sansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_OSDL2sansS"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_OSDL2sansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    plotnames.push_back("h_ST_SSDLsansSH"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("ST",1));

	    plotnames.push_back("h_nBm_OSDL2sansB"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("nBm",1));
	    plotnames.push_back("h_BTm_OSDL2sansB"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("BTm",1));
	    plotnames.push_back("h_MinMlb_OSDL1sanslb"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("MinMlb",1));
	    plotnames.push_back("h_yield"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("yield",1));//subsequent stuff depends on this.
	    plotnames.push_back("h_yieldsum"); chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable("yieldsum",1));

		//Special background plots to load in	
	    bkgplotnames.push_back("b_HT_OSDL1sansH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_OSDL1sansHlb"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_OSDL1sansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_OSDL2sansH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_OSDL2sansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_SSDLsansH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));
	    bkgplotnames.push_back("b_HT_SSDLsansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("HT",1));

	    bkgplotnames.push_back("b_STSSDL_sansST"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_OSDL1sansS"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_OSDL1sansSlb"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_OSDL1sansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_OSDL2sansS"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_OSDL2sansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));
	    bkgplotnames.push_back("b_ST_SSDLsansSH"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("ST",1));

	    bkgplotnames.push_back("b_nBm_OSDL2sansB"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("nBm",1));
	    bkgplotnames.push_back("b_BTm_OSDL2sansB"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("BTm",1));
	    bkgplotnames.push_back("b_MinMlb_OSDL1sanslb"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("MinMlb",1));
	    bkgplotnames.push_back("b_yield"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("yield",1));
	    bkgplotnames.push_back("b_yieldsum"); chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable("yieldsum",1));

		//load 2D plots
	    plotnames2D.push_back("s_yield"); chosenkinvar_stringmap.set(plotnames2D.back(),allkinvar_stringmap->get_throwable("yield",1));
	    //need to load s_yield; s_yield is like b_yield in that they are both TH2's, but b_yield is for data only. s_yield is for MC. 

	    for (int iTopo = 0; iTopo<nEventTopologies; iTopo++) {
		for (int kKinVar = 0; kKinVar < nKinemVars_all; kKinVar++) {

		    //make a list of the names of all the grid plots
		    plotnames.push_back( string("h_")+s_KinemVars_all[kKinVar]+s_EventTopology[iTopo]);
		    chosenkinvar_stringmap.set(plotnames.back(),allkinvar_stringmap->get_throwable(s_KinemVars_all[kKinVar],2)); //map kinvars to plotname

		    //make a list of the names of all the background grid plots
		    bkgplotnames.push_back( string("b_")+s_KinemVars_all[kKinVar]+s_EventTopology[iTopo]);
		    chosenkinvar_stringmap.set(bkgplotnames.back(),allkinvar_stringmap->get_throwable(s_KinemVars_all[kKinVar],3)); //map kinvars to plotname
		}//end for every kinvar
	    }//end for every topo
	}//end list all special plot names
	catch(std::pair <std::string,int> errorpair){
	    switch(errorpair.second ){
		case 1: cerr<<"Stringmap Error! While setting up specail plot names. Invalid string key "<<errorpair.first<< " sought in allkinvar_stringmap"<<endl; break;
		case 2: cerr<<"Stringmap Error! While setting up general plot names. Invalid string key "<<errorpair.first<< " sought in allkinvar_stringmap"<<endl;
		case 3: cerr<<"Stringmap Error! While setting up general plot names. Invalid string key "<<errorpair.first<< " sought in allkinvar_stringmap"<<endl;
	    }//end switch
	    std::terminate();
	}

	cout<<"Start DMC class setup:"<<endl;
	//add to the list  a list of all the grid plots names to intake, then list all the bkg plots. 

	//Make a list vClasses of all the classes to run
	DMCclass* dataClass = setupDMCclass( dataClassName);
	std::vector<DMCclass*> vBkgClasses     = MCbkgDMCclasses(nominal,nominal,nominal,T50ns_F25ns);//nominal bkgs that will go on the plot. 
	std::vector<DMCclass*> vBkgClassesDOWN = MCbkgDMCclasses(down,nominal,nominal,T50ns_F25ns);
	std::vector<DMCclass*> vBkgClassesUP   = MCbkgDMCclasses(up  ,nominal,nominal,T50ns_F25ns);
	std::vector<DMCclass*> vBkgClassesJERup     = MCbkgDMCclasses(nominal,up  ,nominal,T50ns_F25ns);
	std::vector<DMCclass*> vBkgClassesJERdown   = MCbkgDMCclasses(nominal,down,nominal,T50ns_F25ns);
	std::vector<DMCclass*> vBkgClassesJECup     = MCbkgDMCclasses(nominal,nominal,up  ,T50ns_F25ns);
	std::vector<DMCclass*> vBkgClassesJECdown   = MCbkgDMCclasses(nominal,nominal,down,T50ns_F25ns);

	std::vector<DMCclass*> vSigClassesAll = MCTpTpsigDMCclass(T50ns_F25ns);//all the signal classes, used for limits. 

	std::vector<DMCclass*> vSigClasses_JERup= MCTpTpsigDMCclass(T50ns_F25ns,up);
	std::vector<DMCclass*> vSigClasses_JERdown= MCTpTpsigDMCclass(T50ns_F25ns,down);
	std::vector<DMCclass*> vSigClasses_JECup= MCTpTpsigDMCclass(T50ns_F25ns,nominal,up);
	std::vector<DMCclass*> vSigClasses_JECdown= MCTpTpsigDMCclass(T50ns_F25ns,nominal,down);
	for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JERup.begin();iclass< vSigClasses_JERup.end();iclass++){ vSigClassesAll.push_back((*iclass)); }
	for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JECup.begin();iclass< vSigClasses_JECup.end();iclass++){ vSigClassesAll.push_back((*iclass)); }
	for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JERdown.begin();iclass< vSigClasses_JERdown.end();iclass++){ vSigClassesAll.push_back((*iclass)); }
	for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JECdown.begin();iclass< vSigClasses_JECdown.end();iclass++){ vSigClassesAll.push_back((*iclass)); }

	//vClassesAll
	std::vector<DMCclass*> vClassesAll = allMCbkgClasses(T50ns_F25ns); //to be used for looping. 
	for(std::vector<DMCclass*>::iterator iclass = vSigClassesAll.begin();iclass< vSigClassesAll.end();iclass++) vClassesAll.push_back((*iclass));
	vClassesAll.push_back(dataClass);

	//vClasses and vSigClasses; 
	std::vector<DMCclass*> vSigClasses; //The signal classes to go on the plots
	std::vector<DMCclass*> vClasses; //ALL classes to go on plots. = a copy of vBkgClasses with data and selected MC appended. 
	//copy nominal backgrounds to vClass: 
	for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass< vBkgClasses.end();iclass++){ vClasses.push_back((*iclass)); }
	//find the signal classes you want on the plots. add them to vSigClasses and vClasses. 
	for(std::vector<string>::iterator istr=SigtoInclude.begin();istr<SigtoInclude.end();istr++){ //for all the chosen siganl classes. 
	    for(std::vector<DMCclass*>::iterator iclass = vSigClassesAll.begin();iclass< vSigClassesAll.end();iclass++){ //look @ all sig classes
		if((*iclass)->name.compare(*istr) ==0){ //if it's one of the signal classes you wanted. 
		    vSigClasses.push_back(*iclass);//add to the list of desired signal classes
		    vClasses.push_back(*iclass); //and add it to the list of all classes for the plots .
		    break;
		}
	    }
	}
	vClasses.push_back(dataClass);

//	for(std::vector<DMCclass*>::iterator iclass = vClasses.begin();iclass< vClasses.end();iclass++) vClassesAll.push_back((*iclass));
//	for(std::vector<DMCclass*>::iterator iclass = vBkgClassesUP.begin();iclass< vBkgClassesUP.end();iclass++) vClassesAll.push_back((*iclass));
//	for(std::vector<DMCclass*>::iterator iclass = vBkgClassesDOWN.begin();iclass< vBkgClassesDOWN.end();iclass++) vClassesAll.push_back((*iclass));

	stringmap<DMCclass*>* mClasses =  makemap(vClasses);
	stringmap<DMCclass*>* mClassesAll =  makemap(vClassesAll);

	
	    ///////////////////////////// File Work ///////////////////////////////////////

	    ////////////////////////// LOAD MAIN HISTOGRAMS ///////////////////////////////

	//load in all the histograms from all the files. 
	cout<<"Start loading plots from files"<<endl;
	histtable htable; //[vClass name][plotname]
	histtable2D htable2D;//[vClass name][plot name]
	std::vector<TFile*> vFiles;
	int start_of_data_in_vFiles=-1;//will hold the index of vFiles of the first data file. 
	int start_of_signal_in_vFiles=-1;//will hold the index of vFiles of the first data file. 
	for(std::vector<DMCclass*>::iterator iclass = vClassesAll.begin();iclass<vClassesAll.end();iclass++){ //for every dmc class. 
		cout<<"loading for "<<(*iclass)->name<<endl;
		bool first_block_in_class = true; //tells if it's the first block in the iclass. 
		histmap* temphistmap = new histmap();
		histmap2D* temphistmap2D = new histmap2D();

		for(std::vector<DMCblock*>::iterator iblock = (*iclass)->blocks.begin();iblock<(*iclass)->blocks.end();iblock++){ //for every block
			cout<<"    loading for "<<(*iblock)->name<<endl;

			//if( (*iblock)->int_meta["JEC"] != 0 or (*iblock)->int_meta["JER"] != 0 ) continue; //first load only nominals. 

			if( not fileExists( (*iblock)->string_meta["EventLoopOutRoot"]) ){
			    cerr<<"Error! Cannot find EventLoop file "<<(*iblock)->string_meta["EventLoopOutRoot"]<< " for DMCblock "<<(*iblock)->name<<endl;
			    std::terminate();
			}

			vFiles.push_back(new TFile((*iblock)->string_meta["EventLoopOutRoot"].c_str(), "READ"));
			if((*iclass)->int_meta["isData"]==1   and start_of_data_in_vFiles   ==-1) start_of_data_in_vFiles = vFiles.size()-1;//note which file the data starts on.
			if((*iclass)->int_meta["isSignal"]==1 and start_of_signal_in_vFiles ==-1){
			    start_of_signal_in_vFiles = vFiles.size()-1;//note which file the signal starts on.
				cout<<"setting start_of_signal_in_vFiles to "<<start_of_signal_in_vFiles<<" which is "<<vFiles.back()->GetName()<<" = "<<vFiles[start_of_signal_in_vFiles]->GetName()<<endl;
			}
			vFiles.back()->cd();

	

			///LOAD 1D PLOTS
			for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
				if(not vFiles.back()->GetListOfKeys()->Contains((*iplot).c_str()) ){
				    cerr<<"Error! Cannot find plot "<<*iplot<<" in file "<<(*iblock)->string_meta["EventLoopOutRoot"]<< " for DMCblock "<<(*iblock)->name<<endl;
				    std::terminate();
				}
				//cout<<"On class "<<(*iclass)->name<<" fetching "<<*iplot<<endl;

                        	TH1F* temp = (TH1F*)vFiles.back()->Get((*iplot).c_str());//
				TH1F* temp2;
				if(first_block_in_class) temp2 = (TH1F*)temp->Clone((*iplot + "_" + (*iclass)->name ).c_str());
				else           temp2 = (TH1F*)temp->Clone((*iplot + "_" + (*iblock)->name ).c_str());

				AddOverflow(temp2);
				fix_negatives(temp2);

				if((*iblock)->isMC) temp2->Scale(Integrated_Luminosity_Data*1000.0*(*iblock)->cs_pb/((*iblock)->NGenPoints));

				try{
				    KinematicVar* thiskinvar = chosenkinvar_stringmap.get_throwable(*iplot,2);

					//rebin histogram
				    /*if( thiskinvar->useCustomReBinning) 
					temp2 = (TH1F*)temp2->Rebin(thiskinvar->nbins_rebin / thiskinvar->nbins, (string(temp2->GetName())+"_r").c_str(), thiskinvar->CustomReBinning );
				    else temp2 = (TH1F*)temp2->Rebin(thiskinvar->nbins_rebin, (string(temp2->GetName())+"_r").c_str() );
					*/
					//see Rebin documentation here: https://root.cern.ch/doc/master/classTH1.html#aff6520fdae026334bf34fa1800946790
					//attempt to set labels
					if(thiskinvar->tag.compare("HT") == 0) temp2 = (TH1F*)temp2->Rebin(50,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("ST") == 0) temp2 = (TH1F*)temp2->Rebin(3,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("MET") == 0) temp2 = (TH1F*)temp2->Rebin(12,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("BTm") == 0) temp2 = (TH1F*)temp2->Rebin(30,(string(temp2->GetName())+"_r").c_str());	
					//else if(thiskinvar->tag.compare("BTl") == 0) temp2 = (TH1F*)temp2->Rebin(30,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("MinMlb") == 0) temp2 = (TH1F*)temp2->Rebin(2,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("Mll") == 0) temp2 = (TH1F*)temp2->Rebin(2,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("LepT") == 0) temp2 = (TH1F*)temp2->Rebin(16,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("MSum") == 0) temp2 = (TH1F*)temp2->Rebin(10,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("LHT") == 0) temp2 = (TH1F*)temp2->Rebin(20,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("MSumovST") == 0) temp2 = (TH1F*)temp2->Rebin(4,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("MtSum") == 0) temp2 = (TH1F*)temp2->Rebin(25,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("lepPt") == 0) temp2 = (TH1F*)temp2->Rebin(4,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("jetPt") == 0) temp2 = (TH1F*)temp2->Rebin(8,(string(temp2->GetName())+"_r").c_str());	
					else if(thiskinvar->tag.compare("yield") == 0) temp2 = Fix_Yield_Binning(temp2, thiskinvar); 
					//else if(thiskinvar->tag.compare("yield") == 0) Fix_Yield_Binning(temp2, thiskinvar); 


				    temp2->SetTitle( thiskinvar->titles.c_str() );
				    temp2->SetXTitle( thiskinvar->xlabels.c_str() );
				    temp2->SetYTitle( "Events" );

				    if(first_block_in_class) temphistmap->set(*iplot,temp2); 
				    else{
					Check_binning(temphistmap->get_throwable(*iplot,3),temp2,"Main load binning check");
					temphistmap->get_throwable(*iplot,3)->Add(temp2); 
				    }
				    //cout<<"Class "<<(*iclass)->name<<" block "<<(*iblock)->name<<" plot "<<*iplot<<". Adding "<<temp2->Integral()<<" Sum: "<<
				    	//temphistmap->get_throwable(*iplot)->Integral()<<endl;
				}
				catch(std::pair <std::string,int> errorpair){
				    cerr<<"Stringmap Error! Invalid string key "<<errorpair.first<< " sought in temphistmap. Error code "<<errorpair.second<<endl;
				    std::terminate();
				}
				//cout<<"end "<<*iplot<<endl<<flush;

			} //for ever plot in the file 

			///LOAD 2D PLOTS
			for(std::vector<string>::iterator iplot = plotnames2D.begin(); iplot<plotnames2D.end();iplot++){
				if(not vFiles.back()->GetListOfKeys()->Contains((*iplot).c_str()) ){
				    cerr<<"Error! Cannot find 2D plot "<<*iplot<<" in file "<<(*iblock)->string_meta["EventLoopOutRoot"]<< " for DMCblock "<<(*iblock)->name<<endl;
				    std::terminate();
				}

                        	TH2F* temp = (TH2F*)vFiles.back()->Get((*iplot).c_str());
				TH2F* temp2;
				if(first_block_in_class) temp2 = (TH2F*)temp->Clone((*iplot + "_" + (*iclass)->name ).c_str());
				else           temp2 = (TH2F*)temp->Clone((*iplot + "_" + (*iblock)->name ).c_str());

				AddOverflow(temp2);
				fix_negativesX(temp2);

				if((*iblock)->isMC) temp2->Scale(Integrated_Luminosity_Data*1000.0*(*iblock)->cs_pb/((*iblock)->NGenPoints));

				try{
				    KinematicVar* thiskinvar = chosenkinvar_stringmap.get_throwable(*iplot,2);

					//rebin histogram
					//if(thiskinvar->tag.compare("HT") == 0) temp2 = (TH2F*)temp2->Rebin(50,(string(temp2->GetName())+"_r").c_str());	
					//else if(thiskinvar->tag.compare("ST") == 0) temp2 = (TH2F*)temp2->Rebin(3,(string(temp2->GetName())+"_r").c_str());	
				    temp2->SetTitle( thiskinvar->titles.c_str() );
				    temp2->SetXTitle( thiskinvar->xlabels.c_str() );
				    //temp2->SetYTitle( thiskinvar->ylabels.c_str() );

				    if(first_block_in_class) temphistmap2D->set(*iplot,temp2); 
				    else{
					Check_binning(temphistmap2D->get_throwable(*iplot,3),temp2,"Main load binning check 2D");//xxx
					temphistmap2D->get_throwable(*iplot,3)->Add(temp2); 
				    }
				    //cout<<"Class "<<(*iclass)->name<<" block "<<(*iblock)->name<<" plot "<<*iplot<<". Adding "<<temp2->Integral()<<" Sum: "<<
				    //	temphistmap2D->get_throwable(*iplot)->Integral()<<endl;
				}
				catch(std::pair <std::string,int> errorpair){
				    cerr<<"Stringmap Error! Invalid string key "<<errorpair.first<< " sought in temphistmap2D. Error Code "<<errorpair.second<<endl;
				    std::terminate();
				}
			
			}//end load 2D plots.

			first_block_in_class = false;
			cout<<"    end block"<<endl<<flush;
			//cout<<"    end block   "<<(*iblock)->name<<endl<<flush;
		}//for every block in the class
		htable.set((*iclass)->name,temphistmap);
		htable2D.set((*iclass)->name,temphistmap2D);
	}//end for every DMCclass

	/*cout<<"Test bkgplotname behavior on repeated calling"<<endl;
	    for(std::vector<string>::iterator iplot = bkgplotnames.begin(); iplot<bkgplotnames.end();iplot++){ cout<<*iplot<<endl; }
	cout<<"2"<<endl<<flush;
	    for(std::vector<string>::iterator iplot = bkgplotnames.begin(); iplot<bkgplotnames.end();iplot++){ cout<<*iplot<<endl; }
	cout<<"3"<<endl<<flush;
	    for(std::vector<string>::iterator iplot = bkgplotnames.begin(); iplot<bkgplotnames.end();iplot++){ cout<<*iplot<<endl; }
	cout<<"Should be stable by now. if this isn't changig, then something is changing iplot as it gots."<<endl<<flush;*/
		//you know this produces nothing. 
	

	////////////////////////// Load signal yields /////////////////////////////////////
	        //construct a map of Signal_yields[iClass name in vSigClassesAll][iyield]
	        /*
	string h_yield_strings[nBByields] = {"h_yield_WW", "h_yield_WH", "h_yield_WZ", "h_yield_HH", "h_yield_HZ", "h_yield_ZZ"};
	        //0:WW, 1:WH, 2: WZ, 3: HH, 4: HZ, 5: ZZ 
	stringmap<std::vector<TH1F*>> Signal_yields;//only the ones that are meant to be included. 
	stringmap<std::vector<TH1F*>> Signal_yields_all;//for all the signal. 

	cout<<"Beginning to Fetch Yields"<<endl;
	for(std::vector<DMCclass*>::iterator iclass = vSigClassesAll.begin();iclass<vSigClassesAll.end();iclass++){ //for every dmc class. 
	    bool firstblock = true;
	    std::vector<TH1F*> hists; 

	    for(std::vector<DMCblock*>::iterator iblock = (*iclass)->blocks.begin();iblock<(*iclass)->blocks.end();iblock++){ //for every block
		int thisfile = start_of_signal_in_vFiles++; //appears to not be getting pointed to the right file.
		vFiles[thisfile]->cd();

		for(int iyield = 0;iyield<nBByields;iyield++){
		    if( string(vFiles[thisfile]->GetName()).compare((*iblock)->string_meta["EventLoopOutRoot"]) != 0){
			cerr<<"Yield File Getter has file mismatch: start_of_signal_in_vFiles indicates "<<vFiles[thisfile]->GetName()<<" but we want "<<(*iblock)->string_meta["EventLoopOutRoot"]<<endl;
			std::terminate();
		    } 
		    if(not vFiles[thisfile]->GetListOfKeys()->Contains((h_yield_strings[iyield]).c_str()) ){
			cerr<<"Error! in Get BByields: Cannot find plot "<<h_yield_strings[iyield]<<" in file "<<(*iblock)->string_meta["EventLoopOutRoot"]<< " for DMCblock "<<(*iblock)->name<<endl;
			std::terminate();
		    }

		    TH1F* temp = (TH1F*) vFiles[thisfile]->Get(h_yield_strings[iyield].c_str());
		    TH1F* temp2;
		    if(firstblock) temp2 = (TH1F*)temp->Clone((h_yield_strings[iyield] + "_" + (*iclass)->name ).c_str());
		    else           temp2 = (TH1F*)temp->Clone((h_yield_strings[iyield] + "_" + (*iblock)->name ).c_str());

		    temp2->Scale(Integrated_Luminosity_Data*1000.0*(*iblock)->cs_pb/((*iblock)->NGenPoints));

		    if(firstblock) hists.push_back(temp2);
		    else hists[iyield]->Add(temp2); 
		}//for every h_yield.
		firstblock = false;
	    }//end for every block
	    Signal_yields.set((*iclass)->name,hists);
	}//end for every signal class
*/



	////////////////////////// LOAD BACKGROUND HISTOGRAMS ///////////////////////////////
	cout<<"Start loading bkg plots from files"<<endl;
	//load histograms into histmapbkg

	bool first_block_in_class = true;
	histmap2D* histmapbkg = new histmap2D();
	for(std::vector<DMCblock*>::iterator iblock = dataClass->blocks.begin();iblock<dataClass->blocks.end();iblock++){ //for data
		if( (*iblock)->int_meta["JEC"] != 0 or (*iblock)->int_meta["JER"] != 0 ) continue; //first load only nominals. This should do nothing. 
	    int thisfile = start_of_data_in_vFiles++;
	    vFiles[thisfile]->cd();//cd to the data files. This only works if ddbkgclass only contains dataClass.

	    //cout<<"loading for block "<<(*iblock)->name<<endl;
	    for(std::vector<string>::iterator iplot = bkgplotnames.begin(); iplot<bkgplotnames.end();iplot++){
		if(not vFiles[thisfile]->GetListOfKeys()->Contains((*iplot).c_str()) ){
		    cerr<<"Error! Cannot find plot "<<*iplot<<" in file "<<(*iblock)->string_meta["EventLoopOutRoot"]<< " for DMCblock "<<(*iblock)->name<<endl;
		    std::terminate();
		}
		//cout<<"fetching "<<*iplot<<endl;

		TH2F* temp = (TH2F*)vFiles[thisfile]->Get((*iplot).c_str());///fix.
		//cout<<"bkg "<<(*iblock)->name<<" plot "<<*iplot<<" first bkg bin: "<<temp->GetBinContent(1,1)<<endl;
		TH2F* temp2;
		if(first_block_in_class) temp2 = (TH2F*)temp->Clone((*iplot + "_ddBkg").c_str());
		else{
		    temp2 = (TH2F*)temp->Clone((*iplot + "_" + (*iblock)->name ).c_str());
		    //cout<<"Try cloning under second round with "<<(*iplot) + "_" + (*iblock)->name<<endl<<flush;
		}

		AddOverflowX(temp2);
		fix_negativesX(temp2);
		if(has_negatives(hslice(temp2,1,2))) cout<<"hslice1 still sees negatives after they were fixed."<<endl;  //YYY this should be impossible, if it runs there's a problem! 
		if(has_negatives(extrackBkg(temp2))){
		    cout<<"Error! extrackBkg at "<<temp2->GetName()<<" has negatives. Go fix it."<<endl;
		    std::terminate();
		}

		if((*iblock)->isMC) cout<<"Warning: Somehow MC is getting into the data driven background load loop. Go fix it"<<endl; 

		try{
		    KinematicVar* thiskinvar = chosenkinvar_stringmap.get_throwable(*iplot,2);

		    if(thiskinvar->tag.compare("HT") == 0) temp2 = (TH2F*)temp2->RebinX(40,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("ST") == 0) temp2 = (TH2F*)temp2->RebinX(2,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("MET") == 0) temp2 = (TH2F*)temp2->RebinX(12,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("BTm") == 0) temp2 = (TH2F*)temp2->RebinX(30,(string(temp2->GetName())+"_r").c_str());	
		    //else if(thiskinvar->tag.compare("BTl") == 0) temp2 = (TH2F*)temp2->RebinX(30,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("MinMlb") == 0) temp2 = (TH2F*)temp2->RebinX(2,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("Mll") == 0) temp2 = (TH2F*)temp2->RebinX(2,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("LepT") == 0) temp2 = (TH2F*)temp2->RebinX(16,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("MSum") == 0) temp2 = (TH2F*)temp2->RebinX(10,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("LHT") == 0) temp2 = (TH2F*)temp2->RebinX(20,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("MSumovST") == 0) temp2 = (TH2F*)temp2->RebinX(4,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("MtSum") == 0) temp2 = (TH2F*)temp2->RebinX(25,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("lepPt") == 0) temp2 = (TH2F*)temp2->RebinX(4,(string(temp2->GetName())+"_r").c_str());	
		    else if(thiskinvar->tag.compare("jetPt") == 0) temp2 = (TH2F*)temp2->RebinX(8,(string(temp2->GetName())+"_r").c_str());	

		    temp2->SetTitle( thiskinvar->titles.c_str() );
		    temp2->SetXTitle( thiskinvar->xlabels.c_str() );
		    temp2->SetYTitle( "Events" );

			//change the plot name index to the same index system used by everything else. 
		    string thisbkgplotname(*iplot);//copy iplot
		    thisbkgplotname.replace(0,1,"h");//convert to the h_form for indexing. 
		    //cout<<"Check: iplot should be b_: "<<*iplot<<" and thisbkgplotname should be h_: "<<thisbkgplotname<<endl;
		    Assert(thisbkgplotname.compare(*iplot));

		    if(first_block_in_class) histmapbkg->set(thisbkgplotname,temp2); 
		    else {
			Check_binning(histmapbkg->get_throwable(thisbkgplotname,3),temp2,"Main load binning check");
			histmapbkg->get_throwable(thisbkgplotname,3)->Add(temp2); 
		    }
		}
		catch(std::pair <std::string,int> errorpair){
		    cerr<<"Stringmap Error! Invalid string key "<<errorpair.first<< " sought in histmapbkg. Error code "<<errorpair.second<<endl;
		    std::terminate();
		}//end catch 
	    } //for ever plot in the file 
	    first_block_in_class = false;
	}//for every block in the class

	////////////////////////////////////////////////////////
	//////////////////////// END FILEWORK //////////////////
	////////////////////////////////////////////////////////
	//finished loading all the plots into memory. 
	cout<<"Finished loading all plots from all files"<<endl;


	//Build 1D data driven backgrounds
	histmap histmapbkg1D; 		
	for(std::map<std::string, TH2F*>::iterator iplot=histmapbkg->begin(); iplot!=histmapbkg->end(); ++iplot) {
	    histmapbkg1D.set(iplot->first,  extrackBkg(iplot->second));
	}



	////////////////////////////////////////////////////////
	if(makeLimitFile){
	    cout<<"Try making bkg theta file"<<endl;
	    string thetafile = MakeThetaRootFile_Yield_nonsignal(htable, histmapbkg, htable2D,"test", dataClassName, vBkgClasses, vBkgClassesUP, vBkgClassesDOWN, vBkgClassesJERup, vBkgClassesJERdown, vBkgClassesJECup, vBkgClassesJECdown,allkinvar_stringmap);
	    cout<<"made theta file "<<thetafile<<endl;	

	    cout<<"Try making signal theta file"<<endl;
	    string thetafilesig = MakeThetaRootFile_Yield_simple_signal(htable, histmapbkg, htable2D,"test", dataClassName,allkinvar_stringmap);
	    cout<<"made theta file "<<thetafilesig<<endl;	

	}

	////////////////////////////////////////////////////////
	//////////////////////MAKE PLOTS////////////////////////
	////////////////////////////////////////////////////////

	//Run 2 has different rules for the plot decorations: 
	//no more integal sign, no more sqrt symbol. 
	//use Helvetica. 

	TLatex *TEX_CMSlumi = new TLatex(0.879397, 0.92238,Form("%.1f fb^{-1} (13 TeV)",Integrated_Luminosity_Data));
	TLatex *TEX_CMSlumi_rat = new TLatex(0.943467,0.92,Form("%.1f fb^{-1} (13 TeV)",Integrated_Luminosity_Data));
	TEX_CMSlumi->SetTextAlign(right_justify);
	TEX_CMSlumi_rat->SetTextAlign(right_justify);

	TLatex *TEX_CMSSim = new TLatex(0.174623, 0.92238,"#bf{CMS} #it{Simulation}");
	TLatex *TEX_CMSPrelim = new TLatex(0.174623, 0.92238, "#bf{CMS} #it{Preliminary}");
	TLatex *TEX_CMSReal = new TLatex(0.174623, 0.92238,"#bf{CMS}");

	TLatex *TEX_CMSSim_rat = new TLatex(0.174623,0.92,"#bf{CMS} #it{Simulation}");
	TLatex *TEX_CMSPrelim_rat = new TLatex(0.174623,0.92, "#bf{CMS} #it{Preliminary}");
	TLatex *TEX_CMSReal_rat = new TLatex(0.174623,0.92,"#bf{CMS}");

	PrettyLatex(TEX_CMSlumi,0.04);
	PrettyLatex(TEX_CMSSim,0.04);
	PrettyLatex(TEX_CMSPrelim,0.04);
	PrettyLatex(TEX_CMSReal,0.04);
	int MCcolor0 = kGreen; 
	int MCcolor1 = kBlue; 
	int MCcolor2 = kRed; 
	int MCcolorDef = kMagenta+2; 

	//Inflate Signal.
	try{
	    for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
		for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
		    htable.get_throwable(*imc,5)->get_throwable(*iplot,6)->Scale(SignalInflationFactor); 
		}
	    }
	}//end try;
	catch(std::pair <std::string,int> errorpair){
	    cerr<<"Stringmap Error! While making StackPlots, Invalid string key "<<errorpair.first<< " error code "<<errorpair.second<<endl;
	    std::terminate();
	}


	cout<<"Approach makeStackPlots_lin"<<endl;
	if(makeStackPlots_lin){
	    try{
		for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
		    TH1F* nametemplate = htable.get_throwable( vClasses[0]->name,1)->get_throwable(*iplot,2);
		    TH1F* background = (TH1F*) nametemplate->Clone((*iplot + "_bkg").c_str());
		    background->Reset(); 

		    TCanvas* canv =PrettyCanvas( newTCanvas((*iplot + "_lin").c_str(),""));
		    canv->SetLeftMargin(0.12);
		    canv->cd();

		    THStack* sstack = new THStack((*iplot + "_stack_lin").c_str(), "");

		    TLegend* leg_left = new TLegend( 0.153266, 0.624352, 0.384422, 0.876943);
		    TLegend* leg_right = new TLegend( 0.616834, 0.624352, 0.84799 , 0.876943);
		    PrettyLegend(leg_left,0.041);
		    PrettyLegend(leg_right,0.041);
		    std::vector<TH1F*> hists_for_set_range;

		    TH1F* ddbkghist = histmapbkg1D.get_throwable(*iplot,20);
		    //has_negatives(ddbkghist);
		    TH1F* datahist = htable.get_throwable(dataClassName,7)->get_throwable(*iplot,8);

		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			hists_for_set_range.push_back(htable.get_throwable(*imc,5)->get_throwable(*iplot,6));
		    }
		    hists_for_set_range.push_back(datahist);



		    //beautify data and put it on the legend 
		    PrettyHist(datahist);
		    PrettyMarker(datahist);
		    datahist->SetBinErrorOption(TH1::kPoisson);
		    if(showData) leg_left->AddEntry(datahist,"DATA");

		    //beautify dd bkg and put it on the legend 
		    int ddbkgcolor = kGray;
		    PrettyHist(ddbkghist, ddbkgcolor);
		    PrettyMarker(ddbkghist,ddbkgcolor,20,0.);
		    PrettyFillColor(ddbkghist, ddbkgcolor);
		    ddbkghist->SetBinErrorOption(TH1::kPoisson);
		    if(draw_ddbkg) leg_left->AddEntry(ddbkghist,"DD Bkg");

		    //compute legend division
		    int nTotal = vBkgClasses.size() + SigtoInclude.size() + showData+1; //use this for splitting the legend in two
		    int nBkgLeft = nTotal/2 + nTotal%2 - SigtoInclude.size() - showData-1;//use this for splitting the legend in two

		    //Add all the MC plots and the ddBkg to the stack. Also add them to the 
		    int i = 1;
		    bool first_bkg_class = true;
		    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){
			cout<<"plot "<<*iplot<<" filling bkg for class "<< (*iclass)->name<<endl;
			TH1F* thishist = htable.get_throwable((*iclass)->name,3)->get_throwable(*iplot,4); // threw 4 on h_MinMlb_OSDL1_sansMlb
			cout<<"plotting bkg for "<<(*iclass)->name<<" X: "<<thishist->GetXaxis()->GetTitle()<<" Y: "<<thishist->GetYaxis()->GetTitle()<<endl;

			PrettyFillColor( thishist, (*iclass)->int_meta["FillColor"] );
			PrettyMarker( thishist, (*iclass)->int_meta["FillColor"] ,20,0.);
			cout<<"C13"<<*iplot<<endl;

			cout<<endl;
			if(first_bkg_class){
			    sstack->Draw();//required in order for sstack to have a defined axis. Removing this results in segfaults. 
			}
			else{
			    cout<<endl;
			    cout<<"sstack: "<<sstack->GetXaxis()->GetNbins()<<endl; //this segfaults!
			    cout<<endl;
			    cout<<"C13b"<<endl;

			    Check_binning(sstack->GetXaxis(), thishist->GetXaxis(), "Check axis for drawing mc bkgs"); //this segfaults.
			}
			cout<<"C14"<<*iplot<<endl;
			sstack->Add( thishist);
			Check_binning(background, thishist, "Check axis for building bkg in mc bkgs");
			background->Add( thishist);
			if(i++ <= nBkgLeft) leg_left->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
			else               leg_right->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
			first_bkg_class = false;
		    }//end for all the Backgrounds
		    if(draw_ddbkg){
			Check_binning(sstack->GetXaxis(), ddbkghist->GetXaxis(), "Check axis for drawing ddbkg");
			sstack->Add( ddbkghist);//hopefully this will be the top of the stack.  //this line is not the problem.
		    }
                    if(draw_ddbkg){
			Check_binning(background, ddbkghist, "Check axis for adding ddbkg to bkgs");
			background->Add(ddbkghist);
		    }
		    hists_for_set_range.push_back(background);

		    //void SameRange_and_leave_legend_room(std::vector<TH1F*> hists, float legendFraction=0., Double_t _min = -1.0, Double_t _max = -1.0);
		    SameRange_and_leave_legend_room(hists_for_set_range, 0.37, 0.0, -1);

		    if(((int)SigtoInclude.size())>0){ //I'm guessing this is needed to get the axis labels down.
			TH1F* starter_hist = htable.get_throwable(SigtoInclude[0],10)->get_throwable(*iplot,11);
			starter_hist->Draw("histo");
		    }//end if.
		    sstack->Draw("sameHISTO");	

		    int whichmc = 0; 
		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
				TH1F* thishist = htable.get_throwable(*imc,5)->get_throwable(*iplot,6); //alternative failure point 
				int linecolor;
				switch (whichmc){ //this is inelegant. use meta info.
					case 0: linecolor = MCcolor0 /*kGreen*/; break;
					case 1: linecolor = MCcolor1 /*kBlue*/; break;
					case 2: linecolor = MCcolor2 /*kRed*/; break;
					default:linecolor = MCcolorDef /*kMagenta+2*/; break;
				}
				PrettyHist(thishist, linecolor); //PrettyHist(TH1D* h, int color = 1, int width = 3, int linestyle = 0);
				PrettyMarker(thishist,linecolor,20,0.);
				//thishist->Sumw2();
				thishist->Draw("samehisto");
				int thisTpMass = mClasses->get_throwable(*imc,7)->blocks[0]->int_meta["TprimeMass"];//xxx update class with metainfo	
				leg_left->AddEntry(thishist, ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
				whichmc++;
		    }
			cout<<"drawing hist "<<*iplot<<endl; //problem is after here. 
		    if(showData) datahist->Draw("Esame"); 
			cout<<"fin draw data"<<endl;

		    leg_left->Draw("same");
		    leg_right->Draw("same");

		
		    TLatex *plotlabel = new TLatex(0.07,0.015,(*iplot).c_str());
		    PrettyLatex(plotlabel,0.03);
		    plotlabel->Draw("same");

		    gPad->RedrawAxis();

		    if(showData && preliminary) TEX_CMSPrelim->Draw("same");
		    else if(showData)  TEX_CMSReal->Draw("same");
		    else TEX_CMSSim->Draw("same"); //this will change once you have a data driven Background. 
		    TEX_CMSlumi->Draw("same");

		    //problem is before here. 
		    if(saveImages) SaveCanvas(canv,*iplot + "_lin", &plotdirs,savewhat);
		}//end for every plot. 
	    }//end try;
	    catch(std::pair <std::string,int> errorpair){
		cerr<<"Stringmap Error! While making StackPlots, Invalid string key "<<errorpair.first<< " error code "<<errorpair.second<<endl;
		std::terminate();
	    }
	} //end StackPlots

    cout<<"approach makeStackPlots_lin_ratio"<<endl;
	if(makeStackPlots_lin_ratio){
	    try{
		for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
		    TH1F* nametemplate = htable.get_throwable( vClasses[0]->name,1)->get_throwable(*iplot,2);
		    TH1F* background = (TH1F*) nametemplate->Clone((*iplot + "_bkg").c_str());
		    background->Reset(); 
		    TH1F* MCbackground = (TH1F*) nametemplate->Clone((*iplot + "_mcbkg").c_str());
		    MCbackground->Reset(); 
		    TCanvas* canv =PrettyCanvas( newTCanvas((*iplot + "_linR").c_str(),""));
		    TPad* pad_main_for_ratio = new TPad("pad_main_for_ratio","",0.,0.30,1.,0.94);
		    TPad* pad_ratio = new TPad("pad_ratio","", 0.,0.061,1.,0.30);
		    //TPad* pad_ratio = new TPad("pad_ratio","", 0.,0.145,1.,0.30);
		    pad_main_for_ratio->SetBottomMargin(0);
		    pad_ratio->SetTopMargin(0);
		    pad_ratio->SetBottomMargin(0.43);

		    pad_main_for_ratio->cd();

		    THStack* sstack = new THStack((*iplot + "_stack_linR").c_str(), "");
		    //now for everything on the 
		    TLegend* leg_left = new TLegend( 0.21608, 0.624352, 0.447236, 0.91385);
		    TLegend* leg_right = new TLegend( 0.616834, 0.624352, 0.84799 , 0.91385);
		    PrettyLegend(leg_left,0.041);
		    PrettyLegend(leg_right,0.041);
		    std::vector<TH1F*> hists_for_set_range;

		    TH1F* ddbkghist = histmapbkg1D.get_throwable(*iplot,20);
		    //has_negatives(ddbkghist);
		    TH1F* datahist = htable.get_throwable(dataClassName,7)->get_throwable(*iplot,8);

		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			hists_for_set_range.push_back(htable.get_throwable(*imc,5)->get_throwable(*iplot,6));
		    }
		    hists_for_set_range.push_back(datahist);

		    //beautify data and put it on the legend 
		    PrettyHist(datahist);
		    PrettyMarker(datahist);
		    datahist->SetBinErrorOption(TH1::kPoisson);
		    if(showData) leg_left->AddEntry(datahist,"DATA");

		    //beautify dd bkg and put it on the legend 
		    int ddbkgcolor = kGray;
		    PrettyHist(ddbkghist, ddbkgcolor);
		    PrettyMarker(ddbkghist,ddbkgcolor,20,0.);
		    PrettyFillColor(ddbkghist, ddbkgcolor);
		    ddbkghist->SetBinErrorOption(TH1::kPoisson);
		    if(draw_ddbkg) leg_left->AddEntry(ddbkghist,"DD Bkg");

		    //compute legend division
		    int nTotal = vBkgClasses.size() + SigtoInclude.size() + showData+1; //use this for splitting the legend in two
		    int nBkgLeft = nTotal/2 + nTotal%2 - SigtoInclude.size() - showData-1;//use this for splitting the legend in two

		    //Add all the MC plots and the ddBkg to the stack. Also add them to the 
		    int i = 1;
		    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){
			//cout<<"plot "<<*iplot<<" filling bkg for class "<< (*iclass)->name<<endl;
			TH1F* thishist = htable.get_throwable((*iclass)->name,3)->get_throwable(*iplot,4); // threw 4 on h_MinMlb_OSDL1_sansMlb
			//cout<<"plotting bkg for "<<(*iclass)->name<<" X: "<<thishist->GetXaxis()->GetTitle()<<" Y: "<<thishist->GetYaxis()->GetTitle()<<endl;
			PrettyFillColor( thishist, (*iclass)->int_meta["FillColor"] );
			PrettyMarker( thishist, (*iclass)->int_meta["FillColor"] ,20,0.);

			sstack->Add( thishist);
			background->Add( thishist); 
			MCbackground->Add( thishist); 
			if(i++ <= nBkgLeft) leg_left->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
			else               leg_right->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
		    }//end for all the Backgrounds
		    if(draw_ddbkg) sstack->Add( ddbkghist);//hopefully this will be the top of the stack. 
		    if(draw_ddbkg) background->Add(ddbkghist);
		    hists_for_set_range.push_back(background);

		    //SameRange_and_leave_legend_room(hists_for_set_range, 0.37,false,0.05); //fix scale: 
		    SameRange_and_leave_legend_room(hists_for_set_range, 0.37, 0.0, -1);//********************************

		    if(((int)SigtoInclude.size())>0){ //I'm guessing this is needed to get the axis labels down.
			TH1F* starter_hist = htable.get_throwable(SigtoInclude[0],10)->get_throwable(*iplot,11);
			starter_hist->Draw("histo");
		    }//end if.
		    sstack->Draw("sameHISTO");	

		    int whichmc = 0; 
		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			TH1F* thishist = htable.get_throwable(*imc,5)->get_throwable(*iplot,6); //alternative failure point 
			int linecolor;
			switch (whichmc){ //this is inelegant. use meta info.
			    case 0: linecolor = MCcolor0 /*kGreen*/; break;
			    case 1: linecolor = MCcolor1 /*kBlue*/; break;
			    case 2: linecolor = MCcolor2 /*kRed*/; break;
			    default:linecolor = MCcolorDef /*kMagenta+2*/; break;
			}
			PrettyHist(thishist, linecolor); //PrettyHist(TH1D* h, int color = 1, int width = 3, int linestyle = 0);
			PrettyMarker(thishist,linecolor,20,0.);
			//thishist->Sumw2();
			thishist->Draw("samehisto");
			int thisTpMass = mClasses->get_throwable(*imc,7)->blocks[0]->int_meta["TprimeMass"];//xxx update class with metainfo	
			leg_left->AddEntry(thishist, ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			//leg_left->AddEntry(thishist,mClasses->get_throwable(*imc,7)->string_meta["LegendLabel"].c_str()); // ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			whichmc++;
		    }
		    cout<<"drawing hist "<<*iplot<<endl; //problem is after here. 
		    if(showData) datahist->Draw("Esame"); 

		    leg_left->Draw("same");
		    leg_right->Draw("same");

		    gPad->RedrawAxis();

		    ///////////////// Ratio subplot ///////////////////////
		    pad_ratio->cd();

		    TH1F* ratio;
		    if(use_ddbkg_in_ratio) ratio = DivideHists(datahist,background);    //ot be drawn as data. with Draw("Esame")
		    else ratio = DivideHists(datahist,MCbackground);
		    if(use_ddbkg_in_ratio) ratio->GetYaxis()->SetTitle("Data/Bkg");
		    else ratio->GetYaxis()->SetTitle("Data/MC Bkg");
		    PrettyRatioPlot(ratio);
		    PrettyMarker(ratio);
		    ratio->GetYaxis()->SetRangeUser(0.,2.);
		    ratio->Draw("Esame");
		    TH1F* uncert;
		    if(use_ddbkg_in_ratio) uncert = make_ratio_uncertainty_hist(datahist, background);
		    else uncert = make_ratio_uncertainty_hist(datahist, MCbackground);
		    //PrettyRatioPlot(uncert);
		    PrettyBlock(uncert, kGray,"//thach");//PrettyBlock2(h[3],kRed,3345,2);
		    uncert->Draw("E2same");

		    //Draw the one-line.
		    TAxis* x = ratio->GetXaxis();
		    TLine *OneLine = new TLine(x->GetXmin(),1.0,x->GetXmax(),1.0);
		    OneLine->SetLineColor(kBlack);
		    OneLine->SetLineWidth(2);
		    OneLine->SetLineStyle(7);//dashed.
		    OneLine->Draw("same");

		    ratio->Draw("Esame");

		    gPad->RedrawAxis();

		    ////////////////////////////////////////
		    canv->cd();
		    pad_main_for_ratio->Draw();
		    pad_ratio->Draw("same");

		    TLatex *plotlabel = new TLatex(0.07,0.015,(*iplot).c_str());
		    PrettyLatex(plotlabel,0.03);
		    plotlabel->Draw("same");

		    if(showData && preliminary) TEX_CMSPrelim->Draw("same");
		    else if(showData)  TEX_CMSReal->Draw("same");
		    else TEX_CMSSim->Draw("same"); //this will change once you have a data driven background. 
		    TEX_CMSlumi->Draw("same");

		    //SaveCanvas(canv,plotsdir + *iplot,savewhat);
		    if(saveImages) SaveCanvas(canv,*iplot + "_linRat", &plotdirs,savewhat);
		}//end for every plot. 
	    }//end try;
	    catch(std::pair <std::string,int> errorpair){
		cerr<<"Stringmap Error! While making StackPlots, Invalid string key "<<errorpair.first<< " error code "<<errorpair.second<<endl;
		std::terminate();
	    }
	} //end StackPlots


	cout<<"approach makeStackPlots_log"<<endl;
	if(makeStackPlots_log){
	    try{
		for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
		    TH1F* nametemplate = htable.get_throwable( vClasses[0]->name,1)->get_throwable(*iplot,2);
		    TH1F* background = (TH1F*) nametemplate->Clone((*iplot + "_bkg").c_str());
		    background->Reset(); 
		    //string Xaxislabel =  nametemplate->GetXaxis()->GetTitle();
		    //string Yaxislabel =  nametemplate->GetYaxis()->GetTitle();
		    //string title = nametemplate->GetTitle();
		    //string canvtitle = title + ";" + Xaxislabel + ";" + Yaxislabel;
		    //TCanvas* canv =PrettyCanvas( newTCanvas((*iplot).c_str(),canvtitle.c_str())); //turns out the title is ugly and undesirable.
			
		    TCanvas* canv =PrettyCanvas( newTCanvas((*iplot + "_log").c_str(),""));
		    canv->SetLeftMargin(0.12);
		    canv->cd();
		    canv->SetLogy();
		    THStack* sstack = new THStack((*iplot + "_stack_log").c_str(), "");
		    //now for everything on the 
		    TLegend* leg_left = new TLegend( 0.153266, 0.624352, 0.384422, 0.876943);
		    TLegend* leg_right = new TLegend( 0.616834, 0.624352, 0.84799 , 0.876943);
		    PrettyLegend(leg_left,0.041);
		    PrettyLegend(leg_right,0.041);
		    std::vector<TH1F*> hists_for_set_range;

		    TH1F* ddbkghist = histmapbkg1D.get_throwable(*iplot,20);
		    //has_negatives(ddbkghist);
		    TH1F* datahist = htable.get_throwable(dataClassName,7)->get_throwable(*iplot,8);

		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			//htable.get_throwable(*imc,5)->get_throwable(*iplot,6)->Scale(SignalInflationFactor); 

			//fill a vector with everything to go on this plot. 
			hists_for_set_range.push_back(htable.get_throwable(*imc,5)->get_throwable(*iplot,6));
		    }
		    hists_for_set_range.push_back(datahist);

		    //beautify data and put it on the legend 
		    PrettyHist(datahist);
		    PrettyMarker(datahist);
		    datahist->SetBinErrorOption(TH1::kPoisson);
		    if(showData) leg_left->AddEntry(datahist,"DATA");

		    //beautify dd bkg and put it on the legend 
		    int ddbkgcolor = kGray;
		    PrettyHist(ddbkghist, ddbkgcolor);
		    PrettyMarker(ddbkghist,ddbkgcolor,20,0.);
		    PrettyFillColor(ddbkghist, ddbkgcolor);
		    ddbkghist->SetBinErrorOption(TH1::kPoisson);
		    leg_left->AddEntry(ddbkghist,"DD Bkg");

			//compute legend division
		    int nTotal = vBkgClasses.size() + SigtoInclude.size() + showData+1; //use this for splitting the legend in two
		    int nBkgLeft = nTotal/2 + nTotal%2 - SigtoInclude.size() - showData-1;//use this for splitting the legend in two
		
		    //Add all the MC plots and the ddBkg to the stack. Also add them to the 
		    int i = 1;
		    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){
			//cout<<"plot "<<*iplot<<" filling bkg for class "<< (*iclass)->name<<endl;
			TH1F* thishist = htable.get_throwable((*iclass)->name,3)->get_throwable(*iplot,4); // threw 4 on h_MinMlb_OSDL1_sansMlb
			//cout<<"plotting bkg for "<<(*iclass)->name<<" X: "<<thishist->GetXaxis()->GetTitle()<<" Y: "<<thishist->GetYaxis()->GetTitle()<<endl;
			PrettyFillColor( thishist, (*iclass)->int_meta["FillColor"] );
			PrettyMarker( thishist, (*iclass)->int_meta["FillColor"] ,20,0.);

			sstack->Add( thishist);
			background->Add( thishist); 

			if(i++ <= nBkgLeft) leg_left->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
			else               leg_right->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
		    }//end for all the Backgrounds
		    if(draw_ddbkg) sstack->Add( ddbkghist);//hopefully this will be the top of the stack. 
		    if(draw_ddbkg) background->Add(ddbkghist);
		    hists_for_set_range.push_back(background);


		    //void SameRange_and_leave_legend_room_log(std::vector<TH1F*> hists, float legendFraction, bool tinymin_override, Double_t _min, Double_t _max){
		    SameRange_and_leave_legend_room_log(hists_for_set_range, 0.37,false,0.05); //fix scale: 


		    if(((int)SigtoInclude.size())>0){ //I'm guessing this is needed to get the axis labels down.
			TH1F* starter_hist = htable.get_throwable(SigtoInclude[0],10)->get_throwable(*iplot,11);
			starter_hist->Draw("histo");
		    }//end if.
		    sstack->Draw("sameHISTO");	

		    int whichmc = 0; 
		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			TH1F* thishist = htable.get_throwable(*imc,5)->get_throwable(*iplot,6); //alternative failure point 
			int linecolor;
			switch (whichmc){ //this is inelegant. use meta info.
			    case 0: linecolor = MCcolor0 /*kGreen*/; break;
			    case 1: linecolor = MCcolor1 /*kBlue*/; break;
			    case 2: linecolor = MCcolor2 /*kRed*/; break;
			    default:linecolor = MCcolorDef /*kMagenta+2*/; break;
			}
			PrettyHist(thishist, linecolor); //PrettyHist(TH1D* h, int color = 1, int width = 3, int linestyle = 0);
			PrettyMarker(thishist,linecolor,20,0.);
			//thishist->Sumw2();
			thishist->Draw("samehisto");
			int thisTpMass = mClasses->get_throwable(*imc,7)->blocks[0]->int_meta["TprimeMass"];//xxx update class with metainfo	
			leg_left->AddEntry(thishist, ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			//leg_left->AddEntry(thishist,mClasses->get_throwable(*imc,7)->string_meta["LegendLabel"].c_str()); // ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			whichmc++;
		    }
			cout<<"drawing hist "<<*iplot<<endl; //problem is after here. 
		    if(showData) datahist->Draw("Esame"); 

		    leg_left->Draw("same");
		    leg_right->Draw("same");

		
		    TLatex *plotlabel = new TLatex(0.07,0.015,(*iplot).c_str());
		    PrettyLatex(plotlabel,0.03);
		    plotlabel->Draw("same");

		    gPad->RedrawAxis();

		    if(showData && preliminary) TEX_CMSPrelim->Draw("same");
		    else if(showData)  TEX_CMSReal->Draw("same");
		    else TEX_CMSSim->Draw("same"); //this will change once you have a data driven background. 
		    TEX_CMSlumi->Draw("same");

		    //SaveCanvas(canv,plotsdir + *iplot,savewhat);
		    if(saveImages) SaveCanvas(canv,*iplot + "_log", &plotdirs,savewhat);
		}//end for every plot. 
	    }//end try;
	    catch(std::pair <std::string,int> errorpair){
		cerr<<"Stringmap Error! While making StackPlots, Invalid string key "<<errorpair.first<< " error code "<<errorpair.second<<endl;
		std::terminate();
	    }
	} //end StackPlots


	cout<<"approach makeStackPlots_log_ratio"<<endl;
	if(makeStackPlots_log_ratio){
	    try{
		for(std::vector<string>::iterator iplot = plotnames.begin(); iplot<plotnames.end();iplot++){
		    TH1F* nametemplate = htable.get_throwable( vClasses[0]->name,1)->get_throwable(*iplot,2);
		    TH1F* background = (TH1F*) nametemplate->Clone((*iplot + "_bkg").c_str());
		    background->Reset();
		    TH1F* MCbackground = (TH1F*) nametemplate->Clone((*iplot + "_MCbkg").c_str());
		    MCbackground->Reset();
		    //string Xaxislabel =  nametemplate->GetXaxis()->GetTitle();
		    //string Yaxislabel =  nametemplate->GetYaxis()->GetTitle();
		    //string title = nametemplate->GetTitle();
		    //string canvtitle = title + ";" + Xaxislabel + ";" + Yaxislabel;
		    //TCanvas* canv =PrettyCanvas( newTCanvas((*iplot).c_str(),canvtitle.c_str())); //turns out the title is ugly and undesirable.
			
		    TCanvas* canv =PrettyCanvas( newTCanvas((*iplot + "_logR").c_str(),""));
		    TPad* pad_main_for_ratio = new TPad("pad_main_for_ratio","",0.,0.30,1.,0.94);
		    TPad* pad_ratio = new TPad("pad_ratio","", 0.,0.061,1.,0.30);
		    //TPad* pad_ratio = new TPad("pad_ratio","", 0.,0.145,1.,0.30);
		    pad_main_for_ratio->SetBottomMargin(0);
		    pad_ratio->SetTopMargin(0);
		    pad_ratio->SetBottomMargin(0.43);

		    pad_main_for_ratio->cd();
		    pad_main_for_ratio->SetLogy();
		    THStack* sstack = new THStack((*iplot + "_stack_logR").c_str(), "");
		    //now for everything on the 
		    TLegend* leg_left = new TLegend( 0.21608, 0.624352, 0.447236, 0.91385);
		    TLegend* leg_right = new TLegend( 0.616834, 0.624352, 0.84799 , 0.91385);
		    PrettyLegend(leg_left,0.041);
		    PrettyLegend(leg_right,0.041);
		    std::vector<TH1F*> hists_for_set_range;

		    TH1F* ddbkghist = histmapbkg1D.get_throwable(*iplot,20);
		    //has_negatives(ddbkghist);
		    TH1F* datahist = htable.get_throwable(dataClassName,7)->get_throwable(*iplot,8);

		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			hists_for_set_range.push_back(htable.get_throwable(*imc,5)->get_throwable(*iplot,6));
		    }
		    hists_for_set_range.push_back(datahist);



		    //beautify data and put it on the legend 
		    PrettyHist(datahist);
		    PrettyMarker(datahist);
		    datahist->SetBinErrorOption(TH1::kPoisson);
		    if(showData) leg_left->AddEntry(datahist,"DATA");

		    //beautify dd bkg and put it on the legend 
		    int ddbkgcolor = kGray;
		    PrettyHist(ddbkghist, ddbkgcolor);
		    PrettyMarker(ddbkghist,ddbkgcolor,20,0.);
		    PrettyFillColor(ddbkghist, ddbkgcolor);
		    ddbkghist->SetBinErrorOption(TH1::kPoisson);
		    if(draw_ddbkg) leg_left->AddEntry(ddbkghist,"DD Bkg");

			//compute legend division
		    int nTotal = vBkgClasses.size() + SigtoInclude.size() + showData+1; //use this for splitting the legend in two
		    int nBkgLeft = nTotal/2 + nTotal%2 - SigtoInclude.size() - showData-1;//use this for splitting the legend in two
		
		    //Add all the MC plots and the ddBkg to the stack. Also add them to the 
		    int i = 1;
		    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){
			//cout<<"plot "<<*iplot<<" filling bkg for class "<< (*iclass)->name<<endl;
			TH1F* thishist = htable.get_throwable((*iclass)->name,3)->get_throwable(*iplot,4); // threw 4 on h_MinMlb_OSDL1_sansMlb
			//cout<<"plotting bkg for "<<(*iclass)->name<<" X: "<<thishist->GetXaxis()->GetTitle()<<" Y: "<<thishist->GetYaxis()->GetTitle()<<endl;
			PrettyFillColor( thishist, (*iclass)->int_meta["FillColor"] );
			PrettyMarker( thishist, (*iclass)->int_meta["FillColor"] ,20,0.);

			sstack->Add( thishist);
			background->Add( thishist); 
			MCbackground->Add( thishist); 
			//HERE add the uncertainty to the bkg.

			if(i++ <= nBkgLeft) leg_left->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
			else               leg_right->AddEntry( thishist, (*iclass)->string_meta["LegendLabel"].c_str() );
		    }//end for all the backgrounds
		    if(draw_ddbkg) sstack->Add( ddbkghist);//hopefully this will be the top of the stack. 
		    if(draw_ddbkg) background->Add(ddbkghist);
		    hists_for_set_range.push_back(background);

		    SameRange_and_leave_legend_room_log(hists_for_set_range, 0.37,false,0.05); //fix scale: 

		    if(((int)SigtoInclude.size())>0){ //I'm guessing this is needed to get the axis labels down.
			TH1F* starter_hist = htable.get_throwable(SigtoInclude[0],10)->get_throwable(*iplot,11);
			starter_hist->Draw("histo");
		    }//end if.
		    sstack->Draw("sameHISTO");	

		    int whichmc = 0; 
		    for(std::vector<string>::iterator imc = SigtoInclude.begin();imc<SigtoInclude.end();imc++){
			TH1F* thishist = htable.get_throwable(*imc,5)->get_throwable(*iplot,6); //alternative failure point xxx
			int linecolor;
			switch (whichmc){ //this is inelegant. use meta info.
			    case 0: linecolor = MCcolor0 /*kGreen*/; break;
			    case 1: linecolor = MCcolor1 /*kBlue*/; break;
			    case 2: linecolor = MCcolor2 /*kRed*/; break;
			    default:linecolor = MCcolorDef /*kMagenta+2*/; break;
			}
			PrettyHist(thishist, linecolor); //PrettyHist(TH1D* h, int color = 1, int width = 3, int linestyle = 0);
			PrettyMarker(thishist,linecolor,20,0.);
			//thishist->Sumw2();
			thishist->Draw("samehisto");
			int thisTpMass = mClasses->get_throwable(*imc,7)->blocks[0]->int_meta["TprimeMass"];//xxx update class with metainfo	
			leg_left->AddEntry(thishist, ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			//leg_left->AddEntry(thishist,mClasses->get_throwable(*imc,7)->string_meta["LegendLabel"].c_str()); // ("T'#bar{T}' ("+to_string(thisTpMass) + " GeV) x " + to_string((int) SignalInflationFactor)).c_str() );//xxx could use update with metainfo
			whichmc++;
		    }
			cout<<"drawing hist "<<*iplot<<endl; //problem is after here. 
		    if(showData) datahist->Draw("Esame"); 

		    leg_left->Draw("same");
		    leg_right->Draw("same");

		    gPad->RedrawAxis();

			///////////////// Ratio subplot ///////////////////////
		    pad_ratio->cd();

		    TH1F* ratio;
		    if(use_ddbkg_in_ratio) ratio = DivideHists(datahist,background);	//ot be drawn as data. with Draw("Esame")
		    else ratio = DivideHists(datahist,MCbackground);	//ot be drawn as data. with Draw("Esame")
		    if(use_ddbkg_in_ratio) ratio->GetYaxis()->SetTitle("Data/Bkg");
		    else ratio->GetYaxis()->SetTitle("Data/MC Bkg");
		    PrettyRatioPlot(ratio);
		    PrettyMarker(ratio);
		    ratio->GetYaxis()->SetRangeUser(0.,2.);
		    ratio->Draw("Esame");
		    TH1F* uncert;
		    if(use_ddbkg_in_ratio) uncert = make_ratio_uncertainty_hist(datahist, background);
		    else uncert = make_ratio_uncertainty_hist(datahist, MCbackground);
		    //PrettyRatioPlot(uncert);
		    PrettyBlock(uncert, kGray,"//thach");//PrettyBlock2(h[3],kRed,3345,2);
		    uncert->Draw("E2same");

			//Draw the one-line.
		    TAxis* x = ratio->GetXaxis();
		    TLine *OneLine = new TLine(x->GetXmin(),1.0,x->GetXmax(),1.0);
		    OneLine->SetLineColor(kBlack);
		    OneLine->SetLineWidth(2);
		    OneLine->SetLineStyle(7);//dashed.
		    OneLine->Draw("same");

		    ratio->Draw("Esame");
			
		    gPad->RedrawAxis();

			////////////////////////////////////////
		    canv->cd();
		    pad_main_for_ratio->Draw();
		    pad_ratio->Draw("same");

		    TLatex *plotlabel = new TLatex(0.07,0.015,(*iplot).c_str());
		    PrettyLatex(plotlabel,0.03);
		    plotlabel->Draw("same");

		    if(showData && preliminary) TEX_CMSPrelim->Draw("same");
		    else if(showData)  TEX_CMSReal->Draw("same");
		    else TEX_CMSSim->Draw("same"); //this will change once you have a data driven background. 
		    TEX_CMSlumi->Draw("same");

		    //SaveCanvas(canv,plotsdir + *iplot,savewhat);
		    if(saveImages) SaveCanvas(canv,*iplot + "_logRat", &plotdirs,savewhat);
		}//end for every plot. 
	    }//end try;
	    catch(std::pair <std::string,int> errorpair){
		cerr<<"Stringmap Error! While making StackPlots, Invalid string key "<<errorpair.first<< " error code "<<errorpair.second<<endl;
		std::terminate();
	    }
	} //end StackPlots

	//close all the files you opened. 
	cout<<"begin closing plot files"<<endl;
	for(std::vector<TFile*>::iterator ifile = vFiles.begin();ifile<vFiles.end();ifile++){
	    //(*ifile)->Close(); //Takes forever! Don't use that.
	    gROOT->GetListOfFiles()->Remove(*ifile); //instantanious
	    //You can work around the slow file->Close command byy removing your file explicitly from the list of file (gROOT->GetListOfFiles()->Remove(file);) 
	}
	cout<<"fin post.C"<<endl;
}//end post

TH1F* extrackBkg(TH2F* bkg_hist){
	//this assumes that row1 of the histogram is the main thing to return with everything higher being variations. 
	//take the stdev of the variations and add that systematic in quadurture with the statistical error. 
	//bkg_hist->Sumw2();
	TH1F* out = hslice(bkg_hist,1); //sometimes throws warning. for b_STSSDLsansB_DATA1ele1muRRDf_hslice1...
	int nx = bkg_hist->GetNbinsX();
	int ny = bkg_hist->GetNbinsY();

        for(int i=0;i<=nx+1;i++){//for every horizontal bin, including underflow and overflow
	    float mean = out->GetBinContent(i);
	    float variance = 0;
	    for(int y=2;y<=ny;y++){ //for every filled bin above the mean value slice (ny-1) bins
		variance+=pow(bkg_hist->GetBinContent(i,y)-mean,2);	
	    }
	    variance/=(float)(ny-2);//probably should be ny-2 for sample stdev. 
	    //variance/=(ny-1);//probably should be ny-2 for sample stdev. 
	    float newerror = sqrt(variance+ pow(out->GetBinError(i),2));
            out->SetBinError(i,newerror);
        }
	return out;
}//end extrackBkg


string MakeThetaRootFile_Yield_simple_signal(histtable htable, histmap2D* histmapbkg, histtable2D htable2D, string dir, string dataClassName,stringmap<KinematicVar*>* kinvar_stringmap){

	std::vector<DMCclass*> vSigClasses_nominal= MCTpTpsigDMCclass(T50ns_F25ns);//all the signal classes, used for limits. 
	std::vector<DMCclass*> vSigClasses_JERup= MCTpTpsigDMCclass(T50ns_F25ns,up);//all the signal classes, used for limits. 
	std::vector<DMCclass*> vSigClasses_JERdown= MCTpTpsigDMCclass(T50ns_F25ns,down);//all the signal classes, used for limits. 
	std::vector<DMCclass*> vSigClasses_JECup= MCTpTpsigDMCclass(T50ns_F25ns,nominal,up);//all the signal classes, used for limits. 
	std::vector<DMCclass*> vSigClasses_JECdown= MCTpTpsigDMCclass(T50ns_F25ns,nominal,down);//all the signal classes, used for limits. 
	
	string varname = "yield";
	string plotname = "h_"+varname; 
	string splotname = "s_"+varname; 


	string filename = dir+"/hist4limit_yield_sig.root";
	cout<<"writing signal limit root file to "<<filename<<endl;

	TFile * f = new TFile(filename.c_str(), "RECREATE");
	f->cd();
	try{
	    for(std::vector<DMCclass*>::iterator iclass =  vSigClasses_nominal.begin();iclass< vSigClasses_nominal.end();iclass++){ 
		cout<<"attempt for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		TH1F* thishist = (TH1F*) htable.get_throwable((*iclass)->name,3)->get_throwable(plotname,4)->Clone((	varname+"__"+Steralized_Class_Name((*iclass)->name) ).c_str());
		thishist->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JERup.begin();iclass<vSigClasses_JERup.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		TH1F* thishist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8); //can't find TpTp700fJERup
		TH1F* thishistclone = (TH1F*) thishist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JER__plus").c_str()); 
		thishistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JERdown.begin();iclass<vSigClasses_JERdown.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		TH1F* thishist = htable.get_throwable((*iclass)->name,9)->get_throwable(plotname,10);
		TH1F* thishistclone = (TH1F*) thishist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JER__minus").c_str());
		thishistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JECup.begin();iclass<vSigClasses_JECup.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		TH1F* thishist = htable.get_throwable((*iclass)->name,11)->get_throwable(plotname,12);
		TH1F* thishistclone = (TH1F*) thishist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JEC__plus").c_str());
		thishistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_JECdown.begin();iclass<vSigClasses_JECdown.end();iclass++){ //for every signal class
		//PSES = Parton Shower Eneryg Scale down
		TH1F* thishist = htable.get_throwable((*iclass)->name,13)->get_throwable(plotname,14);
		TH1F* thishistclone = (TH1F*) thishist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JEC__minus").c_str());
		thishistclone->Write();
	    }

	    KinematicVar* kYield = kinvar_stringmap->get_throwable(varname,1);
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_nominal.begin();iclass<vSigClasses_nominal.end();iclass++){ //for every signal class
		cout<<"attempt s_yield for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		string steralized_class_name= Steralized_Class_Name((*iclass)->name);
		TH2F* thisSysHist = (TH2F*) htable2D.get_throwable((*iclass)->name,15)->get_throwable(splotname,16)->Clone((	varname+"__"+steralized_class_name).c_str());
		TH1F* sbks[nSysYields-1];
		/*static const int nSysYields = 1+//nominal
		  2+//PU corrections
		  2+//renorm envelope
		  2+//pdf 1 sigmas. 
		  2+//Julie Jet SFs 
		  4;//b-tagging. */
		//ddbks[0] = (TH1F*) hslice(thisSysHist,1)//nominal
		sbks[0] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,2)->Clone((varname+"__"+steralized_class_name+"__PUCOR__minus").c_str()),kYield);
		sbks[1] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,3)->Clone((varname+"__"+steralized_class_name+"__PUCOR__plus").c_str()),kYield);

		sbks[2] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,4)->Clone((varname+"__"+steralized_class_name+"__RENORM__minus").c_str()),kYield);
		sbks[3] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,5)->Clone((varname+"__"+steralized_class_name+"__RENORM__plus").c_str()),kYield);

		sbks[4] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,6)->Clone((varname+"__"+steralized_class_name+"__PDF__minus").c_str()),kYield);
		sbks[5] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,7)->Clone((varname+"__"+steralized_class_name+"__PDF__plus").c_str()),kYield);

		sbks[6] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,8)->Clone((varname+"__"+steralized_class_name+"__JETSF__plus").c_str()),kYield);
		sbks[7] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,9)->Clone((varname+"__"+steralized_class_name+"__JETSF__minus").c_str()),kYield);

		sbks[8] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,10)->Clone((varname+"__"+steralized_class_name+"__BSF__plus").c_str()),kYield);
		sbks[9] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,11)->Clone((varname+"__"+steralized_class_name+"__BSF__minus").c_str()),kYield);
		sbks[10] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,12)->Clone((varname+"__"+steralized_class_name+"__LSF__plus").c_str()),kYield);
		sbks[11] = Fix_Yield_Binning((TH1F*) hslice(thisSysHist,13)->Clone((varname+"__"+steralized_class_name+"__LSF__minus").c_str()),kYield);
		for(int i=0;i<nSysYields-1;i++) sbks[i]->Write();

		for(int i=0;i<nSysYields-1;i++) delete sbks[i]; //clean up to do once this all works. 
	    }//end for

		//inject constant systemtics bin by bin. 
	    for(std::vector<DMCclass*>::iterator iclass = vSigClasses_nominal.begin();iclass<vSigClasses_nominal.end();iclass++){ //for every signal class
		    //cout<<"attempt for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		    string steralized_class_name= Steralized_Class_Name((*iclass)->name);
		TH1F* thisbkghist = (TH1F*) htable.get_throwable((*iclass)->name,3)->get_throwable(plotname,4)->Clone((	varname+"__"+Steralized_Class_Name((*iclass)->name)+"__constsys").c_str());
		TH1F* constant_uncert_shift_plots[6];

		constant_uncert_shift_plots[0] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__HLT__minus").c_str());
		bump_ee(constant_uncert_shift_plots[0], -trig_uncert_ee);
		bump_em(constant_uncert_shift_plots[0], -trig_uncert_em);
		bump_mm(constant_uncert_shift_plots[0], -trig_uncert_mm);
		constant_uncert_shift_plots[1] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__HLT__plus").c_str());
		bump_ee(constant_uncert_shift_plots[1], trig_uncert_ee);
		bump_em(constant_uncert_shift_plots[1], trig_uncert_em);
		bump_mm(constant_uncert_shift_plots[1], trig_uncert_mm);

		constant_uncert_shift_plots[2] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPID__minus").c_str());
		bump_ee(constant_uncert_shift_plots[2], -2*lepID_uncert_ele);
		bump_em(constant_uncert_shift_plots[2], -(lepID_uncert_ele+lepID_uncert_mu) );
		bump_mm(constant_uncert_shift_plots[2], -2*lepID_uncert_mu);
		constant_uncert_shift_plots[3] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPID__plus").c_str());
		bump_ee(constant_uncert_shift_plots[3], 2*lepID_uncert_ele);
		bump_em(constant_uncert_shift_plots[3], (lepID_uncert_ele+lepID_uncert_mu) );
		bump_mm(constant_uncert_shift_plots[3], 2*lepID_uncert_mu);

		constant_uncert_shift_plots[4] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPISO__minus").c_str());
		bump_ee(constant_uncert_shift_plots[4], -2*lepIso_uncert_ele);
		bump_em(constant_uncert_shift_plots[4], -(lepIso_uncert_ele+lepIso_uncert_mu) );
		bump_mm(constant_uncert_shift_plots[4], -2*lepIso_uncert_mu);
		constant_uncert_shift_plots[5] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPISO__plus").c_str());
		bump_ee(constant_uncert_shift_plots[5], 2*lepIso_uncert_ele);
		bump_em(constant_uncert_shift_plots[5], (lepIso_uncert_ele+lepIso_uncert_mu) );
		bump_mm(constant_uncert_shift_plots[5], 2*lepIso_uncert_mu);

		for(int i=0;i<6;i++) constant_uncert_shift_plots[i]->Write(); //6 = number of 
		for(int i=0;i<6;i++) delete constant_uncert_shift_plots[i];
	    }//end for every background class.


	}catch(std::pair <std::string,int> errorpair){
		cerr<<"Stringmap Error! While making Theta sig root files. Invalid string key "<<errorpair.first<< " with error code "<<errorpair.second<<endl; 
	    std::terminate();
	}//end catch;

	f->Close();
	return filename;
		
}//end MakeThetaRootFile_Yield_simple_signal

string MakeThetaRootFile_Yield_nonsignal(histtable htable, histmap2D* histmapbkg, histtable2D htable2D, string dir, string dataClassName, 
	std::vector<DMCclass*> vBkgClasses,
	std::vector<DMCclass*> vBkgClassesUP, std::vector<DMCclass*> vBkgClassesDOWN, 
	std::vector<DMCclass*> vBkgClassesJERup, std::vector<DMCclass*> vBkgClassesJERdown, 
	std::vector<DMCclass*> vBkgClassesJECup, std::vector<DMCclass*> vBkgClassesJECdown,
	stringmap<KinematicVar*>* kinvar_stringmap){
	//to this you'll be adding JEC, JER.
	//This takes in Data, all backgrounds, and all their variations, and writes them to a file.
	//example call:
	//string thetafile = MakeThetaRootFile_Yield_nonsignal(htable, histmapbkg, "test", dataClassName, vBkgClasses, vBkgClassesUP, vBkgClassesDOWN, vBkgClassesJERup, vBkgClassesJERdown, vBkgClassesJECup, vBkgClassesJECdown);
	
	string varname = "yield";
	string plotname = "h_"+varname; 
	string splotname = "s_"+varname; 

	string filename = dir+"/hist4limit_yield.root";
	cout<<"writing Limit root file to "<<filename<<endl;

	TFile * f = new TFile(filename.c_str(), "RECREATE");
	f->cd();

	try{
	    //fetch data. 
	    TH1F* datahist = (TH1F*) htable.get_throwable(dataClassName,1)->get_throwable(plotname,2)->Clone((varname+"__DATA").c_str());
	    datahist->Write(); //seems ot have happened. 

	    //write all the background histograms. 
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){ //for every bkg class
		cout<<"attempt for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		TH1F* thisbkghist = (TH1F*) htable.get_throwable((*iclass)->name,3)->get_throwable(plotname,4)->Clone((	varname+"__"+Steralized_Class_Name((*iclass)->name) ).c_str());
		//get_throwable("h_yield",4) throws an error.
		thisbkghist->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesUP.begin();iclass<vBkgClassesUP.end();iclass++){ //for every bkg class
		cout<<"attempt for PSES plus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		//PSES = Parton Shower Eneryg Scale up
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,5)->get_throwable(plotname,6);
		//fails to find STUPf in htable. 
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__PSES__plus").c_str());
		thisbkghistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesDOWN.begin();iclass<vBkgClassesDOWN.end();iclass++){ //for every bkg class
		cout<<"attempt for PSES minus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		//PSES = Parton Shower Eneryg Scale down
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8);
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__PSES__minus").c_str());
		thisbkghistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesJERup.begin();iclass<vBkgClassesJERup.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		cout<<"attempt for jer plus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8);
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JER__plus").c_str());
		thisbkghistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesJERdown.begin();iclass<vBkgClassesJERdown.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		cout<<"attempt for jer minus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8);
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JER__minus").c_str());
		thisbkghistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesJECup.begin();iclass<vBkgClassesJECup.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		cout<<"attempt for jec plus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8);
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JEC__plus").c_str());
		thisbkghistclone->Write();
	    }
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClassesJECdown.begin();iclass<vBkgClassesJECdown.end();iclass++){ //for every bkg class
		//PSES = Parton Shower Eneryg Scale down
		cout<<"attempt for jec minus class "<<(*iclass)->name<<" to get "<<plotname<<endl;
		TH1F* thisbkghist = htable.get_throwable((*iclass)->name,7)->get_throwable(plotname,8);
		TH1F* thisbkghistclone = (TH1F*) thisbkghist->Clone((varname+"__"+Steralized_Class_Name((*iclass)->name)+"__JEC__minus").c_str());
		thisbkghistclone->Write();
	    }

	    KinematicVar* kYield = kinvar_stringmap->get_throwable(varname,100);
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){ //for every bkg class
		cout<<"attempt s_yield for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		string steralized_class_name= Steralized_Class_Name((*iclass)->name);
		TH2F* thisSysBkgHist = (TH2F*) htable2D.get_throwable((*iclass)->name,3)->get_throwable(splotname,4)->Clone((	varname+"__"+steralized_class_name).c_str());
//histmap2D* histmapbkg
//typedef stringmap<TH2F*> histmap2D; //itterates over DMC blocks
//typedef stringmap<histmap2D*> histtable2D;
		TH1F* sbks[nSysYields-1];
		/*static const int nSysYields = 1+//nominal
		  2+//PU corrections
		  2+//renorm envelope
		  2+//pdf 1 sigmas. 
		  2+//Julie Jet SFs 
		  4;//b-tagging. */
		//ddbks[0] = (TH1F*) hslice(thisSysBkgHist,1)//nominal
		sbks[0] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,2)->Clone((varname+"__"+steralized_class_name+"__PUCOR__minus").c_str()),kYield);
		sbks[1] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,3)->Clone((varname+"__"+steralized_class_name+"__PUCOR__plus").c_str()),kYield);

		sbks[2] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,4)->Clone((varname+"__"+steralized_class_name+"__RENORM__minus").c_str()),kYield);
		sbks[3] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,5)->Clone((varname+"__"+steralized_class_name+"__RENORM__plus").c_str()),kYield);

		sbks[4] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,6)->Clone((varname+"__"+steralized_class_name+"__PDF__minus").c_str()),kYield);
		sbks[5] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,7)->Clone((varname+"__"+steralized_class_name+"__PDF__plus").c_str()),kYield);

		sbks[6] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,8)->Clone((varname+"__"+steralized_class_name+"__JETSF__plus").c_str()),kYield);
		sbks[7] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,9)->Clone((varname+"__"+steralized_class_name+"__JETSF__minus").c_str()),kYield);

		sbks[8] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,10)->Clone((varname+"__"+steralized_class_name+"__BSF__plus").c_str()),kYield);
		sbks[9] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,11)->Clone((varname+"__"+steralized_class_name+"__BSF__minus").c_str()),kYield);
		sbks[10] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,12)->Clone((varname+"__"+steralized_class_name+"__LSF__plus").c_str()),kYield);
		sbks[11] = Fix_Yield_Binning((TH1F*) hslice(thisSysBkgHist,13)->Clone((varname+"__"+steralized_class_name+"__LSF__minus").c_str()),kYield);
		for(int i=0;i<nSysYields-1;i++) sbks[i]->Write();

		for(int i=0;i<nSysYields-1;i++) delete sbks[i]; //clean up to do once this all works. 
	    }
	    //Get the ddhists 
	    TH2F* ddbkgs = histmapbkg->get_throwable(plotname,3); 
	    //histmapbkg is indexed using the h_ name rather than the b_name
	    //This is done around the line "histmapbkg->set(thisbkgplotname,temp2);"
	    TH1F* ddbks[nmodes];
	    ddbks[0] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,1)->Clone("yield__DDBKG"),kYield);
	    ddbks[1] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,2)->Clone("yield__DDBKG__passrate__plus"),kYield);
	    ddbks[2] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,3)->Clone("yield__DDBKG__passrate__minus"),kYield);
	    ddbks[3] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,4)->Clone("yield__DDBKG__failrate__plus"),kYield);
	    ddbks[4] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,5)->Clone("yield__DDBKG__failrate__minus"),kYield);
	    ddbks[5] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,6)->Clone("yield__DDBKG__qMisIDrate__plus"),kYield);
	    ddbks[6] = Fix_Yield_Binning((TH1F*) hslice(ddbkgs,7)->Clone("yield__DDBKG__qMisIDrate__minus"),kYield);
	    for(int i=0;i<nmodes;i++) ddbks[i]->Write();
	    for(int i=0;i<nmodes;i++) delete ddbks[i];

		//inject constant systemtics bin by bin. 
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){ //for every bkg class
		//cout<<"attempt for class "<<(*iclass)->name<<" to get "<<plotname<<endl;//zzz
		string steralized_class_name= Steralized_Class_Name((*iclass)->name);
		TH1F* thisbkghist = (TH1F*) htable.get_throwable((*iclass)->name,3)->get_throwable(plotname,4)->Clone((	varname+"__"+Steralized_Class_Name((*iclass)->name)+"__constsys").c_str());
		TH1F* constant_uncert_shift_plots[6];

		constant_uncert_shift_plots[0] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__HLT__minus").c_str());
		    bump_ee(constant_uncert_shift_plots[0], -trig_uncert_ee);
		    bump_em(constant_uncert_shift_plots[0], -trig_uncert_em);
		    bump_mm(constant_uncert_shift_plots[0], -trig_uncert_mm);
		constant_uncert_shift_plots[1] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__HLT__plus").c_str());
		    bump_ee(constant_uncert_shift_plots[1], trig_uncert_ee);
		    bump_em(constant_uncert_shift_plots[1], trig_uncert_em);
		    bump_mm(constant_uncert_shift_plots[1], trig_uncert_mm);

		constant_uncert_shift_plots[2] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPID__minus").c_str());
		    bump_ee(constant_uncert_shift_plots[2], -2*lepID_uncert_ele);
		    bump_em(constant_uncert_shift_plots[2], -(lepID_uncert_ele+lepID_uncert_mu) );
		    bump_mm(constant_uncert_shift_plots[2], -2*lepID_uncert_mu);
		constant_uncert_shift_plots[3] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPID__plus").c_str());
		    bump_ee(constant_uncert_shift_plots[3], 2*lepID_uncert_ele);
		    bump_em(constant_uncert_shift_plots[3], (lepID_uncert_ele+lepID_uncert_mu) );
		    bump_mm(constant_uncert_shift_plots[3], 2*lepID_uncert_mu);

		constant_uncert_shift_plots[4] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPISO__minus").c_str());
		    bump_ee(constant_uncert_shift_plots[4], -2*lepIso_uncert_ele);
		    bump_em(constant_uncert_shift_plots[4], -(lepIso_uncert_ele+lepIso_uncert_mu) );
		    bump_mm(constant_uncert_shift_plots[4], -2*lepIso_uncert_mu);
		constant_uncert_shift_plots[5] = (TH1F*) thisbkghist->Clone((varname+"__"+steralized_class_name+"__LEPISO__plus").c_str());
		    bump_ee(constant_uncert_shift_plots[5], 2*lepIso_uncert_ele);
		    bump_em(constant_uncert_shift_plots[5], (lepIso_uncert_ele+lepIso_uncert_mu) );
		    bump_mm(constant_uncert_shift_plots[5], 2*lepIso_uncert_mu);

		for(int i=0;i<6;i++) constant_uncert_shift_plots[i]->Write(); //6 = number of 
		for(int i=0;i<6;i++) delete constant_uncert_shift_plots[i];
	    }//end for every background class.

	}//end try
	catch(std::pair <std::string,int> errorpair){
	    //switch(errorpair.second ){
		//case 1: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in htable"<<endl; break;
		//case 2: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in htable submap"<<endl; break;
		//case 3: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in histmapbkg"<<endl; break;
		//default: 
		cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " with error code "<<errorpair.second<<endl; //break;
	    //}//end switch
	    std::terminate();
	}//end catch;

	f->Close();
	return filename;
} //end MakeThetaRootFile_Yield




std::vector<thetaSigFile*> MakeThetaRootFile_Yield_signalScan(stringmap<std::vector<TH1F*>> Signal_yields,  std::vector<DMCclass*> vSigClassesAll,string dir, int nBRslices){
	//take in signal yields broken up by MCtrue branching and produces a scan of files containing just them. 	
	//I need six versions of h_yield from each signal file: WW, WH, WZ, HZ, HH, ZZ. 
	double div = 1.0/((double) nBRslices); 
	std::vector<thetaSigFile*> thetaSigFiles;
	
	//then I'm going to get their branching ratios and scan them. 
	for(std::vector<DMCclass*>::iterator iclass = vSigClassesAll.begin();iclass<vSigClassesAll.end();iclass++){ //for every bkg class
		std::vector<TH1F*> hists = Signal_yields.get_throwable((*iclass)->name,1);
		for(double bWbr = 0.0; bWbr <= 1.0; bWbr += div){
		    for(double tHbr = 0.0; tHbr <= 1.0-bWbr; tHbr += div){
			string thisfilename = ThetaFileNameSig(dir,(*iclass)->name,bWbr, tHbr);

			TH1F* thissig =  brRescale( hists, bWbr, tHbr,"yield__signal");
			thetaSigFiles.push_back(new thetaSigFile(thisfilename,bWbr, tHbr));
			TFile* f = new TFile(thisfilename.c_str() ,"RECREATE");
			f->cd();
			thissig->Write();
			//eventually you'll be writing a great many more into this file. 
			f->Close();
		    }//end tHbr scan. 
		}//end bWbr scan
        }//end for every class. 
	return thetaSigFiles;
}//end MakeThetaRootFile_Yield_signalScan

string ThetaFileNameSig(string directory, string classname, double bWbr, double tHbr){
	//makes the names for root files going to Theta 
	//for bWbr = 0.12, tHbr = 0.34 class TpTp800f, returns directory/hist4limit_yield_TpTp800f_Wbr12_Hbr34.root;
	char bufferW[5]; //4 for 2 decimal places, 5 for 3. 
	char bufferH[5]; //4 for 2 decimal places, 5 for 3. 
	sprintf(bufferW,"%.3f",bWbr);
	sprintf(bufferH,"%.3f",tHbr);
	string sW(bufferW);
	string sH(bufferH);
	return directory+"/hist4limit_yield_"+classname+"_Wbr"+sW.substr(2)+"_Hbr"+sH.substr(2)+ ".root";
} 

TH1F* brRescale( std::vector<TH1F*> hists, float bWbr, float tHbr, string outname){
	//Take a vector of simulated signal, divided up by branching. Reweight (without changing hists) to a new br. 
	//add that all up and return it.  
    //Assumes the vector is of length 6 = nBByields
    //0:WW, 1:WH, 2: WZ, 3: HH, 4: HZ, 5: ZZ 
    float tZbr = get_bZbr(bWbr, tHbr);

    vector<TH1F*> hout;
    for(int i=0;i<nBByields;i++) hout.push_back( (TH1F*) hists[i]->Clone((((string) hists[i]->GetName()) + "_" + to_string(bWbr) + "_" + to_string(tHbr)).c_str() ) );

	//multiplying by nine = dividing by (1/3)^2
	//the combinatorial factors of 2 cancel. 
    hout[0]->Scale( bWbr*bWbr*9.0 );
    hout[1]->Scale( bWbr*tHbr*9.0 );
    hout[2]->Scale( bWbr*tZbr*9.0 );
    hout[3]->Scale( tHbr*tHbr*9.0 );
    hout[4]->Scale( tHbr*tZbr*9.0 );
    hout[5]->Scale( tZbr*tZbr*9.0 );
	TH1F* out = (TH1F*) hout[0]->Clone(outname.c_str());
    for(int i=1;i<nBByields;i++) out->Add(hout[i]);
    return out;
}//end MCbrReweight

float get_bZbr(float bWbr, float tHbr){
    Assert(bWbr <= 1.0 and bWbr >= 0.0 and tHbr <= 1.0 and tHbr >= 0);
    float tZbr = 1.0 - tHbr - bWbr;
    Assert(tZbr >= 0.0 and tZbr < 1.0);
    return tZbr;
}

string MakeThetaCounts(histtable htable, histmap2D* histmapbkg, string SigClassToUse, std::vector<DMCclass*> vBkgClasses){
	//Here you're going to do the simplest thing. 
	//1. Get a all the background hists, add them into one hist. 
	//2. Then get the signal hists, add them into one hist. 
	//3. Do a very simple counting experiment in Theta to see where the ideal cut value is in terms of optomizing the expected limit. 
	//This will be done for every plot in sight, so it needs to be fast. 
	//You'll need to reach into kinvars and figure out which is the best thign to do. 
	
	string varname = "yield";
	string plotname = "h_"+varname; 

	string dir = ".";
	string LimitRootFileName = dir+"/hist4limit_yield.root";
	cout<<"writing limit root file to "<<LimitRootFileName<<endl;

	TFile * f = new TFile(LimitRootFileName.c_str(), "RECREATE");
	f->cd();

	try{
	    //write all the background histograms. 
	    for(std::vector<DMCclass*>::iterator iclass = vBkgClasses.begin();iclass<vBkgClasses.end();iclass++){ //for every bkg class
		TH1F* thisbkghist = (TH1F*) htable.get_throwable((*iclass)->name,1)->get_throwable(plotname,2)->Clone((plotname+"__"+(*iclass)->name).c_str());
		thisbkghist->Write();
	    }

	    //Get the ddhists
	    TH2F* ddbkgs = histmapbkg->get_throwable(plotname,3); 
	    //histmapbkg is indexed using the h_ name rather than the b_name
	    //This is done around the line "histmapbkg->set(thisbkgplotname,temp2);"
	    TH1F* ddbks[nmodes];
	    ddbks[0] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG");
	    ddbks[1] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__passrate__plus");
	    ddbks[2] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__passrate__minus");
	    ddbks[3] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__failrate__plus");
	    ddbks[4] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__failrate__minus");
	    ddbks[5] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__qMisIDrate__plus");
	    ddbks[6] = (TH1F*) hslice(ddbkgs,1)->Clone("h_yield__DDBKG__qMisIDrate__minus");
	    for(int i=0;i<nmodes;i++) ddbks[i]->Write();

	}//end try
	catch(std::pair <std::string,int> errorpair){
	    switch(errorpair.second ){
		case 1: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in htable"<<endl; break;
		case 2: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in htable submap"<<endl; break;
		case 3: cerr<<"Stringmap Error! While making Theta nonsig root files. Invalid string key "<<errorpair.first<< " sought in histmapbkg"<<endl; break;
	    }//end switch
	    std::terminate();
	}//end catch;

	f->Close();
	return LimitRootFileName;
} //end MakeThetaRootFile_Yield

TH1F* patchYield(TH1F* yield, LabelKinVars allkinvar_stringmap){ //NEEDS TEST
	const bool useOSLD2 = false;
	TH1F* out;	
	try{
		KinematicVar* kYield = allkinvar_stringmap->get_throwable("yield",1);
		int nbinsold = kYield->nbins;
		int nbinsnew = nbinsold; 
		if(!useOSLD2) nbinsnew -= 3;
		out = new TH1F((string(yield->GetName())+"_patch").c_str(), yield->GetTitle(), nbinsnew,0,nbinsnew);
		int nextbinnew = 0, nextbinold = 0;
		for(int ibin = 1; ibin <= nbinsold; ibin++){
			if(!useOSLD2 and (ibin == 2 or ibin == 5 or ibin == 8)) continue;
			out->GetXaxis()->SetBinLabel(nextbinnew,yield->GetXaxis()->GetBinLabel(ibin));
			out->SetBinContent(nextbinnew, yield->GetBinContent(ibin));
			out->SetBinError(nextbinnew++, yield->GetBinError(ibin));
		}//end for
	}//end try
	catch(std::pair <std::string,int> errorpair){
		cout<<"patchYield isn't finidng yeild"<<endl;
		std::terminate();
	}
	return out;
}//end patchYield.

TH1F* make_ratio_uncertainty_hist(TH1F* data, TH1F* bkg){
	//Will return a histogram with bin values 1, but error bars equal to the 
	string name = string(bkg->GetName()) + "uncert";
	TH1F* uncert = new TH1F(*bkg);
	uncert->Reset();
	for(int i=1;i<=bkg->GetNbinsX();i++){
		float bin = bkg->GetBinContent(i);
		if(!aeq(bin,0.)) uncert->SetBinError(i,bkg->GetBinError(i)/pow(bin,2));
		else uncert->SetBinError(i,0);
		uncert->SetBinContent(i,1);
	}
	return uncert;
}//end make_ratio_uncertainty_hist

void fix_negatives(TH1F* hist, bool verbose){
	//Given a histogram that might have negative entries, 
	//Zero those entries and rescale the rest of the histogram to have the same integral. 
	float integ = 0.;
	float pos_integral = 0.;
	float stat_uncert = 0.;
	/**//**//**/if(verbose) cout<<"Investigating fix_negatives"<<endl;

	for(int i=1;i<=hist->GetNbinsX();i++){
		float bin = hist->GetBinContent(i);
		/**//**//**/if(verbose) cout<<"    Bin "<<i<<": "<<bin;
		integ+= bin;
		stat_uncert+= fabs(bin);
		if(bin >=0) pos_integral += bin;
		else{
		    /**//**//**/if(verbose) cout<<"    Observed to be negative, setting to zero; Proof: ";
		    hist->SetBinContent(i,0);
		    hist->SetBinError(i,0);
		    /**//**//**/if(verbose) cout<<hist->GetBinContent(i)<< " +- "<< hist->GetBinError(i);
		}
		/**//**//**/if(verbose) cout<<endl;
	}//for
	stat_uncert = sqrt(stat_uncert);

	// hist->Scale(integ/pos_integral);
	if(integ>=0. and pos_integral>0 ){
	    /**//**//**/if(verbose) cout<<"Positive integral; scaling by "<<integ/pos_integral<<endl;
	    for(int i=1;i<=hist->GetNbinsX();i++){
		float bin = hist->GetBinContent(i);
		float ubin = hist->GetBinError(i);
		
		float newbin = bin*integ/pos_integral;
		hist->SetBinContent(i, newbin);
		if(aeq(bin,0.) or aeq(integ, 0)  ) hist->SetBinError(i, 0.); 
		else hist->SetBinError(i, newbin*sqrt(
				pow(ubin/bin,2) +
				pow(stat_uncert/integ,2) + 
				(1.0/pos_integral)  )  );
		
	    }//end for
	}//end if there's no divide by zero error. 
	else{ //this ought to only occur if all bins are zero, so should do nothing. 
	    if(integ<0)cout<<"Warning! fix_negatives sees "<<hist->GetName()<<" has negative integral"<<endl;
	    /**//**//**/if(verbose) cout<<"Zeroing hist "<<endl;
	    for(int i=1;i<=hist->GetNbinsX();i++){
		/**//**//**/bool more = false;
		/**//**//**/if(verbose and hist->GetBinContent(i)!=0){ cout<<"    Zeroing "<<i<<" Proof: "; more = true;}
		hist->SetBinContent(i, 0.); 
		hist->SetBinError(i, 0);
		/**//**//**/if(verbose and more) cout<<hist->GetBinContent(i)<<" +- "<<hist->GetBinError(i)<<endl;
	    }
	    hist->SetBinContent(0, -1); //notes in the plot that there was an error zeroing. 
	} 

	if(has_negatives(hist)){
	    cout<<"fix_negatives is not working. Go fix it."<<endl;
	    if(not verbose) fix_negatives(hist, true);
	    Assert(0);
	}
}//end fix_negatives

void fix_negativesX(TH2F* hist, bool verbose){
    /**//**//**/if(verbose) cout<<"Investigating fix_negativesX"<<endl;
    vector<int> problem_rows;
    for(int j=1;j<=hist->GetNbinsY();j++){
	float integ = 0.;
	float pos_integral = 0.;
	float stat_uncert = 0.;
	/**//**//**/if(verbose) cout<<"Considering j="<<j<<endl;
	for(int i=1;i<=hist->GetNbinsX();i++){
	    float bin = hist->GetBinContent(i,j);
	    /**//**//**/if(verbose) cout<<"    Row "<<i<<": "<<bin;
	    integ+= bin;
	    stat_uncert+= fabs(bin);
	    if(bin >=0) pos_integral += bin;
	    else{
		/**//**//**/if(verbose) cout<<"    Observed to be negative, setting to zero; Proof: ";
		hist->SetBinContent(i,j,0.0);
		hist->SetBinError(i,j,0.0);
		/**//**//**/if(verbose) cout<<hist->GetBinContent(i,j)<< " +- "<< hist->GetBinError(i,j);
	    }
	    /**//**//**/if(verbose) cout<<endl;
	}//for
	stat_uncert = sqrt(stat_uncert);

	// hist->Scale(integ/pos_integral);
	if(integ>=0 and pos_integral>0 ){
	    /**//**//**/if(verbose) cout<<"Positive integral; scaling by "<<integ/pos_integral<<endl;
	    for(int i=1;i<=hist->GetNbinsX();i++){
		float bin = hist->GetBinContent(i,j);
		float ubin = hist->GetBinError(i,j);

		float newbin = bin*integ/pos_integral;
		hist->SetBinContent(i,j, newbin);
		if(aeq(bin,0.) or aeq(integ, 0)  ) hist->SetBinError(i,j, 0.); 
		else hist->SetBinError(i,j, newbin*sqrt(
			    pow(ubin/bin,2) +
			    pow(stat_uncert/integ,2) + 
			    (1.0/pos_integral)  )  );

	    }//end for
	}//end if there's no divide by zero error. 
	else{
	    if(integ<0) problem_rows.push_back(j);
	    /**//**//**/if(verbose) cout<<"Zeroing row "<<j<<endl;
	    for(int i=1;i<=hist->GetNbinsX();i++){
		/**//**//**/if(verbose) cout<<"    Zeroing "<<i<<","<<j<<" Proof: ";
		hist->SetBinContent(i,j, 0.0);
		hist->SetBinError(i,j, 0.0);
		/**//**//**/if(verbose) cout<<hist->GetBinContent(i,j)<<" +- "<<hist->GetBinError(i,j)<<endl;
	    }
	    hist->SetBinContent(0,j, -1); //notes in the plot that row was 0'ed. 
	}
    }//end for y

	//Complain about all the problem rows. 
    if(problem_rows.size() >0){
	cout<<"Warning! fix_negativesX sees "<<hist->GetName()<<" has negative row integral(s) on row(s) ";
	for(int j=0;j<(int)problem_rows.size();j++)cout<<problem_rows[j]<<" ";
	cout<<endl;
    }

    if(has_negatives(hist)){
	cout<<"fix_negativesX is not working. Go fix it."<<endl;
	if(not verbose) fix_negativesX(hist, true);
	std::terminate();
    }
}//end fix_negativesX

bool has_negatives(TH1F* hist){
	bool has_neg = false;
	int negbin = -1;
	for(int i=1;i<=hist->GetNbinsX() and not has_neg;i++){
		if(hist->GetBinContent(i)<0.0){
		    has_neg = true;
		    negbin = i;
		    cout<<"Hist still has negatives "<<hist->GetName()<< " bin "<<negbin<<" content "<< hist->GetBinContent(negbin)<<" +- "<< hist->GetBinError(negbin)<<endl;
		}
	}//for
	//if(has_neg) cout<<"Hist still has negatives "<<hist->GetName()<< " bin "<<negbin<<" content "<< hist->GetBinContent(negbin)<<" +- "<< hist->GetBinError(negbin)<<endl;
	return has_neg;
}
bool has_negatives(TH2F* hist){
	bool has_neg = false;
	int negbinX = -1;
	int negbinY = -1;
	for(int j=1;j<=hist->GetNbinsY() and not has_neg;j++){
	for(int i=1;i<=hist->GetNbinsX() and not has_neg;i++){
		if(hist->GetBinContent(i,j)<0.0){
		    has_neg = true;
		    negbinX = i;
		    negbinY = j;
		    cout<<"Hist still has negatives "<<hist->GetName()<< " bin "<<negbinX<<","<<negbinY<<" content "<< hist->GetBinContent(negbinX,negbinY)<<" +- "<< hist->GetBinError(negbinX,negbinY)<<endl;
		}
	}}//for
	//if(has_neg) cout<<"Hist still has negatives "<<hist->GetName()<< " bin "<<negbinX<<","<<negbinY<<" content "<< hist->GetBinContent(negbinX,negbinY)<<" +- "<< hist->GetBinError(negbinX,negbinY)<<endl;
	return has_neg;
}

bool Check_binning(TH1F* A, TH1F* B, string complaint){
    //returns true iff their nbins matches
    if(A->GetNbinsX() != B->GetNbinsX()){ 
	cout<<complaint<<" first("<<B->GetName()<<"): "<<A->GetNbinsX()<<" second("<<B->GetName()<<")"<<B->GetNbinsX()<<endl;
	return false;
    }
    return true;
}
bool Check_binning(TH2F* A, TH2F* B, string complaint){
    //returns true iff their nbins matches
    if(A->GetNbinsX() != B->GetNbinsX()) cout<<complaint<<" first("<<B->GetName()<<")X: "<<A->GetNbinsX()<<" second("<<B->GetName()<<")X"<<B->GetNbinsX()<<endl;
    if(A->GetNbinsY() != B->GetNbinsY()) cout<<complaint<<" first("<<B->GetName()<<")Y: "<<A->GetNbinsY()<<" second("<<B->GetName()<<")Y"<<B->GetNbinsY()<<endl;
    return (A->GetNbinsX() == B->GetNbinsX()) and (A->GetNbinsY() == B->GetNbinsY());
}
bool Check_binning(TAxis* A, TAxis* B, string complaint){
    //returns true iff their nbins matches
    //if one of the TAxis comes from a THStack, make sure to call Draw before calling this.
    if(A->GetNbins() != B->GetNbins()){
	cout<<complaint<<" first: "<<A->GetNbins()<<" second"<<B->GetNbins()<<endl;
	return false;
    }
    return true;
}

string  Steralized_Class_Name(string dirty_class_name){
	string clean_class_name = FindAndReplaceLast(dirty_class_name,"UP","");
	FindAndReplaceLast_inplace(clean_class_name,"DOWN","");
	FindAndReplaceLast_inplace(clean_class_name,"up","");
	FindAndReplaceLast_inplace(clean_class_name,"down","");
	FindAndReplaceLast_inplace(clean_class_name,"JER","");
	FindAndReplaceLast_inplace(clean_class_name,"JEC","");
	return clean_class_name;
}

//void Fix_Yield_Binning(TH1F* tempyield, KinematicVar* kinvar, bool include_OSDL1, bool include_OSDL2, bool include_SSDL){
TH1F* Fix_Yield_Binning(TH1F* tempyield, KinematicVar* kinvar, bool include_OSDL1, bool include_OSDL2, bool include_SSDL){
    //Fixes the binning in place: get rid of the weird extra bins on the end and only use the included channels. 
	if(kinvar->nbins != 9){
		cout<<"ERROR! you changed the binning of the yield kinematic variable but didn't update Fix_Yield_Binning! Fix ME"<<endl;
		std::terminate();
	}
	if( not (include_OSDL1 or include_OSDL2 or include_SSDL)){
		cout<<"ERROR! Turn on at least one of the channels to include in FIx_Yield_Binning"<<endl;
		std::terminate();
	}
	int nbins = 9 - (include_OSDL1?0:3) - (include_OSDL2?0:3) - (include_SSDL?0:3);
	string rooname = (string)tempyield->GetName();
	tempyield->SetName((rooname+"_o").c_str());
	TH1F* yieldout = new TH1F(rooname.c_str(),tempyield->GetTitle(),nbins,0,nbins);

	int outbin = 1; 
	for(int inbin = 1;inbin<= 9;inbin++){
	    if( (inbin%3 == 1 and not include_OSDL1) or 
		(inbin%3 == 2 and not include_OSDL2) or
		(inbin%3 == 0 and not include_SSDL)) continue;

	    yieldout->SetBinContent(outbin, tempyield->GetBinContent(inbin));
	    yieldout->SetBinError(outbin, tempyield->GetBinError(inbin));
	    yieldout->GetXaxis()->SetBinLabel(outbin,tempyield->GetXaxis()->GetBinLabel(inbin));

	    outbin++;
	}
	return yieldout;
	//to make this a return instead of replace inline, uncomment return and delete the next three lines
	//delete tempyield; //ends up producing segfaults.
	//tempyield = yieldout;
	//tempyield->SetName(rooname.c_str());
}//end Fix_Yield_Binning


void bump_ee(TH1F* h_yield, float bump_term,bool include_OSDL1, bool include_OSDL2, bool include_SSDL){
    //bump the ee bins by (1+bump_term)
    int channels_per_flavor_combo = (include_OSDL1?1:0) + (include_OSDL2?1:0) + (include_SSDL?1:0);
    if( channels_per_flavor_combo <= 0){
	cout<<"ERROR! Turn on at least one of the channels to include in bump_ee"<<endl;
	std::terminate();
    }
    for(int ibin = 0;ibin < channels_per_flavor_combo; ++ibin)
	h_yield->SetBinContent(ibin+1, h_yield->GetBinContent(ibin+1)*(1.0+bump_term)); //it's ibin+1 because binning starts at 1, not 0. 
}
void bump_mm(TH1F* h_yield, float bump_term,bool include_OSDL1, bool include_OSDL2, bool include_SSDL){
    //bump the mm bins by (1+bump_term)
    int channels_per_flavor_combo = (include_OSDL1?1:0) + (include_OSDL2?1:0) + (include_SSDL?1:0);
    if( channels_per_flavor_combo <= 0){
	cout<<"ERROR! Turn on at least one of the channels to include in bump_mm"<<endl;
	std::terminate();
    }
    for(int ibin = channels_per_flavor_combo;ibin < 2*channels_per_flavor_combo; ++ibin)
	h_yield->SetBinContent(ibin+1, h_yield->GetBinContent(ibin+1)*(1.0+bump_term));//it's ibin+1 because binning starts at 1, not 0. 
}
void bump_em(TH1F* h_yield, float bump_term,bool include_OSDL1, bool include_OSDL2, bool include_SSDL){
    //bump the em bins by (1+bump_term)
    int channels_per_flavor_combo = (include_OSDL1?1:0) + (include_OSDL2?1:0) + (include_SSDL?1:0);
    if( channels_per_flavor_combo <= 0){
	cout<<"ERROR! Turn on at least one of the channels to include in bump_em"<<endl;
	std::terminate();
    }
    for(int ibin = 2*channels_per_flavor_combo;ibin < 3*channels_per_flavor_combo; ++ibin)
	h_yield->SetBinContent(ibin+1, h_yield->GetBinContent(ibin+1)*(1.0+bump_term));//it's ibin+1 because binning starts at 1, not 0. 
}
