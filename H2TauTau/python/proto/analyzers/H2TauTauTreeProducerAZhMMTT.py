from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhMMTT(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhMMTT, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')


        #tt

        self.bookParticle(self.tree, 'Hboson_tt')
        self.bookTau(self.tree, 'H_tt_l1')
        self.bookTau(self.tree, 'H_tt_l2')

        self.bookGenParticle(self.tree, 'H_tt_l1_gen')
        self.bookGenParticle(self.tree, 'H_tt_l2_gen')

        #A_tt

        self.bookParticle(self.tree, 'Aboson_tt')
  

    def process(self, event):
        super(H2TauTauTreeProducerAZhMMTT, self).process(event)

        if hasattr(event, 'Zboson_mm'): #and event.Zboson_mm[0].leg1().gen_match==2 and event.Zboson_mm[0].leg2().gen_match==2:
            Zboson_mm = event.Zboson_mm[0]
            Zmu1_mm = event.Zboson_mm[0].leg1()
            Zmu2_mm = event.Zboson_mm[0].leg2()

          #  print 'Z JALAT'
          #  print event.Zboson_mm[0].leg1()
          #  print event.Zboson_mm[0].leg2()

            self.fillMuon(self.tree, 'Z_mm_l1', Zmu1_mm)
            self.fillMuon(self.tree, 'Z_mm_l2', Zmu2_mm)
            self.fillParticle(self.tree, 'Zboson_mm', Zboson_mm)

            if hasattr(Zmu1_mm, 'genp') and Zmu1_mm.genp:
                self.fillGenParticle(self.tree, 'Z_mm_l1_gen', Zmu1_mm.genp)
            if hasattr(Zmu2_mm, 'genp') and Zmu2_mm.genp:
                self.fillGenParticle(self.tree, 'Z_mm_l2_gen', Zmu2_mm.genp)


        #tt

        if hasattr(event, 'Hboson_tt'):
           # for i in xrange( len(event.Hboson_tt) ):
                #if event.Hboson_tt[i].leg1().gen_match==5 and event.Hboson_tt[i].leg2().gen_match==5:
                Hboson_tt = event.Hboson_tt[0]
                H_tt_tau1 = event.Hboson_tt[0].leg1()
                H_tt_tau2 = event.Hboson_tt[0].leg2()

                 #   print 'H JALAT'
                 #   print 'INDEKSI ON %d' %i
                 #   print event.Hboson_tt[i].leg1()
                 #   print event.Hboson_tt[i].leg2()

                self.fillTau(self.tree, 'H_tt_l1', H_tt_tau1)
                self.fillTau(self.tree, 'H_tt_l2', H_tt_tau2)

                self.fillParticle(self.tree, 'Hboson_tt', Hboson_tt)

                if hasattr(H_tt_tau1, 'genp') and H_tt_tau1.genp:
                    self.fillGenParticle(self.tree, 'H_tt_l1_gen', H_tt_tau1.genp)
                if hasattr(H_tt_tau2, 'genp') and H_tt_tau2.genp:
                    self.fillGenParticle(self.tree, 'H_tt_l2_gen', H_tt_tau2.genp) 
                #else:
                #    print 'NO PASS'

        if hasattr(event, 'Aboson_tt'):
            Aboson_tt = event.Aboson_tt[0]
            self.fillParticle(self.tree, 'Aboson_tt', Aboson_tt)


        self.fillTree(event)
        
