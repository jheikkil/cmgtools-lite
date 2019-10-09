from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhMMEM(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhMMEM, self).declareVariables(setup)


        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')


        #em

        self.bookParticle(self.tree, 'Hboson_em')
        self.bookEle(self.tree, 'H_em_l1')
        self.bookMuon(self.tree, 'H_em_l2')

        self.bookGenParticle(self.tree, 'H_em_l1_gen')
        self.bookGenParticle(self.tree, 'H_em_l2_gen')
       
  
        #A_em

        self.bookParticle(self.tree, 'Aboson_em')


    def process(self, event):
        super(H2TauTauTreeProducerAZhMMEM, self).process(event)

        if hasattr(event, 'Zboson_mm'): #and event.Zboson_mm[0].leg1().gen_match==2 and event.Zboson_mm[0].leg2().gen_match==2:
            Zboson_mm = event.Zboson_mm[0]
            Zmu1_mm = event.Zboson_mm[0].leg1()
            Zmu2_mm = event.Zboson_mm[0].leg2()

            self.fillMuon(self.tree, 'Z_mm_l1', Zmu1_mm)
            self.fillMuon(self.tree, 'Z_mm_l2', Zmu2_mm)
            self.fillParticle(self.tree, 'Zboson_mm', Zboson_mm)

            if hasattr(Zmu1_mm, 'genp') and Zmu1_mm.genp:
                self.fillGenParticle(self.tree, 'Z_mm_l1_gen', Zmu1_mm.genp)
            if hasattr(Zmu2_mm, 'genp') and Zmu2_mm.genp:
                self.fillGenParticle(self.tree, 'Z_mm_l2_gen', Zmu2_mm.genp)

        #em

        if hasattr(event, 'Hboson_em'):
                Hboson_em = event.Hboson_em[0]
                H_em_el1 = event.Hboson_em[0].leg1()
                H_em_mu2 = event.Hboson_em[0].leg2()

                self.fillEle(self.tree, 'H_em_l1', H_em_el1)
                self.fillMuon(self.tree, 'H_em_l2', H_em_mu2)

                self.fillParticle(self.tree, 'Hboson_em', Hboson_em)

                if hasattr(H_em_el1, 'genp') and H_em_el1.genp:
                    self.fillGenParticle(self.tree, 'H_em_l1_gen', H_em_el1.genp)
                if hasattr(H_em_mu2, 'genp') and H_em_mu2.genp:
                    self.fillGenParticle(self.tree, 'H_em_l2_gen', H_em_mu2.genp)


        if hasattr(event, 'Aboson_em'):
            Aboson_em = event.Aboson_em[0]
            self.fillParticle(self.tree, 'Aboson_em', Aboson_em)

        if hasattr(event, 'Zboson_mm') and hasattr(event, 'Hboson_em') and event.Hboson_em[0].mass()>-1 and event.Zboson_mm[0].mass()>-1:
            self.fillTree(event)
        
