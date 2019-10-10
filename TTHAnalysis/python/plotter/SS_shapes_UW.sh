#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
python makeShapeCardsSusy.py mcaET_skimDATA.txt cuts_ET_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/MMET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"      -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_skimDATA.txt cuts_ET_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/EEET/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_skimDATA.txt cuts_TT_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/EETT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_skimDATA.txt cuts_TT_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/MMTT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_skimDATA.txt cuts_MT_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/MMMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_skimDATA.txt cuts_MT_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/EEMT/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_skimDATA.txt cuts_EM_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/MMEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_skimDATA.txt cuts_EM_SS.txt A_svFit 60,0,600 systs_AZh.txt \
-P data_SS --skimPath \
--Fs sf/t masses_SS/{cname}.root \
--FMC sf/t scalesMC_July8/{cname}.root \
   --od /afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2102_SS_10_sv/EEEM/Aconstr_HsvFit90 -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>0 && A_svFit<600" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4*zhTrigWeight' -j 6 --neg --xp "ttW,WH,ZH,ttH,WZ,ZZ,GG,triboson,ttZ,AZH300,AZH350,AZH220,AZH240,AZH260,AZH280,AZH320,AZH340,AZH400,SM,data_FR"    -b EEEM --xf .*MMEM.*;
