#!/usr/bin/env python

####################################################################
#                                                                  #
# Purpose: Compare distributions between data and MC (signal+bkgs) #
# Author : Christina Nelson                                        #
# christina.nelson@cern.ch                                         #
#                                                                  #
####################################################################

import ROOT,os,sys,resource,psutil,argparse
from CalculateSignificance import significance

# Read arguments
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('--histname',        action='store',      dest="histname")
parser.add_argument('--channel',         action='store',      dest="channel")
parser.add_argument('--selection',       action='store',      dest="selection")
parser.add_argument('--tagger',          action='store',      dest="tagger")
parser.add_argument('--atlas',           action='store',      dest="atlas")
parser.add_argument('--samples',         action='store',      dest="samples")
parser.add_argument('--CRdef',           action='store',      dest="CRdef",            default='CR')
parser.add_argument('--addMultijet',     action='store',      dest="addMultijet",      default='NONE')
parser.add_argument('--debug',           action='store_true', dest="debug",            default=False)
parser.add_argument('--compareshapes',   action='store_true', dest="compareShapes",    default=False)
parser.add_argument('--calcsignificance',action='store_true', dest="calcSignificance", default=False)
parser.add_argument('--makeplots',       action='store_true', dest="makePlots",        default=False)
args = parser.parse_args()
# Protections
if args.histname is None:
  print 'ERROR: no histname provided, exiting'
  sys.exit(0)
if args.channel is None:
  print 'ERROR: channel not provided, exiting'
  sys.exit(0)
if args.selection is None:
  print 'ERROR: selection not provided, exiting'
  sys.exit(0)
if args.tagger is None:
  print 'ERROR: tagger not provided, exiting'
  sys.exit(0)
if args.atlas is None:
  print 'ERROR: ATLAS legend not selected, exiting'
  sys.exit(0)
if args.samples is None:
  print 'ERROR: You have selected no sample, exiting'
  sys.exit(0)
HistName              = args.histname
Debug                 = args.debug
Channel               = args.channel
Selection             = args.selection
Tagger                = args.tagger
ATLASlegend           = args.atlas
Samples               = args.samples.split(',')
AddMultijetEstimation = args.addMultijet
CompareShapesInRatio  = args.compareShapes
CRdef                 = args.CRdef
CalcSignificance      = args.calcSignificance
make_Data_vs_MC_Plots = args.makePlots

HistNames = [HistName] # Temporary

from InputFiles import *
from HelperFunctions import *
from Style import *

# Protections
if "Signal_data15" not in Samples and "Signal_data16" not in Samples and "Signal_data17" not in Samples and "Signal_data18" not in Samples:
  print "ERROR: At least one signal_data sample needs to be provided, exiting"
  sys.exit(0)
if "Signal_MC" not in Samples:
  print "ERROR: Signal_MC is missing in Samples, exiting"
  sys.exit(0)

# Luminosity
from Luminosities import *

# Find Alterntive MC Signal samples
AlternativeMCSignals = []
for sample in Samples:
  if 'AltSig' in sample: AlternativeMCSignals.append(sample)

