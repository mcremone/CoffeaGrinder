
sfLepTrack = 1
#  if complicated leptons
for i in range(0, int(np.minimum(2,len(leptons)))):
                if leptons[i][3] ==11:
                    if abs(leptons[i][1]) <2.5 and leptons[i][0] > 10:
                        if leptons[i][2]:
                     
                            sfLepID = sfLepID *valueAt(corrDict,"leptonic_scalefactors_80x_egpog_37ifb_scalefactors_Tight_Electron",leptons[i][1], leptons[i][0])
                            
                        else:
                            
                            sfLepID = sfLepID *valueAt(corrDict,"scaleFactor_electron_summer16_scaleFactor_electron_vetoid_RooCMSShape_pu_0_100",leptons[i][1], leptons[i][0])

                    sfLepTrack = sfLepTrack*valueAt(corrDict,"leptonic_scalefactors_80x_egpog_37ifb_scalefactors_Reco_Electron",abs(leptins[i][1]),leptons[i][0])

                if leptons[i][3]==13:
                    if abs(leptons[i][1]) <2.4 and leptons[i][0] > 10:
                        if leptons[i][2]:
                            
                            sfLepID = sfLepID*valueAt(corrDict,"leptonic_muon_scalefactors_37ifb_scalefactors_TightId_Muon",abs(leptons[i][1]), leptons[i][0])
                            sfLepISO = sfLepIso*valueAt(corrDict,"leptonic_muon_scalefactors_37ifb.root_scalefactors_Iso_MuonTightId",abs(leptons[i][1]),leptons[i][0])
                        else:
                            
                            sfLepID=sfLepID*valueAt(corrDict,"leptonic_muon_scalefactors_37ifb_scalefactors_MuonLooseId_Muon",abs(leptons[i][1]), leptons[i][0])
                            sfLepISO = sfLepIso*valueAt(corrDict,"leptonic_muon_scalefactors_37ifb_scalefactors_Iso_MuonTightId",abs(leptons[i][1]),leptons[i][0])

		    
		    sfLepTrack = sfLepTrack*valueAt(corrDict,"leptonic_Tracking_EfficienciesAndSF_BCDEFGH_ratio_eff_eta3_dr030e030_corr",leptins[i][1],leptons[i][0])
            sf_lepID = np.append(sf_lepID,sfLepID) 
	    sf_lepIso = np.append(sf_lepID,sfLepIso)
	    sf_lepID = np.append(sf_lepTrack,sfLepTrack)


# if not complicated leptons
for i in range(0, int(np.minimum(2,len(leptons)))):
                if leptons[i][3] ==11:
                    if abs(leptons[i][1]) <2.5 and leptons[i][0] > 10:
                        if leptons[i][2]:
                            
                            sfLepID = sfLepID *valueAt(corrDict,"scalefactors_80x_egpog_37ifb_scalefactors_Tight_Electron",leptons[i][1], leptons[i][0])
                            
                        else:
                            
                            sfLepID = sfLepID *valueAt(corrDict,"scaleFactor_electron_summer16_scaleFactor_electron_vetoid_RooCMSShape_pu_0_100",leptons[i][1], leptons[i][0])

                    sfLepTrack = sfLepTrack*valueAt(corrDict,"scaleFactor_electron_reco_summer16.root_scaleFactor_electron_reco_RooCMSShape_pu_0_100",leptons[i][1],leptons[i][0])

                if leptons[i][3]==13:
                    if abs(leptons[i][1]) <2.4 and leptons[i][0] > 10:
                        if leptons[i][2]:
                            
                            sfLepID = sfLepID*valueAt(corrDict,"muon_scalefactors_37ifb_scalefactors_TightId_Muon",abs(leptons[i][1]), leptons[i][0])
                            sfLepISO = sfLepIso*valueAt(corrDict,"muon_scalefactors_37ifb_scalefactors_Iso_MuonTightId",abs(leptons[i][1]),leptons[i][0])
                        else:
                            
                            sfLepID=sfLepID*valueAt(corrDict,"muon_scalefactors_37ifb_scalefactors_MuonLooseId_Muon",abs(leptons[i][1]), leptons[i][0])
                            sfLepISO = sfLepIso*valueAt(corrDict,"muon_scalefactors_37ifb_scalefactors_Iso_MuonLooseId",abs(leptons[i][1]),leptons[i][0])

		    sfLepTrack = sfLepTrack*valueAt(corrDict,"Tracking_12p9_htrack2",abs(leptins[i][1]),leptons[i][0])
            sf_lepID = np.append(sf_lepID,sfLepID) 
	    sf_lepIso = np.append(sf_lepID,sfLepIso)
	    sf_lepID = np.append(sf_lepTrack,sfLepTrack)
# *******************************************************************************************************************************************************************************************


# loop over gen particles

	# if (analysis->processType==kZ)
		# if (analysis->vbf)
		gt->sf_ewkV = GetCorr(cZEWK,gt->genBosonPt);
		valueAt(corrDict,"kfactor_24bins_EWKcorr_Z",)
		# else
		valueAt(corrDict,"kfactors_EWKcorr_Z",)

		h1Corrs[cZEWK]->GetHist()->Divide(h1Corrs[cZNLO]->GetHist());  # ZJets_012j_NLO_nominal
		h1Corrs[cZNLO]->GetHist()->Divide(hZLO);
		TH1D *hZLO    = (TH1D*)fKFactor->Get("ZJets_LO/inv_pt");
	# if (analysis->processType==kW)
		# if vbf
		valueAt(corrDict,"kfactor_24bins_EWKcorr_W",)
		# else
		valueAt(corrDict,"kfactors_EWKcorr_W",)

		h1Corrs[cWEWK]->GetHist()->Divide(h1Corrs[cWNLO]->GetHist());  # WJets_012j_NLO_nominal
		h1Corrs[cWNLO]->GetHist()->Divide(hWLO); 
		TH1D *hWLO    = (TH1D*)fKFactor->Get("WJets_LO/inv_pt");
	# if (analysis->processType==kA) 
		# (gen.pt() > gt->trueGenBosonPt) 
		#if vbf
			valueAt(corrDict,"kfactor_24bins_EWKcorr_photon",)
		# else
			valueAt(corrDict,"kfactors_EWKcorr_photon",)

		 h1Corrs[cAEWK]->GetHist()->Divide(h1Corrs[cANLO]->GetHist());  # "GJets_1j_NLO/nominal_G"
		 h1Corrs[cANLO]->GetHist()->Divide(hALO);
		TH1D *hALO    = (TH1D*)fKFactor->Get("GJets_LO/inv_pt_G");
	# cases where no boson was found
	# if (analysis->processType==kZ)
		same as above
	# else if (analysis->processType==kW) 
		same as above








