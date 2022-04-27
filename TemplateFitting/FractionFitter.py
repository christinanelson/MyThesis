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
TextFile = open('FitterOutputs/'+CR+'/EstimatedNumberOfMultijetEvents_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt','w')

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

# make sum of Templates into T object array for fraction fitter 
Templates = TObjArray(2)
Templates.Add(Histograms["Fake_"+mets])
Templates.Add(Histograms["True_"+mets])

Data = Histograms['Data_SRwoMET_'+mets].Clone("Data")

# use total lumi to organize how initial parameters are set
lumi_years = round(TotalLumi/1000, 1)
if lumi_years == 3.2: # Data15
  if njet == 'a1jet': 
    fake_par = 0.05
    true_par = 0.95
  if njet == 'e1jet': 
    fake_par = 0.01
    true_par = 0.99
  if njet == 'e2jet': 
    fake_par = 0.01
    true_par = 0.99
  if njet == 'e3jet': 
    fake_par = 0.05
    true_par = 0.95
  if njet == 'e4jet': 
    fake_par = 0.05
    true_par = 0.95
  if njet == 'e5jet': 
    fake_par = 0.10
    true_par = 0.95
  if njet == 'gt5jet': 
    fake_par = 0.05
    true_par = 0.95
if lumi_years == 36.2: # Data1516
  if njet == 'a1jet': 
    fake_par = 0.13
    true_par = 0.87
  if njet == 'e1jet': 
    fake_par = 0.12
    true_par = 0.879
  if njet == 'e2jet': 
    fake_par = 0.14
    true_par = 0.86
  if njet == 'e3jet': 
    fake_par = 0.16
    true_par = 0.84
  if njet == 'e4jet': 
    fake_par = 0.17
    true_par = 0.82
  if njet == 'e5jet': 
    fake_par = 0.16
    true_par = 0.83
  if njet == 'gt5jet': 
    fake_par = 0.16
    true_par = 0.84
if lumi_years == 33.0: # Data16
  if njet == 'a1jet': 
    fake_par = 0.13
    true_par = 0.86
  if njet == 'e1jet': 
    fake_par = 0.12
    true_par = 0.879
  if njet == 'e2jet': 
    fake_par = 0.13
    true_par = 0.86
  if njet == 'e3jet': 
    fake_par = 0.15
    true_par = 0.848
  if njet == 'e4jet': 
    fake_par = 0.17
    true_par = 0.82
  if njet == 'e5jet': 
    fake_par = 0.16
    true_par = 0.83
  if njet == 'gt5jet': 
    fake_par = 0.16
    true_par = 0.84
if lumi_years == 44.3: # Data17
  if njet == 'a1jet': 
    fake_par = 0.14
    true_par = 0.85
  if njet == 'e1jet': 
    fake_par = 0.13
    true_par = 0.86
  if njet == 'e2jet': 
    fake_par = 0.14
    true_par = 0.85
  if njet == 'e3jet': 
    fake_par = 0.16
    true_par = 0.83
  if njet == 'e4jet': 
    fake_par = 0.17
    true_par = 0.83
  if njet == 'e5jet': 
    fake_par = 0.18
    true_par = 0.82
  if njet == 'gt5jet': 
    fake_par = 0.17
    true_par = 0.82
if lumi_years == 58.5: # Data18
  if njet == 'a1jet': 
    fake_par = 0.20
    true_par = 0.80
  if njet == 'e1jet': 
    fake_par = 0.17
    true_par = 0.828
  if njet == 'e2jet': 
    fake_par = 0.19
    true_par = 0.80
  if njet == 'e3jet': 
    fake_par = 0.21
    true_par = 0.78
  if njet == 'e4jet': 
    fake_par = 0.21
    true_par = 0.78
  if njet == 'e5jet': 
    fake_par = 0.22
    true_par = 0.78
  if njet == 'gt5jet': 
    fake_par = 0.19
    true_par = 0.80
if lumi_years == 139.0: # Data15/16/17/18
  if njet == 'a1jet': 
    fake_par = 0.14
    true_par = 0.85
  if njet == 'e1jet': 
    fake_par = 0.1393
    true_par = 0.8607
  if njet == 'e2jet': 
    fake_par = 0.156
    true_par = 0.844
  if njet == 'e3jet': 
    fake_par = 0.18
    true_par = 0.82
  if njet == 'e4jet': 
    fake_par = 0.19
    true_par = 0.81
  if njet == 'e5jet': 
    fake_par = 0.19
    true_par = 0.80
  if njet == 'gt5jet': 
    fake_par = 0.18
    true_par = 0.81


