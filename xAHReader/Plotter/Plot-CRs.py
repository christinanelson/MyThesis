############################################
# Author: Christina Nelson                 #
############################################

import os,sys,copy,argparse
#sys.path.append("../xAHReader/Plotter/")
#sys.path.append("../xAHReader/")

from Defs import *

# Import input files from Plotter
PATH = ""
from InputFiles import InputFiles
from Luminosities import *

###########################################################################################
# Functions
###########################################################################################

def rebinHist(hist,name):
  nbins   = hist.GetNbinsX()
  newhist = TH1D(name,'',nbins,1,nbins+1)
  for ibin in range(1,nbins+1):
    newhist.SetBinContent(ibin,hist.GetBinContent(ibin))
  return newhist

###########################################################################################
# Read arguments
###########################################################################################
parser = argparse.ArgumentParser()
parser.add_argument('--years',           action='store',      dest="years",    default='')
parser.add_argument('--njetFlag',        action='store',      dest="njetFlag", default="Inclusive")
parser.add_argument('--muFlag',          action='store',      dest="muFlag",   default="Inclusive")
parser.add_argument('--CRdef',           action='store',      dest="CRdef",    default="CR")
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
CR   = args.CRdef

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
  Files["Data"+dataset+"_CR"]      = InputFiles["Signal_data"+dataset+"_"+Channel+"_"+CR+"_"+Tagger]
  Files["Data"+dataset+"_SRwoMET"] = InputFiles["Signal_data"+dataset+"_"+Channel+"_SRwoMET_"+Tagger]
  if dataset == "15" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "16" and "a" not in Campaigns: Campaigns.append("a")
  elif dataset == "17" and "d" not in Campaigns: Campaigns.append("d")
  elif dataset == "18" and "e" not in Campaigns: Campaigns.append("e")
for campaign in Campaigns:
  Files["MC16"+campaign+"_Signal_CR"]      = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_"+CR+"_"+Tagger]
  Files["MC16"+campaign+"_Signal_SRwoMET"] = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger]
  for bkg in Backgrounds:
    Files["MC16"+campaign+"_"+bkg+"_CR"]      = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_"+CR+"_"+Tagger]
    Files["MC16"+campaign+"_"+bkg+"_SRwoMET"] = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_SRwoMET_"+Tagger]


# Type of selections
Selections = ['CR','SRwoMET']

# Import lists from Arrays                                                                                                          
from Arrays import nJetmultiplicities, muFlags

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
      hist     = File.Get(histname)
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
      if Rebin:
        hist = rebinHist(hist,key)
        hist.GetXaxis().SetRange(bmin,bmax)
      else: hist.GetXaxis().SetRangeUser(xMin,xMax)
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
    if not rangeBinsFound and Rebin:
      bmin    = hist.GetXaxis().FindBin(xMin)
      bminMET = hist.GetXaxis().FindBin(minMET)
      bmax    = hist.GetXaxis().FindBin(xMax)-1
      bmaxMET = hist.GetNbinsX()
      rangeBinsFound = True
    if Rebin:
      hist = rebinHist(hist,key)
      hist.GetXaxis().SetRange(bmin,bmax)
    else: hist.GetXaxis().SetRangeUser(xMin,xMax)
    if key not in Histograms: Histograms[key] = hist.Clone(key)
    else:                     Histograms[key].Add(hist)
  Nevents[key] = Histograms[key].Integral()
  File.Close()
  if Debug: print "DEBUG: Retrieved histogram for key "+key

########################################
# Create True and Fake Histograms
########################################
if Debug: print('DEBUG: Create True and Fake template histograms')
njetFlag = njet+'_' if njet != '' else ''
muflag   = mu+'_'   if mu   != '' else ''
mets     = njetFlag+muflag+HistName
if Debug:
  print('DEBUG: njetFlag = '+njetFlag)
  print('DEBUG: muflag   = '+muflag)
  print('DEBUG: MET histogram = '+mets)


# First fake template will be only Data_CR
Histograms["Fake_"+mets] = Histograms["Data_CR_"+mets].Clone("Fake")

# True template is sum of Signal and EWbkgs in SRwoMET
Histograms["True_"+mets] = Histograms["MC_Signal_SRwoMET_"+mets].Clone("True")
for bkg in Backgrounds: Histograms["True_"+mets].Add(Histograms["MC_"+bkg+"_SRwoMET_"+mets])
# Get total number of predicted truth and fake events
Nevents["True"] = Histograms["True_"+mets].Integral()
Nevents["Fake"] = Histograms["Fake_"+mets].Integral()

# Overlay histograms Data_SRwoMET, MC_Signal_SRwoMET (True template), Data_CR (Fake template)
#if Debug: print('DEBUG: Compare data_SRwoMET with true and fake templates')
#canvas0 = TCanvas()
#canvas0.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalTemplates.pdf[")
#x0frame = x.frame()
#x0frame.SetTitle("")
#hData.plotOn(x0frame,RooFit.Name("hData"),RooFit.LineColor(kGreen),RooFit.MarkerColor(kGreen))
#hTrue.plotOn(x0frame,RooFit.Name("hTrue"),RooFit.LineColor(kBlue),RooFit.MarkerColor(kBlue))
#hFake.plotOn(x0frame,RooFit.Name("hFake"),RooFit.LineColor(kRed),RooFit.MarkerColor(kRed))
#x0frame.Draw()
#canvas0.SetLogy()
#canvas0.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalTemplates.pdf")
#canvas0.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalTemplates.pdf]")
#del canvas0, x0frame

