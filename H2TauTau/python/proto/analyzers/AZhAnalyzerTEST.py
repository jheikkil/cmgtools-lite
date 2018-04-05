import ROOT


from itertools import product
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon


class AZhAnalyzerTEST(Analyzer):

    def declareHandles(self):
        print 'JEE'
        super(AZhAnalyzerTEST, self).declareHandles()
        self.handles['muons'] = AutoHandle(
            'slimmedMuons',
            'std::vector<pat::Muon>'
            )
        
    def process(self, event):
        print 'HURRAAAAAAAA'        
        super(AZhAnalyzerTEST, self).readCollections(event.input)
        event.muons = map(Muon, self.handles['muons'].product())  
        
     


