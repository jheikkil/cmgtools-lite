from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhEETT(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhEETT, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')


        #tt

        self.bookParticle(self.tree, 'Hboson_tt')
        self.bookTau(self.tree, 'H_tt_l1')
        self.bookTau(self.tree, 'H_tt_l2')

        self.bookGenParticle(self.tree, 'H_tt_l1_gen')
        self.bookGenParticle(self.tree, 'H_tt_l2_gen')

        #A_tt

        self.bookParticle(self.tree, 'Aboson_tt')
  

    def process(self, event):
        super(H2TauTauTreeProducerAZhEETT, self).process(event)

        if hasattr(event, 'Zboson_ee'): #and event.Zboson_ee[0].leg1().gen_match==1 and event.Zboson_ee[0].leg2().gen_match==1:
            Zboson_ee = event.Zboson_ee[0]
            Zel1_ee = event.Zboson_ee[0].leg1()
            Zel2_ee = event.Zboson_ee[0].leg2()

            self.fillEle(self.tree, 'Z_ee_l1', Zel1_ee)
            self.fillEle(self.tree, 'Z_ee_l2', Zel2_ee)
            self.fillParticle(self.tree, 'Zboson_ee', Zboson_ee)

            if hasattr(Zel1_ee, 'genp') and Zel1_ee.genp:
                self.fillGenParticle(self.tree, 'Z_ee_l1_gen', Zel1_ee.genp)
            if hasattr(Zel2_ee, 'genp') and Zel2_ee.genp:
                self.fillGenParticle(self.tree, 'Z_ee_l2_gen', Zel2_ee.genp)

        #tt

        if hasattr(event, 'Hboson_tt'):
                Hboson_tt = event.Hboson_tt[0]
                H_tt_tau1 = event.Hboson_tt[0].leg1()
                H_tt_tau2 = event.Hboson_tt[0].leg2()

                self.fillTau(self.tree, 'H_tt_l1', H_tt_tau1)
                self.fillTau(self.tree, 'H_tt_l2', H_tt_tau2)

                self.fillParticle(self.tree, 'Hboson_tt', Hboson_tt)

                if hasattr(H_tt_tau1, 'genp') and H_tt_tau1.genp:
                    self.fillGenParticle(self.tree, 'H_tt_l1_gen', H_tt_tau1.genp)
                if hasattr(H_tt_tau2, 'genp') and H_tt_tau2.genp:
                    self.fillGenParticle(self.tree, 'H_tt_l2_gen', H_tt_tau2.genp) 

        if hasattr(event, 'Aboson_tt'):
            Aboson_tt = event.Aboson_tt[0]
            self.fillParticle(self.tree, 'Aboson_tt', Aboson_tt)

        if hasattr(event, 'Zboson_ee') and hasattr(event, 'Hboson_tt') and event.Hboson_tt[0].mass()>-1 and event.Zboson_ee[0].mass()>-1:
            self.fillTree(event)
        
