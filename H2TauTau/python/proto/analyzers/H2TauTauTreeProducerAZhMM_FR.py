from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhMM_FR(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhMM_FR, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')


        #muon
        self.bookMuon(self.tree, 'muon_FR')
        self.bookGenParticle(self.tree, 'muon_FR')


        #electron
        self.bookEle(self.tree, 'electron_FR')
        self.bookGenParticle(self.tree, 'electron_FR_gen')


        #tau

        self.bookTau(self.tree, 'tau_FR')
        self.bookGenParticle(self.tree, 'tau_FR_gen')



    def process(self, event):
        super(H2TauTauTreeProducerAZhMM_FR, self).process(event)

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

        #THIRD LEPTON HERE

        if hasattr(event, 'muon_FR'):
            muon_FR = event.muon_FR[0]
            self.fillMuon(self.tree, 'muon_FR', muon_FR)

            if hasattr(muon_FR, 'genp') and muon_FR.genp:
                self.fillGenParticle(self.tree, 'muon_FR_gen', muon_FR.genp)

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

        if hasattr(event, 'Zboson_mm') and event.Zboson_mm[0].mass()>-1:
            self.fillTree(event)
        
