import os
import array

#from array import array
from ROOT import TMatrixD, std, TFile, TH1

from TauAnalysis.ClassicSVfit.MeasuredTauLepton import MeasuredTauLepton
from TauAnalysis.ClassicSVfit.ClassicSVfit import ClassicSVfit as SVfitAlgo

#from TauAnalysis.ClassicSVfit.svFitHistogramAdapter import svFitHistogramAdapter

#../../../TauAnalysis/ClassicSVfit/python/
#../../../SVfitStandalone/python/
##from CMGTools.TauAnalysis.ClassicSVfit.SVfitStandaloneAlgorithm import SVfitAlgoOld
#from CMGTools.SVfitStandalone.MeasuredTauLepton import measuredTauLepton


#import needed stuff

#TH1.AddDirectory(False)

#import os
#import array

from CMGTools.TTHAnalysis.treeReAnalyzer import *

class svFit_classic:
    def __init__(self, channel):
        self.branches = [ "A_vis", "A_Hscaled", "A_svFit", "A_svFit_scaled", "A_svFit_constrained",
                          "H_vis", "H_scaled", "H_svFit", "H_svFit_scaled" , "H_svFit_constrained", "H_LT",
                          "A_vis_DM0_up", "A_vis_DM0_dn", "A_vis_DM1_up", "A_vis_DM1_dn", "A_vis_DM10_up",
                          "A_vis_DM10_dn", "A_vis_JEC_up", "A_vis_JEC_dn", "A_vis_UEC_up", "A_vis_UEC_dn",
                          "H_vis_DM0_up", "H_vis_DM0_dn", "H_vis_DM1_up", "H_vis_DM1_dn", "H_vis_DM10_up",
                          "H_vis_DM10_dn", "H_vis_JEC_up", "H_vis_JEC_dn", "H_vis_UEC_up", "H_vis_UEC_dn",
                          "H_LT_DM0_up", "H_LT_DM0_dn", "H_LT_DM1_up", "H_LT_DM1_dn", "H_LT_DM10_up", "H_LT_DM10_dn", "H_LT_JEC_up", "H_LT_JEC_dn", "H_LT_UEC_up", "H_LT_UEC_dn",
                         "A_svFit_DM0_up", "A_svFit_DM0_dn", "A_svFit_DM1_up", "A_svFit_DM1_dn", "A_svFit_DM10_up", "A_svFit_DM10_dn", "A_svFit_JEC_up", "A_svFit_JEC_dn", "A_svFit_UEC_up", "A_svFit_UEC_dn",
                         "A_svFit_constrained_DM0_up", "A_svFit_constrained_DM0_dn", "A_svFit_constrained_DM1_up", "A_svFit_constrained_DM1_dn", "A_svFit_constrained_DM10_up", "A_svFit_constrained_DM10_dn",
                         "A_svFit_constrained_JEC_up", "A_svFit_constrained_JEC_dn", "A_svFit_constrained_UEC_up", "A_svFit_constrained_UEC_dn",
                         "H_svFit_DM0_up", "H_svFit_DM0_dn", "H_svFit_DM1_up", "H_svFit_DM1_dn", "H_svFit_DM10_up",
                         "H_svFit_DM10_dn", "H_svFit_JEC_up", "H_svFit_JEC_dn", "H_svFit_UEC_up", "H_svFit_UEC_dn",
                         "H_svFit_constrained_DM0_up", "H_svFit_constrained_DM0_dn", "H_svFit_constrained_DM1_up", "H_svFit_constrained_DM1_dn", "H_svFit_constrained_DM10_up",
                         "H_svFit_constrained_DM10_dn", "H_svFit_constrained_JEC_up", "H_svFit_constrained_JEC_dn", "H_svFit_constrained_UEC_up", "H_svFit_constrained_UEC_dn"]

        self.channel = channel
    def listBranches(self):
        return self.branches[:]

    def scaleMassPT(self, pt1, eta1, phi1, m1, pt2, eta2, phi2, m2, Mass2scale, scalePT=True ) :
        lorentz1 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz1.SetPtEtaPhiM( pt1, eta1, phi1, m1 )
        lorentz2 = ROOT.TLorentzVector( 0.,0.,0.,0. )
        lorentz2.SetPtEtaPhiM( pt2, eta2, phi2, m2 )

        lorentz3 = ROOT.TLorentzVector( 0.,0.,0.,0. )

        if Mass2scale==91:
            scale = 91.2/(lorentz1 + lorentz2).M()
        else:
            scale = 125.06/(lorentz1 + lorentz2).M()
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

        ##Get Z boson
        ptZ = event.Z_Pt
        etaZ = event.Z_Eta
        phiZ = event.Z_Phi
        mZ = event.m_vis

        Zunscaled = ROOT.TLorentzVector( 0.,0.,0.,0. )
        Zunscaled.SetPtEtaPhiM( ptZ, etaZ, phiZ, mZ )

        #Fetch Higgs legs 
        pt3 = event.shiftedPt_3
        eta3 = event.eta_3
        phi3 = event.phi_3
        m3 = event.m_3
        genmatch3 = event.gen_match_3
        
        pt4 = event.shiftedPt_4
        eta4 = event.eta_4
        phi4 = event.phi_4
        m4 = event.m_4
        genmatch4 = event.gen_match_4

        DM3 = -1
        DM4 = -1


        if self.channel=="EETT" or self.channel=="MMTT":
            DM3 = int(event.decayMode_3)
            DM4 = int(event.decayMode_4)  
        elif self.channel=="EEET" or self.channel=="MMET" or self.channel=="EEMT" or self.channel=="MMMT":
            DM3 = -1                    
            DM4 = int(event.decayMode_4)


        ##print "masses of taus", m3, m4
        #Add here the final state if sentences... for types
        if self.channel=="EETT" or self.channel=="MMTT":
            l1type = 1
            l2type = 1
            if DM3 == 0 and genmatch3 == 5:
                m3 = 0.1395699 
            if DM4 == 0 and genmatch4 == 5:
                m4 = 0.1395699
        if self.channel=="EEET" or self.channel=="MMET":
            l1type = 2
            l2type = 1
       	    m3 = 0.51100e-3  # PDG mass [GeV]
            if DM4 == 0 and genmatch4 == 5:
                m4 = 0.1395699
        if self.channel=="EEMT" or self.channel=="MMMT":
            l1type = 3
            l2type = 1
       	    m3 = 0.105658 # PDG mass [GeV]
            if DM4 == 0 and genmatch4 == 5:
       	        m4 = 0.1395699        
        if self.channel=="EEEM" or self.channel=="MMEM":
            l1type = 2
            l2type = 3
            m3 = 0.51100e-3  # PDG mass [GeV]
       	    m4 = 0.105658    # PDG mass [GeV]
	

        
        ptH = event.H_Pt
        etaH = event.H_Eta
        phiH = event.H_Phi

        #unscaled values
        mH = event.H_vis
        mA = event.Mass
        ret["H_vis"] = mH
        ret["A_vis"] = mA
        ret["H_LT"] = pt3+pt4

        #Get 4-vectors and fill output
        scalePT = True
        Hscaledpt = self.scaleMassPT( pt3, eta3, phi3, m3, pt4, eta4, phi4, m4, 125, scalePT )
       
        #print "juhu"
        ret["H_scaled"] = Hscaledpt.M()
        #print "moi"
        ret["A_Hscaled"] = (Zunscaled+Hscaledpt).M()

 
        #BASIC SVFIT
        #print "JEP"
        leg1 = MeasuredTauLepton(l1type, pt3, eta3, phi3, m3, DM3)
        leg2 = MeasuredTauLepton(l2type, pt4, eta4, phi4, m4, DM4)

        measuredLeptons = std.vector('classic_svFit::MeasuredTauLepton')()

        measuredLeptons.push_back(leg1)
        measuredLeptons.push_back(leg2)

        #Here you take the covariance matrix   
        cov00 = event.metcov00
        cov01 = event.metcov01
        cov11 = event.metcov11


        #In reality this should never happen, and might cause issues if it does..
        if cov00 == -9999:
            cov00 = 0
        if cov01 == -9999:
       	    cov01 = 0
        if cov11 == -9999:
       	    cov11 = 0

        metcov = TMatrixD(2, 2)    
        a_metcov = array('d', [cov00, cov01, cov01, cov11])
        metcov.SetMatrixArray(a_metcov)

        #fetch met
        mex = event.met_px
        mey = event.met_py
        metpt = event.met

        #initialize svfit
        svfit = SVfitAlgo(0)

        if self.channel=="EETT" or self.channel=="MMTT":      
            svfit.addLogM_fixed(True, 5.)
        elif self.channel=="EEMT" or self.channel=="MMMT" or self.channel=="EEET" or self.channel=="MMET":
            svfit.addLogM_fixed(True, 4.)
        elif self.channel=="EEEM" or self.channel=="MMEM":
            svfit.addLogM_fixed(True, 3.)

        svfit.setDiTauMassConstraint(-1)
        svfit.integrate(measuredLeptons, mex, mey, metcov)
  

        m_sV = svfit.getHistogramAdapter().getMass()
        pt_sV = svfit.getHistogramAdapter().getPt()
        eta_sV = svfit.getHistogramAdapter().getEta()
        phi_sV =  svfit.getHistogramAdapter().getPhi()

        HsvFit = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit.SetPtEtaPhiM( pt_sV, eta_sV, phi_sV, m_sV )

        ret["H_svFit"] = HsvFit.M()
        ret["A_svFit"] = (Zunscaled+HsvFit).M()

        #scale mass here
        if m_sV!=0.0:
            scale = 125.06/m_sV
        else:
            scale = 0.0
        HsvFit_scaled = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_scaled.SetPtEtaPhiM( scale*pt_sV, eta_sV, phi_sV, scale*m_sV )
         
        ret["H_svFit_scaled"] = HsvFit_scaled.M()
        ret["A_svFit_scaled"] = (Zunscaled+HsvFit_scaled).M()


        massConstraint = 125.06
        svfit.setDiTauMassConstraint(massConstraint)
        svfit.integrate(measuredLeptons, mex, mey, metcov)

        H_constrained = svfit.getHistogramAdapter().getMass()
        pt_sV_constrained = svfit.getHistogramAdapter().getPt()
        eta_sV_constrained = svfit.getHistogramAdapter().getEta()
        phi_sV_constrained =  svfit.getHistogramAdapter().getPhi()
        
        HsvFit_constrained = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_constrained.SetPtEtaPhiM( pt_sV_constrained, eta_sV_constrained, phi_sV_constrained, H_constrained )

        ret["H_svFit_constrained"] = HsvFit_constrained.M()
        ret["A_svFit_constrained"] = (Zunscaled+HsvFit_constrained).M()


        #let us do the variations
        pt3_dm0_up = pt3
        pt3_dm0_dn = pt3
        pt3_dm1_up = pt3
        pt3_dm1_dn = pt3
        pt3_dm10_up = pt3
        pt3_dm10_dn = pt3

        pt4_dm0_up = pt4
        pt4_dm0_dn = pt4
        pt4_dm1_up = pt4
        pt4_dm1_dn = pt4
        pt4_dm10_up = pt4
        pt4_dm10_dn = pt4

        mex_DM0_up = event.met_px_DM0_up
        mey_DM0_up = event.met_py_DM0_up
        mex_DM0_dn = event.met_px_DM0_down
        mey_DM0_dn = event.met_py_DM0_down

        mex_DM1_up = event.met_px_DM1_up
        mey_DM1_up = event.met_py_DM1_up
        mex_DM1_dn = event.met_px_DM1_down
        mey_DM1_dn = event.met_py_DM1_down

        mex_DM10_up = event.met_px_DM10_up
        mey_DM10_up = event.met_py_DM10_up
        mex_DM10_dn = event.met_px_DM10_down
        mey_DM10_dn = event.met_py_DM10_down

        #JEC

	mex_JEC_up = event.met_px_JetEnUp
        mey_JEC_up = event.met_py_JetEnUp
        mex_JEC_dn = event.met_px_JetEnDown
        mey_JEC_dn = event.met_py_JetEnDown

        #UEC

	mex_UEC_up = event.met_px_UncEnUp
        mey_UEC_up = event.met_py_UncEnUp
        mex_UEC_dn = event.met_px_UncEnDown
        mey_UEC_dn = event.met_py_UncEnDown



        #rerun for JEC and UEC
        ret["H_LT_JEC_up"] = pt3+pt4
        ret["H_LT_JEC_dn"] = pt3+pt4
        ret["H_LT_UEC_up"] = pt3+pt4
        ret["H_LT_UEC_dn"] = pt3+pt4

        ret["H_vis_JEC_up"] = mH
        ret["H_vis_JEC_dn"] = mH
        ret["H_vis_UEC_up"] = mH
        ret["H_vis_UEC_dn"] = mH


        ret["A_vis_JEC_up"] = mA
        ret["A_vis_JEC_dn"] = mA
        ret["A_vis_UEC_up"] = mA
        ret["A_vis_UEC_dn"] = mA


        svfit_JEC_up = SVfitAlgo(0)
        svfit_JEC_dn = SVfitAlgo(0)
        svfit_UEC_up = SVfitAlgo(0)
        svfit_UEC_dn = SVfitAlgo(0)

        svfit_DM0_up = SVfitAlgo(0)
        svfit_DM0_dn = SVfitAlgo(0)
        svfit_DM1_up = SVfitAlgo(0)
        svfit_DM1_dn = SVfitAlgo(0)
        svfit_DM10_up = SVfitAlgo(0)
        svfit_DM10_dn = SVfitAlgo(0)

        if self.channel=="EETT" or self.channel=="MMTT":
            svfit_JEC_up.addLogM_fixed(True, 5.)
            svfit_JEC_dn.addLogM_fixed(True, 5.)
            svfit_UEC_up.addLogM_fixed(True, 5.)
            svfit_UEC_dn.addLogM_fixed(True, 5.)
            svfit_DM0_up.addLogM_fixed(True, 5.)
            svfit_DM0_dn.addLogM_fixed(True, 5.)
            svfit_DM1_up.addLogM_fixed(True, 5.)
            svfit_DM1_dn.addLogM_fixed(True, 5.)
            svfit_DM10_up.addLogM_fixed(True, 5.)
            svfit_DM10_dn.addLogM_fixed(True, 5.)
        elif self.channel=="EEMT" or self.channel=="MMMT" or self.channel=="EEET" or self.channel=="MMET":
            svfit_JEC_up.addLogM_fixed(True, 4.)
            svfit_JEC_dn.addLogM_fixed(True, 4.)
            svfit_UEC_up.addLogM_fixed(True, 4.)
            svfit_UEC_dn.addLogM_fixed(True, 4.)
            svfit_DM0_up.addLogM_fixed(True, 4.)
            svfit_DM0_dn.addLogM_fixed(True, 4.)
            svfit_DM1_up.addLogM_fixed(True, 4.)
            svfit_DM1_dn.addLogM_fixed(True, 4.)
            svfit_DM10_up.addLogM_fixed(True, 4.)
            svfit_DM10_dn.addLogM_fixed(True, 4.)
        elif self.channel=="EEEM" or self.channel=="MMEM":
            svfit_JEC_up.addLogM_fixed(True, 3.)
            svfit_JEC_dn.addLogM_fixed(True, 3.)
            svfit_UEC_up.addLogM_fixed(True, 3.)
            svfit_UEC_dn.addLogM_fixed(True, 3.)
            svfit_DM0_up.addLogM_fixed(True, 3.)
            svfit_DM0_dn.addLogM_fixed(True, 3.)
            svfit_DM1_up.addLogM_fixed(True, 3.)
            svfit_DM1_dn.addLogM_fixed(True, 3.)
            svfit_DM10_up.addLogM_fixed(True, 3.)
            svfit_DM10_dn.addLogM_fixed(True, 3.)


        svfit_JEC_up.integrate(measuredLeptons, mex_JEC_up, mey_JEC_up, metcov)
        svfit_JEC_dn.integrate(measuredLeptons, mex_JEC_dn, mey_JEC_dn, metcov)
        svfit_UEC_up.integrate(measuredLeptons, mex_UEC_up, mey_UEC_up, metcov)
        svfit_UEC_dn.integrate(measuredLeptons, mex_UEC_dn, mey_UEC_dn, metcov)

        HsvFit_JEC_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_JEC_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_UEC_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_UEC_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )

        HsvFit_JEC_up.SetPtEtaPhiM( svfit_JEC_up.getHistogramAdapter().getPt(), svfit_JEC_up.getHistogramAdapter().getEta(), svfit_JEC_up.getHistogramAdapter().getPhi(), svfit_JEC_up.getHistogramAdapter().getMass() )
        HsvFit_JEC_dn.SetPtEtaPhiM( svfit_JEC_dn.getHistogramAdapter().getPt(), svfit_JEC_dn.getHistogramAdapter().getEta(), svfit_JEC_dn.getHistogramAdapter().getPhi(), svfit_JEC_dn.getHistogramAdapter().getMass() )
        HsvFit_UEC_up.SetPtEtaPhiM( svfit_UEC_up.getHistogramAdapter().getPt(), svfit_UEC_up.getHistogramAdapter().getEta(), svfit_UEC_up.getHistogramAdapter().getPhi(), svfit_UEC_up.getHistogramAdapter().getMass() )
        HsvFit_UEC_dn.SetPtEtaPhiM( svfit_UEC_dn.getHistogramAdapter().getPt(), svfit_UEC_dn.getHistogramAdapter().getEta(), svfit_UEC_dn.getHistogramAdapter().getPhi(), svfit_UEC_dn.getHistogramAdapter().getMass() )

        ret["H_svFit_JEC_up"] = HsvFit_JEC_up.M()
        ret["H_svFit_JEC_dn"] = HsvFit_JEC_dn.M()
        ret["H_svFit_UEC_up"] = HsvFit_UEC_up.M()
        ret["H_svFit_UEC_dn"] = HsvFit_UEC_dn.M()

        ret["A_svFit_JEC_up"] = (Zunscaled+HsvFit_JEC_up).M()
        ret["A_svFit_JEC_dn"] = (Zunscaled+HsvFit_JEC_dn).M()
        ret["A_svFit_UEC_up"] = (Zunscaled+HsvFit_UEC_up).M()
        ret["A_svFit_UEC_dn"] = (Zunscaled+HsvFit_UEC_dn).M()


        svfit_JEC_up.setDiTauMassConstraint(massConstraint);
        svfit_JEC_dn.setDiTauMassConstraint(massConstraint);
        svfit_UEC_up.setDiTauMassConstraint(massConstraint);
        svfit_UEC_dn.setDiTauMassConstraint(massConstraint);

        svfit_JEC_up.integrate(measuredLeptons, mex_JEC_up, mey_JEC_up, metcov)
        svfit_JEC_dn.integrate(measuredLeptons, mex_JEC_dn, mey_JEC_dn, metcov)
        svfit_UEC_up.integrate(measuredLeptons, mex_UEC_up, mey_UEC_up, metcov)
        svfit_UEC_dn.integrate(measuredLeptons, mex_UEC_dn, mey_UEC_dn, metcov)


        HsvFit_constrained_JEC_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_constrained_JEC_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_constrained_UEC_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        HsvFit_constrained_UEC_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )

        HsvFit_constrained_JEC_up.SetPtEtaPhiM( svfit_JEC_up.getHistogramAdapter().getPt(), svfit_JEC_up.getHistogramAdapter().getEta(), svfit_JEC_up.getHistogramAdapter().getPhi(), svfit_JEC_up.getHistogramAdapter().getMass() )
        HsvFit_constrained_JEC_dn.SetPtEtaPhiM( svfit_JEC_dn.getHistogramAdapter().getPt(), svfit_JEC_dn.getHistogramAdapter().getEta(), svfit_JEC_dn.getHistogramAdapter().getPhi(), svfit_JEC_dn.getHistogramAdapter().getMass() )
        HsvFit_constrained_UEC_up.SetPtEtaPhiM( svfit_UEC_up.getHistogramAdapter().getPt(), svfit_UEC_up.getHistogramAdapter().getEta(), svfit_UEC_up.getHistogramAdapter().getPhi(), svfit_UEC_up.getHistogramAdapter().getMass() )
        HsvFit_constrained_UEC_dn.SetPtEtaPhiM( svfit_UEC_dn.getHistogramAdapter().getPt(), svfit_UEC_dn.getHistogramAdapter().getEta(), svfit_UEC_dn.getHistogramAdapter().getPhi(), svfit_UEC_dn.getHistogramAdapter().getMass() )

        ret["H_svFit_constrained_JEC_up"] = HsvFit_constrained_JEC_up.M()
        ret["H_svFit_constrained_JEC_dn"] = HsvFit_constrained_JEC_dn.M()
        ret["H_svFit_constrained_UEC_up"] = HsvFit_constrained_UEC_up.M()
        ret["H_svFit_constrained_UEC_dn"] = HsvFit_constrained_UEC_dn.M()

        ret["A_svFit_constrained_JEC_up"] = (Zunscaled+HsvFit_constrained_JEC_up).M()
        ret["A_svFit_constrained_JEC_dn"] = (Zunscaled+HsvFit_constrained_JEC_dn).M()
        ret["A_svFit_constrained_UEC_up"] = (Zunscaled+HsvFit_constrained_UEC_up).M()
        ret["A_svFit_constrained_UEC_dn"] = (Zunscaled+HsvFit_constrained_UEC_dn).M()


        if self.channel in ["EEET", "MMET", "EEMT", "MMMT", "EETT", "MMTT"] and genmatch4==5:
            if DM4==0:
                pt4_dm0_up = event.pt_TES_up_4
                pt4_dm0_dn = event.pt_TES_down_4
            elif DM4==1:
                pt4_dm1_up = event.pt_TES_up_4
                pt4_dm1_dn = event.pt_TES_down_4
            elif DM4==10:
                pt4_dm10_up = event.pt_TES_up_4
                pt4_dm10_dn = event.pt_TES_down_4
        if self.channel in ["EETT", "MMTT"] and genmatch3==5:
            if DM3==0:
                pt3_dm0_up = event.pt_TES_up_3
                pt3_dm0_dn = event.pt_TES_down_3
            elif DM3==1:
                pt3_dm1_up = event.pt_TES_up_3
                pt3_dm1_dn = event.pt_TES_down_3
            elif DM3==10:
                pt3_dm10_up = event.pt_TES_up_3
                pt3_dm10_dn = event.pt_TES_down_3


        ret["H_LT_DM0_up"]= pt3_dm0_up+pt4_dm0_up
        ret["H_LT_DM0_dn"]= pt3_dm0_dn+pt4_dm0_dn
        ret["H_LT_DM1_up"]= pt3_dm1_up+pt4_dm1_up
        ret["H_LT_DM1_dn"]= pt3_dm1_dn+pt4_dm1_dn
        ret["H_LT_DM10_up"]= pt3_dm10_up+pt4_dm10_up
        ret["H_LT_DM10_dn"]= pt3_dm10_dn+pt4_dm10_dn

        #make here the visible masses for H and A
        tau3_DM0_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM0_up.SetPtEtaPhiM( pt3_dm0_up, eta3, phi3, m3)
        tau3_DM0_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM0_dn.SetPtEtaPhiM( pt3_dm0_dn, eta3, phi3, m3)

        tau3_DM1_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM1_up.SetPtEtaPhiM( pt3_dm1_up, eta3, phi3, m3)
        tau3_DM1_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM1_dn.SetPtEtaPhiM( pt3_dm1_dn, eta3, phi3, m3)

        tau3_DM10_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM10_up.SetPtEtaPhiM( pt3_dm10_up, eta3, phi3, m3)
        tau3_DM10_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau3_DM10_dn.SetPtEtaPhiM( pt3_dm10_dn, eta3, phi3, m3)

        tau4_DM0_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM0_up.SetPtEtaPhiM( pt4_dm0_up, eta4, phi4, m4)
        tau4_DM0_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM0_dn.SetPtEtaPhiM( pt4_dm0_dn, eta4, phi4, m4)

        tau4_DM1_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM1_up.SetPtEtaPhiM( pt4_dm1_up, eta4, phi4, m4)
        tau4_DM1_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM1_dn.SetPtEtaPhiM( pt4_dm1_dn, eta4, phi4, m4)

        tau4_DM10_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM10_up.SetPtEtaPhiM( pt4_dm10_up, eta4, phi4, m4)
        tau4_DM10_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
        tau4_DM10_dn.SetPtEtaPhiM( pt4_dm10_dn, eta4, phi4, m4)

        ret["H_vis_DM0_up"]= (tau3_DM0_up+tau4_DM0_up).M()
        ret["H_vis_DM0_dn"]= (tau3_DM0_dn+tau4_DM0_dn).M()
        ret["H_vis_DM1_up"]= (tau3_DM1_up+tau4_DM1_up).M()
        ret["H_vis_DM1_dn"]= (tau3_DM1_dn+tau4_DM1_dn).M()
        ret["H_vis_DM10_up"]= (tau3_DM10_up+tau4_DM10_up).M()
        ret["H_vis_DM10_dn"]= (tau3_DM10_dn+tau4_DM10_dn).M()

        ret["A_vis_DM0_up"]= (Zunscaled+tau3_DM0_up+tau4_DM0_up).M()
        ret["A_vis_DM0_dn"]= (Zunscaled+tau3_DM0_dn+tau4_DM0_dn).M()
        ret["A_vis_DM1_up"]= (Zunscaled+tau3_DM1_up+tau4_DM1_up).M()
        ret["A_vis_DM1_dn"]= (Zunscaled+tau3_DM1_dn+tau4_DM1_dn).M()
        ret["A_vis_DM10_up"]= (Zunscaled+tau3_DM10_up+tau4_DM10_up).M()
        ret["A_vis_DM10_dn"]= (Zunscaled+tau3_DM10_dn+tau4_DM10_dn).M()        


        l3_DM0_nominal = 0
        l3_DM1_nominal = 0
        l3_DM10_nominal = 0

        l4_DM0_nominal = 0
        l4_DM1_nominal = 0
        l4_DM10_nominal = 0

        if self.channel in ["EETT", "MMTT"] and genmatch3==5:
            if DM3 == 0:
                l3_DM1_nominal = 1
                l3_DM10_nominal = 1
            elif DM3 == 1:
                l3_DM0_nominal = 1
                l3_DM10_nominal =  1
            elif DM3 == 10:
                l3_DM0_nominal = 1
                l3_DM1_nominal = 1
        else:
            l3_DM0_nominal = 1
            l3_DM1_nominal = 1
            l3_DM10_nominal = 1

        if self.channel in ["EEET", "MMET", "EEMT", "MMMT", "EETT", "MMTT"] and genmatch4==5:
            if DM4==0:
                l4_DM1_nominal = 1
                l4_DM10_nominal = 1
            elif DM4==1:
                l4_DM0_nominal = 1
                l4_DM10_nominal = 1
            elif DM4==10:
                l4_DM0_nominal = 1
                l4_DM1_nominal = 1
        else:
            l4_DM0_nominal = 1
            l4_DM1_nominal = 1
            l4_DM10_nominal = 1


        if l3_DM0_nominal == 0 or l4_DM0_nominal==0:
            leg1_dm0_up = MeasuredTauLepton(l1type, pt3_dm0_up, eta3, phi3, m3, DM3)
            leg2_dm0_up = MeasuredTauLepton(l2type, pt4_dm0_up, eta4, phi4, m4, DM4)
            measuredLeptons_DM0_up = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM0_up.push_back(leg2_dm0_up)
            measuredLeptons_DM0_up.push_back(leg1_dm0_up)

            svfit_DM0_up.integrate(measuredLeptons_DM0_up, mex_DM0_up, mey_DM0_up, metcov)
            HsvFit_DM0_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM0_up.SetPtEtaPhiM( svfit_DM0_up.getHistogramAdapter().getPt(), svfit_DM0_up.getHistogramAdapter().getEta(), svfit_DM0_up.getHistogramAdapter().getPhi(), svfit_DM0_up.getHistogramAdapter().getMass() )

            ret["H_svFit_DM0_up"] = HsvFit_DM0_up.M()
            ret["A_svFit_DM0_up"] = (Zunscaled+HsvFit_DM0_up).M()

            svfit_DM0_up.setDiTauMassConstraint(massConstraint);
            svfit_DM0_up.integrate(measuredLeptons_DM0_up, mex_DM0_up, mey_DM0_up, metcov)

            HsvFit_constrained_DM0_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM0_up.SetPtEtaPhiM( svfit_DM0_up.getHistogramAdapter().getPt(), svfit_DM0_up.getHistogramAdapter().getEta(), svfit_DM0_up.getHistogramAdapter().getPhi(), svfit_DM0_up.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM0_up"] = HsvFit_constrained_DM0_up.M()
            ret["A_svFit_constrained_DM0_up"] = (Zunscaled+HsvFit_constrained_DM0_up).M()


            leg1_dm0_dn = MeasuredTauLepton(l1type, pt3_dm0_dn, eta3, phi3, m3, DM3)
            leg2_dm0_dn = MeasuredTauLepton(l2type, pt4_dm0_dn, eta4, phi4, m4, DM4)
            measuredLeptons_DM0_dn = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM0_dn.push_back(leg2_dm0_dn)
            measuredLeptons_DM0_dn.push_back(leg1_dm0_dn)

            svfit_DM0_dn.integrate(measuredLeptons_DM0_dn, mex_DM0_dn, mey_DM0_dn, metcov)
            HsvFit_DM0_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM0_dn.SetPtEtaPhiM( svfit_DM0_dn.getHistogramAdapter().getPt(), svfit_DM0_dn.getHistogramAdapter().getEta(), svfit_DM0_dn.getHistogramAdapter().getPhi(), svfit_DM0_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_DM0_dn"] = HsvFit_DM0_dn.M()
            ret["A_svFit_DM0_dn"] = (Zunscaled+HsvFit_DM0_dn).M()

            svfit_DM0_dn.setDiTauMassConstraint(massConstraint);
            svfit_DM0_dn.integrate(measuredLeptons_DM0_dn, mex_DM0_dn, mey_DM0_dn, metcov)

            HsvFit_constrained_DM0_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM0_dn.SetPtEtaPhiM( svfit_DM0_dn.getHistogramAdapter().getPt(), svfit_DM0_dn.getHistogramAdapter().getEta(), svfit_DM0_dn.getHistogramAdapter().getPhi(), svfit_DM0_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM0_dn"] = HsvFit_constrained_DM0_dn.M()
            ret["A_svFit_constrained_DM0_dn"] = (Zunscaled+HsvFit_constrained_DM0_dn).M()
        else:
            ret["H_svFit_DM0_up"] = HsvFit.M()
            ret["H_svFit_DM0_dn"] = HsvFit.M()
            ret["A_svFit_DM0_up"] = (Zunscaled+HsvFit).M()
            ret["A_svFit_DM0_dn"] = (Zunscaled+HsvFit).M()
            ret["H_svFit_constrained_DM0_up"] = HsvFit_constrained.M()
            ret["H_svFit_constrained_DM0_dn"] = HsvFit_constrained.M()
            ret["A_svFit_constrained_DM0_up"] = (Zunscaled+HsvFit_constrained).M()
            ret["A_svFit_constrained_DM0_dn"] = (Zunscaled+HsvFit_constrained).M()

        if l3_DM1_nominal == 0 or l4_DM1_nominal==0:
            leg1_dm1_up = MeasuredTauLepton(l1type, pt3_dm1_up, eta3, phi3, m3, DM3)
            leg2_dm1_up = MeasuredTauLepton(l2type, pt4_dm1_up, eta4, phi4, m4, DM4)
            measuredLeptons_DM1_up = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM1_up.push_back(leg2_dm1_up)
            measuredLeptons_DM1_up.push_back(leg1_dm1_up)

            svfit_DM1_up.integrate(measuredLeptons_DM1_up, mex_DM1_up, mey_DM1_up, metcov)
            HsvFit_DM1_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM1_up.SetPtEtaPhiM( svfit_DM1_up.getHistogramAdapter().getPt(), svfit_DM1_up.getHistogramAdapter().getEta(), svfit_DM1_up.getHistogramAdapter().getPhi(), svfit_DM1_up.getHistogramAdapter().getMass() )

            ret["H_svFit_DM1_up"] = HsvFit_DM1_up.M()
            ret["A_svFit_DM1_up"] = (Zunscaled+HsvFit_DM1_up).M()

            svfit_DM1_up.setDiTauMassConstraint(massConstraint);
            svfit_DM1_up.integrate(measuredLeptons_DM1_up, mex_DM1_up, mey_DM1_up, metcov)

            HsvFit_constrained_DM1_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM1_up.SetPtEtaPhiM( svfit_DM1_up.getHistogramAdapter().getPt(), svfit_DM1_up.getHistogramAdapter().getEta(), svfit_DM1_up.getHistogramAdapter().getPhi(), svfit_DM1_up.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM1_up"] = HsvFit_constrained_DM1_up.M()
            ret["A_svFit_constrained_DM1_up"] = (Zunscaled+HsvFit_constrained_DM1_up).M()


            leg1_dm1_dn = MeasuredTauLepton(l1type, pt3_dm1_dn, eta3, phi3, m3, DM3)
            leg2_dm1_dn = MeasuredTauLepton(l2type, pt4_dm1_dn, eta4, phi4, m4, DM4)
            measuredLeptons_DM1_dn = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM1_dn.push_back(leg2_dm1_dn)
            measuredLeptons_DM1_dn.push_back(leg1_dm1_dn)

            svfit_DM1_dn.integrate(measuredLeptons_DM1_dn, mex_DM1_dn, mey_DM1_dn, metcov)
            HsvFit_DM1_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM1_dn.SetPtEtaPhiM( svfit_DM1_dn.getHistogramAdapter().getPt(), svfit_DM1_dn.getHistogramAdapter().getEta(), svfit_DM1_dn.getHistogramAdapter().getPhi(), svfit_DM1_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_DM1_dn"] = HsvFit_DM1_dn.M()
            ret["A_svFit_DM1_dn"] = (Zunscaled+HsvFit_DM1_dn).M()

            svfit_DM1_dn.setDiTauMassConstraint(massConstraint);
            svfit_DM1_dn.integrate(measuredLeptons_DM1_dn, mex_DM1_dn, mey_DM1_dn, metcov)

            HsvFit_constrained_DM1_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM1_dn.SetPtEtaPhiM( svfit_DM1_dn.getHistogramAdapter().getPt(), svfit_DM1_dn.getHistogramAdapter().getEta(), svfit_DM1_dn.getHistogramAdapter().getPhi(), svfit_DM1_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM1_dn"] = HsvFit_constrained_DM1_dn.M()
            ret["A_svFit_constrained_DM1_dn"] = (Zunscaled+HsvFit_constrained_DM1_dn).M()
        else:
            ret["H_svFit_DM1_up"] = HsvFit.M()
            ret["H_svFit_DM1_dn"] = HsvFit.M()
            ret["A_svFit_DM1_up"] = (Zunscaled+HsvFit).M()
            ret["A_svFit_DM1_dn"] = (Zunscaled+HsvFit).M()
            ret["H_svFit_constrained_DM1_up"] = HsvFit_constrained.M()
            ret["H_svFit_constrained_DM1_dn"] = HsvFit_constrained.M()
            ret["A_svFit_constrained_DM1_up"] = (Zunscaled+HsvFit_constrained).M()
            ret["A_svFit_constrained_DM1_dn"] = (Zunscaled+HsvFit_constrained).M()

        if l3_DM10_nominal == 0 or l4_DM10_nominal==0:
            leg1_dm10_up = MeasuredTauLepton(l1type, pt3_dm10_up, eta3, phi3, m3, DM3)
            leg2_dm10_up = MeasuredTauLepton(l2type, pt4_dm10_up, eta4, phi4, m4, DM4)
            measuredLeptons_DM10_up = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM10_up.push_back(leg2_dm10_up)
            measuredLeptons_DM10_up.push_back(leg1_dm10_up)

            svfit_DM10_up.integrate(measuredLeptons_DM10_up, mex_DM10_up, mey_DM10_up, metcov)
            HsvFit_DM10_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM10_up.SetPtEtaPhiM( svfit_DM10_up.getHistogramAdapter().getPt(), svfit_DM10_up.getHistogramAdapter().getEta(), svfit_DM10_up.getHistogramAdapter().getPhi(), svfit_DM10_up.getHistogramAdapter().getMass() )

            ret["H_svFit_DM10_up"] = HsvFit_DM10_up.M()
            ret["A_svFit_DM10_up"] = (Zunscaled+HsvFit_DM10_up).M()

            svfit_DM10_up.setDiTauMassConstraint(massConstraint);
            svfit_DM10_up.integrate(measuredLeptons_DM10_up, mex_DM10_up, mey_DM10_up, metcov)

            HsvFit_constrained_DM10_up = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM10_up.SetPtEtaPhiM( svfit_DM10_up.getHistogramAdapter().getPt(), svfit_DM10_up.getHistogramAdapter().getEta(), svfit_DM10_up.getHistogramAdapter().getPhi(), svfit_DM10_up.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM10_up"] = HsvFit_constrained_DM10_up.M()
            ret["A_svFit_constrained_DM10_up"] = (Zunscaled+HsvFit_constrained_DM10_up).M()


            leg1_dm10_dn = MeasuredTauLepton(l1type, pt3_dm10_dn, eta3, phi3, m3, DM3)
            leg2_dm10_dn = MeasuredTauLepton(l2type, pt4_dm10_dn, eta4, phi4, m4, DM4)
            measuredLeptons_DM10_dn = std.vector('classic_svFit::MeasuredTauLepton')()
            measuredLeptons_DM10_dn.push_back(leg2_dm10_dn)
            measuredLeptons_DM10_dn.push_back(leg1_dm10_dn)

            svfit_DM10_dn.integrate(measuredLeptons_DM10_dn, mex_DM10_dn, mey_DM10_dn, metcov)
            HsvFit_DM10_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_DM10_dn.SetPtEtaPhiM( svfit_DM10_dn.getHistogramAdapter().getPt(), svfit_DM10_dn.getHistogramAdapter().getEta(), svfit_DM10_dn.getHistogramAdapter().getPhi(), svfit_DM10_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_DM10_dn"] = HsvFit_DM10_dn.M()
            ret["A_svFit_DM10_dn"] = (Zunscaled+HsvFit_DM10_dn).M()

            svfit_DM10_dn.setDiTauMassConstraint(massConstraint);
            svfit_DM10_dn.integrate(measuredLeptons_DM10_dn, mex_DM10_dn, mey_DM10_dn, metcov)

            HsvFit_constrained_DM10_dn = ROOT.TLorentzVector( 0.,0.,0.,0. )
            HsvFit_constrained_DM10_dn.SetPtEtaPhiM( svfit_DM10_dn.getHistogramAdapter().getPt(), svfit_DM10_dn.getHistogramAdapter().getEta(), svfit_DM10_dn.getHistogramAdapter().getPhi(), svfit_DM10_dn.getHistogramAdapter().getMass() )

            ret["H_svFit_constrained_DM10_dn"] = HsvFit_constrained_DM10_dn.M()
            ret["A_svFit_constrained_DM10_dn"] = (Zunscaled+HsvFit_constrained_DM10_dn).M()
        else:
            ret["H_svFit_DM10_up"] = HsvFit.M()
            ret["H_svFit_DM10_dn"] = HsvFit.M()
            ret["A_svFit_DM10_up"] = (Zunscaled+HsvFit).M()
            ret["A_svFit_DM10_dn"] = (Zunscaled+HsvFit).M()
            ret["H_svFit_constrained_DM10_up"] = HsvFit_constrained.M()
            ret["H_svFit_constrained_DM10_dn"] = HsvFit_constrained.M()
            ret["A_svFit_constrained_DM10_up"] = (Zunscaled+HsvFit_constrained).M()
            ret["A_svFit_constrained_DM10_dn"] = (Zunscaled+HsvFit_constrained).M()
  


        return ret


###MODULES = [ ( 'svFit_classicEETT', lambda : svFit_classic("EETT") ), ]
MODULES = [
 ( 'svFit_classicEETT', lambda : svFit_classic("EETT") ),
 ( 'svFit_classicEEET', lambda : svFit_classic("EEET") ),
 ( 'svFit_classicEEEM', lambda : svFit_classic("EEEM") ),
 ( 'svFit_classicEEMT', lambda : svFit_classic("EEMT") ),
 ( 'svFit_classicMMTT', lambda : svFit_classic("MMTT") ),
 ( 'svFit_classicMMET', lambda : svFit_classic("MMET") ),
 ( 'svFit_classicMMEM', lambda : svFit_classic("MMEM") ),
 ( 'svFit_classicMMMT', lambda : svFit_classic("MMMT") ) ]


if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = svFit_classic()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d" % (ev.run, ev.lumi, ev.evt)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)



