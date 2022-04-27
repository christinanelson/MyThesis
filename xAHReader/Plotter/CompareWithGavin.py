#!/usr/bin/env python

####################################################################
#                                                                  #
# Purpose: Compare my results with Gavin                           #
# Author : Jona Bossio (jbossios@cern.ch)                          #
#                                                                  #
####################################################################

GavinInputsPath = '/afs/cern.ch/user/j/jbossios/work/public/SM/WZGroup/W+jets_13TeV/GIT/Official_McGill_and_Tufts/McGill/xAHReader/Plotter/GavinInputs/'

Distributions = { # map histogram naming (Jona vs Gavin)
  'mT'      : 'W_mT',
  'ht'      : 'HT',
  'met'     : 'met',
  'njet'    : 'Njets',
  'j0_pt'   : 'jet1_pt',
  'j0_y'    : 'jet1_y',
  'lep_eta' : 'e_eta',
  'lep_pt'  : 'e_pT',
}

Samples = { # map samples (Jona vs Gavin)
  'Signal_data1516' : 'Data',
  'Signal_MC16a'    : 'STDM4_Wenu_Sherpa221_MC16a',
  'Diboson_MC16a'   : 'STDM4_Diboson_Sherpa222_MC16a',
  'Zee_MC16a'       : 'STDM4_Zee_Sherpa221_MC16a',
  'Top_MC16a'       : 'STDM4_Top_PPy8_MC16a',
#  'Ztautau_MC16a'   : 'STDM4_Ztautau_Sherpa221_MC16a',
#  'Wtaunu_MC16a'    : 'STDM4_Wtaunu_Sherpa221_MC16a.root',
#  'Signal_data15' : 'data15',
#  'Signal_data16' : 'data16',
#  'Signal_data17' : 'data17',
#  'Signal_data18' : 'data18',
}

# TODO: add MJ
#-rw-r--r--. 1 jbossios zp  976K Oct  2 12:56 Multijets_MGPy8.root

# Options for Jona's inputs
Channel     = "EL"
Selection   = "SR"
Tagger      = "MV2c10"
ATLASlegend = "Internal" # Options: Internal, Preliminary, ATLAS and NONE
Debug       = False

####################################################################
## DO NOT MODIFY (below this line)
####################################################################

import ROOT,os,sys,resource,psutil,argparse
from  InputFiles      import *
from  HelperFunctions import *
from  Style           import *

os.system('mkdir Plots/'+Selection+'/'+Tagger)
os.system('mkdir Plots/'+Selection+'/'+Tagger+'/ComparingWithGavin')

# Luminosity
from Luminosities import *

# AtlasStyle
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(True)

