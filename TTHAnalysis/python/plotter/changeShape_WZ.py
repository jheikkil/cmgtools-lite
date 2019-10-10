
import ROOT

newFile_map = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}



file_map_SS = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


file_map_OS = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


#keys = ["eett", "mmtt"]
for channel in file_map_SS.keys() :


    print channel

    inName = file_map_SS[ channel ]
    inName_WZ = file_map_OS[ channel ]
    outName = newFile_map[ channel ]    

    inFile = ROOT.TFile( inName, 'READ' )
    h_SS_forObs = inFile.Get( "x_data_obs" )
    inFile_WZ = ROOT.TFile( inName_WZ, 'READ' )
    h_WZ_forObs = inFile_WZ.Get( "x_WZ" )
    outFile = ROOT.TFile( outName, 'UPDATE' )

    #fetch here obs and FR
    h_FR = outFile.Get( "x_data_FR"  )
    int_FR = h_FR.Integral()

    h_data = outFile.Get( "x_data_obs"  )
    int_data = h_data.Integral()
 
    #make changes to data
    print "DATA, ",int_data, int_FR, int_data-int_FR    

    h_data.Add(h_FR, -1.0)
    int_data2 = h_data.Integral()
    print "data-FR ",int_data2

    #fetch shape for shape for data_FR
    #h_SS_forObs = inFile.Get( "x_data_obs" )
    #h_WZ_forObs = inFile_WZ.Get( "x_WZ" )

    #h_SS_forObs.Scale(0.4)
    #h_WZ_forObs.Scale(0.6)

    h_SS_forObs.Scale(0.4*int_FR/h_SS_forObs.Integral())
    h_WZ_forObs.Scale(0.6*int_FR/h_WZ_forObs.Integral())

    print "EKA nama, ", h_SS_forObs.Integral(), h_WZ_forObs.Integral(), h_SS_forObs.Integral()+h_WZ_forObs.Integral()
    h_SS_forObs.Add(h_WZ_forObs)
    print h_SS_forObs.Integral()
    ####h_SS_forObs.Scale(int_FR/h_SS_forObs.Integral())
    int_SS_obs = h_SS_forObs.Integral()
    print "LISAYS, ",int_SS_obs
    print "FR ",int_FR

    h_data.Add(h_SS_forObs)
    int_data3 = h_data.Integral()

    print "new data, ",h_data.Integral()	
    h_data.Write("x_data_obs", outFile.kOverwrite)

    outFile.Purge()

    outFile.Close()
    inFile_WZ.Close()
    inFile.Close()
