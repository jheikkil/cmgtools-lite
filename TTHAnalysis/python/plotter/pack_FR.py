from math import *
from os.path import basename
import re

import sys
sys.argv.append('-b-')
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv.remove('-b-')
from array import *

def makeH2D(name,xedges,yedges):
    return ROOT.TH2F(name,name,len(xedges)-1,array('f',xedges),len(yedges)-1,array('f',yedges))

def fillSliceY(th2,plot1d,yvalue,xslice):
    ybin = th2.GetYaxis().FindBin(yvalue)
    for xbin in xrange(1,th2.GetNbinsX()+1):
        xval = th2.GetXaxis().GetBinCenter(xbin)
        if xslice[0] <= xval and xval <= xslice[1]:
            for i in xrange(plot1d.GetN()):
                x,xp,xm = plot1d.GetX()[i], plot1d.GetErrorXhigh(i), plot1d.GetErrorYlow(i)
                if x-xm <= xval and xval <= x+xp:
                    th2.SetBinContent(xbin,ybin,plot1d.GetY()[i])
                    th2.SetBinError(xbin,ybin,max(plot1d.GetErrorYlow(i),plot1d.GetErrorYhigh(i)))
def readSliceY(th2,filename,plotname,yvalue,xslice):
    slicefile = ROOT.TFile.Open(filename)
    if not slicefile: raise RuntimeError, "Cannot open "+filename
    plot = slicefile.Get(plotname)
    if not plot: 
        slicefile.ls()
        raise RuntimeError, "Cannot find "+plotname+" in "+filename
    fillSliceY(th2,plot,yvalue,xslice)
    slicefile.Close()
def read2D(th2,filepattern,plotname,yslices,xslice):
    for yvalue,yname in yslices:
        readSliceY(th2,filepattern%yname,plotname,yvalue,xslice)
def readMany2D(processes,th2s,filepattern,plotname,yslices,xslice):
    #print filepattern
    #print plotname
    for (th2,proc) in zip(th2s,processes):
        read2D(th2, filepattern, plotname%proc, yslices, xslice)
def make2D(out,name,xedges,yedges):
    out.cd()
    th2 = makeH2D(name,xedges,yedges)
    return th2

def makeVariants(h):
    shifters = [
        ("up"  ,  lambda pt,eta,fr,err : min(fr+err, 1.0) ),
        ("down",  lambda pt,eta,fr,err : max(fr-err, 0.0) ),
        ("pt1" ,  lambda pt,eta,fr,err : min(max( fr + err * (log(pt/30)/log(3.)), 0.0),1.0) ),
        ("pt2" ,  lambda pt,eta,fr,err : min(max( fr - err * (log(pt/30)/log(3.)), 0.0),1.0) ),
        ("b1"  ,  lambda pt,eta,fr,err : min(max( fr + err if eta < 1.3 else fr, 0.0),1.0) ), 
        ("b2"  ,  lambda pt,eta,fr,err : min(max( fr - err if eta < 1.3 else fr, 0.0),1.0) ),
        ("ec1" ,  lambda pt,eta,fr,err : min(max( fr + err if eta > 1.3 else fr, 0.0),1.0) ), 
        ("ec2" ,  lambda pt,eta,fr,err : min(max( fr - err if eta > 1.3 else fr, 0.0),1.0) ),
    ]
    ret = []
    for s,func in shifters:
        hsyst = h.Clone(h.GetName()+"_"+s)
        for bx in xrange(1,h.GetNbinsX()+1):
            x = h.GetXaxis().GetBinCenter(bx) 
            for by in xrange(1,h.GetNbinsY()+1):
                y = h.GetYaxis().GetBinCenter(by) 
                fr0 = h.GetBinContent(bx,by)
                err = h.GetBinError(bx,by)
                fr = func(x,y,fr0,err)
                print "Variation %-15s: pt %4.1f, eta %3.1f: nominal %.3f +- %.3f --> shifted %.3f "  % (hsyst.GetName(), x, y, fr0, err, fr)
                hsyst.SetBinContent(bx, by, fr)
                hsyst.SetBinError(bx, by, 0)
        ret.append(hsyst)
    return ret
    
