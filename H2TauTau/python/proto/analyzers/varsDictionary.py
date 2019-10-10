# change the branch names here

vars = {}

# Event ID
vars['run'] = {'std': 'run', 'sync': 'run'}
vars['lumi'] = {'std': 'lumi', 'sync': 'lumi'}
vars['event'] = {'std': 'event', 'sync': 'evt'}

vars['XSecLumiWeight'] = {'std': 'XSecLumiWeight', 'sync': 'XSecLumiWeight'}

vars['genboson_genMass'] = {'std': 'genboson_genMass', 'sync': 'genMass'}

# My own variables

vars['Z_mm_aligned'] = {'std': 'Z_mm_aligned', 'sync': 'Z_mm_aligned'}
vars['Z_ee_aligned'] = {'std': 'Z_ee_aligned', 'sync': 'Z_ee_aligned'}

vars['Zboson_mm_SS'] = {'std': 'Z_mm_SS', 'sync': 'Z_SS'}
vars['Zboson_ee_SS'] = {'std': 'Z_ee_SS', 'sync': 'Z_SS'}

vars['Hboson_mt_SS'] = {'std': 'H_mt_SS', 'sync': 'H_SS'}
vars['Hboson_tt_SS'] = {'std': 'H_tt_SS', 'sync': 'H_SS'}
vars['Hboson_et_SS'] = {'std': 'H_et_SS', 'sync': 'H_SS'}
vars['Hboson_em_SS'] = {'std': 'H_em_SS', 'sync': 'H_SS'}

vars['Hboson_mt_METphi'] = {'std': 'H_mt_METphi', 'sync': 'H_METphi'}
vars['Hboson_tt_METphi'] = {'std': 'H_tt_METphi', 'sync': 'H_METphi'}
vars['Hboson_et_METphi'] = {'std': 'H_et_METphi', 'sync': 'H_METphi'}
vars['Hboson_em_METphi'] = {'std': 'H_em_METphi', 'sync': 'H_METphi'}

vars['Aboson_mt_METphi'] = {'std': 'A_mt_METphi', 'sync': 'A_METphi'}
vars['Aboson_tt_METphi'] = {'std': 'A_tt_METphi', 'sync': 'A_METphi'}
vars['Aboson_et_METphi'] = {'std': 'A_et_METphi', 'sync': 'A_METphi'}
vars['Aboson_em_METphi'] = {'std': 'A_em_METphi', 'sync': 'A_METphi'}

# ET
vars['H_et_l1_decayMode'] = {'std': 'H_et_l1_decayMode', 'sync': 'decayMode_3'}
vars['H_et_l2_decayMode'] = {'std': 'H_et_l2_decayMode', 'sync': 'decayMode_4'}

vars['H_em_l1_decayMode'] = {'std': 'H_em_l1_decayMode', 'sync': 'decayMode_3'}
vars['H_em_l2_decayMode'] = {'std': 'H_em_l2_decayMode', 'sync': 'decayMode_4'}

vars['H_mt_l1_decayMode'] = {'std': 'H_mt_l1_decayMode', 'sync': 'decayMode_3'}
vars['H_mt_l2_decayMode'] = {'std': 'H_mt_l2_decayMode', 'sync': 'decayMode_4'}

vars['H_tt_l1_decayMode'] = {'std': 'H_tt_l1_decayMode', 'sync': 'decayMode_3'}
vars['H_tt_l2_decayMode'] = {'std': 'H_tt_l2_decayMode', 'sync': 'decayMode_4'}

vars['H_et_l1_eid_spring16'] = {'std': 'H_et_l1_eid_spring16', 'sync': 'l3_eid_90'}
vars['H_et_l1_eid_spring16_80'] = {'std': 'H_et_l1_eid_spring16_80', 'sync': 'l3_eid_80'}
vars['H_et_l2_againstElectronMVA6'] = {'std': 'H_et_l2_againstElectronMVA6', 'sync': 'l4_againstElectron'}
vars['H_et_l2_byMediumIsolationMVArun2v1DBoldDMwLT'] = {'std': 'H_et_l2_byMediumIsolationMVArun2v1DBoldDMwLT', 'sync': 'l4_byMediumIsolationMVArun2v1DBoldDMwLT'}

#TT
vars['H_tt_l1_byMediumIsolationMVArun2v1DBoldDMwLT'] = {'std': 'H_tt_l1_byMediumIsolationMVArun2v1DBoldDMwLT', 'sync': 'l3_byMediumIsolationMVArun2v1DBoldDMwLT'}
vars['H_tt_l2_byMediumIsolationMVArun2v1DBoldDMwLT'] = {'std': 'H_tt_l2_byMediumIsolationMVArun2v1DBoldDMwLT', 'sync': 'l4_byMediumIsolationMVArun2v1DBoldDMwLT'}


#MT
vars['H_mt_l1_muonid_loose'] = {'std': 'H_mt_l1_muonid_loose', 'sync': 'l3_muonid_loose'}
vars['H_mt_l2_byMediumIsolationMVArun2v1DBoldDMwLT'] = {'std': 'H_mt_l2_byMediumIsolationMVArun2v1DBoldDMwLT', 'sync': 'l4_byMediumIsolationMVArun2v1DBoldDMwLT'}
vars['H_mt_l2_againstMuon3'] = {'std': 'H_mt_l2_againstMuon3', 'sync': 'l4_againstMuon'}

#EM
vars['H_em_l1_eid_spring16'] = {'std': 'H_em_l1_eid_spring16', 'sync': 'l3_eid_90'}
vars['H_em_l1_eid_spring16_80'] = {'std': 'H_em_l1_eid_spring16_80', 'sync': 'l3_eid_80'}
vars['H_em_l2_muonid_loose'] = {'std': 'H_em_l2_muonid_loose', 'sync': 'l4_muonid_loose'}


