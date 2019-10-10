
import ROOT

newFile = ROOT.TFile( 'hadded_0211.root', 'RECREATE' )

name_mapper = {
    'x_AZH220':'azh220',
    'x_AZH240':'azh240',
    'x_AZH320':'azh320',
    'x_AZH260':'azh260',
    'x_AZH350':'azh350',
    'x_AZH300':'azh300',
    'x_AZH280':'azh280',
    'x_AZH400':'azh400',
    'x_AZH340':'azh340',
}


file_map = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_0211/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


channels = ["tt", "mt", "et", "em"]


for channel in channels :

    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'
    if channel == "tt":
        inName = file_map["eett"]
        inName2 = file_map["mmtt"]
    elif channel == "mt":
        inName = file_map["eemt"]
        inName2	= file_map["mmmt"]
    elif channel == "et":
        inName = file_map["eeet"]
        inName2	= file_map["emmt"]
    elif channel == "em":
        inName = file_map["eeem"]
        inName2	= file_map["emmm"]

    inFile = ROOT.TFile( inName, 'READ' )
    inFile2 = ROOT.TFile( inName2, 'READ' ) 
    #print inFile
    #print channel     
    newFile.mkdir( channel )
    #d1 = inFile.Get( channel )

    print channel
    for hName in name_mapper.keys() :
        h = inFile.Get( hName )
        h2 = inFile2.Get( hName )
        h.Add(h2)     
        print h.Integral()
        newFile.cd(channel)
        h.Write()

newFile.Purge()

newFile.Close()
