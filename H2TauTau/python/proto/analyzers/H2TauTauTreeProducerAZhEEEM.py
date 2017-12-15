from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhEEEM(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhEEEM, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')


        #Em
        self.bookParticle(self.tree, 'Hboson_em')
        self.bookEle(self.tree, 'H_em_l1')
        self.bookMuon(self.tree, 'H_em_l2')

        self.bookGenParticle(self.tree, 'H_em_l1_gen')
        self.bookGenParticle(self.tree, 'H_em_l2_gen')
       
        #A_em

        self.bookParticle(self.tree, 'Aboson_em')


    def process(self, event):
        super(H2TauTauTreeProducerAZhEEEM, self).process(event)

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

        #em

        if hasattr(event, 'Hboson_em'):
           # for i in xrange( len(event.Hboson_em) ):
                #if event.Hboson_em[i].leg1().gen_match==3 and event.Hboson_em[i].leg2().gen_match==4:
                Hboson_em = event.Hboson_em[0]
                H_em_el1 = event.Hboson_em[0].leg1()
                H_em_mu2 = event.Hboson_em[0].leg2()

                 #   print 'H JALAT'
                #    print event.Hboson_em[i].leg1()
                 #   print event.Hboson_em[i].leg2()

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

        if hasattr(event, 'Zboson_ee') and hasattr(event, 'Hboson_em') and event.Hboson_em[0].mass()>-1 and event.Zboson_ee[0].mass()>-1:
            self.fillTree(event)

        
