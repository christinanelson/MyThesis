############################################################
# AUTHOR:  Christina Nelson                                #
# DATE:    May 5 2022                                      #
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

# Plotting range [GeV]                                 
xMin = 0
xMax = 350

####################################
# Functions
####################################

def rebinHist(hist,name):
  nbins   = hist.GetNbinsX()
  newhist = TH1D(name,'',nbins,1,nbins+1)
  for ibin in range(1,nbins+1):
    newhist.SetBinContent(ibin,hist.GetBinContent(ibin))
  return newhist

# apply error for respective bin from systs in quadrature: SystsInQuadrature[]
def getChiSquared(data, model):
  chi2 = 0
  for ibin in range(1, model.GetNbinsX()+1):
    observation = data.GetBinContent(ibin)
    expectation = model.GetBinContent(ibin)
    delta = observation - expectation
    #print("obs = "+str(observation)+", exp = "+str(expectation)+", delta = "+str(delta))
    if observation < 1e-9 or expectation < 1e-9: continue
    error = 1
    if doSyst == False: error = observation 
    if doSyst == True:
      # error = sqrt(delta_a^2 + delta_b^2)
      # poisson error for observtion, ie. delta_observation^2 = observation
      syst_err = SystsInQuadrature[ibin]
      error = np.sqrt((syst_err*syst_err)+(observation)) 
    chi2 += delta*delta / error    
    #print("Chi2 = "+str(chi2)+", delta = "+str(delta)+", systErrQuad = "+str(syst_err)+", observation = "+str(observation)+", error_tot  = "+str(error))
    print("Chi2 = "+str(chi2)+", delta = "+str(delta))
  return chi2


####################################
# Read arguments
####################################
parser = argparse.ArgumentParser()
parser.add_argument('--years',           action='store',      dest="years",    default='')
parser.add_argument('--njetFlag',        action='store',      dest="njetFlag", default="Inclusive")
parser.add_argument('--muFlag',          action='store',      dest="muFlag",   default="Inclusive")
parser.add_argument('--CRdef',           action='store',      dest="CRdef",    default="CR")
parser.add_argument('--doSystematics',   action='store',      dest="doSystematics",    default="no")
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
syst = args.doSystematics

if syst == 'no':  doSyst = False
if syst == 'yes': doSyst = True

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



# if doSystematics is true, we want to sum in quadrature the symmetrized variations
SystsInQuadrature = []
SystsSymmetrized  = []
if doSyst == True:
  print ("Summing symmetrized systematics in quadrature")
  if os.path.exists('VariationOutputs/Symmetrized_VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt'):
    print('Opening file VariationOutputs/Symmetrized_VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt')
    # get number of columns
    with open('VariationOutputs/Symmetrized_VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt') as f:
      reader = csv.reader(f,delimiter='\t',skipinitialspace=True)
      first_row = next(reader)
      num_cols = len(first_row)
    # iterate through columns to sum in quadrature
    myfile = open('VariationOutputs/Symmetrized_VariationDeltas_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt', 'r')
    lines = myfile.readlines()
    for i in range(num_cols):
      if i == 0: continue
      syst = 0
      quadSum = 0
      quadSumTot = 0
      for x in lines:
        mysyst = x.split('\t')[i]
        syst = float(mysyst)
        quadSum += (syst*syst)
      quadSumTot = np.sqrt(quadSum)
      SystsInQuadrature.append(quadSumTot)
    print("SYSTS IN QUADRATURE")
    print(SystsInQuadrature)
      

# Output file with estimated number of multijet events for inclusive/W+=1jet/W+=2jet, etc
TextFile = open('FitterOutputs_CB/'+CR+'/EstimatedNumberOfMultijetEvents_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt','w')

# Type of selections
Selections = ['CR','SRwoMET']

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


################################################
# Calculate total luminosity                             
################################################
TotalLumi = 0
for key,lumi in Luminosity.iteritems():
  TotalLumi += lumi


njetFlag = njet+'_' if njet != '' else ''
muflag   = mu+'_'   if mu   != '' else ''
mets     = njetFlag+muflag+HistName


################################################
# Make a Histogram with QuadSummed Syst Errro
# This is for plotting error band in ratio panel                     
################################################
if doSyst == True:
  Histograms["Systematics"] = Histograms["Data_SRwoMET_"+mets].Clone("Systematics")
  Histograms["Systematics"].Reset()
  for ibin in range(1, Histograms["Systematics"].GetNbinsX()):
    syst_binContent = SystsInQuadrature[ibin-1]
    Histograms["Systematics"].SetBinContent(ibin, syst_binContent)




################################################
# Fraction Fitter
################################################
if Debug:
  print('DEBUG: njetFlag = '+njetFlag)
  print('DEBUG: muflag   = '+muflag)
  print('DEBUG: MET histogram = '+mets)

# make 'True' Template from MC Sig + Ewkb
Histograms["True_"+mets] = Histograms["MC_Signal_SRwoMET_"+mets].Clone("True")
for bkd in Backgrounds: Histograms["True_"+mets].Add(Histograms["MC_"+bkd+"_SRwoMET_"+mets])


if doSyst == True:
  for ibin in range(1, Histograms["True_"+mets].GetNbinsX()):
    error_check = Histograms["True_"+mets].GetBinError(ibin)
    print("Error Before = "+str(error_check))
  # set error as sqrt(syst^2 + stat^2) in true template
  for ibin in range(1, Histograms["True_"+mets].GetNbinsX()):
    syst_err = SystsInQuadrature[ibin-1] #recall this is a list, not a hist. index starts at zero.
    bin_err  = Histograms["True_"+mets].GetBinError(ibin)
    binContent_true = Histograms["True_"+mets].GetBinContent(ibin)
    stat_err = np.sqrt(binContent_true)
    quad_error = np.sqrt((syst_err*syst_err) + (stat_err*stat_err)) 
    print("ibn = "+str(ibin)+", binContent = "+str(binContent_true)+", bin_err = "+str(bin_err)+", syst_err = "+str(syst_err)+", quad_err = "+str(quad_error))
    Histograms["True_"+mets].SetBinError(ibin, quad_error)

  for ibin in range(1, Histograms["True_"+mets].GetNbinsX()):
    error_Check = Histograms["True_"+mets].GetBinError(ibin)
    print("Error After = "+str(error_Check))


# make 'Fake' Template from Data in CR
Histograms["Fake_"+mets] = Histograms["Data_CR_"+mets].Clone("Fake")





##################
# Show fit result
##################
#print "##################################################################################"
#print ">>>>>>>>>>>>>>>> FIT RESULT for MET histogram "+mets+" <<<<<<<<<<<<<<<<<"
#print "Status: "+str(int(status))
#print "njetFlag: "+njetFlag
#print "muflag: "+muflag
#print "fake fraction from fit: "+str(fake_fraction)+" +/- "+str(fake_fraction_err)
#print "fake fraction from fit: "+str(true_fraction)+" +/- "+str(true_fraction_err)
#print "sfFake: "+str(sfFake)
#print "sfTrue: "+str(sfTrue)
#print "NMJ: "+str(round(NMJ, 4))
#print "chi2: "+str(chiSquared)
#print "##################################################################################"

# Close output file with estimated number of multijet events
TextFile.close()
#del canvas

print ">>> DONE <<<"
