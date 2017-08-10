import ROOT

import math

from itertools import product
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon
from PhysicsTools.Heppy.physicsobjects.Electron import Electron
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2
from PhysicsTools.Heppy.physicsobjects.Particle import Particle

import pprint
import itertools


mass = {23: 91.2, 25: 125.}

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
        if met!=None:             
            self._met = met
        #else:
        #    print 'Z selvasti, met none'
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status
        self._DR = deltaR(leg1.eta(), leg1.phi(), leg2.eta(), leg2.phi())
        self._LT = leg1.pt() + leg2.pt()

    def DR(self):
        return self._DR

    def LT(self):
        return self._LT

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


class AZhAnalyzer(Analyzer):

    def testDeltaR(self, leg1, leg2, dR_value):
        '''returns True if the two diLepton.leg1() and .leg2() have a delta R larger than the dR_min parameter.'''
        dR = deltaR(leg1.eta(), leg1.phi(),
                    leg2.eta(), leg2.phi())
        #print "dR onkin nyt:::"
        #print dR
        return dR > dR_value

    def constructZboson(self, collection, deltaR_min, event):
        '''Constructs all possible Z bosons using the given collection, and returns the candidate that has the mass the closest to the Z mass.'''

        Z_bosons=[]
        resonances=[]
        event.goodVertices = event.vertices

        m1OK = False
        m2OK = False
        e1OK = False
        e2OK = False

