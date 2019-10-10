#!/bin/bash

#######################################################AVIS#####################################################

python makeShapeCardsSusy.py mcaET_VZtest_FRdata.txt cuts_ET_SS.txt LT 8,30,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/MMET/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b MMET --xf .*EEET.* ;

python makeShapeCardsSusy.py mcaET_VZtest_FRdata.txt cuts_ET_SS.txt LT 8,30,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/EEET/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b EEET --xf .*MMET.* ;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT_SS.txt LT 7,40,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/EETT/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b EETT --xf .*MMTT.* ;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT_SS.txt LT 7,40,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/MMTT/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b MMTT --xf .*EETT.* ;

python makeShapeCardsSusy.py mcaMT_VZtest_FRdata.txt cuts_MT_SS.txt LT 8,30,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/MMMT/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b MMMT --xf .*EEMT.* ;

python makeShapeCardsSusy.py mcaMT_VZtest_FRdata.txt cuts_MT_SS.txt LT 8,30,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/EEMT/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b EEMT --xf .*MMMT.* ;

python makeShapeCardsSusy.py mcaEM_VZtest_FRdata.txt cuts_EM_SS.txt LT 9,20,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/MMEM/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b MMEM --xf .*EEEM.* ;

python makeShapeCardsSusy.py mcaEM_VZtest_FRdata.txt cuts_EM_SS.txt LT 9,20,110 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_June07/EEEM/LT -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6   -b EEEM --xf .*MMEM.* ;

