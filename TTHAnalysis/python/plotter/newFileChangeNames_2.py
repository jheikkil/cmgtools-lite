
import ROOT

newFile = ROOT.TFile( 'dcSync_Avis_SF_btag_LT.root', 'RECREATE' )

name_mapper = {
    'x_ZZ':'ZZ',
    'x_ttZ':'ttZ',
    'x_ggZZ':'ggZZ',
    'x_azh320':'azh320',
    'x_azh260':'azh260',
    'x_azh350':'azh350',
    'x_triboson':'TriBoson',
    'x_azh300':'azh300',
    'x_azh280':'azh280',
    'x_azh400':'azh400',
    'x_azh340':'azh340',
    'x_WZ':'WZ',
    'x_SM':'ggH_hzz',
}


file_map = {
    'eeet_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/EEET/A_vis//common/SR.input.root',
    'emmt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/MMET/A_vis//common/SR.input.root',
    'eett_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/EETT/A_vis//common/SR.input.root',
    'mmtt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/MMTT/A_vis//common/SR.input.root',
    'eemt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/EEMT/A_vis//common/SR.input.root',
    'mmmt_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/MMMT/A_vis//common/SR.input.root',
    'eeem_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/EEEM/A_vis//common/SR.input.root',
    'emmm_inclusive' : '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/MMEM/A_vis//common/SR.input.root',


}


for channel in file_map.keys() :

    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'
    inName = file_map[ channel ]
    
    inFile = ROOT.TFile( inName, 'READ' )
    
    #print inFile
    #print channel     
    #d1 = inFile.Get( channel )
    newFile.mkdir( channel )
    
    for hName in name_mapper.keys() :
        print hName
        h = inFile.Get( hName )
        print h.Integral()
        hNew = h.Clone()
        hNew.SetName( name_mapper[ hName ] )
        hNew.SetTitle( name_mapper[ hName ] )
    
        newFile.cd( channel )
    
        hNew.Write()

newFile.Close()
