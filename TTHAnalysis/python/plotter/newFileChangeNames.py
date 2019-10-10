
import ROOT

inName = '/afs/cern.ch/work/j/jheikkil/testing2018/CMSSW_8_0_26_patch1/src/HiggsAnalysis/CombinedLimit/AZH_May03/EEET/A_vis//common/SR.input.root'

inFile = ROOT.TFile( inName, 'READ' )

name_mapper = {
    'ZZ' : 'x_ZZ',
    'ttZ' : 'x_ttZ',
}

newFile = ROOT.TFile( 'jaanas_new_file.root', 'RECREATE' )

d1 = inFile.Get('eeet_inclusive')
newFile.mkdir( 'jaana_new_dir_eeet' )

for hName in name_mapper.keys() :
    print hName
    h = d1.Get( hName )
    print h.Integral()
    hNew = h.Clone()
    hNew.SetName( name_mapper[ hName ] )
    hNew.SetTitle( name_mapper[ hName ] )

    newFile.cd( 'jaana_new_dir_eeet' )

    hNew.Write()

newFile.Close()
