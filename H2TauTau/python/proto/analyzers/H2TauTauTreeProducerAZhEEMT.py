from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZhEEMT(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZhEEMT, self).declareVariables(setup)

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')


        self.bookParticle(self.tree, 'Hboson_mt')
        self.bookMuon(self.tree, 'H_mt_l1')
        self.bookTau(self.tree, 'H_mt_l2')

        self.bookGenParticle(self.tree, 'H_mt_l1_gen')
        self.bookGenParticle(self.tree, 'H_mt_l2_gen')

        #A_mt

        self.bookParticle(self.tree, 'Aboson_mt')


    def process(self, event):
        super(H2TauTauTreeProducerAZhEEMT, self).process(event)

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

        #mt

        if hasattr(event, 'Hboson_mt'):
            #for i in xrange( len(event.Hboson_mt) ):
                #if event.Hboson_mt[i].leg1().gen_match==4 and event.Hboson_mt[i].leg2().gen_match==5:
                Hboson_mt = event.Hboson_mt[0]
                H_mt_mu1 = event.Hboson_mt[0].leg1()
                H_mt_tau2 = event.Hboson_mt[0].leg2()

                #    print 'H JALAT'
                #    print event.Hboson_mt[i].leg1()
                #    print event.Hboson_mt[i].leg2()

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

        self.fillTree(event)
        
