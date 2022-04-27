##########################################################################
# AUTHOR:  Christina Nelson                                              #
#          christina.nelson@cern.ch                                      #
# PURPOSE: Make template fits to estimate the multi-jet background       #       
# DATE:    02 July 2019                                                  #
#                                                                        #
# PURPOSE:                                                               #
# 	    Estimate QCD multijet background contribution in SR          #
#                                                                        #
# PROCEDURE:                                                             #
#          Get PDFs for signal+EWbkgs and QCD multijet background        #
#          True PDF: MET hist in MC(signal+EWbkgs) in SR~                #
#          Fake PDF: MET hist in Data in CR subtracting MC signal+EWbkgs #
#          SR~: Same as SR but w/o MET cut                               #
#          Fit true+fake model to data in SR and obtain true and fake    #
#          SFs so the true+fake fit matches with the data                #
#          Use fake SF to scale true MET hist in CR                      #
##########################################################################

import os,sys,copy,argparse
sys.path.append("../xAHReader_nominal/Plotter/")
sys.path.append("../xAHReader_nominal/")

from Defs import *

# Import input files from Plotter
PATH = ""
from InputFiles import InputFiles
from Luminosities import *

# Fitting range [GeV]                                 
xMin = 0
xMax = 200

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

# Output file with estimated number of multijet events for inclusive/W+=1jet/W+=2jet, etc
TextFile = open('FitterOutputs/'+CR+'/EstimatedNumberOfMultijetEvents_'+DataPeriod+'_njet'+njet+'_mu'+mu+'.txt','w')

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

# Protection
if Nevents["Fake"] == 0:
  print('FATAL: Nevents["Fake"] == 0, exiting')
  sys.exit(0) # protection

#########################
# Get true and fake PDFs
#########################
if Debug: print('DEBUG: Create True and Fake PDFs')
if Rebin:
  x = RooRealVar("x", "MET bin", bmin, bmax+1)
  x.setBins(bmax)
else: x = RooRealVar("x", "MET [GeV]", xMin, xMax)
hFake   = RooDataHist("hFake","",RooArgList(x),Histograms["Fake_"+mets])
hTrue   = RooDataHist("hTrue","",RooArgList(x),Histograms["True_"+mets])
if not ClosureTest: hData = RooDataHist("hData","",RooArgList(x),Histograms["Data_SRwoMET_"+mets])
PDFtrue = RooHistPdf("PDFtrue","",RooArgSet(x),hTrue)
PDFfake = RooHistPdf("PDFfake","",RooArgSet(x),hFake)

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

# Compare histograms with PDFs for first fit
if Debug: print('DEBUG: Compare histograms with PDFs')
canvas1 = TCanvas()
legend = TLegend(0.6,0.3,0.9,0.5)
canvas1.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PDFs_vs_Histograms.pdf[")
x1frame = x.frame()
x1frame.SetTitle("")
hTrue.plotOn(x1frame,RooFit.Name("hTrue"),RooFit.LineColor(kGreen+2),RooFit.MarkerColor(kGreen+2))
PDFtrue.plotOn(x1frame,RooFit.Name("PDFtrue"),RooFit.LineColor(kGreen+2))
hFake.plotOn(x1frame,RooFit.Name("hFake"),RooFit.LineColor(kRed),RooFit.MarkerColor(kRed))
PDFfake.plotOn(x1frame,RooFit.Name("PDFfake"),RooFit.LineColor(kRed))
x1frame.Draw()
legend.AddEntry("hTrue","True hist","p")
legend.AddEntry("PDFtrue","True PDF","l")
legend.AddEntry("hFake","Fake hist","p")
legend.AddEntry("PDFfake","Fake PDF","l")
legend.Draw("same")
canvas1.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PDFs_vs_Histograms.pdf")
canvas1.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PDFs_vs_Histograms.pdf]")
del canvas1, x1frame, legend

