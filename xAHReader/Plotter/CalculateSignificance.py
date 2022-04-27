##################################################################################################
# Purpose: Calculate significance for each observable                                            #
# Authors: Christina Nelson (christina.nelson@mail.mcgill.ca) and Jona Bossio (jbossios@cern.ch) #
#                                                                                                #
##################################################################################################

import ROOT,os,sys,math,resource,psutil
from Style import *

def significance(histname, Hist_MC_Signal, Hist_MC_Backgrounds, Debug, DataPeriod, Channel, Selection, Tagger):

  myhist, myselection = histname.split('_',1)  # eg. myhist=ht, myselection=bjetVeto
  if Debug: print "DEBUG: Calculating significance for '{}' with '{}' selection".format(myhist,myselection)

  # TCanvas
  if Debug: print "DEBUG: Create TCanvas"
  Canvas  = ROOT.TCanvas()
  outName = "OutputROOTFiles/Significance/{0}_{1}_{2}_{3}_{4}_{5}".format(DataPeriod,Channel,Selection,Tagger,myhist,myselection)

  # Set log-x/y scale (if requested)
  if Debug: print "DEBUG: Set log-X scale if requested"
  if myhist in Logx: Canvas.SetLogx()
  if Debug: print "DEBUG: Set log-Y scale if requested"
  if myhist in Logy: Canvas.SetLogy()

  # Create S/sqrt(S+B) histogram
  significanceHist  = Hist_MC_Signal.Clone("Significance") # will be S/sqrt(S+B)
  sqrtSBHist        = Hist_MC_Signal.Clone("sqrtSB")       # Will be sqrt(S+B)

  # Sum backgrounds to the signal
  for key,hist in Hist_MC_Backgrounds.iteritems():
    sqrtSBHist.Add(hist)

  # Loop over bins to take sqrt of each bin content of S+B histogram
  if myhist != 'met_mtw':
    nbins = sqrtSBHist.GetNbinsX()
    for ibin in range(1, nbins+1):
      events = sqrtSBHist.GetBinContent(ibin)
      sqrt   = math.sqrt(events) if events > 0 else 0
      sqrtSBHist.SetBinContent(ibin,sqrt)
      sqrtSBHist.SetBinError(ibin,0)
  elif myhist == 'met_mtw':
    nbins_x = sqrtSBHist.GetNbinsX()
    nbins_y = sqrtSBHist.GetNbinsY()
    for ibin_x in range(1,nbins_x+1):
      for ibin_y in range(1,nbins_y+1):
        events = sqrtSBHist.GetBinContent(ibin_x, ibin_y)
        sqrt   = math.sqrt(events) if events > 0 else 0
        sqrtSBHist.SetBinContent(ibin_x,ibin_y,sqrt)
        sqrtSBHist.SetBinError(ibin_x,xbin_y,0)
    significanceHist.SetLogx()
    significanceHist.SetLogy()

  # Divide signal by sqrt(S+B) to get significance (S/sqrt(S+B))
  significanceHist.Divide(sqrtSBHist)

  # Set x-axis range
  if XaxisRange.has_key(histname):
    significanceHist.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])

  # Save significance histogram to a ROOT file
  significanceHist.SaveAs(outName+'.root')

  if Debug: print "DEBUG: Significance calculation DONE"
