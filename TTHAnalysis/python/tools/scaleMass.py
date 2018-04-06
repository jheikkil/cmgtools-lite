
from CMGTools.TTHAnalysis.treeReAnalyzer import *

class scaleMass:
    def __init__(self):
        self.branches = [ "A_scaled", "A_scaledPT", 
                          "A_Hscaled", "A_HscaledPT",
                          "A_Zscaled", "A_ZscaledPT"] 

    def listBranches(self):
        return self.branches[:]

    def getDoubleMass(self, pt1, eta1, phi1, m1, pt2, eta2, phi2, m2 ) :
        lorentz1 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz1.SetPtEtaPhiM( pt1, eta1, phi1, m1 )
        lorentz2 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz2.SetPtEtaPhiM( pt2, eta2, phi2, m2 )

        return (lorentz1 + lorentz2).M()


    def scaleMassPT(self, pt1, eta1, phi1, m1, pt2, eta2, phi2, m2, Mass2scale, scalePT=True ) :
        lorentz1 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz1.SetPtEtaPhiM( pt1, eta1, phi1, m1 )
        lorentz2 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz2.SetPtEtaPhiM( pt2, eta2, phi2, m2 )

        lorentz3 = ROOT.TLorentzVector( 0.,0.,0.,0. )

        if Mass2scale==91:
            scale = 91.2/(lorentz1 + lorentz2).M()
        else:
            scale = 125.0/(lorentz1 + lorentz2).M()
        phi = (lorentz1 + lorentz2).Phi()
        eta = (lorentz1 + lorentz2).Eta()
        pt = (lorentz1 + lorentz2).Pt()
        mass = (lorentz1 + lorentz2).M()

        if scalePT:
            lorentz3.SetPtEtaPhiM( scale*pt, eta, phi, scale*mass )
        else:
            lorentz3.SetPtEtaPhiM( pt, eta, phi, scale*mass )

        return lorentz3

    def __call__(self,event):
        #(met, metphi)  = event.met, event.met_phi
        # prepare output
        ret = dict([(name,0.0) for name in self.branches])

        #Z legs
        pt1 = event.pt_1
        eta1 = event.eta_1 
        phi1 = event.phi_1 
        m1 = event.m_1 

        m2 = event.m_2 
        pt2 = event.pt_2 
        eta2 = event.eta_2 
        phi2 = event.phi_2 

        ptZ = event.Z_Pt 
        etaZ = event.Z_Eta 
        phiZ = event.Z_Phi
        mZ = event.m_vis 

        Zunscaled = ROOT.TLorentzVector( 0.,0.,0.,0. )
        Zunscaled.SetPtEtaPhiM( ptZ, etaZ, phiZ, mZ )

        #Ztesti = self.getDoubleMass( pt1, eta1, phi1, m1, pt2, eta2, phi2, m2 )

        #print mZ
        #print Zunscaled.M()
        #print Ztesti

        #H legs
        pt3 = event.pt_3 
        eta3 = event.eta_3 
        phi3 = event.phi_3 
        m3 = event.m_3 

        pt4 = event.pt_4 
        eta4 = event.eta_4 
        phi4 = event.phi_4 
        m4 = event.m_4 

        ptH = event.H_Pt 
        etaH = event.H_Eta 
        phiH = event.H_Phi 
        mH = event.H_vis 

        Hunscaled = ROOT.TLorentzVector( 0.,0.,0.,0. )
        Hunscaled.SetPtEtaPhiM( ptH, etaH, phiH, mH )

        #Htesti = self.getDoubleMass( pt3, eta3, phi3, m3, pt4, eta4, phi4, m4 )

       	#print mH
       	#print Hunscaled.M()
       	#print Htesti


    #Get 4-vectors and fill output
        scalePT = False
        Zscaled = self.scaleMassPT( pt1, eta1, phi1, m1, pt2, eta2, phi2, m2, 91, scalePT )
       	scalePT	= True
        Zscaledpt = self.scaleMassPT( pt1, eta1, phi1, m1, pt2, eta2, phi2, m2, 91, scalePT )

       	scalePT	= False
        Hscaled = self.scaleMassPT( pt3, eta3, phi3, m3, pt4, eta4, phi4, m4, 125, scalePT )
       	scalePT	= True
        Hscaledpt = self.scaleMassPT( pt3, eta3, phi3, m3, pt4, eta4, phi4, m4, 125, scalePT )
 
        ret["A_scaled"] = (Zscaled+Hscaled).M()
        ret["A_scaledPT"] = (Zscaledpt + Hscaledpt).M()
 
        ret["A_Hscaled"] = (Zunscaled+Hscaled).M()
        ret["A_HscaledPT"] = (Zunscaled+Hscaledpt).M()

        ret["A_Zscaled"] = (Zscaled+Hunscaled).M()
        ret["A_ZscaledPT"] = (Zscaledpt+Hunscaled).M()

        return ret


MODULES = [ ( 'scaleMass', lambda : scaleMass() ), ]

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
