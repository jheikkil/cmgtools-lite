from CMGTools.H2TauTau.proto.analyzers.H2TauTauTreeProducer import H2TauTauTreeProducer


class H2TauTauTreeProducerAZh(H2TauTauTreeProducer):

    '''Tree producer for the H->tau tau->mu mu analysis.'''

    def declareVariables(self, setup):

        super(H2TauTauTreeProducerAZh, self).declareVariables(setup)

       # self.bookMuon(self.tree, 'l1')
       # self.bookMuon(self.tree, 'l2')

       # self.bookGenParticle(self.tree, 'l1_gen')
       # self.bookGenParticle(self.tree, 'l2_gen')

        self.bookParticle(self.tree, 'Zboson')
        self.bookLepton(self.tree, 'Z_l1')
        self.bookLepton(self.tree, 'Z_l2')

        self.bookGenParticle(self.tree, 'Z_l1_gen')
        self.bookGenParticle(self.tree, 'Z_l2_gen')

        self.bookParticle(self.tree, 'Zboson_mm')
        self.bookMuon(self.tree, 'Z_mm_l1')
        self.bookMuon(self.tree, 'Z_mm_l2')

        self.bookGenParticle(self.tree, 'Z_mm_l1_gen')
        self.bookGenParticle(self.tree, 'Z_mm_l2_gen')

        self.bookParticle(self.tree, 'Zboson_ee')
        self.bookEle(self.tree, 'Z_ee_l1')
        self.bookEle(self.tree, 'Z_ee_l2')

        self.bookGenParticle(self.tree, 'Z_ee_l1_gen')
        self.bookGenParticle(self.tree, 'Z_ee_l2_gen')


        self.bookParticle(self.tree, 'Hboson')
        self.bookLepton(self.tree, 'H_l1')
        self.bookLepton(self.tree, 'H_l2')

        self.bookGenParticle(self.tree, 'H_l1_gen')
        self.bookGenParticle(self.tree, 'H_l2_gen')

        #mt

        self.bookParticle(self.tree, 'Hboson_mt')
        self.bookMuon(self.tree, 'H_mt_l1')
        self.bookTau(self.tree, 'H_mt_l2')

        self.bookGenParticle(self.tree, 'H_mt_l1_gen')
        self.bookGenParticle(self.tree, 'H_mt_l2_gen')

        #et

        self.bookParticle(self.tree, 'Hboson_et')
        self.bookEle(self.tree, 'H_et_l1')
        self.bookTau(self.tree, 'H_et_l2')

        self.bookGenParticle(self.tree, 'H_et_l1_gen')
        self.bookGenParticle(self.tree, 'H_et_l2_gen')

        #tt

        self.bookParticle(self.tree, 'Hboson_tt')
        self.bookTau(self.tree, 'H_tt_l1')
        self.bookTau(self.tree, 'H_tt_l2')

        self.bookGenParticle(self.tree, 'H_tt_l1_gen')
        self.bookGenParticle(self.tree, 'H_tt_l2_gen')

        #em

        self.bookParticle(self.tree, 'Hboson_em')
        self.bookEle(self.tree, 'H_em_l1')
        self.bookMuon(self.tree, 'H_em_l2')

        self.bookGenParticle(self.tree, 'H_em_l1_gen')
        self.bookGenParticle(self.tree, 'H_em_l2_gen')
       
        #A
        
        self.bookParticle(self.tree, 'Aboson')

        self.bookTau(self.tree, 'tau1')
        self.bookGenParticle(self.tree, 'tau1_gen')

    def process(self, event):
        super(H2TauTauTreeProducerAZh, self).process(event)

      #  mu1 = event.diLepton.leg1()
      #  mu2 = event.diLepton.leg2()
 
            
      #  self.fillMuon(self.tree, 'l1', mu1)
      #  self.fillMuon(self.tree, 'l2', mu2)

        if hasattr(event, 'Zboson'):
            Zboson = event.Zboson[0]
            Zmu1 = event.Zboson[0].leg1()
            Zmu2 = event.Zboson[0].leg2()         

          #  print 'Z JALAT'
          #  print event.Zboson[0].leg1()
          #  print event.Zboson[0].leg2()

            self.fillLepton(self.tree, 'Z_l1', Zmu1)
            self.fillLepton(self.tree, 'Z_l2', Zmu2)
            self.fillParticle(self.tree, 'Zboson', Zboson)

            if hasattr(Zmu1, 'genp') and Zmu1.genp:
                self.fillGenParticle(self.tree, 'Z_l1_gen', Zmu1.genp)
            if hasattr(Zmu2, 'genp') and Zmu2.genp:
                self.fillGenParticle(self.tree, 'Z_l2_gen', Zmu2.genp)

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

        if hasattr(event, 'Hboson'):
            Hboson = event.Hboson[0]
            Hmu1 = event.Hboson[0].leg1()
       	    Htau2 = event.Hboson[0].leg2()

            #print 'H JALAT'
            #print event.Hboson[0].leg1()
            #print event.Hboson[0].leg2()

            self.fillLepton(self.tree, 'H_l1', Hmu1)
       	    self.fillLepton(self.tree, 'H_l2', Htau2)
            
            self.fillParticle(self.tree, 'Hboson', Hboson)

            if hasattr(Hmu1, 'genp') and Hmu1.genp:
                self.fillGenParticle(self.tree, 'H_l1_gen', Hmu1.genp)
            if hasattr(Htau2, 'genp') and Htau2.genp:
       	        self.fillGenParticle(self.tree, 'H_l2_gen', Htau2.genp)


        #mt

        if hasattr(event, 'Hboson_mt'):
            for i in xrange( len(event.Hboson_mt) ):
                #if event.Hboson_mt[i].leg1().gen_match==4 and event.Hboson_mt[i].leg2().gen_match==5:
                    Hboson_mt = event.Hboson_mt[i]
                    H_mt_mu1 = event.Hboson_mt[i].leg1()
                    H_mt_tau2 = event.Hboson_mt[i].leg2()

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


        #et

        if hasattr(event, 'Hboson_et'):
            for i in xrange( len(event.Hboson_et) ):
                #if event.Hboson_et[i].leg1().gen_match==3 and event.Hboson_et[i].leg2().gen_match==5:
                    Hboson_et = event.Hboson_et[i]
                    H_et_el1 = event.Hboson_et[i].leg1()
                    H_et_tau2 = event.Hboson_et[i].leg2()

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

        #tt

        if hasattr(event, 'Hboson_tt'):
            for i in xrange( len(event.Hboson_tt) ):
                #if event.Hboson_tt[i].leg1().gen_match==5 and event.Hboson_tt[i].leg2().gen_match==5:
                    Hboson_tt = event.Hboson_tt[i]
                    H_tt_tau1 = event.Hboson_tt[i].leg1()
                    H_tt_tau2 = event.Hboson_tt[i].leg2()

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
        #em

        if hasattr(event, 'Hboson_em'):
            for i in xrange( len(event.Hboson_em) ):
                #if event.Hboson_em[i].leg1().gen_match==3 and event.Hboson_em[i].leg2().gen_match==4:
                    Hboson_em = event.Hboson_em[i]
                    H_em_el1 = event.Hboson_em[i].leg1()
                    H_em_mu2 = event.Hboson_em[i].leg2()

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


        if hasattr(event, 'Aboson'):
            Aboson = event.Aboson[0]
            self.fillParticle(self.tree, 'Aboson', Aboson)

       # if hasattr(mu1, 'genp') and mu1.genp:
       #     self.fillGenParticle(self.tree, 'l1_gen', mu1.genp)
       # if hasattr(mu2, 'genp') and mu2.genp:
       #     self.fillGenParticle(self.tree, 'l2_gen', mu2.genp)

        #if event.selectedTaus:
        if hasattr(event, 'selectedTaus'):
            tau1 = event.selectedTaus[0]
            self.fillTau(self.tree, 'tau1', tau1)
            if hasattr(tau1, 'genp') and tau1.genp:
                self.fillGenParticle(self.tree, 'tau1_gen', tau1.genp)

        self.fillTree(event)
        
