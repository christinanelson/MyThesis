#!/usr/bin/env python

###########################################################################
#                                                                         #
# Purpose: Compare MET distributions b/w different samples and selections #
# Author : Jona Bossio (jbossios@cern.ch)                                 #
#                                                                         #
###########################################################################

Comparisons = {
#  'DatavsMC_CR'         : ['Signal_data15:CR','Signal_data16:CR','Top:CR','Diboson:CR','Zee:CR','Signal:CR','Dijets:CR'],
  'DatavsMC_CR'            : ['Signal_data15:CR','Signal_data16:CR','Top:CR','Diboson:CR','Zee:CR','Signal:CR'],
  'DataCR_vs_MCSRwoMET'    : ['Signal_data15:CR','Signal_data16:CR','Top:SRwoMET','Diboson:SRwoMET','Zee:SRwoMET','Signal:SRwoMET'],
  'DataCRmed_vs_MCSRwoMET' : ['Signal_data15:CRmed','Signal_data16:CRmed','Top:SRwoMET','Diboson:SRwoMET','Zee:SRwoMET','Signal:SRwoMET'],
  'DatavsMC_CRmed'         : ['Signal_data15:CRmed','Signal_data16:CRmed','Top:CRmed','Diboson:CRmed','Zee:CRmed','Signal:CRmed'],
}

Channel     = 'EL'
Tagger      = 'MV2c10'
Debug       = False
ATLASlegend = "Internal" # Options: Internal, Preliminary, ATLAS and NONE

###########################################################################
# DO NOT MODIFY
###########################################################################

import ROOT,os,sys,resource,psutil

HistName  = 'met'
HistNames = [HistName] # Temporary

from InputFiles      import *
from HelperFunctions import *
from Style           import *
from Luminosities    import *

