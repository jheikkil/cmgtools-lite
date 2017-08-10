import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.config import printComps
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# Tau-tau analyzers
from PhysicsTools.Heppy.analyzers.core.all import TriggerMatchAnalyzer


from CMGTools.H2TauTau.proto.analyzers.MuMuAnalyzer import MuMuAnalyzer
from CMGTools.H2TauTau.proto.analyzers.CountEvents import CountEvents
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerMuons import AZhAnalyzerMuons
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerZboson import AZhAnalyzerZboson      
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzer import AZhAnalyzer
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerHboson import AZhAnalyzerHboson
from CMGTools.H2TauTau.proto.analyzers.LeptonSelector import LeptonSelector
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZh import H2TauTauTreeProducerAZh
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEEMT import H2TauTauTreeProducerAZhEEMT
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMMET import H2TauTauTreeProducerAZhMMET
from CMGTools.H2TauTau.proto.analyzers.LeptonWeighter import LeptonWeighter
from CMGTools.H2TauTau.proto.analyzers.SVfitProducer import SVfitProducer

from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
from CMGTools.H2TauTau.proto.analyzers.FileCleaner import FileCleaner

from CMGTools.H2TauTau.proto.samples.spring16.htt_common import backgrounds_mu, sm_signals, mssm_signals, data_single_muon, sync_list, DY_sync_list, WZ_sync_list

from CMGTools.RootTools.utils.splitFactor import splitFactor
from CMGTools.H2TauTau.proto.samples.spring16.triggers_muMu import mc_triggers, mc_triggerfilters
from CMGTools.H2TauTau.proto.samples.spring16.triggers_muMu import data_triggers, data_triggerfilters

from CMGTools.RootTools.samples.autoAAAconfig import autoAAA

# common configuration and sequence
from CMGTools.H2TauTau.htt_ntuple_base_cff import commonSequence, httGenAna, triggerAna, jetAna, puFileData, puFileMC, eventSelector

# mu-mu specific configuration settings
#nEvents = getHeppyOption('nEvents', 100)
production = getHeppyOption('production', False)
pick_events = getHeppyOption('pick_events', False)
syncntuple = getHeppyOption('syncntuple', True)
cmssw = getHeppyOption('cmssw', False)
computeSVfit = getHeppyOption('computeSVfit', False)
data = getHeppyOption('data', False)
reapplyJEC = getHeppyOption('reapplyJEC', True)
applyIDISO = getHeppyOption('applyIDISO', False)

#if getHeppyOption('test'):
#    test = getHeppyOption('test')


inputSample = cfg.MCComponent(
    'test_component',
    files = '/afs/cern.ch/work/j/jheikkil/MSSM2017/CMSSW_8_0_25/src/CMGTools/H2TauTau/cfgPython/AZh/pickevents.root'  # returns a list of file for this release
    # a list of local or xrootd files can be specified by hand.
)


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
        jetAna.recalibrateJets = False
        jetAna.mcGT = 'Summer16_23Sep2016V3_MC'
        jetAna.dataGT = 'Summer16_23Sep2016HV3_DATA'
# Define mu-mu specific modules

#CountEvents = cfg.Analyzer(
#    CountEvents,
#    name='CountEvents',     
#    jetCol='slimmedJets',
#    channel='',
#    genPtCut=8.
#)

#AZhAnaMuons = cfg.Analyzer(
#    AZhAnalyzerMuons,
#    name='AZhAnalyzerMuons',
#)


LepSelector = cfg.Analyzer(
    LeptonSelector,
    name='LepSelector',
    applyIDISO = True if applyIDISO else False,
    doElectronScaleCorrections=False,
    #isMC = False if data else True,
)

#LepSelector.doElectronScaleCorrections = {

#        'data' : 'EgammaAnalysis/ElectronTools/data/Moriond17_23Jan_ele',

#        'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',

#                      'gedelectron_p4combination_25ns'),

#        'isSync': syncntuple,
#        'isMC' : False if data else True
#}

trigMatcherEls = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcherEls",
    label='Els',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    trgObjSelectors = [ lambda t : t.path("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",1,0)],
    collToMatch = 'electrons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
    collMatchDRCut = 0.5,
    univoqueMatching = True,
    id = 11,
    pt1 = 24,
    pt2 = 13,
    verbose = False,
)

trigMatcherMus = trigMatcherEls.clone(
    name="trigMatcherMus",
    label='Mus',
    collToMatch = 'muons',
    trgObjSelectors = [ lambda t : t.path("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",1,0) or t.path("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",1,0)],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    id = 13,
    pt1 = 18,
    pt2 = 10,
)


AZhAnaZboson = cfg.Analyzer(
    AZhAnalyzer,
    name='Zdimuon',
    pdgid = 23,
    applyIDISO = True if applyIDISO else False,
    MC = False if data else True,
    filter_func = lambda x : True,
)


#triggerCuts = trigMatcherEls.clone(
#    name="triggerCuts",
#    label='triggerCuts',
#    applyCuts = True,
#)


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

EEMTtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhEEMT,
    name='H2TauTauTreeProducerAZhEEMT',
    addMoreJetInfo=True,
    varStyle='sync'
)

MMETtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMMET,
    name='H2TauTauTreeProducerAZhMMET',
    addMoreJetInfo=True,
    varStyle='sync'
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
samples = backgrounds_mu + sm_signals + mssm_signals + sync_list + [inputSample]
#samples = sync_list + [inputSample]
inputJaana = sync_list

###################################################
###              ASSIGN PU to MC                ###
###################################################
for mc in samples:
    mc.puFileData = puFileData
    mc.puFileMC = puFileMC
    if hasattr(mc, 'dataset'):
        if 'PUSpring16' in mc.dataset:
            print 'Attaching Spring 16 pileup to sample', mc.dataset
        # mc.puFileData = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/data_pu_25-07-2016_69p2mb_60.root'
            mc.puFileMC = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/MC_Spring16_PU25_Startup_800.root'


# Additional samples

# split_factor = 3e4
split_factor = 2e5 


sequence=commonSequence
#sequence.insert(sequence.index(httGenAna), MuMuAna)
#sequence.insert(sequence.index(MuMuAna), AZhAnaMuons)
#sequence.insert(sequence.index(httGenAna), CountEvents)
#sequence.insert(sequence.index(jetAna), AZhAnaZboson)
sequence.insert(sequence.index(httGenAna), LepSelector)
sequence.insert(sequence.index(httGenAna), trigMatcherEls)
sequence.insert(sequence.index(httGenAna), trigMatcherMus)
sequence.insert(sequence.index(httGenAna), AZhAnaZboson)
#sequence.insert(sequence.index(httGenAna), triggerCuts)
#sequence.append(muonWeighter1)
#sequence.append(muonWeighter2)
if computeSVfit:
    sequence.append(svfitProducer)
sequence.append(treeProducer)
sequence.append(EEMTtreeProducer)
sequence.append(MMETtreeProducer)
if syncntuple:
    sequence.append(syncTreeProducer)

if pick_events:
    eventSelector.toSelect = []
    sequence.insert(0, eventSelector)

if not cmssw:
    module = [s for s in sequence if s.name == 'MCWeighter'][0]
    sequence.remove(module)

test = getHeppyOption('test')

#DYtest = getHeppyOption('DYtest')
#if DYtest:
#    selectedComponents=DY_sync_list
#else:

selectedComponents=sync_list

#selectedComponents=[inputSample]

#selectedComponents=DY_sync_list
#selectedComponents=WZ_sync_list

if test == '1':
    #print "MPOO"
    #selectedComponents = sync_list 
    #selectedComponents = selectedComponents[:1]
    #print selectedComponents[0]
    comp = selectedComponents[0]
    comp.files = comp.files[:1]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]
elif test == '2':
    #from CMGTools.Production.promptRecoRunRangeFilter import filterWithCollection
    #selectedComponents = []
    for comp in selectedComponents:
        #if comp.isData: comp.files = filterWithCollection(comp.files, [274315,275658,276363,276454])
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
        print comp
        #nev = getattr(comp, 'dataset_entries', 0)
       	#print "number of entries:" 
        #print nev


elif test != None:
    raise RuntimeError, "Unknown test %r" % test

if not production and test == None:
    #print "TUTII"
    #comp = [b for b in backgrounds_mu if b.name == 'DYJetsToLL_M50_LO'][0]
    # comp = data_list[0] if data else sync_list[0]
    #comp = selectedComponents[0]
    #selectedComponents = [comp]
    print 'OK JAAANAAAAA'
    #comp = inputJaana[0]
    #for b in inputJaana:
    for comp in selectedComponents:
    #for i in xrange(len(inputJaana)):
        #print inputJaana[i]
        #comp = inputJaana[i]
        comp.splitFactor = 100
        #selectedComponents += [comp]
   # comp2 = inputJaana[1]
    #comp.splitFactor = 1#00
  #  comp2.splitFactor = 1
    # comp.files = comp.files[14:16]

#test = getHeppyOption('test')
#if test == '1':
#    comp = selectedComponents[0]
#    comp.files = comp.files[:1]
#    comp.splitFactor = 1
#    comp.fineSplitFactor = 1
#    selectedComponents = [ comp ]
#elif test == '2':
#    from CMGTools.Production.promptRecoRunRangeFilter import filterWithCollection
#    for comp in selectedComponents:
#        if comp.isData: comp.files = filterWithCollection(comp.files, [274315,275658,276363,276454])
#        comp.files = comp.files[:1]
#        comp.splitFactor = 1
#        comp.fineSplitFactor = 1
#elif test != None:
#    raise RuntimeError, "Unknown test %r" % test

#autoAAA(selectedComponents)

print "TASSSA SEQUAENCE:"
print sequence


preprocessor = None
if cmssw:
    sequence.append(fileCleaner)
    preprocessor = CmsswPreprocessor(
        "$CMSSW_BASE/src/CMGTools/H2TauTau/prod/h2TauTauMiniAOD_mumu_data_cfg.py" if data else "$CMSSW_BASE/src/CMGTools/H2TauTau/prod/h2TauTauMiniAOD_mumu_cfg.py", addOrigAsSecondary=False)

#maxEvents=100

# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events

#Events.options.maxEvents=100

config = cfg.Config(components=selectedComponents,
                    sequence=sequence,
                    services=[],
                    preprocessor=preprocessor,
                    events_class=Events
                    )

#options = cfg.Options(maxEvents=100,
#                     )

printComps(config.components, True)

