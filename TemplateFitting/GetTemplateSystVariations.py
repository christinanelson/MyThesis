############################################################
# AUTHOR:  Christina Nelson                                #
# DATE:    May 5 2022                                      #
# Gets difference between nominal and syst variation       #
# for the MC true template. This is done before Multijet   #
# background fit is done.
############################################################

import os,sys,copy,argparse,psutil
sys.path.append("../xAHReader/Plotter/")
sys.path.append("../xAHReader/")

import csv
from Defs import *

# Import input files from Plotter
PATH = ""
from InputFiles import InputFiles
from Luminosities import *
from SystematicsNames_short import Systematics

####################################
# Read arguments
####################################
parser = argparse.ArgumentParser()
parser.add_argument('--years',           action='store',      dest="years",    default='')
parser.add_argument('--njetFlag',        action='store',      dest="njetFlag", default="Inclusive")
parser.add_argument('--muFlag',          action='store',      dest="muFlag",   default="Inclusive")
parser.add_argument('--variation',       action='store',      dest="variation",   default="")

args = parser.parse_args()

if args.years == '':
  print('ERROR: No years were provided, exiting')
  sys.exit(0)

# Get list of years
Datasets = []
YearsStr = args.years
Years    = YearsStr.split('1')
for year in Years:
  if year == '': continue
  Datasets.append('1'+year)

# Get flags
njet = args.njetFlag
mu   = args.muFlag
syst_var = args.variation

if njet == 'Inclusive': njet = ''
if mu   == 'Inclusive': mu   = ''

print('FITINFO: Running on the following dataset ')
print(Datasets)

Channel = "EL" # "EL" or "MU"

# Import lists from Arrays                          
from Arrays import nJetmultiplicities, muFlags
import ROOT
from ROOT import *
import os,sys
gROOT.SetBatch(True)

# Set AtlasStyle
gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
SetAtlasStyle()

####################
# Choose luminosity
####################
Luminosity = dict()
Luminosity["a"] = 0
for dataset in Datasets:
  if dataset=="15":
    Luminosity["a"] += Luminosity_2015
  elif dataset=="16":
    Luminosity["a"] += Luminosity_2016
  elif dataset=="17":
    Luminosity["d"] = Luminosity_2017
  elif dataset=="18":
    Luminosity["e"] = Luminosity_2018

####################################
# Calculate total luminosity                             
####################################
TotalLumi = 0
for key,lumi in Luminosity.iteritems():
  TotalLumi += lumi

Files = dict()
Campaigns  = []
for dataset in Datasets:
  DataPeriod = "Data"+dataset
  if dataset == "15" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "16" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "17" and "d" not in Campaigns: Campaigns.append("d")
  elif dataset == "18" and "e" not in Campaigns: Campaigns.append("e")
for campaign in Campaigns:
  Files["MC16"+campaign+"_Signal_SRwoMET"] = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger]
  for bkg in Backgrounds:
    Files["MC16"+campaign+"_"+bkg+"_SRwoMET"] = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger]

################################
# Get NOMINAL once
# Input files: only need SRwoMET
################################
Histograms = dict()
Nevents        = dict()
njetFlag       = njet+'_' if njet != '' else ''
muflag         = mu+'_' if mu != '' else ''

