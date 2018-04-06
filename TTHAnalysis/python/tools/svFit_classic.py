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
    def __init__(self):
        self.branches = [ "H_scaled", "H_vis", "H_constrained" ]

    def listBranches(self):
        return self.branches[:]

    def __call__(self,event):
        #(met, metphi)  = event.met, event.met_phi
        # prepare output
        ret = dict([(name,0.0) for name in self.branches])


        #H legs
        pt3 = event.pt_3
        eta3 = event.eta_3
        phi3 = event.phi_3
        m3 = event.m_3
        DM3 = int(event.decayMode_3)

        pt4 = event.pt_4
        eta4 = event.eta_4
        phi4 = event.phi_4
        m4 = event.m_4
        DM4 = int(event.decayMode_4)

        mH = event.H_vis

        #catch types
        l1type = 1
        l2type = 1

        #svfit part
        #print "MOI JAANA"

        #print pt4, eta4, phi4, m4, DM4

        leg1 = MeasuredTauLepton(l1type, pt3, eta3, phi3, m3, DM3)
        leg2 = MeasuredTauLepton(l2type, pt4, eta4, phi4, m4, DM4)

        #print "juhuu"

        measuredLeptons = std.vector('classic_svFit::MeasuredTauLepton')()
        #print "measuredLeptons"
        #print measuredLeptons

        ## RIC: not really needed since SVfit internally sorts the inputs
        #if hasattr(self.cfg_ana, 'order') and self.cfg_ana.order == '12':
        #    measuredLeptons.push_back(leg1)
        #    measuredLeptons.push_back(leg2)
        #else:
        measuredLeptons.push_back(leg2)
        measuredLeptons.push_back(leg1)

        #      print measuredLeptons        

        metcov = TMatrixD(2, 2)
    
        a_metcov = array('d', [787.352, -178.63, -178.63, 179.545])
        #a_metcov.append(-178.63)
        #a_metcov.append(-178.63)
        #a_metcov.append(179.545)
     
        
        #print "matrix toimi"
        metcov.SetMatrixArray(a_metcov)

        mex = event.met_px
        mey = event.met_py

        svfit = SVfitAlgo(0)

        #print "svfit ok"
        #if hasattr(self.cfg_ana, 'integrateOverVisPtResponse') and \
        #    self.cfg_ana.integrateOverVisPtResponse:

        #    shift = not((self.cfg_ana.l1type == 'tau' and     \
        #                 leg1.decayMode() not in [0, 1, 10]) or \
        #                (self.cfg_ana.l2type == 'tau' and     \
        #                 leg2.decayMode() not in [0, 1, 10]))
        #    svfit.shiftVisPt(shift, self.inputFile_visPtResolution)

        # add an additional logM(tau,tau) term to the nll
        # to suppress tails on M(tau,tau) (default is false)
        # svfit.addLogM(False)
      
        svfit.addLogM_fixed(True, 5.)
        #//svFitAlgo.addLogM_dynamic(true, "(m/1000.)*15.");
        #//svFitAlgo.setMaxObjFunctionCalls(100000); // CV: default is 100000 evaluations of integrand per event
        #svFitAlgo.setLikelihoodFileName("testClassicSVfit.root");  
        ##svfit.setDiTauMassConstraint(-1);

        #if self.cfg_ana.integration == 'VEGAS':
        svfit.integrate(measuredLeptons, mex, mey, metcov)

        #elif self.cfg_ana.integration == 'MarkovChain':
        #    svfit.integrateMarkovChain()
        #else:
        #    print 'The integration method must be defined in the cfg as "integration".'
        #    print 'Options: [VEGAS, MarkovChain]'
        #    raise

        # debug
        #if self.cfg_ana.verbose:
        #    if abs(event.diLepton.svfitMass()-svfit.mass()) > 0.01:
        #        print 'WARNING: run {RUN}, lumi {LUMI}, event {EVT}'.format(RUN=str(event.run),
        #                                                                    LUMI=str(event.lumi),
        #                                                                    EVT=str(event.eventId))
        #        print 'precomputed svfit mass   ', event.diLepton.svfitMass()
        #        print 'svfit mass computed here ', svfit.mass()

        # method override
        H_scaled = svfit.getHistogramAdapter().getMass()
        ret["H_scaled"] = H_scaled
        ret["H_vis"] = mH
        #event.diLepton.svfitMassError = svfit.massUncert
        #event.diLepton.svfitTransverseMass = svfit.transverseMass

        massConstraint = 125.06
        svfit.setDiTauMassConstraint(massConstraint);
        svfit.integrate(measuredLeptons, mex, mey, metcov)
        H_constrained = svfit.getHistogramAdapter().getMass()
        
        ret["H_constrained"] = H_constrained
        # add also the pt, eta and phi as computed by SVfit
        #if self.cfg_ana.integration == 'MarkovChain':
        #    event.diLepton.svfitPt = svfit.pt
        #    event.diLepton.svfitPtError = svfit.ptUncert
        #    event.diLepton.svfitEta = svfit.eta
        #    event.diLepton.svfitPhi = svfit.phi
        #    event.diLepton.svfitMET = svfit.fittedMET
        #    event.diLepton.svfitTaus = svfit.fittedTauLeptons

        print "ennen ja jalkeen ja jalkeen constrained:",mH,H_scaled,H_constrained

        #ret["A_scaled"] = 3.0

        return ret


MODULES = [ ( 'svFit_classic', lambda : svFit_classic() ), ]

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



