#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/MMET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6     -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/EEET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6    -b EEET --xf .*MMET.*;


python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/MMMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6    -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/EEMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6    -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/MMEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6    -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM.txt A_svFit_constrained 15,0,600 systs_AZh.txt \
-P AZh_MC --skimPath \
--Fs sf/t massesMC_July6/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0708_FR_OBS/EEEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6    -b EEEM --xf .*MMEM.*;