for Key,FileName in Files.iteritems():
  if Debug: print('DEBUG: Reading met histograms for Key,FileName = {},{}'.format(Key,FileName))
  # Open file
  File = TFile.Open(PATH+FileName)
  if not File:
    print PATH+FileName+" not found, exiting"
    sys.exit(0)  
  TH1.AddDirectory(0)
  # Get met histograms
  # first construct the key
  SelInKey = Key.split('_')[2]  #get selection from key
  if 'Signal' in Key: Sample = "MC_Signal_"
  else:               Sample = 'MC_'+Key.split(SelInKey)[0].split('_')[1]+'_'
  key = Sample+SelInKey+'_'+njetFlag+muflag+HistName
  # if case is not Inclusive, sum corresponding histograms
  if 'a' in njet:
    if   njet == 'a0jet': cases = ['e0jet','e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
    elif njet == 'a1jet': cases = ['e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
    elif njet == 'a2jet': cases = ['e2jet','e3jet','e4jet','e5jet','gt5jet']
    for case in cases:
      caseFlag = case+'_' if case != '' else ''
      histname = caseFlag+muflag+HistName
      hist     = File.Get(histname)
      if not hist:
        print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
        sys.exit(0)
      if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
      elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
      elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
      if key not in Histograms: Histograms[key] = hist.Clone(key)
      else:                     Histograms[key].Add(hist)
  else: # inclusive case
    histname = njetFlag+muflag+HistName
    hist     = File.Get(histname)
    if not hist:
      print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
      sys.exit(0)
    if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
    elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
    elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
    if key not in Histograms: Histograms[key] = hist.Clone(key)
    else:                     Histograms[key].Add(hist)
  File.Close()
  print "DEBUG: Retrieved histogram for key "+key


# Output file with variation differences for each bin 
SystVarFile      = 'VariationOutputs/VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt'
SystVarFile_symm = 'VariationOutputs/Symmetrized_VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt'



# Loop over EACH SYSTEMATIC
for syst in Systematics:
  syst_short = syst # preserve short syst name
  print("************************")
  print("SYST_SHORT = "+syst_short)
  # process EACH pair separately and keep results in list
  vardiff_1    = [] # to hold 'down' or 'parallel' variation
  vardiff_2    = [] # to hold 'up' or 'perpendicular' variation
  vardiff_symm = [] # to hold the 'symmetrized' variation
  for ipair in range(1,3):    
    print("************************")
    print("ipair = "+str(ipair))
    if syst == "MET_SoftTrk" and ipair == 1: sigma = "_ResoPara"
    elif syst == "MET_SoftTrk" and ipair == 2: sigma = "_ResoPerp"
    elif syst != "MET SoftTrk" and ipair == 1: sigma = "_down"
    elif syst != "MET_SoftTrk" and ipair == 2: sigma = "_up" 
    syst_sigma = syst+sigma 
    print ("SYSTEMATIC VARIATION = "+syst_sigma)
    Files_systs = dict()
    Campaigns_systs  = []
    for dataset in Datasets:
      if   dataset == "15" and "a" not in Campaigns_systs: Campaigns_systs.append("a")
      elif dataset == "16" and "a" not in Campaigns_systs: Campaigns_systs.append("a")
      elif dataset == "17" and "d" not in Campaigns_systs: Campaigns_systs.append("d")
      elif dataset == "18" and "e" not in Campaigns_systs: Campaigns_systs.append("e")
    for campaign in Campaigns_systs:
      Files_systs["MC16"+campaign+"_Signal_SRwoMET_"+syst_sigma] = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger+"_"+syst_sigma]
      for bkg in Backgrounds:
        Files_systs["MC16"+campaign+"_"+bkg+"_SRwoMET_"+syst_sigma] = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger+"_"+syst_sigma]
    # consutruct keys with syst name appended
    for Key,FileName in Files_systs.iteritems():
      if Debug: print("FileName = "+FileName)
      if Debug: print('DEBUG: Reading met histograms for Key,FileName = {},{}'.format(Key,FileName))
      # Open file
      File = TFile.Open(PATH+FileName)
      if not File:
        print PATH+FileName+" not found, exiting"
        sys.exit(0)  
      TH1.AddDirectory(0)
      # Get met histograms
      # first construct the key
      SelInKey = Key.split('_')[2]  #get selection from key
      if 'Signal' in Key: Sample = "MC_Signal_"
      else:               Sample = 'MC_'+Key.split(SelInKey)[0].split('_')[1]+'_'
      key = Sample+SelInKey+'_'+njetFlag+muflag+HistName+'_'+syst_sigma
      # if case is not Inclusive, sum corresponding histograms
      if 'a' in njet:
        if   njet == 'a0jet': cases = ['e0jet','e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
        elif njet == 'a1jet': cases = ['e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
        elif njet == 'a2jet': cases = ['e2jet','e3jet','e4jet','e5jet','gt5jet']
        for case in cases:
          caseFlag = case+'_' if case != '' else ''
          histname = caseFlag+muflag+HistName
          hist     = File.Get(histname)
          if not hist:
            print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
            sys.exit(0)
          if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
          elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
          elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
          if key not in Histograms: Histograms[key] = hist.Clone(key)
          else:                     Histograms[key].Add(hist)
      else: # inclusive case
        histname = njetFlag+muflag+HistName
        hist     = File.Get(histname)
        if not hist:
          print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
          sys.exit(0)
        if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
        elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
        elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
        if key not in Histograms: Histograms[key] = hist.Clone(key)
        else:                     Histograms[key].Add(hist)
      File.Close()
      print "DEBUG: Retrieved histogram for key "+key


    ######################################################
    # Make True Templates from nominal and syst variation
    # Calculate difference: delta = nominal - variation 
    ######################################################
    njetFlag = njet+'_' if njet != '' else ''
    muflag   = mu+'_'   if mu   != '' else ''
    mets     = njetFlag+muflag+HistName
    if Debug:
      print('DEBUG: njetFlag = '+njetFlag)
      print('DEBUG: muflag   = '+muflag)
      print('DEBUG: MET histogram = '+mets)

    # nominal 'True' Template from MC Sig + Ewkb
    Histograms["True_"+mets] = Histograms["MC_Signal_SRwoMET_"+mets].Clone("True")
    for bkd in Backgrounds: Histograms["True_"+mets].Add(Histograms["MC_"+bkd+"_SRwoMET_"+mets])

    # variation 'True' Template 
    Histograms["True_"+mets+"_"+syst_sigma] = Histograms["MC_Signal_SRwoMET_"+mets+"_"+syst_sigma].Clone("True_"+syst_sigma)
    for bkd in Backgrounds: Histograms["True_"+mets+"_"+syst_sigma].Add(Histograms["MC_"+bkd+"_SRwoMET_"+mets+"_"+syst_sigma])


    # calculate delta = nominal - variation
    delta = Histograms["True_"+mets].Clone("delta")
    nominal  = Histograms["True_"+mets].Clone("nominal")
    variation = Histograms["True_"+mets+"_"+syst_sigma].Clone("variation")
    # delta = nominal - systVariation
    delta.Add(variation, -1.0)
  
    for ibin in range(1, nominal.GetNbinsX()+1):
      n = nominal.GetBinContent(ibin)
      v = variation.GetBinContent(ibin)
      #print("bin = "+str(ibin)+", nominal = "+str(n)+", variation = "+str(v))

    # get down (parallel) variation difference        
    if "ResoPara" in syst_sigma or "down" in syst_sigma:
      print (">>>>>>> IN RESO_PARA/DOWN")
      for ibin in range(0, delta.GetXaxis().GetNbins()):
        #if ibin == 5: break # temporary just for TESTING
        if ibin == 0: 
          diff = syst_sigma #write syst name
        else:
          diff = delta.GetBinContent(ibin)
        vardiff_1.append(diff)
      with open(SystVarFile, 'a') as outfile_1:
        writer_1 = csv.writer(outfile_1, delimiter = '\t')
        writer_1.writerow(vardiff_1)
        
    # get up (perpendicular) variation difference
    if "ResoPerp" in syst_sigma or "up" in syst_sigma:
      print (">>>>>>> IN RESO_PERP/UP")
      for ibin in range(0, delta.GetXaxis().GetNbins()):
        #if ibin == 5: break # TEMPORARY just for TESTING
        if ibin == 0: 
          diff = syst_sigma #write syst name
          ibin = "nBin"
        else:
          diff = delta.GetBinContent(ibin)
        vardiff_2.append(diff)
      with open(SystVarFile, 'a') as outfile_2:
        writer_2 = csv.writer(outfile_2, delimiter = '\t')
        writer_2.writerow(vardiff_2)

    print("PRINTING VARDIFF")
    print(vardiff_1)
    print(vardiff_2)
    print(len(vardiff_1))
    print(len(vardiff_2))

    if vardiff_1 and vardiff_2:
      vardiff_symm.append(syst_short)
      for delta_1, delta_2 in zip(vardiff_1[1:], vardiff_2[1:]):
        d1 = abs(float(delta_1))
        d2 = abs(float(delta_2))
        delta_symmetric = 0.5*(d1+d2)
        vardiff_symm.append(delta_symmetric)
      with open(SystVarFile_symm, 'a') as outfile_symm:
        writer_symm = csv.writer(outfile_symm, delimiter='\t')
        writer_symm.writerow(vardiff_symm)
      
    print("SYMDIFF")    
    print(vardiff_symm)


    #####################################################################################
    # Plotting nominal and syst-var overlayed with ratio of (nom-var)/nom on bottom panel
    #####################################################################################
    canvas = TCanvas()
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.4, 1, 1.0)
    pad1.SetTopMargin(0.08)
    pad1.SetBottomMargin(0.03)
    pad1.Draw("same")
    pad1.cd()
    pad1.SetLogy()
    Histograms["True_"+mets].GetXaxis().SetTitle("MET [GeV]")
    Histograms["True_"+mets].GetYaxis().SetTitle("Events / 5 GeV")
    Histograms["True_"+mets].GetXaxis().SetRangeUser(0, 350)
    Histograms["True_"+mets].GetXaxis().SetLabelSize(0.)
    Histograms["True_"+mets].GetXaxis().SetTitleSize(0.)
    Histograms["True_"+mets].GetYaxis().SetTitleSize(20)
    Histograms["True_"+mets].GetYaxis().SetTitleFont(43)
    Histograms["True_"+mets].GetYaxis().SetLabelFont(43)
    Histograms["True_"+mets].GetYaxis().SetLabelSize(19)
    Histograms["True_"+mets].GetYaxis().SetTitleOffset(1.3)
    max_nom = Histograms["True_"+mets].GetMaximum()
    Histograms["True_"+mets].SetMaximum(max_nom*max_nom)
    Histograms["True_"+mets].SetMinimum(1)
    Histograms["True_"+mets].Draw("same")
    Histograms["True_"+mets+"_"+syst_sigma].SetLineColor(kRed)
    Histograms["True_"+mets+"_"+syst_sigma].SetMarkerColor(kRed)
    Histograms["True_"+mets+"_"+syst_sigma].Draw("same")
    
    # show ATLAS legend                                                      
    atlas = "#scale[1.8]{#font[72]{ATLAS} #font[42]{Internal} 13 TeV, "+str(round(TotalLumi/1000,1))+" fb^{-1} }";
    ATLASBlock = ROOT.TLatex(0.35,0.80,atlas)
    ATLASBlock.SetNDC()
    ATLASBlock.Draw("same")
    if 'a1' in njetFlag: njet_text = "njet #geq 1"
    if 'e1' in njetFlag: njet_text =  "njet = 1"
    if 'e2' in njetFlag: njet_text =  "njet = 2"
    if 'e3' in njetFlag: njet_text =  "njet = 3"
    if 'e4' in njetFlag: njet_text =  "njet = 4"
    if 'e5' in njetFlag: njet_text =  "njet = 5"
    if 'gt5' in njetFlag: njet_text =  "njet #geq 5"
    # show channel                                                           
    channel = "#scale[1.8]{"
    channel += "#it{W}#rightarrow#it{e}#nu + "+njet_text+"}"
    TextBlock = ROOT.TLatex(0.25,0.70,channel)
    TextBlock.SetNDC()
    TextBlock.Draw("same")
    
    # Add histograms to THStack and draw legends                          
    Legend = ROOT.TLegend(0.4,0.43,0.92,0.7)
    Legend.SetTextFont(42)
    Legend.SetTextSize(0.08)
    Legend.AddEntry(Histograms["True_"+mets], "Nominal", "p")
    Legend.AddEntry(Histograms["True_"+mets+"_"+syst_sigma], syst_sigma, "p")
    Legend.Draw("same")
    
    canvas.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.4)
    pad2.SetTopMargin(0.12)
    pad2.SetBottomMargin(0.32)
    pad2.Draw()
    pad2.cd()
    # ratio = (nominal - variation) / nominal = delta /  nominal
    ratio = delta.Clone("ratio")
    ratio.Divide(nominal)
    ratio.GetXaxis().SetRangeUser(0, 350)
    ratio.SetMinimum(-1.6)
    ratio.SetMaximum(0.6)
    ratio.GetYaxis().SetNdivisions(8)
    ratio.Draw("same")
    ratio.GetYaxis().SetTitleSize(20)
    ratio.GetYaxis().SetTitleFont(43)
    ratio.GetYaxis().SetLabelFont(43)
    ratio.GetYaxis().SetLabelSize(19)
    ratio.GetYaxis().SetTitleOffset(1.3)
    ratio.GetYaxis().SetTitle("(nom-syst) / nom")
    ratio.GetXaxis().SetTitleSize(20)
    ratio.GetXaxis().SetTitleFont(43)
    ratio.GetXaxis().SetLabelFont(43)
    ratio.GetXaxis().SetLabelSize(19)
    ratio.GetXaxis().SetTitleOffset(3)
    ratio.GetXaxis().SetTitle("MET [GeV]")
    ratio.GetXaxis().SetNdivisions(510)
    
    canvas.Update()
    canvas.SaveAs("Plots/Variations/"+DataPeriod+"_"+njetFlag+muflag+"_"+syst_sigma+".jpg")

    del canvas

print ">>> DONE <<<"