# EE
vars['Zboson_ee_pt'] = {'std': 'Zboson_ee_pt', 'sync': 'Z_Pt'}
vars['Zboson_ee_mass']= {'std': 'Zboson_ee_mass', 'sync': 'm_vis'}
vars['Zboson_ee_DR'] = {'std': 'Zboson_ee_DR', 'sync': 'Z_DR'}
vars['Zboson_ee_eta'] = {'std': 'Zboson_ee_eta', 'sync': 'Z_Eta'}
vars['Zboson_ee_phi'] = {'std': 'Zboson_ee_phi', 'sync': 'Z_Phi'}

vars['Z_ee_l1_pt']  = {'std': 'Z_ee_l1_pt', 'sync': 'pt_1'}
vars['Z_ee_l1_phi']  = {'std': 'Z_ee_l1_phi', 'sync': 'phi_1'}
vars['Z_ee_l1_eta']  = {'std': 'Z_ee_l1_eta', 'sync': 'eta_1'}
vars['Z_ee_l1_reliso05']  = {'std': 'Z_ee_l1_reliso05', 'sync': 'iso_1'}

vars['Z_ee_l2_pt']  = {'std': 'Z_ee_l2_pt', 'sync': 'pt_2'}
vars['Z_ee_l2_phi']  = {'std': 'Z_ee_l2_phi', 'sync': 'phi_2'}
vars['Z_ee_l2_eta']  = {'std': 'Z_ee_l2_eta', 'sync': 'eta_2'}
vars['Z_ee_l2_reliso05']  = {'std': 'Z_ee_l2_reliso05', 'sync': 'iso_2'}

#Variable('eid_spring16MVAraw', lambda ele: ele.mvaRun2('Spring16GP')),
vars['Z_ee_l1_eid_spring16MVAraw']  = {'std': 'Z_ee_l1_eid_spring16MVAraw', 'sync': 'IdRawMva_1'}
vars['Z_ee_l2_eid_spring16MVAraw']  = {'std': 'Z_ee_l2_eid_spring16MVAraw', 'sync': 'IdRawMva_2'}

vars['Z_ee_l1_gen_match']  = {'std': 'Z_ee_l1_gen_match', 'sync': 'gen_match_1'}
vars['Z_ee_l2_gen_match']  = {'std': 'Z_ee_l2_gen_match', 'sync': 'gen_match_2'}

vars['Z_mm_l1_gen_match']  = {'std': 'Z_mm_l1_gen_match', 'sync': 'gen_match_1'}
vars['Z_mm_l2_gen_match']  = {'std': 'Z_mm_l2_gen_match', 'sync': 'gen_match_2'}

vars['H_et_l1_gen_match']  = {'std': 'H_et_l1_gen_match', 'sync': 'gen_match_3'}
vars['H_et_l2_gen_match']  = {'std': 'H_et_l2_gen_match', 'sync': 'gen_match_4'}

vars['H_em_l1_gen_match']  = {'std': 'H_em_l1_gen_match', 'sync': 'gen_match_3'}
vars['H_em_l2_gen_match']  = {'std': 'H_em_l2_gen_match', 'sync': 'gen_match_4'}

vars['H_tt_l1_gen_match']  = {'std': 'H_tt_l1_gen_match', 'sync': 'gen_match_3'}
vars['H_tt_l2_gen_match']  = {'std': 'H_tt_l2_gen_match', 'sync': 'gen_match_4'}

vars['H_mt_l1_gen_match']  = {'std': 'H_mt_l1_gen_match', 'sync': 'gen_match_3'}
vars['H_mt_l2_gen_match']  = {'std': 'H_mt_l2_gen_match', 'sync': 'gen_match_4'}

vars['Z_ee_l1_mass'] = {'std': 'Z_ee_l1_mass', 'sync': 'm_1'}
vars['Z_ee_l2_mass'] = {'std': 'Z_ee_l2_mass', 'sync': 'm_2'}


vars['H_mt_l1_mass'] = {'std': 'H_mt_l1_mass', 'sync': 'm_3'}
vars['H_mt_l2_mass'] = {'std': 'H_mt_l2_mass', 'sync': 'm_4'}

vars['H_tt_l1_mass'] = {'std': 'H_tt_l1_mass', 'sync': 'm_3'}
vars['H_tt_l2_mass'] = {'std': 'H_tt_l2_mass', 'sync': 'm_4'}

vars['H_et_l1_mass'] = {'std': 'H_et_l1_mass', 'sync': 'm_3'}
vars['H_et_l2_mass'] = {'std': 'H_et_l2_mass', 'sync': 'm_4'}

vars['H_em_l1_mass'] = {'std': 'H_em_l1_mass', 'sync': 'm_3'}
vars['H_em_l2_mass'] = {'std': 'H_em_l2_mass', 'sync': 'm_4'}


vars['H_tt_l1_unscaledPt'] = {'std': 'H_tt_l1_unscaledPt', 'sync': 'pt_3'}
vars['H_tt_l2_unscaledPt'] = {'std': 'H_tt_l2_unscaledPt', 'sync': 'pt_4'}

vars['H_mt_l1_unscaledPt'] = {'std': 'H_mt_l1_unscaledPt', 'sync': 'pt_3'}
vars['H_mt_l2_unscaledPt'] = {'std': 'H_mt_l2_unscaledPt', 'sync': 'pt_4'}

vars['H_et_l1_unscaledPt'] = {'std': 'H_et_l1_unscaledPt', 'sync': 'pt_3'}
vars['H_et_l2_unscaledPt'] = {'std': 'H_et_l2_unscaledPt', 'sync': 'pt_4'}

vars['H_em_l1_unscaledPt'] = {'std': 'H_em_l1_unscaledPt', 'sync': 'pt_3'}
vars['H_em_l2_unscaledPt'] = {'std': 'H_em_l2_unscaledPt', 'sync': 'pt_4'}

vars['H_tt_l1_TES_down_pt'] = {'std': 'H_tt_l1_TES_down_pt', 'sync': 'pt_TES_down_3'}
vars['H_tt_l2_TES_down_pt'] = {'std': 'H_tt_l2_TES_down_pt', 'sync': 'pt_TES_down_4'}

vars['H_mt_l1_TES_down_pt'] = {'std': 'H_mt_l1_TES_down_pt', 'sync': 'pt_TES_down_3'}
vars['H_mt_l2_TES_down_pt'] = {'std': 'H_mt_l2_TES_down_pt', 'sync': 'pt_TES_down_4'}

