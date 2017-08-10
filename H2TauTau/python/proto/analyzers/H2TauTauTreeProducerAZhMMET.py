from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhMMET(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhMMET, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')

        #et

        self.bookParticle(self.tree, 'Hboson_et')
        self.bookEle(self.tree, 'H_et_l1')
        self.bookTau(self.tree, 'H_et_l2')

        self.bookGenParticle(self.tree, 'H_et_l1_gen')
        self.bookGenParticle(self.tree, 'H_et_l2_gen')

        #A_et

        self.bookParticle(self.tree, 'Aboson_et')

    def process(self, event):
        super(H2TauTauTreeProducerAZhMMET, self).process(event)

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

        #et

        if hasattr(event, 'Hboson_et'):
           # for i in xrange( len(event.Hboson_et) ):
                #if event.Hboson_et[i].leg1().gen_match==3 and event.Hboson_et[i].leg2().gen_match==5:
                Hboson_et = event.Hboson_et[0]
                H_et_el1 = event.Hboson_et[0].leg1()
                H_et_tau2 = event.Hboson_et[0].leg2()

                 #   print 'H JALAT'
                 #   print event.Hboson_et[i].leg1()
                 #   print event.Hboson_et[i].leg2()

                self.fillEle(self.tree, 'H_et_l1', H_et_el1)
                self.fillTau(self.tree, 'H_et_l2', H_et_tau2)

                self.fillParticle(self.tree, 'Hboson_et', Hboson_et)

                if hasattr(H_et_el1, 'genp') and H_et_el1.genp:
                    self.fillGenParticle(self.tree, 'H_et_l1_gen', H_et_el1.genp)
                if hasattr(H_et_tau2, 'genp') and H_et_tau2.genp:
                    self.fillGenParticle(self.tree, 'H_et_l2_gen', H_et_tau2.genp)

        if hasattr(event, 'Aboson_et'):
            Aboson_et = event.Aboson_et[0]
            self.fillParticle(self.tree, 'Aboson_et', Aboson_et)

        self.fillTree(event)
        
