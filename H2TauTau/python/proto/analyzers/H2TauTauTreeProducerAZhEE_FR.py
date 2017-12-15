from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhEE_FR(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhEE_FR, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')


        #muon
        self.bookMuon(self.tree, 'muon_FR')
        self.bookGenParticle(self.tree, 'muon_FR_gen')


        #electron
        self.bookEle(self.tree, 'electron_FR')
        self.bookGenParticle(self.tree, 'electron_FR_gen')


        #tau

        self.bookTau(self.tree, 'tau_FR')
        self.bookGenParticle(self.tree, 'tau_FR_gen')



    def process(self, event):
        super(H2TauTauTreeProducerAZhEE_FR, self).process(event)

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

        #THIRD LEPTON HERE

        if hasattr(event, 'muon_FR'):
            muon_FR_l1 = event.muon_FR[0]
            self.fillMuon(self.tree, 'muon_FR', muon_FR_l1)

            if hasattr(muon_FR_l1, 'genp') and muon_FR_l1.genp:
            #    print "tayta tama"
                self.fillGenParticle(self.tree, 'muon_FR_gen', muon_FR_l1.genp)

        if hasattr(event, 'electron_FR'):
            electron_FR = event.electron_FR[0]
            self.fillEle(self.tree, 'electron_FR', electron_FR)

            if hasattr(electron_FR, 'genp') and electron_FR.genp:
                self.fillGenParticle(self.tree, 'electron_FR_gen', electron_FR.genp)

        if hasattr(event, 'tau_FR'):
            tau_FR = event.tau_FR[0]
            self.fillTau(self.tree, 'tau_FR', tau_FR)

            if hasattr(tau_FR, 'genp') and tau_FR.genp:
                self.fillGenParticle(self.tree, 'tau_FR_gen', tau_FR.genp)

        if hasattr(event, 'Zboson_ee') and event.Zboson_ee[0].mass()>-1:
            self.fillTree(event)
        
