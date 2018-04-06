#import os
#import array

#from array import array
from ROOT import TMatrixD, std, TFile, TH1

#from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from CMGTools.SVfitStandalone.SVfitStandaloneAlgorithm import SVfitAlgo
from CMGTools.SVfitStandalone.MeasuredTauLepton import measuredTauLepton

#TH1.AddDirectory(False)

import os
import array

from CMGTools.TTHAnalysis.treeReAnalyzer import *

class svFit:
    def __init__(self):
        self.branches = [ "H_scaled", "H_vis" ]

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

        leg1 = measuredTauLepton(l1type, pt3, eta3, phi3, m3, DM3)
        leg2 = measuredTauLepton(l2type, pt4, eta4, phi4, m4, DM4)

        measuredLeptons = std.vector('svFitStandalone::MeasuredTauLepton')()

        #print "measuredLeptons"
        #print measuredLeptons

        ## RIC: not really needed since SVfit internally sorts the inputs
        #if hasattr(self.cfg_ana, 'order') and self.cfg_ana.order == '12':
        #    measuredLeptons.push_back(leg1)
        #    measuredLeptons.push_back(leg2)
        #else:
        measuredLeptons.push_back(leg2)
        measuredLeptons.push_back(leg1)

        metcov = TMatrixD(2, 2)
    
        a_metcov = array('d', [787.352, -178.63, -178.63, 179.545])
        #a_metcov.append(-178.63)
        #a_metcov.append(-178.63)
        #a_metcov.append(179.545)
     
        
        ##print "matrix toimi"
        metcov.SetMatrixArray(a_metcov)

        mex = event.met_px
        mey = event.met_py

        svfit = SVfitAlgo(measuredLeptons, mex, mey, metcov, False)


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

        #if self.cfg_ana.integration == 'VEGAS':
        svfit.integrateVEGAS()
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
        ret["H_scaled"] = svfit.mass()
        ret["H_vis"] = mH
        #event.diLepton.svfitMassError = svfit.massUncert
        #event.diLepton.svfitTransverseMass = svfit.transverseMass

        # add also the pt, eta and phi as computed by SVfit
        #if self.cfg_ana.integration == 'MarkovChain':
        #    event.diLepton.svfitPt = svfit.pt
        #    event.diLepton.svfitPtError = svfit.ptUncert
        #    event.diLepton.svfitEta = svfit.eta
        #    event.diLepton.svfitPhi = svfit.phi
        #    event.diLepton.svfitMET = svfit.fittedMET
        #    event.diLepton.svfitTaus = svfit.fittedTauLeptons

        print "ennen ja jalkeen :",mH,svfit.mass()

        #ret["A_scaled"] = 3.0

        return ret


MODULES = [ ( 'svFit', lambda : svFit() ), ]

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = svFit()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d" % (ev.run, ev.lumi, ev.evt)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)