def styles(hs,ext=False):
    colors = { 'Data':ROOT.kBlack, 'MC W+jets':ROOT.kRed+1, 'MC DY':ROOT.kAzure+1, 'QCD':ROOT.kAzure+1,
               'nominal':ROOT.kBlack, 'up':ROOT.kGray+1, 'down':ROOT.kGray+1, 
                'pt1':ROOT.kRed+1, 'pt2':ROOT.kBlue+2,
                'b1':ROOT.kViolet+1, 'b2':ROOT.kGreen+2,
                'ec1':ROOT.kViolet+1, 'ec2':ROOT.kGreen+2,}
    if ext: 
        del colors['Data']
        colors['jet + l'] = ROOT.kBlack
        colors['Z + l'] = ROOT.kGray+2
        colors['MC DY'] = ROOT.kViolet+1
    for label,h in hs:
        for n,c in colors.iteritems():
            if n in label:
                print "%s in %s" % (n, label)
                h.SetLineColor(c)
                h.SetMarkerColor(c)
        if ext:
            if "Z + l" in label or "DY" in label:
                h.SetMarkerSize(1.5); h.SetMarkerStyle(ROOT.kFullCircle)
            elif "jet + l" in label or "QCD" in label:
                h.SetMarkerSize(2.0); h.SetMarkerStyle(ROOT.kOpenSquare)
            else:
                h.SetMarkerStyle(ROOT.kDot)
        h.SetLineWidth(3)
        h.GetXaxis().SetTitle("lepton p_{T} (GeV)")
#        h.GetXaxis().SetTitle("lepton p_{T}^{corr} (GeV)")

