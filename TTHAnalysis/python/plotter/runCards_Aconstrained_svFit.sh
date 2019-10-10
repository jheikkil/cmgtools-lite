#!/bin/bash

#######################################################OTHER A BOSON MASSES#####################################################
	
for mass in $(cat HsvFitmasses.txt); 
do python makeShapeCardsSusy.py mcaET_VZtest_FRdata.txt cuts_ET.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/MMET/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6  --xp data -b MMET --xf .*EEET.*;

python makeShapeCardsSusy.py mcaET_VZtest_FRdata.txt cuts_ET.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/EEET/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEET --xf .*MMET.*;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/EETT/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EETT --xf .*MMTT.*;

python makeShapeCardsSusy.py mcaTT_VZtest_FRdata.txt cuts_TT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/MMTT/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMTT --xf .*EETT.*;

python makeShapeCardsSusy.py mcaMT_VZtest_FRdata.txt cuts_MT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/MMMT/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMMT --xf .*EEMT.*;

python makeShapeCardsSusy.py mcaMT_VZtest_FRdata.txt cuts_MT.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/EEMT/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEMT --xf .*MMMT.*;

python makeShapeCardsSusy.py mcaEM_VZtest_FRdata.txt cuts_EM.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/MMEM/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b MMEM --xf .*EEEM.*;

python makeShapeCardsSusy.py mcaEM_VZtest_FRdata.txt cuts_EM.txt A_svFit_constrained 10,200,600 systs.txt \
-P /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/NTuplesBKG/ --skimPath \
--Fs sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/massTrees/{cname}.root \
--FMC sf/t /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/CMGTools/TTHAnalysis/python/plotter/scaleFactorsMay04/{cname}.root \
--asimov --od /afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May08/EEEM/A_svFit_constrained_HsvFitZmass$mass -l 35.9 -A "entry point" zeroMass "H_svFit_constrained > 0 && H_svFit>90 && H_svFit < 180 && abs(91.1876-m_vis)<$mass" \
-W 'weight_gen*puweight*electronSF_1*electronSF_2*electronSF_3*electronSF_4*muonSF_1*muonSF_2*muonSF_3*muonSF_4*tauSF_3*tauSF_4' -j 6 --xp data -b EEEM --xf .*MMEM.*;
done;
