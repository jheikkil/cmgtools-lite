
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.config import printComps
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# Tau-tau analyzers
from PhysicsTools.Heppy.analyzers.core.all import TriggerMatchAnalyzer
from PhysicsTools.Heppy.analyzers.core.all import TriggerBitFilter

from CMGTools.H2TauTau.proto.analyzers.MuMuAnalyzer import MuMuAnalyzer
from CMGTools.H2TauTau.proto.analyzers.CountEvents import CountEvents
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerMuons import AZhAnalyzerMuons
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerZboson import AZhAnalyzerZboson      
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzer import AZhAnalyzer
from CMGTools.H2TauTau.proto.analyzers.AZhAnalyzerHboson import AZhAnalyzerHboson
from CMGTools.H2TauTau.proto.analyzers.LeptonSelector import LeptonSelector
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZh import H2TauTauTreeProducerAZh

from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEEMT import H2TauTauTreeProducerAZhEEMT
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEEET import H2TauTauTreeProducerAZhEEET
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEETT import H2TauTauTreeProducerAZhEETT
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEEEM import H2TauTauTreeProducerAZhEEEM


from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhEE_FR import H2TauTauTreeProducerAZhEE_FR
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMM_FR import H2TauTauTreeProducerAZhMM_FR


from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMMMT import H2TauTauTreeProducerAZhMMMT
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMMET import H2TauTauTreeProducerAZhMMET
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMMTT import H2TauTauTreeProducerAZhMMTT
from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducerAZhMMEM import H2TauTauTreeProducerAZhMMEM



from CMGTools.H2TauTau.proto.analyzers.LeptonWeighter import LeptonWeighter
from CMGTools.H2TauTau.proto.analyzers.SVfitProducer import SVfitProducer

from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
from CMGTools.H2TauTau.proto.analyzers.FileCleaner import FileCleaner

from CMGTools.H2TauTau.proto.samples.spring16.htt_common import backgrounds_mu, sm_signals, mssm_signals, data_single_muon, sync_list, DY_sync_list, WZ_sync_list, AZH_control, AZH_data, ZZ_control2, AZH_tight, AZH_test, AZH_masses, DY_inc, AZH_data_single
from CMGTools.H2TauTau.proto.samples.spring16.htt_common import *



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
applyIDISO = getHeppyOption('applyIDISO', False) #if you want to run control plots/signal, select true
FAKERATE = getHeppyOption('FAKERATE', False)


#inputSample = cfg.MCComponent(
#    'test_component',
#    files = '/afs/cern.ch/work/j/jheikkil/MSSM2017/CMSSW_8_0_25/src/CMGTools/H2TauTau/cfgPython/AZh/pickevents.root'  # returns a list of file for this release
#    # a list of local or xrootd files can be specified by hand.
#)


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


LepSelector = cfg.Analyzer(
    LeptonSelector,
    name='LepSelector',
    applyIDISO = True if applyIDISO else False,
    doElectronScaleCorrections=False,
    #ofakeRate = True if FAKERATE else False,
    #isMC = False if data else True,
)


trigMatcherEls = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcherEls",
    label='Els',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    trgObjSelectors = [ lambda t : t.path("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",1,0) or t.path("HLT_Ele27_WPTight_Gsf_v*",1,0)],
    collToMatch = 'electrons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
    collMatchDRCut = 0.5,
    univoqueMatching = True,
    id = 11,
    pt1 = 24,
    pt2 = 13,
    verbose = False,
    data = True if data else False,
    ##name = comp.name
    ##dataName = comp.name,

)

trigMatcherMusDouble = trigMatcherEls.clone(
    name="trigMatcherMusDouble",
    label='Mus',
    collToMatch = 'muons',
    trgObjSelectors = [ lambda t : t.path("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",1,0) or t.path("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",1,0)],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    id = 13,
    pt1 = 18,
    pt2 = 10,
    data = True if data else False,
    ##dataName = comp.name,
)	

trigMatcherMusSingle = trigMatcherMusDouble.clone(
    name="trigMatcherMusSingle",
    label='Mus',
    collToMatch = 'muons',
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu24_v*",1,0) or t.path("HLT_IsoTkMu24_v*",1,0)],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    id = 13,
    pt1 = 18,
    pt2 = 10,
    data = True if data else False,
    ##dataName = comp.name,
)


AZhAnaZboson = cfg.Analyzer(
    AZhAnalyzer,
    name='Zdimuon',
    pdgid = 23,
    applyIDISO = True if applyIDISO else False,
    MC = False if data else True,
    FAKERATE = True if FAKERATE else False,
    filter_func = lambda x : True,
)



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

EEETtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhEEET,
    name='H2TauTauTreeProducerAZhEEET',
    addMoreJetInfo=True,
    varStyle='sync'
)


EETTtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhEETT,
    name='H2TauTauTreeProducerAZhEETT',
    addMoreJetInfo=True,
    varStyle='sync'
)


EEEMtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhEEEM,
    name='H2TauTauTreeProducerAZhEEEM',
    addMoreJetInfo=True,
    varStyle='sync'
)


MMETtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMMET,
    name='H2TauTauTreeProducerAZhMMET',
    addMoreJetInfo=True,
    varStyle='sync'
)

MMMTtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMMMT,
    name='H2TauTauTreeProducerAZhMMMT',
    addMoreJetInfo=True,
    varStyle='sync'
)


MMTTtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMMTT,
    name='H2TauTauTreeProducerAZhMMTT',
    addMoreJetInfo=True,
    varStyle='sync'
)


MMEMtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMMEM,
    name='H2TauTauTreeProducerAZhMMEM',
    addMoreJetInfo=True,
    varStyle='sync'
)


EE_FRtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhEE_FR,
    name='H2TauTauTreeProducerAZhEE_FR',
    addMoreJetInfo=True,
    varStyle='sync'
)


MM_FRtreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZhMM_FR,
    name='H2TauTauTreeProducerAZhMM_FR',
    addMoreJetInfo=True,
    varStyle='sync'
)


syncTreeProducer = cfg.Analyzer(
    H2TauTauTreeProducerAZh,
    name='H2TauTauSyncTreeProducerAZh',
    varStyle='sync'
)


fileCleaner = cfg.Analyzer(
    FileCleaner,
    name='FileCleaner'
)

# Minimal list of samples
samples=[]
#samples = DY_all
#samples = ttZ_control
#samples = DY_inc
#samples = backgrounds_mu + sm_signals + mssm_signals + AZH_control
##samples = [inputSample]
samples = AZH_control
##samples = AZH_masses
##samples = sync_list
#inputJaana = sync_list

###################################################
###              ASSIGN PU to MC                ###
###################################################
if samples:
    for mc in samples:
        mc.puFileData = puFileData
        mc.puFileMC = puFileMC
        ##print mc.dataset
        if hasattr(mc, 'dataset'):
            if 'PUSpring16' in mc.dataset:
                print 'Attaching Spring 16 pileup to sample', mc.dataset
        # mc.puFileData = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/data_pu_25-07-2016_69p2mb_60.root'
                mc.puFileMC = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/MC_Spring16_PU25_Startup_800.root'


# Additional samples

# split_factor = 3e4
split_factor = 2e5 


sequence=commonSequence
sequence.insert(sequence.index(httGenAna), LepSelector)
sequence.insert(sequence.index(httGenAna), trigMatcherEls)
sequence.insert(sequence.index(httGenAna), trigMatcherMusDouble)
sequence.insert(sequence.index(httGenAna), trigMatcherMusSingle)
sequence.insert(sequence.index(httGenAna), AZhAnaZboson)
if computeSVfit:
    sequence.append(svfitProducer)

test = getHeppyOption('test')

if syncntuple and (test==None or test=='1') and FAKERATE:
    sequence.append(EE_FRtreeProducer)
    sequence.append(MM_FRtreeProducer)

if syncntuple and (test==None or test=='1' or test=='2') and not FAKERATE:
    sequence.append(EEMTtreeProducer)
    sequence.append(EEETtreeProducer)
    sequence.append(EETTtreeProducer)
    sequence.append(EEEMtreeProducer)

    sequence.append(MMMTtreeProducer)
    sequence.append(MMETtreeProducer)
    sequence.append(MMTTtreeProducer)
    sequence.append(MMEMtreeProducer)


if pick_events:
    eventSelector.toSelect = []
    sequence.insert(0, eventSelector)

if not cmssw:
    module = [s for s in sequence if s.name == 'MCWeighter'][0]
    sequence.remove(module)


#selectedComponents=ZZ_control2
#selectedComponents=AZH_tight
#selectedComponents=AZH_control
#selectedComponents=[inputSample]
selectedComponents=samples
#selectedComponents=AZH_data
#selectedComponents=DY_inc
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
    #print "Component name:"
    #print comp.name
elif test == '2':
    #from CMGTools.Production.promptRecoRunRangeFilter import filterWithCollection
    #selectedComponents = []
    for comp in selectedComponents:
        #if comp.isData: comp.files = filterWithCollection(comp.files, [274315,275658,276363,276454])
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
  #      print comp
        #nev = getattr(comp, 'dataset_entries', 0)
       	#print "number of entries:" 
        #print nev
elif test == '3':
    split_factor=1 

elif test != None:
    raise RuntimeError, "Unknown test %r" % test

if not production and not data and test == None:
    #print "TUTII"
    #comp = [b for b in backgrounds_mu if b.name == 'DYJetsToLL_M50_LO'][0]
    # comp = data_list[0] if data else sync_list[0]
    #comp = selectedComponents[0]
    #selectedComponents = [comp]
    #print 'OK JAAANAAAAA'
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

autoAAA(selectedComponents)

#print "TASSSA SEQUAENCE:"
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

