import os,sys
from ROOT import *
from InputFiles import *
from Style import *

#################################################################################
# Get Hist
#################################################################################
def GetHist(sample,histname,debug=False):

  # Get File
  if debug: print "DEBUG: (GetHist) get file"
  if sample not in InputFiles:
    msg = sample+" not found in InputFiles dictionary, exiting"
    return None,msg
  File = TFile.Open(InputFiles[sample])
  if not File:
    msg = InputFiles[sample]+" not found, exiting"
    return None,msg

  # Get Histogram
  if debug: print "DEBUG: (GetHist) get histogram"
  Hist_orig = File.Get(histname)
  if not Hist_orig:
    msg = histname+" not found in "+InputFiles[sample]+", exiting"
    return None, msg
  Hist = Hist_orig.Clone(histname+"_cloned")
  Hist.SetDirectory(0) # detach from file
  File.Close()

  if 'TM' not in histname and 'met_mtw' not in histname:
    # Rebin
    if debug: print "DEBUG: (GetHist) rebin"
    if "jet_eta" in histname or "jet_phi" in histname: Hist.Rebin(4)

    # Set FillStyle
    if debug: print "DEBUG: (GetHist) setFillStyle"
    Hist.SetFillStyle(1001)

    # Divide by bin-width
    if debug: print "DEBUG: (GetHist) divide by bin-width"
    Hist.Scale(1,'width')

    # Set X-axis range
    if debug: print "DEBUG: (GetHist) set x-axis range"
    if XaxisRange.has_key(histname):
      Hist.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])

  if debug: print "DEBUG: (GetHist) all done"

  return Hist,'OK'

#################################################################################
# Get Total Histogram
#################################################################################
def GetTotalHist(Samples,histname,debug,luminosity=dict()):

  if debug: print "DEBUG: (GetTotalHist) list of samples:"
  if debug: print Samples

  Campaigns = ['MC16a','MC16d','MC16e']

  # Get first histogram
  if debug: print "DEBUG: (GetTotalHist) get first {} histogram in {}".format(histname,Samples[0])
  TotalHist,MSG = GetHist(Samples[0],histname,debug)
  if debug and 'met_mtw' not in histname: print "DEBUG: Integral = {}".format(TotalHist.Integral())
  if MSG != 'OK': return None,MSG
  for campaign in Campaigns:
    if campaign in Samples[0] and 'cutflow' not in histname: TotalHist.Scale(luminosity[campaign])
  if debug and 'met_mtw' not in histname: print "DEBUG: Integral (after scaling) = {}".format(TotalHist.Integral())

  # Now sum all the rest
  if debug: print "DEBUG: (GetTotalHist) sum all the rest"
  for isample in range(1,len(Samples)):
    Hist,msg = GetHist(Samples[isample],histname,debug)
    if msg != 'OK': return None,msg
    for campaign in Campaigns:
      if campaign in Samples[isample] and 'cutflow' not in histname: Hist.Scale(luminosity[campaign])
    TotalHist.Add(Hist)
    Hist.Delete()

  if debug and 'met_mtw' not in histname: print "DEBUG: Integral (after adding the rest of the samples) = {}".format(TotalHist.Integral())

  if debug: print "DEBUG: (GetTotalHist) all done"

  return TotalHist,'OK'
