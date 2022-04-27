#!/usr/bin/env python

####################################################################
#                                                                  #
# Purpose: Compare distributions between data and MC (signal+bkgs) #
# Author : Christina Nelson                                        #
#                                                                  #
####################################################################

import ROOT,os,sys,resource,psutil

Channel   = "MU"

Selection = "SR"

Tagger    = "MV2c10"

Debug     = False

###########################################
## DO NOT MODIFY
###########################################

Samples  = [
  "Signal_data15",
  "Signal_data16",
  "Signal_MC",
]

from InputFiles import *
from HelperFunctions import *
from Style import *

# Protections
if "Signal_MC" not in Samples:
  print "ERROR: Signal_MC is missing in Samples, exiting"
  sys.exit(0)

# Luminosity
from Luminosities import *

# Total luminosity and needed campaigns
Luminosity         = 0
Campaigns          = []
DataPeriods        = []
DataSamples        = [] # List of data samples
MCSignalSamples    = [] # List of MC signal samples
BackgroundSamples  = dict() # List of MC Background samples for each background type
for sample in Samples:
  if "data15" in sample:
    Luminosity += Luminosity_2015
    Campaigns.append("MC16a")
    MCSignalSamples.append("Signal_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("15")
  elif "data16" in sample:
    Luminosity += Luminosity_2016
    if "MC16a" not in Campaigns:
      Campaigns.append("MC16a")
      MCSignalSamples.append("Signal_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("16")
  elif "data17" in sample:
    Luminosity += Luminosity_2017
    Campaigns.append("MC16d")
    MCSignalSamples.append("Signal_MC16d_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("17")
  elif "data18" in sample:
    Luminosity += Luminosity_2018
    Campaigns.append("MC16e")
    MCSignalSamples.append("Signal_MC16e_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("18")
for sample in Samples:
  if "Signal" not in sample:
    BackgroundSamples[sample] = []
    for campaign in Campaigns:
      BackgroundSamples[sample].append(sample+"_"+campaign+"_"+Channel+"_"+Selection+"_"+Tagger)

Campaign   = "MC16"
for campaign in Campaigns:
  if Campaign != "MC16": Campaign += "+"
  if campaign == "MC16a": Campaign += "a"
  elif campaign == "MC16d": Campaign += "d"
  elif campaign == "MC16e": Campaign += "e"
DataPeriod = "Data"
for period in DataPeriods:
  if DataPeriod != "Data": DataPeriod += "+"
  DataPeriod += period

# AtlasStyle
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
ROOT.SetAtlasStyle()

#################################################################################################
# Transfer matrices
#################################################################################################

if Debug: print "DEBUG: Plot transfer matrices"

Flavours = ['FlavA1B_','FlavA1C_']

TMs = [
  'Zmass',
  'Zpt',
  'Zpt_ZjjHF',
  'Zabsy',
  'deltaRZjHF',
  'deltaPhiZjHF',
  'deltaYZjHF',
  'deltaRjjHF',
  'deltaPhijjHF',
  'deltaYjjHF',
  'HFjet0_pt',
  'HFjet0_absy',
  'pTjjHF',
  'mjjHF',
  'pTjjHFovermjjHF',
]

from Style import *

# Loop over flavours
for flavour in Flavours:

  # Loop over TMs
  for obs in TMs:

    histname = "TM_" + flavour + obs

    # Get total number of events
    if Debug: print "DEBUG: Get "+histname+" hist"
    Hist,msg = GetTotalHist(MCSignalSamples,histname)
    if msg != 'OK':
      print msg
      print histname+" not found, exiting"
      sys.exit(0)
    Hist.Scale(Luminosity)
    
    ROOT.gStyle.SetPalette(ROOT.kRainBow)
    ROOT.gROOT.SetBatch(True)
    
    # TCanvas
    if Debug: print "DEBUG: Create TCanvas"
    Canvas  = ROOT.TCanvas()
    Canvas.SetRightMargin(0.21)
    if 'delta' not in obs and 'absy' not in obs:
      Canvas.SetLogx()
      Canvas.SetLogy()
      Hist.GetXaxis().SetMoreLogLabels()
    if obs == 'HFjet0_pt': Hist.GetXaxis().SetRangeUser(20,900)
    if obs == 'HFjet0_pt': Hist.GetYaxis().SetRangeUser(20,900)
    Hist.GetXaxis().SetTitleSize(20)
    Hist.GetXaxis().SetTitleFont(43)
    Hist.GetXaxis().SetLabelFont(43)
    Hist.GetXaxis().SetLabelSize(19)
    Hist.GetXaxis().SetTitleOffset(1.4)
    Hist.GetXaxis().SetTitle("Reco "+XaxisTitles[obs])
    Hist.GetYaxis().SetMoreLogLabels()
    Hist.GetYaxis().SetTitleSize(20)
    Hist.GetYaxis().SetTitleFont(43)
    Hist.GetYaxis().SetLabelFont(43)
    Hist.GetYaxis().SetLabelSize(19)
    Hist.GetYaxis().SetTitleOffset(1.5)
    Hist.GetYaxis().SetTitle("Truth "+XaxisTitles[obs])

    outName = "Plots/{0}_{1}_{2}_{3}.pdf".format(Channel,Selection,Tagger,"TM_"+flavour+obs+"_MCZjetOnly")
    Canvas.Print(outName+"[")

    #gStyle.SetPadTopMargin(0.1)
    #gStyle.SetPadBottomMargin(0.18)
    #gStyle.SetPadRightMargin(0.25)
    
    Hist.Draw("colz")
    
    # Save PDF
    if Debug: print "DEBUG: Save/print PDF"
    Canvas.Print(outName)
    Canvas.Print(outName+"]")

print ">>> ALL DONE <<<"
