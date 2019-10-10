
import ROOT

newFile_map = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsUW_3010/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}



file_map_SS = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/2609_SS/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


file_map_OS = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'emmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'emmm' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/0810_WZ/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


#keys = ["eett", "mmtt"]
for channel in file_map_SS.keys() :


    print channel
    #inName = '/afs/cern.ch/work/t/truggles/public/forAZH/dcSync/20180501/htt_zh.inputs-mssm-13TeV_4LMass_new.root'
    inName = file_map_SS[ channel ]
    inName_WZ = file_map_OS[ channel ]
    outName = newFile_map[ channel ]    

    #outFile = ROOT.TFile( outName, 'UPDATE' )
    inFile = ROOT.TFile( inName, 'READ' )
    inFile_WZ = ROOT.TFile( inName_WZ, 'READ' )
    outFile = ROOT.TFile( outName, 'UPDATE' )

    #fetch here obs and FR
    h_FR = outFile.Get( "x_data_FR"  )
    int_FR = h_FR.Integral()

    h_data = outFile.Get( "x_data_obs"  )
    int_data = h_data.Integral()
 
    #make changes to data
    print "DATA, ",int_data, int_FR, int_data-int_FR    

    h_data.Add(h_FR, -1.0)
    int_data2 = h_data.Integral()
    print "data-FR ",int_data2

    #fetch shape for shape for data_FR
    h_SS_forShape = inFile.Get( "x_data_obs" )
    h_SS_forObs = inFile.Get( "x_data_obs" )
    h_WZ_forObs = inFile_WZ.Get( "x_WZ" )

    h_SS_forObs.Scale(0.4*int_FR/h_SS_forObs.Integral())
    h_WZ_forObs.Scale(0.6*int_FR/h_WZ_forObs.Integral())

    print "EKA nama, ", h_SS_forObs.Integral(), h_WZ_forObs.Integral(), h_SS_forObs.Integral()+h_WZ_forObs.Integral()
    h_SS_forObs.Add(h_WZ_forObs)
    int_SS_obs = h_SS_forObs.Integral()
    print "LISAYS, ",int_SS_obs
    print "FR ",int_FR

    #h_SS_forObs.Scale(int_FR/int_SS_obs)
    h_data.Add(h_SS_forObs)
    int_data3 = h_data.Integral()

    print "new data, ",h_data.Integral()	
    h_data.Write("x_data_obs_3", outFile.kOverwrite)

    #change the shape
    print "Changing the FR shape"
    #h_SS_forShape = inFile.Get( "x_data_obs" )
    int_SS_shape = h_SS_forShape.Integral()
    h_SS_forShape.Scale(int_FR/int_SS_shape)
    h_SS_forShape.SetName("x_data_FR") 
    h_SS_forShape.Write("x_data_FR", outFile.kOverwrite)
    #outFile.Delete("x_data_FR;1")
    
    #h_data.Add(h_SS_forShape)
    #int_data3 = h_data.Integral()

    #print "new data, ",int_data3
    #h_data.Write("x_data_obs") #, outFile.kOverwrite)
    #outFile.Delete("x_data_obs;1")

    run = 0

    if run and channel in ["eett", "mmtt"]:
        # get and scale x_data_FR_FRtau_normDown-, x_data_FR_FRtau_normUp
        h_FR_up = outFile.Get( "x_data_FR_FRtau_normUp")
        h_FR_dn = outFile.Get( "x_data_FR_FRtau_normDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        
        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.Write("x_data_FR_FRtau_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
       	h_SS_forShape.Write("x_data_FR_FRtau_normDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_FRtau_normUp;1")
        #outFile.Delete("x_data_FR_FRtau_normDown;1")

    elif run and channel in ["eeet", "mmet"]:
        # x_data_FR_FRel_normDown, x_data_FR_FRel_normUp, x_data_FR_FRtau_normUp, x_data_FR_FRtau_normDown
        h_FR_up = outFile.Get( "x_data_FR_FRtau_normUp")
        h_FR_dn = outFile.Get( "x_data_FR_FRtau_normDown")
        h_FR_up2 = outFile.Get( "x_data_FR_FRel_normUp")
        h_FR_dn2 = outFile.Get( "x_data_FR_FRel_normDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

       	h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.Write("x_data_FR_FRtau_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
        h_SS_forShape.Write("x_data_FR_FRtau_normDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.Write("x_data_FR_FRel_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
       	h_SS_forShape.Write("x_data_FR_FRel_normDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_FRtau_normUp;1")
       	#outFile.Delete("x_data_FR_FRtau_normDown;1")
        #outFile.Delete("x_data_FR_FRel_normUp;1")
       	#outFile.Delete("x_data_FR_FRel_normDown;1")

    elif run and channel in ["eeem", "mmem"]:
        h_FR_up = outFile.Get( "x_data_FR_FRel_normUp")
        h_FR_dn = outFile.Get( "x_data_FR_FRel_normDown")
        h_FR_up2 = outFile.Get( "x_data_FR_FRmu_normUp")
       	h_FR_dn2 = outFile.Get( "x_data_FR_FRmu_normDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.Write("x_data_FR_FRel_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
       	h_SS_forShape.Write("x_data_FR_FRel_normDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.Write("x_data_FR_FRmu_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
       	h_SS_forShape.Write("x_data_FR_FRmu_normDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_FRel_normUp;1")
       	#outFile.Delete("x_data_FR_FRel_normDown;1")
        #outFile.Delete("x_data_FR_FRmu_normUp;1")
       	#outFile.Delete("x_data_FR_FRmu_normDown;1")

    elif run and channel in ["eemt", "mmmt"]:
        h_FR_up = outFile.Get( "x_data_FR_FRtau_normUp")
        h_FR_dn = outFile.Get( "x_data_FR_FRtau_normDown")
        h_FR_up2 = outFile.Get( "x_data_FR_FRmu_normUp")
       	h_FR_dn2 = outFile.Get( "x_data_FR_FRmu_normDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.Write("x_data_FR_FRtau_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
       	h_SS_forShape.Write("x_data_FR_FRtau_normDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.Write("x_data_FR_FRmu_normUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
       	h_SS_forShape.Write("x_data_FR_FRmu_normDown", outFile.kOverwrite)
    
       # x_data_FR_FRmu_normDown, x_data_FR_FRmu_normUp
        #outFile.Delete("x_data_FR_FRtau_normUp;1")
        #outFile.Delete("x_data_FR_FRtau_normDown;1")
        #outFile.Delete("x_data_FR_FRmu_normUp;1")
        #outFile.Delete("x_data_FR_FRmu_normDown;1")


    
    
    outFile.Purge()
    #outFile.Purge("x_data_obs")
    #outFile.Purge()
    outFile.Close()
    inFile.Close()
