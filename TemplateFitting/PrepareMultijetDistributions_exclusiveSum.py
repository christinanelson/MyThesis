############################################################################
## AUTHORS: Christina Nelson and Jona Bossio                               #
## DATE:    11 September 2020                                              #
##                                                                         #
## PURPOSE:                                                                #
##          Prepare multijet distributions summing each exjet contribution #
##                                                                         #
## PROCEDURE:                                                              #
##          Get estimated multijet #events (from fitter outputs)           #
##          Multijet distributions will be:                                #
##          subtracted data scaled to agree with estimated MJ # events     #
##          This is done for each exclusive njet case                      #
##          Final multijet distribution is the sum of each multijet        #
##          distribution in each exclusive njet case                       #
############################################################################

CRdef = 'CR' # options: CR and CRmed

YearCombinations = [
  ['15',],
  ['16'],
  ['15','16'],
]

from Defs import *

import os,sys
sys.path.append("../xAHReader/Plotter/")
sys.path.append("../xAHReader/")

# Import input files
PATH = ""
from InputFiles import InputFiles
from Luminosities import *

Channel = "EL" # "El" or "MU"

for Datasets in YearCombinations:
  # Input files
  Files = dict()
  Campaigns  = []
  DataPeriod = 'Data'
  for dataset in Datasets:
    DataPeriod += dataset
    Files["Data"+dataset+"_CR"]      = InputFiles["Signal_data"+dataset+"_"+Channel+"_"+CRdef+"_"+Tagger]
    if dataset == "15" and "a" not in Campaigns: Campaigns.append("a")
    elif dataset == "16" and "a" not in Campaigns: Campaigns.append("a")
    elif dataset == "17" and "d" not in Campaigns: Campaigns.append("d")
    elif dataset == "18" and "e" not in Campaigns: Campaigns.append("e")
  for campaign in Campaigns:
    Files["MC16"+campaign+"_Signal_CR"]      = InputFiles["Signal_MC16"+campaign+"_"+Channel+"_"+CRdef+"_"+Tagger]
    for bkg in Backgrounds:
      Files["MC16"+campaign+"_"+bkg+"_CR"]      = InputFiles[bkg+"_MC16"+campaign+"_"+Channel+"_"+CRdef+"_"+Tagger]
  
  # Type of selections
  Selections = ['CR']
  
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
  Nevents    = dict()
  for Key,FileName in Files.iteritems():
    # open file
    File = TFile.Open(PATH+FileName)
    if not File:
      print PATH+FileName+" not found, exiting"
      sys.exit(0)  
    # get kinematic histograms and normalize
    for var,njet in Observables.iteritems():
      njetFlag = njet+'_' if njet != 'Inclusive' else ''
      key      = Key+'_'+njetFlag+var
      if njet == 'Inclusive' and var=='njet':
	histname = var
        kinh     = File.Get(histname)
        if not kinh:
          print "ERROR: "+histname+" not found in "+PATH+FileName+", exiting"
          sys.exit(0)
        kinh.SetDirectory(0)
        if "MC16a"   in Key: kinh.Scale(Luminosity["a"])
        elif "MC16d" in Key: kinh.Scale(Luminosity["d"])
        elif "MC16e" in Key: kinh.Scale(Luminosity["e"])
        Histograms[key] = kinh
        for bkd in Backgrounds:
          Histograms["MC_"+bkd+"_CR_"+histname]      = 0
        for sel in Selections:
          Histograms["Data_"+sel+"_"+histname]       = 0
          Histograms["MC_Signal_"+sel+"_"+histname]  = 0
      else: # exclusive njet set
        if njet   == 'a0jet'    : cases = ['e0jet','e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
        elif njet == 'a1jet'    : cases = ['e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
        elif njet == 'a2jet'    : cases = ['e2jet','e3jet','e4jet','e5jet','gt5jet']
        for case in cases:
          caseFlag = case+'_' if case != '' else ''
          histname = caseFlag+var
          kinh     = File.Get(histname)
          key = Key+'_'+case+'_'+var
          if not kinh:
            print "ERROR: "+histname+" not found in "+PATH+FileName+", exiting"
            sys.exit(0)
          kinh.SetDirectory(0)
          if "MC16a"   in Key: kinh.Scale(Luminosity["a"])
          elif "MC16d" in Key: kinh.Scale(Luminosity["d"])
          elif "MC16e" in Key: kinh.Scale(Luminosity["e"])
          Histograms[key] = kinh
          for bkd in Backgrounds:
            Histograms["MC_"+bkd+"_CR_"+histname]      = 0
          for sel in Selections:
            Histograms["Data_"+sel+"_"+histname]       = 0
            Histograms["MC_Signal_"+sel+"_"+histname]  = 0

  ######################################
  # Prepare final data and MC histogram
  ######################################
  for key,hist in Histograms.iteritems():
    if hist == 0: continue                      
    if 'MC_' in key or 'Data_' in key: continue # skip the key for the histograms that we want to create
    name = hist.GetName()
    if "Data" in key:
      SelInKey = key.split('_')[1] # get selection from key
      Sample   = "Data_"
    else: # MC
      SelInKey = key.split('_')[2]  #get selection from key
      if 'Signal' in key: Sample = "MC_Signal_"
      else: Sample = 'MC_'+key.split(SelInKey)[0].split('_')[1]+'_'
    if Histograms[Sample+SelInKey+"_"+name] == 0:
      Histograms[Sample+SelInKey+"_"+name] = hist
      Nevents[Sample+SelInKey+"_"+name]    = hist.Integral()

  ########################################
  # Create multijet histograms
  ########################################
  nMJevents = dict() # number of estimated multijet events
  mu = '' # Temporary
  # Get estimated number of multijet events in inclusive events
  if njet == "inclusive":
    FileName  = 'FitterOutputs/'+CRdef+'/EstimatedNumberOfMultijetEvents_'+DataPeriod+'_njet_mu'+mu+'.txt'
    print('INFO: Opening '+FileName)
    File      = open(FileName)
    case = ''
    if not File:
      print('ERROR: '+FileName+' not found, exiting')
      sys.exit(0)
    for line in File:
      info            = line.split(' ')
      key             = info[0]
      nEvents         = info[1]
      nMJevents[case] = float(nEvents)
  # Get estimated number of multijet events for each exjet case
  for case in ['e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']:
    FileName  = 'FitterOutputs/'+CRdef+'/EstimatedNumberOfMultijetEvents_'+DataPeriod+'_njet'+case+'_mu'+mu+'.txt'
    File      = open(FileName)
    if not File:
      print('ERROR: '+FileName+' not found, exiting')
      sys.exit(0)
    for line in File:
      info            = line.split(' ')
      key             = info[0]
      nEvents         = info[1]
      nMJevents[case] = float(nEvents)

  # Get multijet distribution for each exjet case
  for var,njetFlag in Observables.iteritems(): # loop over variables/observables
    #if   njetFlag == 'a0jet':     cases = ['e0jet','e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
    if njetFlag == 'a1jet':       cases = ['e1jet','e2jet','e3jet','e4jet','e5jet','gt5jet']
    elif njetFlag == 'a2jet':     cases = ['e2jet','e3jet','e4jet','e5jet','gt5jet']
    for case in cases:
      Nmj = nMJevents[case]
      print "############################################################################"
      print "INFO: variable: "+var

      # Prepare multijet histogram starting from the distribution of the observable in data_CR
      if case != '': case = '{}_'.format(case)
      Histograms["Multijet_"+case+var] = Histograms["Data_CR_"+case+var].Clone("Multijet_"+case+var)

      print "INFO: Estimated number of MJ events for "+case+"             = "+str(Nmj)
      print "INFO: Number of data events in CR for "+case+"               = "+str(Histograms["Multijet_"+case+var].Integral())

      # Get total number of MC signal + EWbkgs in CR
      MCtotal = Histograms["MC_Signal_CR_"+case+var].Integral()
      for bkg in Backgrounds: MCtotal += Histograms["MC_"+bkg+"_CR_"+case+var].Integral()

      print "INFO: Number of MCsignal+EWBKGS events in CR for "+case+"    = "+str(MCtotal)

      # Scale multijet distribution such as the total number after scaling and subtracting agrees with the estimated MJ events
      Histograms["Multijet_"+case+var].Scale((Nmj+MCtotal)/Histograms["Multijet_"+case+var].Integral())

      # Subtract MC signal and EWbkgs from CR
      Histograms["Multijet_"+case+var].Add(Histograms["MC_Signal_CR_"+case+var],-1)
      for bkg in Backgrounds: Histograms["Multijet_"+case+var].Add(Histograms["MC_"+bkg+"_CR_"+case+var],-1)

      # Total number of multijet events in SR
      Nkin = Histograms["Multijet_"+case+var].Integral()
      print "INFO: Number of events in final MJ distribution for "+case+" = "+str(Nkin)
    
  # Save all multijet distributions
  OutputFileName = "FitterOutputs/"+CRdef+"/MultijetDistributions_"+DataPeriod+"_Exclusive.root"
  OutputFile     = TFile(OutputFileName,"RECREATE")
  # Save summed histogram for each observable
  for var in Observables:
    SumHists = 0
    for key,Hist in Histograms.items():
      if 'Multijet_' in key and var in key:
        if SumHists == 0: SumHists = Hist.Clone("TotalMultijet_{}".format(var))
        else:             SumHists.Add(Hist)
    SumHists.Write()
  # Save individual histograms
  for key,Hist in Histograms.items():
    if 'njet' in key: continue # saved already
    if 'Multijet_' in key: Hist.Write()
  OutputFile.Close()

print ">>> ALL DONE <<<"
