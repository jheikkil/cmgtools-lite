#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/MMET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data    -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/EEET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/EETT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/MMTT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/MMMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/EEMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/MMEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
  --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2408_FR_EXP/EEEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --xp data   -b EEEM --xf .*MMEM.*;
