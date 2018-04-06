import ROOT

import math

from itertools import product
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon
from PhysicsTools.Heppy.physicsobjects.Electron import Electron
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2, deltaPhi
from PhysicsTools.Heppy.physicsobjects.Particle import Particle

import pprint
import itertools


mass = {23: 91.1876, 25: 125.}

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
        #if met!=None:             
        #    self._met = met
        #else:
        #    
        #    print 'Z selvasti, met none'
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status
        self._DR = deltaR(leg1.eta(), leg1.phi(), leg2.eta(), leg2.phi())
        self._LT = leg1.pt() + leg2.pt()
        if met!=None:
            self._met = met
            self._METphi = deltaPhi( met.phi(), self._p4.phi() ) 
        else:
            self._METphi = -999

    def METphi(self):
        return self._METphi

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

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(AZhAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.dataName = getattr(self.cfg_comp, "name", None)


    def testDeltaR(self, leg1, leg2, dR_value):
        '''returns True if the two diLepton.leg1() and .leg2() have a delta R larger than the dR_min parameter.'''
        dR = deltaR(leg1.eta(), leg1.phi(),
                    leg2.eta(), leg2.phi())
        #if abs(leg2.pdgId() ) == 15:
        #    print "dR onkin nyt:::"
        #    print dR
        return dR > dR_value

    def constructZboson(self, collection, deltaR_min, event):
        '''Constructs all possible Z bosons using the given collection, and returns the candidate that has the mass the closest to the Z mass.'''

        Z_bosons=[]
        resonances=[]
        resonances_id=[]
        event.goodVertices = event.vertices

        m1OK = False
        m2OK = False
        e1OK = False
        e2OK = False

        for leg1, leg2 in itertools.combinations(collection,2):
            m1OK = False
       	    m2OK = False
       	    e1OK = False
       	    e2OK = False
            if leg2.pt()>leg1.pt():
                leg_dummy=leg1
                leg1=leg2
                leg2=leg_dummy
            leg1.event = event.input.object()
            leg2.event = event.input.object()
            leg1.associatedVertex = event.goodVertices[0]
            leg2.associatedVertex = event.goodVertices[0]


            if (leg1.charge()+leg2.charge())==0 and self.testDeltaR(leg1, leg2, deltaR_min):
                Zbosoni = Resonance(leg1, leg2, None, 23, 3)
                resonances.append( Zbosoni )

                #check muon id iso
                m1OK = abs(Zbosoni.leg1().pdgId())==13 and leg1.muonID('POG_ID_Loose') and leg1.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.25 and leg1.pt()>10
                m2OK = abs(Zbosoni.leg2().pdgId())==13 and leg2.muonID('POG_ID_Loose') and leg2.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.25 and leg2.pt()>10

                #check ele id iso
                e1OK = abs(Zbosoni.leg1().pdgId())==11 and leg1.mvaIDRun2('Spring16', 'POG90') and leg1.pt()>10 # and leg1.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3
                e2OK = abs(Zbosoni.leg2().pdgId())==11 and leg2.mvaIDRun2('Spring16', 'POG90') and leg2.pt()>10 # and leg2.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) < 0.3

                if m1OK and m2OK:
                   #print "MU OK"
                   resonances_id.append( Zbosoni )
                elif e1OK and e2OK:
                   #print "ELE OK"
                   resonances_id.append( Zbosoni ) 
    
        nominal_mass = mass[23]
        resonances.sort(key=lambda x: abs(x.mass()-nominal_mass))
        resonances_id.sort(key=lambda x: abs(x.mass()-nominal_mass))

        Z_aligned=0
        if resonances_id and resonances:
            if resonances[0]==resonances_id[0]:
                Z_aligned = 1

        if resonances:
            if 60 < resonances[0].mass() < 120:
                #print "MASS OK"
                Z_bosons.append(resonances[0])
            if abs(resonances[0].leg1().pdgId())==11:
                setattr(event, 'Z_ee_aligned', Z_aligned)
            else:
                setattr(event, 'Z_mm_aligned', Z_aligned)        

        return Z_bosons

    def constructHbosonLepTau(self, leg1, leg2, deltaR_min, event):
        '''Constructs all possible H bosons using the given collections for leptons and taus, and returns the candidate that has the mass the closest to the H mass.'''

        #print "HERE WE ARE"
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
            #print tau.pt()
            lepton.associatedVertex = event.goodVertices[0]
            tau.associatedVertex = event.goodVertices[0]
            #print "tau id"
            #print tau.tauID('againstElectronTightMVA6')
            if abs(lepton.pdgId() ) == 13 and tau.tauID('againstMuonTight3') > 0.5: 
             #   print "tauok MU"
                tauOK=True
            elif abs(lepton.pdgId() ) == 11 and tau.tauID('againstElectronTightMVA6') > 0.5:
             #   print "tauOK ELS"
                tauOK=True 
            di_tau = Resonance(lepton, tau, met, 25, 3)
            di_tau.mvaMetSig = None
            #print "deltar:"
            #print self.testDeltaR(lepton, tau, deltaR_min)
            #print "for lepton:"
            #print abs(lepton.dxy())
            #print abs(lepton.dz())
            #print "tauOK"
            #print tauOK
            #print "getting to the initial check:"
            if self.testDeltaR(lepton, tau, deltaR_min) and abs(lepton.dxy()) < 0.045 and abs(lepton.dz()) < 0.2 and tauOK: #di_tau.charge()==0 remove for fakerate
                #print "JEEJEEE"
                H_bosons.append(di_tau)
                                  
        H_bosons.sort(key=lambda x: x.pt(), reverse=True)
        #for bosoni in H_bosons:
        #    print "MASSA"
        #    print bosoni.mass()

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

        #print "AZHANALYZER-----------------------------------------"
        #print "Meidan kommpis onkin talla kertaa"
        #print self.dataName

        #if "Single" not in self.dataName:
        #    print "Minusta meni oikein!"

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


        event.isSignal = True

        allLeptons = []
        allLeptons += muons
        allLeptons += electrons
        allLeptons += taus


        allLeptonsFinal = []
        allLeptonsFinal += allLeptons

	
        Z_muons = []
        Z_electrons = []

        Z_muons = self.constructZboson(muons, 0.3, event)
        Z_electrons = self.constructZboson(electrons, 0.3, event)
            
        Z_resonance = []

        Z_matched = 0

        #Throw away events with EEMM
        if (Z_muons and Z_electrons and event.Z_mm_aligned>0 and event.Z_ee_aligned>0):
            #print "THERE WAS TOO"
            Z_resonance = []
            Z_muons = []
            Z_electrons = []
        elif Z_muons and event.Z_mm_aligned>0:
            #print "MUONS"
            Z_electrons=[]
            Z_resonance.append(Z_muons[0])
            #high pt legs
            if Z_muons[0].leg1().pt()>27 and Z_muons[0].leg2().pt()>27:
                #print "HIGH PT"
                if (hasattr(Z_muons[0].leg1(),'matchedTrgObjMus_Double') and hasattr(Z_muons[0].leg2(),'matchedTrgObjMus_Double')) and "Single" not in self.dataName:
                    Z_matched = 1
                elif (hasattr(Z_muons[0].leg1(),'matchedTrgObjMus_Single') or hasattr(Z_muons[0].leg2(),'matchedTrgObjMus_Single')):
                    Z_matched = 1
            #medium pt legs
            elif Z_muons[0].leg1().pt()>27 and Z_muons[0].leg2().pt()<27 and Z_muons[0].leg2().pt()>10:
                #print "MEDIUM"
                if (hasattr(Z_muons[0].leg1(),'matchedTrgObjMus_Double') and hasattr(Z_muons[0].leg2(),'matchedTrgObjMus_Double')) and "Single" not in self.dataName:
                    ##print "DINGIDN"
       	       	    Z_matched = 1
       	       	elif (hasattr(Z_muons[0].leg1(),'matchedTrgObjMus_Single')):
                    ##print "DINGDIN"
       	       	    Z_matched = 1
            #low pt
            elif Z_muons[0].leg1().pt()<27 and Z_muons[0].leg1().pt()>19 and Z_muons[0].leg2().pt()<27 and Z_muons[0].leg2().pt()>10:
                #print "LOW"
                if (hasattr(Z_muons[0].leg1(),'matchedTrgObjMus_Double') and hasattr(Z_muons[0].leg2(),'matchedTrgObjMus_Double')) and "Single" not in self.dataName:
       	       	    Z_matched = 1
        elif Z_electrons and event.Z_ee_aligned>0:
            #print "ELS"
            Z_muons=[]
            Z_resonance.append(Z_electrons[0])
            #high pt
            if Z_electrons[0].leg1().pt()>32 and Z_electrons[0].leg2().pt()>32:
                if (hasattr(Z_electrons[0].leg1(),'matchedTrgObjEls_Double') and hasattr(Z_electrons[0].leg2(),'matchedTrgObjEls_Double')) and "Single" not in self.dataName:
                    Z_matched = 1
                elif (hasattr(Z_electrons[0].leg1(),'matchedTrgObjEls_Single') or hasattr(Z_electrons[0].leg2(),'matchedTrgObjEls_Single')):
                    Z_matched = 1
            #medium
            elif Z_electrons[0].leg1().pt()>32 and Z_electrons[0].leg2().pt()>17.5 and Z_electrons[0].leg2().pt()<32:
                if (hasattr(Z_electrons[0].leg1(),'matchedTrgObjEls_Double') and hasattr(Z_electrons[0].leg2(),'matchedTrgObjEls_Double')) and "Single" not in self.dataName:
                    Z_matched = 1
                elif (hasattr(Z_electrons[0].leg1(),'matchedTrgObjEls_Single')):
                    Z_matched = 1
            #low pt
            elif Z_electrons[0].leg1().pt()<32 and Z_electrons[0].leg1().pt()>27.5 and Z_electrons[0].leg2().pt()>17.5 and Z_electrons[0].leg2().pt()<32:
                if (hasattr(Z_electrons[0].leg1(),'matchedTrgObjEls_Double') and hasattr(Z_electrons[0].leg2(),'matchedTrgObjEls_Double')) and "Single" not in self.dataName:
                    Z_matched = 1

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

        if not Z_matched:
            return False

        if Z_resonance and self.cfg_ana.FAKERATE and Z_matched:
            Zleg1=Z_resonance[0].leg1()
            Zleg2=Z_resonance[0].leg2()

            if Zleg1 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg1)
            if Zleg2 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg2)

            if (Z_muons):
                setattr(event, 'Z_mm_len', len(Z_muons))
                setattr(event, 'Zboson_mm', Z_muons)
            if (Z_electrons):
                setattr(event, 'Z_ee_len', len(Z_electrons))
                setattr(event, 'Zboson_ee', Z_electrons)

            if abs(allLeptonsFinal[0].pdgId())==11:
                setattr(event, 'electron_FR', allLeptonsFinal)

            elif abs(allLeptonsFinal[0].pdgId())==13:
                setattr(event, 'muon_FR', allLeptonsFinal)
 
            elif abs(allLeptonsFinal[0].pdgId())==15:
                setattr(event, 'tau_FR', allLeptonsFinal)

            return True

        if Z_resonance and not self.cfg_ana.FAKERATE and Z_matched:
            #print "RAKENNA H"
            Zleg1=Z_resonance[0].leg1()
            Zleg2=Z_resonance[0].leg2()


            if Zleg1 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg1)
            if Zleg2 in allLeptonsFinal:
                allLeptonsFinal.remove(Zleg2)
            
            for leg1, leg2 in itertools.combinations(allLeptonsFinal,2):
              #  if (leg1.charge()+leg2.charge())==0: #for fakerate
                if leg1.pt()>10 and leg2.pt()>10:
                    if leg1 in taus and leg2 in taus:
                        H_diTau = self.constructHbosondiTau(leg1, leg2, 0.5, event)
                        if H_diTau and self.testDeltaR(Zleg1, leg1, 0.5) and self.testDeltaR(Zleg1, leg2, 0.5) and self.testDeltaR(Zleg2, leg1, 0.5) and self.testDeltaR(Zleg2, leg2, 0.5):
                        #if H_diTau and Z1_matched==1 and Z2_matched==1 and self.testDeltaR(Zleg1, leg1, 0.5) and self.testDeltaR(Zleg1, leg2, 0.5) and self.testDeltaR(Zleg2, leg1, 0.5) and self.testDeltaR(Zleg2, leg2, 0.5):
                            H_tt.append(H_diTau[0])
                        #H_resonance.append(H_diTau[0])
                    elif (leg1 in taus) or (leg2 in taus):
                        if (leg1 in muons) or (leg2 in muons):
                            H_muTau = self.constructHbosonLepTau(leg1, leg2, 0.5, event)
                            if H_muTau and self.testDeltaR(Zleg1, H_muTau[0].leg1(), 0.3) and self.testDeltaR(Zleg1, H_muTau[0].leg2(), 0.5) and self.testDeltaR(Zleg2, H_muTau[0].leg1(), 0.3) and self.testDeltaR(Zleg2, H_muTau[0].leg2(), 0.5):
                                ##if Z1_matched==1 and Z2_matched==1:
                                H_mt.append(H_muTau[0])
                                #elif (Z1_matched==0 or Z2_matched==0) and hasattr(H_muTau[0].leg1(),'matchedTrgObjMus'):
                                #    H_mt.append(H_muTau[0])

                         #   print "OKEI TOSI JEES"
                         #   H_resonance.append(H_muTau[0])
                        if (leg1 in electrons) or (leg2 in electrons):
                        #print "----------------------------"
                        #print "OIS ET"
                            H_eleTau = self.constructHbosonLepTau(leg1, leg2, 0.5, event)
                            if H_eleTau and self.testDeltaR(Zleg1, H_eleTau[0].leg1(), 0.3) and self.testDeltaR(Zleg1, H_eleTau[0].leg2(), 0.5) and self.testDeltaR(Zleg2, H_eleTau[0].leg1(), 0.3) and self.testDeltaR(Zleg2, H_eleTau[0].leg2(), 0.5):
                                #print "LISAA LISTAAN"
                                ##if Z1_matched==1 and Z2_matched==1:
                                H_et.append(H_eleTau[0])
                               	##elif (Z1_matched==0 or Z2_matched==0) and hasattr(H_eleTau[0].leg1(),'matchedTrgObjEls'):
                                ##    H_et.append(H_eleTau[0])
                        #    H_resonance.append(H_eleTau[0])
                    else:
                        if (abs( leg1.pdgId() ) + abs( leg2.pdgId() )) not in [22,26]:   
                            H_eleMu = self.constructHbosonEleMu(leg1, leg2, 0.3, event)
                            if H_eleMu and self.testDeltaR(Zleg1, leg1, 0.3) and self.testDeltaR(Zleg1, leg2, 0.3) and self.testDeltaR(Zleg2, leg1, 0.3) and self.testDeltaR(Zleg2, leg2, 0.3):
                                  	       	       	### CHECK THAT TWO TAUS	DO NOT OVERLAP WITH Z LEGS
                                ###if Z1_matched==1 and Z2_matched==1:
                                H_em.append(H_eleMu[0])
                                ##elif (Z1_matched==0 or Z2_matched==0) and (hasattr(H_eleMu[0].leg1(),'matchedTrgObjEls') or hasattr(H_eleMu[0].leg2(),'matchedTrgObjMus') ): 
                                ##    H_em.append(H_eleMu[0])
                        #    H_resonance.append(H_eleMu[0])
        
        if (Z_muons):
            if H_tt and ( len(muonsGOOD) != 2 or len(electronsGOOD) != 0 ):
                H_tt=[]
            if H_et and ( len(muonsGOOD) != 2 or len(electronsGOOD) > 1 ):
                H_et=[]
            if H_mt and ( 2>len(muonsGOOD) or len(muonsGOOD)>3 or len(electronsGOOD) != 0 ):
                H_mt=[]
            if H_em and ( 2>len(muonsGOOD) or len(muonsGOOD)>3 or len(electronsGOOD) > 1 ):
                H_em=[]
        elif (Z_electrons):
            #print "OK"
            if H_tt and ( len(muonsGOOD) != 0 or len(electronsGOOD) != 2 ):
                #print "HYLKY HTT"
                H_tt=[]
       	    if H_et and ( len(muonsGOOD) != 0 or 2>len(electronsGOOD) or len(electronsGOOD)>3 ):
                #print len(muonsGOOD)
                #print len(electronsGOOD)
                #print "HYLKY HET"
                H_et=[]
       	    if H_mt and ( len(muonsGOOD) > 1 or len(electronsGOOD) != 2 ):
                #print "HYLKAA"
                #print len(muonsGOOD)
                #print len(electronsGOOD)
                H_mt=[]
       	    if H_em and ( len(muonsGOOD) > 1 or 2>len(electronsGOOD) or len(electronsGOOD)>3 ):
                #print "HYLKY HEM"
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
           # print "HET"
           # print "HeT: "
           # print len(H_et)
       	   # print H_et[0].LT()
       	    H_resonance.append(H_et[0])
        if H_mt:
         #   print "HmT: "
         #   print len(H_mt)
         #   print H_mt[0].pt()
          #  print H_mt[0].LT()
          #  print H_mt[0].leg1().pt()
          #  print H_mt[1].LT()
          #  print H_mt[1].leg1().pt()

       	    H_resonance.append(H_mt[0])
        if H_em:
       	    H_resonance.append(H_em[0]) 

        H_resonance.sort(key=lambda x: x.pt(), reverse=True)

        #print "len resonances"
        #print len(H_resonance)

       #another check
        if self.cfg_ana.applyIDISO and len(H_resonance)>1:
            H_resonance = []
  
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
           # print "MOLEMMAT OLI"
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
                #print "JEEE, LOPPU"
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
