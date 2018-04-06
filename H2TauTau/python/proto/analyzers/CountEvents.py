import math
import os
import ROOT

from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import bestMatch

from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject
from PhysicsTools.Heppy.physicsobjects.GenParticle import GenParticle

from CMGTools.H2TauTau.proto.analyzers.TauGenTreeProducer import TauGenTreeProducer

if "/sDYReweighting_cc.so" not in ROOT.gSystem.GetLibraries(): 
    ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/H2TauTau/python/proto/plotter/DYReweighting.cc+" % os.environ['CMSSW_BASE']);
    from ROOT import getDYWeight


class CountEvents(Analyzer):

    '''Add generator information to hard leptons.
    '''
    def declareHandles(self):
        super(CountEvents, self).declareHandles()

        self.mchandles['genInfo'] = AutoHandle(('generator','',''), 'GenEventInfoProduct' )
        self.mchandles['genJets'] = AutoHandle('slimmedGenJets', 'std::vector<reco::GenJet>')
        self.mchandles['genParticles'] = AutoHandle('prunedGenParticles', 'std::vector<reco::GenParticle')

        self.handles['jets'] = AutoHandle(self.cfg_ana.jetCol, 'std::vector<pat::Jet>')

    def beginLoop(self, setup):
        super(CountEvents,self).beginLoop(setup)
        self.counters.addCounter('Zbosonit')
        self.count = self.counters.counter('Zbosonit')

        self.count.register('all A bosons')
        self.count.register('A boson mass in [220, 350]')
       	#self.count.register('All three passed: Z_mm')
        #self.count.register('All three passed: Z_ee')
        self.count.register('A from passed Z and H')
        self.count.register('A from passed Z_mm and H')
        self.count.register('All three passed: Z_mm')
        self.count.register('A from passed Z_ee and H')
        self.count.register('All three passed: Z_ee')

        self.count.register('Z_mm and H_mt')
        self.count.register('Z_mm and H_et')
        self.count.register('Z_mm and H_tt')
        self.count.register('Z_mm and H_em')
        self.count.register('Z_mm others')
        self.count.register('Z_ee and H_mt')
        self.count.register('Z_ee and H_et')
        self.count.register('Z_ee and H_tt')
        self.count.register('Z_ee and H_em')
        self.count.register('Z_ee others')
        self.count.register('Z others')
        self.count.register('H_mt')
        self.count.register('H_et')
        self.count.register('H_tt')
        self.count.register('H_em')
        self.count.register('H others')


        #self.count.register('As self daughter')
        #self.count.register('0: Z and 1: H')
        #self.count.register('0: H and 1: Z')

        self.count.register('all Z bosons')
        self.count.register('es from Z bosons')
        self.count.register('mus from Z bosons')
        self.count.register('taus from Z bosons')
        self.count.register('el pair from Z')       
        self.count.register('mu pair from Z')
        self.count.register('ta pair from Z') 

        self.count.register('Zel pair passing 20:2.5')
        self.count.register('Zmu pair passing 20:2.4')
        self.count.register('Zta pair passing 20:2.3')

        self.count.register('all H bosons')
        self.count.register('taus from H bosons')
        self.count.register('tau number 1')
        self.count.register('final tau number 1')
        self.count.register('tau number 2')
        self.count.register('final tau number 2')
        self.count.register('tau changed')
        self.count.register('tau did not change')

        #self.count.register('hadronic taus from H bosons')
        #self.count.register('2nd hadronic taus from H bosons')
        self.count.register('electron from taus from H bosons')
        self.count.register('muon from taus from H bosons')
        self.count.register('electrons and muons')

        #self.count.register('em')

       # self.count.register('mt: passed 10:2.4')
       # self.count.register('mm: passed 10:2.4')
       # self.count.register('ee: passed 10:2.5')
        #self.count.register('et: passed 10:2.5') 
       # self.count.register('em: passed 10:2.5 and 10:2.4')

        self.count.register('et')
        self.count.register('et: passed 10:2.5 and 20:2.3')
       # self.count.register('et: passed pt,eta,IDISO')

        self.count.register('mt')
        self.count.register('mt: passed 10:2.4 and 20:2.3')
        #self.count.register('.-.-.-.-.-.-.-.-.--.')

        self.count.register('em')
        self.count.register('em: passed 10:2.5 and 10:2.4')
        #self.count.register('--------------------') 

        self.count.register('mm')
        self.count.register('mm: passed 10:2.4')
        #self.count.register('---------------------')

        self.count.register('ee')
        self.count.register('ee: passed 10:2.5')
        #self.count.register('---------------------')

        self.count.register('tt')
        self.count.register('tt: passed 20:2.3')
        #self.count.register('tt: passed pt,eta,IDISO')
        #self.count.register('muon from 2nd taus from H bosons')
        #self.count.register('secondary leptonic decays')

        self.count.register('testi way tt:')
        self.count.register('2nd way tt:')
        self.count.register('2nd way tt: passed')
        #self.count.register('hadronic decays')
        #self.count.register('2nd hadronic decays')


    def process(self, event, FillCounter=True):
        event.genmet_pt = -99.
        event.genmet_eta = -99.
        event.genmet_e = -99.
        event.genmet_px = -99.
        event.genmet_py = -99.
        event.genmet_phi = -99.
        event.weight_gen = 1.

        if self.cfg_comp.isData:
            return True

        self.readCollections(event.input)


        event.genJets = self.mchandles['genJets'].product()
        event.jets = self.handles['jets'].product()
        event.genParticles = self.mchandles['genParticles'].product()

        event.Abosons = [p for p in event.genParticles if abs(p.pdgId()) in [36] and p.isLastCopy()]
        event.Zbosons = [p for p in event.genParticles if abs(p.pdgId()) in [23] and 60<=p.mass()<=120]
        event.Hbosons = [p for p in event.genParticles if abs(p.pdgId()) in [25]]

       
        self.counters.addCounter('pituudet')
        self.count2 = self.counters.counter('pituudet')

        self.count2.register('all A bosons')
        self.count2.register('all Z bosons')
        self.count2.register('all H bosons')

        for i in xrange(len(event.Abosons)):
            self.count2.inc('all A bosons')
        for j in xrange(len(event.Zbosons)):
            self.count2.inc('all Z bosons')
        for k in xrange(len(event.Hbosons)):
            self.count2.inc('all H bosons')

 
        for Abosoni in event.Abosons:
             Abosoni_passed = 0
             self.count.inc('all A bosons')
             if 220<=Abosoni.mass()<=350:
                 Abosoni_passed = 1
                 self.count.inc('A boson mass in [220, 350]')
       #     Z_mm_passed = 0
       #     Z_ee_passed = 0
            #add booleans for h
       #     for i_d in xrange(Abosoni.numberOfDaughters()):
       #         if Abosoni.daughter(i_d).pdgId() == 23:
       #             self.count.inc('all Z bosons')
       #             Zboson = Abosoni.daughter(i_d)
       #             if abs( Zboson.daughter(0).pdgId() )==11 and abs( Zboson.daughter(1).pdgId() )==11:
       #                 self.count.inc('el pair from Z')
       #                 if Zboson.daughter(0).pt()>20 and abs( Zboson.daughter(0).eta() ) < 2.5 and Zboson.daughter(1).pt()>20 and abs( Zboson.daughter(1).eta() ) < 2.5:
       #                     self.count.inc('Zel pair passing 20:2.5')
       #                     Z_ee_passed = 1
       #             if abs( Zboson.daughter(0).pdgId() )==13 and abs( Zboson.daughter(1).pdgId() )==13:
       #                 self.count.inc('mu pair from Z')
       #                 if Zboson.daughter(0).pt()>20 and abs( Zboson.daughter(0).eta() ) < 2.4 and Zboson.daughter(1).pt()>20 and abs( Zboson.daughter(1).eta() ) < 2.4:
       #                     self.count.inc('Zmu pair passing 20:2.4')
       #                     Z_mm_passed = 1
       #         elif Abosoni.daughter(i_d).pdgId() == 25: 
       #             Hboson = Abosoni.daughter(i_d)
       #             self.count.inc('all H bosons')
                    # mt, et, tt, em
                    # cuts
            #check if both ok
            #add new counter
                  
            
          


               #if Abosoni.daughter(i_d).pdgId() == Abosoni.pdgId():
                #    self.count.inc('As self daughter')
                #    return CountEvents.getFinalTau(tau.daughter(i_d))
                #return tau  
            #if Abosoni.daughter(0).pdgId()==23 and Abosoni.daughter(1).pdgId()==25:
            #    print '0: Z, 1: H'
            #    self.count.inc('0: Z and 1: H')
            #elif Abosoni.daughter(0).pdgId()==25 and Abosoni.daughter(1).pdgId()==23:
            #    self.count.inc('0: H and 1: Z')
 
        Z_mm_passed = 0
        Z_ee_passed = 0
        Z_tt_passed = 0

        for Zbosoni in event.Zbosons:
      #      print 'nyt gene Z'
      #      print 'tyttaria monta:'
            self.count.inc('all Z bosons')
       #     Z_mm_passed = 0
       #     Z_ee_passed = 0
       #     Z_tt_passed = 0
      #      print Zbosoni.numberOfDaughters()
            if abs( Zbosoni.daughter(0).pdgId() )==11 and abs( Zbosoni.daughter(1).pdgId() )==11:
                self.count.inc('el pair from Z')
                if (Zbosoni.daughter(0).pt()>20 or Zbosoni.daughter(1).pt()>20) and abs( Zbosoni.daughter(0).eta() ) < 2.5 and abs( Zbosoni.daughter(1).eta() ) < 2.5: #and Zbosoni.daughter(1).pt()>20
                    self.count.inc('Zel pair passing 20:2.5')
                    Z_ee_passed = 1
            if abs( Zbosoni.daughter(0).pdgId() )==13 and abs( Zbosoni.daughter(1).pdgId() )==13:
       	       	self.count.inc('mu pair from Z')
                if (Zbosoni.daughter(0).pt()>20 or Zbosoni.daughter(1).pt()>20) and abs( Zbosoni.daughter(0).eta() ) < 2.4  and abs( Zbosoni.daughter(1).eta() ) < 2.4: #and Zbosoni.daughter(1).pt()>20
                    self.count.inc('Zmu pair passing 20:2.4')
                    Z_mm_passed = 1
            if abs( Zbosoni.daughter(0).pdgId() )==15 and abs( Zbosoni.daughter(1).pdgId() )==15:
       	       	self.count.inc('ta pair from Z')
                if Zbosoni.daughter(0).pt()>20 and abs( Zbosoni.daughter(0).eta() ) < 2.3 and Zbosoni.daughter(1).pt()>20 and abs( Zbosoni.daughter(1).eta() ) < 2.3:
                    self.count.inc('Zta pair passing 20:2.3')
                    Z_tt_passed = 1
            for i_d in xrange(Zbosoni.numberOfDaughters()):
                if abs( Zbosoni.daughter(i_d).pdgId() ) in [11]:
                    print 'nyt oli elektroni'          
                    self.count.inc('es from Z bosons')
                if abs( Zbosoni.daughter(i_d).pdgId() ) in [13]:
                    print 'nyt oli muons'
       	       	    self.count.inc('mus from Z bosons')
                if abs( Zbosoni.daughter(i_d).pdgId() ) in [15]:
                    print 'nyt oli taus'
       	       	    self.count.inc('taus from Z bosons')   
        
        H_mt = 0
        H_et = 0
        H_tt = 0
        H_em = 0


         # use these 
        for Hbosoni in event.Hbosons:
            self.count.inc('all H bosons')        
            print Hbosoni.numberOfDaughters()
            H_mt = 0
            H_et = 0
            H_tt = 0
            H_em = 0
            leptonic_m_1 = 0
       	    leptonic_m_2 = 0
            leptonic_e_1 = 0
            leptonic_e_2 = 0
            tau_e1_passed = 0
            tau_e2_passed = 0
            #tau_e1_passIDISO = 0
            #tau_e2_passIDISO = 0
            tau_m1_passed = 0
            #tau_m1_passIDISO = 0
            tau_m2_passed = 0
            #tau_m1_passIDISO = 0
            tau1_had = 0
            tau2_had = 0
            tau1_had_passed = 0
            tau2_had_passed = 0
            tau1_had_passIDISO = 0
            tau2_had_passIDISO = 0
            tau1_testi = 0
            tau2_testi = 0
            for i_d in xrange(Hbosoni.numberOfDaughters()):
                #make sure to count taus
                if abs( Hbosoni.daughter(i_d).pdgId() ) in [15]:
                    print 'nyt Higgsista tau number'
                    print i_d
                    self.count.inc('taus from H bosons') #this works 
                original_tau = Hbosoni.daughter(i_d)
                tau = Hbosoni.daughter(i_d)
                final_tau = self.getFinalTau(Hbosoni.daughter(i_d))
                if i_d == 0:
                    self.count.inc('tau number 1')
                    if final_tau != original_tau:
                        self.count.inc('final tau number 1')
                        tau = final_tau                           
                if i_d == 1:
                    self.count.inc('tau number 2')
                    if final_tau != original_tau:
                        self.count.inc('final tau number 2')
                        tau = final_tau
                if tau == original_tau:
                    self.count.inc('tau did not change')
                else:
                    self.count.inc('tau changed')
                #if tau.pt>
                for j_d in xrange( tau.numberOfDaughters() ):
                    if abs( tau.daughter(j_d).pdgId() )==11 and tau.daughter(j_d).statusFlags().isDirectPromptTauDecayProduct():
                        self.count.inc('electron from taus from H bosons')
                        self.count.inc('electrons and muons')
                        if i_d == 0:
                            leptonic_e_1 = 1
                            if tau.daughter(j_d).pt()>10 and abs( tau.daughter(j_d).eta() ) < 2.5:
                                tau_e1_passed = 1
                                #if 
                        if i_d == 1: 
                            leptonic_e_2 = 1
                            if tau.daughter(j_d).pt()>10 and abs( tau.daughter(j_d).eta() ) < 2.5:
       	       	                tau_e2_passed = 1
                                #ID ISO CUT
                    if abs( tau.daughter(j_d).pdgId() )==13 and tau.daughter(j_d).statusFlags().isDirectPromptTauDecayProduct():
                        self.count.inc('muon from taus from H bosons')
                        self.count.inc('electrons and muons')
                        if i_d == 0:
                            leptonic_m_1 = 1
                            if tau.daughter(j_d).pt()>10 and abs( tau.daughter(j_d).eta() ) < 2.4:
       	       	                tau_m1_passed = 1
                                #ID ISO CUT
                                #if tau.daughter(j_d).muonID('POG_ID_Medium_ICHEP') and tau.daughter(j_d).relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15:
                                #    tau_m1_passIDISO = 1
                        if i_d == 1:
                            leptonic_m_2 = 1
                            if tau.daughter(j_d).pt()>10 and abs( tau.daughter(j_d).eta() ) < 2.4:
       	          	        tau_m2_passed = 1
                                #ID ISO CUT
                                #if tau.daughter(j_d).muonID('POG_ID_Medium_ICHEP') and tau.daughter(j_d).relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) < 0.15:
       	       	       	       	#    tau_m2_passIDISO = 1
                    if ( tau.numberOfDaughters() -j_d )==1 and abs( tau.daughter(j_d).pdgId() )!=13 and abs( tau.daughter(j_d).pdgId() )!=11:
                        if leptonic_e_1 == 0 and leptonic_m_1 == 0 and i_d==0:
                            tau1_had = 1
                            if tau.pt()>21 and abs( tau.eta() ) < 2.3:
                                tau1_had_passed = 1
                                #ID ISO CUT
                        if leptonic_e_2 == 0 and leptonic_m_2 == 0 and i_d==1:
                            tau2_had = 1  
                            if tau.pt()>21 and abs( tau.eta() ) < 2.3:
       	       	   	        tau2_had_passed	= 1
                                #ID ISO CUT   
                        #    self.count.inc('hadronic decays')
            if leptonic_e_1 == 0 and leptonic_m_1 == 0:
                tau1_testi = 1
            if leptonic_e_2 == 0 and leptonic_m_2 == 0:
                tau2_testi = 1    
            if leptonic_e_1==1 and leptonic_e_2==1:
                print "ee"
                self.count.inc('ee')
                if tau_e1_passed == 1 and tau_e2_passed == 1:
                    self.count.inc('ee: passed 10:2.5')
            elif (leptonic_e_1==1 and tau2_had==1) or (tau1_had==1 and leptonic_e_2==1):
      	        print "et"
                self.count.inc('et')
                if (leptonic_e_1==1 and tau2_had==1 and tau2_had_passed == 1 and tau_e1_passed == 1) or (leptonic_e_2==1 and tau1_had==1 and tau1_had_passed == 1 and tau_e2_passed == 1):
       	   	    self.count.inc('et: passed 10:2.5 and 20:2.3')
                    H_et = 1
            elif leptonic_m_1==1 and leptonic_m_2==1:
       	   	print "mm"
                self.count.inc('mm')
                if tau_m1_passed == 1 and tau_m2_passed == 1:
       	       	    self.count.inc('mm: passed 10:2.4')
                    #if tau_m1_passIDISO == 1 and tau_m2_passIDISO == 1:
                    #    self.count.inc('mm: passed pt,eta,IDISO')
            elif (leptonic_m_1==1 and tau2_had==1) or (tau1_had==1 and leptonic_m_2==1):
                print "mt"
                self.count.inc('mt')
                if (leptonic_m_1==1 and tau_m1_passed == 1 and tau2_had==1 and tau2_had_passed == 1) or (leptonic_m_2==1 and tau_m2_passed == 1 and tau1_had==1 and tau1_had_passed == 1):
                    self.count.inc('mt: passed 10:2.4 and 20:2.3')
                    H_mt = 1
            elif (leptonic_m_1==1 and leptonic_e_2 == 1) or (leptonic_e_1==1 and leptonic_m_2==1):
       	       	print "em"   
                self.count.inc('em')
                if (leptonic_m_1==1 and tau_m1_passed == 1 and leptonic_e_2==1 and tau_e2_passed == 1) or (leptonic_m_2==1 and tau_m2_passed == 1 and leptonic_e_1==1 and tau_e1_passed == 1):
       	       	    self.count.inc('em: passed 10:2.5 and 10:2.4')
                    H_em = 1
            else:
                print "tt"
                self.count.inc('tt')
                #if event.Hbosons and Hbosoni.numberOfDaughters() == 2:
                if self.getFinalTau(Hbosoni.daughter(0)).pt()>21 and abs( self.getFinalTau(Hbosoni.daughter(0)).eta() ) < 2.3 and self.getFinalTau(Hbosoni.daughter(1)).pt()>21 and abs( self.getFinalTau(Hbosoni.daughter(1)).eta() ) < 2.3: 
                    self.count.inc('tt: passed 20:2.3')              
                    H_tt = 1   
            if tau1_had==1 and tau2_had==1:
                print "tt 2"
                self.count.inc('2nd way tt:')
                if tau1_had_passed == 1 and tau2_had_passed == 1:
                    self.count.inc('2nd way tt: passed')   
            if tau1_testi == 1 and tau2_testi == 1:
                self.count.inc('testi way tt:')           
        #save hadronic taus


        if H_mt == 1:
            self.count.inc('H_mt')
        elif H_et == 1:
            self.count.inc('H_et')
        elif H_tt == 1:
            self.count.inc('H_tt')
        elif H_em == 1:
            self.count.inc('H_em')
        else:
            self.count.inc('H others')

        if Z_mm_passed == 1:
            if H_mt == 1:
                self.count.inc('Z_mm and H_mt')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_mm and H')
                if 220<=Abosoni.mass()<=350:
                    self.count.inc('All three passed: Z_mm')
            elif H_et == 1:
                self.count.inc('Z_mm and H_et')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_mm and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_mm')
            elif H_tt == 1:
                self.count.inc('Z_mm and H_tt')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_mm and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_mm')
            elif H_em == 1:
                self.count.inc('Z_mm and H_em')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_mm and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_mm')
            else:
                self.count.inc('Z_mm others')
        elif Z_ee_passed == 1: 
            if H_mt == 1:
                self.count.inc('Z_ee and H_mt')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_ee and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_ee')
            elif H_et == 1:
                self.count.inc('Z_ee and H_et')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_ee and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_ee')
            elif H_tt == 1:
                self.count.inc('Z_ee and H_tt')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_ee and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_ee')
            elif H_em == 1:
                self.count.inc('Z_ee and H_em')
                self.count.inc('A from passed Z and H')
                self.count.inc('A from passed Z_ee and H')
                if 220<=Abosoni.mass()<=350:
       	       	    self.count.inc('All three passed: Z_ee')
            else:
                self.count.inc('Z_ee others')
        else:
            self.count.inc('Z others')

        event.genleps = [p for p in event.genParticles if abs(p.pdgId()) in [11, 13] and p.statusFlags().isPrompt()]
        event.gentauleps = [p for p in event.genParticles if abs(p.pdgId()) in [11, 13] and p.statusFlags().isDirectPromptTauDecayProduct()]
        event.gentaus = [p for p in event.genParticles if abs(p.pdgId()) == 15 and p.statusFlags().isPrompt() and not any(abs(self.getFinalTau(p).daughter(i_d).pdgId()) in [11, 13] for i_d in xrange(self.getFinalTau(p).numberOfDaughters()))]
        self.getGenTauJets(event)

        


        event.weight_gen = self.mchandles['genInfo'].product().weight()
        event.eventWeight *= event.weight_gen

        # gen MET as sum of the neutrino 4-momenta
        neutrinos = [
            p for p in event.genParticles if abs(p.pdgId()) in (12, 14, 16) and p.status() == 1]

        genmet = ROOT.math.XYZTLorentzVectorD()
        for nu in neutrinos:
            genmet += nu.p4()

        event.genmet_pt = genmet.pt()
        event.genmet_eta = genmet.eta()
        event.genmet_e = genmet.e()
        event.genmet_px = genmet.px()
        event.genmet_py = genmet.py()
        event.genmet_phi = genmet.phi()

        ptcut = 0.
        # you can apply a pt cut on the gen leptons, electrons and muons
        # in HIG-13-004 it was 8 GeV
        if hasattr(self.cfg_ana, 'genPtCut'):
            ptcut = self.cfg_ana.genPtCut



        self.ptSelGentauleps = [lep for lep in event.gentauleps if lep.pt() > ptcut]
        self.ptSelGenleps = [lep for lep in event.genleps if lep.pt() > ptcut]
        self.ptSelGenSummary = []
        # self.ptSelGenSummary = [p for p in event.generatorSummary if p.pt() > ptcut and abs(p.pdgId()) not in [6, 11, 13, 15, 23, 24, 25, 35, 36, 37]]
        # self.ptSelGentaus    = [ lep for lep in event.gentaus    if lep.pt()
        # > ptcut ] # not needed

        #self.l1 = event.diLepton.leg1()
        #self.l2 = event.diLepton.leg2()

        #self.genMatch(event, self.l1, self.ptSelGentauleps, self.ptSelGenleps, self.ptSelGenSummary)
        #self.genMatch(event, self.l2, self.ptSelGentauleps, self.ptSelGenleps, self.ptSelGenSummary)

        #self.attachGenStatusFlag(self.l1)
        #self.attachGenStatusFlag(self.l2)


        #if hasattr(event, 'selectedTaus'):
        #    for tau in event.selectedTaus:
        #        self.genMatch(event, tau, self.ptSelGentauleps, self.ptSelGenleps, self.ptSelGenSummary)

        #if self.cfg_comp.name.find('TT') != -1 or self.cfg_comp.name.find('TTH') == -1:
        #    self.getTopPtWeight(event)

        #if self.cfg_comp.name.find('DY') != -1:
        #    self.getDYMassPtWeight(event)

        return True

    @staticmethod
    def attachGenStatusFlag(lepton):        
        flag = 6

        gen_p = lepton.genp if hasattr(lepton, 'genp') else None
        # Check if we matched a generator particle and it's not a gen jet
        if gen_p and not hasattr(gen_p, 'detFlavour'):
            pdg_id = abs(gen_p.pdgId())
            if pdg_id == 15:
                if gen_p.pt() > 15.:
                    flag = 5
            elif gen_p.pt() > 8.:
                if pdg_id == 11:
                    flag = 1
                elif pdg_id == 13:
                    flag = 2
                # else:
                #     print 'Matched gen p with weird pdg ID', pdg_id

                if flag in [1, 2]:
                    if gen_p.statusFlags().isDirectPromptTauDecayProduct():
                        flag += 2
                    elif not gen_p.statusFlags().isPrompt():
                        flag = 6

        lepton.gen_match = flag


    @staticmethod
    def getFinalTau(tau):
        for i_d in xrange(tau.numberOfDaughters()):
            if tau.daughter(i_d).pdgId() == tau.pdgId():
                return CountEvents.getFinalTau(tau.daughter(i_d))
        return tau        

    @staticmethod
    def getGenTauJets(event):
        event.genTauJets = []
        event.genTauJetConstituents = []
        for gentau in event.gentaus:
            gentau = CountEvents.getFinalTau(gentau)

            c_genjet = TauGenTreeProducer.finalDaughters(gentau)
            c_genjet = [d for d in c_genjet if abs(d.pdgId()) not in [12, 14, 16]]
            p4_genjet = sum((d.p4() for d in c_genjet if abs(d.pdgId()) not in [12, 14, 16]), ROOT.math.XYZTLorentzVectorD())

            genjet = GenParticle(gentau)
            genjet.setP4(p4_genjet)

            if p4_genjet.pt() > 15.:
                event.genTauJets.append(genjet)
                event.genTauJetConstituents.append(c_genjet)


    @staticmethod
    def genMatch(event, leg, ptSelGentauleps, ptSelGenleps, ptSelGenSummary, 
                 dR=0.2, matchAll=True):

        dR2 = dR * dR

        leg.isTauHad = False
        leg.isTauLep = False
        leg.isPromptLep = False
        leg.genp = None

        best_dr2 = dR2

        # The following would work for pat::Taus, but we also want to flag a 
        # muon/electron as coming from a hadronic tau with the usual definition
        # if this happens

        # if hasattr(leg, 'genJet') and leg.genJet():
        #     if leg.genJet().pt() > 15.:
        #         dr2 = deltaR2(leg.eta(), leg.phi(), leg.genJet().eta(), leg.genJet().phi())
        #         if dr2 < best_dr2:
        #             best_dr2 = dr2
        #             leg.genp = leg.genJet()
        #             leg.genp.setPdgId(-15 * leg.genp.charge())
        #             leg.isTauHad = True
        
        # RM: needed to append genTauJets to the events,
        #     when genMatch is used as a static method
        if not hasattr(event, 'genTauJets'):
            CountEvents.getGenTauJets(event)

        l1match, dR2best = bestMatch(leg, event.genTauJets)
        if dR2best < best_dr2:
            best_dr2 = dR2best
            leg.genp = GenParticle(l1match)
            leg.genp.setPdgId(-15 * leg.genp.charge())
            leg.isTauHad = True
            # if not leg.genJet():
            #     print 'Warning, tau does not have matched gen tau'
            # elif leg.genJet().pt() < 15.:
            #     print 'Warning, tau has matched gen jet but with pt =', leg.genJet().pt()

        # to generated leptons from taus
        l1match, dR2best = bestMatch(leg, ptSelGentauleps)
        if dR2best < best_dr2:
            best_dr2 = dR2best
            leg.genp = l1match
            leg.isTauLep = True
            leg.isTauHad = False

        # to generated prompt leptons
        l1match, dR2best = bestMatch(leg, ptSelGenleps)
        if dR2best < best_dr2:
            best_dr2 = dR2best
            leg.genp = l1match
            leg.isPromptLep = True
            leg.isTauLep = False
            leg.isTauHad = False

        if best_dr2 < dR2:
            return

        # match with any other relevant gen particle
        if matchAll:
            l1match, dR2best = bestMatch(leg, ptSelGenSummary)
            if dR2best < best_dr2:
                leg.genp = l1match
                return

            # Ok do one more Pythia 8 trick...
            # This is to overcome that the GenAnalyzer doesn't like particles
            # that have daughters with same pdgId and status 71
            if not hasattr(event, 'pythiaQuarksGluons'):
                event.pythiaQuarksGluons = []
                for gen in event.genParticles:
                    pdg = abs(gen.pdgId())
                    status = gen.status()
                    if pdg in [1, 2, 3, 4, 5, 21] and status > 3:
                        if gen.isMostlyLikePythia6Status3():
                            event.pythiaQuarksGluons.append(gen)

            
            l1match, dR2best = bestMatch(leg, event.pythiaQuarksGluons)
            if dR2best < best_dr2:
                leg.genp = l1match
                return

            # Now this may be a pileup lepton, or one whose ancestor doesn't
            # appear in the gen summary because it's an unclear case in Pythia 8
            # To check the latter, match against jets as well...
            l1match, dR2best = bestMatch(leg, event.genJets)
            # Check if there's a gen jet with pT > 10 GeV (otherwise it's PU)
            if dR2best < dR2 and l1match.pt() > 10.:
                leg.genp = PhysicsObject(l1match)

                jet, dR2best = bestMatch(l1match, event.jets)

                if dR2best < dR2:
                    leg.genp.detFlavour = jet.partonFlavour()
                else:
                    print 'no match found', leg.pt(), leg.eta()

    @staticmethod
    def getTopPtWeight(event):
        ttbar = [p for p in event.genParticles if abs(p.pdgId()) == 6 and p.statusFlags().isLastCopy() and p.statusFlags().fromHardProcess()]

        if len(ttbar) == 2:
            top_1_pt = ttbar[0].pt()
            top_2_pt = ttbar[1].pt()

            if top_1_pt > 400:
                top_1_pt = 400.
            if top_2_pt > 400:
                top_2_pt = 400.

            topweight = math.sqrt(math.exp(0.156-0.00137*top_1_pt)*math.exp(0.156-0.00137*top_2_pt))

            event.top_1_pt = top_1_pt
            event.top_2_pt = top_2_pt
            event.topweight = topweight
            event.eventWeight *= topweight

    @staticmethod
    def p4sum(ps):
        '''Returns four-vector sum of objects in passed list. Returns None
        if empty. Note that python sum doesn't work since p4() + 0/None fails,
        but will be possible in future python'''
        if not ps:
            return None
        p4 = ps[0].p4()
        for i in xrange(len(ps) - 1):
            p4 += ps[i + 1].p4()
        return p4


    @staticmethod
    def getParentBoson(event):
        leptons_prompt = [p for p in event.genParticles if abs(p.pdgId()) in [11, 12, 13, 14] and p.fromHardProcessFinalState()]
        taus_prompt = [p for p in event.genParticles if p.statusFlags().isDirectHardProcessTauDecayProduct()]
        all = leptons_prompt + taus_prompt
        return CountEvents.p4sum(all)

    @staticmethod 
    def getDYMassPtWeight(event):
        if not hasattr(event, 'parentBoson'):
            event.parentBoson = CountEvents.getParentBoson(event)
        event.dy_weight = getDYWeight(event.parentBoson.mass(), event.parentBoson.pt())

