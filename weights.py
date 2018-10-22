
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