# Loop over requested comparisons
for Key,SampleList in Comparisons.iteritems():
  # Get list of samples
  Samples = dict()
  for sample in SampleList: # loop over samples
    Split = sample.split(':')
    Samples[Split[0]] = Split[1] # key: sample, value: selection

  # Total luminosity and needed campaigns
  Luminosity          = dict() # collect luminosity for each MC campaign
  Luminosity["MC16a"] = 0
  Luminosity["MC16d"] = 0
  Luminosity["MC16e"] = 0
  Campaigns           = []
  DataPeriods         = []
  DataSamples         = [] # List of data samples
  MCSamples           = [] # List of MC samples
  for sample,Selection in Samples.iteritems(): # get data samples
    if "data15" in sample:
      Luminosity["MC16a"] += Luminosity_2015
      Campaigns.append("MC16a")
      DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
      DataPeriods.append("15")
    elif "data16" in sample:
      Luminosity["MC16a"] += Luminosity_2016
      if "MC16a" not in Campaigns: Campaigns.append("MC16a")
      DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
      DataPeriods.append("16")
    elif "data17" in sample:
      Luminosity["MC16d"] += Luminosity_2017
      Campaigns.append("MC16d")
      DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
      DataPeriods.append("17")
    elif "data18" in sample:
      Luminosity["MC16e"] += Luminosity_2018
      Campaigns.append("MC16e")
      DataSamples.append(sample+"_"+Channel+"_"+Selection+"_"+Tagger)
      DataPeriods.append("18")
  for sample,Selection in Samples.iteritems(): # get MC samples
    if "data" not in sample:
      for campaign in Campaigns:
        MCSamples.append(sample+"_"+campaign+"_"+Channel+"_"+Selection+"_"+Tagger)
  TotalLumi = 0
  for key,lumi in Luminosity.iteritems(): TotalLumi += lumi
  
  Campaign   = "MC16"
  for campaign in Campaigns:
    if Campaign != "MC16":    Campaign += "+"
    if campaign == "MC16a":   Campaign += "a"
    elif campaign == "MC16d": Campaign += "d"
    elif campaign == "MC16e": Campaign += "e"
  DataPeriod = "Data"
  for period in DataPeriods:
    if DataPeriod != "Data": DataPeriod += "+"
    DataPeriod += period
  
  # AtlasStyle
  ROOT.gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
  ROOT.SetAtlasStyle()
  ROOT.gROOT.SetBatch(True)
  
  # Loop over histograms
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
    Hist_Data.SetLineColor(ROOT.kBlack)
    Hist_Data.SetFillColor(ROOT.kBlack)
  
    # Get total MC histogram
    DijetsFound = False
    if Debug: print "DEBUG: Get MC histograms"
    counter = 0
    for mc in MCSamples:
      if 'Dijets' in mc:
	DijetsFound = True
        continue # skip dijets
      hist,msg = GetTotalHist([mc],histname,Debug,Luminosity)
      if msg != 'OK':
        print msg
        sys.exit(0)
      if counter == 0: Hist_MC = hist
      else:            Hist_MC.Add(hist)
      counter += 1
    if Debug: print "DEBUG: MC histogram retrieved"
    if Debug: print "DEBUG: Set line and fill color for MC histogram"
    Hist_MC.SetLineColor(ROOT.kRed+1)
    Hist_MC.SetFillColor(ROOT.kRed+1)

    # Plot Dijets (if requested)
    if DijetsFound:
      counter = 0
      for mc in MCSamples:
        if 'Dijets' not in mc: continue # skip other MCs
        hist,msg = GetTotalHist([mc],histname,Debug,Luminosity)
        if msg != 'OK':
          print msg
          sys.exit(0)
        if counter == 0: Hist_Dijets = hist
        else:            Hist_Dijets.Add(hist)
        counter += 1
      Hist_Dijets.SetLineColor(ROOT.kBlue)
      Hist_Dijets.SetFillColor(ROOT.kBlue)
 
    ########################
    # Make Plot
    ########################
  
    # TCanvas
    if Debug: print "DEBUG: Create TCanvas"
    Canvas  = ROOT.TCanvas()
    outName = "Plots/{0}_{1}.pdf".format(Key,histname)
    Canvas.Print(outName+"[")
  
    # TPad for upper panel
    #if Debug: print "DEBUG: Create TPad for upper panel"
    #pad1 = ROOT.TPad("pad1","pad1",0,0.4,1,1.0)
    #pad1.SetTopMargin(0.08)
    #pad1.SetBottomMargin(0.03)
    #pad1.Draw()
    #pad1.cd()
  
    # Set log scales (if requested)
    if Debug: print "DEBUG: Set log scales if requested"
    if histname in Logx:
      Canvas.SetLogx()
    Canvas.SetLogx()
    if histname in Logy:
      Canvas.SetLogy()
  
    # Add histograms to THStack and draw legends
    Legends = ROOT.TLegend(0.8,0.7,0.92,0.9)
    Legends.SetTextFont(42)
  
    Hist_Data.Draw("E P")
    Hist_Data.GetXaxis().SetRangeUser(0,1500)
    if XaxisTitles.has_key(histname):
      Hist_Data.GetXaxis().SetTitleSize(20)
      Hist_Data.GetXaxis().SetTitleFont(43)
      Hist_Data.GetXaxis().SetLabelFont(43)
      Hist_Data.GetXaxis().SetLabelSize(19)
      Hist_Data.GetXaxis().SetTitleOffset(3)
      Hist_Data.GetXaxis().SetTitle(XaxisTitles[histname])
      Hist_Data.GetXaxis().SetNdivisions(510)
    #Hist_Data.GetXaxis().SetLabelSize(0.)
    #Hist_Data.GetXaxis().SetTitleSize(0.)
    Hist_Data.GetYaxis().SetTitleSize(20)
    Hist_Data.GetYaxis().SetTitleFont(43)
    Hist_Data.GetYaxis().SetLabelFont(43)
    Hist_Data.GetYaxis().SetLabelSize(19)
    Hist_Data.GetYaxis().SetTitleOffset(1.3)
    Hist_Data.GetYaxis().SetTitle("Events / bin-width")
    Hist_Data.SetMinimum(1)
    Legends.AddEntry(Hist_Data,"Data","p")
  
    # THStack for MC samples
    if Debug: print "DEBUG: Draw THSTack with MC histograms"
    StackMC = ROOT.THStack()
    StackMC.Add(Hist_MC,"HIST][")
    Legends.AddEntry(Hist_MC,"MC","f")
    if DijetsFound:
      StackMC.Add(Hist_Dijets,"HIST][")
      Legends.AddEntry(Hist_Dijets,"Dijets","f")
    StackMC.Draw("same nostack")
    StackMC.GetXaxis().SetRangeUser(0,1500)
  
    if Debug: print "DEBUG: Draw data histogram"
    Hist_Data.Draw("same")
    
    if XaxisRange.has_key(histname):
      StackMC.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])
    maxY = Hist_Data.GetMaximum()
    if StackMC.GetMaximum() > maxY: maxY = StackMC.GetMaximum()
    maxYscaling = 1E5
    if "absy" in histname or "phi" in histname or "eta" in histname or "deltaR" in histname or "deltaPhi" in histname or "Weight" in histname: maxYscaling = 2E7
    if "Weight" in histname: maxYscaling = 1E9
    StackMC.GetYaxis().SetRangeUser(1,maxY*maxYscaling)
    Hist_Data.GetYaxis().SetRangeUser(1,maxY*maxYscaling)
  
    #StackMC.GetXaxis().SetLabelSize(0.)
    #StackMC.GetXaxis().SetTitleSize(0.)
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
    #if Debug: print "DEBUG: Create TPad for bottom panel"
    #Canvas.cd()
    #pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.4)
    #pad2.SetTopMargin(0.03)
    #pad2.SetBottomMargin(0.32)
    #pad2.Draw()
    #pad2.cd()
  
    # Set log-y scale (if requested)
    #if Debug: print "DEBUG: Set log-Y scale if requested"
    #if histname in Logx:
    #  pad2.SetLogx()
    #pad2.SetLogx()
  
    # Create data/MC histogram
    #if Debug: print "DEBUG: Create data/MC histogram"
    #ratioHist = Hist_MC.Clone("ratioHist")
    #ratioHist.Divide(Hist_Data)
    #ratioHist.SetLineColor(ROOT.kBlack)
  
    # Set range of ratio panel
    #minY = -0.05
    #maxY = 2.05
    #if "Weight" in histname:
    #  minY = -0.05
    #  maxY = 3.05
    #ratioHist.SetMinimum(minY)
    #ratioHist.SetMaximum(maxY)
   
    # Draw data/MC ratio
    #if Debug: print "DEBUG: Draw MC/data ratio"
    #ratioHist.Draw("e0")
  
    # Draw line at data/MC==1
    #if Debug: print "DEBUG: Draw line at MC/data==1"
    #nbins = ratioHist.GetNbinsX()
    #if histname in XaxisRange:
    #  minX = XaxisRange[histname][0]
    #  maxX = XaxisRange[histname][1]
    #else:
    #  minX = ratioHist.GetXaxis().GetBinLowEdge(1)
    #  maxX = ratioHist.GetXaxis().GetBinUpEdge(nbins)
    #Line = ROOT.TLine(minX,1,maxX,1)
    #Line.SetLineStyle(7)
    #Line.Draw("same")
  
    # Set x-axis title
    #if Debug: print "DEBUG: Set X-axis title"
    #histkey = histname
    #if histname == "lep_pt":
    #  histkey = "mu_pt" if Channel == "MU" else "el_pt"
    #elif histname == "lep_eta":
    #  histkey = "mu_eta" if Channel == "MU" else "el_eta"
    #elif histname == "lep_phi":
    #  histkey = "mu_phi" if Channel == "MU" else "el_phi"
    #if XaxisTitles.has_key(histkey):
    #  ratioHist.GetXaxis().SetTitleSize(20)
    #  ratioHist.GetXaxis().SetTitleFont(43)
    #  ratioHist.GetXaxis().SetLabelFont(43)
    #  ratioHist.GetXaxis().SetLabelSize(19)
    #  ratioHist.GetXaxis().SetTitleOffset(3)
    #  ratioHist.GetXaxis().SetTitle(XaxisTitles[histkey])
    #  ratioHist.GetXaxis().SetNdivisions(510)
  
    #ratioHist.GetYaxis().SetTitleSize(20)
    #ratioHist.GetYaxis().SetTitleFont(43)
    #ratioHist.GetYaxis().SetLabelFont(43)
    #ratioHist.GetYaxis().SetLabelSize(19)
    #ratioHist.GetYaxis().SetTitleOffset(1.3)
    #ratioHist.GetYaxis().SetTitle("MC / Data")
    #ratioHist.GetXaxis().SetRangeUser(0,1500)
  
    # Save PDF
    if Debug: print "DEBUG: Save/print PDF"
    Canvas.Print(outName)
    Canvas.Print(outName+"]")
  
    #ratioHist.Delete()
    Hist_MC.Delete()
    Hist_Data.Delete()
    if DijetsFound: Hist_Dijets.Delete()
  
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

