#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET_SS.txt H_LT 8,30,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/MMET/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6   -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET_SS.txt H_LT 8,30,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/EEET/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT_SS.txt H_LT 7,40,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/EETT/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT_SS.txt H_LT 7,40,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/MMTT/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT_SS.txt H_LT 8,30,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/MMMT/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT_SS.txt H_LT 8,30,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/EEMT/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM_SS.txt H_LT 9,20,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/MMEM/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM_SS.txt H_LT 9,20,110 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
 --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/SS_July24/EEEM/H_LT -l 35.9  \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6  -b EEEM --xf .*MMEM.*;

