//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Oct  6 20:40:49 2016 by ROOT version 6.02/13
// from TTree ljmet/ljmet
// found on file: /user_data/rsyarif/LJMet80x_3lepTT_2016_8_31_rizki_step1hadds_dilepTrigReady/nominal/DoubleEG_PRB_hadd.root
//////////////////////////////////////////////////////////

#ifndef step2_h
#define step2_h

#include <iostream>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

using namespace std;

class step2 {
public :
   TTree          *inputTree;   //!pointer to the analyzed TTree or TChain
   TFile          *inputFile, *outputFile;
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Int_t           event_CommonCalc;
   Int_t           run_CommonCalc;
   Int_t           lumi_CommonCalc;
   Int_t           nPV_singleLepCalc;
   Int_t           nTrueInteractions_singleLepCalc;
   Int_t           isElectron;
   Int_t           isMuon;
   Int_t           MCPastTrigger;
   Int_t           MCPastTriggerAlt;
   Int_t           DataPastTrigger;
   Int_t           DataPastTriggerAlt;
   Bool_t          isTHBW_TpTpCalc;
   Bool_t          isTHTH_TpTpCalc;
   Bool_t          isBWBW_TpTpCalc;
   Bool_t          isTZBW_TpTpCalc;
   Bool_t          isTZTH_TpTpCalc;
   Bool_t          isTZTZ_TpTpCalc;
   Bool_t          isBHTW_TpTpCalc;
   Bool_t          isBHBH_TpTpCalc;
   Bool_t          isTWTW_TpTpCalc;
   Bool_t          isBZTW_TpTpCalc;
   Bool_t          isBZBH_TpTpCalc;
   Bool_t          isBZBZ_TpTpCalc;
   Int_t           NLeptonDecays_TpTpCalc;
   Double_t        MCWeight_singleLepCalc;
   vector<double>  *renormWeights;
   vector<float>   *pdfWeights;
   Float_t         JetSF_pTNbwflat;
   Float_t         JetSFup_pTNbwflat;
   Float_t         JetSFdn_pTNbwflat;
   Float_t         JetSFupwide_pTNbwflat;
   Float_t         JetSFdnwide_pTNbwflat;
   Float_t         pileupWeight;
   Float_t         pileupWeightUp;
   Float_t         pileupWeightDown;
   Float_t         TrigEffAltWeight;
   Float_t         TrigEffWeight;
   Float_t         TrigEffWeightUncert;
   Float_t         isoSF;
   Float_t         lepIdSF;
   Float_t         EGammaGsfSF;
   Float_t         MuTrkSF;
   Bool_t          isPassTrilepton;
   Int_t           isEEE;
   Int_t           isEEM;
   Int_t           isEMM;
   Int_t           isMMM;
   Int_t           isTTT;
   Int_t           isTTL;
   Int_t           isTLT;
   Int_t           isLTT;
   Int_t           isTLL;
   Int_t           isLTL;
   Int_t           isLLT;
   Int_t           isLLL;
   Int_t           MCPastTrigger_dilep;
   Int_t           DataPastTrigger_dilep;
   Int_t           MCPastTrigger_dilep_anth;
   Int_t           DataPastTrigger_dilep_anth;
   Int_t           MCPastTrigger_dilepHT;
   Int_t           DataPastTrigger_dilepHT;
   Int_t           MCPastTrigger_trilep;
   Int_t           DataPastTrigger_trilep;
   Double_t        ttbarMass_TTbarMassCalc;
   Double_t        corr_met_singleLepCalc;
   Double_t        corr_met_phi_singleLepCalc;
   Float_t         leptonPt_singleLepCalc;
   Float_t         leptonEta_singleLepCalc;
   Float_t         leptonPhi_singleLepCalc;
   Float_t         leptonEnergy_singleLepCalc;
   Float_t         leptonMiniIso_singleLepCalc;
   Float_t         leptonRelIso_singleLepCalc;
   Float_t         leptonDxy_singleLepCalc;
   Float_t         leptonDz_singleLepCalc;
   Int_t           leptonCharge_singleLepCalc;
   Int_t           elTrigPresel_singleLepCalc;
   vector<float>   *AllLeptonElPt_PtOrdered;
   vector<float>   *AllLeptonElEta_PtOrdered;
   vector<float>   *AllLeptonElPhi_PtOrdered;
   vector<float>   *AllLeptonElEnergy_PtOrdered;
   vector<float>   *AllLeptonElMiniIso_PtOrdered;
   vector<int>     *AllLeptonElFlavor_PtOrdered;
   vector<int>     *AllLeptonElIsTight_PtOrdered;
   vector<float>   *AllLeptonMuPt_PtOrdered;
   vector<float>   *AllLeptonMuEta_PtOrdered;
   vector<float>   *AllLeptonMuPhi_PtOrdered;
   vector<float>   *AllLeptonMuEnergy_PtOrdered;
   vector<float>   *AllLeptonMuMiniIso_PtOrdered;
   vector<int>     *AllLeptonMuFlavor_PtOrdered;
   vector<int>     *AllLeptonMuIsTight_PtOrdered;
   vector<float>   *AllLeptonPt_PtOrdered;
   vector<float>   *AllLeptonEta_PtOrdered;
   vector<float>   *AllLeptonPhi_PtOrdered;
   vector<float>   *AllLeptonEnergy_PtOrdered;
   vector<float>   *AllLeptonMiniIso_PtOrdered;
   vector<int>     *AllLeptonFlavor_PtOrdered;
   vector<int>     *AllLeptonIsTight_PtOrdered;
   vector<int>     *AllLeptonCharge_PtOrdered;
   Int_t           AllLeptonCount_PtOrdered;
   vector<float>   *TightLeptonPt_PtOrdered;
   vector<float>   *TightLeptonEta_PtOrdered;
   vector<float>   *TightLeptonPhi_PtOrdered;
   vector<float>   *TightLeptonEnergy_PtOrdered;
   vector<float>   *TightLeptonMiniIso_PtOrdered;
   vector<int>     *TightLeptonFlavor_PtOrdered;
   vector<int>     *TightLeptonCharge_PtOrdered;
   vector<double>  *theJetPt_JetSubCalc_PtOrdered;
   vector<double>  *theJetEta_JetSubCalc_PtOrdered;
   vector<double>  *theJetPhi_JetSubCalc_PtOrdered;
   vector<double>  *theJetEnergy_JetSubCalc_PtOrdered;
   vector<int>     *theJetBTag_JetSubCalc_PtOrdered;
   vector<int>     *theJetBTag_bSFup_JetSubCalc_PtOrdered;
   vector<int>     *theJetBTag_bSFdn_JetSubCalc_PtOrdered;
   vector<int>     *theJetBTag_lSFup_JetSubCalc_PtOrdered;
   vector<int>     *theJetBTag_lSFdn_JetSubCalc_PtOrdered;
   vector<int>     *HadronicVHtID_JetSubCalc;
   vector<double>  *HadronicVHtPt_JetSubCalc;
   vector<double>  *HadronicVHtEta_JetSubCalc;
   vector<double>  *HadronicVHtPhi_JetSubCalc;
   vector<double>  *HadronicVHtEnergy_JetSubCalc;
   vector<double>  *theJetAK8Pt_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8Eta_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8Phi_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8Energy_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8PrunedMass_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered;
   vector<float>   *theJetAK8SoftDropMass_JetSubCalc_PtOrdered;
   vector<float>   *theJetAK8MaxSubCSV_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8NjettinessTau1_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8NjettinessTau2_JetSubCalc_PtOrdered;
   vector<float>   *theJetAK8NjettinessTau3_JetSubCalc_PtOrdered;
   vector<int>     *theJetAK8Wmatch_JetSubCalc_PtOrdered;
   vector<int>     *theJetAK8Tmatch_JetSubCalc_PtOrdered;
   vector<int>     *theJetAK8Zmatch_JetSubCalc_PtOrdered;
   vector<int>     *theJetAK8Hmatch_JetSubCalc_PtOrdered;
   vector<double>  *theJetAK8MatchedPt_JetSubCalc_PtOrdered;
   vector<double>  *genJetPt_singleLepCalc;
   vector<double>  *genJetEta_singleLepCalc;
   vector<double>  *genJetPhi_singleLepCalc;
   vector<double>  *genJetEnergy_singleLepCalc;
   Float_t         BJetLeadPt;
   vector<double>  *BJetLeadPt_shifts;
   Float_t         WJetLeadPt;
   vector<double>  *WJetLeadPt_shifts;
   Float_t         TJetLeadPt;
   vector<double>  *TJetLeadPt_shifts;
   Float_t         AK4HTpMETpLepPt;
   Float_t         AK4HT;
   vector<float>   *ddBkgWeights;
   Int_t           NJets_JetSubCalc;
   Int_t           NJetsAK8_JetSubCalc;
   Int_t           NJetsCSVwithSF_JetSubCalc;
   Int_t           NJetsCSVwithSF_JetSubCalc_noLepCorr;
   vector<int>     *NJetsCSVwithSF_JetSubCalc_shifts;
   vector<int>     *NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts;
   Int_t           NJetsHtagged;
   vector<int>     *NJetsHtagged_shifts;
   Float_t         topPt;
   Float_t         topPtGen;
   Float_t         topMass;
   Float_t         minMleppBjet;
   vector<double>  *minMleppBjet_shifts;
   Float_t         minMleppJet;
   Float_t         genTopPt;
   Float_t         genAntiTopPt;
   Float_t         topPtWeight;
   Float_t         topPtWeightPast400;
   Float_t         topPtWeightHighPt;
   Float_t         deltaRlepJetInMinMljet;
   Float_t         deltaRlepbJetInMinMlb;
   vector<double>  *deltaRlepbJetInMinMlb_shifts;
   Float_t         deltaPhilepJetInMinMljet;
   Float_t         deltaPhilepbJetInMinMlb;
   vector<double>  *deltaPhilepbJetInMinMlb_shifts;
   Float_t         deltaRtopWjet;
   Float_t         deltaRlepWjet;
   Float_t         deltaRlepTjet;
   Float_t         deltaPhitopWjet;
   Float_t         deltaPhilepWjet;
   Float_t         deltaPhilepTjet;
   vector<double>  *deltaRtopWjet_shifts;
   vector<double>  *deltaRlepWjet_shifts;
   vector<double>  *deltaRlepTjet_shifts;
   vector<double>  *deltaPhitopWjet_shifts;
   vector<double>  *deltaPhilepWjet_shifts;
   vector<double>  *deltaPhilepTjet_shifts;
   Int_t           NJetsWtagged_0p6;
   vector<int>     *NJetsWtagged_0p6_shifts;
   Int_t           NJetsTtagged_0p81;
   vector<int>     *NJetsTtagged_0p81_shifts;
   Float_t         minDR_leadAK8otherAK8;
   Float_t         minDR_lepAK8;
   Float_t         minDR_lepJet;
   Float_t         ptRel_lepJet;
   Float_t         MT_lepMet;
   vector<float>   *deltaR_lepJets;
   vector<float>   *deltaR_lepBJets;
   vector<double>  *deltaR_lepBJets_bSFup;
   vector<double>  *deltaR_lepBJets_bSFdn;
   vector<double>  *deltaR_lepBJets_lSFup;
   vector<double>  *deltaR_lepBJets_lSFdn;
   vector<double>  *deltaR_lepAK8s;
   vector<double>  *deltaPhi_lepJets;
   vector<double>  *deltaPhi_lepBJets;
   vector<double>  *deltaPhi_lepBJets_bSFup;
   vector<double>  *deltaPhi_lepBJets_bSFdn;
   vector<double>  *deltaPhi_lepBJets_lSFup;
   vector<double>  *deltaPhi_lepBJets_lSFdn;
   vector<double>  *deltaPhi_lepAK8s;
   vector<double>  *mass_lepJets;
   vector<double>  *mass_lepBJets;
   vector<double>  *mass_lepBJets_bSFup;
   vector<double>  *mass_lepBJets_bSFdn;
   vector<double>  *mass_lepBJets_lSFup;
   vector<double>  *mass_lepBJets_lSFdn;
   vector<double>  *mass_lepAK8s;
   vector<float>   *minDR_lepJets;
   vector<float>   *minDR_lepBJets;
   vector<float>   *deltaR_lep1Jets;
   vector<float>   *deltaR_lep2Jets;
   vector<float>   *deltaR_lep3Jets;
   vector<float>   *deltaR_lepClosestJet;
   vector<float>   *PtRelLepClosestJet;
   Float_t         Mll_sameFlavorOS;
   vector<float>   *MllOS_allComb;
   Float_t         MllOS_allComb_min;
   Float_t         MllOS_allComb_max;
   Float_t         Mlll;