vars['H_et_l1_TES_down_pt'] = {'std': 'H_et_l1_TES_down_pt', 'sync': 'pt_TES_down_3'}
vars['H_et_l2_TES_down_pt'] = {'std': 'H_et_l2_TES_down_pt', 'sync': 'pt_TES_down_4'}

vars['H_em_l1_TES_down_pt'] = {'std': 'H_em_l1_TES_down_pt', 'sync': 'pt_TES_down_3'}
vars['H_em_l2_TES_down_pt'] = {'std': 'H_em_l2_TES_down_pt', 'sync': 'pt_TES_down_4'}


vars['H_tt_l1_TES_up_pt'] = {'std': 'H_tt_l1_TES_up_pt', 'sync': 'pt_TES_up_3'}
vars['H_tt_l2_TES_up_pt'] = {'std': 'H_tt_l2_TES_up_pt', 'sync': 'pt_TES_up_4'}

vars['H_mt_l1_TES_up_pt'] = {'std': 'H_mt_l1_TES_up_pt', 'sync': 'pt_TES_up_3'}
vars['H_mt_l2_TES_up_pt'] = {'std': 'H_mt_l2_TES_up_pt', 'sync': 'pt_TES_up_4'}

vars['H_et_l1_TES_up_pt'] = {'std': 'H_et_l1_TES_up_pt', 'sync': 'pt_TES_up_3'}
vars['H_et_l2_TES_up_pt'] = {'std': 'H_et_l2_TES_up_pt', 'sync': 'pt_TES_up_4'}

vars['H_em_l1_TES_up_pt'] = {'std': 'H_em_l1_TES_up_pt', 'sync': 'pt_TES_up_3'}
vars['H_em_l2_TES_up_pt'] = {'std': 'H_em_l2_TES_up_pt', 'sync': 'pt_TES_up_4'}
# MM

vars['Zboson_mm_pt'] = {'std': 'Zboson_mm_pt', 'sync': 'Z_Pt'}
vars['Zboson_mm_mass']= {'std': 'Zboson_mm_mass', 'sync': 'm_vis'}
vars['Zboson_mm_DR'] = {'std': 'Zboson_mm_DR', 'sync': 'Z_DR'}

vars['Z_mm_l1_pt']  = {'std': 'Z_mm_l1_pt', 'sync': 'pt_1'}
vars['Z_mm_l1_phi']  = {'std': 'Z_mm_l1_phi', 'sync': 'phi_1'}
vars['Z_mm_l1_eta']  = {'std': 'Z_mm_l1_eta', 'sync': 'eta_1'}
vars['Z_mm_l1_reliso05']  = {'std': 'Z_mm_l1_reliso05', 'sync': 'iso_1'}

vars['Z_mm_l2_pt']  = {'std': 'Z_mm_l2_pt', 'sync': 'pt_2'}
vars['Z_mm_l2_phi']  = {'std': 'Z_mm_l2_phi', 'sync': 'phi_2'}
vars['Z_mm_l2_eta']  = {'std': 'Z_mm_l2_eta', 'sync': 'eta_2'}
vars['Z_mm_l2_reliso05']  = {'std': 'Z_mm_l2_reliso05', 'sync': 'iso_2'}


vars['Zboson_mm_eta'] = {'std': 'Zboson_mm_eta', 'sync': 'Z_Eta'}
vars['Zboson_mm_phi'] = {'std': 'Zboson_mm_phi', 'sync': 'Z_Phi'}

vars['Z_mm_l1_mass'] = {'std': 'Z_mm_l1_mass', 'sync': 'm_1'}
vars['Z_mm_l2_mass'] = {'std': 'Z_mm_l2_mass', 'sync': 'm_2'}


#MT

vars['Hboson_mt_pt'] = {'std': 'Hboson_mt_pt', 'sync': 'H_Pt'}
vars['Hboson_mt_mass']= {'std': 'Hboson_mt_mass', 'sync': 'H_vis'}
vars['Hboson_mt_DR'] = {'std': 'Hboson_mt_DR', 'sync': 'H_DR'}
vars['Hboson_mt_eta'] = {'std': 'Hboson_mt_eta', 'sync': 'H_Eta'}
vars['Hboson_mt_phi'] = {'std': 'Hboson_mt_phi', 'sync': 'H_Phi'}

vars['Aboson_mt_mass'] = {'std': 'Aboson_mt_mass', 'sync': 'Mass'}
vars['Aboson_mt_eta'] = {'std': 'Aboson_mt_eta', 'sync': 'A_Eta'}
vars['Aboson_mt_phi'] = {'std': 'Aboson_mt_phi', 'sync': 'A_Phi'}
vars['Aboson_mt_pt'] = {'std': 'Aboson_mt_pt', 'sync': 'A_Pt'}


vars['H_mt_l1_pt']  = {'std': 'H_mt_l1_pt', 'sync': 'shiftedPt_3'}
vars['H_mt_l1_phi']  = {'std': 'H_mt_l1_phi', 'sync': 'phi_3'}
vars['H_mt_l1_eta']  = {'std': 'H_mt_l1_eta', 'sync': 'eta_3'}
vars['H_mt_l1_reliso05']  = {'std': 'H_mt_l1_reliso05', 'sync': 'iso_3'}

vars['H_mt_l2_pt']  = {'std': 'H_mt_l2_pt', 'sync': 'shiftedPt_4'}
vars['H_mt_l2_phi']  = {'std': 'H_mt_l2_phi', 'sync': 'phi_4'}
vars['H_mt_l2_eta']  = {'std': 'H_mt_l2_eta', 'sync': 'eta_4'}
vars['H_mt_l2_byIsolationMVArun2v1DBoldDMwLTraw']  = {'std': 'H_mt_l2_byIsolationMVArun2v1DBoldDMwLTraw', 'sync': 'iso_4'}



#ET
vars['Hboson_et_eta'] = {'std': 'Hboson_et_eta', 'sync': 'H_Eta'}
vars['Hboson_et_phi'] = {'std': 'Hboson_et_phi', 'sync': 'H_Phi'}

