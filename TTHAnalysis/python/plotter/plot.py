from ROOT import TFile
tfile = TFile.Open("/afs/cern.ch/work/j/jheikkil/combineHarvester/CMSSW_8_1_0/src/CombineHarvester/CombineTools/fitDiagnostics/fitDiagnosticslltt_300.root")
tfile.cd()
for h in tfile.GetListOfKeys():
    h = h.ReadObj()
    print h.ClassName(), h.GetName()
