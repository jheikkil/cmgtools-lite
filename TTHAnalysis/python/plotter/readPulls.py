from decimal import Decimal
from math import log
from collections import OrderedDict

#/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/

#failing
prefit_0 = ["/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_10_20_muonFR_signal_fail_prefit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_20_30_muonFR_signal_fail_prefit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_30_40_muonFR_signal_fail_prefit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_40_60_muonFR_signal_fail_prefit.txt"]

postfit_0 = ["/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_10_20_muonFR_signal_fail_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_20_30_muonFR_signal_fail_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_30_40_muonFR_signal_fail_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_40_60_muonFR_signal_fail_postfit.txt"]

#list of prefit files, passing 
prefit_1 = ["/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_10_20_muonFR_signal_pass_prefit.txt", 
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_20_30_muonFR_signal_pass_prefit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_30_40_muonFR_signal_pass_prefit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_40_60_muonFR_signal_pass_prefit.txt"]

postfit_1 = ["/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_10_20_muonFR_signal_pass_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_20_30_muonFR_signal_pass_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_30_40_muonFR_signal_pass_postfit.txt",
"/eos/user/j/jheikkil/www/FR_Oct12/muon_1p2_muonFR_signal_pt.dir/pfmt_fix_for_pt_bin_40_60_muonFR_signal_pass_postfit.txt"]

pulls_fail = OrderedDict()
pulls_pass = OrderedDict()

for index in range(4):
    VZ_pre_fail = 0.0
    VZ_post_fail = 0.0
    VZ_pre_pass = 0.0
    VZ_post_pass = 0.0 

    VZ_pre_fail_err = 0.0
    VZ_post_fail_err = 0.0
    VZ_pre_pass_err = 0.0
    VZ_post_pass_err = 0.0

    DY_pre_pass = 0.0
    DY_pre_fail = 0.0

    for case in range(2):
        #print "Case is: ", case
        if case == 0: ##fail
            f1=open(prefit_0[index], "r")
            f2=open(postfit_0[index], "r")
        else: #pass
            f1=open(prefit_1[index], "r")
            f2=open(postfit_1[index], "r")

        lines_1 = f1.readlines()
        lines_2 = f2.readlines()

        #-5 for constrained, -3 for old
        #print lines_1[-3]
        theta = float(lines_1[-5].split()[2])
        theta_Unc = float(lines_1[-5].split()[4])
        #print theta, theta_Unc

        if case == 0:
            VZ_pre_fail = float(lines_1[1].split()[1])
            VZ_post_fail = float(lines_2[1].split()[1])
            DY_pre_fail = float(lines_1[0].split()[1])
            VZ_pre_fail_err = float(lines_1[1].split()[3])
            VZ_post_fail_err = float(lines_2[1].split()[3])
        else:
            VZ_pre_pass = float(lines_1[1].split()[1])
            VZ_post_pass = float(lines_2[1].split()[1])
       	    DY_pre_pass = float(lines_1[0].split()[1])
            VZ_pre_pass_err = float(lines_1[1].split()[3])
            VZ_post_pass_err = float(lines_2[1].split()[3])
          
    total_post = VZ_post_fail + VZ_post_pass
    total_pre = VZ_pre_fail + VZ_pre_pass
    ratio_VZ = total_post/total_pre ##(VZ_post_fail + VZ_post_pass)/(VZ_pre_fail + VZ_pre_pass)   

    ratio_VZ_unc = ratio_VZ*pow( (VZ_post_fail_err*VZ_post_fail_err + VZ_post_pass_err*VZ_post_pass_err)/pow(total_post, 2) + (VZ_pre_pass_err*VZ_pre_pass_err+VZ_pre_fail_err*VZ_pre_fail_err)/pow(total_pre, 2), 0.5)   

    ratio_pass = VZ_pre_pass/(DY_pre_pass + VZ_pre_pass)
    ratio_fail = VZ_pre_fail/(DY_pre_fail + VZ_pre_fail)

    ratio_fit = pow(2, theta)
    ratio_fit_Up = pow(2, theta+theta_Unc)-pow(2,theta)
    ratio_fit_Dn = pow(2, theta-theta_Unc)-pow(2,theta) 

    #print log(2)

    print "Passing and failing %.1f, %.1f" %(100*ratio_pass,100*ratio_fail)
    print "Ratio from the fit: %.2f + %.2f %.2f" %(ratio_fit, ratio_fit_Up, ratio_fit_Dn)
 
       #VZ_pre = lines_1[1].split()
       #VZ_post = lines_2[1].split()

       #DY_pre = lines_1[0].split()
       #DY_post = lines_2[0].split()
 
       #print VZ_pre,VZ_post,DY_pre#,DY_post

       #VZ_pre_value = float(VZ_pre[1])
       #VZ_post_value = float(VZ_post[1])

       #VZ_pre_error = float(VZ_pre[3])
       #VZ_post_error = float(VZ_post[3])
       
       #DY_pre_value = float(DY_pre[1])

       #print VZ_pre_value, VZ_post_value
       #print VZ_pre_value/(VZ_pre_value+DY_pre_value)
       #ratio = VZ_post_value/VZ_pre_value
       #if VZ_post_value > 0.0:
       #    ratio_unc = ratio*pow( (pow((VZ_pre_error/VZ_pre_value),2) + pow((VZ_post_error/VZ_post_value),2)), 0.5  )       
       #else:
       #    ratio_unc = 0.0                      
       #print "Pull is ", ratio
       #print "Uncertainty ", ratio_unc
       #if case == 0:
       #    pulls_fail[ratio] = ratio_unc
       #else:
       #    pulls_pass[ratio] = ratio_unc

#print "Failing pulls: ", pulls_fail
#print "Passing pulls: ", pulls_pass
