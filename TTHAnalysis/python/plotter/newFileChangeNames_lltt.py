
import ROOT

newFile = ROOT.TFile( 'dcSync_AsvConstr_SF_btag_July26_LT80.root', 'RECREATE' )

name_mapper = {
    'x_ZZ':'ZZ',
    'x_data_FR':'data_FR',
    'x_ttZ':'ttZ',
    'x_ttH' : 'ttH', 
    'x_ttW' : 'ttW',
    'x_WH' : 'WH_htt125',
    'x_ZH' : 'ZH_htt125',
    'x_GG':'ggZZ',
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
}


file_map = {
    'eett_inclusive' : 'lltt_LT80.root',
    'mmtt_inclusive' : 'lltt_LT80.root',
    'mmmt_inclusive' : 'llmt.root',
    'mmet_inclusive' : 'llet.root',
    'mmem_inclusive' : 'llem.root',
    'eemt_inclusive' : 'llmt.root',
    'eeet_inclusive' : 'llet.root',
    'eeem_inclusive' : 'llem.root',

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
        #print hName
        h = inFile.Get( hName )
        #print h.Integral()
        hNew = h.Clone()
        hNew.SetName( name_mapper[ hName ] )
        hNew.SetTitle( name_mapper[ hName ] )
        #print hNew.Integral()
        newFile.cd( channel )
    
        hNew.Write()
    hFR = inFile.Get("x_data_FR")
    hWZ = inFile.Get("x_WZ")
    hFR.Add(hWZ) 
    h_allFakes = hFR.Clone()
    h_allFakes.SetName( "allFakes" )
    h_allFakes.SetTitle( "allFakes" )
    newFile.cd(channel)
    h_allFakes.Write()

newFile.Close()
