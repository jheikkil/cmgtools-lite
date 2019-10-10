
import ROOT

newFile_map = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'mmet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'mmem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/cardsOS_final_0705/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}
	


file_map_SS = {
    'eeet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/EEET/Aconstr_HsvFit90/common/SR.input.root',
    'mmet' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/MMET/Aconstr_HsvFit90/common/SR.input.root',
    'eett' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/EETT/Aconstr_HsvFit90/common/SR.input.root',
    'mmtt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/MMTT/Aconstr_HsvFit90/common/SR.input.root',
    'eemt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/EEMT/Aconstr_HsvFit90/common/SR.input.root',
    'mmmt' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/MMMT/Aconstr_HsvFit90/common/SR.input.root',
    'eeem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/EEEM/Aconstr_HsvFit90/common/SR.input.root',
    'mmem' : '/afs/cern.ch/work/j/jheikkil/testaus/CMSSW_9_4_6_patch1/src/HiggsAnalysis/CombinedLimit/1504_SS_final/MMEM/Aconstr_HsvFit90/common/SR.input.root',


}


#keys = ["eemt", "mmmt"]
for channel in file_map_SS.keys() :
#for channel in keys:

    print channel
    inName = file_map_SS[ channel ]
    outName = newFile_map[ channel ]    

    inFile = ROOT.TFile( inName, 'READ' )
    outFile = ROOT.TFile( outName, 'UPDATE' )

    #fetch here obs and FR
    h_FR = outFile.Get( "x_data_FR"  )
    int_FR = h_FR.Integral()

    #fetch shape for shape for data_FR
    h_SS_forShape = inFile.Get( "x_data_obs" )

    int_SS_shape = h_SS_forShape.Integral()
    h_SS_forShape.Scale(int_FR/int_SS_shape)
    h_SS_forShape.SetName("x_data_FR") 
    h_SS_forShape.Write("x_data_FR", outFile.kOverwrite)

    for bin in range(1,h_SS_forShape.GetNbinsX()+1):
        print bin, h_SS_forShape.GetBinContent(bin)
        if h_SS_forShape.GetBinContent(bin) < 0: #was <= 0
            print "APUAAAA"

    run = 1

    if run and channel in ["eett", "mmtt"]:
        print "Changing up and down"
        # get and scale x_data_FR_CMS_fake_tDown-, x_data_FR_CMS_fake_tUp
        h_FR_up = outFile.Get( "x_data_FR_CMS_fake_tUp")
        h_FR_dn = outFile.Get( "x_data_FR_CMS_fake_tDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        
        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_tUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_tDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_CMS_fake_tUp;1")
        #outFile.Delete("x_data_FR_CMS_fake_tDown;1")

    elif run and channel in ["eeet", "mmet"]:
        print "Changing up and down"
        # x_data_FR_CMS_fake_eDown, x_data_FR_CMS_fake_eUp, x_data_FR_CMS_fake_tUp, x_data_FR_CMS_fake_tDown
        h_FR_up = outFile.Get( "x_data_FR_CMS_fake_tUp")
        h_FR_dn = outFile.Get( "x_data_FR_CMS_fake_tDown")
        h_FR_up2 = outFile.Get( "x_data_FR_CMS_fake_eUp")
        h_FR_dn2 = outFile.Get( "x_data_FR_CMS_fake_eDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

       	h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_tUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tDown")
        h_SS_forShape.Write("x_data_FR_CMS_fake_tDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_eUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_eUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_eDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_eDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_CMS_fake_tUp;1")
       	#outFile.Delete("x_data_FR_CMS_fake_tDown;1")
        #outFile.Delete("x_data_FR_CMS_fake_eUp;1")
       	#outFile.Delete("x_data_FR_CMS_fake_eDown;1")

    elif run and channel in ["eeem", "mmem"]:
        print "Changing up and down"
        h_FR_up = outFile.Get( "x_data_FR_CMS_fake_eUp")
        h_FR_dn = outFile.Get( "x_data_FR_CMS_fake_eDown")
        h_FR_up2 = outFile.Get( "x_data_FR_CMS_fake_mUp")
       	h_FR_dn2 = outFile.Get( "x_data_FR_CMS_fake_mDown")
        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()
        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_eUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_eUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_eDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_eDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_mUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_mUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_mDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_mDown", outFile.kOverwrite)

        #outFile.Delete("x_data_FR_CMS_fake_eUp;1")
       	#outFile.Delete("x_data_FR_CMS_fake_eDown;1")
        #outFile.Delete("x_data_FR_CMS_fake_mUp;1")
       	#outFile.Delete("x_data_FR_CMS_fake_mDown;1")

    elif run and channel in ["eemt", "mmmt"]:
        print "Changing up and down"
        h_FR_up = outFile.Get( "x_data_FR_CMS_fake_tUp")
        h_FR_dn = outFile.Get( "x_data_FR_CMS_fake_tDown")
        h_FR_up2 = outFile.Get( "x_data_FR_CMS_fake_mUp")
       	h_FR_dn2 = outFile.Get( "x_data_FR_CMS_fake_mDown")

        int_FR_up = h_FR_up.Integral()
        int_FR_dn = h_FR_dn.Integral()

        int_FR_up2 = h_FR_up2.Integral()
        int_FR_dn2 = h_FR_dn2.Integral()

        h_SS_forShape.Scale(int_FR_up/int_FR)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_tUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn/int_FR_up)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_tDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_tDown", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_up2/int_FR_dn)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_mUp")
        h_SS_forShape.Write("x_data_FR_CMS_fake_mUp", outFile.kOverwrite)

        h_SS_forShape.Scale(int_FR_dn2/int_FR_up2)
        h_SS_forShape.SetName("x_data_FR_CMS_fake_mDown")
       	h_SS_forShape.Write("x_data_FR_CMS_fake_mDown", outFile.kOverwrite)
    
       # x_data_FR_CMS_fake_mDown, x_data_FR_CMS_fake_mUp
        #outFile.Delete("x_data_FR_CMS_fake_tUp;1")
        #outFile.Delete("x_data_FR_CMS_fake_tDown;1")
        #outFile.Delete("x_data_FR_CMS_fake_mUp;1")
        #outFile.Delete("x_data_FR_CMS_fake_mDown;1")


    
    
    outFile.Purge()
    #outFile.Purge("x_data_obs")
    #outFile.Purge()
    outFile.Close()
    inFile.Close()