# initialize fit on data
fit = TFractionFitter(Data, Templates)
fitter = fit.GetFitter()
fitter.Config().ParSettings(0).Set("fakeFrac", fake_par, 0.01, 0.0, 1.0) # fake fraction initialize parameter
fitter.Config().ParSettings(1).Set("trueFrac", true_par, 0.001, 0.0, 1.0) # true fraction initialize parameter
# 0.001 is the step size, aka error.

# bin 5: 20 GeV, bin Nbins max GeV
# bin 5: 20 GeV, bin 41: 200 GeV
# bin 6: 25 GeV, bin 26: 125 GeV
# bin 4: 15 GeV, bin 41: 200 GeV
# bin 4: 15 GeV, bin 21: 100 GeV
# bin 1: 0  GeV, bin 41: 200 GeV
# bin 4: 15 GeV, bin 17: 80 GeV
min_bin = 4
max_bin = 20

# Restricting Fit Range
fit.SetRangeX(min_bin, max_bin)

status = fit.Fit()
print("Status = "+str(int(status)))
print(status)

# variables or interest
sfFake = 0
sfTrue = 0
sfFake_err = 0
sfTrue_err = 0
nFake_og = 0
nTrue_og = 0
nFake_scaled = 0
nTrue_scaled = 0
fake_fraction = 0
fake_fraction_err = 0
true_fraction = 0
true_fraction_err = 0
chiSquared = 0
NMJ = 0

p0 = ROOT.Double() # fake fraction result from fit
p1 = ROOT.Double() # true fraction result from fit
p0err = ROOT.Double() # fake fraction error from fit
p1err = ROOT.Double() # true fraction error from fit