   // List of branches
   TBranch        *b_event_CommonCalc;   //!
   TBranch        *b_run_CommonCalc;   //!
   TBranch        *b_lumi_CommonCalc;   //!
   TBranch        *b_nPV_singleLepCalc;   //!
   TBranch        *b_nTrueInteractions_singleLepCalc;   //!
   TBranch        *b_isElectron;   //!
   TBranch        *b_isMuon;   //!
   TBranch        *b_MCPastTrigger;   //!
   TBranch        *b_MCPastTriggerAlt;   //!
   TBranch        *b_DataPastTrigger;   //!
   TBranch        *b_DataPastTriggerAlt;   //!
   TBranch        *b_isTHBW_TpTpCalc;   //!
   TBranch        *b_isTHTH_TpTpCalc;   //!
   TBranch        *b_isBWBW_TpTpCalc;   //!
   TBranch        *b_isTZBW_TpTpCalc;   //!
   TBranch        *b_isTZTH_TpTpCalc;   //!
   TBranch        *b_isTZTZ_TpTpCalc;   //!
   TBranch        *b_isBHTW_TpTpCalc;   //!
   TBranch        *b_isBHBH_TpTpCalc;   //!
   TBranch        *b_isTWTW_TpTpCalc;   //!
   TBranch        *b_isBZTW_TpTpCalc;   //!
   TBranch        *b_isBZBH_TpTpCalc;   //!
   TBranch        *b_isBZBZ_TpTpCalc;   //!
   TBranch        *b_NLeptonDecays_TpTpCalc;   //!
   TBranch        *b_MCWeight_singleLepCalc;   //!
   TBranch        *b_renormWeights;   //!
   TBranch        *b_pdfWeights;   //!
   TBranch        *b_JetSF_pTNbwflat;   //!
   TBranch        *b_JetSFup_pTNbwflat;   //!
   TBranch        *b_JetSFdn_pTNbwflat;   //!
   TBranch        *b_JetSFupwide_pTNbwflat;   //!
   TBranch        *b_JetSFdnwide_pTNbwflat;   //!
   TBranch        *b_pileupWeight;   //!
   TBranch        *b_pileupWeightUp;   //!
   TBranch        *b_pileupWeightDown;   //!
   TBranch        *b_TrigEffAltWeight;   //!
   TBranch        *b_TrigEffWeight;   //!
   TBranch        *b_TrigEffWeightUncert;   //!
   TBranch        *b_isoSF;   //!
   TBranch        *b_lepIdSF;   //!
   TBranch        *b_EGammaGsfSF;   //!
   TBranch        *b_MuTrkSF;   //!
   TBranch        *b_isPassTrilepton;   //!
   TBranch        *b_isEEE;   //!
   TBranch        *b_isEEM;   //!
   TBranch        *b_isEMM;   //!
   TBranch        *b_isMMM;   //!
   TBranch        *b_isTTT;   //!
   TBranch        *b_isTTL;   //!
   TBranch        *b_isTLT;   //!
   TBranch        *b_isLTT;   //!
   TBranch        *b_isTLL;   //!
   TBranch        *b_isLTL;   //!
   TBranch        *b_isLLT;   //!
   TBranch        *b_isLLL;   //!
   TBranch        *b_MCPastTrigger_dilep;   //!
   TBranch        *b_DataPastTrigger_dilep;   //!
   TBranch        *b_MCPastTrigger_dilep_anth;   //!
   TBranch        *b_DataPastTrigger_dilep_anth;   //!
   TBranch        *b_MCPastTrigger_dilepHT;   //!
   TBranch        *b_DataPastTrigger_dilepHT;   //!
   TBranch        *b_MCPastTrigger_trilep;   //!
   TBranch        *b_DataPastTrigger_trilep;   //!
   TBranch        *b_ttbarMass_TTbarMassCalc;   //!
   TBranch        *b_corr_met_singleLepCalc;   //!
   TBranch        *b_corr_met_phi_singleLepCalc;   //!
   TBranch        *b_leptonPt_singleLepCalc;   //!
   TBranch        *b_leptonEta_singleLepCalc;   //!
   TBranch        *b_leptonPhi_singleLepCalc;   //!
   TBranch        *b_leptonEnergy_singleLepCalc;   //!
   TBranch        *b_leptonMiniIso_singleLepCalc;   //!
   TBranch        *b_leptonRelIso_singleLepCalc;   //!
   TBranch        *b_leptonDxy_singleLepCalc;   //!
   TBranch        *b_leptonDz_singleLepCalc;   //!
   TBranch        *b_leptonCharge_singleLepCalc;   //!
   TBranch        *b_elTrigPresel_singleLepCalc;   //!
   TBranch        *b_AllLeptonElPt_PtOrdered;   //!
   TBranch        *b_AllLeptonElEta_PtOrdered;   //!
   TBranch        *b_AllLeptonElPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonElEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonElMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonElFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonElIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonMuPt_PtOrdered;   //!
   TBranch        *b_AllLeptonMuEta_PtOrdered;   //!
   TBranch        *b_AllLeptonMuPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonMuEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonMuMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonMuFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonMuIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonPt_PtOrdered;   //!
   TBranch        *b_AllLeptonEta_PtOrdered;   //!
   TBranch        *b_AllLeptonPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonCharge_PtOrdered;   //!
   TBranch        *b_AllLeptonCount_PtOrdered;   //!
   TBranch        *b_TightLeptonPt_PtOrdered;   //!
   TBranch        *b_TightLeptonEta_PtOrdered;   //!
   TBranch        *b_TightLeptonPhi_PtOrdered;   //!
   TBranch        *b_TightLeptonEnergy_PtOrdered;   //!
   TBranch        *b_TightLeptonMiniIso_PtOrdered;   //!
   TBranch        *b_TightLeptonFlavor_PtOrdered;   //!
   TBranch        *b_TightLeptonCharge_PtOrdered;   //!
   TBranch        *b_theJetPt_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetEta_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetPhi_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetEnergy_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetBTag_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetBTag_bSFup_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetBTag_bSFdn_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetBTag_lSFup_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetBTag_lSFdn_JetSubCalc_PtOrdered;   //!
   TBranch        *b_HadronicVHtID_JetSubCalc;   //!
   TBranch        *b_HadronicVHtPt_JetSubCalc;   //!
   TBranch        *b_HadronicVHtEta_JetSubCalc;   //!
   TBranch        *b_HadronicVHtPhi_JetSubCalc;   //!
   TBranch        *b_HadronicVHtEnergy_JetSubCalc;   //!
   TBranch        *b_theJetAK8Pt_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Eta_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Phi_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Energy_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8PrunedMass_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8SoftDropMass_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8MaxSubCSV_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8NjettinessTau1_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8NjettinessTau2_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8NjettinessTau3_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Wmatch_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Tmatch_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Zmatch_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8Hmatch_JetSubCalc_PtOrdered;   //!
   TBranch        *b_theJetAK8MatchedPt_JetSubCalc_PtOrdered;   //!
   TBranch        *b_genJetPt_singleLepCalc;   //!
   TBranch        *b_genJetEta_singleLepCalc;   //!
   TBranch        *b_genJetPhi_singleLepCalc;   //!
   TBranch        *b_genJetEnergy_singleLepCalc;   //!
   TBranch        *b_BJetLeadPt;   //!
   TBranch        *b_BJetLeadPt_shifts;   //!
   TBranch        *b_WJetLeadPt;   //!
   TBranch        *b_WJetLeadPt_shifts;   //!
   TBranch        *b_TJetLeadPt;   //!
   TBranch        *b_TJetLeadPt_shifts;   //!
   TBranch        *b_AK4HTpMETpLepPt;   //!
   TBranch        *b_AK4HT;   //!
   TBranch        *b_ddBkgWeights;   //!
   TBranch        *b_NJets_JetSubCalc;   //!
   TBranch        *b_NJetsAK8_JetSubCalc;   //!
   TBranch        *b_NJetsCSVwithSF_JetSubCalc;   //!
   TBranch        *b_NJetsCSVwithSF_JetSubCalc_noLepCorr;   //!
   TBranch        *b_NJetsCSVwithSF_JetSubCalc_shifts;   //!
   TBranch        *b_NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts;   //!
   TBranch        *b_NJetsHtagged;   //!
   TBranch        *b_NJetsHtagged_shifts;   //!
   TBranch        *b_topPt;   //!
   TBranch        *b_topPtGen;   //!
   TBranch        *b_topMass;   //!
   TBranch        *b_minMleppBjet;   //!
   TBranch        *b_minMleppBjet_shifts;   //!
   TBranch        *b_mixnMleppJet;   //!
   TBranch        *b_genTopPt;   //!
   TBranch        *b_genAntiTopPt;   //!
   TBranch        *b_topPtWeight;   //!
   TBranch        *b_topPtWeightPast400;   //!
   TBranch        *b_topPtWeightHighPt;   //!
   TBranch        *b_deltaRlepJetInMinMljet;   //!
   TBranch        *b_deltaRlepbJetInMinMlb;   //!
   TBranch        *b_deltaRlepbJetInMinMlb_shifts;   //!
   TBranch        *b_deltaPhilepJetInMinMljet;   //!
   TBranch        *b_deltaPhilepbJetInMinMlb;   //!
   TBranch        *b_deltaPhilepbJetInMinMlb_shifts;   //!
   TBranch        *b_deltaRtopWjet;   //!
   TBranch        *b_deltaRlepWjet;   //!
   TBranch        *b_deltaRlepTjet;   //!
   TBranch        *b_deltaPhitopWjet;   //!
   TBranch        *b_deltaPhilepWjet;   //!
   TBranch        *b_deltaPhilepTjet;   //!
   TBranch        *b_deltaRtopWjet_shifts;   //!
   TBranch        *b_deltaRlepWjet_shifts;   //!
   TBranch        *b_deltaRlepTjet_shifts;   //!
   TBranch        *b_deltaPhitopWjet_shifts;   //!
   TBranch        *b_deltaPhilepWjet_shifts;   //!
   TBranch        *b_deltaPhilepTjet_shifts;   //!
   TBranch        *b_NJetsWtagged_0p6;   //!
   TBranch        *b_NJetsWtagged_0p6_shifts;   //!
   TBranch        *b_NJetsTtagged_0p81;   //!
   TBranch        *b_NJetsTtagged_0p81_shifts;   //!
   TBranch        *b_minDR_leadAK8otherAK8;   //!
   TBranch        *b_minDR_lepAK8;   //!
   TBranch        *b_minDR_lepJet;   //!
   TBranch        *b_ptRel_lepJet;   //!
   TBranch        *b_MT_lepMet;   //!
   TBranch        *b_deltaR_lepJets;   //!
   TBranch        *b_deltaR_lepBJets;   //!
   TBranch        *b_deltaR_lepBJets_bSFup;   //!
   TBranch        *b_deltaR_lepBJets_bSFdn;   //!
   TBranch        *b_deltaR_lepBJets_lSFup;   //!
   TBranch        *b_deltaR_lepBJets_lSFdn;   //!
   TBranch        *b_deltaR_lepAK8s;   //!
   TBranch        *b_deltaPhi_lepJets;   //!
   TBranch        *b_deltaPhi_lepBJets;   //!
   TBranch        *b_deltaPhi_lepBJets_bSFup;   //!
   TBranch        *b_deltaPhi_lepBJets_bSFdn;   //!
   TBranch        *b_deltaPhi_lepBJets_lSFup;   //!
   TBranch        *b_deltaPhi_lepBJets_lSFdn;   //!
   TBranch        *b_deltaPhi_lepAK8s;   //!
   TBranch        *b_mass_lepJets;   //!
   TBranch        *b_mass_lepBJets;   //!
   TBranch        *b_mass_lepBJets_bSFup;   //!
   TBranch        *b_mass_lepBJets_bSFdn;   //!
   TBranch        *b_mass_lepBJets_lSFup;   //!
   TBranch        *b_mass_lepBJets_lSFdn;   //!
   TBranch        *b_mass_lepAK8s;   //!
   TBranch        *b_minDR_lepJets;   //!
   TBranch        *b_minDR_lepBJets;   //!
   TBranch        *b_deltaR_lep1Jets;   //!
   TBranch        *b_deltaR_lep2Jets;   //!
   TBranch        *b_deltaR_lep3Jets;   //!
   TBranch        *b_deltaR_lepClosestJet;   //!
   TBranch        *b_PtRelLepClosestJet;   //!
   TBranch        *b_Mll_sameFlavorOS;   //!
   TBranch        *b_MllOS_allComb;   //!
   TBranch        *b_MllOS_allComb_min;   //!
   TBranch        *b_MllOS_allComb_max;   //!
   TBranch        *b_Mlll;   //!

