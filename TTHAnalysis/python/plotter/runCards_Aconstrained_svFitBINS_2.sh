#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/EETT/A_svFit_constrained_HsvFitBINS_LT50_0080 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && H_svFit < 80  " \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/MMTT/A_svFit_constrained_HsvFitBINS_LT50_0080 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && H_svFit < 80  " \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMTT --xf .*EETT.*;


python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/EETT/A_svFit_constrained_HsvFitBINS_LT50_80140 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>=80 && H_svFit < 140  " \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/MMTT/A_svFit_constrained_HsvFitBINS_LT50_80140 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>=80 && H_svFit < 140  " \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMTT --xf .*EETT.*;


python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/EETT/A_svFit_constrained_HsvFitBINS_LT50_140180 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>=140 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May21/MMTT/A_svFit_constrained_HsvFitBINS_LT50_140180 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>=140 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMTT --xf .*EETT.*;


