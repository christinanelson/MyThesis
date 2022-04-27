############################################################
# AUTHOR:  Christina Nelson                                #
# DATE:    April 4 2022                                    #
############################################################

import os,sys,copy,argparse,os.path,csv,psutil
sys.path.append("../xAHReader/Plotter/")
sys.path.append("../xAHReader/")
from os import path
import numpy as np
from Defs import *

# Import input files from Plotter
PATH = ""
from InputFiles import InputFiles
from Luminosities import *


####################################
# Read arguments
####################################
parser = argparse.ArgumentParser()
parser.add_argument('--years',           action='store',      dest="years",    default='')
parser.add_argument('--njetFlag',        action='store',      dest="njetFlag", default="Inclusive")
parser.add_argument('--muFlag',          action='store',      dest="muFlag",   default="Inclusive")
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

if njet == 'Inclusive': njet = ''
if mu   == 'Inclusive': mu   = ''

print('FITINFO: Running on the following dataset ')
print(Datasets)

Channel = "EL" # "EL" or "MU"

# Input files
Files = dict()
Campaigns  = []
DataPeriod = 'Data'
for dataset in Datasets:
  DataPeriod += dataset
  Files["Data"+dataset+"_SR"] = InputFiles["Signal_data"+dataset+"_"+Channel+"_SR_"+Tagger]
  if dataset == "15" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "16" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "17" and "d" not in Campaigns: Campaigns.append("d")
  elif dataset == "18" and "e" not in Campaigns: Campaigns.append("e")
for campaign in Campaigns:
  Files["MC16"+campaign+"_Signal_SR"]    = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_SR_"+Tagger]
  for bkg in Backgrounds:
    Files["MC16"+campaign+"_"+bkg+"_SR"] = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_SR_"+Tagger]



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

#######################
# Get input histograms
#######################
Histograms = dict()
Nevents        = dict()
njetFlag       = njet+'_' if njet != '' else ''
muflag         = mu+'_' if mu != '' else ''
rangeBinsFound = False

HistName = "njet"
for Key,FileName in Files.iteritems():
  if Debug: print('DEBUG: Reading njet histograms for Key,FileName = {},{}'.format(Key,FileName))
  # Open file
  File = TFile.Open(PATH+FileName)
  if not File:
    print PATH+FileName+" not found, exiting"
    sys.exit(0)  
  TH1.AddDirectory(0)
  # Get met histograms
  # first construct the key
  if "Data" in Key:
    SelInKey = Key.split('_')[1] # get selection from key
    Sample   = "Data_"
  else: # MC
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
      if "Data" in key: 
        hist = File.Get(HistName)
        print("Data, getting "+HistName)
      if "Data" not in key: 
        hist = File.Get(histname)
        print("MC, getting "+histname)
      if not hist:
        print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
        sys.exit(0)
      if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
      elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
      elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
      if not rangeBinsFound and Rebin:
        bmin    = hist.GetXaxis().FindBin(xMin)
	bminMET = hist.GetXaxis().FindBin(minMET)
        bmax    = hist.GetXaxis().FindBin(xMax)-1
        bmaxMET = hist.GetNbinsX()
        rangeBinsFound = True
      if key not in Histograms: Histograms[key] = hist.Clone(key)
      else:                     Histograms[key].Add(hist)
  else: # inclusive case
    histname = njetFlag+muflag+HistName
    if "Data" in key: 
      #hist = File.Get(HistName)
      hist = File.Get(histname)
      #print("Data, getting "+HistName)
    if "Data" not in key: 
      hist = File.Get(histname)
      #print("MC, getting "+histname)

    if not hist:
      print "FATAL: "+histname+" not found in "+PATH+FileName+", exiting"
      sys.exit(0)
    if "MC16a"   in Key: hist.Scale(Luminosity["a"]) # Scale MC16a to luminosity data15/16
    elif "MC16d" in Key: hist.Scale(Luminosity["d"]) # Scale MC16d to luminosity data17
    elif "MC16e" in Key: hist.Scale(Luminosity["e"]) # Scale MC16e to luminosity data18
    if not rangeBinsFound and Rebin:
      bmin    = hist.GetXaxis().FindBin(xMin)
      bminMET = hist.GetXaxis().FindBin(minMET)
      bmax    = hist.GetXaxis().FindBin(xMax)-1
      bmaxMET = hist.GetNbinsX()
      rangeBinsFound = True
    if key not in Histograms: Histograms[key] = hist.Clone(key)
    else:                     Histograms[key].Add(hist)
  Nevents[key] = Histograms[key].Integral()
  File.Close()
  if Debug: print "DEBUG: Retrieved histogram for key "+key


################################################
# Calculate total luminosity                             
################################################
TotalLumi = 0
for key,lumi in Luminosity.iteritems():
  TotalLumi += lumi


njetFlag = njet+'_' if njet != '' else ''
muflag   = mu+'_'   if mu   != '' else ''
mets     = njetFlag+muflag+HistName


nEntries_Data      = Histograms["Data_SR_"+mets].Integral()
nEntries_MCsig     = Histograms["MC_Signal_SR_"+mets].Integral()
nEntries_MCzee     = Histograms["MC_Zee_SR_"+mets].Integral()
nEntries_MCdiboson = Histograms["MC_Diboson_SR_"+mets].Integral()
nEntries_MCtop     = Histograms["MC_Top_SR_"+mets].Integral()

print("Data = "+str(nEntries_Data)+", MCsig = "+str(nEntries_MCsig)+", MCdiboson = "+str(nEntries_MCdiboson)+", MCtop = "+str(nEntries_MCtop)+", MCzee = "+str(nEntries_MCzee))

ratio_MCsig     = nEntries_MCsig     / nEntries_Data
ratio_MCzee     = nEntries_MCzee     / nEntries_Data
ratio_MCdiboson = nEntries_MCdiboson / nEntries_Data
ratio_MCtop     = nEntries_MCtop     / nEntries_Data

print("Ratios: MCsig/Data = "+str(ratio_MCsig)+", MCdiboson/Data = "+str(ratio_MCdiboson)+", MCtop/Data = "+str(ratio_MCtop)+", MCzee/Data = "+str(ratio_MCzee))

print ">>> DONE <<<"
