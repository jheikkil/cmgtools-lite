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
        self.branches = [ "electronSF_1", "electronSF_2", "electronSF_3", "electronSF_4",
                          "muonSF_1", "muonSF_2", "muonSF_3", "muonSF_4",
                          "tauSF_3", "tauSF_4" ]

    def listBranches(self):
        return self.branches[:]

    def getGSFAndWPScaleFactor( self, wp, pt, eta ) :
        #print "TULTIIN TNNE"
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
        #elif wp == 'WP80' :
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
        #print "JEE ISO"
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
        SF = 1.
        # Make sure we stay on our histograms
        if eta > 2.39 : eta = 2.39
        elif eta < -2.39 : eta = -2.39
        if vtx > 45 : vtx = 45
        elif vtx < 1 : vtx = 1
        SF = self.Tk_eta.Eval( eta )
        SF *= self.Tk_vtx.Eval( vtx )
        return SF


    def __call__(self,event):
        #(met, metphi)  = event.met, event.met_phi
        # prepare output
        #print "EKA OSUUS"
        ret = dict([(name,0.0) for name in self.branches])

        #Z legs
        pt1 = event.pt_1
        eta1 = event.eta_1

        pt2 = event.pt_2
        eta2 = event.eta_2

        #H legs
        pt3 = event.pt_3
        eta3 = event.eta_3

        pt4 = event.pt_4
        eta4 = event.eta_4

        vtx = event.npv

        match_t1 = 1
        match_t2 = 1


        if self.channel == "EEMT":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["muonSF_3"] = self.getIDScaleFactor( 'Loose', pt3, eta3, vtx )*self.getRelIsoScaleFactor( 'Loose', pt3, eta3, vtx )*self.getTkScaleFactor( eta3, vtx )
            match_t2 = event.gen_match_4

            ret["electronSF_3"] = 1.0

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_4"] = 1.0

        elif self.channel == "EEET":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'WP80', pt3, eta3 )
            match_t2 = event.gen_match_4

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0

        elif self.channel == "EEEM":
            ret["electronSF_1"] = self.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = self.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'WP80', pt3, eta3 )
            ret["muonSF_4"] = self.getIDScaleFactor( 'Loose', pt4, eta4, vtx )*self.getRelIsoScaleFactor( 'Loose', pt4, eta4, vtx )*self.getTkScaleFactor( eta4, vtx )

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

            ret["muonSF_3"] = self.getIDScaleFactor( 'Loose', pt3, eta3, vtx )*self.getRelIsoScaleFactor( 'Loose', pt3, eta3, vtx )*self.getTkScaleFactor( eta3, vtx )
            match_t2 = event.gen_match_4

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0
            ret["electronSF_3"] = 1.0

            ret["muonSF_4"] = 1.0

        elif self.channel == "MMET":
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'WP80', pt3, eta3 )
            match_t2 = event.gen_match_4

            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0

            ret["electronSF_1"] = 1.0
            ret["electronSF_2"] = 1.0

        elif self.channel == "MMEM":
            ret["muonSF_1"] = self.getIDScaleFactor( 'Loose', pt1, eta1, vtx )*self.getRelIsoScaleFactor( 'Loose', pt1, eta1, vtx )*self.getTkScaleFactor( eta1, vtx )
            ret["muonSF_2"] = self.getIDScaleFactor( 'Loose', pt2, eta2, vtx )*self.getRelIsoScaleFactor( 'Loose', pt2, eta2, vtx )*self.getTkScaleFactor( eta2, vtx )

            ret["electronSF_3"] = self.getGSFAndWPScaleFactor( 'WP80', pt3, eta3 )
            ret["muonSF_3"] = 1.0	

            ret["muonSF_4"] = self.getIDScaleFactor( 'Loose', pt3, eta3, vtx )*self.getRelIsoScaleFactor( 'Loose', pt3, eta3, vtx )*self.getTkScaleFactor( eta3, vtx )

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
            ret["tauSF_3"] = 0.95
        else:
            ret["tauSF_3"] = 1.0
        if match_t2 == 5:
            ret["tauSF_4"] = 0.95
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
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
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


