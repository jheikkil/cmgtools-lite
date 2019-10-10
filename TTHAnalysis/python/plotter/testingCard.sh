#!/bin/bash

#######################################################AVIS#####################################################

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/MMET/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/EEET/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/EETT/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/MMTT/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/MMMT/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/EEMT/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/MMEM/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_vis 10,150,550 systs_AZh.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od testingCards/EEEM/A_vis -l 35.9 \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEEM --xf .*MMEM.*;
