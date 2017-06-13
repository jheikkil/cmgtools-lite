import ROOT


from itertools import product
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Muon
from PhysicsTools.Heppy.physicsobjects.Electron import Electron
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.HeppyCore.utils.deltar import deltaR2


class AZhAnalyzerMuons(Analyzer):

    def declareHandles(self):
        super(AZhAnalyzerMuons, self).declareHandles()
        self.handles['muons'] = AutoHandle(
            'slimmedMuons',
            'std::vector<pat::Muon>'
            )

        self.handles['electrons'] = AutoHandle(
            'slimmedElectrons',
            'std::vector<pat::Electron>'
            )        

        self.handles['taus'] = AutoHandle(
                'slimmedTaus',
                'std::vector<pat::Tau>'
            )
        
        self.handles['met'] = AutoHandle(
                'slimmedMETs',
                'std::vector<pat::MET>'
            )
  
    def process(self, event):
        super(AZhAnalyzerMuons, self).readCollections(event.input)
        muons = map(Muon, self.handles['muons'].product())  
        electrons = map(Electron, self.handles['electrons'].product())
        taus = map(Tau, self.handles['taus'].product())
        met = self.handles['met'].product()[0]

        setattr(event, 'muons', muons)
        setattr(event, 'electrons', electrons)
        setattr(event, 'taus', taus) 
        setattr(event, 'met', met)