###############
# Create model
###############
if Debug: print('DEBUG: Create 1st model')
nFake  = RooRealVar("nFake","nFake",Nevents["Fake"],0.,Nevents["Data_SRwoMET_"+mets])
nTrue  = RooRealVar("nTrue","nTrue",Nevents["True"],0.,Nevents["Data_SRwoMET_"+mets])
Model  = RooAddPdf("model","model",RooArgList(PDFtrue,PDFfake),RooArgList(nTrue,nFake))
Model.getVariables().Print("v")
Model.Print('t')

##########################################
# Generate data from model (if requested)
##########################################
extra = ""
if ClosureTest:
  extra = "_closureTest"
  hData = Model.generate(RooArgSet(x),Nevents["Data_SRwoMET_"+mets])

####################
# Fit model to data
####################
print('FITINFO: Fit model to data (1 of 2)')
fitResult = Model.fitTo(hData, RooFit.Extended(True), RooFit.Save(), RooFit.SumW2Error(True))

# Print INFO
print(' * * * Result from 1st fit * * * ')
print('FITINFO: pre-fit nFake = '+str(Nevents["Fake"]))
print('FITINFO: pre-fit nTrue = '+str(Nevents["True"]))
print('FITINFO: Extracted nFake = '+str(nFake.getVal()))
print('FITINFO: Extracted nTrue = '+str(nTrue.getVal()))
extracted1stNdata = nTrue.getVal()+nFake.getVal()
print('FITINFO: Extracted nData = '+str(extracted1stNdata))
print('FITINFO: Observed  nData = '+str(Histograms["Data_SRwoMET_"+mets].Integral()))
print(' * * * * * * * * * * * * * * * * ')

# Protection
if abs(extracted1stNdata - Histograms["Data_SRwoMET_"+mets].Integral()) > (0.001*extracted1stNdata):
  print 'FITERROR: extracted data does not match with observed data (1st fit)'

#############################
# Show fake+true fit to data
#############################
#canvas2 = TCanvas()
#canvas2.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitResult"+extra+".pdf[")
#x2frame = x.frame()
#x2frame.SetTitle("")
#hData.plotOn(x2frame,RooFit.Name("data"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack))
#Model.plotOn(x2frame,RooFit.Name("model"),RooFit.LineColor(kGreen+2),RooFit.LineStyle(kDashed))
#x2frame.Draw()
#canvas2.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitResult"+extra+".pdf")
#canvas2.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitResult"+extra+".pdf]")
#del canvas2

#################
# Calculate chi2
#################
#chi2 = x2frame.chiSquare("model","data")
#del x2frame

##################
# Paper-like plot
##################
if Debug: print('DEBUG: Make PreFitPaperPlot')
canvas3 = TCanvas()
canvas3.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitPaperPlot"+extra+".pdf[")
x3frame = x.frame()
x3frame.SetTitle("")
hData.plotOn(x3frame,RooFit.Name("DataPlot"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack),RooFit.LineWidth(2))
Model.plotOn(x3frame,RooFit.Name("TruePlot"),RooFit.Components("PDFtrue"),RooFit.LineColor(kGreen+2),RooFit.LineStyle(kDashed))
Model.plotOn(x3frame,RooFit.Name("FakePlot"),RooFit.Components("PDFfake"),RooFit.LineColor(kRed), RooFit.LineStyle(kDashed))
Model.plotOn(x3frame,RooFit.Name("ModelPlot"),RooFit.LineColor(kBlue))
x3frame.Draw()
Legends3 = TLegend(0.6,0.75,0.8,0.9)
Legends3.SetTextFont(42)
if ClosureTest: Legends3.AddEntry(x3frame.findObject("DataPlot"),"Pseudo-data","p")
else:           Legends3.AddEntry(x3frame.findObject("DataPlot"),"Data","p")
Legends3.AddEntry(x3frame.findObject("ModelPlot"),"Model","l")
Legends3.AddEntry(x3frame.findObject("TruePlot"),"True component","l")
Legends3.AddEntry(x3frame.findObject("FakePlot"),"Fake component","l")
Legends3.Draw("same")
canvas3.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitPaperPlot"+extra+".pdf")
canvas3.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"PreFitPaperPlot"+extra+".pdf]")
del canvas3, x3frame, Model

