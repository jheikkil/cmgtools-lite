import ROOT

import math

from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon
from PhysicsTools.Heppy.physicsobjects.Electron import Electron
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2


#from CMGTools.H2TauTau.proto.physicsobjects.DiObject import DirectDiTau
from PhysicsTools.Heppy.physicsobjects.Particle import Particle


class Resonance(Particle):
    '''Resonance decaying into 2 particles.
    The interface of this class mimics the interface of the CMS Candidate class.
    In this way Resonance objects or CMS Candidate objects can be processed
    transparently.
    '''

    def __init__(self, leg1, leg2, met, pdgid, status=3):
        '''
	Parameters (stored as attributes):
        leg1,2 : first and second leg.
        pdgid  : pdg code of the resonance
        status : status code of the resonance
        '''
	self._leg1 = leg1
        self._leg2 = leg2
        self._p4 = leg1.p4() + leg2.p4() #+ met.p4()
        self._met = met
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status

    def p4(self):
        return self._p4

    def leg1(self):
        return self._leg1

    def leg2(self):
        return self._leg2

    def pt(self):
        return self._p4.pt()

    def energy(self):
        return self._p4.energy()

    def eta(self):
        return self._p4.eta()

    def phi(self):
        return self._p4.phi()

    def mass(self):
        return self._p4.mass()

    def charge(self):
        return self._charge

    def pdgId(self):
        return self._pdgid

    def met(self):
        return self._met

    def svfitMass(self):
        return -999.

    def svfitTransverseMass(self):
        return -999.

    def svfitMassError(self):
        return -999.

    def svfitPt(self):
        return -999.

    def svfitPtError(self):
        return -999.

    def svfitEta(self):
        return -999.

    def svfitPhi(self):
        return -999.

    def __getattr__(self, name):
        '''Redefine getattr to original version.'''
        raise AttributeError

