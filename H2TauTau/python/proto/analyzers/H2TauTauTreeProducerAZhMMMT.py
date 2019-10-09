from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhMMMT(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhMMMT, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')

        #mt

        self.bookParticle(self.tree, 'Hboson_mt')
        self.bookMuon(self.tree, 'H_mt_l1')
        self.bookTau(self.tree, 'H_mt_l2')

        self.bookGenParticle(self.tree, 'H_mt_l1_gen')
        self.bookGenParticle(self.tree, 'H_mt_l2_gen')

        #A_mt

        self.bookParticle(self.tree, 'Aboson_mt')


    def process(self, event):
        super(H2TauTauTreeProducerAZhMMMT, self).process(event)

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

        #mt

        if hasattr(event, 'Hboson_mt'):
                Hboson_mt = event.Hboson_mt[0]
                H_mt_mu1 = event.Hboson_mt[0].leg1()
                H_mt_tau2 = event.Hboson_mt[0].leg2()

                self.fillMuon(self.tree, 'H_mt_l1', H_mt_mu1)
                self.fillTau(self.tree, 'H_mt_l2', H_mt_tau2)

                self.fillParticle(self.tree, 'Hboson_mt', Hboson_mt)

                if hasattr(H_mt_mu1, 'genp') and H_mt_mu1.genp:
                    self.fillGenParticle(self.tree, 'H_mt_l1_gen', H_mt_mu1.genp)
                if hasattr(H_mt_tau2, 'genp') and H_mt_tau2.genp:
                    self.fillGenParticle(self.tree, 'H_mt_l2_gen', H_mt_tau2.genp)


        if hasattr(event, 'Aboson_mt'):
            Aboson_mt = event.Aboson_mt[0]
            self.fillParticle(self.tree, 'Aboson_mt', Aboson_mt)


        if hasattr(event, 'Zboson_mm') and hasattr(event, 'Hboson_mt') and event.Hboson_mt[0].mass()>-1 and event.Zboson_mm[0].mass()>-1:
            self.fillTree(event)
        