# make plots if fit has converged
if int(status) == 0:
  result = fit.GetPlot()
  fit.GetResult(0, p0, p0err)
  fit.GetResult(1, p1, p1err)
  fake_fraction = round(p0, 4)
  fake_fraction_err = round(p0err, 4)
  true_fraction = round(p1, 4)
  true_fraction_err = round(p1err, 4)
  # Top Panel: Distributions
  canvas = TCanvas()
  pad1 = ROOT.TPad("pad1", "pad1", 0, 0.4, 1, 1.0)
  pad1.SetTopMargin(0.08)
  pad1.SetBottomMargin(0.03)
  pad1.Draw("same")
  pad1.cd()
  #pad1.SetLogy()
  Histograms["Data_SRwoMET_"+mets].GetXaxis().SetTitle("MET [GeV]")
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetTitle("Events / (5)")
  dataMax = Histograms["Data_SRwoMET_"+mets].GetMaximum()
  # set max plot a bit larger than max data, for viewing with legends
  maxPlot = dataMax*dataMax
  #Histograms["Data_SRwoMET_"+mets].SetMaximum(maxPlot)
  Histograms["Data_SRwoMET_"+mets].GetXaxis().SetLabelSize(0.)
  Histograms["Data_SRwoMET_"+mets].GetXaxis().SetTitleSize(0.)
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetTitleSize(20.)
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetTitleFont(43)
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetLabelFont(43)
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetLabelSize(19)
  Histograms["Data_SRwoMET_"+mets].GetYaxis().SetTitleOffset(1.3)
  Histograms["Data_SRwoMET_"+mets].Draw("same")
  result.SetLineColor(kMagenta)
  result.Draw("same")
  # integral of fit range to get Nevents before and after scaling
  Nfake_prefit = 0
  Ntrue_prefit = 0
  for ibin in range(min_bin, max_bin):
    Nfake_prefit += Histograms["Fake_"+mets].GetBinContent(ibin)
    Ntrue_prefit += Histograms["True_"+mets].GetBinContent(ibin)
  Nfit_tot = result.Integral()
  Nfake_postfit = Nfit_tot*fake_fraction
  Ntrue_postfit = Nfit_tot*true_fraction
  # calculate fake and true scale factors, ie. amount original templates need to be scaled by for fit
  sfFake = Nfake_postfit/Nfake_prefit
  sfTrue = Ntrue_postfit/Ntrue_prefit
  
  # histogram to show scaled fake and true component of fit
  fake_scaled = Histograms["Fake_"+mets].Clone("fake_scaled")
  true_scaled = Histograms["True_"+mets].Clone("true_scaled")
  for ibin in range(0, min_bin):
    fake_scaled.SetBinContent(ibin, 0)
    true_scaled.SetBinContent(ibin, 0)
  fake_scaled.Scale(sfFake)
  fake_scaled.SetMarkerColor(kRed-9)
  fake_scaled.Draw("same ep")
  true_scaled.Scale(sfTrue)
  true_scaled.SetMarkerColor(kAzure-9)
  true_scaled.Draw("same ep")
  # original input histograms for comparison
  Histograms["Fake_"+mets].SetMarkerColor(kRed)
  Histograms["Fake_"+mets].Draw("same ep")
  Histograms["True_"+mets].SetMarkerColor(kBlue)
  Histograms["True_"+mets].SetLineColor(kBlue)
  Histograms["True_"+mets].Draw("same ep")

  # get estimated number of multijet events from scaled fake template above 25 GeV met
  NMJ = 0
  Model_SRrange = 0
  for ibin in range(0, max_bin):
    met = fake_scaled.GetBinLowEdge(ibin)
    if met>25:
      binContent_nmj = fake_scaled.GetBinContent(ibin)
      NMJ += binContent_nmj
      binContent_model = result.GetBinContent(ibin)
      Model_SRrange += binContent_model      
      print("met = "+str(met)+", binContent_nmj   = "+str(binContent_nmj))
      print("met = "+str(met)+", binContent_model = "+str(binContent_model))
  
  #print("NMJ = "+str(NMJ))
  #print("Model_SRrange = "+str(Model_SRrange))
  MJ_fraction_SR = NMJ/Model_SRrange

  # get chisqaured calculated by function above
  data_fitRegion = Histograms['Data_SRwoMET_'+mets].Clone("data_fitRegion")
  bin_iterator = min_bin
  for ibin in range(0, data_fitRegion.GetNbinsX()+1):
    if ibin < min_bin or ibin > max_bin: data_fitRegion.SetBinContent(ibin, 0)
    #data_fitRegion.SetBinContent(ibin, Histograms["Data_SRwoMET_"+mets].GetBinContent(ibin))

  for ibin in range(0, data_fitRegion.GetNbinsX()+1):
    binContent = data_fitRegion.GetBinContent(ibin)
    resultBinContent = result.GetBinContent(ibin)
    #print("bin = "+str(ibin)+", binContent = "+str(binContent)+", resultBinContent = "+str(resultBinContent))
      
  NDF = (data_fitRegion.GetNbinsX()+1)-2 # minus two for the number of templates used
  chiSquared = getChiSquared(data_fitRegion, result)/NDF
  
  # show ATLAS legend                                               
  atlas = "#scale[1.6]{#font[72]{ATLAS} #font[42]{Internal} 13 TeV, "+str(round(TotalLumi/1000,1))+" fb^{-1} }";
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
  channel = "#scale[1.6]{"
  channel += "#it{W}#rightarrow#it{e}#nu + "+njet_text+"}"
  TextBlock = ROOT.TLatex(0.25,0.7,channel)
  TextBlock.SetNDC()
  TextBlock.Draw("same")

  # show values of interest
  show_chi2 = "#scale[1.6]{#chi^{2} = "+str(round(chiSquared, 4))+"}"
  chiBlock = ROOT.TLatex(0.65, 0.7, show_chi2)
  chiBlock.SetNDC()
  chiBlock.Draw("same")
  show_fakeFrac = "#scale[1.6]{FakeFrac = "+str(fake_fraction)+" #pm "+str(fake_fraction_err)+"}"
  show_trueFrac = "#scale[1.6]{TrueFrac = "+str(true_fraction)+" #pm "+str(true_fraction_err)+"}"
  show_fakeSF   = "#scale[1.6]{SF_{fake} = "+str(round(sfFake, 4))+", }"
  show_trueSF   = "#scale[1.6]{SF_{true} = "+str(round(sfTrue, 4))+"}"
  show_NMJ      = "#scale[1.6]{N_{MJ} = "+str(round(NMJ, 4))+"}"
  min_met       = (min_bin-1)*5 # GeV
  max_met       = (max_bin)*5 # GeV 
  fitRange      = "#scale[1.6]{Fit Range: ("+str(min_met)+", "+str(max_met)+") GeV}"
  MJfraction    = "#scale[1.6]{MJ Fraction in SR: "+str(round(MJ_fraction_SR, 4))+"}"
  ffBlock = ROOT.TLatex(0.35, 0.62, show_fakeFrac)
  ffBlock.SetNDC()
  ffBlock.Draw("same")        
  tfBlock = ROOT.TLatex(0.35, 0.54, show_trueFrac)
  tfBlock.SetNDC()
  tfBlock.Draw("same")
  fSFBlock = ROOT.TLatex(0.35, 0.46, show_fakeSF)
  fSFBlock.SetNDC()
  fSFBlock.Draw("same")
  tSFBlock = ROOT.TLatex(0.65, 0.46, show_trueSF)
  tSFBlock.SetNDC()
  tSFBlock.Draw("same")         
  nmjBlock = ROOT.TLatex(0.6, 0.22, show_NMJ)
  nmjBlock.SetNDC()
  nmjBlock.Draw("same")
  MJfracBlock = ROOT.TLatex(0.5, 0.3, MJfraction)
  MJfracBlock.SetNDC()
  MJfracBlock.Draw("same")
  FRBlock = ROOT.TLatex(0.5, 0.38, fitRange)
  FRBlock.SetNDC()
  FRBlock.Draw("same")

  # Bottom Panel: show ratio of Fit/Data and if doSysts, show syst and stat error bands
  canvas.cd()
  pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.4)
  pad2.SetTopMargin(0.12)
  pad2.SetBottomMargin(0.32)
  pad2.Draw()
  pad2.cd()
  ratio = result.Clone("ratio")
  ratio.Divide(Histograms["Data_SRwoMET_"+mets])
  ratio.GetXaxis().SetRangeUser(xMin, xMax)
  if doSyst == True:
    ratio.SetMinimum(0.0)
    ratio.SetMaximum(2) 
  if doSyst == False:
    ratio.SetMinimum(0.8) 
    ratio.SetMaximum(1.2)
    
  ratio.GetYaxis().SetNdivisions(5)
  ratio.Draw("same")
  ratio.GetYaxis().SetTitleSize(20)
  ratio.GetYaxis().SetTitleFont(43)
  ratio.GetYaxis().SetLabelFont(43)
  ratio.GetYaxis().SetLabelSize(19)
  ratio.GetYaxis().SetTitleOffset(1.3)
  ratio.GetYaxis().SetTitle("Fit / Data")
  ratio.GetXaxis().SetTitleSize(20)
  ratio.GetXaxis().SetTitleFont(43)
  ratio.GetXaxis().SetLabelFont(43)
  ratio.GetXaxis().SetLabelSize(19)
  ratio.GetXaxis().SetTitleOffset(3)
  ratio.GetXaxis().SetTitle("MET [GeV]")
  ratio.GetXaxis().SetNdivisions(510)

  if doSyst == True:
    systErrBand = result.Clone("systErrBand")
    systErrBand.Reset()
    systErrBand.SetFillColor(ROOT.kGray+1)
    systErrBand.SetFillStyle(3356)
    systErrBand.SetMarkerStyle(1)
    systErrBand.SetMarkerColorAlpha(ROOT.kBlack, 1.0)
    for ibin in range(1, systErrBand.GetNbinsX()):
      systErrBand.SetBinContent(ibin, 1.0)
      syst_error = SystsInQuadrature[ibin-1]
      nom_binContent = Histograms["True_"+mets].GetBinContent(ibin)
      relative_error = (syst_error / nom_binContent)/2
      print("ibin = "+str(ibin)+", syst_error = "+str(syst_error)+", nominal = "+str(nom_binContent)+", relative_error = "+str(relative_error))
      systErrBand.SetBinError(ibin, relative_error)
    systErrBand.Draw("e3 same")

  canvas.Update()
  # save our beautiful plot <3
  canvas.SaveAs("Plots/"+CR+"/FractionFitter_"+DataPeriod+"_"+njetFlag+muflag+".jpg")


# Save number of estimated multijet events in SR
if muflag == '' and not ClosureTest:
  if njetFlag == '':
    TextFile.write('Inclusive '+str(NMJ)+'\n')
  else:
    TextFile.write(njetFlag.replace('_','')+' '+str(NMJ)+'\n')


##################
# Show fit result
##################
print "##################################################################################"
print ">>>>>>>>>>>>>>>> FIT RESULT for MET histogram "+mets+" <<<<<<<<<<<<<<<<<"
print "Status: "+str(int(status))
print "njetFlag: "+njetFlag
print "muflag: "+muflag
print "fake fraction from fit: "+str(fake_fraction)+" +/- "+str(fake_fraction_err)
print "fake fraction from fit: "+str(true_fraction)+" +/- "+str(true_fraction_err)
print "sfFake: "+str(sfFake)
print "sfTrue: "+str(sfTrue)
print "NMJ: "+str(round(NMJ, 4))
print "chi2: "+str(chiSquared)
print "##################################################################################"

# Close output file with estimated number of multijet events
TextFile.close()
if int(status) == 0: del canvas

print ">>> DONE <<<"