# Total luminosity and needed campaigns
Luminosity         = dict() # collect luminosity for each MC campaign
Luminosity["MC16a"]= 0
Luminosity["MC16d"]= 0
Luminosity["MC16e"]= 0
Campaigns          = []
DataPeriods        = []
DataSamples        = [] # List of data samples
MCSignalSamples    = [] # List of MC signal samples
MCAltSigSamples    = [] # List if Alternative MC signal samples
BackgroundSamples  = dict() # List of MC Background samples for each background type
for sample in Samples:
  if "data15" in sample:
    Luminosity["MC16a"] += Luminosity_2015
    Campaigns.append("MC16a")
    MCSignalSamples.append("Signal_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
    for altsig in AlternativeMCSignals:
      MCAltSigSamples.append(altsig+"_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("15")
  elif "data16" in sample:
    Luminosity["MC16a"] += Luminosity_2016
    if "MC16a" not in Campaigns:
      Campaigns.append("MC16a")
      MCSignalSamples.append("Signal_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
      for altsig in AlternativeMCSignals:
        MCAltSigSamples.append(altsig+"_MC16a_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("16")
  elif "data17" in sample:
    Luminosity["MC16d"] += Luminosity_2017
    Campaigns.append("MC16d")
    MCSignalSamples.append("Signal_MC16d_"+Channel+"_"+Selection+"_"+Tagger)
    for altsig in AlternativeMCSignals:
      MCAltSigSamples.append(altsig+"_MC16d_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("17")
  elif "data18" in sample:
    Luminosity["MC16e"] += Luminosity_2018
    Campaigns.append("MC16e")
    MCSignalSamples.append("Signal_MC16e_"+Channel+"_"+Selection+"_"+Tagger)
    for altsig in AlternativeMCSignals:
      MCAltSigSamples.append(altsig+"_MC16e_"+Channel+"_"+Selection+"_"+Tagger)
    DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
    DataPeriods.append("18")
for sample in Samples:
  if "Sig" not in sample:
    BackgroundSamples[sample] = []
    for campaign in Campaigns:
      BackgroundSamples[sample].append(sample+"_"+campaign+"_"+Channel+"_"+Selection+"_"+Tagger)
        
# Calculate total luminosity
TotalLumi = 0
for key,lumi in Luminosity.iteritems():
  TotalLumi += lumi

Campaign   = "MC16"
for campaign in Campaigns:
  if Campaign != "MC16": Campaign += "+"
  if campaign == "MC16a": Campaign += "a"
  elif campaign == "MC16d": Campaign += "d"
  elif campaign == "MC16e": Campaign += "e"
DataPeriod = "Data"
for period in DataPeriods:
  #if DataPeriod != "Data": DataPeriod += "+"
  DataPeriod += period

# Get multijet histograms for Data vs MC plots
MultijetHistograms = dict()
if AddMultijetEstimation == 'Inclusive' and make_Data_vs_MC_Plots:
  InputFileName = '../../TemplateFitting/FitterOutputs/'+CRdef+'/MultijetDistributions_'+DataPeriod+'.root'
  InputFile     = ROOT.TFile.Open(InputFileName)
  if not InputFile:
    print "ERROR: input with multijet estimation not found, exiting"
    sys.exit(0)
  for key in HistNames:
    if key == 'correctedAndScaledAverageMu' or key == 'jet_eta' or key == 'jet_y' or 'j2_' in key: continue # skip (no multijet estimation available)
    histname = 'Multijet_'+key
    hist     = InputFile.Get(histname)
    if not hist:
      print 'ERROR: '+histname+' not found, exiting'
      sys.exit(0)
    hist.SetDirectory(0)
    if Debug: print('DEBUG: Integral of MJ histogram for {} in {} = {}'.format(key,DataPeriod,hist.Integral()))
    # Divide by bin-width
    if Debug: print "DEBUG: divide MJ hist by bin-width"
    for binX in range(1,hist.GetNbinsX()+1):
      if hist.GetBinWidth(binX)!=0:
        hist.SetBinContent(binX, hist.GetBinContent(binX)/hist.GetBinWidth(binX))
        hist.SetBinError(binX, hist.GetBinError(binX)/hist.GetBinWidth(binX))
      else:
        hist.SetBinContent(binX, 0)
        hist.SetBinError(binX, 0)
    # Set X-axis range
    if Debug: print "DEBUG: set x-axis range for the MJ hist"
    if XaxisRange.has_key(histname):
      hist.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])
    MultijetHistograms[key] = hist
elif AddMultijetEstimation == 'Exclusive' and make_Data_vs_MC_Plots:
  InputFileName = '../../TemplateFitting/FitterOutputs/'+CRdef+'/MultijetDistributions_'+DataPeriod+'_Exclusive.root'
  InputFile     = ROOT.TFile.Open(InputFileName)
  if not InputFile:
    print "ERROR: input with multijet estimation not found, exiting"
    sys.exit(0)
  for key in HistNames:
    if key == 'correctedAndScaledAverageMu' or key == 'jet_eta' or key == 'jet_y' or 'j2_' in key: continue # skip (no multijet estimation available)
    histname = 'TotalMultijet_'+key
    hist     = InputFile.Get(histname)
    if not hist:
      print 'ERROR: '+histname+' not found, exiting'
      sys.exit(0)
    hist.SetDirectory(0)
    if Debug: print('DEBUG: Integral of MJ histogram for {} in {} = {}'.format(key,DataPeriod,hist.Integral()))
    # Divide by bin-width
    if Debug: print "DEBUG: divide MJ hist by bin-width"
    for binX in range(1,hist.GetNbinsX()+1):
      if hist.GetBinWidth(binX)!=0:
        hist.SetBinContent(binX, hist.GetBinContent(binX)/hist.GetBinWidth(binX))
        hist.SetBinError(binX, hist.GetBinError(binX)/hist.GetBinWidth(binX))
      else:
        hist.SetBinContent(binX, 0)
        hist.SetBinError(binX, 0)
    # Set X-axis range
    if Debug: print "DEBUG: set x-axis range for the MJ hist"
    if XaxisRange.has_key(histname):
      hist.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])
    MultijetHistograms[key] = hist


# AtlasStyle
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(True)

# Loop over histograms
Hist_MC_Backgrounds = dict()
for histname in HistNames:

  if "Weight" in histname: histname = Tagger+histname # pseudo-continuous b-tagging weight

  if Debug: print "###########################################################"
  if Debug: print "DEBUG: Producing PDF for '"+histname+"' histogram"
  if Debug: print "DEBUG: Memory usage = {0} (MB)".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
  if Debug: pid = os.getpid()
  if Debug: py  = psutil.Process(pid)
  if Debug: print "DEBUG: CPU[0] = {0} (%)".format(py.cpu_percent())

  ############################
  # Get Histograms
  ############################

  # Total data histogram
  if Debug: print "DEBUG: Get Data histogram"
  Hist_Data,msg = GetTotalHist(DataSamples,histname,Debug)
  if msg != 'OK':
    print msg
    print histname+" not found, exiting"
    sys.exit(0)
  if Debug: print "DEBUG: Data histogram retrieved"
  if Debug: print "DEBUG: Set line and fill color for data histogram"
  Hist_Data.SetMarkerStyle(20)
  if Debug: print('DEBUG: Integral of data histogram for {} in {} = {}'.format(histname,DataPeriod,Hist_Data.Integral()))

  # Total MC Signal histogram
  if Debug: print "DEBUG: Get MC Signal histograms"
  Hist_MC_Signal,msg = GetTotalHist(MCSignalSamples,histname,Debug,Luminosity)
  if msg != 'OK':
    print msg
    print histname+" not found, exiting"
    sys.exit(0)
  Hist_MC_Signal.SetLineColor(ROOT.kBlack)
  Hist_MC_Signal.SetMarkerStyle(1) # No marker for MC histograms

  if Debug: print('DEBUG: Integral of MC signal histogram for {} in {} = {}'.format(histname,DataPeriod,Hist_MC_Signal.Integral()))

  # Total histogram for each alternative MC Signal sample
  Hist_Alt_MC_Signals = dict() # Histogram for each alternative MC signal sample
  altcounter = 0
  if make_Data_vs_MC_Plots:
    for alt in AlternativeMCSignals: # Loop over different alternative MC signal samples
      AltSamples = [] # List of campaigns for each alternative MC signal sample
      for sample in MCAltSigSamples:
        if alt in sample: AltSamples.append(sample)
      Hist,msg = GetTotalHist(AltSamples,histname,Debug,Luminosity)
      if msg != 'OK':
        print msg
        print histname+" not found, exiting"
        sys.exit(0)
      Hist.SetLineColor(AltColors[altcounter])
      Hist.SetLineStyle(AltLines[altcounter])
      Hist.SetMarkerStyle(1)
      Hist_Alt_MC_Signals[alt] = Hist
      altcounter += 1

  # Histogram for each background sample
  if Debug: print "DEBUG: Get MC Background histograms"
  for key,value in BackgroundSamples.iteritems():
    hist,msg = GetTotalHist(value,histname,Debug,Luminosity)
    if msg != 'OK':
      print msg
      sys.exit(0)
    else: Hist_MC_Backgrounds[key] = hist
  # Set line color and scale background histograms
  counter = 0
  for key,hist in Hist_MC_Backgrounds.iteritems():
    if Debug: print('DEBUG: Integral of MC {} histogram for {} in {} = {}'.format(key,histname,DataPeriod,hist.Integral()))
    hist.SetLineColor(Colors[counter])
    hist.SetFillColor(Colors[counter])
    counter += 1

  ########################################
  # Calculate significance (if requested)
  ########################################
  if CalcSignificance: significance(histname, Hist_MC_Signal, Hist_MC_Backgrounds, Debug, DataPeriod, Channel, Selection, Tagger)
  
  #######################################
  # Make Data vs MC Plots (if requested)
  #######################################
  if not make_Data_vs_MC_Plots: continue # skip code below for making MC/data plots
  # TCanvas
  if Debug: print "DEBUG: Create TCanvas"
  Canvas  = ROOT.TCanvas()
  extra   = '_compareShapes' if CompareShapesInRatio else ''
  if AddMultijetEstimation != 'NONE': extra += '_withMultijet'+AddMultijetEstimation+CRdef
  outName = "Plots/{0}/{1}/{2}_{3}_{4}_{5}{6}.jpg".format(Selection,DataPeriod,Channel,Selection,Tagger,histname,extra)
  #Canvas.Print(outName+"[")

  # TPad for upper panel
  if Debug: print "DEBUG: Create TPad for upper panel"
  pad1 = ROOT.TPad("pad1","pad1",0,0.4,1,1.0)
  pad1.SetTopMargin(0.08)
  pad1.SetBottomMargin(0.03)
  pad1.Draw()
  pad1.cd()

  # Set log scales (if requested)
  if Debug: print "DEBUG: Set log scales if requested"
  if histname in Logx:
    pad1.SetLogx()
  if histname in Logy:
    pad1.SetLogy()
  if "Weight" in histname: pad1.SetLogy()

  # Add histograms to THStack and draw legends
  Legends = ROOT.TLegend(0.7,0.43,0.92,0.9)
  Legends.SetTextFont(42)

  Hist_Data.Draw("E P")
  Hist_Data.GetXaxis().SetLabelSize(0.)
  Hist_Data.GetXaxis().SetTitleSize(0.)
  Hist_Data.GetYaxis().SetTitleSize(20)
  Hist_Data.GetYaxis().SetTitleFont(43)
  Hist_Data.GetYaxis().SetLabelFont(43)
  Hist_Data.GetYaxis().SetLabelSize(19)
  Hist_Data.GetYaxis().SetTitleOffset(1.3)
  Hist_Data.GetYaxis().SetTitle("Events / bin-width")
  Hist_Data.SetMinimum(1)
  Legends.AddEntry(Hist_Data,"Data","p")

  # THStack for MC samples
  StackMC = ROOT.THStack()

  # THStack for altetnative MC signal samples
  StackAlt = ROOT.THStack()

  # Add MC backgrounds to StackMC
  for key,hist in Hist_MC_Backgrounds.iteritems():
    StackMC.Add(hist,"HIST][")
    if key == "Top":         legend = "Top quark"
    elif key == "Wmunu":     legend = "W(#rightarrow#mu#nu)+jets"
    elif key == "Wtaunu":    legend = "W(#rightarrow#tau#nu)+jets"
    elif key == "Ztautau":   legend = "Z(#rightarrow#tau#tau)+jets"
    elif key == "Zee":       legend = "Z(#rightarrow e e )+jets"
    else: legend = key
    Legends.AddEntry(hist,legend,"f")

  if AddMultijetEstimation != 'NONE':
    if histname in MultijetHistograms:
      MultijetHistograms[histname].SetLineColor(Colors[counter])
      MultijetHistograms[histname].SetFillColor(Colors[counter])
      StackMC.Add(MultijetHistograms[histname],"HIST][")
      Legends.AddEntry(MultijetHistograms[histname],'Multijet','f')

  StackMC.Add(Hist_MC_Signal,"HIST][")
  if Channel == "MU": Legends.AddEntry(Hist_MC_Signal,"W(#rightarrow#mu#nu)+jets Sherpa 2.2.1","f")
  else:               Legends.AddEntry(Hist_MC_Signal,"W(#rightarrow e #nu)+jets Sherpa 2.2.1","f")   # electron channel
  
  # Prepare final histogram for each alt signal sample
  FinalAltSignals = dict()
  for sample,hist in Hist_Alt_MC_Signals.iteritems(): # loop over alt samples
    # Sum backgrounds
    for key,histbkg in Hist_MC_Backgrounds.iteritems(): # loop over backgrounds
      hist.Add(histbkg)
    FinalAltSignals[sample] = hist
    StackAlt.Add(hist,"HIST][")
    legend = 'UPDATE'
    if 'MGPy8' in sample:
      if Channel == 'MU': legend = "W(#rightarrow#mu#nu)+jets MGPy8"
      else:               legend = "W(#rightarrow e #nu)+jets MGPy8"
    Legends.AddEntry(hist,legend,"l")

  if Debug: print "DEBUG: Draw THStack with MC histograms"
  StackMC.Draw("same")

  if Debug: print "DEBUG: Draw data histogram"
  Hist_Data.Draw("psame")


  if Debug: print "DEBUG: Draw THStack with alternatie MC signal histograms"
  StackAlt.Draw("same")

  
  if XaxisRange.has_key(histname):
    StackMC.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])
  maxY = Hist_Data.GetMaximum()
  if StackMC.GetMaximum() > maxY: maxY = StackMC.GetMaximum()
  maxYscaling = 1E5
  if "absy" in histname or "phi" in histname or "eta" in histname or "deltaR" in histname or "deltaPhi" in histname or "Weight" in histname: maxYscaling = 2E7
  if "Weight" in histname: maxYscaling = 1E9
  StackMC.GetYaxis().SetRangeUser(1,maxY*maxYscaling)
  Hist_Data.GetYaxis().SetRangeUser(1,maxY*maxYscaling)

  StackMC.GetXaxis().SetLabelSize(0.)
  StackMC.GetXaxis().SetTitleSize(0.)
  StackMC.GetYaxis().SetTitleSize(20)
  StackMC.GetYaxis().SetTitleFont(43)
  StackMC.GetYaxis().SetLabelFont(43)
  StackMC.GetYaxis().SetLabelSize(19)
  StackMC.GetYaxis().SetTitleOffset(1.3)
  StackMC.GetYaxis().SetTitle("Events / bin-width")

  if Debug: print "DEBUG: Draw legends"
  Legends.Draw("same")

  ROOT.gPad.RedrawAxis()

  # Show ATLAS legend
  if Debug: print "DEBUG: Show ATLAS legend"
  if   ATLASlegend == "Internal":    atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS} #font[42]{Internal}}}";
  elif ATLASlegend == "Preliminary": atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS} #font[42]{Preliminary}}}";
  elif ATLASlegend == "ATLAS":       atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS}}}";
  else:
    print "ERROR: ATLASlegend not recognized, exiting"
    sys.exit(0)
  ATLASBlock = ROOT.TLatex(0.2,0.8,atlas)
  ATLASBlock.SetNDC()
  ATLASBlock.Draw("same")

  # Show CME and luminosity
  if Debug: print "DEBUG: Show CME and luminosity"
  CME = "#scale[1.5]{13 TeV, "+str(round(TotalLumi/1000,1))+" fb^{-1}}"
  CMEblock = ROOT.TLatex(0.2,0.7,CME)
  CMEblock.SetNDC()
  CMEblock.Draw("same")

  # Show channel
  if Debug: print "DEBUG: Show channel type"
  channel = "#scale[1.5]{"
  channel += "#mu" if Channel == "MU" else "e"
  channel += " channel}"
  TextBlock = ROOT.TLatex(0.2,0.6,channel)
  TextBlock.SetNDC()
  TextBlock.Draw("same")
  
  # TPad for bottom plot
  if Debug: print "DEBUG: Create TPad for bottom panel"
  Canvas.cd()
  pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.4)
  pad2.SetTopMargin(0.03)
  pad2.SetBottomMargin(0.32)
  pad2.Draw()
  pad2.cd()

  # Set log-y scale (if requested)
  if Debug: print "DEBUG: Set log-Y scale if requested"
  if histname in Logx:
    pad2.SetLogx()

  # Create data/MC histogram
  if Debug: print "DEBUG: Create data/MC histogram"
  if not CompareShapesInRatio:
    ratioHist = Hist_MC_Signal.Clone("ratioHist")
    for key,hist in Hist_MC_Backgrounds.iteritems():
      ratioHist.Add(hist)
    if AddMultijetEstimation != 'NONE':
      if histname in MultijetHistograms:
        ratioHist.Add(MultijetHistograms[histname])
    ratioHist.Divide(Hist_Data)    
  else:
    ratioHist = Hist_MC_Signal.Clone("ratioHist")
    for key,hist in Hist_MC_Backgrounds.iteritems():
      ratioHist.Add(hist)
    if AddMultijetEstimation != 'NONE':
      if histname in MultijetHistograms:
        ratioHist.Add(MultijetHistograms[histname])
    ratioHist.Scale(1./ratioHist.Integral())
    DataNormalized = Hist_Data.Clone("NormalizedData")
    DataNormalized.Scale(1./DataNormalized.Integral())
    ratioHist.Divide(DataNormalized)

  ratioHist.SetLineColor(ROOT.kBlack)
  ratioHist.SetMarkerStyle(20)
  ratioHist.SetMarkerColor(ROOT.kBlack)

  altcounter = 0
  # Create ratios for alternative MC signal samples
  AltRatioHists = dict()
  for sample,hist in FinalAltSignals.iteritems():
    altRatio = hist.Clone(sample+"_ratio")
    altRatio.Divide(Hist_Data)
    altRatio.SetMarkerStyle(AltMarkers[altcounter])
    altRatio.SetMarkerColor(AltColors[altcounter])
    AltRatioHists[sample] = altRatio
    altcounter += 1

  # Set y-axis range of ratio panel
  minY = -0.05
  maxY = 2.05
  if "Weight" in histname:
    minY = -0.05
    maxY = 3.05
  ratioHist.SetMinimum(minY)
  ratioHist.SetMaximum(maxY)
  for sample,hist in AltRatioHists.iteritems():
    hist.SetMinimum(minY)
    hist.SetMaximum(maxY)

  # Draw data/MC ratio
  if Debug: print "DEBUG: Draw MC/data ratio"
  ratioHist.Draw("e0")
  for sample,hist in AltRatioHists.iteritems():
    hist.Draw("e0same")
  
  # Draw line at data/MC==1
  if Debug: print "DEBUG: Draw line at MC/data==1"
  nbins = ratioHist.GetNbinsX()
  if histname in XaxisRange:
    minX = XaxisRange[histname][0]
    maxX = XaxisRange[histname][1]
  else:
    minX = ratioHist.GetXaxis().GetBinLowEdge(1)
    maxX = ratioHist.GetXaxis().GetBinUpEdge(nbins)
  Line = ROOT.TLine(minX,1,maxX,1)
  Line.SetLineStyle(7)
  Line.Draw("same")

  # Set x-axis title
  if Debug: print "DEBUG: Set X-axis title"
  histkey = histname
  if histname == "lep_pt":
    histkey = "mu_pt" if Channel == "MU" else "el_pt"
  elif histname == "lep_eta":
    histkey = "mu_eta" if Channel == "MU" else "el_eta"
  elif histname == "lep_phi":
    histkey = "mu_phi" if Channel == "MU" else "el_phi"
  if XaxisTitles.has_key(histkey):
    ratioHist.GetXaxis().SetTitleSize(20)
    ratioHist.GetXaxis().SetTitleFont(43)
    ratioHist.GetXaxis().SetLabelFont(43)
    ratioHist.GetXaxis().SetLabelSize(19)
    ratioHist.GetXaxis().SetTitleOffset(3)
    ratioHist.GetXaxis().SetTitle(XaxisTitles[histkey])
    ratioHist.GetXaxis().SetNdivisions(510)

  ratioHist.GetYaxis().SetTitleSize(20)
  ratioHist.GetYaxis().SetTitleFont(43)
  ratioHist.GetYaxis().SetLabelFont(43)
  ratioHist.GetYaxis().SetLabelSize(19)
  ratioHist.GetYaxis().SetTitleOffset(1.3)
  ratioHist.GetYaxis().SetTitle("MC / Data")

  # Save PDF
  if Debug: print "DEBUG: Save/print PDF"
  Canvas.Print(outName)
  #Canvas.Print(outName+"]")

  ratioHist.Delete()
  # Clear dict
  for key,hist in Hist_MC_Backgrounds.iteritems():
    hist.Delete()
  Hist_MC_Backgrounds.clear()

