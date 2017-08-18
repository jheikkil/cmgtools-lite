from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.Particle import Particle

import pprint 
import itertools

mass = {23: 91., 25: 125.}

class Resonance(Particle):
    '''Resonance decaying into 2 particles.
    The interface of this class mimics the interface of the CMS Candidate class. 
    In this way Resonance objects or CMS Candidate objects can be processed 
    transparently. 
    '''

    def __init__(self, leg1, leg2, pdgid, status=3): 
        '''
        Parameters (stored as attributes):
        leg1,2 : first and second leg.
        pdgid  : pdg code of the resonance
        status : status code of the resonance
        '''
        self._leg1 = leg1
        self._leg2 = leg2 
        self._p4 = leg1.p4() + leg2.p4()
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status

    def leg1(self):
        return self._leg1

    def leg2(self):
        return self._leg2
    
    def p4(self):
        return self._p4

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


class AZhAnalyzerZboson(Analyzer):
    '''Builds resonances from an input collection of particles. 
    Example configuration:
    from PhysicsTools.Heppy.analyzers.examples.ResonanceBuilder import ResonanceBuilder
    dimuons = cfg.Analyzer(
       ResonanceBuilder,
       'dimuons',                            
       leg_collection = 'muons',             # input collection
       filter_func = lambda x : True,        # filtering function for input objects. here, take all.
       pdgid = 23                            # pdgid for the resonances, here Z
       )
    This analyzer puts one collection in the event:
    event.dimuons : all resonances, sorted by their distance to the nominal mass
                    corresponding to the specified pdgid
    '''
    def process(self, event, FillCounter=True):

        self.counters.addCounter('23')
        count = self.counters.counter('23')
        count.register('all pairs Mu')
        count.register('accepted pairs Mu')

        count.register('all pairs El')
        count.register('accepted pairs El')


        legsMu = event.muons
        legsMu = [legMu for legMu in legsMu if abs(legMu.eta())<2.4 and legMu.pt()>10]

        legsEl = event.electrons
        legsEl = [legEl for legEl in legsEl if abs(legEl.eta())<2.5]

        legsMu.sort(key=lambda x: x.pt())
        legsMu.reverse()

        legsEl.sort(key=lambda x: x.pt())
        legsEl.reverse()

        for jee in legsMu:
            print jee


        resonancesMu = []
        resonancesEl = []
        #leftOverMuons = []

#        legsMu_testPT = []
        
         #u)>1:
         #   if legsMu[0].pt()>20 and legsMu[1].pt()>10:
         #      legsMu_final.append(legsMu[0])
         #      legsMu_final.append(legsMu[1])

        #for jee2 in legsMu_final:
        #    print jee2

        for leg1, leg2 in itertools.combinations(legsMu,2):
            count.inc('all pairs Mu')
            leg1.associatedVertex = event.goodVertices[0]
            leg2.associatedVertex = event.goodVertices[0]
            if (leg1.charge()+leg2.charge())==0:
                if leg1.muonID('POG_ID_Medium_ICHEP') and abs(leg1.dxy()) < 0.045 and abs(leg1.dz()) < 0.2 and leg1.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15 and leg2.muonID('POG_ID_Medium_ICHEP') and abs(leg2.dxy()) < 0.045 and abs(leg2.dz()) < 0.2 and leg2.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15:
                    count.inc('accepted pairs Mu')
                    resonancesMu.append( Resonance(leg1, leg2, self.cfg_ana.pdgid, 3) )
                #else:
                #    print leg1.relIso()
                #    print leg2.relIso()
            #else:
            #print leg1.charge()+leg2.charge()

        for legE1, legE2 in itertools.combinations(legsEl,2):
            count.inc('all pairs El')
            legE1.associatedVertex = event.goodVertices[0]
            legE2.associatedVertex = event.goodVertices[0]
            if (legE1.charge()+legE2.charge())==0:
                if (legE1.relIso() < 0.15) and (legE2.relIso() < 0.15):
                    count.inc('accepted pairs El')
                    resonancesEl.append( Resonance(legE1, legE2, self.cfg_ana.pdgid, 3) )
             #   else:
             #       print legE1.relIso()
             #       print legE2.relIso()
            #else:
            #    print legE1.charge()+legE2.charge()


        # sorting according to distance to nominal mass
     
        nominal_mass = mass[self.cfg_ana.pdgid]

        resonancesMu.sort(key=lambda x: abs(x.mass()-nominal_mass))
        resonancesEl.sort(key=lambda x: abs(x.mass()-nominal_mass))

        resonances=[]
        resonancesLegs=[]
        #leg1Resonance=[]
        #leg2Resonance=[]

        print 'length of El legs is %d' %len(legsEl)
        print 'resonances El length is %d' %len(resonancesEl)

        print 'length of Mu legs is %d' %len(legsMu)
        print 'resonances Mu length is %d' %len(resonancesMu)
        print 'masses of Mus are'

        for bosoni in resonancesMu:
            print bosoni.mass()

        if resonancesMu and resonancesEl:
            print 'NYT OLI MOLEMMAT, EI TALLENNETA'
            #if abs(resonancesMu[0].mass()-nominal_mass) < abs(resonancesEl[0].mass()-nominal_mass):
            #   print 'nyt muonipari lahempana'
            #   resonances.append(resonancesMu[0])
            #   resonancesLegs.append(resonancesMu[0].leg1)
	    #   resonancesLegs.append(resonancesMu[0].leg2)
            #   #leg1Resonance.append(resonancesMu[0].leg1)
            #   #leg2Resonance.append(resonancesMu[0].leg2)
            #else:
            #   print 'nyt elektronipari lahempana'
            #   #resonances.append(resonancesEl[0])
            print 'resoEl closest mass: '
            print resonancesEl[0].mass()
            print 'resoMu closest mass: '
            print resonancesMu[0].mass()
        elif len(resonancesEl)>0 and len(resonancesMu)==0:
            print 'resoEl closest mass: '
            print resonancesEl[0].mass()
            #resonances.append(resonancesEl[0])
        elif len(resonancesMu)>0 and len(resonancesEl)==0:
            print 'resoMu closest mass: '
            print resonancesMu[0].mass()
            if 60 <= resonancesMu[0].mass() <= 120:
                resonances.append(resonancesMu[0])
                resonancesLegs.append(resonancesMu[0].leg1)
                resonancesLegs.append(resonancesMu[0].leg2)
            #leg1Resonance.append(resonancesMu[0].leg1)
            #leg2Resonance.append(resonancesMu[0].leg2)
        else:
            print 'Nothing'
          
        #if resonances:   
        #    for leg in legs:
        #        if leg == resonances[0].leg1:
        #            print "JALKA ON 1. JALKA"
        #        elif leg == resonances[0].leg2:
        #            print "JALKA ON 2. JALKA"    
        #        else:
        #            print "EI KUMPIKAAN"
        #            if (leg.relIso() < 0.15):
        #                count.inc('left over muons')
        #                print 'ISOLAATIO KUNNOSSA, LAITETAAN TALTEEN'  
        #                leftOverMuons.append(leg)  
        
        print 'resonances length is %d' %len(resonances)
        print resonances
        print 'resonances legs length is  %d' %len(resonancesLegs)
       	print resonancesLegs
        #print 'resonances length is %d' %len(leg2Resonance)
       	#print leg2Resonance



        setattr(event, 'ZbosonLegs', resonancesLegs)
        #setattr(event, 'ZbosonLeg2', leg2Resonance)
        setattr(event, 'Zboson', resonances)

