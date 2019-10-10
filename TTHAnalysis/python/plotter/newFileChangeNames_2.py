
import ROOT

newFile = ROOT.TFile( 'check_3010.root', 'RECREATE' )

name_mapper = {
    'x_ZZ':'ZZ',
    'x_data_FR':'allFakes',
    'x_ttZ':'ttZ',
    'x_ttH' : 'ttH', 
    'x_ttW' : 'ttW',
    'x_WH' : 'WH_htt125',
    'x_ZH' : 'ZH_htt125',
    'x_GG':'ggZZ',
    'x_AZH220':'azh220',
    'x_AZH240':'azh240',
    'x_AZH320':'azh320',
    'x_AZH260':'azh260',
    'x_AZH350':'azh350',
    'x_triboson':'TriBoson',
    'x_AZH300':'azh300',
    'x_AZH280':'azh280',
    'x_AZH400':'azh400',
    'x_AZH340':'azh340',
    'x_WZ':'WZ',
    'x_SM':'ggH_hzz125',
    'x_data_obs':'data_obs',
}


file_map = {
    'eeet_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm_inclusive' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_2210/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


for channel in file_map.keys() :

    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'
    inName = file_map[ channel ]
    
    inFile = ROOT.TFile( inName, 'READ' )
    
    #print inFile
    #print channel     
    #d1 = inFile.Get( channel )
    newFile.mkdir( channel )

    print channel
    
    for hName in name_mapper.keys() :
        #print hName
        if inFile.Get(hName):
            h = inFile.Get( hName )
        #print h.Integral()
            hNew = h.Clone()
            hNew.SetName( name_mapper[ hName ] )
            hNew.SetTitle( name_mapper[ hName ] )
        #print hNew.Integral()
            newFile.cd( channel )
    
            hNew.Write()
    #hFR = inFile.Get("x_data_FR")
    #hWZ = inFile.Get("x_WZ")
    #print "Integrals"
    #print hWZ.Integral()
    #print hFR.Integral()
    #print hWZ.Integral()+hFR.Integral()
    #print hWZ.Integral()/(hWZ.Integral()+hFR.Integral())


    #hFR.Add(hWZ) 

    #h_allFakes = hFR.Clone()
    #h_allFakes.SetName( "allFakes" )
    #h_allFakes.SetTitle( "allFakes" )
    #newFile.cd(channel)
    #h_allFakes.Write()



newFile.Close()