   step2(TString inputFileName, TString outputFileName);
   virtual ~step2();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef step2_cxx
step2::step2(TString inputFileName, TString outputFileName) : inputTree(0), inputFile(0), outputFile(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
  std::cout<<"Opening file: "<<inputFileName<<std::endl;
  inputFile=TFile::Open(inputFileName);
  inputTree=(TTree*)inputFile->Get("ljmet");
  if(inputTree->GetEntries()==0) std::cout<<"WARNING! Found 0 events in the tree!!!!"<<std::endl;;
  
  outputFile=new TFile(outputFileName,"RECREATE");   
  
  Init(inputTree);
}

step2::~step2()
{
   if (!inputTree) return;
   delete inputTree->GetCurrentFile();
}

Int_t step2::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!inputTree) return 0;
   return inputTree->GetEntry(entry);
}
Long64_t step2::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!inputTree) return -5;
   Long64_t centry = inputTree->LoadTree(entry);
   if (centry < 0) return centry;
   if (inputTree->GetTreeNumber() != fCurrent) {
      fCurrent = inputTree->GetTreeNumber();
      Notify();
   }
   return centry;
}

void step2::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   renormWeights = 0;
   pdfWeights = 0;
   AllLeptonElPt_PtOrdered = 0;
   AllLeptonElEta_PtOrdered = 0;
   AllLeptonElPhi_PtOrdered = 0;
   AllLeptonElEnergy_PtOrdered = 0;
   AllLeptonElMiniIso_PtOrdered = 0;
   AllLeptonElFlavor_PtOrdered = 0;
   AllLeptonElIsTight_PtOrdered = 0;
   AllLeptonMuPt_PtOrdered = 0;
   AllLeptonMuEta_PtOrdered = 0;
   AllLeptonMuPhi_PtOrdered = 0;
   AllLeptonMuEnergy_PtOrdered = 0;
   AllLeptonMuMiniIso_PtOrdered = 0;
   AllLeptonMuFlavor_PtOrdered = 0;
   AllLeptonMuIsTight_PtOrdered = 0;
   AllLeptonPt_PtOrdered = 0;
   AllLeptonEta_PtOrdered = 0;
   AllLeptonPhi_PtOrdered = 0;
   AllLeptonEnergy_PtOrdered = 0;
   AllLeptonMiniIso_PtOrdered = 0;
   AllLeptonFlavor_PtOrdered = 0;
   AllLeptonIsTight_PtOrdered = 0;
   AllLeptonCharge_PtOrdered = 0;
   TightLeptonPt_PtOrdered = 0;
   TightLeptonEta_PtOrdered = 0;
   TightLeptonPhi_PtOrdered = 0;
   TightLeptonEnergy_PtOrdered = 0;
   TightLeptonMiniIso_PtOrdered = 0;
   TightLeptonFlavor_PtOrdered = 0;
   TightLeptonCharge_PtOrdered = 0;
   theJetPt_JetSubCalc_PtOrdered = 0;
   theJetEta_JetSubCalc_PtOrdered = 0;
   theJetPhi_JetSubCalc_PtOrdered = 0;
   theJetEnergy_JetSubCalc_PtOrdered = 0;
   theJetBTag_JetSubCalc_PtOrdered = 0;
   theJetBTag_bSFup_JetSubCalc_PtOrdered = 0;
   theJetBTag_bSFdn_JetSubCalc_PtOrdered = 0;
   theJetBTag_lSFup_JetSubCalc_PtOrdered = 0;
   theJetBTag_lSFdn_JetSubCalc_PtOrdered = 0;
   HadronicVHtID_JetSubCalc = 0;
   HadronicVHtPt_JetSubCalc = 0;
   HadronicVHtEta_JetSubCalc = 0;
   HadronicVHtPhi_JetSubCalc = 0;
   HadronicVHtEnergy_JetSubCalc = 0;
   theJetAK8Pt_JetSubCalc_PtOrdered = 0;
   theJetAK8Eta_JetSubCalc_PtOrdered = 0;
   theJetAK8Phi_JetSubCalc_PtOrdered = 0;
   theJetAK8Energy_JetSubCalc_PtOrdered = 0;
   theJetAK8PrunedMass_JetSubCalc_PtOrdered = 0;
   theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered = 0;
   theJetAK8SoftDropMass_JetSubCalc_PtOrdered = 0;
   theJetAK8MaxSubCSV_JetSubCalc_PtOrdered = 0;
   theJetAK8NjettinessTau1_JetSubCalc_PtOrdered = 0;
   theJetAK8NjettinessTau2_JetSubCalc_PtOrdered = 0;
   theJetAK8NjettinessTau3_JetSubCalc_PtOrdered = 0;
   theJetAK8Wmatch_JetSubCalc_PtOrdered = 0;
   theJetAK8Tmatch_JetSubCalc_PtOrdered = 0;
   theJetAK8Zmatch_JetSubCalc_PtOrdered = 0;
   theJetAK8Hmatch_JetSubCalc_PtOrdered = 0;
   theJetAK8MatchedPt_JetSubCalc_PtOrdered = 0;
   genJetPt_singleLepCalc = 0;
   genJetEta_singleLepCalc = 0;
   genJetPhi_singleLepCalc = 0;
   genJetEnergy_singleLepCalc = 0;
   BJetLeadPt_shifts = 0;
   WJetLeadPt_shifts = 0;
   TJetLeadPt_shifts = 0;
   ddBkgWeights = 0;
   NJetsCSVwithSF_JetSubCalc_shifts = 0;
   NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts = 0;
   NJetsHtagged_shifts = 0;
   minMleppBjet_shifts = 0;
   deltaRlepbJetInMinMlb_shifts = 0;
   deltaPhilepbJetInMinMlb_shifts = 0;
   deltaRtopWjet_shifts = 0;
   deltaRlepWjet_shifts = 0;
   deltaRlepTjet_shifts = 0;
   deltaPhitopWjet_shifts = 0;
   deltaPhilepWjet_shifts = 0;
   deltaPhilepTjet_shifts = 0;
   NJetsWtagged_0p6_shifts = 0;
   NJetsTtagged_0p81_shifts = 0;
   deltaR_lepJets = 0;
   deltaR_lepBJets = 0;
   deltaR_lepBJets_bSFup = 0;
   deltaR_lepBJets_bSFdn = 0;
   deltaR_lepBJets_lSFup = 0;
   deltaR_lepBJets_lSFdn = 0;
   deltaR_lepAK8s = 0;
   deltaPhi_lepJets = 0;
   deltaPhi_lepBJets = 0;
   deltaPhi_lepBJets_bSFup = 0;
   deltaPhi_lepBJets_bSFdn = 0;
   deltaPhi_lepBJets_lSFup = 0;
   deltaPhi_lepBJets_lSFdn = 0;
   deltaPhi_lepAK8s = 0;
   mass_lepJets = 0;
   mass_lepBJets = 0;
   mass_lepBJets_bSFup = 0;
   mass_lepBJets_bSFdn = 0;
   mass_lepBJets_lSFup = 0;
   mass_lepBJets_lSFdn = 0;
   mass_lepAK8s = 0;
   minDR_lepJets = 0;
   minDR_lepBJets = 0;
   deltaR_lep1Jets = 0;
   deltaR_lep2Jets = 0;
   deltaR_lep3Jets = 0;
   deltaR_lepClosestJet = 0;
   PtRelLepClosestJet = 0;
   MllOS_allComb = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   inputTree = tree;
   fCurrent = -1;
   inputTree->SetMakeClass(1);

   inputTree->SetBranchAddress("event_CommonCalc", &event_CommonCalc, &b_event_CommonCalc);
   inputTree->SetBranchAddress("run_CommonCalc", &run_CommonCalc, &b_run_CommonCalc);
   inputTree->SetBranchAddress("lumi_CommonCalc", &lumi_CommonCalc, &b_lumi_CommonCalc);
   inputTree->SetBranchAddress("nPV_singleLepCalc", &nPV_singleLepCalc, &b_nPV_singleLepCalc);
   inputTree->SetBranchAddress("nTrueInteractions_singleLepCalc", &nTrueInteractions_singleLepCalc, &b_nTrueInteractions_singleLepCalc);
   inputTree->SetBranchAddress("isElectron", &isElectron, &b_isElectron);
   inputTree->SetBranchAddress("isMuon", &isMuon, &b_isMuon);
   inputTree->SetBranchAddress("MCPastTrigger", &MCPastTrigger, &b_MCPastTrigger);
   inputTree->SetBranchAddress("MCPastTriggerAlt", &MCPastTriggerAlt, &b_MCPastTriggerAlt);
   inputTree->SetBranchAddress("DataPastTrigger", &DataPastTrigger, &b_DataPastTrigger);
   inputTree->SetBranchAddress("DataPastTriggerAlt", &DataPastTriggerAlt, &b_DataPastTriggerAlt);
   inputTree->SetBranchAddress("isTHBW_TpTpCalc", &isTHBW_TpTpCalc, &b_isTHBW_TpTpCalc);
   inputTree->SetBranchAddress("isTHTH_TpTpCalc", &isTHTH_TpTpCalc, &b_isTHTH_TpTpCalc);
   inputTree->SetBranchAddress("isBWBW_TpTpCalc", &isBWBW_TpTpCalc, &b_isBWBW_TpTpCalc);
   inputTree->SetBranchAddress("isTZBW_TpTpCalc", &isTZBW_TpTpCalc, &b_isTZBW_TpTpCalc);
   inputTree->SetBranchAddress("isTZTH_TpTpCalc", &isTZTH_TpTpCalc, &b_isTZTH_TpTpCalc);
   inputTree->SetBranchAddress("isTZTZ_TpTpCalc", &isTZTZ_TpTpCalc, &b_isTZTZ_TpTpCalc);
   inputTree->SetBranchAddress("isBHTW_TpTpCalc", &isBHTW_TpTpCalc, &b_isBHTW_TpTpCalc);
   inputTree->SetBranchAddress("isBHBH_TpTpCalc", &isBHBH_TpTpCalc, &b_isBHBH_TpTpCalc);
   inputTree->SetBranchAddress("isTWTW_TpTpCalc", &isTWTW_TpTpCalc, &b_isTWTW_TpTpCalc);
   inputTree->SetBranchAddress("isBZTW_TpTpCalc", &isBZTW_TpTpCalc, &b_isBZTW_TpTpCalc);
   inputTree->SetBranchAddress("isBZBH_TpTpCalc", &isBZBH_TpTpCalc, &b_isBZBH_TpTpCalc);
   inputTree->SetBranchAddress("isBZBZ_TpTpCalc", &isBZBZ_TpTpCalc, &b_isBZBZ_TpTpCalc);
   inputTree->SetBranchAddress("NLeptonDecays_TpTpCalc", &NLeptonDecays_TpTpCalc, &b_NLeptonDecays_TpTpCalc);
   inputTree->SetBranchAddress("MCWeight_singleLepCalc", &MCWeight_singleLepCalc, &b_MCWeight_singleLepCalc);
   inputTree->SetBranchAddress("renormWeights", &renormWeights, &b_renormWeights);
   inputTree->SetBranchAddress("pdfWeights", &pdfWeights, &b_pdfWeights);
   inputTree->SetBranchAddress("JetSF_pTNbwflat", &JetSF_pTNbwflat, &b_JetSF_pTNbwflat);
   inputTree->SetBranchAddress("JetSFup_pTNbwflat", &JetSFup_pTNbwflat, &b_JetSFup_pTNbwflat);
   inputTree->SetBranchAddress("JetSFdn_pTNbwflat", &JetSFdn_pTNbwflat, &b_JetSFdn_pTNbwflat);
   inputTree->SetBranchAddress("JetSFupwide_pTNbwflat", &JetSFupwide_pTNbwflat, &b_JetSFupwide_pTNbwflat);
   inputTree->SetBranchAddress("JetSFdnwide_pTNbwflat", &JetSFdnwide_pTNbwflat, &b_JetSFdnwide_pTNbwflat);
   inputTree->SetBranchAddress("pileupWeight", &pileupWeight, &b_pileupWeight);
   inputTree->SetBranchAddress("pileupWeightUp", &pileupWeightUp, &b_pileupWeightUp);
   inputTree->SetBranchAddress("pileupWeightDown", &pileupWeightDown, &b_pileupWeightDown);
   inputTree->SetBranchAddress("TrigEffAltWeight", &TrigEffAltWeight, &b_TrigEffAltWeight);
   inputTree->SetBranchAddress("TrigEffWeight", &TrigEffWeight, &b_TrigEffWeight);
   inputTree->SetBranchAddress("TrigEffWeightUncert", &TrigEffWeightUncert, &b_TrigEffWeightUncert);
   inputTree->SetBranchAddress("isoSF", &isoSF, &b_isoSF);
   inputTree->SetBranchAddress("lepIdSF", &lepIdSF, &b_lepIdSF);
   inputTree->SetBranchAddress("EGammaGsfSF", &EGammaGsfSF, &b_EGammaGsfSF);
   inputTree->SetBranchAddress("MuTrkSF", &MuTrkSF, &b_MuTrkSF);
   inputTree->SetBranchAddress("isPassTrilepton", &isPassTrilepton, &b_isPassTrilepton);
   inputTree->SetBranchAddress("isEEE", &isEEE, &b_isEEE);
   inputTree->SetBranchAddress("isEEM", &isEEM, &b_isEEM);
   inputTree->SetBranchAddress("isEMM", &isEMM, &b_isEMM);
   inputTree->SetBranchAddress("isMMM", &isMMM, &b_isMMM);
   inputTree->SetBranchAddress("isTTT", &isTTT, &b_isTTT);
   inputTree->SetBranchAddress("isTTL", &isTTL, &b_isTTL);
   inputTree->SetBranchAddress("isTLT", &isTLT, &b_isTLT);
   inputTree->SetBranchAddress("isLTT", &isLTT, &b_isLTT);
   inputTree->SetBranchAddress("isTLL", &isTLL, &b_isTLL);
   inputTree->SetBranchAddress("isLTL", &isLTL, &b_isLTL);
   inputTree->SetBranchAddress("isLLT", &isLLT, &b_isLLT);
   inputTree->SetBranchAddress("isLLL", &isLLL, &b_isLLL);
