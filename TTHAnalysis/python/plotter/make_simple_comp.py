import ROOT


f = ROOT.TFile('/afs/cern.ch/work/t/truggles/public/forJaana/shape_syst_example/example_combine_input_file_from_ZH.root','r')

d = f.Get('mmtt_LT2D')

h1 = d.Get('ZZ_CMS_scale_t_1prong_13TeVUp')
h2 = d.Get('ZZ')
h3 = d.Get('ZZ_CMS_scale_t_1prong_13TeVDown')

print "Up Int:", h1.Integral()
print "Nom Int:", h2.Integral()
print "Down Int:", h3.Integral()

c = ROOT.TCanvas('c','c',500,500)

h1.SetLineColor(ROOT.kRed)
h1.Draw()
h2.SetLineColor(ROOT.kBlack)
h2.Draw('SAME')
h3.SetLineColor(ROOT.kBlue)
h3.Draw('SAME')

ROOT.gPad.BuildLegend()
ROOT.gPad.SetLogy()

c.SaveAs('tmp.png')