vars['Hboson_et_pt'] = {'std': 'Hboson_et_pt', 'sync': 'H_Pt'}
vars['Hboson_et_mass']= {'std': 'Hboson_et_mass', 'sync': 'H_vis'}
vars['Hboson_et_DR'] = {'std': 'Hboson_et_DR', 'sync': 'H_DR'}

vars['Aboson_et_mass'] = {'std': 'Aboson_et_mass', 'sync': 'Mass'}
vars['Aboson_et_eta'] = {'std': 'Aboson_et_eta', 'sync': 'A_Eta'}
vars['Aboson_et_phi'] = {'std': 'Aboson_et_phi', 'sync': 'A_Phi'}
vars['Aboson_et_pt'] = {'std': 'Aboson_et_pt', 'sync': 'A_Pt'}


vars['H_et_l1_pt']  = {'std': 'H_et_l1_pt', 'sync': 'shiftedPt_3'}
vars['H_et_l1_phi']  = {'std': 'H_et_l1_phi', 'sync': 'phi_3'}
vars['H_et_l1_eta']  = {'std': 'H_et_l1_eta', 'sync': 'eta_3'}
vars['H_et_l1_reliso05']  = {'std': 'H_et_l1_reliso05', 'sync': 'iso_3'}
vars['H_et_l1_eid_spring16MVAraw']  = {'std': 'H_et_l1_eid_spring16MVAraw', 'sync': 'IdRawMva_3'}


vars['H_et_l2_pt']  = {'std': 'H_et_l2_pt', 'sync': 'shiftedPt_4'}
vars['H_et_l2_phi']  = {'std': 'H_et_l2_phi', 'sync': 'phi_4'}
vars['H_et_l2_eta']  = {'std': 'H_et_l2_eta', 'sync': 'eta_4'}
vars['H_et_l2_byIsolationMVArun2v1DBoldDMwLTraw']  = {'std': 'H_et_l2_byIsolationMVArun2v1DBoldDMwLTraw', 'sync': 'iso_4'}

# TT

vars['Hboson_tt_eta'] = {'std': 'Hboson_tt_eta', 'sync': 'H_Eta'}
vars['Hboson_tt_phi'] = {'std': 'Hboson_tt_phi', 'sync': 'H_Phi'}


vars['Hboson_tt_pt'] = {'std': 'Hboson_tt_pt', 'sync': 'H_Pt'}
vars['Hboson_tt_mass']= {'std': 'Hboson_tt_mass', 'sync': 'H_vis'}
vars['Hboson_tt_DR'] = {'std': 'Hboson_tt_DR', 'sync': 'H_DR'}

vars['Aboson_tt_mass'] = {'std': 'Aboson_tt_mass', 'sync': 'Mass'}
vars['Aboson_tt_eta'] = {'std': 'Aboson_tt_eta', 'sync': 'A_Eta'}
vars['Aboson_tt_phi'] = {'std': 'Aboson_tt_phi', 'sync': 'A_Phi'}
vars['Aboson_tt_pt'] = {'std': 'Aboson_tt_pt', 'sync': 'A_Pt'}


vars['H_tt_l1_pt']  = {'std': 'H_tt_l1_pt', 'sync': 'shiftedPt_3'}
vars['H_tt_l1_phi']  = {'std': 'H_tt_l1_phi', 'sync': 'phi_3'}
vars['H_tt_l1_eta']  = {'std': 'H_tt_l1_eta', 'sync': 'eta_3'}
vars['H_tt_l1_byIsolationMVArun2v1DBoldDMwLTraw']  = {'std': 'H_tt_l1_byIsolationMVArun2v1DBoldDMwLTraw', 'sync': 'iso_3'}

vars['H_tt_l2_pt']  = {'std': 'H_tt_l2_pt', 'sync': 'shiftedPt_4'}
vars['H_tt_l2_phi']  = {'std': 'H_tt_l2_phi', 'sync': 'phi_4'}
vars['H_tt_l2_eta']  = {'std': 'H_tt_l2_eta', 'sync': 'eta_4'}
vars['H_tt_l2_byIsolationMVArun2v1DBoldDMwLTraw']  = {'std': 'H_tt_l2_byIsolationMVArun2v1DBoldDMwLTraw', 'sync': 'iso_4'}

#EM
vars['Hboson_em_eta'] = {'std': 'Hboson_em_eta', 'sync': 'H_Eta'}
vars['Hboson_em_phi'] = {'std': 'Hboson_em_phi', 'sync': 'H_Phi'}

vars['Hboson_em_pt'] = {'std': 'Hboson_em_pt', 'sync': 'H_Pt'}
vars['Hboson_em_mass']= {'std': 'Hboson_em_mass', 'sync': 'H_vis'}
vars['Hboson_em_DR'] = {'std': 'Hboson_em_DR', 'sync': 'H_DR'}

vars['Aboson_em_mass'] = {'std': 'Aboson_em_mass', 'sync': 'Mass'}
vars['Aboson_em_eta'] = {'std': 'Aboson_em_eta', 'sync': 'A_Eta'}
vars['Aboson_em_phi'] = {'std': 'Aboson_em_phi', 'sync': 'A_Phi'}
vars['Aboson_em_pt'] = {'std': 'Aboson_em_pt', 'sync': 'A_Pt'}

vars['H_em_l1_pt']  = {'std': 'H_em_l1_pt', 'sync': 'shiftedPt_3'}
vars['H_em_l1_phi']  = {'std': 'H_em_l1_phi', 'sync': 'phi_3'}
vars['H_em_l1_eta']  = {'std': 'H_em_l1_eta', 'sync': 'eta_3'}
vars['H_em_l1_reliso05']  = {'std': 'H_em_l1_reliso05', 'sync': 'iso_3'}

