'''
A Class to interface with Electron Scale Factors:
https://twiki.cern.ch/twiki/bin/view/CMS/EgammaIDRecipesRun2#Electron_efficiencies_and_scale
Currently using WP90
Also, GSF SFs must be applied on top as well
'''


from CMGTools.TTHAnalysis.treeReAnalyzer import *

class scaleFactors:
    def __init__(self, channel):

        self.f_el = ROOT.TFile("%s/src/CMGTools/TTHAnalysis/data/egammaEffi.txt_EGM2D.root" % os.environ['CMSSW_BASE']) 

        self.channel = channel
        self.branches = [ "electronSF_1", "electronSF_2", "electronSF_3", "electronSF_4",
                          "muonSF_1", "muonSF_2", "muonSF_3", "muonSF_4",
                          "tauSF_3", "tauSF_4" ]
        self.f_el.Close()

    def listBranches(self):
        return self.branches[:]

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
            SF *= self.wp90SF.GetBinContent( self.wp90SF.FindBin( eta, pt ) )
            return SF
        elif wp == 'WP80' :
            SF *= self.wp80SF.GetBinContent( self.wp80SF.FindBin( eta, pt ) )
            return SF
        else :
            return SF


    def __call__(self,event):
        #(met, metphi)  = event.met, event.met_phi
        # prepare output
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

        if self.channel == "EETT":
            ret["electronSF_1"] = eSF.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
            ret["electronSF_2"] = eSF.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )
            ret["electronSF_3"] = 1.0
            ret["electronSF_4"] = 1.0

            ret["muonSF_1"] = 1.0
            ret["muonSF_2"] = 1.0
            ret["muonSF_3"] = 1.0
            ret["muonSF_4"] = 1.0

            ret["tauSF_3"] = 0.95
            ret["tauSF_4"] = 0.95

        return ret


MODULES = [ ( 'scaleFactors', lambda : scaleFactors("EETT") ), ]

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = scaleMass()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d" % (ev.run, ev.lumi, ev.evt)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)



import ROOT
from ROOT import TTree
from array import array


class ElectronSF :
    """A class to provide electron SFs for
    Isolation, ID and Trigger (not using trigger currenly)"""
    

    def __init__( self ):

        ### Load the ICHEP SFs provided by the Electron POG
        self.electronGSFFile = ROOT.TFile( 'egammaEffi.txt_EGM2D.root', 'r' )
        self.gsfSF = self.electronGSFFile.Get( 'EGamma_SF2D' )

        self.electronWP80File = ROOT.TFile( 'egammaEffi.txt_EGM2D.root', 'r' )
        self.wp80SF = self.electronWP80File.Get( 'EGamma_SF2D' )

        self.electronWP90File = ROOT.TFile( 'egammaEffi.txt_EGM2D.root', 'r' )
        self.wp90SF = self.electronWP90File.Get( 'EGamma_SF2D' )



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
            SF *= self.wp90SF.GetBinContent( self.wp90SF.FindBin( eta, pt ) )
            return SF
        elif wp == 'WP80' :
            SF *= self.wp80SF.GetBinContent( self.wp80SF.FindBin( eta, pt ) )
            return SF
        else :
            return SF


        

if __name__ == '__main__' :
    eSF = ElectronSF()

    f = ROOT.TFile('EETT_aug15_sync_triggerTESTI.root','update')

    t = f.Get('tree')

    #electrons
    electronSF_1 = array('d', [ 0 ] )
    eleSFB = t.Branch('electronSF_1', electronSF_1, 'electronSF_1/D')
 
    electronSF_2 = array('d', [ 0 ] )
    ele2SFB = t.Branch('electronSF_2', electronSF_2, 'electronSF_2/D')

    electronSF_3 = array('d', [ 0 ] )
    ele3SFB = t.Branch('electronSF_3', electronSF_3, 'electronSF_3/D')

    electronSF_4 = array('d', [ 0 ] )
    ele4SFB = t.Branch('electronSF_4', electronSF_4, 'electronSF_4/D')

    #muons
    muonSF_1 = array('d', [ 0 ] )
    muonSFB = t.Branch('muonSF_1', muonSF_1, 'muonSF_1/D')

    muonSF_2 = array('d', [ 0 ] )
    muon2SFB = t.Branch('muonSF_2', muonSF_2, 'muonSF_2/D')

    muonSF_3 = array('d', [ 0 ] )
    muon3SFB = t.Branch('muonSF_3', muonSF_3, 'muonSF_3/D')

    muonSF_4 = array('d', [ 0 ] )
    muon4SFB = t.Branch('muonSF_4', muonSF_4, 'muonSF_4/D')

    #taus
    tauSF_3 = array('d', [ 0 ] )
    tau3SFB = t.Branch('tauSF_3', tauSF_3, 'tauSF_3/D')

    tauSF_4 = array('d', [ 0 ] )
    tau4SFB = t.Branch('tauSF_4', tauSF_4, 'tauSF_4/D')


    for row in t :
        pt1 = getattr( row, 'pt_1' )
        eta1 = getattr( row, 'eta_1' )
        pt2 = getattr( row, 'pt_2' )
        eta2 = getattr( row, 'eta_2' )
        
        electronSF_1[0] = eSF.getGSFAndWPScaleFactor( 'WP90', pt1, eta1 )
        electronSF_2[0] = eSF.getGSFAndWPScaleFactor( 'WP90', pt2, eta2 )

        electronSF_3[0] = 1.0
        electronSF_4[0] = 1.0 

        muonSF_1[0] = 1.0
        muonSF_2[0] = 1.0
        muonSF_3[0] = 1.0
        muonSF_4[0] = 1.0
     
        tauSF_3[0] = 1.0
        tauSF_4[0] = 1.0
        
        eleSFB.Fill()
        ele2SFB.Fill()
        ele3SFB.Fill()
        ele4SFB.Fill()

        muonSFB.Fill()
        muon2SFB.Fill()
        muon3SFB.Fill()
        muon4SFB.Fill()          
 
        tau3SFB.Fill()
        tau4SFB.Fill()
    #t.Fill()

    #t.Print()
    f.cd()
    t.Write()
    f.Close()

