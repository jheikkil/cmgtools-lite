'''
A Class to interface with Electron Scale Factors:
https://twiki.cern.ch/twiki/bin/view/CMS/EgammaIDRecipesRun2#Electron_efficiencies_and_scale
Currently using WP90
Also, GSF SFs must be applied on top as well
'''

from CMGTools.TTHAnalysis.treeReAnalyzer import *
import re,os
import ROOT

class scaleFactors:
    def __init__(self,channel):
        from sys import argv
 
        self.chunk = argv[1].split("/")[-2]
        print self.chunk

        self.massFile = ROOT.TFile('gen_mass_SFs.root', 'r')
        self.mass350 = self.massFile.Get( 'mA350_SF' )
        self.mass400 = self.massFile.Get( 'mA400_SF' )


        #if wp == 'IdIso0p10' :
        #    self.elecSFFile = ROOT.TFile("%s/src/CMGTools/H2TauTau/data/Electron_IdIso_IsoLt0p1_eff.root" % os.environ['CMSSW_BASE'])
        #if wp == 'IdIso0p15' :
        self.elecSFFile = ROOT.TFile("%s/src/CMGTools/H2TauTau/data/Electron_IdIso_IsoLt0p15_eff.root" % os.environ['CMSSW_BASE'])
        self.mcBarrel = self.elecSFFile.Get( 'ZMassEtaLt1p48_MC' )
        self.mcMid = self.elecSFFile.Get( 'ZMassEta1p48to2p1_MC' )
        self.mcEndcap = self.elecSFFile.Get( 'ZMassEtaGt2p1_MC' )
        self.dataBarrel = self.elecSFFile.Get( 'ZMassEtaLt1p48_Data' )
        self.dataMid = self.elecSFFile.Get( 'ZMassEta1p48to2p1_Data' )
        self.dataEndcap = self.elecSFFile.Get( 'ZMassEtaGt2p1_Data' )


        #electrons
        self.f_el = ROOT.TFile("%s/src/CMGTools/TTHAnalysis/data/2016Electron_GSF_EG2D.root" % os.environ['CMSSW_BASE']) 
        self.gsfSF = self.f_el.Get( 'EGamma_SF2D' )
        ##TODO: ADD RIGHT FILES
        self.f_el_80 = ROOT.TFile("%s/src/CMGTools/TTHAnalysis/data/2016Electron_WP80_EG2D.root" % os.environ['CMSSW_BASE'])
        self.wp80SF = self.f_el_80.Get( 'EGamma_SF2D' )

        self.f_el_90 = ROOT.TFile("%s/src/CMGTools/TTHAnalysis/data/2016Electron_WP90_EG2D.root" % os.environ['CMSSW_BASE'])
        self.wp90SF = self.f_el_90.Get( 'EGamma_SF2D' )

        #muons
        self.bcdef = 0.76
        self.gh = 0.24
        #ID files
        self.muonIDFile1 = ROOT.TFile( "%s/src/CMGTools/TTHAnalysis/data/2016MuonEfficienciesAndSF_BCDEF_ID.root" % os.environ['CMSSW_BASE'])
        self.muonIDFile2 = ROOT.TFile( "%s/src/CMGTools/TTHAnalysis/data/2016MuonEfficienciesAndSF_GH_ID.root" % os.environ['CMSSW_BASE'])

        self.ID_L_eta1 = self.muonIDFile1.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_eta/eta_ratio' )
        self.ID_L_pt1 = self.muonIDFile1.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_pt/pt_ratio' )
        self.ID_L_vtx1 = self.muonIDFile1.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_vtx/tag_nVertices_ratio' )
        self.ID_M_eta1 = self.muonIDFile1.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_eta/eta_ratio' )
        self.ID_M_pt1 = self.muonIDFile1.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_pt/pt_ratio' )
        self.ID_M_vtx1 = self.muonIDFile1.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_vtx/tag_nVertices_ratio' )

        self.ID_L_eta2 = self.muonIDFile2.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_eta/eta_ratio' )
        self.ID_L_pt2 = self.muonIDFile2.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_pt/pt_ratio' )
        self.ID_L_vtx2 = self.muonIDFile2.Get( 'MC_NUM_LooseID_DEN_genTracks_PAR_vtx/tag_nVertices_ratio' )
        self.ID_M_eta2 = self.muonIDFile2.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_eta/eta_ratio' )
        self.ID_M_pt2 = self.muonIDFile2.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_pt/pt_ratio' )
        self.ID_M_vtx2 = self.muonIDFile2.Get( 'MC_NUM_MediumID_DEN_genTracks_PAR_vtx/tag_nVertices_ratio' )

        #iso files

        self.muonIsoFile1 = ROOT.TFile( "%s/src/CMGTools/TTHAnalysis/data/2016MuonEfficienciesAndSF_BCDEF_ISO.root" % os.environ['CMSSW_BASE'])
        self.muonIsoFile2 = ROOT.TFile( "%s/src/CMGTools/TTHAnalysis/data/2016MuonEfficienciesAndSF_GH_ISO.root" % os.environ['CMSSW_BASE'])

        self.RelIso_L_eta1 = self.muonIsoFile1.Get( 'LooseISO_LooseID_eta/eta_ratio' )
        self.RelIso_L_pt1 = self.muonIsoFile1.Get( 'LooseISO_LooseID_pt/pt_ratio' )
        self.RelIso_L_vtx1 = self.muonIsoFile1.Get( 'LooseISO_LooseID_vtx/tag_nVertices_ratio' )
        self.RelIso_T_eta1 = self.muonIsoFile1.Get( 'TightISO_TightID_eta/eta_ratio' )
        self.RelIso_T_pt1 = self.muonIsoFile1.Get( 'TightISO_TightID_pt/pt_ratio' )
        self.RelIso_T_vtx1 = self.muonIsoFile1.Get( 'TightISO_TightID_vtx/tag_nVertices_ratio' )

        self.RelIso_L_eta2 = self.muonIsoFile2.Get( 'LooseISO_LooseID_eta/eta_ratio' )
        self.RelIso_L_pt2 = self.muonIsoFile2.Get( 'LooseISO_LooseID_pt/pt_ratio' )
        self.RelIso_L_vtx2 = self.muonIsoFile2.Get( 'LooseISO_LooseID_vtx/tag_nVertices_ratio' )
        self.RelIso_T_eta2 = self.muonIsoFile2.Get( 'TightISO_TightID_eta/eta_ratio' )
        self.RelIso_T_pt2 = self.muonIsoFile2.Get( 'TightISO_TightID_pt/pt_ratio' )
        self.RelIso_T_vtx2 = self.muonIsoFile2.Get( 'TightISO_TightID_vtx/tag_nVertices_ratio' )



        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffsRun2#Tracking_efficiency_provided_by
        self.muonTkFile = ROOT.TFile( "%s/src/CMGTools/TTHAnalysis/data/2016MuonEfficienciesAndSF_BDEFGH_TRK.root" % os.environ['CMSSW_BASE'])
        self.Tk_eta = self.muonTkFile.Get( 'ratio_eff_eta3_dr030e030_corr' )
        self.Tk_vtx = self.muonTkFile.Get( 'ratio_eff_vtx_dr030e030_corr' )

        self.channel = channel
        #print self.channel


        self.ptMax = 199.0
        self.nvtxMax = 49

        ### Load the zhSF for the appropriate zType
        if self.channel in ['EETT', 'EEMT', 'EEET', 'EEEM'] :
            print "JEEJEE EETT EEMT EET EEEM"
            self.etaMax = 2.49
            self.singleTrigThreshold = 28.0
            self.subleadingDoubleTrigThreshold = 13.0
            self.singleMin = 27.1
            self.doubleSubleadingMin = 7.1
            self.doubleLeadingMin = 23.1
            self.singleName = 'HLT_Ele27_WPTight_Gsf'
            self.doubleLeadingName = 'HLT_Ele23_CaloIdL_TrackIdL_IsoVL'
            self.doubleSubleadingName = 'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_and_DZ'

        if self.channel in ['MMTT', 'MMMT', 'MMET', 'MMEM'] :
            print "JUHJUHJUH"
            self.etaMax = 2.39
            self.singleTrigThreshold = 25.0
            self.subleadingDoubleTrigThreshold = 10.0
            self.singleMin = 23.1
            self.doubleSubleadingMin = 7.1
            self.doubleLeadingMin = 15.1
            self.singleName = 'HLT_Mu24'
            self.doubleLeadingName = 'HLT_Mu17_TrkIsoVVL'
            self.doubleSubleadingName = 'HLT_Mu8_and_DZ'

        self.sfFile = ROOT.TFile( 'zhTriggerSFs_2016Full_extended.root', 'r' )
        self.singleTriggerData = self.sfFile.Get( self.singleName+'_data' )
        self.doubleLeadingData = self.sfFile.Get( self.doubleLeadingName+'_data' )
        self.doubleSubleadingData = self.sfFile.Get( self.doubleSubleadingName+'_data' )
        self.singleTriggerMC = self.sfFile.Get( self.singleName+'_MC' )
        self.doubleLeadingMC = self.sfFile.Get( self.doubleLeadingName+'_MC' )
        self.doubleSubleadingMC = self.sfFile.Get( self.doubleSubleadingName+'_MC' )

        ###self.branches = [ "triggerSF" ]


        self.branches = [ "electronSF_1", "electronSF_2", "electronSF_3", "electronSF_4",
                          "muonSF_1", "muonSF_2", "muonSF_3", "muonSF_4",
                          "tauSF_3", "tauSF_4", "zhTrigWeight", "massSF"]

    def listBranches(self):
        return self.branches[:]

    def getIDAndIsoScaleFactor( self, pt, eta ) :
        #print wp
        # Make sure we stay on our histograms
        if pt > 99 : pt = 99
        elif pt < 11 : pt = 11
        absEta = abs(eta)

        if absEta <= 1.48 :
            return self.dataBarrel.Eval( pt ) / self.mcBarrel.Eval( pt )
        elif absEta <= 2.1 :
            return self.dataMid.Eval( pt ) / self.mcMid.Eval( pt )
        else :
            return self.dataEndcap.Eval( pt ) / self.mcEndcap.Eval( pt )



    def getGSFAndWPScaleFactor( self, wp, pt, eta ) :
       	assert( wp in ['WP90', 'WP80', 'TrkOnly'] ), "Given WP (%s) is not supported" % wp
        #print wp
        # Make sure we stay on our histograms
        if pt > 199 : pt = 199
        elif pt < 20 : pt = 20
        if eta > 2.5 : eta = 2.5
        elif eta < -2.5 : eta = -2.5

        # GSF file cuts off at pt 25 GeV
        ptGSF = pt if pt > 26 else 26
        SF = self.gsfSF.GetBinContent( self.gsfSF.FindBin( eta, ptGSF ) )
        if wp == 'TrkOnly' : return SF
        if wp == 'WP90' :
            SF *= self.wp90SF.GetBinContent(self.wp90SF.FindBin( eta, pt ) )
            return SF
        elif wp == 'WP80' :
            SF *= self.wp80SF.GetBinContent( self.wp80SF.FindBin( eta, pt ) )
            return SF
        else :
            return SF

    def getIDScaleFactor( self, ID, pt, eta, vtx ) :
        #print "ID",ID
        SF = 1.
        # Make sure we stay on our histograms
        if pt > 199 : pt = 199
        elif pt < 20 : pt = 21
        if vtx > 50 : vtx = 50
        if ID == 'Loose' :
            SF1 = self.ID_L_eta1.GetBinContent( self.ID_L_eta1.FindBin( eta ) )
            SF1 *= self.ID_L_pt1.GetBinContent( self.ID_L_pt1.FindBin( pt ) )
            SF1 *= self.ID_L_vtx1.GetBinContent( self.ID_L_vtx1.FindBin( vtx ) )
            SF1 *= self.bcdef
            SF2 = self.ID_L_eta2.GetBinContent( self.ID_L_eta2.FindBin( eta ) )
            SF2 *= self.ID_L_pt2.GetBinContent( self.ID_L_pt2.FindBin( pt ) )
            SF2 *= self.ID_L_vtx2.GetBinContent( self.ID_L_vtx2.FindBin( vtx ) )
            SF2 *= self.gh
            return SF1 + SF2
        elif ID == 'Medium' :
            SF1 = self.ID_M_eta1.GetBinContent( self.ID_M_eta1.FindBin( eta ) )
            SF1 *= self.ID_M_pt1.GetBinContent( self.ID_M_pt1.FindBin( pt ) )
            SF1 *= self.ID_M_vtx1.GetBinContent( self.ID_M_vtx1.FindBin( vtx ) )
            SF1 *= self.bcdef
            SF2 = self.ID_M_eta2.GetBinContent( self.ID_M_eta2.FindBin( eta ) )
            SF2 *= self.ID_M_pt2.GetBinContent( self.ID_M_pt2.FindBin( pt ) )
            SF2 *= self.ID_M_vtx2.GetBinContent( self.ID_M_vtx2.FindBin( vtx ) )
            SF2 *= self.gh
            return SF1 + SF2
        else :
            return SF

    def getRelIsoScaleFactor( self, Iso, pt, eta, vtx ) :
        #print "Iso",Iso
        SF = 1.
        # Make sure we stay on our histograms
        if pt > 199 : pt = 199
        elif pt < 20 : pt = 21
        if vtx > 50 : vtx = 50
        if Iso == 'Loose' :
            SF1 = self.RelIso_L_eta1.GetBinContent( self.RelIso_L_eta1.FindBin( eta ) )
            SF1 *= self.RelIso_L_pt1.GetBinContent( self.RelIso_L_pt1.FindBin( pt ) )
            SF1 *= self.RelIso_L_vtx1.GetBinContent( self.RelIso_L_vtx1.FindBin( vtx ) )
            SF1 *= self.bcdef
            SF2 = self.RelIso_L_eta2.GetBinContent( self.RelIso_L_eta2.FindBin( eta ) )
            SF2 *= self.RelIso_L_pt2.GetBinContent( self.RelIso_L_pt2.FindBin( pt ) )
            SF2 *= self.RelIso_L_vtx2.GetBinContent( self.RelIso_L_vtx2.FindBin( vtx ) )
            SF2 *= self.gh
            return SF1 + SF2
        elif Iso == 'Tight' :
            SF1 = self.RelIso_T_eta1.GetBinContent( self.RelIso_T_eta1.FindBin( eta ) )
            SF1 *= self.RelIso_T_pt1.GetBinContent( self.RelIso_T_pt1.FindBin( pt ) )
            SF1 *= self.RelIso_T_vtx1.GetBinContent( self.RelIso_T_vtx1.FindBin( vtx ) )
            SF1 *= self.bcdef
            SF2 = self.RelIso_T_eta2.GetBinContent( self.RelIso_T_eta2.FindBin( eta ) )
            SF2 *= self.RelIso_T_pt2.GetBinContent( self.RelIso_T_pt2.FindBin( pt ) )
            SF2 *= self.RelIso_T_vtx2.GetBinContent( self.RelIso_T_vtx2.FindBin( vtx ) )
            SF2 *= self.gh
            return SF1 + SF2
        else :
            return SF

    def getTkScaleFactor( self, eta, vtx ) :
        #print "Tk",Tk
        SF = 0.995
        # Make sure we stay on our histograms
        #if eta > 2.39 : eta = 2.39
        #elif eta < -2.39 : eta = -2.39
        #if vtx > 45 : vtx = 45
        #elif vtx < 1 : vtx = 1
        #SF = self.Tk_eta.Eval( eta )
        #SF *= self.Tk_vtx.Eval( vtx )
        return SF

    def getZHTriggerSF( self, nvtx, pt1, eta1, pt2, eta2 ) :
        assert( pt1 >= pt2 ), "Lepton pTs must be ordered"

        # Make sure we stay on our histograms
        if pt1 > self.ptMax : pt1 = self.ptMax
        elif pt1 < self.doubleLeadingMin : pt1 = self.doubleLeadingMin
        if pt2 > self.ptMax : pt2 = self.ptMax
        elif pt2 < self.doubleSubleadingMin : pt2 = self.doubleSubleadingMin

        if eta1 > self.etaMax : eta1 = self.etaMax
        elif eta1 < -1 * self.etaMax : eta1 = -1 * self.etaMax

        if eta2 > self.etaMax : eta2 = self.etaMax
        elif eta2 < -1 * self.etaMax : eta2 = -1 * self.etaMax

        if nvtx > self.nvtxMax : nvtx = self.nvtxMax

        #print nvtx, pt1, eta1, pt2, eta2

        # In Z->EE it is possible to not fire the double trigger b/c
        # of low pT subleading with high pT leading firing single E
        ineff_data = 1.0
        ineff_mc = 1.0
        # Check double lep thresholds
        if pt2 > self.subleadingDoubleTrigThreshold :
            ineff_data *= (1. - self.doubleLeadingData.GetBinContent( self.doubleLeadingData.FindBin( pt1, eta1 ) ) \
                    * self.doubleSubleadingData.GetBinContent( self.doubleSubleadingData.FindBin( pt2, nvtx ) ) )
            ineff_mc *= (1. - self.doubleLeadingMC.GetBinContent( self.doubleLeadingMC.FindBin( pt1, eta1 ) ) \
                    * self.doubleSubleadingMC.GetBinContent( self.doubleSubleadingMC.FindBin( pt2, nvtx ) ) )
            #print self.doubleLeadingMC.GetBinContent( self.doubleLeadingMC.FindBin( pt1, eta1 ) )
            #print self.doubleSubleadingMC.GetBinContent( self.doubleSubleadingMC.FindBin( pt2, nvtx ) )
            #print 1, ineff_mc

        # second "region"
        if pt1 > self.singleTrigThreshold :
            ineff_data *= (1. - self.singleTriggerData.GetBinContent( self.singleTriggerData.FindBin( pt1, eta1 ) ) )
            ineff_mc *= (1. - self.singleTriggerMC.GetBinContent( self.singleTriggerMC.FindBin( pt1, eta1 ) ) )
            #print 2, ineff_mc

            # third "region" only possible if second region is true
            if pt2 > self.singleTrigThreshold :
                ineff_data *= (1. - self.singleTriggerData.GetBinContent( self.singleTriggerData.FindBin( pt2, eta2 ) ) )
                ineff_mc *= (1. - self.singleTriggerMC.GetBinContent( self.singleTriggerMC.FindBin( pt2, eta2 ) ) )
                #print 3, ineff_mc

        #print 4, ineff_mc
        eff_data = 1.0 - ineff_data
        eff_mc = 1.0 - ineff_mc
        return eff_data / eff_mc


    def getZHTriggerDataEff( self, nvtx, pt1, eta1, pt2, eta2 ) :
        assert( pt1 >= pt2 ), "Lepton pTs must be ordered"

        # Make sure we stay on our histograms
        if pt1 > self.ptMax : pt1 = self.ptMax
        elif pt1 < self.doubleLeadingMin : pt1 = self.doubleLeadingMin
        if pt2 > self.ptMax : pt2 = self.ptMax
        elif pt2 < self.doubleSubleadingMin : pt2 = self.doubleSubleadingMin

        if eta1 > self.etaMax : eta1 = self.etaMax
        elif eta1 < -1 * self.etaMax : eta1 = -1 * self.etaMax

        if eta2 > self.etaMax : eta2 = self.etaMax
        elif eta2 < -1 * self.etaMax : eta2 = -1 * self.etaMax

        if nvtx > self.nvtxMax : nvtx = self.nvtxMax

        # In Z->EE it is possible to not fire the double trigger b/c
        # of low pT subleading with high pT leading firing single E
        ineff_data = 1.0
        # Check double lep thresholds
        if pt2 > self.subleadingDoubleTrigThreshold :
            ineff_data *= (1. - self.doubleLeadingData.GetBinContent( self.doubleLeadingData.FindBin( pt1, eta1 ) ) \
                    * self.doubleSubleadingData.GetBinContent( self.doubleSubleadingData.FindBin( pt2, nvtx ) ) )

        # second "region"
        if pt1 > self.singleTrigThreshold :
            ineff_data *= (1. - self.singleTriggerData.GetBinContent( self.singleTriggerData.FindBin( pt1, eta1 ) ) )

            # third "region" only possible if second region is true
            if pt2 > self.singleTrigThreshold :
                ineff_data *= (1. - self.singleTriggerData.GetBinContent( self.singleTriggerData.FindBin( pt2, eta2 ) ) )

        eff_data = 1.0 - ineff_data
        return eff_data


    def getZHTriggerMCEff( self, nvtx, pt1, eta1, pt2, eta2 ) :
        assert( pt1 >= pt2 ), "Lepton pTs must be ordered"

        # Make sure we stay on our histograms
        if pt1 > self.ptMax : pt1 = self.ptMax
        elif pt1 < self.doubleLeadingMin : pt1 = self.doubleLeadingMin
        if pt2 > self.ptMax : pt2 = self.ptMax
        elif pt2 < self.doubleSubleadingMin : pt2 = self.doubleSubleadingMin

        if eta1 > self.etaMax : eta1 = self.etaMax
        elif eta1 < -1 * self.etaMax : eta1 = -1 * self.etaMax

        if eta2 > self.etaMax : eta2 = self.etaMax
        elif eta2 < -1 * self.etaMax : eta2 = -1 * self.etaMax

        if nvtx > self.nvtxMax : nvtx = self.nvtxMax

        # In Z->EE it is possible to not fire the double trigger b/c
        # of low pT subleading with high pT leading firing single E
        ineff_mc = 1.0
        # Check double lep thresholds
        if pt2 > self.subleadingDoubleTrigThreshold :
            ineff_mc *= (1. - self.doubleLeadingMC.GetBinContent( self.doubleLeadingMC.FindBin( pt1, eta1 ) ) \
                    * self.doubleSubleadingMC.GetBinContent( self.doubleSubleadingMC.FindBin( pt2, nvtx ) ) )

        # second "region"
        if pt1 > self.singleTrigThreshold :
            ineff_mc *= (1. - self.singleTriggerMC.GetBinContent( self.singleTriggerMC.FindBin( pt1, eta1 ) ) )

            # third "region" only possible if second region is true
            if pt2 > self.singleTrigThreshold :
                ineff_mc *= (1. - self.singleTriggerMC.GetBinContent( self.singleTriggerMC.FindBin( pt2, eta2 ) ) )

        eff_mc = 1.0 - ineff_mc
        return eff_mc


    def massScaling(self, genMass, chunk) :
        SF = 1.0
        ###print "we are getting the massScale"
        if "350" in chunk:
            if genMass>=360:
                genMass = 359
            elif genMass<340:
                genMass = 340
            ###print "genMass: ", genMass
            SF =  self.mass350.GetBinContent( self.mass350.FindBin(genMass) )
            #print "scaleFactor: ", SF  
        elif "400" in chunk:
            if genMass>=410:
       	       	genMass	= 409 
       	    elif genMass<390:
       	       	genMass	= 390
            SF =  self.mass400.GetBinContent( self.mass400.FindBin(genMass) )
 
        return SF

    def __call__(self,event):
        #(met, metphi)  = event.met, event.met_phi
        ret = dict([(name,0.0) for name in self.branches])

        #Z legs
        pt1 = event.pt_1
        eta1 = event.eta_1

        pt2 = event.pt_2
        eta2 = event.eta_2

        #H legs
        pt3 = event.shiftedPt_3
        eta3 = event.eta_3

        pt4 = event.shiftedPt_4
        eta4 = event.eta_4

        vtx = event.npv

        match_t1 = 1
        match_t2 = 1

        genMass = event.genMass
        scaleMass = 1.0
        #print self.chunk
        if "350" in self.chunk or "400" in self.chunk:
            scaleMass = self.massScaling(genMass, self.chunk)
        ret["massSF"] = scaleMass

        ##ret["evt"] = event.evt
        SF = self.getZHTriggerSF( vtx, pt1, eta1, pt2, eta2 )
        ret["zhTrigWeight"] = SF

            

        if self.channel == "EEMT":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["muonSF_3"] = self.getIDScaleFactor( 'Loose', pt3, eta3, vtx )*self.getRelIsoScaleFactor( 'Tight', pt3, eta3, vtx )*self.getTkScaleFactor( eta3, vtx )
            match_t2 = event.gen_match_4

            ret["electronSF_3"] = 1.0

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_4"] = 1.0

        elif self.channel == "EEET":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'TrkOnly', pt3, eta3 )*self.getIDAndIsoScaleFactor( pt3, eta3 )
            match_t2 = event.gen_match_4

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0

        elif self.channel == "EEEM":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'TrkOnly', pt3, eta3 )*self.getIDAndIsoScaleFactor( pt3, eta3 )
            ret["muonSF_4"] = self.getIDScaleFactor( 'Loose', pt4, eta4, vtx )*self.getRelIsoScaleFactor( 'Tight', pt4, eta4, vtx )*self.getTkScaleFactor( eta4, vtx )

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_3"] = 1.0

        elif self.channel == "EETT":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            match_t1 = event.gen_match_3
            match_t2 = event.gen_match_4

            ret["electronSF_3"] = 1.0

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0


        elif self.channel == "MMMT":
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            ret["muonSF_3"] = self.getIDScaleFactor( 'Loose', pt3, eta3, vtx )*self.getRelIsoScaleFactor( 'Tight', pt3, eta3, vtx )*self.getTkScaleFactor( eta3, vtx )
            match_t2 = event.gen_match_4

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0
            ret["electronSF_3"] = 1.0

            ret["muonSF_4"] = 1.0

        elif self.channel == "MMET":
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'TrkOnly', pt3, eta3 )*self.getIDAndIsoScaleFactor( pt3, eta3 )
            match_t2 = event.gen_match_4

            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0

        elif self.channel == "MMEM":
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'TrkOnly', pt3, eta3 )*self.getIDAndIsoScaleFactor( pt3, eta3 )
            ret["muonSF_3"] = 1.0	

            ret["muonSF_4"] = self.getIDScaleFactor( 'Loose', pt4, eta4, vtx )*self.getRelIsoScaleFactor( 'Tight', pt4, eta4, vtx )*self.getTkScaleFactor( eta4, vtx )

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0

        elif self.channel == "MMTT":
            #####print "taalla ollaanJEEEEEEEEEEEEEEEEEEEEE"
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            match_t1 = event.gen_match_3
            match_t2 = event.gen_match_4

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0
            ret["electronSF_3"] = 1.0

            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0
        #unchanged variables
        ret["electronSF_4"] = 1.0       

        if match_t1 == 5:
            ret["tauSF_3"] = 0.97
        else:
            ret["tauSF_3"] = 1.0
        if match_t2 == 5:
            ret["tauSF_4"] = 0.97
        else:
            ret["tauSF_4"] = 1.0

        return ret


MODULES = [ 
 ( 'scaleFactorsEETT', lambda : scaleFactors("EETT") ), 
 ( 'scaleFactorsEEET', lambda : scaleFactors("EEET") ), 
 ( 'scaleFactorsEEEM', lambda : scaleFactors("EEEM") ), 
 ( 'scaleFactorsEEMT', lambda : scaleFactors("EEMT") ), 
 ( 'scaleFactorsMMTT', lambda : scaleFactors("MMTT") ), 
 ( 'scaleFactorsMMET', lambda : scaleFactors("MMET") ), 
 ( 'scaleFactorsMMEM', lambda : scaleFactors("MMEM") ),  
 ( 'scaleFactorsMMMT', lambda : scaleFactors("MMMT") ) ]


if __name__ == '__main__':
    from sys import argv
    #filename = argv[1]
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    #chunk = argv[2]
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = scaleFactors()
            self.f_el.Close()	
            self.f_el_80.Close()
            self.f_el_90.Close()
            self.muonIsoFile1.Close()
            self.muonIsoFile2.Close()
            self.muonIDFile1.Close()
            self.muonIDFile2.Close()
            self.muonTkFile.Close()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d" % (ev.run, ev.lumi, ev.evt)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)