######################################
# Prepare new fake template histogram
######################################
# Get SF to apply to Data_CR to create final Fake template (such that scaled old fake - MCtotalCR = extracted nFake from 1st fit)

# 1) get total number of MC signal+EWbkgs events in CR
nMCtotalCR = Nevents["MC_Signal_CR_"+mets]
for bkg in Backgrounds: nMCtotalCR += Nevents["MC_"+bkg+"_CR_"+mets]

# 2) calculate SF such that scaled old fake - MCtotalCR = extracted nFake from 1st fit
SFdataCR = (nFake.getVal()+nMCtotalCR)/Nevents["Fake"]

# 3) prepare new fake template histogram scaling old fake template
Histograms["NewFake_"+mets] = Histograms["Fake_"+mets].Clone("NewFake_"+mets)
if abs(Nevents['Fake'] - Histograms["NewFake_"+mets].Integral()) > (0.001*Nevents['Fake']) : # protection
  print 'FITERROR: number of events in non-scaled new fake template do not agree with number of events from 1st fake template'
  print 'Nevents["Fake"] = '+str(Nevents['Fake'])
  print 'Histograms["NewFake_"+mets].Integral() = '+str(Histograms["NewFake_"+mets].Integral())
Histograms["NewFake_"+mets].Scale(SFdataCR)

# Print INFO
print('FITINFO: #Events in True template                                         = '+str(Nevents['True']))
print('FITINFO: #Events in 1st Fake template                                     = '+str(Nevents['Fake']))
print('FITINFO: #Events in extracted nFake (1st fit)                             = '+str(nFake.getVal()))
print('FITINFO: #Events in scaled 1st Fake template                              = '+str(Histograms["NewFake_"+mets].Integral()))
print('FITINFO: #Events in MC signal + EWbkgs in CR                              = '+str(nMCtotalCR))

# 4) subtract signal_CR and EWbkgs_CR to new fake template
Histograms["NewFake_"+mets].Add(Histograms["MC_Signal_CR_"+mets],-1)
for bkg in Backgrounds: Histograms["NewFake_"+mets].Add(Histograms["MC_"+bkg+"_CR_"+mets],-1)  
Nevents["NewFake"] = Histograms["NewFake_"+mets].Integral()
print "FITINFO: #Events in 2nd Fake template (1st template scaled and subtrated) = "+str(Nevents["NewFake"])

if Debug:
  print "DEBUG: #events MC_Signal_CR = "+str(Nevents["MC_Signal_CR_"+mets])
  for bkg in Backgrounds: print "DEBUG: #events MC_"+bkg+"_CR = "+str(Nevents["MC_"+bkg+"_CR_"+mets])

##################################
# Create new model
##################################

if Debug: print('DEBUG: Create new (final) model')
hNewFake   = RooDataHist("hNewFake","",RooArgList(x),Histograms["NewFake_"+mets])
NewPDFfake = RooHistPdf("NewPDFfake","",RooArgSet(x),hNewFake)
hNewTrue   = RooDataHist("hNewTrue","",RooArgList(x),Histograms["True_"+mets])
NewPDFtrue = RooHistPdf("NewPDFtrue","",RooArgSet(x),hNewTrue)
nNewFake   = RooRealVar("nNewFake","",Nevents["NewFake"],0.,Nevents["Data_SRwoMET_"+mets])
nNewTrue   = RooRealVar("nNewTrue","",Nevents["True"],0.,Nevents["Data_SRwoMET_"+mets])
NewModel   = RooAddPdf("newmodel","newmodel",RooArgList(NewPDFtrue,NewPDFfake),RooArgList(nNewTrue,nNewFake))

