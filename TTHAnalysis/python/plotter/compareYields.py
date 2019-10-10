
import ROOT
ROOT.gROOT.SetBatch(True)


File1 = ROOT.TFile( 'hadded_0211.root', 'READ' )
File2 = ROOT.TFile( 'hadded_0211_mass.root', 'READ' )



channels = ["tt", "mt", "et", "em"]
names = ['x_AZH220',
    'x_AZH240',
    'x_AZH260',
    'x_AZH280',
    'x_AZH300',
    'x_AZH320',
    'x_AZH340',
    'x_AZH350',
    'x_AZH400',
]


c = ROOT.TCanvas('c','c',600,600)
p = ROOT.TPad('p','p',0,0,1,1,)
p.Draw()
p.cd()
p.SetLeftMargin( 0.15 )

for hName in names:
    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'

    #inFile = ROOT.TFile( inName, 'READ' )
    #inFile2 = ROOT.TFile( inName2, 'READ' ) 
    #print inFile
    #print channel     
    #File1.( channel )
    #d1 = inFile.Get( channel )

    for channel in channels :
        print hName, channel
        h = File1.Get( channel+"/"+hName )
        h2 = File2.Get( channel+"/"+hName )
        print("%.3f/%.3f=%.3f " %(h2.Integral(), h.Integral(), h2.Integral()/h.Integral()))
        #h2.SetLineColor(ROOT.kRed)
        #h2.SetMarkerColor(ROOT.kRed)
        #h.SetMaximum(1.2*h.GetMaximum())
        #h.Draw()
        #h2.Draw("SAME")
        #c.SaveAs('/eos/user/j/jheikkil/www/gen_mass_eff/azh%s_%s.png' % (hName, channel) )
        