vars['H_em_l2_pt']  = {'std': 'H_em_l2_pt', 'sync': 'shiftedPt_4'}
vars['H_em_l2_phi']  = {'std': 'H_em_l2_phi', 'sync': 'phi_4'}
vars['H_em_l2_eta']  = {'std': 'H_em_l2_eta', 'sync': 'eta_4'}
vars['H_em_l2_reliso05']  = {'std': 'H_em_l2_reliso05', 'sync': 'iso_4'}
vars['H_em_l1_eid_spring16MVAraw']  = {'std': 'H_em_l1_eid_spring16MVAraw', 'sync': 'IdRawMva_3'}


# Generator info
vars['geninfo_tt'] = {'std': 'geninfo_tt', 'sync': 'isZtt'}
vars['geninfo_mt'] = {'std': 'geninfo_mt', 'sync': 'isZmt'}
vars['geninfo_et'] = {'std': 'geninfo_et', 'sync': 'isZet'}
vars['geninfo_ee'] = {'std': 'geninfo_ee', 'sync': 'isZee'}
vars['geninfo_mm'] = {'std': 'geninfo_mm', 'sync': 'isZmm'}
vars['geninfo_em'] = {'std': 'geninfo_em', 'sync': 'isZem'}
vars['geninfo_EE'] = {'std': 'geninfo_EE', 'sync': 'isZEE'}
vars['geninfo_MM'] = {'std': 'geninfo_MM', 'sync': 'isZMM'}
vars['geninfo_LL'] = {'std': 'geninfo_LL', 'sync': 'isZLL'}
vars['geninfo_fakeid'] = {'std': 'geninfo_fakeid', 'sync': 'isFake'}

# Weights
vars['weight'] = {'std': 'weight', 'sync': 'weight'}
vars['weight_vertex'] = {'std': 'weight_vertex', 'sync': 'puweight'}

# PileUp
vars['geninfo_nup'] = {'geninfo_nup': 'NUP', 'sync': 'NUP'}
vars['geninfo_invmass'] = {'geninfo_invmass': 'geninvmass', 'sync': 'geninvmass'}
vars['n_vertices'] = {'std': 'n_vertices', 'sync': 'npv'}
vars['npu'] = {'std': 'npu', 'sync': 'npu'}
vars['nPU'] = {'std': 'nPU', 'sync': 'npu'}
vars['rho'] = {'std': 'rho', 'sync': 'rho'}

# Lepton vetoes
vars['veto_dilepton'] = {'std':'veto_dilepton', 'sync':'dilepton_veto'}
vars['veto_thirdlepton'] = {'std':'veto_thirdlepton', 'sync':'extramuon_veto'}
vars['veto_otherlepton'] = {'std':'veto_otherlepton', 'sync':'extraelec_veto'}


# Leg 1 (tau, mu, ele)
vars['l1_pt'] = {'std': 'l1_pt', 'sync': 'pt_1'}
vars['l1_phi'] = {'std': 'l1_phi', 'sync': 'phi_1'}
vars['l1_eta'] = {'std': 'l1_eta', 'sync': 'eta_1'}
vars['l1_mass'] = {'std': 'l1_mass', 'sync': 'massa_1'}
vars['l1_charge'] = {'std': 'l1_charge', 'sync': 'q_1'}
vars['l1_dxy'] = {'std': 'l1_dxy', 'sync': 'd0_1'}
vars['l1_dz'] = {'std': 'l1_dz', 'sync': 'dZ_1'}
vars['mt'] = {'std': 'mt', 'sync': 'mt_1'}
vars['puppimet_mt1'] = {'std': 'puppimet_mt1', 'sync': 'puppimt_1'}
vars['pfmet_mt1'] = {'std': 'pfmet_mt1', 'sync': 'pfmt_1'}
vars['l1_reliso05'] = {'std': 'l1_reliso05', 'sync': 'iso_1'}
vars['l1_muonid_loose'] = {'std': 'l1_muonid_loose', 'sync': 'id_m_loose_1'}
vars['l1_muonid_medium'] = {'std': 'l1_muonid_medium', 'sync': 'id_m_medium_1'}
vars['l1_muonid_tight'] = {'std': 'l1_muonid_tight', 'sync': 'id_m_tight_1'}
vars['l1_muonid_tightnovtx'] = {'std': 'l1_muonid_tightnovtx', 'sync': 'id_m_tightnovtx_1'}
vars['l1_muonid_highpt'] = {'std': 'l1_muonid_highpt', 'sync': 'id_m_highpt_1'}
vars['l1_eid_nontrigmva_loose'] = {'std': 'l1_eid_nontrigmva_loose', 'sync': 'id_e_mva_nt_loose_1'}
vars['l1_eid_nontrigmva_tight'] = {'std': 'l1_eid_nontrigmva_tight', 'sync': 'id_e_mva_nt_tight_1'}
vars['l1_eid_veto'] = {'std': 'l1_eid_veto', 'sync': 'id_e_cut_veto_1'}
vars['l1_eid_loose'] = {'std': 'l1_eid_loose', 'sync': 'id_e_cut_loose_1'}
vars['l1_eid_medium'] = {'std': 'l1_eid_medium', 'sync': 'id_e_cut_medium_1'}
vars['l1_eid_tight'] = {'std': 'l1_eid_tight', 'sync': 'id_e_cut_tight_1'}
vars['l1_weight_trigger'] = {'std': 'l1_weight_trigger', 'sync': 'trigweight_1'}
vars['l1_weight_tracking'] = {'std': 'l1_weight_tracking', 'sync': 'trackingweight_1'}
vars['l1_weight_idiso'] = {'std': 'l1_weight_idiso', 'sync': 'idisoweight_1'}
vars['l1_againstElectronLooseMVA5'] = {'std': 'l1_againstElectronLooseMVA5', 'sync': 'againstElectronLooseMVA5_1'}
vars['l1_againstElectronMediumMVA5'] = {'std': 'l1_againstElectronMediumMVA5', 'sync': 'againstElectronMediumMVA5_1'}
vars['l1_againstElectronTightMVA5'] = {'std': 'l1_againstElectronTightMVA5', 'sync': 'againstElectronTightMVA5_1'}
vars['l1_againstElectronVLooseMVA5'] = {'std': 'l1_againstElectronVLooseMVA5', 'sync': 'againstElectronVLooseMVA5_1'}
vars['l1_againstElectronVTightMVA5'] = {'std': 'l1_againstElectronVTightMVA5', 'sync': 'againstElectronVTightMVA5_1'}
vars['l1_againstMuonLoose3'] = {'std': 'l1_againstMuonLoose3', 'sync': 'againstMuonLoose3_1'}
vars['l1_againstMuonTight3'] = {'std': 'l1_againstMuonTight3', 'sync': 'againstMuonTight3_1'}
vars['l1_byCombinedIsolationDeltaBetaCorrRaw3Hits'] = {'std': 'l1_byCombinedIsolationDeltaBetaCorrRaw3Hits', 'sync': 'byCombinedIsolationDeltaBetaCorrRaw3Hits_1'}
vars['l1_byIsolationMVArun2v1newDMwoLTraw'] = {'std': 'l1_byIsolationMVArun2v1newDMwoLTraw', 'sync': 'byIsolationMVArun2v1newDMwoLTraw_1'}
vars['l1_byIsolationMVArun2v1oldDMwoLTraw'] = {'std': 'l1_byIsolationMVArun2v1oldDMwoLTraw', 'sync': 'byIsolationMVArun2v1oldDMwoLTraw_1'}
vars['l1_byIsolationMVArun2v1newDMwLTraw'] = {'std': 'l1_byIsolationMVArun2v1newDMwLTraw', 'sync': 'byIsolationMVArun2v1newDMwLTraw_1'}
vars['l1_byIsolationMVArun2v1oldDMwLTraw'] = {'std': 'l1_byIsolationMVArun2v1oldDMwLTraw', 'sync': 'byIsolationMVArun2v1oldDMwLTraw_1'}
vars['l1_chargedIsoPtSum'] = {'std': 'l1_chargedIsoPtSum', 'sync': 'chargedIsoPtSum_1'}
vars['l1_decayModeFinding'] = {'std': 'l1_decayModeFinding', 'sync': 'decayModeFindingOldDMs_1'}
vars['l1_decayModeFindingNewDMs'] = {'std': 'l1_decayModeFindingNewDMs', 'sync': 'decayModeFindingNewDMs_1'}
vars['l1_neutralIsoPtSum'] = {'std': 'l1_neutralIsoPtSum', 'sync': 'neutralIsoPtSum_1'}
vars['l1_puCorrPtSum'] = {'std': 'l1_puCorrPtSum', 'sync': 'puCorrPtSum_1'}
vars['l1_gen_match'] = {'std': 'l1_gen_match', 'sync': 'gen_match_1'}
vars['l1_byTightIsolationMVArun2v1DBoldDMwLT'] = {'std': 'l1_byTightIsolationMVArun2v1DBoldDMwLT', 'sync': 'byTightIsolationMVArun2v1DBoldDMwLT_1'}# For sync check

