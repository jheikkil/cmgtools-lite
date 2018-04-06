import PhysicsTools.HeppyCore.framework.config as cfg

# import all analysers:
# Heppy analyzers
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.core.EventSelector import EventSelector
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer import PileUpAnalyzer
# from PhysicsTools.Heppy.analyzers.gen.GeneratorAnalyzer import GeneratorAnalyzer
from PhysicsTools.Heppy.analyzers.gen.LHEWeightAnalyzer import LHEWeightAnalyzer

# Tau-tau analyzers
from CMGTools.H2TauTau.proto.analyzers.MCWeighter import MCWeighter
from CMGTools.H2TauTau.proto.analyzers.TriggerAnalyzer import TriggerAnalyzer
from CMGTools.H2TauTau.proto.analyzers.JetAnalyzer import JetAnalyzer
from CMGTools.H2TauTau.proto.analyzers.EmbedWeighter import EmbedWeighter
from CMGTools.H2TauTau.proto.analyzers.HTTGenAnalyzer_jaana import HTTGenAnalyzer_jaana
from CMGTools.H2TauTau.proto.analyzers.NJetsAnalyzer import NJetsAnalyzer
from CMGTools.H2TauTau.proto.analyzers.HiggsPtWeighter import HiggsPtWeighter
from CMGTools.H2TauTau.proto.analyzers.VBFAnalyzer import VBFAnalyzer
from CMGTools.H2TauTau.proto.analyzers.RecoilCorrector import RecoilCorrector

# TTH analyzers
from CMGTools.TTHAnalysis.analyzers.ttHhistoCounterAnalyzer import ttHhistoCounterAnalyzer
from CMGTools.TTHAnalysis.analyzers.susyParameterScanAnalyzer import susyParameterScanAnalyzer

puFileMC = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/MC_Spring16_PU25_Startup.root'
# puFileData = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/data_pu_25-07-2016_69p2mb_60.root'
puFileData = '/afs/cern.ch/user/a/anehrkor/public/Data_Pileup_2016_July22.root'


susyCounter = cfg.Analyzer(
    ttHhistoCounterAnalyzer, name="ttHhistoCounterAnalyzer",
    SMS_max_mass=3000,  # maximum mass allowed in the scan
    # SMS_mass_1='genSusyMScan1',  # first scanned mass
    # SMS_mass_2='genSusyMScan2',  # second scanned mass
    SMS_mass_1='genSusyMChargino',  # first scanned mass
    SMS_mass_2='genSusyMNeutralino',  # second scanned mass
    SMS_varying_masses=['genSusyMStau'],  # other mass variables that are expected to change in the tree (e.g., in T1tttt it should be set to ['genSusyMGluino','genSusyMNeutralino'])
    SMS_regexp_evtGenMass='genSusyM.+',
    bypass_trackMass_check=True  # bypass check that non-scanned masses are the same in all events
)

#defined here to be pulled in from channel-specific configs
eventSelector = cfg.Analyzer(
    EventSelector,
    name='EventSelector',
    toSelect=[]
)

lheWeightAna = cfg.Analyzer(
    LHEWeightAnalyzer, name="LHEWeightAnalyzer",
    useLumiInfo=False,
)

#explain what lumisections to use, JSON file attached to the relevant data sample directly
jsonAna = cfg.Analyzer(
    JSONAnalyzer,
    name='JSONAnalyzer',
)

#count events before any selection to normalise samples, used if run heppy
skimAna = cfg.Analyzer(
    SkimAnalyzerCount,
    name='SkimAnalyzerCount'
)

#in principle same as skimAna, used if we have preprocessor
mcWeighter = cfg.Analyzer(
    MCWeighter,
    name='MCWeighter'
)

#include trigger information, triggers added to the samples
triggerAna = cfg.Analyzer(
    TriggerAnalyzer,
    name='TriggerAnalyzer',
    addTriggerObjects=True,
    requireTrigger=True,
    usePrescaled=False
)

#select primary vertices, do not weight them - done my pileup analyzer (based on true number of interactions)
vertexAna = cfg.Analyzer(
    VertexAnalyzer,
    name='VertexAnalyzer',
    fixedWeight=1,
    keepFailingEvents=True,
    verbose=False
)

#Corrects MC pileup to given data pileup.
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer,
    name='PileUpAnalyzer',
    true=True
)

# genAna = GeneratorAnalyzer.defaultConfig

# genAna.savePreFSRParticleIds = [1, 2, 3, 4, 5, 21]

# Save SUSY masses
susyScanAna = cfg.Analyzer(
    susyParameterScanAnalyzer, name="susyParameterScanAnalyzer",
    doLHE=True,
    useLumiInfo=False,
)

#generator analyzer, e.g. save status flags 
httGenAna = cfg.Analyzer(
    HTTGenAnalyzer_jaana,
    name='HTTGenAnalyzer',
    jetCol='slimmedJets',
    channel='',
    genPtCut=8.
)

#jet analyzer
jetAna = cfg.Analyzer(
    JetAnalyzer,
    name='JetAnalyzer',
    jetCol='slimmedJets',
    jetPt=20.,
    jetEta=4.7,
    relaxJetId=False, # relax = do not apply jet ID
    relaxPuJetId=True, # relax = do not apply pileup jet ID
    jerCorr=False,
    #jesCorr = 1., # Shift jet energy scale in terms of uncertainties (1 = +1 sigma)
    puJetIDDisc='pileupJetId:fullDiscriminant',
)

#save variables targeted at VBF Higgs production
vbfAna = cfg.Analyzer(
    VBFAnalyzer,
    name='VBFAnalyzer',
    cjvPtCut=20., # jet pT cut for central jet veto
    Mjj=500., # minimum dijet mass, only used for counting
    deltaEta=3.5  # minimum delta eta, only used for counting
)

#apply recoilCorrs or not
recoilCorr = cfg.Analyzer(
    RecoilCorrector,
    name='RecoilCorrector',
    apply=False
)

embedWeighter = cfg.Analyzer(
    EmbedWeighter,
    name='EmbedWeighter',
    isRecHit=False,
    verbose=False
)

#stich samples where we have separate samples with specific gen cuts
NJetsAna = cfg.Analyzer(
    NJetsAnalyzer,
    name='NJetsAnalyzer',
    fillTree=True,
    verbose=False
)

higgsWeighter = cfg.Analyzer(
    HiggsPtWeighter,
    name='HiggsPtWeighter',
)


###################################################
###                  SEQUENCE                   ###
###################################################
commonSequence = cfg.Sequence([
    #lheWeightAna,
    jsonAna,
    skimAna,
    mcWeighter,
    # genAna,
    # susyScanAna,
    triggerAna, # First analyser that applies selections
    vertexAna,
    httGenAna,
    jetAna,
    #vbfAna,
    recoilCorr,
    pileUpAna,
    #embedWeighter,
    NJetsAna,
    #higgsWeighter
])