print ">>> ALL DONE <<<"

#################################################################################################
# Truth and reco cutflow
#################################################################################################

#if Debug: print "DEBUG: Produce truth and reco cutflow plots"

#Types = ["reco","truth"]

#for Type in Types:

#  histname = "cutflow_" + Type

#  # Get total number of events
#  if Debug: print "DEBUG: Get "+histname+" hist"
#  Hist,msg = GetTotalHist(MCSignalSamples,histname,Debug,Luminosity)
#  if msg != 'OK':
#    print msg
#    print histname+" not found, exiting"
#    sys.exit(0)
  
#  # TCanvas
#  if Debug: print "DEBUG: Create TCanvas"
#  Canvas  = ROOT.TCanvas()
#  outName = "Plots/{0}_{1}_{2}_{3}.pdf".format(Channel,Selection,Tagger,"Cutflow_"+Type+"_MCZjetOnly")
#  Canvas.Print(outName+"[")

#  # Compute acceptance for each bin
#  nbins = Hist.GetNbinsX()
#  for ibin in range(2,nbins+1):
#    BinContent = Hist.GetBinContent(ibin)
#    if BinContent !=0: 
#      acceptance = BinContent/Hist.GetBinContent(1)
#      Hist.SetBinContent(ibin,acceptance)
#      Hist.SetBinError(ibin,0)
#  Hist.SetBinContent(1,1)
#  Hist.SetBinError(1,0)
  