# Leg 2 (tau, mu, ele)
vars['l2_pt'] = {'std': 'l2_pt', 'sync': 'pt_2'}
vars['l2_phi'] = {'std': 'l2_phi', 'sync': 'phi_2'}
vars['l2_eta'] = {'std': 'l2_eta', 'sync': 'eta_2'}
vars['l2_mass'] = {'std': 'l2_mass', 'sync': 'm_2'}
vars['l2_charge'] = {'std': 'l2_charge', 'sync': 'q_2'}
vars['l2_dxy'] = {'std': 'l2_dxy', 'sync': 'd0_2'}
vars['l2_dz'] = {'std': 'l2_dz', 'sync': 'dZ_2'}
vars['mt_leg2'] = {'std': 'mt_leg2', 'sync': 'mt_2'}
vars['puppimet_mt2'] = {'std': 'puppimet_mt2', 'sync': 'puppimt_2'}
vars['pfmet_mt2'] = {'std': 'pfmet_mt2', 'sync': 'pfmt_2'}
vars['l2_reliso05'] = {'std': 'l2_reliso05', 'sync': 'iso_2'}
vars['l2_muonid_loose'] = {'std': 'l2_muonid_loose', 'sync': 'id_m_loose_2'}
vars['l2_muonid_medium'] = {'std': 'l2_muonid_medium', 'sync': 'id_m_medium_2'}
vars['l2_muonid_tight'] = {'std': 'l2_muonid_tight', 'sync': 'id_m_tight_2'}
vars['l2_muonid_tightnovtx'] = {'std': 'l2_muonid_tightnovtx', 'sync': 'id_m_tightnovtx_2'}
vars['l2_muonid_highpt'] = {'std': 'l2_muonid_highpt', 'sync': 'id_m_highpt_2'}
vars['l2_eid_nontrigmva_loose'] = {'std': 'l2_eid_nontrigmva_loose', 'sync': 'id_e_mva_nt_loose_2'}
vars['l2_eid_nontrigmva_tight'] = {'std': 'l2_eid_nontrigmva_tight', 'sync': 'id_e_mva_nt_loose_2'}
vars['l2_eid_veto'] = {'std': 'l2_eid_veto', 'sync': 'id_e_cut_veto_2'}
vars['l2_eid_loose'] = {'std': 'l2_eid_loose', 'sync': 'id_e_cut_loose_2'}
vars['l2_eid_medium'] = {'std': 'l2_eid_medium', 'sync': 'id_e_cut_medium_2'}
vars['l2_eid_tight'] = {'std': 'l2_eid_tight', 'sync': 'id_e_cut_tight_2'}
vars['l2_weight_trigger'] = {'std': 'l2_weight_trigger', 'sync': 'trigweight_2'}
vars['l2_weight_tracking'] = {'std': 'l2_weight_tracking', 'sync': 'trackingweight_2'}
vars['l2_againstElectronLooseMVA5'] = {'std': 'l2_againstElectronLooseMVA5', 'sync': 'againstElectronLooseMVA5_2'}
vars['l2_againstElectronMediumMVA5'] = {'std': 'l2_againstElectronMediumMVA5', 'sync': 'againstElectronMediumMVA5_2'}
vars['l2_againstElectronTightMVA5'] = {'std': 'l2_againstElectronTightMVA5', 'sync': 'againstElectronTightMVA5_2'}
vars['l2_againstElectronVLooseMVA5'] = {'std': 'l2_againstElectronVLooseMVA5', 'sync': 'againstElectronVLooseMVA5_2'}
vars['l2_againstElectronVTightMVA5'] = {'std': 'l2_againstElectronVTightMVA5', 'sync': 'againstElectronVTightMVA5_2'}
vars['l2_againstMuonLoose3'] = {'std': 'l2_againstMuonLoose3', 'sync': 'againstMuonLoose3_2'}
vars['l2_againstMuonTight3'] = {'std': 'l2_againstMuonTight3', 'sync': 'againstMuonTight3_2'}
vars['l2_byCombinedIsolationDeltaBetaCorrRaw3Hits'] = {'std': 'l2_byCombinedIsolationDeltaBetaCorrRaw3Hits', 'sync': 'byCombinedIsolationDeltaBetaCorrRaw3Hits_2'}
vars['l2_byIsolationMVArun2v1newDMwoLTraw'] = {'std': 'l2_byIsolationMVArun2v1newDMwoLTraw', 'sync': 'byIsolationMVArun2v1newDMwoLTraw_2'}
vars['l2_byIsolationMVArun2v1oldDMwoLTraw'] = {'std': 'l2_byIsolationMVArun2v1oldDMwoLTraw', 'sync': 'byIsolationMVArun2v1oldDMwoLTraw_2'}
vars['l2_byIsolationMVArun2v1newDMwLTraw'] = {'std': 'l2_byIsolationMVArun2v1newDMwLTraw', 'sync': 'byIsolationMVArun2v1newDMwLTraw_2'}
vars['l2_byIsolationMVArun2v1oldDMwLTraw'] = {'std': 'l2_byIsolationMVArun2v1oldDMwLTraw', 'sync': 'byIsolationMVArun2v1oldDMwLTraw_2'}
vars['l2_chargedIsoPtSum'] = {'std': 'l2_chargedIsoPtSum', 'sync': 'chargedIsoPtSum_2'}
vars['l2_decayModeFinding'] = {'std': 'l2_decayModeFinding', 'sync': 'decayModeFindingOldDMs_2'}
vars['l2_decayModeFindingNewDMs'] = {'std': 'l2_decayModeFindingNewDMs', 'sync': 'decayModeFindingNewDMs_2'}
vars['l2_neutralIsoPtSum'] = {'std': 'l2_neutralIsoPtSum', 'sync': 'neutralIsoPtSum_2'}
vars['l2_puCorrPtSum'] = {'std': 'l2_puCorrPtSum', 'sync': 'puCorrPtSum_2'}
vars['l2_gen_match'] = {'std': 'l2_gen_match', 'sync': 'gen_match_2'}
vars['l2_byTightIsolationMVArun2v1DBoldDMwLT'] = {'std': 'l2_byTightIsolationMVArun2v1DBoldDMwLT', 'sync': 'mva_olddm_tight_2'}# For sync check
vars['l2_byMediumIsolationMVArun2v1DBoldDMwLT'] = {'std': 'l2_byMediumIsolationMVArun2v1DBoldDMwLT', 'sync': 'mva_olddm_medium_2'}# For sync check

