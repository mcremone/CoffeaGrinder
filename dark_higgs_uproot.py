import uproot, uproot_methods
import numpy as np
import fnal_column_analysis_tools
from fnal_column_analysis_tools.analysis_objects import JaggedCandidateArray


extractor = fnal_column_analysis_tools.lookup_tools.extractor()
extractor.add_weight_sets(['* * eleTrig.root'])
extractor.finalize()

evaluator = extractor.make_evaluator()



f = "nano_5.root"

met_trigger_paths = ["HLT_PFMET170_NoiseCleaned",
            "HLT_PFMET170_HBHECleaned",
            "HLT_PFMET170_JetIdCleaned",
            "HLT_PFMET170_NotCleaned",
            "HLT_PFMET170_HBHE_BeamHaloCleaned",
            "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight",
            "HLT_PFMETNoMu110_NoiseCleaned_PFMHTNoMu110_IDTight",
            "HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight",
            "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight",
            "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight",
            "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight",
            "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"]
met_trigger_columns = Table({path:path for path in met_trigger_paths.items()})

singleele_trigger_paths = ["HLT_Ele27_WP85_Gsf",
          "HLT_Ele27_WPLoose_Gsf",
          "HLT_Ele105_CaloIdVT_GsfTrkIdT",
          "HLT_Ele27_WPTight_Gsf",
          "HLT_Ele30_WPTight_Gsf",
          "HLT_Ele27_eta2p1_WPTight_Gsf",
          "HLT_Ele32_eta2p1_WPTight_Gsf",
          "HLT_Ele35_WPLoose_Gsf",
          "HLT_ECALHT800"]
singleele_trigger_columns = Table({path:path for path in singleele_trigger_paths.items()})

singlephoton_triggerpaths = ["HLT_Photon175",
          "HLT_Photon200",
          "HLT_Photon165_HE10",
          "HLT_Photon36_R9Id90_HE10_IsoM",
          "HLT_Photon50_R9Id90_HE10_IsoM",
          "HLT_Photon75_R9Id90_HE10_IsoM",
          "HLT_Photon90_R9Id90_HE10_IsoM",
          "HLT_Photon120_R9Id90_HE10_IsoM",
          "HLT_Photon165_R9Id90_HE10_IsoM",
          "HLT_Photon300_NoHE",
          "HLT_ECALHT800",
          "HLT_CaloJet500_NoJetID"]
singlephoton_trigger_columns = Table({path:path for path in singlephoton_trigger_paths.items()})


electron_columns = {'pt':'Electron_pt','eta':'Electron_eta','phi':'Electron_phi','mass':'Electron_mass','iso':'Electron_pfRelIso03_all','dxy':'Electron_dxy','dz':'Electron_dz','id':'Electron_mvaSpring16GP_WP90'}

muon_columns = {'pt':'Muon_pt','eta':'Muon_eta','phi':'Muon_phi','mass':'Muon_mass','iso':'Muon_pfRelIso04_all','dxy':'Muon_dxy','dz':'Muon_dz'}


jet_columns = {'pt':'Jet_pt','eta':'Jet_eta','phi':'Jet_phi','mass':'Jet_mass','id':'Jet_jetId'}

tau_columns = {'pt':'Tau_pt','eta':'Tau_eta','phi':'Tau_phi','mass':'Tau_mass','decayMode':'Tau_idDecayMode','decayModeNew':'Tau_idDecayModeNewDMs','id':'Tau_idMVAnewDM'}

photon_columns = {'pt':'Photon_pt','eta':'Photon_eta','phi':'Photon_phi','mass':'Photon_mass',}

all_columns [electron_columns,muon_columns]

columns = []
for cols in all_columns: columns.extend(list(cols.values()))

for arrays in uproot.iterate(f,'Events',columns,entrysteps=50000):

        triggers = JaggedCandidateArray.candidatesfromcounts(arrays[met_trigger_columns['HLT_PFMET170_NoiseCleaned']].counts, **{'MET':np.prod([arrays[val].content for val in met_trigger_columns]),'SingleEle':np.prod([arrays[val].content for val in singleelectron_trigger_columns]),'SinglePhoton':np.prod([arrays[val].content for val in singlephoton_trigger_columns])}
        
        electrons = JaggedCandidateArray.candidatesfromcounts(arrays[electron_columns['pt']].counts, **{key:arrays[val].content for key,val in electron_columns.items()})
                                                             
        muons = JaggedCandidateArray.candidatesfromcounts(arrays[muon_columns['pt']].counts, **{key:arrays[val].content for key,val in muon_columns.items()})
                                                             
        taus = JaggedCandidateArray.candidatesfromcounts(arrays[tau_columns['pt']].counts, **{key:arrays[val].content for key,val in tau_columns.items()})
                                                             
        photons = JaggedCandidateArray.candidatesfromcounts(arrays[tau_columns['pt']].counts, **{key:arrays[val].content for key,val in photon_columns.items()})
                                                             
        jets = JaggedCandidateArray.candidatesfromcounts(arrays[tau_columns['pt']].counts, **{key:arrays[val].content for key,val in jet_columns.items()})

loose_electron_selection = (electrons.pt>7)*(abs(electrons.eta)<2.4)*(abs(electrons.dxy)<0.05)*(abs(electrons.dz)<0.2)*(electrons.iso<0.4)*(electrons.id)
loose_muon_selection =  (muons.pt>5)*(abs(muons.eta)<2.4)*(abs(muons.dxy)<0.5)*(abs(muons.dz)<1.0)*(muons.iso<0.4)
loose_photon_selection = (photons.pt>15)*(abs(photons.eta)<2.5)

tau_selection = (taus.pt>18)*(abs(taus.eta)<2.3)*(taus.decayMode)*(taus.id)
jet_selection = (jets.pt>25)*(abs(jets.eta)<4.5)*(jets.id&2)

loose_electrons = electrons[loose_electron_selection]
loose_muons = muons[loose_muon_selection]
loose_photons = photons[loose_photon_selection]



e_counts = loose_electrons.counts
e_sfTrigg = np.ones(loose_electrons.size)
e_sfTrigg[e_counts>0] = 1 - evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])
e_sfTrigg[e_counts > 1] =  1- (1- evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>1,0], loose_electrons.pt[e_counts > 1,0]))*(1- evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>1,1], loose_electrons.pt[e_counts > 1,1]))

#print evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])





