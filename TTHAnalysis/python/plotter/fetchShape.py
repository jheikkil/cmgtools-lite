
import ROOT

newFile_map = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0810/MMEM/Aconstr_HsvFit90/common/SR.input.root',


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


for channel in file_map_SS.keys() :


    print channel
    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'
    inName = file_map_SS[ channel ]
    inName_WZ = file_map_OS[ channel ]
    outName = newFile_map[ channel ]    

    inFile = ROOT.TFile( inName, 'READ' )
    inFile_WZ = ROOT.TFile( inName_WZ, 'READ' )
    outFile = ROOT.TFile( outName, 'UPDATE' )
    
    #for hName in name_mapper.keys() :
        #print hName
    h_SS = inFile.Get( "x_data_obs" )

    print "h_SS"
    print h_SS.Integral()
    h_SS.Scale(0.4)
    print h_SS.Integral()
    
    #int_SS = h_SS.Integral()
    
    print "h_WZ"
    h_WZ = inFile_WZ.Get( "x_WZ" )
    print h_WZ.Integral()
    h_WZ.Scale(0.6)
    print h_WZ.Integral()
    
    h_SS.Add(h_WZ)
    h_SS.Integral()    

    int_SS=h_SS.Integral()
    print int_SS
    #int_WZ = h_WZ.Integral()

    h_FR = outFile.Get( "x_data_FR"  )
    int_FR = h_FR.Integral()


    h_SS.Scale(int_FR/int_SS)

    print "Integrals FR and SS after ",int_FR,h_SS.Integral()
    outFile.cd()
    h_SS.Write("x_data_FR", outFile.kOverwrite)

    outFile.Close()
    inFile.Close()