# Overlay templates with scaled histograms to show agreement between componenets and histograms (1st fit)
#canvas4 = TCanvas()
#canvas4.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_1.pdf[")
#x4frame = x.frame()
#x4frame.SetTitle("")
#Histograms["ScaledTrue_"+mets] = Histograms["True_"+mets].Clone("ScaledTrue_"+mets)
#Histograms["ScaledTrue_"+mets].Scale(nTrue.getVal()/Nevents["True"])
#hScaledTrue = RooDataHist("hScaledTrue","",RooArgList(x),Histograms["ScaledTrue_"+mets])
#hScaledFake = RooDataHist("hScaledFake","",RooArgList(x),Histograms["NewFake0_"+mets])
#x4frame.SetMaximum(5500E3)
#hData.plotOn(x4frame,RooFit.Name("DataPlot"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack),RooFit.LineWidth(2))
#Model.plotOn(x4frame,RooFit.Name("TruePlot"),RooFit.Components("PDFtrue"),RooFit.LineColor(kGreen+2),RooFit.LineStyle(kDashed))
#Model.plotOn(x4frame,RooFit.Name("FakePlot"),RooFit.Components("PDFfake"),RooFit.LineColor(kRed+2),RooFit.LineStyle(kDashed))
#Model.plotOn(x4frame,RooFit.Name("ModelPlot"),RooFit.LineColor(kBlue))
#hScaledFake.plotOn(x4frame,RooFit.Name("hScaledFake"),RooFit.LineColor(kBlue),RooFit.MarkerColor(kBlue))
#hFake.plotOn(x4frame,RooFit.Name("hFake"),RooFit.LineColor(kRed),RooFit.MarkerColor(kRed),RooFit.MarkerStyle(43))
#hScaledTrue.plotOn(x4frame,RooFit.Name("hScaledTrue"),RooFit.LineColor(kCyan),RooFit.MarkerColor(kCyan))
#hTrue.plotOn(x4frame,RooFit.Name("hTrue"),RooFit.LineColor(kGreen+2),RooFit.MarkerColor(kGreen+2),RooFit.MarkerStyle(43))
#mylegends = TLegend(0.57,0.65,0.9,0.9)
#mylegends.SetTextFont(42)
#mylegends.SetTextSize(0.03)
#mylegends.AddEntry(x4frame.findObject("DataPlot"),"Data","p")
#mylegends.AddEntry(x4frame.findObject("TruePlot"),"True component of model","l")
#mylegends.AddEntry(x4frame.findObject("FakePlot"),"Fake component of model","l")
#mylegends.AddEntry(x4frame.findObject("ModelPlot"),"Model","l")
#mylegends.AddEntry(x4frame.findObject("hScaledFake"),"Scaled Fake hist","p")
#mylegends.AddEntry(x4frame.findObject("hFake"),"Fake hist","p")
#mylegends.AddEntry(x4frame.findObject("hScaledTrue"),"Scaled True hist","p")
#mylegends.AddEntry(x4frame.findObject("hTrue"),"True hist","p")  
#x4frame.Draw("same")
#mylegends.Draw("same")
#canvas4.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_1.pdf")
#canvas4.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_1.pdf]")
#del canvas4, x4frame

# Overlay histograms Data_SRwoMET, MC_Signal_SRwoMET (True template), Data_CR (Fake template)
#Histograms["SigCR_"+mets] = Histograms["MC_Signal_CR_"+mets].Clone("SigCR_"+mets)
#for bkg in Backgrounds: Histograms["SigCR_"+mets].Add(Histograms["MC_"+bkg+"_CR_"+mets])
#hSigCR = RooDataHist("hSigCR","",RooArgList(x),Histograms["SigCR_"+mets])
#hNewScaledFake = RooDataHist("hNewScaledFake","",RooArgList(x),Histograms["NewFake_"+mets])
#canvas5 = TCanvas()
#canvas5.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalCRTemplates.pdf[")
#x5frame = x.frame()
#x5frame.SetTitle("")
#x5frame.SetMaximum(5500E3)
#hSigCR.plotOn(x5frame,RooFit.Name("hSigCR"),RooFit.LineColor(kGreen+2),RooFit.MarkerColor(kGreen+2))
#hNewScaledFake.plotOn(x5frame,RooFit.Name("hNewScaledFake"),RooFit.LineColor(kBlue),RooFit.MarkerColor(kBlue))
#hFake.plotOn(x5frame,RooFit.Name("hFake"),RooFit.LineColor(kRed),RooFit.MarkerColor(kRed),RooFit.MarkerStyle(43))
#Mylegends = TLegend(0.57,0.75,0.9,0.9)
#Mylegends.SetTextFont(42)
#Mylegends.SetTextSize(0.03)
#Mylegends.AddEntry(x5frame.findObject("hSigCR"),"Sig+EWbkg in CR","p")
#Mylegends.AddEntry(x5frame.findObject("hNewScaledFake"), "scaled Fake - (Sig+EWbkg) in CR")
#Mylegends.AddEntry(x5frame.findObject("hFake"),"Fake hist","p")
#x5frame.Draw("same")
#Mylegends.Draw("same")
#canvas5.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalCRTemplates.pdf")
#canvas5.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"totalCRTemplates.pdf]")
#del canvas5, x5frame

