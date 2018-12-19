import uproot, uproot_methods
import numpy as np
import fnal_column_analysis_tools
from fnal_column_analysis_tools.analysis_objects import JaggedCandidateArray


extractor = fnal_column_analysis_tools.lookup_tools.extractor()
extractor.add_weight_sets(['* * eleTrig.root','* * muon_trig_Run2016BtoF.root'])
extractor.finalize()

evaluator = extractor.make_evaluator()



f = "nano_5.root"

electron_columns = {'pt':'Electron_pt','eta':'Electron_eta','phi':'Electron_phi','mass':'Electron_mass','iso':'Electron_pfRelIso03_all','dxy':'Electron_dxy','dz':'Electron_dz','id':'Electron_mvaSpring16GP_WP90'}

muon_columns = {'pt':'Muon_pt','eta':'Muon_eta','phi':'Muon_phi','mass':'Muon_mass','iso':'Muon_pfRelIso04_all','dxy':'Muon_dxy','dz':'Muon_dz'}


jet_columns = {'pt':'Jet_pt','eta':'Jet_eta','phi':'Jet_phi','mass':'Jet_mass','id':'Jet_jetId'}

#tau_columns = {'pt':'Tau_pt','eta':'Tau_eta','phi':'Tau_phi','mass':'Tau_mass','decayMode':'Tau_idDecayMode','decayModeNew':'Tau_idDecayModeNewDMs','id':'Tau_idMVAnewDM'}

#photon_columns = {'pt':'Photon_pt','eta':'Photon_eta','phi':'Photon_phi','mass':'Photon_mass',}

all_columns = [electron_columns,muon_columns]

columns = []
for cols in all_columns: columns.extend(list(cols.values()))

for arrays in uproot.iterate(f,'Events',columns,entrysteps=50000):
        electrons = JaggedCandidateArray.candidatesfromcounts(arrays[electron_columns['pt']].counts, **{key:arrays[val].content for key,val in electron_columns.items()})
        muons = JaggedCandidateArray.candidatesfromcounts(arrays[muon_columns['pt']].counts, **{key:arrays[val].content for key,val in muon_columns.items()})
        #photons = JaggedCandidateArray.candidatesfromcounts(arrays[photon_columns['pt']].counts, **{key:arrays[val].content for key,val in photon_columns.items()})
        #taus = JaggedCandidateArray.candidatesfromcounts(arrays[tau_columns['pt']].counts, **{key:arrays[val].content for key,val in tau_columns.items()})
        

loose_electron_selection = (electrons.pt>7)*(abs(electrons.eta)<2.4)*(abs(electrons.dxy)<0.05)*(abs(electrons.dz)<0.2)*(electrons.iso<0.4)*(electrons.id)
loose_muon_selection =  (muons.pt>5)*(abs(muons.eta)<2.4)*(abs(muons.dxy)<0.5)*(abs(muons.dz)<1.0)*(muons.iso<0.4)
#loose_photon_selection = (photons.pt>15)*(abs(photons.eta)<2.5)

#tau_selection = (taus.pt>18)*(abs(taus.eta)<2.3)*(taus.decayMode)*(taus.id)
#jet_selection = (jets.pt>25)*(abs(jets.eta)<4.5)*(jets.id&2)

loose_electrons = electrons[loose_electron_selection]
loose_muons = muons[loose_muon_selection]
#loose_photons = photons[loose_photon_selection]



e_counts = loose_electrons.counts
e_sfTrigg = np.ones(loose_electrons.size)
e_sfTrigg[e_counts>0] = 1 - evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])
e_sfTrigg[e_counts > 1] =  1- (1- evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>1,0], loose_electrons.pt[e_counts > 1,0]))*(1- evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>1,1], loose_electrons.pt[e_counts > 1,1]))


loose_m_selection = (muons.pt>5)*(abs(muons.eta)<2.4)*(abs(muons["dxy"])<0.5)*(abs(muons["dz"])<1)*(muons["iso"]<0.4)
loose_muons = muons[loose_m_selection]

m_counts = loose_muons.counts
m_sfTrigg = np.ones(loose_muons.size)

# reall muon sf = "IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesDATA/pt_abseta_DATA"

m_sfTrigg[m_counts>0] =  evaluator["IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio"](loose_muons.eta[m_counts>0,0], loose_muons.pt[m_counts > 0,0])
m_sfTrigg[m_counts > 1] =  1- (1- evaluator["IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio"](loose_muons.eta[m_counts>1,0], loose_muons.pt[m_counts > 1,0]))*(1- evaluator["IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio"](loose_muons.eta[m_counts>1,1], loose_muons.pt[m_counts > 1,1]))



#print evaluator["hEffEtaPt"](loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])





