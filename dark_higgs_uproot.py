import uproot, uproot_methods
import numpy as np
import fnal_column_analysis_tools
from fnal_column_analysis_tools.analysis_objects import JaggedCandidateArray

def dummySF(eta, pt):
	return (eta+pt)/(eta*pt)

f = uproot.open("nano_5.root")
e = f["Events"]

electron_columns = {'pt':'Electron_pt','eta':'Electron_eta','phi':'Electron_phi','mass':'Electron_mass'}

muon_columns = {'pt':'Muon_pt','eta':'Muon_eta','phi':'Muon_phi','mass':'Muon_mass'}

electrons = JaggedCandidateArray.candidatesfromcounts(arrays[electron_columns['pt']].counts, **{key:arrays[val].content for key,val in electron_columns.items()})
muons = JaggedCandidateArray.candidatesfromcounts(arrays[muon_columns['pt']].counts, **{key:arrays[val].content for key,val in muon_columns.items()})

electrons.add_attributes(iso=Electron_pfRelIso03_all,dxy=Electron_dxy,dz=Electron_dz,id=Electron_mvaSpring16GP_WP90)
muons.add_attributes(iso=Muon_pfRelIso04_all,dxy=Muon_dxy,dz=Muon_dz)
                                                                                                                                                                #loose lepton selection
	#loose electron selection

loose_e_selection = (electrons.pt>7)*(abs(electrons.eta)<2.4)*(abs(electrons["dxy"])<0.05)*(abs(electrons["dz"])<0.2)*(electrons["pfRelIso03_all"]<0.4)*(electrons["mvaSpring16GP_WP90"])
loose_electrons = electrons[loose_e_selection]
e_counts = loose_electrons.counts
e_sfTrigg = np.ones(loose_electrons.size)
e_sfTrigg[e_counts>0] = 1 - dummySF(loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])
e_sfTrigg[e_counts > 1] =  1- (1- dummySF(loose_electrons.eta[e_counts>1,0], loose_electrons.pt[e_counts > 1,0]))*(1- dummySF(loose_electrons.eta[e_counts>1,1], loose_electrons.pt[e_counts > 1,1]))