# di-tau pair
vars['pthiggs'] = {'std': 'pthiggs', 'sync': 'pt_tt'}
vars['visMass'] = {'std': 'visMass', 'sync': 'm_vis_tt'}
vars['mt_total'] = {'std': 'mt_total', 'sync': 'mt_tot'}
vars['mvis'] = {'std': 'mvis', 'sync': 'm_vis_tt2'}
vars['svfit_mass'] = {'std': 'svfit_mass', 'sync': 'm_sv'}
vars['svfit_transverse_mass'] = {'std':'svfit_transverse_mass', 'sync':'mt_sv'}
vars['svfit_pt'] = {'std': 'svfit_pt', 'sync': 'pt_sv'}
vars['svfit_eta'] = {'std': 'svfit_eta', 'sync': 'eta_sv'}
vars['svfit_phi'] = {'std': 'svfit_phi', 'sync': 'phi_sv'}
vars['svfit_met'] = {'std': 'svfit_met', 'sync': 'met_sv'}

# MET
vars['met_pt'] = {'std': 'met_pt', 'sync': 'met'}
#vars['pfmet_pt'] = {'std': 'pfmet_pt', 'sync': 'met'}
#vars['pfmet_phi'] = {'std': 'pfmet_phi', 'sync': 'metphi'}
#vars['met_ptmva'] = {'std': 'met_ptmva', 'sync': 'mvamet'}
#vars['met_phimva'] = {'std': 'met_phimva', 'sync': 'mvametphimva'}
#vars['puppimet_pt'] = {'std': 'puppimet_pt', 'sync': 'puppimet'}
#vars['puppimet_phi'] = {'std': 'puppimet_phi', 'sync': 'puppimetphi'}
#vars['pzeta_vis'] = {'std': 'pzeta_vis', 'sync': 'pzetavis'}
#vars['pzeta_met'] = {'std': 'pzeta_met', 'sync': 'pzetamiss'}

vars['met_cov00'] = {'std': 'met_cov00', 'sync': 'mvacov00'}
vars['met_cov01'] = {'std': 'met_cov01', 'sync': 'mvacov01'}
vars['met_cov10'] = {'std': 'met_cov10', 'sync': 'mvacov10'}
vars['met_cov11'] = {'std': 'met_cov11', 'sync': 'mvacov11'}

# VBF
vars['ditau_mjj'] = {'std': 'ditau_mjj', 'sync': 'mjj'}
vars['ditau_deta'] = {'std': 'ditau_deta', 'sync': 'jdeta'}
vars['ditau_nCentral'] = {'std': 'ditau_n_central', 'sync': 'njetingap'}
vars['ditau_nCentral'] = {'std': 'ditau_n_central20', 'sync': 'njetingap20'}
vars['ditau_mva'] = {'std': 'ditau_mva', 'sync': 'mva'}