#        print "LET US MAKE A Z"

        for leg1, leg2 in itertools.combinations(collection,2):
            m1OK = False
       	    m2OK = False
       	    e1OK = False
       	    e2OK = False
       #     if leg1.pt()>20 or leg2.pt()>20: #remove
            if leg2.pt()>leg1.pt():
                leg_dummy=leg1
                leg1=leg2
                leg2=leg_dummy
            leg1.event = event.input.object()
            leg2.event = event.input.object()
            leg1.associatedVertex = event.goodVertices[0]
            leg2.associatedVertex = event.goodVertices[0]
            if (leg1.charge()+leg2.charge())==0 and self.testDeltaR(leg1, leg2, deltaR_min):
             #   print "LOOKS GOOD"
                Zbosoni = Resonance(leg1, leg2, None, 23, 3)
                #check muon id iso
                m1OK = abs(Zbosoni.leg1().pdgId())==13 and leg1.muonID('POG_ID_Loose') and leg1.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.25
                m2OK = abs(Zbosoni.leg2().pdgId())==13 and leg2.muonID('POG_ID_Loose') and leg2.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.25
                #check ele id iso
                #e1OK = abs(Zbosoni.leg1().pdgId())==11 and leg1.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90') and leg1.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3
                #e2OK = abs(Zbosoni.leg2().pdgId())==11 and leg2.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90') and leg2.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3
               
                e1OK = abs(Zbosoni.leg1().pdgId())==11 and leg1.mvaIDRun2('Spring16', 'POG90') and leg1.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3
                e2OK = abs(Zbosoni.leg2().pdgId())==11 and leg2.mvaIDRun2('Spring16', 'POG90') and leg2.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3


             #   print "muons:"
             #   print m1OK 
             #   print m2OK
             #   print "els:"
             #   print e1OK
             #   print e2OK

             #   if e1OK or e2OK:
             #      print "leg1"
             #      print Zbosoni.leg1().pt()
             #      print Zbosoni.leg1().pdgId()
             #      print Zbosoni.leg1().relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0)
             #      print "id:"
             #      print Zbosoni.leg1().mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90')
             #      print "uusi:"
             #      print Zbosoni.leg1().mvaIDRun2('Spring16', 'POG90')
             #      print "leg 2"
             #      print Zbosoni.leg2().pt()
             #      print Zbosoni.leg2().pdgId()
             #      print "iso"
             #      print Zbosoni.leg2().relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0)
             #      print "id:"
             #      print Zbosoni.leg2().mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90')
             #      print "uusi:"
             #      print Zbosoni.leg2().mvaIDRun2('Spring16', 'POG90')

                if m1OK and m2OK:
               #    print "muons OK"
                   resonances.append( Zbosoni )
                elif e1OK and e2OK:
              #     print "z ok"
                   resonances.append( Zbosoni ) 
    
        nominal_mass = mass[23]
        resonances.sort(key=lambda x: abs(x.mass()-nominal_mass))

        if resonances:
            if 60 < resonances[0].mass() < 120:
               # print "JEE"
                Z_bosons.append(resonances[0])
        
        return Z_bosons

    def constructHbosonLepTau(self, leg1, leg2, deltaR_min, event):
        '''Constructs all possible H bosons using the given collections for leptons and taus, and returns the candidate that has the mass the closest to the H mass.'''

        H_bosons=[]

        event.goodVertices = event.vertices

        met=event.met

        if abs(leg1.pdgId()) == 15:
            tau = leg1
            lepton = leg2
        else:
            lepton = leg1
            tau = leg2
 
        tauOK = False

        if tau.pt()>20:
            lepton.associatedVertex = event.goodVertices[0]
            tau.associatedVertex = event.goodVertices[0]
            if abs(lepton.pdgId() ) == 13 and tau.tauID('againstMuonTight3') > 0.5: 
                tauOK=True
            elif abs(lepton.pdgId() ) == 11 and tau.tauID('againstElectronTightMVA6') > 0.5:
                tauOK=True 
            di_tau = Resonance(lepton, tau, met, 25, 3)
            di_tau.mvaMetSig = None
            if self.testDeltaR(lepton, tau, deltaR_min) and abs(lepton.dxy()) < 0.045 and abs(lepton.dz()) < 0.2 and tauOK: #di_tau.charge()==0 remove for fakerate
                H_bosons.append(di_tau)
                                  
        H_bosons.sort(key=lambda x: x.pt(), reverse=True)

        return H_bosons

    def constructHbosondiTau(self, leg1, leg2, deltaR_min, event):
        '''Constructs all possible H bosons using the given tau legs, and returns the candidate that has the mass the closest to the H mass.'''

        H_bosons=[]
        event.goodVertices = event.vertices
        met=event.met
 
        if leg1.pt()>20 and leg2.pt()>20:
            if leg2.pt()>leg1.pt():
               leg_dummy=leg1
               leg1=leg2
               leg2=leg_dummy
            leg1.associatedVertex = event.goodVertices[0]
            leg2.associatedVertex = event.goodVertices[0]
            di_tau = Resonance(leg1, leg2, met, 25, 3)
            di_tau.mvaMetSig = None
            if self.testDeltaR(leg1, leg2, deltaR_min): #and di_tau.charge()==0
                H_bosons.append(di_tau)

        H_bosons.sort(key=lambda x: x.pt(), reverse=True)

        return H_bosons

    def constructHbosonEleMu(self, leg1, leg2, deltaR_min, event):
        '''Constructs all possible H bosons using the given collections for muons and electrons, and returns the candidate that has the mass the closest to the H mass.'''

        H_bosons=[]
        event.goodVertices = event.vertices
        met=event.met

        if abs(leg1.pdgId()) == 11:
            electron = leg1
            muon = leg2
        else:
            muon = leg1
            electron = leg2       

        electron.associatedVertex = event.goodVertices[0]
        muon.associatedVertex = event.goodVertices[0]
        if abs(electron.dxy()) < 0.045 and abs(electron.dz()) < 0.2 and abs(muon.dxy()) < 0.045 and abs(muon.dz()) < 0.2 and self.testDeltaR(electron, muon, deltaR_min):
            di_tau = Resonance(electron, muon, met, 25, 3)
            di_tau.mvaMetSig = None
          #  if di_tau.charge()==0: remove charge for Fakerate
            H_bosons.append(di_tau)


        H_bosons.sort(key=lambda x: x.pt(), reverse=True)

        return H_bosons


    def process(self, event):

        #read collection and map necessary objects

        super(AZhAnalyzer, self).readCollections(event.input)

        event.goodVertices = event.vertices

        muons = [ muon for muon in event.muons ] #event.muons #map(Muon, self.handles['muons'].product())  
        electrons = event.electrons #map(Electron, self.handles['electrons'].product())
        taus = event.taus #map(Tau, self.handles['taus'].product())
        met = event.met #self.handles['met'].product()[0] 

        muonsGOOD = event.muonsGOOD
        electronsGOOD = event.electronsGOOD
        tausGOOD = event.tausGOOD

        #ADD LATER ON: electron.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) <= 1

        if self.cfg_ana.MC:
           #print "CROSS"
           XSecLumiWeight = 1.0
           setattr(event, 'XSecLumiWeight', XSecLumiWeight)


      #  print "muons bad and good:"
      #  print len(muons)
      #  print len(muonsGOOD)

      #  print "elss bad and good:"
      # 	print len(electrons)  
      # 	print len(electronsGOOD)

      #  print "taus:"
      # 	print len(taus)  


        #EXTRA LEPTON VETO

        #check how many electrons and muons we have 
        if ( len(muonsGOOD)+len(electronsGOOD) )<2 or ( len(muonsGOOD)+len(electronsGOOD) )>4:
      #      print "TOTAL NUMBER JUST WRONG"
            return False

        #we cannot have more than 3 electrons or 3 muons at this point anymore
        if ( len(muonsGOOD) > 3 ) or ( len(electronsGOOD) > 3):
      #      print "MORE THAN 3 MUONS OR ELECTRONS"
            return False


        event.isSignal = True

        #maybe not needed?
       # setattr(event, 'muons', muons)
       # setattr(event, 'electrons', electrons)
       # setattr(event, 'taus', taus) 
       # setattr(event, 'met', met)


        #muons = [ muon for muon in muons if muon.pt()>10 and abs(muon.eta())<2.4 and muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15]
        #electrons = [ electron for electron in electrons if electron.pt()>10 and abs(electron.eta())<2.5 and electron.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.1]
        #taus = [ tau for tau in taus if tau.pt()>10 and abs(tau.eta())<2.3 and tau.tauID('byTightIsolationMVArun2v1DBoldDMwLT') > 0.5]

        #make the final cuts cuts
       # muons = [ muon for muon in muons if muon.pt()>10 and abs(muon.eta())<2.4 and muon.muonID('POG_ID_Medium_ICHEP') and muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15] 
       # electrons = [ electron for electron in electrons if electron.pt()>10 and abs(electron.eta())<2.5 and electron.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90') and electron.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) <= 1 and electron.passConversionVeto() and electron.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.1]
       # taus = [ tau for tau in taus if tau.pt()>10 and abs(tau.eta())<2.3 and tau.tauID('decayModeFinding') > 0.5 and abs(tau.leadChargedHadrCand().dz()) < 0.2 and tau.tauID('byTightIsolationMVArun2v1DBoldDMwLT') > 0.5 and tau.tauID('againstElectronVLooseMVA6') > 0.5 and tau.tauID('againstMuonTight3') > 0.5]

        #for DY test
       # muons = [ muon for muon in muons if muon.pt()>10 and abs(muon.eta())<2.4 and muon.muonID('POG_ID_Loose') and muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.25]
       # electrons = [ electron for electron in electrons if electron.pt()>10 and abs(electron.eta())<2.5 and electron.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90') and electron.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) <= 1 and electron.passConversionVeto() and electron.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3]
       # taus = [ tau for tau in taus if tau.pt()>10 and abs(tau.eta())<2.3 and tau.tauID('decayModeFinding') > 0.5 and abs(tau.leadChargedHadrCand().dz()) < 0.2 and tau.tauID('byMediumIsolationMVArun2v1DBoldDMwLT') > 0.5 and tau.tauID('againstElectronVLooseMVA6') > 0.5 and tau.tauID('againstMuonLoose3') > 0.5]

 
        #muons = [ muon for muon in muons if muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15]
        #electrons = [ electron for electron in electrons if electron.mvaIDRun2('NonTrigSpring15MiniAOD', 'POG90') and electron.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.1 and electron.gsfTrack().hitPattern().numberOfHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) <= 1 and electron.passConversionVeto()]
        #taus = [ tau for tau in taus if tau.tauID('decayModeFinding') > 0.5 and abs(tau.leadChargedHadrCand().dz()) < 0.2 and tau.tauID('byTightIsolationMVArun2v1DBoldDMwLT') > 0.5 and tau.tauID('againstElectronVLooseMVA6') > 0.5 and tau.tauID('againstMuonTight3') > 0.5]


        allLeptons = []
        allLeptons += muons
        allLeptons += electrons
        allLeptons += taus

       # setattr(event, 'allLeptons', len(allLeptons))
       # setattr(event, 'selectedLeptons', allLeptons)

        allLeptonsFinal = []
        allLeptonsFinal += allLeptons

        #if len(allLeptons)==4:
        #    fourLeptons = True
        #else:
        #    return False
           
	
        Z_muons = []
        Z_electrons = []

        Z_muons = self.constructZboson(muons, 0.3, event)
        Z_electrons = self.constructZboson(electrons, 0.3, event)
            
        Z_resonance = []

        #Throw away events with EEMM
        if (Z_muons and Z_electrons):
       #     print "THERE WAS TOO"
            Z_resonance = []
            Z_muons = []
            Z_electrons = []
        elif Z_muons and not Z_electrons:
        #    print "MUONS"
            Z_resonance.append(Z_muons[0])
        elif not Z_muons and Z_electrons:
        #    print "ELS"
            Z_resonance.append(Z_electrons[0])

            
        #construct the H boson here if there is a good Z candidate:

        H_resonance=[]      
        H_muTau = []
        H_eleTau = []
        H_diTau = []
        H_eleMu = []

        H_tt = []
        H_mt = []
        H_et = []
        H_em = []

        nominal_massH = mass[25]


        if Z_resonance:

            Zleg1=Z_resonance[0].leg1()
            Zleg2=Z_resonance[0].leg2()

            if Zleg1 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg1)
            if Zleg2 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg2)
            
            for leg1, leg2 in itertools.combinations(allLeptonsFinal,2):
              #  if (leg1.charge()+leg2.charge())==0: #for fakerate
                if leg1 in taus and leg2 in taus:
                    H_diTau = self.constructHbosondiTau(leg1, leg2, 0.5, event)
                    if H_diTau and self.testDeltaR(Zleg1, leg1, 0.5) and self.testDeltaR(Zleg1, leg2, 0.5) and self.testDeltaR(Zleg2, leg1, 0.5) and self.testDeltaR(Zleg2, leg2, 0.5):
                        H_tt.append(H_diTau[0])
                        #H_resonance.append(H_diTau[0])
                elif (leg1 in taus) or (leg2 in taus):
                    if (leg1 in muons) or (leg2 in muons):
                        H_muTau = self.constructHbosonLepTau(leg1, leg2, 0.5, event)
                        if H_muTau and self.testDeltaR(Zleg1, H_muTau[0].leg1(), 0.3) and self.testDeltaR(Zleg1, H_muTau[0].leg2(), 0.5) and self.testDeltaR(Zleg2, H_muTau[0].leg1(), 0.3) and self.testDeltaR(Zleg2, H_muTau[0].leg2(), 0.5):
                            H_mt.append(H_muTau[0])
                         #   H_resonance.append(H_muTau[0])
                    if (leg1 in electrons) or (leg2 in electrons):
                        H_eleTau = self.constructHbosonLepTau(leg1, leg2, 0.5, event)
                        if H_eleTau and self.testDeltaR(Zleg1, H_eleTau[0].leg1(), 0.3) and self.testDeltaR(Zleg1, H_eleTau[0].leg2(), 0.5) and self.testDeltaR(Zleg2, H_eleTau[0].leg1(), 0.3) and self.testDeltaR(Zleg2, H_eleTau[0].leg2(), 0.5):
                                   	       	       	### CHECK THAT TWO TAUS	DO NOT OVERLAP WITH Z LEGS
                            H_et.append(H_eleTau[0])
                        #    H_resonance.append(H_eleTau[0])
                else:
                    if (abs( leg1.pdgId() ) + abs( leg2.pdgId() )) not in [22,26]:   
                        H_eleMu = self.constructHbosonEleMu(leg1, leg2, 0.3, event)
                        if H_eleMu and self.testDeltaR(Zleg1, leg1, 0.3) and self.testDeltaR(Zleg1, leg2, 0.3) and self.testDeltaR(Zleg2, leg1, 0.3) and self.testDeltaR(Zleg2, leg2, 0.3):
                                  	       	       	### CHECK THAT TWO TAUS	DO NOT OVERLAP WITH Z LEGS
                            H_em.append(H_eleMu[0])
                        #    H_resonance.append(H_eleMu[0])
        
         ### CHECK THAT FINAL LEPTON

     #   H_tt.sort(key=lambda x: x.LT(), reverse=True)
     #   H_et.sort(key=lambda x: x.LT(), reverse=True)
     #   H_mt.sort(key=lambda x: x.LT(), reverse=True)
     #   H_em.sort(key=lambda x: x.LT(), reverse=True)

     #   H_resonance.sort(key=lambda x: x.LT(), reverse=True)

        if (Z_muons):
            if H_tt and ( len(muonsGOOD) != 2 or len(electronsGOOD) != 0 ):
                H_tt=[]
            if H_et and ( len(muonsGOOD) != 2 or len(electronsGOOD) > 1 ):
                H_et=[]
            if H_mt and ( 2<len(muonsGOOD) or len(muonsGOOD)>3 or len(electronsGOOD) != 0 ):
                H_mt=[]
            if H_em and ( 2<len(muonsGOOD) or len(muonsGOOD)>3 or len(electronsGOOD) > 1 ):
                H_em=[]
        elif (Z_electrons):
            if H_tt and ( len(muonsGOOD) != 0 or len(electronsGOOD) != 2 ):
                H_tt=[]
       	    if H_et and ( len(muonsGOOD) != 0 or 2<len(electronsGOOD) or len(electronsGOOD)>3 ):
                H_et=[]
       	    if H_mt and ( len(muonsGOOD) > 1 or len(electronsGOOD) != 2 ):
               # "HYLKAA"
               # print len(muonsGOOD)
               # print len(electronsGOOD)
                H_mt=[]
       	    if H_em and ( len(muonsGOOD) > 1 or 2<len(electronsGOOD) or len(electronsGOOD)>3 ):
                H_em=[]
      
        
        #just to be sure
        H_tt.sort(key=lambda x: x.LT(), reverse=True)
        H_et.sort(key=lambda x: x.LT(), reverse=True)
        H_mt.sort(key=lambda x: x.LT(), reverse=True)
        H_em.sort(key=lambda x: x.LT(), reverse=True)

        if H_tt:
         #   print "HTT: "
         #   print len(H_tt)
       	 #   print H_tt[0].LT()
         #   print H_tt[0].pt()
            H_resonance.append(H_tt[0])
        if H_et:
           # print "HeT: "
           # print len(H_et)
       	   # print H_et[0].LT()
       	    H_resonance.append(H_et[0])
        if H_mt:
         #   print "HmT: "
         #   print len(H_mt)
       	 #   print H_mt[0].LT()
         #   print H_mt[0].pt()
       	    H_resonance.append(H_mt[0])
        if H_em:
           # print "Hem: "
           # print len(H_em)
       	  #  print H_em[0].LT()
       	    H_resonance.append(H_em[0]) 

        H_resonance.sort(key=lambda x: x.pt(), reverse=True)

       # print "len resonances"
       # print len(H_resonance)
  
        #If more than one Higgs, take the one with the largest LT
       # if (len(H_em) + len(H_et) + len(H_tt) + len(H_mt) > 1):
       #     H_resonance=H_resonance[:1]
       #     Hleg1=H_resonance[0].leg1()
       #     Hleg2=H_resonance[0].leg2()
       #     if H_tt:              
       #         if Hleg1 == H_tt[0].leg1() and Hleg2 == H_tt[0].leg2():
       #             #print "KORKEIN LT"
       #             H_tt=H_tt[:1]                
       #             H_em=[]
       #             H_mt=[]
       #             H_et=[]
       #     if H_et:
       #	        if Hleg1 == H_et[0].leg1() and Hleg2 == H_et[0].leg2():
       #             H_et=H_et[:1]
       #             H_em=[]
       #	       	    H_mt=[]
       #	       	    H_tt=[]
       #     if H_mt:
       #	        if Hleg1 == H_mt[0].leg1() and Hleg2 == H_mt[0].leg2():
       #             #print "MT"
       #             H_mt=H_mt[:1]
       #             H_em=[]
       #	       	    H_tt=[]
       #	       	    H_et=[]
       #     if H_em:
       #	        if Hleg1 == H_em[0].leg1() and Hleg2 == H_em[0].leg2():
       #             H_em=H_em[:1]
       #             H_tt=[]
       #	       	    H_mt=[]
       #	       	    H_et=[]

               
        setattr(event, 'allLeptonsFinal', len(allLeptonsFinal))

        if (H_resonance and Z_resonance):
          #  print "MOLEMMAT OLI"
            if (Z_muons):
                setattr(event, 'Z_mm_len', len(Z_muons))
                setattr(event, 'Zboson_mm', Z_muons)
            if (Z_electrons):
                setattr(event, 'Z_ee_len', len(Z_electrons))
                setattr(event, 'Zboson_ee', Z_electrons)
            setattr(event, 'Zboson', Z_resonance)
            setattr(event, 'Hboson', H_resonance)
            if (H_em):
                setattr(event, 'H_em_len', len(H_em))
                setattr(event, 'Hboson_em', H_em)#H_eleMu)
                Aboson = Resonance(H_em[0], Z_resonance[0], met, 36, 3)
                A_resonance=[]
                A_resonance.append(Aboson)
                setattr(event, 'Aboson_em', A_resonance)
            if (H_et):
                setattr(event, 'Hboson_et', H_et)#H_eleTau)
                setattr(event, 'H_et_len', len(H_et))
                Aboson = Resonance(H_et[0], Z_resonance[0], met, 36, 3)
       	       	A_resonance=[]
                A_resonance.append(Aboson)
                setattr(event, 'Aboson_et', A_resonance)
            if (H_mt):
                setattr(event, 'H_mt_len', len(H_mt))
                setattr(event, 'Hboson_mt', H_mt)#H_muTau)
                Aboson = Resonance(H_mt[0], Z_resonance[0], met, 36, 3)
       	       	A_resonance=[]
                A_resonance.append(Aboson)
                setattr(event, 'Aboson_mt', A_resonance)
            if (H_tt):
                setattr(event, 'H_tt_len', len(H_tt))
                setattr(event, 'Hboson_tt', H_tt)
                Aboson = Resonance(H_tt[0], Z_resonance[0], met, 36, 3)
       	       	A_resonance=[]
                A_resonance.append(Aboson)
                setattr(event, 'Aboson_tt', A_resonance)
            return True
        else:
            return False

        #construct the A boson here

       # A_resonance=[]

       # if Z_resonance and H_resonance:
       #     Aboson = Resonance(H_resonance[0], Z_resonance[0], met, 36, 3)
           # if 220<=Aboson.mass()<=350:
       #     A_resonance.append(Aboson)
       #     setattr(event, 'Aboson', A_resonance)
       #     return True
       # else:
       #     return False  
