import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
lumi = 35870.

run_range = (273158, 284044)
label = "_runs%s_%s"%(run_range[0], run_range[1])


###-------DoubleMu------###


DoubleMuon_Run2016B_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016B_03Feb2017_v1"        , "/DoubleMuon/Run2016B-03Feb2017_ver1-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_03Feb2017_v2        = kreator.makeDataComponent("DoubleMuon_Run2016B_03Feb2017_v2"        , "/DoubleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD"        , "CMS", ".*root", json)

DoubleMuon_Run2016C_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016C_03Feb2017_v1"        , "/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016D_03Feb2017_v1"        , "/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016E_03Feb2017_v1"        , "/DoubleMuon/Run2016E-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016F_03Feb2017_v1"        , "/DoubleMuon/Run2016F-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016G_03Feb2017_v1"        , "/DoubleMuon/Run2016G-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)

DoubleMuon_Run2016H_03Feb2017_v1        = kreator.makeDataComponent("DoubleMuon_Run2016H_03Feb2017_v1"        , "/DoubleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_03Feb2017_v2        = kreator.makeDataComponent("DoubleMuon_Run2016H_03Feb2017_v2"        , "/DoubleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"        , "CMS", ".*root", json)
 

###-----DoubleEle-----###


DoubleEG_Run2016B_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016B_03Feb2017_v1"        , "/DoubleEG/Run2016B-03Feb2017_ver1-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016B_03Feb2017_v2        = kreator.makeDataComponent("DoubleEG_Run2016B_03Feb2017_v2"        , "/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"        , "CMS", ".*root", json)

DoubleEG_Run2016C_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016C_03Feb2017_v1"        , "/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016D_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016D_03Feb2017_v1"        , "/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016E_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016E_03Feb2017_v1"        , "/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016F_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016F_03Feb2017_v1"        , "/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016G_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016G_03Feb2017_v1"        , "/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)

DoubleEG_Run2016H_03Feb2017_v1        = kreator.makeDataComponent("DoubleEG_Run2016H_03Feb2017_v1"        , "/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleEG_Run2016H_03Feb2017_v2        = kreator.makeDataComponent("DoubleEG_Run2016H_03Feb2017_v2"        , "/DoubleEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"        , "CMS", ".*root", json)


dataSamples_DoubleMu_AZH = [DoubleMuon_Run2016B_03Feb2017_v1, DoubleMuon_Run2016B_03Feb2017_v2, DoubleMuon_Run2016C_03Feb2017_v1, DoubleMuon_Run2016D_03Feb2017_v1, DoubleMuon_Run2016E_03Feb2017_v1, DoubleMuon_Run2016F_03Feb2017_v1, DoubleMuon_Run2016G_03Feb2017_v1, DoubleMuon_Run2016H_03Feb2017_v1, DoubleMuon_Run2016H_03Feb2017_v2 ]
dataSamples_DoubleEl_AZH = [DoubleEG_Run2016B_03Feb2017_v1, DoubleEG_Run2016B_03Feb2017_v2, DoubleEG_Run2016C_03Feb2017_v1, DoubleEG_Run2016D_03Feb2017_v1, DoubleEG_Run2016E_03Feb2017_v1, DoubleEG_Run2016F_03Feb2017_v1, DoubleEG_Run2016G_03Feb2017_v1, DoubleEG_Run2016H_03Feb2017_v1, DoubleEG_Run2016H_03Feb2017_v2 ]

dataSamples_AZH = dataSamples_DoubleMu_AZH + dataSamples_DoubleEl_AZH

samples = dataSamples_AZH

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True
    comp.lumi = lumi

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
