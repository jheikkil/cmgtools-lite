
import ROOT
import copy
import math

from itertools import product
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon
from PhysicsTools.Heppy.physicsobjects.Electron import Electron
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2, deltaPhi
from PhysicsTools.Heppy.physicsobjects.Particle import Particle
from CMGTools.H2TauTau.proto.analyzers.HTTGenAnalyzer import HTTGenAnalyzer




import pprint
import itertools


class TauScaler(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(TauScaler,self).__init__(cfg_ana,cfg_comp,looperName)
        self.dataName = getattr(self.cfg_comp, "name", None)

    def declareHandles(self):
        super(TauScaler, self).declareHandles()

        self.mchandles['genParticles'] = AutoHandle('prunedGenParticles', 'std::vector<reco::GenParticle')


    def process(self, event):

        #read collection and map necessary objects

        super(TauScaler, self).readCollections(event.input)

        event.goodVertices = event.vertices

        genParticles = self.mchandles['genParticles'].product()
        ptSelGentauleps = [p for p in genParticles if abs(p.pdgId()) in [11, 13] and p.statusFlags().isDirectPromptTauDecayProduct() and p.pt() > 8.]
        ptSelGenleps = [p for p in genParticles if abs(p.pdgId()) in [11, 13] and p.statusFlags().isPrompt() and p.pt() > 8.]
        event.gentaus = [p for p in event.genParticles if abs(p.pdgId()) == 15 and p.statusFlags().isPrompt() and not any(abs(HTTGenAnalyzer.getFinalTau(p).daughter(i_d).pdgId()) in [11, 13] for i_d in xrange(HTTGenAnalyzer.getFinalTau(p).numberOfDaughters()))]


        # scale leptons
        for tau in event.taus:
            self.Scale(tau, ptSelGentauleps, ptSelGenleps, event)
            event.met.setP4(event.met.p4()-(tau.p4()-tau.unscaledP4))
            tau.TES_downP4 = copy.deepcopy(tau.p4())
            tau.TES_upP4 = copy.deepcopy(tau.p4())
            if (abs(tau.p4().pt()-tau.unscaledP4.pt())>1e-5) and tau.gen_match==5:
                tau.TES_downP4 *= 0.988
                tau.TES_upP4 *= 1.012

        #for each tec, create the uncertainty
        taus_DM0  = [tau for tau in event.taus if tau.decayMode() == 0 and tau.gen_match==5]
        taus_DM1  = [tau for tau in event.taus if tau.decayMode() == 1 and tau.gen_match==5]
        taus_DM10 = [tau for tau in event.taus if tau.decayMode() == 10 and tau.gen_match==5]

        metTES_down_0 =  event.met.p4()
        metTES_up_0   = event.met.p4()

        metTES_down_1 = event.met.p4()
        metTES_up_1   = event.met.p4()

        metTES_down_10 = event.met.p4()
        metTES_up_10   = event.met.p4()

        ###print "MOIKKA, pt for 10", metTES_down_10.pt(), metTES_up_10.pt()

        for tau in taus_DM0:
           metTES_down_0 -= (tau.TES_downP4-tau.p4())
           metTES_up_0 -= (tau.TES_upP4-tau.p4())

        for tau in taus_DM1:
           metTES_down_1 -= (tau.TES_downP4-tau.p4()) 
           metTES_up_1 -= (tau.TES_upP4-tau.p4()) 

        for tau in taus_DM10:
           metTES_down_10 -= (tau.TES_downP4-tau.p4()) 
           metTES_up_10 -= (tau.TES_upP4-tau.p4()) 
        

        #Compute met uncertainties here
        event.met_px_DM0_up  = metTES_up_0.px()
        event.met_py_DM0_up = metTES_up_0.py()
        event.met_pt_DM0_up = metTES_up_0.pt()
        event.met_phi_DM0_up = metTES_up_0.phi()

        event.met_px_DM0_down  = metTES_down_0.px()
        event.met_py_DM0_down = metTES_down_0.py()
        event.met_pt_DM0_down = metTES_down_0.pt()
        event.met_phi_DM0_down = metTES_down_0.phi()

        event.met_px_DM1_up  = metTES_up_1.px()
        event.met_py_DM1_up = metTES_up_1.py()
        event.met_pt_DM1_up = metTES_up_1.pt()
        event.met_phi_DM1_up = metTES_up_1.phi()

        event.met_px_DM1_down  = metTES_down_1.px()
        event.met_py_DM1_down = metTES_down_1.py()
        event.met_pt_DM1_down = metTES_down_1.pt()
       	event.met_phi_DM1_down = metTES_down_1.phi()
       
        event.met_px_DM10_up  = metTES_up_10.px()
        event.met_py_DM10_up = metTES_up_10.py()
        event.met_pt_DM10_up = metTES_up_10.pt()
        event.met_phi_DM10_up = metTES_up_10.phi()
 
        event.met_px_DM10_down  = metTES_down_10.px()
        event.met_py_DM10_down = metTES_down_10.py()
        event.met_pt_DM10_down = metTES_down_10.pt()
       	event.met_phi_DM10_down = metTES_down_10.phi()


        event.met_px_JetEnUp = event.met.shiftedPx(event.met.JetEnUp)
        event.met_py_JetEnUp = event.met.shiftedPy(event.met.JetEnUp)
        event.met_pt_JetEnUp = event.met.shiftedPt(event.met.JetEnUp)
        event.met_phi_JetEnUp = event.met.shiftedPhi(event.met.JetEnUp)

        event.met_px_JetEnDown = event.met.shiftedPx(event.met.JetEnDown)
        event.met_py_JetEnDown = event.met.shiftedPy(event.met.JetEnDown)
        event.met_pt_JetEnDown = event.met.shiftedPt(event.met.JetEnDown)
        event.met_phi_JetEnDown = event.met.shiftedPhi(event.met.JetEnDown)

        event.met_px_UncEnUp = event.met.shiftedPx(event.met.UnclusteredEnUp)
        event.met_py_UncEnUp = event.met.shiftedPy(event.met.UnclusteredEnUp)
        event.met_pt_UncEnUp = event.met.shiftedPt(event.met.UnclusteredEnUp)
        event.met_phi_UncEnUp = event.met.shiftedPhi(event.met.UnclusteredEnUp)

        event.met_px_UncEnDown = event.met.shiftedPx(event.met.UnclusteredEnDown)
        event.met_py_UncEnDown = event.met.shiftedPy(event.met.UnclusteredEnDown)
        event.met_pt_UncEnDown = event.met.shiftedPt(event.met.UnclusteredEnDown)
        event.met_phi_UncEnDown = event.met.shiftedPhi(event.met.UnclusteredEnDown)
            
        return True


    def Scale(self, tau, ptSelGentauleps, ptSelGenleps, event):
        # this function should take values of scales from a file
        tau.unscaledP4 = copy.deepcopy(tau.p4())
        HTTGenAnalyzer.genMatch(event, tau, ptSelGentauleps, ptSelGenleps, [])
        HTTGenAnalyzer.attachGenStatusFlag(tau)
        if tau.gen_match==5:
            if tau.decayMode() == 0:
                tau.scaleEnergy(0.995)
            elif tau.decayMode() == 1:
                tau.scaleEnergy(1.011)
            elif tau.decayMode() == 10:
                tau.scaleEnergy(1.006)
        elif tau.gen_match==1 or tau.gen_match == 3:
            if tau.decayMode() == 1:
                tau.scaleEnergy(1.095)
        elif tau.gen_match == 2 or tau.gen_match == 4 :
            if tau.decayMode() == 1 :
                tau.scaleEnergy(1.015)
