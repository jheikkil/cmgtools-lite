from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhEEET(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhEEET, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')

        #et

        self.bookParticle(self.tree, 'Hboson_et')
        self.bookEle(self.tree, 'H_et_l1')
        self.bookTau(self.tree, 'H_et_l2')

        self.bookGenParticle(self.tree, 'H_et_l1_gen')
        self.bookGenParticle(self.tree, 'H_et_l2_gen')

        #A_et

        self.bookParticle(self.tree, 'Aboson_et')

    def process(self, event):
        super(H2TauTauTreeProducerAZhEEET, self).process(event)

        if hasattr(event, 'Zboson_ee'): #and event.Zboson_ee[0].leg1().gen_match==1 and event.Zboson_ee[0].leg2().gen_match==1:
            Zboson_ee = event.Zboson_ee[0]
            Zel1_ee = event.Zboson_ee[0].leg1()
            Zel2_ee = event.Zboson_ee[0].leg2()

           # print 'Z JALAT'
           # print event.Zboson_ee[0].leg1()
           # print event.Zboson_ee[0].leg2()

            self.fillEle(self.tree, 'Z_ee_l1', Zel1_ee)
            self.fillEle(self.tree, 'Z_ee_l2', Zel2_ee)
            self.fillParticle(self.tree, 'Zboson_ee', Zboson_ee)

            if hasattr(Zel1_ee, 'genp') and Zel1_ee.genp:
                self.fillGenParticle(self.tree, 'Z_ee_l1_gen', Zel1_ee.genp)
            if hasattr(Zel2_ee, 'genp') and Zel2_ee.genp:
                self.fillGenParticle(self.tree, 'Z_ee_l2_gen', Zel2_ee.genp)

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

        if hasattr(event, 'Zboson_ee') and hasattr(event, 'Hboson_et') and event.Hboson_et[0].mass()>-1 and event.Zboson_ee[0].mass()>-1:
            self.fillTree(event)

        