# Fit new model to data
print('FITINFO: Fit (new) model to data (2 of 2)')
newfitResult = NewModel.fitTo(hData, RooFit.Extended(True), RooFit.Save(), RooFit.SumW2Error(True))

# Print INFO
print(' * * * Result from 2nd fit * * * ')
print('FITINFO: pre-fit nFake = '+str(Nevents["NewFake"]))
print('FITINFO: pre-fit nTrue = '+str(Nevents["True"]))
print('FITINFO: Extracted nFake = '+str(nNewFake.getVal()))
print('FITINFO: Extracted nTrue = '+str(nNewTrue.getVal()))
extracted2ndNdata = nNewTrue.getVal()+nNewFake.getVal()
print('FITINFO: Extracted nData = '+str(extracted2ndNdata))
print('FITINFO: Observed  nData = '+str(Histograms["Data_SRwoMET_"+mets].Integral()))
print(' * * * * * * * * * * * * * * * * ')

# Protection
if abs(extracted2ndNdata - Histograms["Data_SRwoMET_"+mets].Integral()) > (0.001*extracted2ndNdata):
  print 'FITERROR: extracted data does not match with observed data (2nd fit)'

# Overlay templates with scaled histograms to show agreement between components and histograms (2nd fit)
#canvas6 = TCanvas()
#canvas6.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_2.pdf[")
#x6frame = x.frame()
#x6frame.SetTitle("")
#Histograms["NewScaledTrue_"+mets] = Histograms["True_"+mets].Clone("NewScaledTrue_"+mets)
#Histograms["NewScaledTrue_"+mets].Scale(nNewTrue.getVal()/Nevents["True"])
#hNewScaledTrue = RooDataHist("hNewScaledTrue","",RooArgList(x),Histograms["NewScaledTrue_"+mets])
#Histograms["NewScaledFake_"+mets] = Histograms["NewFake_"+mets].Clone("NewScaledFake_"+mets)
#Histograms["NewScaledFake_"+mets].Scale(nNewFake.getVal()/Nevents["NewFake"])
#hNewScaledFake = RooDataHist("hNewScaledFake","",RooArgList(x),Histograms["NewScaledFake_"+mets])
#x6frame.SetMaximum(5500E3)
#hData.plotOn(x6frame,RooFit.Name("DataPlot"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack),RooFit.LineWidth(2))
#NewModel.plotOn(x6frame,RooFit.Name("NewTruePlot"),RooFit.Components("NewPDFtrue"),RooFit.LineColor(kGreen+2),RooFit.LineStyle(kDashed))
#NewModel.plotOn(x6frame,RooFit.Name("NewFakePlot"),RooFit.Components("NewPDFfake"),RooFit.LineColor(kRed+2),RooFit.LineStyle(kDashed))
#NewModel.plotOn(x6frame,RooFit.Name("NewModelPlot"),RooFit.LineColor(kBlue))
#hNewScaledFake.plotOn(x6frame,RooFit.Name("hNewScaledFake"),RooFit.LineColor(kBlue),RooFit.MarkerColor(kBlue))
#hNewFake.plotOn(x6frame,RooFit.Name("hNewFake"),RooFit.LineColor(kRed),RooFit.MarkerColor(kRed),RooFit.MarkerStyle(43))
#hNewScaledTrue.plotOn(x6frame,RooFit.Name("hNewScaledTrue"),RooFit.LineColor(kCyan),RooFit.MarkerColor(kCyan))
#hNewTrue.plotOn(x6frame,RooFit.Name("hNewTrue"),RooFit.LineColor(kGreen+2),RooFit.MarkerColor(kGreen+2),RooFit.MarkerStyle(43))
#mylegend = TLegend(0.57,0.6,0.9,0.9)
#mylegend.SetTextFont(42)
#mylegend.SetTextSize(0.03)
#mylegend.AddEntry(x6frame.findObject("DataPlot"),"Data","p")
#mylegend.AddEntry(x6frame.findObject("NewTruePlot"),"New True component of model","l")
#mylegend.AddEntry(x6frame.findObject("NewFakePlot"),"New Fake component of model","l")
#mylegend.AddEntry(x6frame.findObject("NewModelPlot"),"New Model","l")
#mylegend.AddEntry(x6frame.findObject("hNewScaledFake"),"New Scaled Fake hist","p")
#mylegend.AddEntry(x6frame.findObject("hNewFake"),"New Fake hist","p")
#mylegend.AddEntry(x6frame.findObject("hNewScaledTrue"),"New Scaled True hist","p")
#mylegend.AddEntry(x6frame.findObject("hNewTrue"),"New True hist","p")
#x6frame.Draw("same")
#mylegend.Draw("same")
#canvas6.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_2.pdf")
#canvas6.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"ModelTemplates_ScaledHists_2.pdf]")
#del canvas6, x6frame