class HiggsAnalyzer(Analyzer):

 #   def buildDiLeptonsSingle(self, leptons, event):
 #       di_leptons = []#
 #	met = event.met
 #	for muon in leptons:
 #          for tau in event.taus:
 #              if tau.relIso() < 1.5:
 #                  di_tau = DirectDiTau(muon, tau, met)
 #                  di_tau.leg2().associatedVertex = event.goodVertices[0]
 #                  di_tau.leg1().associatedVertex = event.goodVertices[0]
 #                  di_tau.mvaMetSig = None
 #                  di_leptons.append(di_tau)
 #       return di_leptons

    def testDeltaR(self, diLepton):
        '''returns True if the two diLepton.leg1() and .leg2() have a delta R larger than the dR_min parameter.'''
        dR = deltaR(diLepton.leg1().eta(), diLepton.leg1().phi(),
                    diLepton.leg2().eta(), diLepton.leg2().phi())
        print 'NYT ARVOKSI TULI'
        print dR
        return dR > 0.5


    def process(self, event):
   
        event.goodVertices = event.vertices

        self.counters.addCounter('25')
        count = self.counters.counter('25')
        count.register('all pairs Higgs')
        count.register('accepted pairs Higgs')


        met=event.met

        leptons=[]

        if event.Zboson:
            Zleg1=event.Zboson[0].leg1()
            Zleg2=event.Zboson[0].leg2()
            print Zleg1
            print Zleg2

        for muon in event.muons:
            print '-----'
            print "MUONI ON"
            print muon
            if event.Zboson:
                if muon==Zleg1 or muon==Zleg2:
                    print 'OLI KAYTETTY, NAMA OVAT JALAT'
                    print Zleg1
                    print Zleg2
                    print 'ON KAYTETTY, JATKA'
                    continue
            if muon.muonID('POG_ID_Medium_ICHEP') and muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15 and abs(muon.eta())<2.4 and muon.pt()>10:
                #print 'OK'
                #print muon
                leptons.append(muon)

        print 'NO NYT, LEPTONS PITUUS'
        print len(leptons)


        leptons.sort(key=lambda x: x.pt())
        leptons.reverse()

        
        if leptons:
            for lepton in leptons:
                print lepton
        
        taus = []

        for tau in event.taus:
            if tau.tauID('byTightIsolationMVArun2v1DBoldDMwLT') > 0.5 and tau.tauID('againstElectronVLooseMVA6') > 0.5 and tau.tauID('againstMuonTight3') > 0.5 and abs(tau.eta())<2.3 and tau.pt()>21:
                taus.append(tau)

        taus.sort(key=lambda x: x.pt())
        taus.reverse()

        if taus:
            for tau in taus:
                print tau

        resonances=[]
  
        di_leptons=[]

        if event.Zboson: 
            for lepton in leptons:
                for tau in taus:  
                    lepton.associatedVertex = event.goodVertices[0]
                    tau.associatedVertex = event.goodVertices[0]
                    if abs(lepton.dxy()) < 0.045 and abs(lepton.dz()) < 0.2:
                        count.inc('all pairs Higgs')
                        di_tau = Resonance(lepton, tau, met, self.cfg_ana.pdgid, 3)
                        di_tau.mvaMetSig = None
                        if di_tau.charge()==0 and self.testDeltaR(di_tau):
                           count.inc('accepted pairs Higgs')
                           print 'VARAUS OK TAULLA'
                           di_leptons.append(di_tau)
        resonances=di_leptons

        print 'NYT, RESONANCES PITUUS'
        print len(resonances)
 
        nominal_mass = 125

        resonances.sort(key=lambda x: abs(x.mass()-nominal_mass))

        if resonances:
            print 'lahin massa:'
            print resonances[0].mass()

        Aboson = []
        Abosonit = []

        if resonances and event.Zboson:
            print 'contstruct A'
            Aboson = Resonance(resonances[0], event.Zboson[0], met, 36, 3)
            if 220<Aboson.mass()<=350:
                print 'OK, AN MASSA'
                print Aboson.mass()
                Abosonit.append(Aboson)            

        if Abosonit:
           print 'NYT ON A BOSONIEN PITUUS'
           print len(Abosonit)
           print 'PRINTTAAN NE JALAT'
           print Abosonit[0].leg1()
           print Abosonit[0].leg2()
           print 'JALKOJEN JALAT'
           print event.Zboson[0].leg1()
           print event.Zboson[0].leg2()
           print resonances[0].leg1()
           print resonances[0].leg2()


        setattr(event, 'Aboson', Abosonit)
        setattr(event, 'Hboson', resonances)
     

        #event.selectedTaus = [Tau(tau) for tau in self.handles['taus'].product() 
        #                      if tau.pt() > 18. 
        #                      and deltaR2(tau, event.leg1) > 0.25
        #                      and deltaR2(tau, event.leg2) > 0.25]

        #for tau in event.selectedTaus:
        #    tau.associatedVertex = event.goodVertices[0]

        #event.otherLeptons = event.selectedTaus[:]

        #event.pfmet = self.handles['pfMET'].product()[0]
        #event.puppimet = self.handles['puppiMET'].product()[0]

        return True
     
    def testLeg1ID(self, muon):
        return self.testLeg2ID(muon)
        

    def testLeg1Iso(self, muon, isocut):
        return self.testLeg2Iso(muon, isocut)


    def testVertex(self, lepton):
        '''Tests vertex constraints, for mu'''
        return abs(lepton.dxy()) < 0.045 and abs(lepton.dz()) < 0.2 


    def testLeg2ID(self, muon):
        '''Tight muon selection, no isolation requirement'''
        return muon.muonID('POG_ID_Medium_ICHEP') and self.testVertex(muon)
               

    def testLeg2Iso(self, muon, isocut):
        '''Tight muon selection, with isolation requirement'''
        if isocut is None:
            isocut = self.cfg_ana.iso2

        return muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < isocut    

    def testElectronID(self, electron):
        return electron.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90')