# Loop over histograms
for sampleJona,sampleGavin in Samples.iteritems():
  for histJona,histGavin in Distributions.iteritems():
  
    if Debug: print "###########################################################"
    if Debug: print "DEBUG: Producing PDF for '"+histJona+"' histogram"
    if Debug: print "DEBUG: Memory usage = {0} (MB)".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
    if Debug: pid = os.getpid()
    if Debug: py  = psutil.Process(pid)
    if Debug: print "DEBUG: CPU[0] = {0} (%)".format(py.cpu_percent())
  
    # Total luminosity and needed campaigns
    Luminosity          = dict() # collect luminosity for each MC campaign
    Luminosity["MC16a"] = Luminosity_2015+Luminosity_2016
    Luminosity["MC16d"] = Luminosity_2017
    Luminosity["MC16e"] = Luminosity_2018
      
    ############################
    # Get Histograms
    ############################
  
    # Get my histograms
    if Debug: print "DEBUG: Get Jona histogram"
    Hist_Jona,msg = GetTotalHist([sampleJona+'_'+Channel+'_SR_'+Tagger],histJona,Debug,Luminosity)
    if msg != 'OK':
      print msg
      print histJona+" not found, exiting"
      sys.exit(0)
    if Debug: print "DEBUG: Jona histogram retrieved"
    if Debug: print "DEBUG: Set line and fill color for Jona histogram"
    Hist_Jona.SetLineColor(ROOT.kBlack)
    Hist_Jona.SetMarkerColor(ROOT.kBlack)
    Hist_Jona.SetFillColor(ROOT.kBlack)
    
    # Get Gavin histograms
    GavinFileName = GavinInputsPath+sampleGavin+'.root'
    GavinFile     = ROOT.TFile.Open(GavinFileName)
    if not GavinFile:
      print 'ERROR: '+GavinFileName+' not found, exiting'
      sys.exit(0)
    Hist_Gavin = GavinFile.Get(histGavin)
    if not Hist_Gavin:
      print('{} not found, exiting'.format(histGavin))
      sys.exit(0)
    #if 'Data' not in sampleGavin: # Temporary
    #  if   'MC16a' in sampleGavin: Hist_Gavin.Scale(Luminosity['MC16a'])
    #  elif 'MC16d' in sampleGavin: Hist_Gavin.Scale(Luminosity['MC16d'])
    #  elif 'MC16e' in sampleGavin: Hist_Gavin.Scale(Luminosity['MC16e'])
    Hist_Gavin.SetLineColor(ROOT.kRed+1)
    Hist_Gavin.SetMarkerColor(ROOT.kRed+1)
    Hist_Gavin.SetFillColor(ROOT.kRed+1)

    # Divide by bin-width
    for binX in range(1,Hist_Gavin.GetNbinsX()+1):
      if Hist_Gavin.GetBinWidth(binX)!=0:
        Hist_Gavin.SetBinContent(binX, Hist_Gavin.GetBinContent(binX)/Hist_Gavin.GetBinWidth(binX))
        Hist_Gavin.SetBinError(binX, Hist_Gavin.GetBinError(binX)/Hist_Gavin.GetBinWidth(binX))
      else:
        Hist_Gavin.SetBinContent(binX, 0)
        Hist_Gavin.SetBinError(binX, 0)

    histnameBase = histJona.replace('_Te1','')
    histnameBase = histnameBase.replace('_Ti2','')
    histnameBase = histnameBase.replace('_Ti1','')
    histkey = histnameBase
    if histJona == "lep_pt":
      histkey = "mu_pt" if Channel == "MU" else "el_pt"

    # Set X-axis range
    if XaxisRange.has_key(histkey):
      Hist_Gavin.GetXaxis().SetRangeUser(XaxisRange[histkey][0],XaxisRange[histkey][1])
  
    ########################
    # Make Plot
    ########################
  
    # TCanvas
    if Debug: print "DEBUG: Create TCanvas"
    Canvas  = ROOT.TCanvas()
    outName = "Plots/{0}/{1}/ComparingWithGavin/{2}_{3}_{4}.pdf".format(Selection,Tagger,sampleGavin,Channel,histJona)
    Canvas.Print(outName+"[")
  
    # TPad for upper panel
    if Debug: print "DEBUG: Create TPad for upper panel"
    pad1 = ROOT.TPad("pad1","pad1",0,0.4,1,1.0)
    pad1.SetTopMargin(0.08)
    pad1.SetBottomMargin(0.03)
    pad1.Draw()
    pad1.cd()
  
    # Set log scales (if requested)
    if Debug: print "DEBUG: Set log scales if requested"
    if histnameBase in Logx:
      pad1.SetLogx()
      #Canvas.SetLogx()
    if histnameBase in Logy:
      pad1.SetLogy()
      #Canvas.SetLogy()
  
    # Add histograms to THStack and draw legends
    Legends = ROOT.TLegend(0.65,0.7,0.92,0.9)
    Legends.SetTextFont(42)

    # Show Federico/Jona ratio
    CMEblock = ROOT.TLatex(0.2,0.25,'Gavin/Jona = '+str(round(Hist_Gavin.Integral()/Hist_Jona.Integral(),2)))
    CMEblock.SetNDC()
    CMEblock.Draw("same")
  
  #  Hist_Jona.Draw("E P")
  #  Hist_Jona.GetXaxis().SetLabelSize(0.)
  #  Hist_Jona.GetXaxis().SetTitleSize(0.)
  #  Hist_Jona.GetYaxis().SetTitleSize(20)
  #  Hist_Jona.GetYaxis().SetTitleFont(43)
  #  Hist_Jona.GetYaxis().SetLabelFont(43)
  #  Hist_Jona.GetYaxis().SetLabelSize(19)
  #  Hist_Jona.GetYaxis().SetTitleOffset(1.3)
  #  Hist_Jona.GetYaxis().SetTitle("Events / bin-width")
  #  Hist_Jona.SetMinimum(1)
  #  Legends.AddEntry(Hist_Jona,"Jona","p")
  
    # THStack for MC samples
    StackMC = ROOT.THStack()
  
    StackMC.Add(Hist_Jona,"p")
    Legends.AddEntry(Hist_Jona,'Jona ('+str(Hist_Jona.Integral())+')',"p")
    StackMC.Add(Hist_Gavin,"p")
    Legends.AddEntry(Hist_Gavin,'Gavin ('+str(Hist_Gavin.Integral())+')',"p")
  
    if Debug: print "DEBUG: Draw THSTack with MC histograms"
    StackMC.Draw("nostack")
    
    if XaxisRange.has_key(histnameBase):
      StackMC.GetXaxis().SetRangeUser(XaxisRange[histnameBase][0],XaxisRange[histnameBase][1])
    #maxY = Hist_Data.GetMaximum()
    #if StackMC.GetMaximum() > maxY: maxY = StackMC.GetMaximum()
    #maxYscaling = 1E5
    #if "absy" in histname or "phi" in histname or "eta" in histname or "deltaR" in histname or "deltaPhi" in histname or "Weight" in histname: maxYscaling = 2E7
    #if "Weight" in histname: maxYscaling = 1E9
    #StackMC.GetYaxis().SetRangeUser(1,maxY*maxYscaling)
    #Hist_Data.GetYaxis().SetRangeUser(1,maxY*maxYscaling)
  
    StackMC.GetXaxis().SetLabelSize(0.)
    StackMC.GetXaxis().SetTitleSize(0.)
    if XaxisTitles.has_key(histkey):
      #StackMC.GetXaxis().SetTitleSize(20)
      StackMC.GetXaxis().SetTitleFont(43)
      StackMC.GetXaxis().SetLabelFont(43)
      #StackMC.GetXaxis().SetLabelSize(19)
      StackMC.GetXaxis().SetTitleOffset(1.3)
      StackMC.GetXaxis().SetTitle(XaxisTitles[histkey])
      StackMC.GetXaxis().SetNdivisions(510)
    StackMC.GetYaxis().SetTitleSize(20)
    StackMC.GetYaxis().SetTitleFont(43)
    StackMC.GetYaxis().SetLabelFont(43)
    StackMC.GetYaxis().SetLabelSize(19)
    StackMC.GetYaxis().SetTitleOffset(1.3)
    StackMC.GetYaxis().SetTitle("Events / bin-width")

    StackMC.Draw("same nostack")

    if Debug: print "DEBUG: Draw legends"
    Legends.Draw("same")
  
    ROOT.gPad.RedrawAxis()
  
    # Show ATLAS legend
    #if Debug: print "DEBUG: Show ATLAS legend"
    #if ATLASlegend != 'NONE':
    #  if   ATLASlegend == "Internal":    atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS} #font[42]{Internal}}}";
    #  elif ATLASlegend == "Preliminary": atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS} #font[42]{Preliminary}}}";
    #  elif ATLASlegend == "ATLAS":       atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS}}}";
    #  else:
    #    print "ERROR: ATLASlegend not recognized, exiting"
    #    sys.exit(0)
    #  ATLASBlock = ROOT.TLatex(0.2,0.8,atlas)
    #  ATLASBlock.SetNDC()
    #  ATLASBlock.Draw("same")
  
    # Show CME and luminosity
    #if Debug: print "DEBUG: Show CME and luminosity"
    #CME = "#scale[1.5]{13 TeV, "+str(round(TotalLumi/1000,1))+" fb^{-1}}"
    #topY = 0.7 if ATLASlegend != 'NONE' else 0.8
    #CMEblock = ROOT.TLatex(0.2,topY,CME)
    #CMEblock.SetNDC()
    #CMEblock.Draw("same")

    # Show sample
    TextBlock = ROOT.TLatex(0.2,0.85,sampleGavin)
    TextBlock.SetNDC()
    TextBlock.Draw('same')
  
    # Show channel
    #if Debug: print "DEBUG: Show channel type"
    #channel = "#scale[1.5]{"
    #channel += "#mu" if Channel == "MU" else "e"
    #channel += " channel}"
    #topY = 0.6 if ATLASlegend != 'NONE' else 0.7
    #TextBlock = ROOT.TLatex(0.2,topY,channel)
    #TextBlock.SetNDC()
    #TextBlock.Draw("same")
    
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
    if histnameBase in Logx:
      pad2.SetLogx()
  
    # Create data/MC histogram
    if Debug: print "DEBUG: Create Gavin/Jona histogram"
    ratioHist = Hist_Gavin.Clone("ratioHist")
    ratioHist.SetLineColor(ROOT.kRed+1)
    if Debug: print "DEBUG: Before dividing by bin width for "+histJona
    ratioHist.Divide(Hist_Jona)
  
    # Set y-axis range of ratio panel
    minY = -0.05
    maxY = 2.05
    ratioHist.SetMinimum(minY)
    ratioHist.SetMaximum(maxY)
  
    # Set x-axis range of ratio panel
    nbins = ratioHist.GetNbinsX()
    if histnameBase in XaxisRange:
      minX = XaxisRange[histnameBase][0]
      maxX = XaxisRange[histnameBase][1]
    else:
      minX = ratioHist.GetXaxis().GetBinLowEdge(1)
      maxX = ratioHist.GetXaxis().GetBinUpEdge(nbins)
    ratioHist.GetXaxis().SetRangeUser(minX,maxX)
   
    # Draw data/MC ratio
    if Debug: print "DEBUG: Draw MC/data ratio"
    ratioHist.Draw("e0")
  
    # Draw line at data/MC==1
    if Debug: print "DEBUG: Draw line at MC/data==1"
    Line = ROOT.TLine(minX,1,maxX,1)
    Line.SetLineStyle(7)
    Line.Draw("same")
  
    # Set x-axis title
    if Debug: print "DEBUG: Set X-axis title"
    histkey = histnameBase
    if histJona == "lep_pt":
      histkey = "mu_pt" if Channel == "MU" else "el_pt"
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
    ratioHist.GetYaxis().SetTitle("Gavin / Jona")
  
    # Save PDF
    if Debug: print "DEBUG: Save/print PDF"
    Canvas.Print(outName)
    Canvas.Print(outName+"]")
  
    Hist_Jona.Delete()
    Hist_Gavin.Delete()
    ratioHist.Delete()

print '>>> DONE <<<'