vars['ditau_jdphi'] = {'std': 'ditau_jdphi', 'sync': 'jdphi'}
vars['ditau_dijetpt'] = {'std': 'ditau_dijetpt', 'sync': 'dijetpt'}
vars['ditau_dijetphi'] = {'std': 'ditau_dijetphi', 'sync': 'dijetphi'}
vars['ditau_hdijetphi'] = {'std': 'ditau_hdijetphi', 'sync': 'hdijetphi'}
vars['ditau_visjeteta'] = {'std': 'ditau_visjeteta', 'sync': 'visjeteta'}
vars['ditau_ptvis'] = {'std': 'ditau_ptvis', 'sync': 'ptvis'}

# N Jets
vars['n_jets'] = {'std': 'n_jets', 'sync': 'jetVeto30'}
vars['n_jets_20'] = {'std': 'n_jets_20', 'sync': 'njetspt20'}
vars['n_bjets'] = {'std': 'n_bjets', 'sync': 'bjetCISVVeto20Medium_full'}
vars['n_bjets_tt'] = {'std': 'n_bjets_tt', 'sync': 'bjetCISVVeto20Medium_tt'}
vars['n_bjets_et'] = {'std': 'n_bjets_et', 'sync': 'bjetCISVVeto20Medium_et'}
vars['n_bjets_mt'] = {'std': 'n_bjets_mt', 'sync': 'bjetCISVVeto20Medium_mt'}
vars['n_bjets_em'] = {'std': 'n_bjets_em', 'sync': 'bjetCISVVeto20Medium_em'}


# Jet 1
vars['jet1_pt'] = {'std': 'jet1_pt', 'sync': 'jpt_1'}
vars['jet1_eta'] = {'std': 'jet1_eta', 'sync': 'jeta_1'}
vars['jet1_phi'] = {'std': 'jet1_phi', 'sync': 'jphi_1'}
vars['jet1_rawfactor'] = {'std': 'jet1_rawfactor', 'sync': 'jrawf_1'}
vars['jet1_mva_pu'] = {'std': 'jet1_mva_pu', 'sync': 'jmva_1'}
vars['jet1_id_loose'] = {'std': 'jet1_id_loose', 'sync': 'jpfid_1'}
vars['jet1_id_pu'] = {'std': 'jet1_id_pu', 'sync': 'jpuid_1'}
vars['jet1_csv'] = {'std': 'jet1_csv', 'sync': 'jcsv_1'}

# Jet 2
vars['jet2_pt'] = {'std': 'jet2_pt', 'sync': 'jpt_2'}
vars['jet2_eta'] = {'std': 'jet2_eta', 'sync': 'jeta_2'}
vars['jet2_phi'] = {'std': 'jet2_phi', 'sync': 'jphi_2'}
vars['jet2_rawfactor'] = {'std': 'jet2_rawfactor', 'sync': 'jrawf_2'}
vars['jet2_mva_pu'] = {'std': 'jet2_mva_pu', 'sync': 'jmva_2'}
vars['jet2_id_loose'] = {'std': 'jet2_id_loose', 'sync': 'jpfid_2'}
vars['jet2_id_pu'] = {'std': 'jet2_id_pu', 'sync': 'jpuid_2'}
vars['jet2_csv'] = {'std': 'jet2_csv', 'sync': 'jcsv_2'}

# bJet 1
vars['bjet1_pt'] = {'std': 'bjet1_pt', 'sync': 'bpt_1'}
vars['bjet1_eta'] = {'std': 'bjet1_eta', 'sync': 'beta_1'}
vars['bjet1_phi'] = {'std': 'bjet1_phi', 'sync': 'bphi_1'}
vars['bjet1_rawfactor'] = {'std': 'bjet1_rawfactor', 'sync': 'brawf_1'}
vars['bjet1_mva_pu'] = {'std': 'bjet1_mva_pu', 'sync': 'bmva_1'}
vars['bjet1_id_loose'] = {'std': 'bjet1_id_loose', 'sync': 'bpfid_1'}
vars['bjet1_id_pu'] = {'std': 'bjet1_id_pu', 'sync': 'bpuid_1'}
vars['bjet1_csv'] = {'std': 'bjet1_csv', 'sync': 'bcsv_1'}

# bJet 2
vars['bjet2_pt'] = {'std': 'bjet2_pt', 'sync': 'bpt_2'}
vars['bjet2_eta'] = {'std': 'bjet2_eta', 'sync': 'beta_2'}
vars['bjet2_phi'] = {'std': 'bjet2_phi', 'sync': 'bphi_2'}
vars['bjet2_rawfactor'] = {'std': 'bjet2_rawfactor', 'sync': 'brawf_2'}
vars['bjet2_mva_pu'] = {'std': 'bjet2_mva_pu', 'sync': 'bmva_2'}
vars['bjet2_id_loose'] = {'std': 'bjet2_id_loose', 'sync': 'bpfid_2'}
vars['bjet2_id_pu'] = {'std': 'bjet2_id_pu', 'sync': 'bpuid_2'}
vars['bjet2_csv'] = {'std': 'bjet2_csv', 'sync': 'bcsv_2'}

# trigger names
vars['trigger_ditau35'] = {'std':'trigger_ditau35', 'sync':'trg_fired_doubletau'}
vars['trigger_ditau35_combiso'] = {'std':'trigger_ditau35_combiso', 'sync':'trg_fired_doubletau_combiso'}
vars['trigger_singletau140'] = {'std':'trigger_singletau140', 'sync':'trg_fired_singletau'}
vars['trigger_singletau120'] = {'std':'trigger_singletau120', 'sync':'trg_fired_singletau120'}

vars['trigger_matched_ditau35'] = {'std':'trigger_matched_ditau35', 'sync':'trg_doubletau'}
vars['trigger_matched_ditau35_combiso'] = {'std':'trigger_matched_ditau35_combiso', 'sync':'trg_doubletau_combiso'}
vars['trigger_matched_singletau140'] = {'std':'trigger_matched_singletau140', 'sync':'trg_singletau'}
vars['trigger_matched_singletau120'] = {'std':'trigger_matched_singletau120', 'sync':'trg_singletau120'}
