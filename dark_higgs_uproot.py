import uproot, uproot_methods
import numpy as np
import fnal_column_analysis_tools
from fnal_column_analysis_tools.analysis_objects import JaggedCandidateArray

def dummySF(eta, pt):
	return (eta+pt)/(eta*pt)

f = uproot.open("nano_5.root")
e = f["Events"]

electrons_pt = np.concatenate(e.array("Electron_pt"))
electrons_eta = np.concatenate(e.array("Electron_eta"))
electrons_phi = np.concatenate(e.array("Electron_phi"))
electrons_mass = np.concatenate(e.array("Electron_mass"))
e_counts = e.array("nElectron")

muons_pt = np.concatenate(e.array("Muon_pt"))
muons_eta = np.concatenate(e.array("Muon_eta"))
muons_phi = np.concatenate(e.array("Muon_phi"))
muons_mass = np.concatenate( e.array("Muon_mass"))
m_counts = e.array("nMuon")

muons = JaggedCandidateArray.candidatesfromcounts(m_counts,pt = muons_pt, eta=muons_eta, phi=muons_phi, mass=muons_mass)
muons.add_attributes(pfRelIso04_all=np.concatenate(e.array("Muon_pfRelIso04_all")),
					 dxy=np.concatenate(e.array("Muon_dxy")),
					 dz=np.concatenate(e.array("Muon_dz"))
					)

electrons = JaggedCandidateArray.candidatesfromcounts(e_counts,pt = electrons_pt, eta=electrons_eta, phi=electrons_phi, mass=electrons_mass)
electrons.add_attributes(pfRelIso03_all=np.concatenate(e.array("Electron_pfRelIso03_all")),
						 dxy=np.concatenate(e.array("Electron_dxy")),
						 dz=np.concatenate(e.array("Electron_dz")),
						 mvaSpring16GP_WP90=np.concatenate(e.array("Electron_mvaSpring16GP_WP90"))
				    	)                                                                                                                                                                                                      

#loose lepton selection
	#loose electron selection

loose_e_selection = (electrons.pt>7)*(abs(electrons.eta)<2.4)*(abs(electrons["dxy"])<0.05)*(abs(electrons["dz"])<0.2)*(electrons["pfRelIso03_all"]<0.4)*(electrons["mvaSpring16GP_WP90"])
loose_electrons = electrons[loose_e_selection]
e_counts = loose_electrons.counts
e_sfTrigg = np.ones(loose_electrons.size)
e_sfTrigg[e_counts>0] = 1 - dummySF(loose_electrons.eta[e_counts>0,0], loose_electrons.pt[e_counts > 0,0])
e_sfTrigg[e_counts > 1] =  1- (1- dummySF(loose_electrons.eta[e_counts>1,0], loose_electrons.pt[e_counts > 1,0]))*(1- dummySF(loose_electrons.eta[e_counts>1,1], loose_electrons.pt[e_counts > 1,1]))