#  Hist.SetLineColor(ROOT.kBlue)
#  Hist.Draw("")
  
#  Hist.GetYaxis().SetTitleSize(20)
#  Hist.GetYaxis().SetTitleFont(43)
#  Hist.GetYaxis().SetLabelFont(43)
#  Hist.GetYaxis().SetLabelSize(19)
#  Hist.GetYaxis().SetTitleOffset(1.3)
#  Hist.GetYaxis().SetTitle("Acceptance")
  
#  ROOT.gPad.RedrawAxis()
  
#  # Show channel
#  if Debug: print "DEBUG: Show channel type"
#  channel = "#mu" if Channel == "MU" else "e"
#  channel += " channel"
#  TextBlock = ROOT.TLatex(0.7,0.8,channel)
#  TextBlock.SetNDC()
#  TextBlock.Draw("same")

#  # Show final acceptance
#  if Debug: print "DEBUG: Show acceptance"
#  Str = "Acceptance ("+Type+"): "+str(round(acceptance,2))
#  TextBlock2 = ROOT.TLatex(0.55,0.85,Str)
#  TextBlock2.SetNDC()
#  TextBlock2.Draw("same")
  
#  # Save PDF
#  if Debug: print "DEBUG: Save/print PDF"
#  Canvas.Print(outName)
#  Canvas.Print(outName+"]")

