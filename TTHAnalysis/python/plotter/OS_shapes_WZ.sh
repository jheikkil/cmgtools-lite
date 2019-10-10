#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--FMC sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ       -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_June22.txt cuts_ET_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EETT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_June22.txt cuts_TT_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMTT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_June22.txt cuts_MT_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_June22.txt cuts_EM_OS.txt A_svFit_constrained 30,0,600 systs_AZh.txt \
-P MC_OS_relaxed --skimPath \
--Fs sf/t masses_OS/{cname}.root \
--FMC sf/t scales_OS/{cname}.root \
   --asimov --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && A_svFit_constrained<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg -p WZ     -b EEEM --xf .*MMEM.*;
