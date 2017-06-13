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
        self.leg1 = leg1 
        self.leg2 = leg2 
        self._p4 = leg1.p4() + leg2.p4()
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status
    
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


class AZhAnalyzerHboson(Analyzer):
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

        self.counters.addCounter('Hboson')
        count = self.counters.counter('Hboson')
        count.register('all pairs')
        count.register('used pairs')
        count.register('accepted pairs')
 
        legsMu = event.muons
        legsMu = [legMu for legMu in legsMu if self.cfg_ana.filter_func(legMu)]

        resonances = []
        leg1Resonance=[]
        leg2Resonance=[]


        for leg1, leg2 in itertools.combinations(legsMu,2):
            count.inc('all pairs')
            leg1.associatedVertex = event.goodVertices[0]
            leg2.associatedVertex = event.goodVertices[0]
            if event.ZbosonLegs:
                if leg1 in event.ZbosonLegs or leg2 in event.ZbosonLegs:
                #if leg1==event.ZbosonLeg1[0] or leg1==event.ZbosonLeg2[0] or leg2==event.ZbosonLeg1[0] or leg2==event.ZbosonLeg2[0]:
                    print 'OLI KAYTETTY'
                    count.inc('used pairs')
                    print event.ZbosonLegs
                    print event.ZbosonLegs[0]
                    print event.ZbosonLegs[1]
                    print 'tassa leg1'
                    print leg1
                    print 'tassa leg2'
                    print leg2
                    continue
            if (leg1.charge()+leg2.charge())==0:
                if (leg1.relIso() < 0.15) and (leg2.relIso() < 0.15):
                    count.inc('accepted pairs')
                    resonances.append( Resonance(leg1, leg2, self.cfg_ana.pdgid, 3) )

     
        nominal_mass = mass[self.cfg_ana.pdgid]

        resonances.sort(key=lambda x: abs(x.mass()-nominal_mass))

        print 'length of Mu legs is %d' %len(legsMu)
        print 'resonances Mu length is %d' %len(resonances)

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
        print 'resonances leg1 length is %d' %len(leg1Resonance)
       	print leg1Resonance
        print 'resonances length is %d' %len(leg2Resonance)
       	print leg2Resonance



        setattr(event, 'Hbosonleg1', leg1Resonance)
        setattr(event, 'Hbosonleg2', leg2Resonance)
        setattr(event, 'Hboson', resonances)