//    inputTree->SetBranchAddress("MCPastTrigger", &MCPastTrigger, &b_MCPastTrigger);
//    inputTree->SetBranchAddress("MCPastTriggerAlt", &MCPastTriggerAlt, &b_MCPastTriggerAlt);
//    inputTree->SetBranchAddress("DataPastTrigger", &DataPastTrigger, &b_DataPastTrigger);
//    inputTree->SetBranchAddress("DataPastTriggerAlt", &DataPastTriggerAlt, &b_DataPastTriggerAlt);
   inputTree->SetBranchAddress("MCPastTrigger_dilep", &MCPastTrigger_dilep, &b_MCPastTrigger_dilep);
   inputTree->SetBranchAddress("DataPastTrigger_dilep", &DataPastTrigger_dilep, &b_DataPastTrigger_dilep);
   inputTree->SetBranchAddress("MCPastTrigger_dilep_anth", &MCPastTrigger_dilep_anth, &b_MCPastTrigger_dilep_anth);
   inputTree->SetBranchAddress("DataPastTrigger_dilep_anth", &DataPastTrigger_dilep_anth, &b_DataPastTrigger_dilep_anth);
   inputTree->SetBranchAddress("MCPastTrigger_dilepHT", &MCPastTrigger_dilepHT, &b_MCPastTrigger_dilepHT);
   inputTree->SetBranchAddress("DataPastTrigger_dilepHT", &DataPastTrigger_dilepHT, &b_DataPastTrigger_dilepHT);
   inputTree->SetBranchAddress("MCPastTrigger_trilep", &MCPastTrigger_trilep, &b_MCPastTrigger_trilep);
   inputTree->SetBranchAddress("DataPastTrigger_trilep", &DataPastTrigger_trilep, &b_DataPastTrigger_trilep);
   inputTree->SetBranchAddress("ttbarMass_TTbarMassCalc", &ttbarMass_TTbarMassCalc, &b_ttbarMass_TTbarMassCalc);
   inputTree->SetBranchAddress("corr_met_singleLepCalc", &corr_met_singleLepCalc, &b_corr_met_singleLepCalc);
   inputTree->SetBranchAddress("corr_met_phi_singleLepCalc", &corr_met_phi_singleLepCalc, &b_corr_met_phi_singleLepCalc);
   inputTree->SetBranchAddress("leptonPt_singleLepCalc", &leptonPt_singleLepCalc, &b_leptonPt_singleLepCalc);
   inputTree->SetBranchAddress("leptonEta_singleLepCalc", &leptonEta_singleLepCalc, &b_leptonEta_singleLepCalc);
   inputTree->SetBranchAddress("leptonPhi_singleLepCalc", &leptonPhi_singleLepCalc, &b_leptonPhi_singleLepCalc);
   inputTree->SetBranchAddress("leptonEnergy_singleLepCalc", &leptonEnergy_singleLepCalc, &b_leptonEnergy_singleLepCalc);
   inputTree->SetBranchAddress("leptonMiniIso_singleLepCalc", &leptonMiniIso_singleLepCalc, &b_leptonMiniIso_singleLepCalc);
   inputTree->SetBranchAddress("leptonRelIso_singleLepCalc", &leptonRelIso_singleLepCalc, &b_leptonRelIso_singleLepCalc);
   inputTree->SetBranchAddress("leptonDxy_singleLepCalc", &leptonDxy_singleLepCalc, &b_leptonDxy_singleLepCalc);
   inputTree->SetBranchAddress("leptonDz_singleLepCalc", &leptonDz_singleLepCalc, &b_leptonDz_singleLepCalc);
   inputTree->SetBranchAddress("leptonCharge_singleLepCalc", &leptonCharge_singleLepCalc, &b_leptonCharge_singleLepCalc);
   inputTree->SetBranchAddress("elTrigPresel_singleLepCalc", &elTrigPresel_singleLepCalc, &b_elTrigPresel_singleLepCalc);
   inputTree->SetBranchAddress("AllLeptonElPt_PtOrdered", &AllLeptonElPt_PtOrdered, &b_AllLeptonElPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElEta_PtOrdered", &AllLeptonElEta_PtOrdered, &b_AllLeptonElEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElPhi_PtOrdered", &AllLeptonElPhi_PtOrdered, &b_AllLeptonElPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElEnergy_PtOrdered", &AllLeptonElEnergy_PtOrdered, &b_AllLeptonElEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElMiniIso_PtOrdered", &AllLeptonElMiniIso_PtOrdered, &b_AllLeptonElMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElFlavor_PtOrdered", &AllLeptonElFlavor_PtOrdered, &b_AllLeptonElFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElIsTight_PtOrdered", &AllLeptonElIsTight_PtOrdered, &b_AllLeptonElIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuPt_PtOrdered", &AllLeptonMuPt_PtOrdered, &b_AllLeptonMuPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuEta_PtOrdered", &AllLeptonMuEta_PtOrdered, &b_AllLeptonMuEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuPhi_PtOrdered", &AllLeptonMuPhi_PtOrdered, &b_AllLeptonMuPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuEnergy_PtOrdered", &AllLeptonMuEnergy_PtOrdered, &b_AllLeptonMuEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuMiniIso_PtOrdered", &AllLeptonMuMiniIso_PtOrdered, &b_AllLeptonMuMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuFlavor_PtOrdered", &AllLeptonMuFlavor_PtOrdered, &b_AllLeptonMuFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuIsTight_PtOrdered", &AllLeptonMuIsTight_PtOrdered, &b_AllLeptonMuIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonPt_PtOrdered", &AllLeptonPt_PtOrdered, &b_AllLeptonPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonEta_PtOrdered", &AllLeptonEta_PtOrdered, &b_AllLeptonEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonPhi_PtOrdered", &AllLeptonPhi_PtOrdered, &b_AllLeptonPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonEnergy_PtOrdered", &AllLeptonEnergy_PtOrdered, &b_AllLeptonEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMiniIso_PtOrdered", &AllLeptonMiniIso_PtOrdered, &b_AllLeptonMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonFlavor_PtOrdered", &AllLeptonFlavor_PtOrdered, &b_AllLeptonFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonIsTight_PtOrdered", &AllLeptonIsTight_PtOrdered, &b_AllLeptonIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonCharge_PtOrdered", &AllLeptonCharge_PtOrdered, &b_AllLeptonCharge_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonCount_PtOrdered", &AllLeptonCount_PtOrdered, &b_AllLeptonCount_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonPt_PtOrdered", &TightLeptonPt_PtOrdered, &b_TightLeptonPt_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonEta_PtOrdered", &TightLeptonEta_PtOrdered, &b_TightLeptonEta_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonPhi_PtOrdered", &TightLeptonPhi_PtOrdered, &b_TightLeptonPhi_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonEnergy_PtOrdered", &TightLeptonEnergy_PtOrdered, &b_TightLeptonEnergy_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonMiniIso_PtOrdered", &TightLeptonMiniIso_PtOrdered, &b_TightLeptonMiniIso_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonFlavor_PtOrdered", &TightLeptonFlavor_PtOrdered, &b_TightLeptonFlavor_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonCharge_PtOrdered", &TightLeptonCharge_PtOrdered, &b_TightLeptonCharge_PtOrdered);
   inputTree->SetBranchAddress("theJetPt_JetSubCalc_PtOrdered", &theJetPt_JetSubCalc_PtOrdered, &b_theJetPt_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetEta_JetSubCalc_PtOrdered", &theJetEta_JetSubCalc_PtOrdered, &b_theJetEta_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetPhi_JetSubCalc_PtOrdered", &theJetPhi_JetSubCalc_PtOrdered, &b_theJetPhi_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetEnergy_JetSubCalc_PtOrdered", &theJetEnergy_JetSubCalc_PtOrdered, &b_theJetEnergy_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetBTag_JetSubCalc_PtOrdered", &theJetBTag_JetSubCalc_PtOrdered, &b_theJetBTag_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetBTag_bSFup_JetSubCalc_PtOrdered", &theJetBTag_bSFup_JetSubCalc_PtOrdered, &b_theJetBTag_bSFup_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetBTag_bSFdn_JetSubCalc_PtOrdered", &theJetBTag_bSFdn_JetSubCalc_PtOrdered, &b_theJetBTag_bSFdn_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetBTag_lSFup_JetSubCalc_PtOrdered", &theJetBTag_lSFup_JetSubCalc_PtOrdered, &b_theJetBTag_lSFup_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetBTag_lSFdn_JetSubCalc_PtOrdered", &theJetBTag_lSFdn_JetSubCalc_PtOrdered, &b_theJetBTag_lSFdn_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("HadronicVHtID_JetSubCalc", &HadronicVHtID_JetSubCalc, &b_HadronicVHtID_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtPt_JetSubCalc", &HadronicVHtPt_JetSubCalc, &b_HadronicVHtPt_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtEta_JetSubCalc", &HadronicVHtEta_JetSubCalc, &b_HadronicVHtEta_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtPhi_JetSubCalc", &HadronicVHtPhi_JetSubCalc, &b_HadronicVHtPhi_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtEnergy_JetSubCalc", &HadronicVHtEnergy_JetSubCalc, &b_HadronicVHtEnergy_JetSubCalc);
   inputTree->SetBranchAddress("theJetAK8Pt_JetSubCalc_PtOrdered", &theJetAK8Pt_JetSubCalc_PtOrdered, &b_theJetAK8Pt_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Eta_JetSubCalc_PtOrdered", &theJetAK8Eta_JetSubCalc_PtOrdered, &b_theJetAK8Eta_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Phi_JetSubCalc_PtOrdered", &theJetAK8Phi_JetSubCalc_PtOrdered, &b_theJetAK8Phi_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Energy_JetSubCalc_PtOrdered", &theJetAK8Energy_JetSubCalc_PtOrdered, &b_theJetAK8Energy_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8PrunedMass_JetSubCalc_PtOrdered", &theJetAK8PrunedMass_JetSubCalc_PtOrdered, &b_theJetAK8PrunedMass_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered", &theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered, &b_theJetAK8PrunedMassWtagUncerts_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8SoftDropMass_JetSubCalc_PtOrdered", &theJetAK8SoftDropMass_JetSubCalc_PtOrdered, &b_theJetAK8SoftDropMass_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8MaxSubCSV_JetSubCalc_PtOrdered", &theJetAK8MaxSubCSV_JetSubCalc_PtOrdered, &b_theJetAK8MaxSubCSV_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8NjettinessTau1_JetSubCalc_PtOrdered", &theJetAK8NjettinessTau1_JetSubCalc_PtOrdered, &b_theJetAK8NjettinessTau1_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8NjettinessTau2_JetSubCalc_PtOrdered", &theJetAK8NjettinessTau2_JetSubCalc_PtOrdered, &b_theJetAK8NjettinessTau2_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8NjettinessTau3_JetSubCalc_PtOrdered", &theJetAK8NjettinessTau3_JetSubCalc_PtOrdered, &b_theJetAK8NjettinessTau3_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Wmatch_JetSubCalc_PtOrdered", &theJetAK8Wmatch_JetSubCalc_PtOrdered, &b_theJetAK8Wmatch_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Tmatch_JetSubCalc_PtOrdered", &theJetAK8Tmatch_JetSubCalc_PtOrdered, &b_theJetAK8Tmatch_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Zmatch_JetSubCalc_PtOrdered", &theJetAK8Zmatch_JetSubCalc_PtOrdered, &b_theJetAK8Zmatch_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8Hmatch_JetSubCalc_PtOrdered", &theJetAK8Hmatch_JetSubCalc_PtOrdered, &b_theJetAK8Hmatch_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("theJetAK8MatchedPt_JetSubCalc_PtOrdered", &theJetAK8MatchedPt_JetSubCalc_PtOrdered, &b_theJetAK8MatchedPt_JetSubCalc_PtOrdered);
   inputTree->SetBranchAddress("genJetPt_singleLepCalc", &genJetPt_singleLepCalc, &b_genJetPt_singleLepCalc);
   inputTree->SetBranchAddress("genJetEta_singleLepCalc", &genJetEta_singleLepCalc, &b_genJetEta_singleLepCalc);
   inputTree->SetBranchAddress("genJetPhi_singleLepCalc", &genJetPhi_singleLepCalc, &b_genJetPhi_singleLepCalc);
   inputTree->SetBranchAddress("genJetEnergy_singleLepCalc", &genJetEnergy_singleLepCalc, &b_genJetEnergy_singleLepCalc);
   inputTree->SetBranchAddress("BJetLeadPt", &BJetLeadPt, &b_BJetLeadPt);
   inputTree->SetBranchAddress("BJetLeadPt_shifts", &BJetLeadPt_shifts, &b_BJetLeadPt_shifts);
   inputTree->SetBranchAddress("WJetLeadPt", &WJetLeadPt, &b_WJetLeadPt);
   inputTree->SetBranchAddress("WJetLeadPt_shifts", &WJetLeadPt_shifts, &b_WJetLeadPt_shifts);
   inputTree->SetBranchAddress("TJetLeadPt", &TJetLeadPt, &b_TJetLeadPt);
   inputTree->SetBranchAddress("TJetLeadPt_shifts", &TJetLeadPt_shifts, &b_TJetLeadPt_shifts);
   inputTree->SetBranchAddress("AK4HTpMETpLepPt", &AK4HTpMETpLepPt, &b_AK4HTpMETpLepPt);
   inputTree->SetBranchAddress("AK4HT", &AK4HT, &b_AK4HT);
   inputTree->SetBranchAddress("ddBkgWeights", &ddBkgWeights, &b_ddBkgWeights);
   inputTree->SetBranchAddress("NJets_JetSubCalc", &NJets_JetSubCalc, &b_NJets_JetSubCalc);
   inputTree->SetBranchAddress("NJetsAK8_JetSubCalc", &NJetsAK8_JetSubCalc, &b_NJetsAK8_JetSubCalc);
   inputTree->SetBranchAddress("NJetsCSVwithSF_JetSubCalc", &NJetsCSVwithSF_JetSubCalc, &b_NJetsCSVwithSF_JetSubCalc);
   inputTree->SetBranchAddress("NJetsCSVwithSF_JetSubCalc_noLepCorr", &NJetsCSVwithSF_JetSubCalc_noLepCorr, &b_NJetsCSVwithSF_JetSubCalc_noLepCorr);
   inputTree->SetBranchAddress("NJetsCSVwithSF_JetSubCalc_shifts", &NJetsCSVwithSF_JetSubCalc_shifts, &b_NJetsCSVwithSF_JetSubCalc_shifts);
   inputTree->SetBranchAddress("NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts", &NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts, &b_NJetsCSVwithSF_JetSubCalc_noLepCorr_shifts);
   inputTree->SetBranchAddress("NJetsHtagged", &NJetsHtagged, &b_NJetsHtagged);
   inputTree->SetBranchAddress("NJetsHtagged_shifts", &NJetsHtagged_shifts, &b_NJetsHtagged_shifts);
   inputTree->SetBranchAddress("topPt", &topPt, &b_topPt);
   inputTree->SetBranchAddress("topPtGen", &topPtGen, &b_topPtGen);
   inputTree->SetBranchAddress("topMass", &topMass, &b_topMass);
   inputTree->SetBranchAddress("minMleppBjet", &minMleppBjet, &b_minMleppBjet);
   inputTree->SetBranchAddress("minMleppBjet_shifts", &minMleppBjet_shifts, &b_minMleppBjet_shifts);
   inputTree->SetBranchAddress("minMleppJet", &minMleppJet, &b_mixnMleppJet);
   inputTree->SetBranchAddress("genTopPt", &genTopPt, &b_genTopPt);
   inputTree->SetBranchAddress("genAntiTopPt", &genAntiTopPt, &b_genAntiTopPt);
   inputTree->SetBranchAddress("topPtWeight", &topPtWeight, &b_topPtWeight);
   inputTree->SetBranchAddress("topPtWeightPast400", &topPtWeightPast400, &b_topPtWeightPast400);
   inputTree->SetBranchAddress("topPtWeightHighPt", &topPtWeightHighPt, &b_topPtWeightHighPt);
   inputTree->SetBranchAddress("deltaRlepJetInMinMljet", &deltaRlepJetInMinMljet, &b_deltaRlepJetInMinMljet);
   inputTree->SetBranchAddress("deltaRlepbJetInMinMlb", &deltaRlepbJetInMinMlb, &b_deltaRlepbJetInMinMlb);
   inputTree->SetBranchAddress("deltaRlepbJetInMinMlb_shifts", &deltaRlepbJetInMinMlb_shifts, &b_deltaRlepbJetInMinMlb_shifts);
   inputTree->SetBranchAddress("deltaPhilepJetInMinMljet", &deltaPhilepJetInMinMljet, &b_deltaPhilepJetInMinMljet);
   inputTree->SetBranchAddress("deltaPhilepbJetInMinMlb", &deltaPhilepbJetInMinMlb, &b_deltaPhilepbJetInMinMlb);
   inputTree->SetBranchAddress("deltaPhilepbJetInMinMlb_shifts", &deltaPhilepbJetInMinMlb_shifts, &b_deltaPhilepbJetInMinMlb_shifts);
   inputTree->SetBranchAddress("deltaRtopWjet", &deltaRtopWjet, &b_deltaRtopWjet);
   inputTree->SetBranchAddress("deltaRlepWjet", &deltaRlepWjet, &b_deltaRlepWjet);
   inputTree->SetBranchAddress("deltaRlepTjet", &deltaRlepTjet, &b_deltaRlepTjet);
   inputTree->SetBranchAddress("deltaPhitopWjet", &deltaPhitopWjet, &b_deltaPhitopWjet);
   inputTree->SetBranchAddress("deltaPhilepWjet", &deltaPhilepWjet, &b_deltaPhilepWjet);
   inputTree->SetBranchAddress("deltaPhilepTjet", &deltaPhilepTjet, &b_deltaPhilepTjet);
   inputTree->SetBranchAddress("deltaRtopWjet_shifts", &deltaRtopWjet_shifts, &b_deltaRtopWjet_shifts);
   inputTree->SetBranchAddress("deltaRlepWjet_shifts", &deltaRlepWjet_shifts, &b_deltaRlepWjet_shifts);
   inputTree->SetBranchAddress("deltaRlepTjet_shifts", &deltaRlepTjet_shifts, &b_deltaRlepTjet_shifts);
   inputTree->SetBranchAddress("deltaPhitopWjet_shifts", &deltaPhitopWjet_shifts, &b_deltaPhitopWjet_shifts);
   inputTree->SetBranchAddress("deltaPhilepWjet_shifts", &deltaPhilepWjet_shifts, &b_deltaPhilepWjet_shifts);
   inputTree->SetBranchAddress("deltaPhilepTjet_shifts", &deltaPhilepTjet_shifts, &b_deltaPhilepTjet_shifts);
   inputTree->SetBranchAddress("NJetsWtagged_0p6", &NJetsWtagged_0p6, &b_NJetsWtagged_0p6);
   inputTree->SetBranchAddress("NJetsWtagged_0p6_shifts", &NJetsWtagged_0p6_shifts, &b_NJetsWtagged_0p6_shifts);
   inputTree->SetBranchAddress("NJetsTtagged_0p81", &NJetsTtagged_0p81, &b_NJetsTtagged_0p81);
   inputTree->SetBranchAddress("NJetsTtagged_0p81_shifts", &NJetsTtagged_0p81_shifts, &b_NJetsTtagged_0p81_shifts);
   inputTree->SetBranchAddress("minDR_leadAK8otherAK8", &minDR_leadAK8otherAK8, &b_minDR_leadAK8otherAK8);
   inputTree->SetBranchAddress("minDR_lepAK8", &minDR_lepAK8, &b_minDR_lepAK8);
   inputTree->SetBranchAddress("minDR_lepJet", &minDR_lepJet, &b_minDR_lepJet);
   inputTree->SetBranchAddress("ptRel_lepJet", &ptRel_lepJet, &b_ptRel_lepJet);
   inputTree->SetBranchAddress("MT_lepMet", &MT_lepMet, &b_MT_lepMet);
   inputTree->SetBranchAddress("deltaR_lepJets", &deltaR_lepJets, &b_deltaR_lepJets);
   inputTree->SetBranchAddress("deltaR_lepBJets", &deltaR_lepBJets, &b_deltaR_lepBJets);
   inputTree->SetBranchAddress("deltaR_lepBJets_bSFup", &deltaR_lepBJets_bSFup, &b_deltaR_lepBJets_bSFup);
   inputTree->SetBranchAddress("deltaR_lepBJets_bSFdn", &deltaR_lepBJets_bSFdn, &b_deltaR_lepBJets_bSFdn);
   inputTree->SetBranchAddress("deltaR_lepBJets_lSFup", &deltaR_lepBJets_lSFup, &b_deltaR_lepBJets_lSFup);
   inputTree->SetBranchAddress("deltaR_lepBJets_lSFdn", &deltaR_lepBJets_lSFdn, &b_deltaR_lepBJets_lSFdn);
   inputTree->SetBranchAddress("deltaR_lepAK8s", &deltaR_lepAK8s, &b_deltaR_lepAK8s);
   inputTree->SetBranchAddress("deltaPhi_lepJets", &deltaPhi_lepJets, &b_deltaPhi_lepJets);
   inputTree->SetBranchAddress("deltaPhi_lepBJets", &deltaPhi_lepBJets, &b_deltaPhi_lepBJets);
   inputTree->SetBranchAddress("deltaPhi_lepBJets_bSFup", &deltaPhi_lepBJets_bSFup, &b_deltaPhi_lepBJets_bSFup);
   inputTree->SetBranchAddress("deltaPhi_lepBJets_bSFdn", &deltaPhi_lepBJets_bSFdn, &b_deltaPhi_lepBJets_bSFdn);
   inputTree->SetBranchAddress("deltaPhi_lepBJets_lSFup", &deltaPhi_lepBJets_lSFup, &b_deltaPhi_lepBJets_lSFup);
   inputTree->SetBranchAddress("deltaPhi_lepBJets_lSFdn", &deltaPhi_lepBJets_lSFdn, &b_deltaPhi_lepBJets_lSFdn);
   inputTree->SetBranchAddress("deltaPhi_lepAK8s", &deltaPhi_lepAK8s, &b_deltaPhi_lepAK8s);
   inputTree->SetBranchAddress("mass_lepJets", &mass_lepJets, &b_mass_lepJets);
   inputTree->SetBranchAddress("mass_lepBJets", &mass_lepBJets, &b_mass_lepBJets);
   inputTree->SetBranchAddress("mass_lepBJets_bSFup", &mass_lepBJets_bSFup, &b_mass_lepBJets_bSFup);
   inputTree->SetBranchAddress("mass_lepBJets_bSFdn", &mass_lepBJets_bSFdn, &b_mass_lepBJets_bSFdn);
   inputTree->SetBranchAddress("mass_lepBJets_lSFup", &mass_lepBJets_lSFup, &b_mass_lepBJets_lSFup);
   inputTree->SetBranchAddress("mass_lepBJets_lSFdn", &mass_lepBJets_lSFdn, &b_mass_lepBJets_lSFdn);
   inputTree->SetBranchAddress("mass_lepAK8s", &mass_lepAK8s, &b_mass_lepAK8s);
   inputTree->SetBranchAddress("minDR_lepJets", &minDR_lepJets, &b_minDR_lepJets);
   inputTree->SetBranchAddress("minDR_lepBJets", &minDR_lepBJets, &b_minDR_lepBJets);
   inputTree->SetBranchAddress("deltaR_lep1Jets", &deltaR_lep1Jets, &b_deltaR_lep1Jets);
   inputTree->SetBranchAddress("deltaR_lep2Jets", &deltaR_lep2Jets, &b_deltaR_lep2Jets);
   inputTree->SetBranchAddress("deltaR_lep3Jets", &deltaR_lep3Jets, &b_deltaR_lep3Jets);
   inputTree->SetBranchAddress("deltaR_lepClosestJet", &deltaR_lepClosestJet, &b_deltaR_lepClosestJet);
   inputTree->SetBranchAddress("PtRelLepClosestJet", &PtRelLepClosestJet, &b_PtRelLepClosestJet);
   inputTree->SetBranchAddress("Mll_sameFlavorOS", &Mll_sameFlavorOS, &b_Mll_sameFlavorOS);
   inputTree->SetBranchAddress("MllOS_allComb", &MllOS_allComb, &b_MllOS_allComb);
   inputTree->SetBranchAddress("MllOS_allComb_min", &MllOS_allComb_min, &b_MllOS_allComb_min);
   inputTree->SetBranchAddress("MllOS_allComb_max", &MllOS_allComb_max, &b_MllOS_allComb_max);
   inputTree->SetBranchAddress("Mlll", &Mlll, &b_Mlll);
   Notify();
}

Bool_t step2::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void step2::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!inputTree) return;
   inputTree->Show(entry);
}
Int_t step2::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef step2_cxx
