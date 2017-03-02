import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.config import printComps
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# Tau-tau analyzers
from CMGTools.H2TauTau.proto.analyzers.MuMuAnalyzer import MuMuAnalyzer
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerMuons import AZhAnalyzerMuons
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerZboson import AZhAnalyzerZboson      
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzer import AZhAnalyzer
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerHboson import AZhAnalyzerHboson
from CMGTools.H2TauTau.proto.analyzers.HiggsAnalyzer import HiggsAnalyzer
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZh import H2TauTauTreeProducerAZh
from CMGTools.H2TauTau.proto.analyzers.LeptonWeighter import LeptonWeighter
from CMGTools.H2TauTau.proto.analyzers.SVfitProducer import SVfitProducer

from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
from CMGTools.H2TauTau.proto.analyzers.FileCleaner import FileCleaner

from CMGTools.H2TauTau.proto.samples.spring16.htt_common import backgrounds_mu, sm_signals, mssm_signals, data_single_muon, sync_list

from CMGTools.RootTools.utils.splitFactor import splitFactor
from CMGTools.H2TauTau.proto.samples.spring16.triggers_muMu import mc_triggers, mc_triggerfilters
from CMGTools.H2TauTau.proto.samples.spring16.triggers_muMu import data_triggers, data_triggerfilters

from CMGTools.RootTools.samples.autoAAAconfig import autoAAA

# common configuration and sequence
from CMGTools.H2TauTau.htt_ntuple_base_cff_jaana import commonSequence, httGenAna, triggerAna, jetAna, puFileData, puFileMC, eventSelector

# mu-mu specific configuration settings
production = getHeppyOption('production', False)
pick_events = getHeppyOption('pick_events', False)
syncntuple = getHeppyOption('syncntuple', True)
cmssw = getHeppyOption('cmssw', False)
computeSVfit = getHeppyOption('computeSVfit', False)
data = getHeppyOption('data', False)
reapplyJEC = getHeppyOption('reapplyJEC', True)

httGenAna.channel = ''

# Just to be sure
if production:
    syncntuple = False
    pick_events = False

if reapplyJEC:
    if cmssw:
        jetAna.jetCol = 'patJetsReapplyJEC'
        httGenAna.jetCol = 'patJetsReapplyJEC'
    else:
        jetAna.recalibrateJets = True

# Define mu-mu specific modules

#AZhAnaMuons = cfg.Analyzer(
#    AZhAnalyzerMuons,
#    name='AZhAnalyzerMuons',
#)

AZhAnaZboson = cfg.Analyzer(
    AZhAnalyzer,
    name='Zdimuon',
    pdgid = 23,
    filter_func = lambda x : True,
)

#AZhAnaHboson = cfg.Analyzer(
#    HiggsAnalyzer,
#    name='HiggsAnalyzer',
#    pdgid=25,
    # triggerMap = pathsAndFilters,
#    verbose=False    
    #filter_func = lambda x : True,
#)


#MuMuAna = cfg.Analyzer(
#    MuMuAnalyzer,
#    name='MuMuAnalyzer',
#    pt1=23,
#    eta1=2.4,
#    iso1=0.15,
#    pt2=10,
#    eta2=2.4,
#    iso2=0.15,
#    m_min=10,
#    m_max=99999,
#    dR_min=0.5,
    # triggerMap = pathsAndFilters,
#    from_single_objects=True,
#    verbose=False
#)

#if cmssw:
#    MuMuAna.from_single_objects = True


#muonWeighter1 = cfg.Analyzer(
#    LeptonWeighter,
#    name='LeptonWeighter_mu_1',
#    dataEffFiles={
#        'trigger':'$CMSSW_BASE/src/CMGTools/H2TauTau/data/Muon_IsoMu22_eff_Spring16.root',
#    },
#    scaleFactorFiles={
#        'idiso':'$CMSSW_BASE/src/CMGTools/H2TauTau/data/Muon_IdIso0p1_spring16.root',
#    },
#    lepton='leg1',
#    disable=False
#)

#muonWeighter2 = cfg.Analyzer(
#    LeptonWeighter,
#    name='LeptonWeighter_mu_2',
#    scaleFactorFiles={
#        'idiso':'$CMSSW_BASE/src/CMGTools/H2TauTau/data/Muon_IdIso0p1_spring16.root',
#    },
#    lepton='leg2',
#    disable=False
#)

treeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZh,
    name='H2TauTauTreeProducerAZh',
    addMoreJetInfo=True
)

syncTreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZh,
    name='H2TauTauSyncTreeProducerAZh',
    varStyle='sync'
)

#svfitProducer = cfg.Analyzer(
#    SVfitProducer,
#    name='SVfitProducer',
#    integration='VEGAS',
    # integration='MarkovChain',
    # debug=True,
#    l1type='muon',
#    l2type='muon'
#)

fileCleaner = cfg.Analyzer(
    FileCleaner,
    name='FileCleaner'
)

# Minimal list of samples
samples = backgrounds_mu + sm_signals + mssm_signals + sync_list
inputJaana = sync_list
# Additional samples

# split_factor = 3e4
split_factor = 1 #2e5


sequence=commonSequence
#sequence.insert(sequence.index(httGenAna), MuMuAna)
#sequence.insert(sequence.index(MuMuAna), AZhAnaMuons)
sequence.insert(sequence.index(httGenAna), AZhAnaZboson)
#sequence.insert(sequence.index(MuMuAna), AZhAnaHboson)
#sequence.append(muonWeighter1)
#sequence.append(muonWeighter2)
if computeSVfit:
    sequence.append(svfitProducer)
sequence.append(treeProducer)
if syncntuple:
    sequence.append(syncTreeProducer)

if pick_events:
    eventSelector.toSelect = []
    sequence.insert(0, eventSelector)

if not cmssw:
    module = [s for s in sequence if s.name == 'MCWeighter'][0]
    sequence.remove(module)

if not production:
    #comp = [b for b in backgrounds_mu if b.name == 'DYJetsToLL_M50_LO'][0]
    # comp = data_list[0] if data else sync_list[0]
    #comp = selectedComponents[0]
    #selectedComponents = [comp]
    print 'OK JAAANAAAAA'
    comp = inputJaana[0]
    comp.splitFactor = 1#00
    # comp.files = comp.files[14:16]

#autoAAA(selectedComponents)

print "TASSSA SEQUAENCE:"
print sequence

preprocessor = None
if cmssw:
    sequence.append(fileCleaner)
    preprocessor = CmsswPreprocessor(
        "$CMSSW_BASE/src/CMGTools/H2TauTau/prod/h2TauTauMiniAOD_mumu_data_cfg.py" if data else "$CMSSW_BASE/src/CMGTools/H2TauTau/prod/h2TauTauMiniAOD_mumu_cfg.py", addOrigAsSecondary=False)

# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config(components=inputJaana,
                    sequence=sequence,
                    services=[],
                    preprocessor=preprocessor,
                    events_class=Events
                    )

printComps(config.components, True)