if __name__ == "__main__":
    from CMGTools.TTHAnalysis.plotter.mcEfficiencies import stackEffs, graphFromXSlice
    import os.path
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] path out")
    parser.add_option("--pdir", dest="outdir", default=None, help="Output directory for plots");
    parser.add_option("--xcut", dest="xcut", default=None, nargs=2, type='float', help="X axis cut");
    parser.add_option("--xrange", dest="xrange", default=None, nargs=2, type='float', help="X axis range");
    parser.add_option("--yrange", dest="yrange", default=(0,0.6), nargs=2, type='float', help="Y axis range");
    parser.add_option("--logy", dest="logy", default=False, action='store_true', help="Do y axis in log scale");
    parser.add_option("--ytitle", dest="ytitle", default="Fake rate", type='string', help="Y axis title");
    parser.add_option("--fontsize", dest="fontsize", default=0.05, type='float', help="Legend font size");
    parser.add_option("--legendWidth", dest="legendWidth", type="float", default=0.35, help="Width of the legend")
    parser.add_option("--grid", dest="showGrid", action="store_true", default=False, help="Show grid lines")
    parser.add_option("--legend",  dest="legend",  default="TL",  type="string", help="Legend position (BR, TR)")
    parser.add_option("--compare", dest="compare", default="", help="Samples to compare (by default, all except the totals)")
    parser.add_option("--showRatio", dest="showRatio", action="store_true", default=True, help="Add a data/sim ratio plot at the bottom")
    parser.add_option("--rr", "--ratioRange", dest="ratioRange", type="float", nargs=2, default=(0,2.4), help="Min and max for the ratio")
    parser.add_option("--normEffUncToLumi", dest="normEffUncToLumi", action="store_true", default=False, help="Normalize the dataset to the given lumi for the uncertainties on the calculated efficiency")
    (options, args) = parser.parse_args()
    (outname) = args[0]
    print outname
    outfile = ROOT.TFile.Open(outname,"RECREATE")
    if options.outdir:
        if not os.path.exists(options.outdir):
            os.system("mkdir -p "+options.outdir)
            if os.path.exists("/afs/cern.ch"): os.system("cp /afs/cern.ch/user/g/gpetrucc/php/index.php "+options.outdir)
        ROOT.gROOT.ProcessLine(".x tdrstyle.cc")
        ROOT.gStyle.SetOptStat(0)
    if True:
       ptbins_el =  [10,20,30,40,50,60]#[ 5.0,7.5,10,15,20,30]
       ptbins_mu =  [10,20,30,40,50,60]#[ 3.5,5.0,7.5,10,15,20,30 ]
       ptbins_tau =  [20,25,30,40,50,70,100]
       etabins_el = [0, 1.479, 2.5]
       etabins_tau = [0, 1.479, 2.3]
       etabins_mu = [0, 1.2, 2.4]
       etaslices_el = [ (0.4,"1p5"), (1.8,"2p5") ]
       etaslices_tau = [ (0.4,"1p5"), (1.8,"2p3") ]
       etaslices_mu = [ (0.4,"1p2"), (1.8,"2p4") ]
 
       DMbins_tau = [0, 1, 10]
       DMslices_tau = [ (0.4,"0"), (1.8,"1"), (10, "10") ]
       el    = [ "eleFR_signal_vs_pt_signal_2d_prefit_graph", "eleFR_signal_vs_pt_signal_2d_prefit_graph" ]
       mu    = [ "muonFR_signal_vs_pt_signal_2d_prefit_graph", "muonFR_signal_vs_pt_signal_2d_prefit_graph" ] 
       #ta    = [ "tauFR_numLL_vs_pt_signal_2d_prefit_graph", "tauFR_numLL_vs_pt_signal_2d_prefit_graph" ]
       ta00 = ["tau-DM0_lltt_AllEta_leptonPt_graph", "tau-DM0_lltt_AllEta_leptonPt_graph"]
       ta01 = ["tau-DM1_lltt_AllEta_leptonPt_graph", "tau-DM1_lltt_AllEta_leptonPt_graph"]
       ta10 = ["tau-DM10_lltt_AllEta_leptonPt_graph", "tau-DM10_lltt_AllEta_leptonPt_graph"]
       ta_jet  = [ "tauFR_numLL_vs_pt_jet_signal_2d_prefit_graph", "tauFR_numLL_vs_pt_jet_signal_2d_prefit_graph" ]
       el_data = ["eleFR_signal_vs_pt_pfmt_fix_data_sub_prefit", "eleFR_signal_vs_pt_pfmt_fix_data_sub_prefit"] 
       mu_data = ["muonFR_signal_vs_pt_pfmt_fix_data_sub_prefit", "muonFR_signal_vs_pt_pfmt_fix_data_sub_prefit"]
       ta_data = ["tauFR_numLL_vs_pt_pfmt_fix_data_fit", "tauFR_numLL_vs_pt_pfmt_fix_data_fit"]
       ta_data_jet = ["tauFR_numLL_vs_pt_jet_pfmt_fix_data_fit", "tauFR_numLL_vs_pt_jet_pfmt_fix_data_fit"]
       #XsD    = [ "DY",  "data_comb" ]
       #Xnices = [ "MC QCD/DY", "Data, comb." ]
   #    h2d_el = [ make2D(outfile, "FR_ele", ptbins_el, etabins_el) ]
   #    h2d_mu = [ make2D(outfile, "FR_muon", ptbins_mu, etabins_mu)]
      ## h2d_tau = [ make2D(outfile, "FR_tau", ptbins_tau, DMbins_tau)]
       #h2d_tau = [ make2D(outfile, "FR_tau", ptbins_tau, etabins_tau)]
       h2d_tau0 = [ make2D(outfile, "FR_tau_DM0", ptbins_tau, DMbins_tau)]
       h2d_tau1 = [ make2D(outfile, "FR_tau_DM1", ptbins_tau, DMbins_tau)]
       h2d_tau10 = [ make2D(outfile, "FR_tau_DM10", ptbins_tau, DMbins_tau)]
    #   h2d_tauJET = [ make2D(outfile, "FR_tau_jet", ptbins_tau, etabins_tau)]
   #    h2d_elD = [ make2D(outfile, "FR_ele_data", ptbins_el, etabins_el) ]
   #    h2d_muD = [ make2D(outfile, "FR_muon_data", ptbins_mu, etabins_mu)]
      # h2d_tauD = [ make2D(outfile, "FR_tau_data", ptbins_tau, etabins_tau)]
    ##   h2d_tauD = [ make2D(outfile, "FR_tau_data", ptbins_tau, DMbins_tau)]
      # h2d_tauD0 = [ make2D(outfile, "FR_tau_data_DM0", ptbins_tau, etabins_tau)]
      # h2d_tauD1 = [ make2D(outfile, "FR_tau_data_DM1", ptbins_tau, etabins_tau)]
      # h2d_tauD10 = [ make2D(outfile, "FR_tau_data_DM10", ptbins_tau, etabins_tau)]


     #  h2d_tauDJET = [ make2D(outfile, "FR_tau_jet_data", ptbins_tau, etabins_tau)]
       #h2d_el_DY = [ make2D(outfile, "FR_SOS_DY_el_"+X, ptbins_el, etabins_el) for X in XsD ]
       #h2d_mu_DY = [ make2D(outfile, "FR_SOS_DY_mu_"+X, ptbins_mu, etabins_mu) for X in XsD ]
       #h2d_el_WJ = [ make2D(outfile,"FR_SOS_el_WJets", ptbins_el, etabins_el) ]
       #h2d_mu_WJ = [ make2D(outfile,"FR_SOS_mu_WJets", ptbins_mu, etabins_mu) ]
       #h2d_el_PB = [ make2D(outfile,"FR_SOS_el_PromptBkg", ptbins_el, etabins_el) ]
       #h2d_mu_PB = [ make2D(outfile,"FR_SOS_mu_PromptBkg", ptbins_mu, etabins_mu) ]

       Plots="/afs/cern.ch/work/j/jheikkil/MSSM2017/CMSSW_8_0_25/src/CMGTools/TTHAnalysis/python/plotter"
       Z3l=None # "z3l/v2.1.1"
       #QCD="qcd1l/v3.0.1"
       QCD="qcd1l/v3.1"

       #### Electrons: 
       ##readMany2D(el, h2d_el,    "/".join([Plots, "FR_ele_%s.root"]), "%s", etaslices_el, (5,999) )
       ##readMany2D(el_data, h2d_elD,    "/".join([Plots, "FR_ele_%s.root"]), "%s", etaslices_el, (5,999) )
       #if Z3l:
       #   readMany2D(XsD, h2d_el_DY, "/".join([Plots, Z3l, "el/fakerates-mtW3R/fr_sub_eta_%s_comp.root"]), "%s", etaslices_el, (5,999) )

       #### Muons: 
       # up to 10 from Mu3
       ##readMany2D(mu, h2d_mu, "/".join([Plots, "FR_muon_%s.root"]), "%s", etaslices_mu, (5,999) )
       readMany2D(ta00, h2d_tau0, "/".join([Plots, "tyler%s.root"]), "%s", DMslices_tau, (5,999) )
       readMany2D(ta01, h2d_tau1, "/".join([Plots, "tyler%s.root"]), "%s", DMslices_tau, (5,999) )
       readMany2D(ta10, h2d_tau10, "/".join([Plots, "tyler%s.root"]), "%s", DMslices_tau, (5,999) )

      # readMany2D(ta, h2d_tau0, "/".join([Plots, "tau_%s_genmatch6_DM0.root"]), "%s", etaslices_tau, (5,999) )
     #  readMany2D(ta, h2d_tau1, "/".join([Plots, "tau_%s_genmatch6_DM1.root"]), "%s", etaslices_tau, (5,999) )
     #  readMany2D(ta, h2d_tau10, "/".join([Plots, "tau_%s_genmatch6_DM10.root"]), "%s", etaslices_tau, (5,999) )
       ##readMany2D(ta_jet, h2d_tauJET, "/".join([Plots, "tau_%s_genmatch6.root"]), "%s", etaslices_tau, (5,999) )
       ##readMany2D([ make2D(outfile, "FR_tau", ptbins_tau, etabins_tau)]mu_data, h2d_muD, "/".join([Plots, "FR_muon_%s.root"]), "%s", etaslices_mu, (5,999) )
      ## readMany2D(ta_data, h2d_tauD, "/".join([Plots, "tau_genmatch6_DM%s.root"]), "%s", DMslices_tau, (5,999) )
       
     #  readMany2D(ta_data, h2d_tauD0, "/".join([Plots, "tau_%s_genmatch6_DM0.root"]), "%s", etaslices_tau, (5,999) )
     #  readMany2D(ta_data, h2d_tauD1, "/".join([Plots, "tau_%s_genmatch6_DM1.root"]), "%s", etaslices_tau, (5,999) )
     #  readMany2D(ta_data, h2d_tauD10, "/".join([Plots, "tau_%s_genmatch6_DM10.root"]), "%s", etaslices_tau, (5,999) )

       ##readMany2D(ta_data_jet, h2d_tauDJET, "/".join([Plots, "tau_%s_genmatch6.root"]), "%s", etaslices_tau, (5,999) )

       # over 10 from Mu8
       #readMany2D(XsQ, h2d_mu, "/".join([Plots, QCD, "mu/HLT_Mu8/fakerates-mtW3R/fr_sub_eta_%s_comp.root"]), "%s", etaslices_mu, (10,999) )
       # DY version
       #if Z3l:
       #   readMany2D(XsD, h2d_mu_DY, "/".join([Plots, Z3l, "mu/fakerates-mtW3R/fr_sub_eta_%s_comp.root"]), "%s", etaslices_mu, (3.5,999) )

       #### TT MC-truth
       #MCPlots="plots/80X/sos/fr-mc/v3.0.1"; ID="wpSOS_ip3d_ptd_3.0_20"; Jet="rec50_bAny"
       #MCPlots="plots/80X/sos/fr-mc/v3.1"; ID="wpSOS_ip3d_pti_300_20"; Jet="rec90_bAny"
       #XVar="IP3D_Full_pt_fine"
       #readMany2D(["WJ_red"], h2d_el_WJ, "/".join([MCPlots, "el_"+ID+"_"+Jet+"_eta_%s.root"]), XVar+"_%s", etaslices_el, (5,999) )
       #readMany2D(["WJ_red"], h2d_mu_WJ, "/".join([MCPlots, "mu_"+ID+"_"+Jet+"_eta_%s.root"]), XVar+"_%s", etaslices_mu, (3.5,999) )

       #### Prompt rate for background
       #readMany2D(["PromptBkg"], h2d_el_PB, "/".join([MCPlots, "el_prB_"+ID+"_"+Jet+"_eta_%s.root"]), XVar+"_%s", etaslices_el, (5,999) )
       #readMany2D(["PromptBkg"], h2d_mu_PB, "/".join([MCPlots, "mu_prB_"+ID+"_"+Jet+"_eta_%s.root"]), XVar+"_%s", etaslices_mu, (3.5,999) )

       # Serialize
       #for h in h2d_mu: outfile.WriteTObject(h)
       for h in h2d_tau0 + h2d_tau1 + h2d_tau10: outfile.WriteTObject(h)
       #for h in h2d_el + h2d_mu + h2d_tau + h2d_elD + h2d_muD + h2d_tauD: outfile.WriteTObject(h) #+ h2d_el_DY + h2d_mu + h2d_mu_DY:    outfile.WriteTObject(h)
       #for h in h2d_el_WJ + h2d_mu_WJ: outfile.WriteTObject(h)
       #for h in h2d_el_PB + h2d_mu_PB: outfile.WriteTObject(h)

       # Plot
       if options.outdir:
           for lep,h2d,h2dtt,nicemc,nicedata,xcuts in (
                    ("el",h2d_el,h2d_el_WJ,"QCD","jet + l",[]),  ("el_DY",h2d_el_DY,h2d_el_WJ,"DY","Z + l",[]),
                    ("mu",h2d_mu,h2d_mu_WJ,"QCD","jet + l",[10]),("mu_DY",h2d_mu_DY,h2d_mu_WJ,"DY","Z + l",[])):
              if ("DY" in lep) and not Z3l: continue
              Xnices[0] = "MC "+nicemc
              Xnices[1] = "Data, "+nicedata
              for ieta,eta in enumerate(["barrel","endcap"]):
                  effs = [ (n,graphFromXSlice(h,ieta+1)) for (n,h) in zip(Xnices,h2d) ]
                  effs.insert(1, ("MC W+jets",graphFromXSlice(h2dtt[0],ieta+1)) )
                  styles(effs)
                  options.xlines = xcuts
                  stackEffs(options.outdir+"/fr_%s_%s.root"%(lep,eta), None,effs,options)
              variants = makeVariants(h2d[1])
              for v in variants: outfile.WriteTObject(v, v.GetName())
              for ieta,eta in enumerate(["barrel","endcap"]):
                  effs = [ ('nominal', graphFromXSlice(h2d[1],ieta+1)) ]
                  for v in variants: 
                    label = v.GetName().rsplit("_",1)[1]
                    if label in ('b1' ,'b2' ) and eta == "endcap": continue
                    if label in ('ec1','ec2') and eta == "barrel": continue
                    effs.append( (label, graphFromXSlice(v,ieta+1) ) )
                  styles(effs)
                  options.xlines = xcuts
                  stackEffs(options.outdir+"/variants_fr_%s_%s.root"%(lep,eta), None,effs,options)
           for lep,h2d,h2ddy,h2dtt,xcuts in (
                    ("el_all",h2d_el,h2d_el_DY,h2d_el_WJ,[]),
                    ("mu_all",h2d_mu,h2d_mu_DY,h2d_mu_WJ,[10])):
              if not Z3l: continue
              Xnices = [ "MC W+jets", "MC QCD", "MC DY", "Data, jet + l", "Data, Z + l" ]
              h2ds   = [ h2dtt[0], h2d[0], h2ddy[0], h2d[1], h2ddy[1] ]
              for ieta,eta in enumerate(["barrel","endcap"]):
                  effs = [ (n,graphFromXSlice(h,ieta+1)) for (n,h) in zip(Xnices,h2ds) ]
                  styles(effs, ext=True)
                  options.xlines = xcuts
                  stackEffs(options.outdir+"/fr_%s_%s.root"%(lep,eta), None,effs,options)

    outfile.ls()
