
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


for channel in file_map_SS.keys() :


    print channel
    inName = file_map_SS[ channel ]
    outName = newFile_map[ channel ]    

    #outFile = ROOT.TFile( outName, 'UPDATE' )
    inFile = ROOT.TFile( inName, 'READ' )
    outFile = ROOT.TFile( outName, 'UPDATE' )

    #fetch here obs and FR
    h_FR = outFile.Get( "x_data_FR"  )
    int_FR = h_FR.Integral()

    #fetch shape for shape for data_FR
    h_SS_forShape = inFile.Get( "x_data_obs" )

    h_SS_forShape.Write("h_SS_forShape", outFile.kOverwrite)

    #change the shape
    int_SS_shape = h_SS_forShape.Integral()
    h_SS_forShape.Scale(int_FR/int_SS_shape)
    h_SS_forShape.SetName("x_data_FR") 
    h_SS_forShape.Write("x_data_FR", outFile.kOverwrite)
    
    outFile.Close()
    inFile.Close()
