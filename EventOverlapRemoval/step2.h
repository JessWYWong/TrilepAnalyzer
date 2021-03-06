//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat Oct 29 18:18:45 2016 by ROOT version 6.02/13
// from TTree ljmet/ljmet
// found on file: /user_data/rsyarif/LJMet80x_3lepTT_2016_10_13_rizki_step1hadds_ddbkgscan/nominal/DoubleEG_PRB_hadd.root
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
   Int_t           nPV_MultiLepCalc;
   Int_t           nTrueInteractions_MultiLepCalc;
   Int_t           isElectron;
   Int_t           isMuon;
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
   Bool_t          tPrimePt_TpTpCalc;
   Int_t           NLeptonDecays_TpTpCalc;
   Double_t        MCWeight_MultiLepCalc;
   vector<double>  *renormWeights;
   vector<float>   *pdfWeights;
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
   Int_t           MCPastTrigger;
   Int_t           DataPastTrigger;
   Int_t           MCPastTrigger_dilep;
   Int_t           DataPastTrigger_dilep;
   Double_t        ttbarMass_TTbarMassCalc;
   Double_t        corr_met_MultiLepCalc;
   Double_t        corr_met_phi_MultiLepCalc;
   Float_t         leptonPt_MultiLepCalc;
   Float_t         leptonEta_MultiLepCalc;
   Float_t         leptonPhi_MultiLepCalc;
   Float_t         leptonEnergy_MultiLepCalc;
   Float_t         leptonMiniIso_MultiLepCalc;
   Float_t         leptonRelIso_MultiLepCalc;
   Float_t         leptonDxy_MultiLepCalc;
   Float_t         leptonDz_MultiLepCalc;
   Int_t           leptonCharge_MultiLepCalc;
   Int_t           elTrigPresel_MultiLepCalc;
   Int_t           elNotConversion_MultiLepCalc;
   vector<float>   *AllLeptonElPt_PtOrdered;
   vector<float>   *AllLeptonElEta_PtOrdered;
   vector<float>   *AllLeptonElPhi_PtOrdered;
   vector<float>   *AllLeptonElEnergy_PtOrdered;
   vector<float>   *AllLeptonElMiniIso_PtOrdered;
   vector<int>     *AllLeptonElFlavor_PtOrdered;
   vector<int>     *AllLeptonElIsTight_PtOrdered;
   Int_t           AllLeptonElCount_PtOrdered;
   vector<float>   *AllLeptonElDxy_PtOrdered;
   vector<float>   *AllLeptonElDz_PtOrdered;
   vector<float>   *AllLeptonElPt_PtOrderedOnly;
   vector<float>   *AllLeptonElEta_PtOrderedOnly;
   vector<float>   *AllLeptonElPhi_PtOrderedOnly;
   vector<float>   *AllLeptonElEnergy_PtOrderedOnly;
   vector<float>   *AllLeptonElMiniIso_PtOrderedOnly;
   vector<int>     *AllLeptonElFlavor_PtOrderedOnly;
   vector<int>     *AllLeptonElIsTight_PtOrderedOnly;
   vector<float>   *AllLeptonElDxy_PtOrderedOnly;
   vector<float>   *AllLeptonElDz_PtOrderedOnly;
   vector<float>   *AllLeptonElPt_PtOrderedOnly_top3;
   vector<float>   *AllLeptonElEta_PtOrderedOnly_top3;
   vector<float>   *AllLeptonElPhi_PtOrderedOnly_top3;
   vector<float>   *AllLeptonElEnergy_PtOrderedOnly_top3;
   vector<float>   *AllLeptonElMiniIso_PtOrderedOnly_top3;
   vector<int>     *AllLeptonElFlavor_PtOrderedOnly_top3;
   vector<int>     *AllLeptonElIsTight_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMuPt_PtOrdered;
   vector<float>   *AllLeptonMuEta_PtOrdered;
   vector<float>   *AllLeptonMuPhi_PtOrdered;
   vector<float>   *AllLeptonMuEnergy_PtOrdered;
   vector<float>   *AllLeptonMuMiniIso_PtOrdered;
   vector<int>     *AllLeptonMuFlavor_PtOrdered;
   vector<int>     *AllLeptonMuIsTight_PtOrdered;
   Int_t           AllLeptonMuCount_PtOrdered;
   vector<float>   *AllLeptonMuDxy_PtOrdered;
   vector<float>   *AllLeptonMuDz_PtOrdered;
   vector<float>   *AllLeptonMuPt_PtOrderedOnly;
   vector<float>   *AllLeptonMuEta_PtOrderedOnly;
   vector<float>   *AllLeptonMuPhi_PtOrderedOnly;
   vector<float>   *AllLeptonMuEnergy_PtOrderedOnly;
   vector<float>   *AllLeptonMuMiniIso_PtOrderedOnly;
   vector<int>     *AllLeptonMuFlavor_PtOrderedOnly;
   vector<int>     *AllLeptonMuIsTight_PtOrderedOnly;
   vector<float>   *AllLeptonMuDxy_PtOrderedOnly;
   vector<float>   *AllLeptonMuDz_PtOrderedOnly;
   vector<float>   *AllLeptonMuPt_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMuEta_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMuPhi_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMuEnergy_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMuMiniIso_PtOrderedOnly_top3;
   vector<int>     *AllLeptonMuFlavor_PtOrderedOnly_top3;
   vector<int>     *AllLeptonMuIsTight_PtOrderedOnly_top3;
   vector<float>   *AllLeptonPt_PtOrdered;
   vector<float>   *AllLeptonEta_PtOrdered;
   vector<float>   *AllLeptonPhi_PtOrdered;
   vector<float>   *AllLeptonEnergy_PtOrdered;
   vector<float>   *AllLeptonMiniIso_PtOrdered;
   vector<int>     *AllLeptonFlavor_PtOrdered;
   vector<int>     *AllLeptonIsTight_PtOrdered;
   vector<int>     *AllLeptonCharge_PtOrdered;
   Int_t           AllLeptonCount_PtOrdered;
   vector<float>   *AllLeptonDxy_PtOrdered;
   vector<float>   *AllLeptonDz_PtOrdered;
   vector<float>   *AllLeptonPt_PtOrderedOnly;
   vector<float>   *AllLeptonEta_PtOrderedOnly;
   vector<float>   *AllLeptonPhi_PtOrderedOnly;
   vector<float>   *AllLeptonEnergy_PtOrderedOnly;
   vector<float>   *AllLeptonMiniIso_PtOrderedOnly;
   vector<int>     *AllLeptonFlavor_PtOrderedOnly;
   vector<int>     *AllLeptonIsTight_PtOrderedOnly;
   vector<int>     *AllLeptonCharge_PtOrderedOnly;
   vector<float>   *AllLeptonDxy_PtOrderedOnly;
   vector<float>   *AllLeptonDz_PtOrderedOnly;
   vector<float>   *AllLeptonPt_PtOrderedOnly_top3;
   vector<float>   *AllLeptonEta_PtOrderedOnly_top3;
   vector<float>   *AllLeptonPhi_PtOrderedOnly_top3;
   vector<float>   *AllLeptonEnergy_PtOrderedOnly_top3;
   vector<float>   *AllLeptonMiniIso_PtOrderedOnly_top3;
   vector<int>     *AllLeptonFlavor_PtOrderedOnly_top3;
   vector<int>     *AllLeptonIsTight_PtOrderedOnly_top3;
   vector<int>     *AllLeptonCharge_PtOrderedOnly_top3;
   vector<float>   *TightLeptonPt_PtOrdered;
   vector<float>   *TightLeptonEta_PtOrdered;
   vector<float>   *TightLeptonPhi_PtOrdered;
   vector<float>   *TightLeptonEnergy_PtOrdered;
   vector<float>   *TightLeptonMiniIso_PtOrdered;
   vector<int>     *TightLeptonFlavor_PtOrdered;
   vector<int>     *TightLeptonCharge_PtOrdered;
   vector<double>  *AK4JetPt_MultiLepCalc_PtOrdered;
   vector<double>  *AK4JetEta_MultiLepCalc_PtOrdered;
   vector<double>  *AK4JetPhi_MultiLepCalc_PtOrdered;
   vector<double>  *AK4JetEnergy_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetFlav_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetBTag_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetBTag_bSFup_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetBTag_lSFup_MultiLepCalc_PtOrdered;
   vector<int>     *AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered;
   vector<int>     *HadronicVHtID_JetSubCalc;
   vector<double>  *HadronicVHtPt_JetSubCalc;
   vector<double>  *HadronicVHtEta_JetSubCalc;
   vector<double>  *HadronicVHtPhi_JetSubCalc;
   vector<double>  *HadronicVHtEnergy_JetSubCalc;
   vector<double>  *genJetPt_MultiLepCalc;
   vector<double>  *genJetEta_MultiLepCalc;
   vector<double>  *genJetPhi_MultiLepCalc;
   vector<double>  *genJetEnergy_MultiLepCalc;
   Float_t         BJetLeadPt;
   vector<double>  *BJetLeadPt_shifts;
   Float_t         WJetLeadPt;
   vector<double>  *WJetLeadPt_shifts;
   Float_t         TJetLeadPt;
   vector<double>  *TJetLeadPt_shifts;
   Float_t         AK4HTpMETpLepPt;
   Float_t         AK4HT;
   vector<float>   *ddBkgWeights;
   vector<float>   *ddBkgWeights_scan;
   vector<float>   *ddBkgWeights_scan_muFR;
   vector<float>   *ddBkgWeights_scan_elFR;
   Int_t           NJets_MultiLepCalc;
   Int_t           NJetsAK8_JetSubCalc;
   Int_t           NJetsBTag_MultiLepCalc;
   Int_t           NJetsBTagwithSF_MultiLepCalc;
   vector<int>     *NJetsBTagwithSF_MultiLepCalc_shifts;
   Int_t           NJetsBTagwithSF_MultiLepCalc_noLepCorr;
   vector<int>     *NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts;
   Float_t         topPt;
   Float_t         topPtGen;
   Float_t         topMass;
   Float_t         minMleppBjet;
   vector<double>  *minMleppBjet_shifts;
   Float_t         minMleppJet;
   Float_t         minMlllBjet;
   vector<double>  *minMlllBjet_shifts;
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
   Float_t         minDR_lep1Jet;
   Float_t         minDR_lep2Jet;
   Float_t         minDR_lep3Jet;
   Float_t         minDR_lepMET;
   Float_t         minDR_METJet;
   Float_t         minDPhi_METJet;
   Float_t         ptRel_minDRlepJet;
   Float_t         ptRel_minDRlep1Jet;
   Float_t         ptRel_minDRlep2Jet;
   Float_t         ptRel_minDRlep3Jet;
   Float_t         MT_lepMet;
   vector<double>  *deltaR_lepJets;
   vector<double>  *deltaR_lep1Jets;
   vector<double>  *deltaR_lep2Jets;
   vector<double>  *deltaR_lep3Jets;
   vector<double>  *ptRel_lepJets;
   vector<double>  *ptRel_lep1Jets;
   vector<double>  *ptRel_lep2Jets;
   vector<double>  *ptRel_lep3Jets;
   vector<double>  *deltaR_lepMETs;
   vector<double>  *deltaR_METJets;
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
   TBranch        *b_nPV_MultiLepCalc;   //!
   TBranch        *b_nTrueInteractions_MultiLepCalc;   //!
   TBranch        *b_isElectron;   //!
   TBranch        *b_isMuon;   //!
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
   TBranch        *b_tPrimePt_TpTpCalc;   //!
   TBranch        *b_NLeptonDecays_TpTpCalc;   //!
   TBranch        *b_MCWeight_MultiLepCalc;   //!
   TBranch        *b_renormWeights;   //!
   TBranch        *b_pdfWeights;   //!
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
   TBranch        *b_MCPastTrigger;   //!
   TBranch        *b_DataPastTrigger;   //!
   TBranch        *b_MCPastTrigger_dilep;   //!
   TBranch        *b_DataPastTrigger_dilep;   //!
   TBranch        *b_ttbarMass_TTbarMassCalc;   //!
   TBranch        *b_corr_met_MultiLepCalc;   //!
   TBranch        *b_corr_met_phi_MultiLepCalc;   //!
   TBranch        *b_leptonPt_MultiLepCalc;   //!
   TBranch        *b_leptonEta_MultiLepCalc;   //!
   TBranch        *b_leptonPhi_MultiLepCalc;   //!
   TBranch        *b_leptonEnergy_MultiLepCalc;   //!
   TBranch        *b_leptonMiniIso_MultiLepCalc;   //!
   TBranch        *b_leptonRelIso_MultiLepCalc;   //!
   TBranch        *b_leptonDxy_MultiLepCalc;   //!
   TBranch        *b_leptonDz_MultiLepCalc;   //!
   TBranch        *b_leptonCharge_MultiLepCalc;   //!
   TBranch        *b_elTrigPresel_MultiLepCalc;   //!
   TBranch        *b_elNotConversion_MultiLepCalc;   //!
   TBranch        *b_AllLeptonElPt_PtOrdered;   //!
   TBranch        *b_AllLeptonElEta_PtOrdered;   //!
   TBranch        *b_AllLeptonElPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonElEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonElMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonElFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonElIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonElCount_PtOrdered;   //!
   TBranch        *b_AllLeptonElDxy_PtOrdered;   //!
   TBranch        *b_AllLeptonElDz_PtOrdered;   //!
   TBranch        *b_AllLeptonElPt_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElEta_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElPhi_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElEnergy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElMiniIso_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElFlavor_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElIsTight_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElDxy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElDz_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonElPt_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElEta_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElPhi_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElEnergy_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElMiniIso_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElFlavor_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonElIsTight_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuPt_PtOrdered;   //!
   TBranch        *b_AllLeptonMuEta_PtOrdered;   //!
   TBranch        *b_AllLeptonMuPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonMuEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonMuMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonMuFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonMuIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonMuCount_PtOrdered;   //!
   TBranch        *b_AllLeptonMuDxy_PtOrdered;   //!
   TBranch        *b_AllLeptonMuDz_PtOrdered;   //!
   TBranch        *b_AllLeptonMuPt_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuEta_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuPhi_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuEnergy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuMiniIso_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuFlavor_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuIsTight_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuDxy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuDz_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMuPt_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuEta_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuPhi_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuEnergy_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuMiniIso_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuFlavor_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMuIsTight_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonPt_PtOrdered;   //!
   TBranch        *b_AllLeptonEta_PtOrdered;   //!
   TBranch        *b_AllLeptonPhi_PtOrdered;   //!
   TBranch        *b_AllLeptonEnergy_PtOrdered;   //!
   TBranch        *b_AllLeptonMiniIso_PtOrdered;   //!
   TBranch        *b_AllLeptonFlavor_PtOrdered;   //!
   TBranch        *b_AllLeptonIsTight_PtOrdered;   //!
   TBranch        *b_AllLeptonCharge_PtOrdered;   //!
   TBranch        *b_AllLeptonCount_PtOrdered;   //!
   TBranch        *b_AllLeptonDxy_PtOrdered;   //!
   TBranch        *b_AllLeptonDz_PtOrdered;   //!
   TBranch        *b_AllLeptonPt_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonEta_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonPhi_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonEnergy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonMiniIso_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonFlavor_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonIsTight_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonCharge_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonDxy_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonDz_PtOrderedOnly;   //!
   TBranch        *b_AllLeptonPt_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonEta_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonPhi_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonEnergy_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonMiniIso_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonFlavor_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonIsTight_PtOrderedOnly_top3;   //!
   TBranch        *b_AllLeptonCharge_PtOrderedOnly_top3;   //!
   TBranch        *b_TightLeptonPt_PtOrdered;   //!
   TBranch        *b_TightLeptonEta_PtOrdered;   //!
   TBranch        *b_TightLeptonPhi_PtOrdered;   //!
   TBranch        *b_TightLeptonEnergy_PtOrdered;   //!
   TBranch        *b_TightLeptonMiniIso_PtOrdered;   //!
   TBranch        *b_TightLeptonFlavor_PtOrdered;   //!
   TBranch        *b_TightLeptonCharge_PtOrdered;   //!
   TBranch        *b_AK4JetPt_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetEta_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetPhi_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetEnergy_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetFlav_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetBTag_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetBTag_bSFup_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetBTag_lSFup_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered;   //!
   TBranch        *b_HadronicVHtID_JetSubCalc;   //!
   TBranch        *b_HadronicVHtPt_JetSubCalc;   //!
   TBranch        *b_HadronicVHtEta_JetSubCalc;   //!
   TBranch        *b_HadronicVHtPhi_JetSubCalc;   //!
   TBranch        *b_HadronicVHtEnergy_JetSubCalc;   //!
   TBranch        *b_genJetPt_MultiLepCalc;   //!
   TBranch        *b_genJetEta_MultiLepCalc;   //!
   TBranch        *b_genJetPhi_MultiLepCalc;   //!
   TBranch        *b_genJetEnergy_MultiLepCalc;   //!
   TBranch        *b_BJetLeadPt;   //!
   TBranch        *b_BJetLeadPt_shifts;   //!
   TBranch        *b_WJetLeadPt;   //!
   TBranch        *b_WJetLeadPt_shifts;   //!
   TBranch        *b_TJetLeadPt;   //!
   TBranch        *b_TJetLeadPt_shifts;   //!
   TBranch        *b_AK4HTpMETpLepPt;   //!
   TBranch        *b_AK4HT;   //!
   TBranch        *b_ddBkgWeights;   //!
   TBranch        *b_ddBkgWeights_scan;   //!
   TBranch        *b_ddBkgWeights_scan_muFR;   //!
   TBranch        *b_ddBkgWeights_scan_elFR;   //!
   TBranch        *b_NJets_MultiLepCalc;   //!
   TBranch        *b_NJetsAK8_JetSubCalc;   //!
   TBranch        *b_NJetsBTag_MultiLepCalc;   //!
   TBranch        *b_NJetsBTagwithSF_MultiLepCalc;   //!
   TBranch        *b_NJetsBTagwithSF_MultiLepCalc_shifts;   //!
   TBranch        *b_NJetsBTagwithSF_MultiLepCalc_noLepCorr;   //!
   TBranch        *b_NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts;   //!
   TBranch        *b_topPt;   //!
   TBranch        *b_topPtGen;   //!
   TBranch        *b_topMass;   //!
   TBranch        *b_minMleppBjet;   //!
   TBranch        *b_minMleppBjet_shifts;   //!
   TBranch        *b_mixnMleppJet;   //!
   TBranch        *b_minMlllBjet;   //!
   TBranch        *b_minMlllBjet_shifts;   //!
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
   TBranch        *b_minDR_lep1Jet;   //!
   TBranch        *b_minDR_lep2Jet;   //!
   TBranch        *b_minDR_lep3Jet;   //!
   TBranch        *b_minDR_lepMET;   //!
   TBranch        *b_minDR_METJet;   //!
   TBranch        *b_minDPhi_METJet;   //!
   TBranch        *b_ptRel_minDRlepJet;   //!
   TBranch        *b_ptRel_minDRlep1Jet;   //!
   TBranch        *b_ptRel_minDRlep2Jet;   //!
   TBranch        *b_ptRel_minDRlep3Jet;   //!
   TBranch        *b_MT_lepMet;   //!
   TBranch        *b_deltaR_lepJets;   //!
   TBranch        *b_deltaR_lep1Jets;   //!
   TBranch        *b_deltaR_lep2Jets;   //!
   TBranch        *b_deltaR_lep3Jets;   //!
   TBranch        *b_ptRel_lepJets;   //!
   TBranch        *b_ptRel_lep1Jets;   //!
   TBranch        *b_ptRel_lep2Jets;   //!
   TBranch        *b_ptRel_lep3Jets;   //!
   TBranch        *b_deltaR_lepMETs;   //!
   TBranch        *b_deltaR_METJets;   //!
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
   AllLeptonElDxy_PtOrdered = 0;
   AllLeptonElDz_PtOrdered = 0;
   AllLeptonElPt_PtOrderedOnly = 0;
   AllLeptonElEta_PtOrderedOnly = 0;
   AllLeptonElPhi_PtOrderedOnly = 0;
   AllLeptonElEnergy_PtOrderedOnly = 0;
   AllLeptonElMiniIso_PtOrderedOnly = 0;
   AllLeptonElFlavor_PtOrderedOnly = 0;
   AllLeptonElIsTight_PtOrderedOnly = 0;
   AllLeptonElDxy_PtOrderedOnly = 0;
   AllLeptonElDz_PtOrderedOnly = 0;
   AllLeptonElPt_PtOrderedOnly_top3 = 0;
   AllLeptonElEta_PtOrderedOnly_top3 = 0;
   AllLeptonElPhi_PtOrderedOnly_top3 = 0;
   AllLeptonElEnergy_PtOrderedOnly_top3 = 0;
   AllLeptonElMiniIso_PtOrderedOnly_top3 = 0;
   AllLeptonElFlavor_PtOrderedOnly_top3 = 0;
   AllLeptonElIsTight_PtOrderedOnly_top3 = 0;
   AllLeptonMuPt_PtOrdered = 0;
   AllLeptonMuEta_PtOrdered = 0;
   AllLeptonMuPhi_PtOrdered = 0;
   AllLeptonMuEnergy_PtOrdered = 0;
   AllLeptonMuMiniIso_PtOrdered = 0;
   AllLeptonMuFlavor_PtOrdered = 0;
   AllLeptonMuIsTight_PtOrdered = 0;
   AllLeptonMuDxy_PtOrdered = 0;
   AllLeptonMuDz_PtOrdered = 0;
   AllLeptonMuPt_PtOrderedOnly = 0;
   AllLeptonMuEta_PtOrderedOnly = 0;
   AllLeptonMuPhi_PtOrderedOnly = 0;
   AllLeptonMuEnergy_PtOrderedOnly = 0;
   AllLeptonMuMiniIso_PtOrderedOnly = 0;
   AllLeptonMuFlavor_PtOrderedOnly = 0;
   AllLeptonMuIsTight_PtOrderedOnly = 0;
   AllLeptonMuDxy_PtOrderedOnly = 0;
   AllLeptonMuDz_PtOrderedOnly = 0;
   AllLeptonMuPt_PtOrderedOnly_top3 = 0;
   AllLeptonMuEta_PtOrderedOnly_top3 = 0;
   AllLeptonMuPhi_PtOrderedOnly_top3 = 0;
   AllLeptonMuEnergy_PtOrderedOnly_top3 = 0;
   AllLeptonMuMiniIso_PtOrderedOnly_top3 = 0;
   AllLeptonMuFlavor_PtOrderedOnly_top3 = 0;
   AllLeptonMuIsTight_PtOrderedOnly_top3 = 0;
   AllLeptonPt_PtOrdered = 0;
   AllLeptonEta_PtOrdered = 0;
   AllLeptonPhi_PtOrdered = 0;
   AllLeptonEnergy_PtOrdered = 0;
   AllLeptonMiniIso_PtOrdered = 0;
   AllLeptonFlavor_PtOrdered = 0;
   AllLeptonIsTight_PtOrdered = 0;
   AllLeptonCharge_PtOrdered = 0;
   AllLeptonDxy_PtOrdered = 0;
   AllLeptonDz_PtOrdered = 0;
   AllLeptonPt_PtOrderedOnly = 0;
   AllLeptonEta_PtOrderedOnly = 0;
   AllLeptonPhi_PtOrderedOnly = 0;
   AllLeptonEnergy_PtOrderedOnly = 0;
   AllLeptonMiniIso_PtOrderedOnly = 0;
   AllLeptonFlavor_PtOrderedOnly = 0;
   AllLeptonIsTight_PtOrderedOnly = 0;
   AllLeptonCharge_PtOrderedOnly = 0;
   AllLeptonDxy_PtOrderedOnly = 0;
   AllLeptonDz_PtOrderedOnly = 0;
   AllLeptonPt_PtOrderedOnly_top3 = 0;
   AllLeptonEta_PtOrderedOnly_top3 = 0;
   AllLeptonPhi_PtOrderedOnly_top3 = 0;
   AllLeptonEnergy_PtOrderedOnly_top3 = 0;
   AllLeptonMiniIso_PtOrderedOnly_top3 = 0;
   AllLeptonFlavor_PtOrderedOnly_top3 = 0;
   AllLeptonIsTight_PtOrderedOnly_top3 = 0;
   AllLeptonCharge_PtOrderedOnly_top3 = 0;
   TightLeptonPt_PtOrdered = 0;
   TightLeptonEta_PtOrdered = 0;
   TightLeptonPhi_PtOrdered = 0;
   TightLeptonEnergy_PtOrdered = 0;
   TightLeptonMiniIso_PtOrdered = 0;
   TightLeptonFlavor_PtOrdered = 0;
   TightLeptonCharge_PtOrdered = 0;
   AK4JetPt_MultiLepCalc_PtOrdered = 0;
   AK4JetEta_MultiLepCalc_PtOrdered = 0;
   AK4JetPhi_MultiLepCalc_PtOrdered = 0;
   AK4JetEnergy_MultiLepCalc_PtOrdered = 0;
   AK4JetFlav_MultiLepCalc_PtOrdered = 0;
   AK4JetBTag_MultiLepCalc_PtOrdered = 0;
   AK4JetBTag_bSFup_MultiLepCalc_PtOrdered = 0;
   AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered = 0;
   AK4JetBTag_lSFup_MultiLepCalc_PtOrdered = 0;
   AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered = 0;
   HadronicVHtID_JetSubCalc = 0;
   HadronicVHtPt_JetSubCalc = 0;
   HadronicVHtEta_JetSubCalc = 0;
   HadronicVHtPhi_JetSubCalc = 0;
   HadronicVHtEnergy_JetSubCalc = 0;
   genJetPt_MultiLepCalc = 0;
   genJetEta_MultiLepCalc = 0;
   genJetPhi_MultiLepCalc = 0;
   genJetEnergy_MultiLepCalc = 0;
   BJetLeadPt_shifts = 0;
   WJetLeadPt_shifts = 0;
   TJetLeadPt_shifts = 0;
   ddBkgWeights = 0;
   ddBkgWeights_scan = 0;
   ddBkgWeights_scan_muFR = 0;
   ddBkgWeights_scan_elFR = 0;
   NJetsBTagwithSF_MultiLepCalc_shifts = 0;
   NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts = 0;
   minMleppBjet_shifts = 0;
   minMlllBjet_shifts = 0;
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
   deltaR_lep1Jets = 0;
   deltaR_lep2Jets = 0;
   deltaR_lep3Jets = 0;
   ptRel_lepJets = 0;
   ptRel_lep1Jets = 0;
   ptRel_lep2Jets = 0;
   ptRel_lep3Jets = 0;
   deltaR_lepMETs = 0;
   deltaR_METJets = 0;
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
   inputTree->SetBranchAddress("nPV_MultiLepCalc", &nPV_MultiLepCalc, &b_nPV_MultiLepCalc);
   inputTree->SetBranchAddress("nTrueInteractions_MultiLepCalc", &nTrueInteractions_MultiLepCalc, &b_nTrueInteractions_MultiLepCalc);
   inputTree->SetBranchAddress("isElectron", &isElectron, &b_isElectron);
   inputTree->SetBranchAddress("isMuon", &isMuon, &b_isMuon);
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
   inputTree->SetBranchAddress("tPrimePt_TpTpCalc", &tPrimePt_TpTpCalc, &b_tPrimePt_TpTpCalc);
   inputTree->SetBranchAddress("NLeptonDecays_TpTpCalc", &NLeptonDecays_TpTpCalc, &b_NLeptonDecays_TpTpCalc);
   inputTree->SetBranchAddress("MCWeight_MultiLepCalc", &MCWeight_MultiLepCalc, &b_MCWeight_MultiLepCalc);
   inputTree->SetBranchAddress("renormWeights", &renormWeights, &b_renormWeights);
   inputTree->SetBranchAddress("pdfWeights", &pdfWeights, &b_pdfWeights);
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
   inputTree->SetBranchAddress("MCPastTrigger", &MCPastTrigger, &b_MCPastTrigger);
   inputTree->SetBranchAddress("DataPastTrigger", &DataPastTrigger, &b_DataPastTrigger);
   inputTree->SetBranchAddress("MCPastTrigger_dilep", &MCPastTrigger_dilep, &b_MCPastTrigger_dilep);
   inputTree->SetBranchAddress("DataPastTrigger_dilep", &DataPastTrigger_dilep, &b_DataPastTrigger_dilep);
   inputTree->SetBranchAddress("ttbarMass_TTbarMassCalc", &ttbarMass_TTbarMassCalc, &b_ttbarMass_TTbarMassCalc);
   inputTree->SetBranchAddress("corr_met_MultiLepCalc", &corr_met_MultiLepCalc, &b_corr_met_MultiLepCalc);
   inputTree->SetBranchAddress("corr_met_phi_MultiLepCalc", &corr_met_phi_MultiLepCalc, &b_corr_met_phi_MultiLepCalc);
   inputTree->SetBranchAddress("leptonPt_MultiLepCalc", &leptonPt_MultiLepCalc, &b_leptonPt_MultiLepCalc);
   inputTree->SetBranchAddress("leptonEta_MultiLepCalc", &leptonEta_MultiLepCalc, &b_leptonEta_MultiLepCalc);
   inputTree->SetBranchAddress("leptonPhi_MultiLepCalc", &leptonPhi_MultiLepCalc, &b_leptonPhi_MultiLepCalc);
   inputTree->SetBranchAddress("leptonEnergy_MultiLepCalc", &leptonEnergy_MultiLepCalc, &b_leptonEnergy_MultiLepCalc);
   inputTree->SetBranchAddress("leptonMiniIso_MultiLepCalc", &leptonMiniIso_MultiLepCalc, &b_leptonMiniIso_MultiLepCalc);
   inputTree->SetBranchAddress("leptonRelIso_MultiLepCalc", &leptonRelIso_MultiLepCalc, &b_leptonRelIso_MultiLepCalc);
   inputTree->SetBranchAddress("leptonDxy_MultiLepCalc", &leptonDxy_MultiLepCalc, &b_leptonDxy_MultiLepCalc);
   inputTree->SetBranchAddress("leptonDz_MultiLepCalc", &leptonDz_MultiLepCalc, &b_leptonDz_MultiLepCalc);
   inputTree->SetBranchAddress("leptonCharge_MultiLepCalc", &leptonCharge_MultiLepCalc, &b_leptonCharge_MultiLepCalc);
   inputTree->SetBranchAddress("elTrigPresel_MultiLepCalc", &elTrigPresel_MultiLepCalc, &b_elTrigPresel_MultiLepCalc);
   inputTree->SetBranchAddress("elNotConversion_MultiLepCalc", &elNotConversion_MultiLepCalc, &b_elNotConversion_MultiLepCalc);
   inputTree->SetBranchAddress("AllLeptonElPt_PtOrdered", &AllLeptonElPt_PtOrdered, &b_AllLeptonElPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElEta_PtOrdered", &AllLeptonElEta_PtOrdered, &b_AllLeptonElEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElPhi_PtOrdered", &AllLeptonElPhi_PtOrdered, &b_AllLeptonElPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElEnergy_PtOrdered", &AllLeptonElEnergy_PtOrdered, &b_AllLeptonElEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElMiniIso_PtOrdered", &AllLeptonElMiniIso_PtOrdered, &b_AllLeptonElMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElFlavor_PtOrdered", &AllLeptonElFlavor_PtOrdered, &b_AllLeptonElFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElIsTight_PtOrdered", &AllLeptonElIsTight_PtOrdered, &b_AllLeptonElIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElCount_PtOrdered", &AllLeptonElCount_PtOrdered, &b_AllLeptonElCount_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElDxy_PtOrdered", &AllLeptonElDxy_PtOrdered, &b_AllLeptonElDxy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElDz_PtOrdered", &AllLeptonElDz_PtOrdered, &b_AllLeptonElDz_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonElPt_PtOrderedOnly", &AllLeptonElPt_PtOrderedOnly, &b_AllLeptonElPt_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElEta_PtOrderedOnly", &AllLeptonElEta_PtOrderedOnly, &b_AllLeptonElEta_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElPhi_PtOrderedOnly", &AllLeptonElPhi_PtOrderedOnly, &b_AllLeptonElPhi_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElEnergy_PtOrderedOnly", &AllLeptonElEnergy_PtOrderedOnly, &b_AllLeptonElEnergy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElMiniIso_PtOrderedOnly", &AllLeptonElMiniIso_PtOrderedOnly, &b_AllLeptonElMiniIso_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElFlavor_PtOrderedOnly", &AllLeptonElFlavor_PtOrderedOnly, &b_AllLeptonElFlavor_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElIsTight_PtOrderedOnly", &AllLeptonElIsTight_PtOrderedOnly, &b_AllLeptonElIsTight_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElDxy_PtOrderedOnly", &AllLeptonElDxy_PtOrderedOnly, &b_AllLeptonElDxy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElDz_PtOrderedOnly", &AllLeptonElDz_PtOrderedOnly, &b_AllLeptonElDz_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonElPt_PtOrderedOnly_top3", &AllLeptonElPt_PtOrderedOnly_top3, &b_AllLeptonElPt_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElEta_PtOrderedOnly_top3", &AllLeptonElEta_PtOrderedOnly_top3, &b_AllLeptonElEta_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElPhi_PtOrderedOnly_top3", &AllLeptonElPhi_PtOrderedOnly_top3, &b_AllLeptonElPhi_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElEnergy_PtOrderedOnly_top3", &AllLeptonElEnergy_PtOrderedOnly_top3, &b_AllLeptonElEnergy_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElMiniIso_PtOrderedOnly_top3", &AllLeptonElMiniIso_PtOrderedOnly_top3, &b_AllLeptonElMiniIso_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElFlavor_PtOrderedOnly_top3", &AllLeptonElFlavor_PtOrderedOnly_top3, &b_AllLeptonElFlavor_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonElIsTight_PtOrderedOnly_top3", &AllLeptonElIsTight_PtOrderedOnly_top3, &b_AllLeptonElIsTight_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuPt_PtOrdered", &AllLeptonMuPt_PtOrdered, &b_AllLeptonMuPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuEta_PtOrdered", &AllLeptonMuEta_PtOrdered, &b_AllLeptonMuEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuPhi_PtOrdered", &AllLeptonMuPhi_PtOrdered, &b_AllLeptonMuPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuEnergy_PtOrdered", &AllLeptonMuEnergy_PtOrdered, &b_AllLeptonMuEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuMiniIso_PtOrdered", &AllLeptonMuMiniIso_PtOrdered, &b_AllLeptonMuMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuFlavor_PtOrdered", &AllLeptonMuFlavor_PtOrdered, &b_AllLeptonMuFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuIsTight_PtOrdered", &AllLeptonMuIsTight_PtOrdered, &b_AllLeptonMuIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuCount_PtOrdered", &AllLeptonMuCount_PtOrdered, &b_AllLeptonMuCount_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuDxy_PtOrdered", &AllLeptonMuDxy_PtOrdered, &b_AllLeptonMuDxy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuDz_PtOrdered", &AllLeptonMuDz_PtOrdered, &b_AllLeptonMuDz_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMuPt_PtOrderedOnly", &AllLeptonMuPt_PtOrderedOnly, &b_AllLeptonMuPt_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuEta_PtOrderedOnly", &AllLeptonMuEta_PtOrderedOnly, &b_AllLeptonMuEta_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuPhi_PtOrderedOnly", &AllLeptonMuPhi_PtOrderedOnly, &b_AllLeptonMuPhi_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuEnergy_PtOrderedOnly", &AllLeptonMuEnergy_PtOrderedOnly, &b_AllLeptonMuEnergy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuMiniIso_PtOrderedOnly", &AllLeptonMuMiniIso_PtOrderedOnly, &b_AllLeptonMuMiniIso_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuFlavor_PtOrderedOnly", &AllLeptonMuFlavor_PtOrderedOnly, &b_AllLeptonMuFlavor_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuIsTight_PtOrderedOnly", &AllLeptonMuIsTight_PtOrderedOnly, &b_AllLeptonMuIsTight_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuDxy_PtOrderedOnly", &AllLeptonMuDxy_PtOrderedOnly, &b_AllLeptonMuDxy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuDz_PtOrderedOnly", &AllLeptonMuDz_PtOrderedOnly, &b_AllLeptonMuDz_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMuPt_PtOrderedOnly_top3", &AllLeptonMuPt_PtOrderedOnly_top3, &b_AllLeptonMuPt_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuEta_PtOrderedOnly_top3", &AllLeptonMuEta_PtOrderedOnly_top3, &b_AllLeptonMuEta_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuPhi_PtOrderedOnly_top3", &AllLeptonMuPhi_PtOrderedOnly_top3, &b_AllLeptonMuPhi_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuEnergy_PtOrderedOnly_top3", &AllLeptonMuEnergy_PtOrderedOnly_top3, &b_AllLeptonMuEnergy_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuMiniIso_PtOrderedOnly_top3", &AllLeptonMuMiniIso_PtOrderedOnly_top3, &b_AllLeptonMuMiniIso_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuFlavor_PtOrderedOnly_top3", &AllLeptonMuFlavor_PtOrderedOnly_top3, &b_AllLeptonMuFlavor_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMuIsTight_PtOrderedOnly_top3", &AllLeptonMuIsTight_PtOrderedOnly_top3, &b_AllLeptonMuIsTight_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonPt_PtOrdered", &AllLeptonPt_PtOrdered, &b_AllLeptonPt_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonEta_PtOrdered", &AllLeptonEta_PtOrdered, &b_AllLeptonEta_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonPhi_PtOrdered", &AllLeptonPhi_PtOrdered, &b_AllLeptonPhi_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonEnergy_PtOrdered", &AllLeptonEnergy_PtOrdered, &b_AllLeptonEnergy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonMiniIso_PtOrdered", &AllLeptonMiniIso_PtOrdered, &b_AllLeptonMiniIso_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonFlavor_PtOrdered", &AllLeptonFlavor_PtOrdered, &b_AllLeptonFlavor_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonIsTight_PtOrdered", &AllLeptonIsTight_PtOrdered, &b_AllLeptonIsTight_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonCharge_PtOrdered", &AllLeptonCharge_PtOrdered, &b_AllLeptonCharge_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonCount_PtOrdered", &AllLeptonCount_PtOrdered, &b_AllLeptonCount_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonDxy_PtOrdered", &AllLeptonDxy_PtOrdered, &b_AllLeptonDxy_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonDz_PtOrdered", &AllLeptonDz_PtOrdered, &b_AllLeptonDz_PtOrdered);
   inputTree->SetBranchAddress("AllLeptonPt_PtOrderedOnly", &AllLeptonPt_PtOrderedOnly, &b_AllLeptonPt_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonEta_PtOrderedOnly", &AllLeptonEta_PtOrderedOnly, &b_AllLeptonEta_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonPhi_PtOrderedOnly", &AllLeptonPhi_PtOrderedOnly, &b_AllLeptonPhi_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonEnergy_PtOrderedOnly", &AllLeptonEnergy_PtOrderedOnly, &b_AllLeptonEnergy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonMiniIso_PtOrderedOnly", &AllLeptonMiniIso_PtOrderedOnly, &b_AllLeptonMiniIso_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonFlavor_PtOrderedOnly", &AllLeptonFlavor_PtOrderedOnly, &b_AllLeptonFlavor_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonIsTight_PtOrderedOnly", &AllLeptonIsTight_PtOrderedOnly, &b_AllLeptonIsTight_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonCharge_PtOrderedOnly", &AllLeptonCharge_PtOrderedOnly, &b_AllLeptonCharge_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonDxy_PtOrderedOnly", &AllLeptonDxy_PtOrderedOnly, &b_AllLeptonDxy_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonDz_PtOrderedOnly", &AllLeptonDz_PtOrderedOnly, &b_AllLeptonDz_PtOrderedOnly);
   inputTree->SetBranchAddress("AllLeptonPt_PtOrderedOnly_top3", &AllLeptonPt_PtOrderedOnly_top3, &b_AllLeptonPt_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonEta_PtOrderedOnly_top3", &AllLeptonEta_PtOrderedOnly_top3, &b_AllLeptonEta_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonPhi_PtOrderedOnly_top3", &AllLeptonPhi_PtOrderedOnly_top3, &b_AllLeptonPhi_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonEnergy_PtOrderedOnly_top3", &AllLeptonEnergy_PtOrderedOnly_top3, &b_AllLeptonEnergy_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonMiniIso_PtOrderedOnly_top3", &AllLeptonMiniIso_PtOrderedOnly_top3, &b_AllLeptonMiniIso_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonFlavor_PtOrderedOnly_top3", &AllLeptonFlavor_PtOrderedOnly_top3, &b_AllLeptonFlavor_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonIsTight_PtOrderedOnly_top3", &AllLeptonIsTight_PtOrderedOnly_top3, &b_AllLeptonIsTight_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("AllLeptonCharge_PtOrderedOnly_top3", &AllLeptonCharge_PtOrderedOnly_top3, &b_AllLeptonCharge_PtOrderedOnly_top3);
   inputTree->SetBranchAddress("TightLeptonPt_PtOrdered", &TightLeptonPt_PtOrdered, &b_TightLeptonPt_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonEta_PtOrdered", &TightLeptonEta_PtOrdered, &b_TightLeptonEta_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonPhi_PtOrdered", &TightLeptonPhi_PtOrdered, &b_TightLeptonPhi_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonEnergy_PtOrdered", &TightLeptonEnergy_PtOrdered, &b_TightLeptonEnergy_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonMiniIso_PtOrdered", &TightLeptonMiniIso_PtOrdered, &b_TightLeptonMiniIso_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonFlavor_PtOrdered", &TightLeptonFlavor_PtOrdered, &b_TightLeptonFlavor_PtOrdered);
   inputTree->SetBranchAddress("TightLeptonCharge_PtOrdered", &TightLeptonCharge_PtOrdered, &b_TightLeptonCharge_PtOrdered);
   inputTree->SetBranchAddress("AK4JetPt_MultiLepCalc_PtOrdered", &AK4JetPt_MultiLepCalc_PtOrdered, &b_AK4JetPt_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetEta_MultiLepCalc_PtOrdered", &AK4JetEta_MultiLepCalc_PtOrdered, &b_AK4JetEta_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetPhi_MultiLepCalc_PtOrdered", &AK4JetPhi_MultiLepCalc_PtOrdered, &b_AK4JetPhi_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetEnergy_MultiLepCalc_PtOrdered", &AK4JetEnergy_MultiLepCalc_PtOrdered, &b_AK4JetEnergy_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetFlav_MultiLepCalc_PtOrdered", &AK4JetFlav_MultiLepCalc_PtOrdered, &b_AK4JetFlav_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetBTag_MultiLepCalc_PtOrdered", &AK4JetBTag_MultiLepCalc_PtOrdered, &b_AK4JetBTag_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetBTag_bSFup_MultiLepCalc_PtOrdered", &AK4JetBTag_bSFup_MultiLepCalc_PtOrdered, &b_AK4JetBTag_bSFup_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered", &AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered, &b_AK4JetBTag_bSFdn_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetBTag_lSFup_MultiLepCalc_PtOrdered", &AK4JetBTag_lSFup_MultiLepCalc_PtOrdered, &b_AK4JetBTag_lSFup_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered", &AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered, &b_AK4JetBTag_lSFdn_MultiLepCalc_PtOrdered);
   inputTree->SetBranchAddress("HadronicVHtID_JetSubCalc", &HadronicVHtID_JetSubCalc, &b_HadronicVHtID_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtPt_JetSubCalc", &HadronicVHtPt_JetSubCalc, &b_HadronicVHtPt_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtEta_JetSubCalc", &HadronicVHtEta_JetSubCalc, &b_HadronicVHtEta_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtPhi_JetSubCalc", &HadronicVHtPhi_JetSubCalc, &b_HadronicVHtPhi_JetSubCalc);
   inputTree->SetBranchAddress("HadronicVHtEnergy_JetSubCalc", &HadronicVHtEnergy_JetSubCalc, &b_HadronicVHtEnergy_JetSubCalc);
   inputTree->SetBranchAddress("genJetPt_MultiLepCalc", &genJetPt_MultiLepCalc, &b_genJetPt_MultiLepCalc);
   inputTree->SetBranchAddress("genJetEta_MultiLepCalc", &genJetEta_MultiLepCalc, &b_genJetEta_MultiLepCalc);
   inputTree->SetBranchAddress("genJetPhi_MultiLepCalc", &genJetPhi_MultiLepCalc, &b_genJetPhi_MultiLepCalc);
   inputTree->SetBranchAddress("genJetEnergy_MultiLepCalc", &genJetEnergy_MultiLepCalc, &b_genJetEnergy_MultiLepCalc);
   inputTree->SetBranchAddress("BJetLeadPt", &BJetLeadPt, &b_BJetLeadPt);
   inputTree->SetBranchAddress("BJetLeadPt_shifts", &BJetLeadPt_shifts, &b_BJetLeadPt_shifts);
   inputTree->SetBranchAddress("WJetLeadPt", &WJetLeadPt, &b_WJetLeadPt);
   inputTree->SetBranchAddress("WJetLeadPt_shifts", &WJetLeadPt_shifts, &b_WJetLeadPt_shifts);
   inputTree->SetBranchAddress("TJetLeadPt", &TJetLeadPt, &b_TJetLeadPt);
   inputTree->SetBranchAddress("TJetLeadPt_shifts", &TJetLeadPt_shifts, &b_TJetLeadPt_shifts);
   inputTree->SetBranchAddress("AK4HTpMETpLepPt", &AK4HTpMETpLepPt, &b_AK4HTpMETpLepPt);
   inputTree->SetBranchAddress("AK4HT", &AK4HT, &b_AK4HT);
   inputTree->SetBranchAddress("ddBkgWeights", &ddBkgWeights, &b_ddBkgWeights);
   inputTree->SetBranchAddress("ddBkgWeights_scan", &ddBkgWeights_scan, &b_ddBkgWeights_scan);
   inputTree->SetBranchAddress("ddBkgWeights_scan_muFR", &ddBkgWeights_scan_muFR, &b_ddBkgWeights_scan_muFR);
   inputTree->SetBranchAddress("ddBkgWeights_scan_elFR", &ddBkgWeights_scan_elFR, &b_ddBkgWeights_scan_elFR);
   inputTree->SetBranchAddress("NJets_MultiLepCalc", &NJets_MultiLepCalc, &b_NJets_MultiLepCalc);
   inputTree->SetBranchAddress("NJetsAK8_JetSubCalc", &NJetsAK8_JetSubCalc, &b_NJetsAK8_JetSubCalc);
   inputTree->SetBranchAddress("NJetsBTag_MultiLepCalc", &NJetsBTag_MultiLepCalc, &b_NJetsBTag_MultiLepCalc);
   inputTree->SetBranchAddress("NJetsBTagwithSF_MultiLepCalc", &NJetsBTagwithSF_MultiLepCalc, &b_NJetsBTagwithSF_MultiLepCalc);
   inputTree->SetBranchAddress("NJetsBTagwithSF_MultiLepCalc_shifts", &NJetsBTagwithSF_MultiLepCalc_shifts, &b_NJetsBTagwithSF_MultiLepCalc_shifts);
   inputTree->SetBranchAddress("NJetsBTagwithSF_MultiLepCalc_noLepCorr", &NJetsBTagwithSF_MultiLepCalc_noLepCorr, &b_NJetsBTagwithSF_MultiLepCalc_noLepCorr);
   inputTree->SetBranchAddress("NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts", &NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts, &b_NJetsBTagwithSF_MultiLepCalc_noLepCorr_shifts);
   inputTree->SetBranchAddress("topPt", &topPt, &b_topPt);
   inputTree->SetBranchAddress("topPtGen", &topPtGen, &b_topPtGen);
   inputTree->SetBranchAddress("topMass", &topMass, &b_topMass);
   inputTree->SetBranchAddress("minMleppBjet", &minMleppBjet, &b_minMleppBjet);
   inputTree->SetBranchAddress("minMleppBjet_shifts", &minMleppBjet_shifts, &b_minMleppBjet_shifts);
   inputTree->SetBranchAddress("minMleppJet", &minMleppJet, &b_mixnMleppJet);
   inputTree->SetBranchAddress("minMlllBjet", &minMlllBjet, &b_minMlllBjet);
   inputTree->SetBranchAddress("minMlllBjet_shifts", &minMlllBjet_shifts, &b_minMlllBjet_shifts);
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
   inputTree->SetBranchAddress("minDR_lep1Jet", &minDR_lep1Jet, &b_minDR_lep1Jet);
   inputTree->SetBranchAddress("minDR_lep2Jet", &minDR_lep2Jet, &b_minDR_lep2Jet);
   inputTree->SetBranchAddress("minDR_lep3Jet", &minDR_lep3Jet, &b_minDR_lep3Jet);
   inputTree->SetBranchAddress("minDR_lepMET", &minDR_lepMET, &b_minDR_lepMET);
   inputTree->SetBranchAddress("minDR_METJet", &minDR_METJet, &b_minDR_METJet);
   inputTree->SetBranchAddress("minDPhi_METJet", &minDPhi_METJet, &b_minDPhi_METJet);
   inputTree->SetBranchAddress("ptRel_minDRlepJet", &ptRel_minDRlepJet, &b_ptRel_minDRlepJet);
   inputTree->SetBranchAddress("ptRel_minDRlep1Jet", &ptRel_minDRlep1Jet, &b_ptRel_minDRlep1Jet);
   inputTree->SetBranchAddress("ptRel_minDRlep2Jet", &ptRel_minDRlep2Jet, &b_ptRel_minDRlep2Jet);
   inputTree->SetBranchAddress("ptRel_minDRlep3Jet", &ptRel_minDRlep3Jet, &b_ptRel_minDRlep3Jet);
   inputTree->SetBranchAddress("MT_lepMet", &MT_lepMet, &b_MT_lepMet);
   inputTree->SetBranchAddress("deltaR_lepJets", &deltaR_lepJets, &b_deltaR_lepJets);
   inputTree->SetBranchAddress("deltaR_lep1Jets", &deltaR_lep1Jets, &b_deltaR_lep1Jets);
   inputTree->SetBranchAddress("deltaR_lep2Jets", &deltaR_lep2Jets, &b_deltaR_lep2Jets);
   inputTree->SetBranchAddress("deltaR_lep3Jets", &deltaR_lep3Jets, &b_deltaR_lep3Jets);
   inputTree->SetBranchAddress("ptRel_lepJets", &ptRel_lepJets, &b_ptRel_lepJets);
   inputTree->SetBranchAddress("ptRel_lep1Jets", &ptRel_lep1Jets, &b_ptRel_lep1Jets);
   inputTree->SetBranchAddress("ptRel_lep2Jets", &ptRel_lep2Jets, &b_ptRel_lep2Jets);
   inputTree->SetBranchAddress("ptRel_lep3Jets", &ptRel_lep3Jets, &b_ptRel_lep3Jets);
   inputTree->SetBranchAddress("deltaR_lepMETs", &deltaR_lepMETs, &b_deltaR_lepMETs);
   inputTree->SetBranchAddress("deltaR_METJets", &deltaR_METJets, &b_deltaR_METJets);
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