#############################
# Show fake+true fit to data
#############################
#canvas7 = TCanvas()
#canvas7.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitResult"+extra+".pdf[")
#x7frame = x.frame()
#x7frame.SetTitle("")
#hData.plotOn(x7frame,RooFit.Name("data"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack))
#NewModel.plotOn(x7frame,RooFit.Name("newmodel"),RooFit.LineColor(kBlue))
#x7frame.Draw()
#canvas7.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitResult"+extra+".pdf")
#canvas7.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitResult"+extra+".pdf]")
#del canvas7

#################
# Calculate chi2
#################
#chi2 = x7frame.chiSquare("newmodel","data")
#del x7frame

# Paper-like plot
if Debug: print('DEBUG: Make FitPaperPlot')
canvas8 = TCanvas()
canvas8.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitPaperPlot"+extra+".pdf[")
x8frame = x.frame()
x8frame.SetMaximum(1)
x8frame.SetTitle("")
hData.plotOn(x8frame,RooFit.Name("DataPlot"),RooFit.LineColor(kBlack),RooFit.MarkerColor(kBlack),RooFit.LineWidth(2))
NewModel.plotOn(x8frame,RooFit.Name("NewTruePlot"),RooFit.Components("NewPDFtrue"),RooFit.LineColor(kGreen+2),RooFit.LineStyle(kDashed))
NewModel.plotOn(x8frame,RooFit.Name("NewFakePlot"),RooFit.Components("NewPDFfake"),RooFit.LineColor(kRed), RooFit.LineStyle(kDashed))
NewModel.plotOn(x8frame,RooFit.Name("NewModelPlot"),RooFit.LineColor(kBlue))
x8frame.Draw()
Legends8 = TLegend(0.6,0.75,0.8,0.9)
Legends8.SetTextFont(42)
Legends8.SetTextFont(42)
if ClosureTest: Legends8.AddEntry(x8frame.findObject("DataPlot"),"Pseudo-data","p")
else:           Legends8.AddEntry(x8frame.findObject("DataPlot"),"Data","p")
Legends8.AddEntry(x8frame.findObject("NewModelPlot"),"Model","l")
Legends8.AddEntry(x8frame.findObject("NewTruePlot"),"True component","l")
Legends8.AddEntry(x8frame.findObject("NewFakePlot"),"Fake component","l")
Legends8.Draw("same")
canvas8.Modified()
canvas8.Update()
canvas8.cd(0)
canvas8.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitPaperPlot"+extra+".pdf")
canvas8.Print("Plots/"+CR+"/"+DataPeriod+"_"+njetFlag+muflag+"FitPaperPlot"+extra+".pdf]")
del canvas8, x8frame

######################################################################
# Get final multijet estimation in SRwoMET and SR
######################################################################
Histograms["MJ_"+mets] = Histograms["Data_CR_"+mets].Clone("MJ_"+mets)

# Number of events after scaling Data in CR by 8TeVlike SF
Histograms["MJ_"+mets].Scale((nNewFake.getVal()+nMCtotalCR)/Nevents["Fake"])
Nmj = Histograms["MJ_"+mets].Integral()
print "FITINFO: #Events in new fake template (before subtraction) scaled by 2nd SF = "+str(Nmj)

# Number of events after subtracting MC EWbkgs in CR
for bkg in Backgrounds: Histograms["MJ_"+mets].Add(Histograms["MC_"+bkg+"_CR_"+mets],-1)
# Set to zero first negative bin and all of the ones above that one
FirstNegativeBin = -1
for ibin in range(1,Histograms["MJ_"+mets].GetNbinsX()+1): # Loop over bins
  if Histograms["MJ_"+mets].GetBinContent(ibin) < 0:
    print('FITWARNING: Negative bin (after subtracting bkgs): '+str(ibin)+' (MET = '+str(Histograms["MJ_"+mets].GetBinCenter(ibin))+')')
    Histograms["MJ_"+mets].SetBinContent(ibin,0)
    FirstNegativeBin = ibin
    break
if FirstNegativeBin != -1:
  for ibin in range(FirstNegativeBin+1,Histograms["MJ_"+mets].GetNbinsX()+1): # Loop over bins
    Histograms["MJ_"+mets].SetBinContent(ibin,0)

# Number of events after subtration of MC signal
Histograms["MJ_"+mets].Add(Histograms["MC_Signal_CR_"+mets],-1)
Nmj = Histograms["MJ_"+mets].Integral()
# Set to zero first negative bin and all of the ones above that one
FirstNegativeBin = -1
for ibin in range(1,Histograms["MJ_"+mets].GetNbinsX()+1):
  if Histograms["MJ_"+mets].GetBinContent(ibin) < 0:
    print('FITWARNING: Negative bin (after subtracting bkgs+signal): '+str(ibin)+' (MET = '+str(Histograms["MJ_"+mets].GetBinCenter(ibin))+')')
    Histograms["MJ_"+mets].SetBinContent(ibin,0)
    FirstNegativeBin = ibin
    break
if FirstNegativeBin != -1:
  for ibin in range(FirstNegativeBin+1,Histograms["MJ_"+mets].GetNbinsX()+1): # Loop over bins
    Histograms["MJ_"+mets].SetBinContent(ibin,0)

# Show estimated number of multijet events in SRwoMET
print "FITINFO: # MJ Events (data_CRxSF - MC_bkgs_CR - MC_Signal_CR) in SRwoMET = "+str(Nmj)

# Protection
if abs(nNewFake.getVal() - Nmj) > (0.001*Nmj):
  print('FITERROR: Number of MJ events in SRwoMET does not match with extracted fake events in SRwoMET')
  print('nNewFake.getVal()    = '+str(nNewFake.getVal()))
  print('MJ events in SRwoMET = '+str(Nmj))

# Get estimated # of MJ events in SR
if Rebin: Histograms["MJ_"+mets].GetXaxis().SetRange(bminMET,bmaxMET)
else:
  axis = Histograms["MJ_"+mets].GetXaxis()
  bmin = axis.FindBin(minMET)
  bmax = Histograms["MJ_"+mets].GetNbinsX()
  Histograms["MJ_"+mets].GetXaxis().SetRange(bmin,bmax)
Nmj  = Histograms["MJ_"+mets].Integral() # This is the estimated number of multijet events in SR
print "FITINFO: # MJ Events (data_CRxSF - MC_bkgs_CR - MC_Signal_CR) in SR = "+str(Nmj)

# Save number of estimated multijet events in SR
if muflag == '' and not ClosureTest:
  if njetFlag == '':
    TextFile.write('Inclusive '+str(Nmj)+'\n')
  else:
    TextFile.write(njetFlag.replace('_','')+' '+str(Nmj)+'\n')

##################
# Show fit result
##################
print "##################################################################################"
print ">>>>>>>>>>>>>>>> FIT RESULT for MET histogram "+mets+" <<<<<<<<<<<<<<<<<"
print "Status: "+str(newfitResult.status())
print "njetFlag: "+njetFlag
print "muflag: "+muflag
print "sfFake: "+str(nNewFake.getVal()/Nevents["NewFake"])
print "sfFakeError: "+str(nNewFake.getError()/Nevents["NewFake"])
print "sfFake(8TeVlike): "+str((nNewFake.getVal()+nMCtotalCR)/Nevents["Fake"])
print "nFake extracted: "+str(nNewFake.getVal())
print "nFake original: "+str(Nevents["True"])
print "sfTrue: "+str(nNewTrue.getVal()/Nevents["True"])
print "sfTrueError: "+str(nNewTrue.getError()/Nevents["True"])
print "nTrue: "+str(nNewTrue.getVal())
print "nExtracted: "+str(nNewTrue.getVal()+nNewFake.getVal())
print "nData: "+str(Nevents["Data_SRwoMET_"+mets])
if Rebin: print "Observed  #Events data_SR: "+str(Histograms["Data_SRwoMET_"+mets].Integral(bminMET,bmaxMET))
else:     print "Observed  #Events data_SR: "+str(Histograms["Data_SRwoMET_"+mets].Integral(bmin,bmax))
print "Estimated #Events MJ_SR: "+str(Nmj)
if Rebin: print "f_{MJ,SR} (%): "+str(100*(Nmj/Histograms["Data_SRwoMET_"+mets].Integral(bminMET,bmaxMET)))
else:     print "f_{MJ,SR} (%): "+str(100*(Nmj/Histograms["Data_SRwoMET_"+mets].Integral(bmin,bmax)))
#print "chi2: "+str(chi2)
print "##################################################################################"

# Close output file with estimated number of multijet events
TextFile.close()
del NewModel

print ">>> DONE <<<"

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
# Input distributions
#hFakeDist = TH1D("hFakeDist","",300,0,300) # MET distribution in Data in CR (signal+EWbkgs contribution should be substracted TODO)
#hFakeDist.Sumw2()
#hTrueDist = TH1D("hTrueDist","",300,0,300) # MET distribution in MC(signal+EWbkgs) in SRwoMET
#hTrueDist.Sumw2()
## Fill fake/true MET distributions
#for i in range(0,10000):
#  FakeRandom = gRandom.Gaus(20,5)
#  hFakeDist.Fill(FakeRandom)
#  TrueRandom = gRandom.Gaus(10,5)
#  hTrueDist.Fill(TrueRandom)
## Normalize distributions
#hFakeDist.Scale(1./hFakeDist.Integral())
#hTrueDist.Scale(1./hTrueDist.Integral())
#print "hFakeDist.Integral(): "+str(hFakeDist.Integral())
#print "hTrueDist.Integral(): "+str(hTrueDist.Integral())
#RooAddPdf model("model","model",RooArgList(PdfTrue,PdfFake),fTrue)
#RooFitResult* res = model.fitTo(hData, Save());
#SRwoMETdata = Histograms["Data_CR"].Clone("SRwoMETdata")
#SRwoMETdata.Add(Histograms["MC_Signal"])
#hData  = RooDataHist("hData","",RooArgList(x),SRwoMETdata)
#fitResult.floatParsFinal().Print("s")
