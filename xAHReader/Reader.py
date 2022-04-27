#################################################################################
## Author:  Christina Nelson                                                    # 
## Date:    April 27, 2020                                                      #
## Purpose: Read TTrees produced with MakeTTrees_Wjets and fill histograms      #
#################################################################################

###################################################
## TODO
###################################################
# Add Wpt
# Implement b-tagging SFs
# Allow to estimate uncertainties from MC variations
# Add a TLatex kind of class with the description of the ROOT file
# Add Truth MET cut?
# Add separated cuts for truth (jet pT, lepton pT/eta, etc)
###################################################

from ROOT import *
import os,sys,argparse,array
from HelperClasses import *
from HelperFunctions import *
from Selections import *
from Arrays import *
from Dicts import *
from metadata_dict import MetadataFiles

# Read arguments
parser = argparse.ArgumentParser()

parser.add_argument('--path',            action='store',      dest="path")
parser.add_argument('--outPATH',         action='store',      dest="outPATH")
parser.add_argument('--file',            action='store',      dest="inputFile")

parser.add_argument('--channel',         action='store',      dest="channel")
parser.add_argument('--dataset',         action='store',      dest="dataset")
parser.add_argument('--selection',       action='store',      dest="selection")
parser.add_argument('--tagger',          action='store',      dest="tagger")
parser.add_argument('--debug',           action='store_true', dest="debug")
parser.add_argument('--noReco',          action='store_true', dest="noReco")
parser.add_argument('--noTruth',         action='store_true', dest="noTruth")
parser.add_argument('--noSFs',           action='store_true', dest="noSFs")
parser.add_argument('--noSampleWeights', action='store_true', dest="noSampleWeights")
parser.add_argument('--noPRW',           action='store_true', dest="noPRW")
parser.add_argument('--readAMI',         action='store_true', dest="readAMI")
parser.add_argument('--printInfo',       action='store_true', dest="printInfo", default=False)

args = parser.parse_args()

# Sample type
Channel          = args.channel
Dataset          = args.dataset

# Jet Flavour Tagger
Tagger           = args.tagger

# MC Weights (only meaningful for MC, not used in data)
useSFs           = not args.noSFs
useSampleWeights = not args.noSampleWeights
usePRW           = not args.noPRW
readAMI          = args.readAMI

# Selection
Selection        = args.selection

# Distributions
fillReco  = not args.noReco
fillTruth = not args.noTruth

# Debugging
Debug = args.debug

# Print event level information
PrintInfo = args.printInfo

# Protections
if "MU" not in Channel and "EL" not in Channel:
  print ("ERROR: Channel not recognised, exiting")
  sys.exit(0)
if Dataset not in DatasetOptions:
  print ("ERROR: Dataset not recognised, exiting")
  sys.exit(0)
if args.path is None:
  print ("ERROR: path to input file not provided, exiting")
  sys.exit(0)
if args.outPATH is None:
  print ("ERROR: path to output files (outPATH) not provided, exiting")
  sys.exit(0)
if args.inputFile is None:
  print ("ERROR: input file not provided, exiting")
  sys.exit(0)
if Tagger not in Taggers:
  print ("ERROR: Flavour Jet Tagger not recognized, exiting")
  sys.exit(0)

# MC?
MC = False
if 'Data' not in Dataset:
  MC = True

# Protections
if not MC: # data
  if useSFs:           useSFs           = False
  if useSampleWeights: useSampleWeights = False
  if usePRW:           usePRW           = False
  if fillTruth:        fillTruth        = False
if MC and readAMI and not useSampleWeights:
  print ("ERROR: asked to read AMI info but not to use sample weights, exiting")
  sys.exit(0)

# Get MC16 campaign
if MC:
  if "MC16a" in Dataset:
    campaign = "a"
  elif "MC16d" in Dataset:
    campaign = "d"
  elif "MC16e" in Dataset:
    campaign = "e"

# Print INFO
if useSFs:
  print ("INFO: Using scale factors")
if useSampleWeights:
  print ("INFO: Using sample weights")
if usePRW:
  print ("INFO: Using PRW")

###############################
# Read AMI info (if requested)
###############################
if readAMI:
  FileName = "ami_reader.txt"
  AMIFile  = open(FileName,'r')
  lines    = AMIFile.readlines()
  AMIxss = dict() # cross section values
  AMIeff = dict() # efficiency values
  AMIk   = dict() # k-factor values
  for line in lines: # loop over lines
    Line = line.split(" ")
    dsid = int(Line[0]) # first column is dsid
    AMIxss[dsid] = float(Line[1]) # second column is cross section
    AMIeff[dsid] = float(Line[2]) if '\n' not in Line[2] else float(Line[2][:-2]) # third column is efficiency
    if len(Line) > 3: kFactor = Line[3] # fourth column (if available) is k-factor
    else: kFactor = '1.0'
    AMIk[dsid] = float(kFactor) if '\n' not in kFactor else float(kFactor)

#####################
# Output file name
#####################

# Identify DSID/dataPeriod
if MC:
  DSID = getDSID(args.path)
else:
  period = getPeriod(args.path)

inputFileName  = args.inputFile.replace(".root","")

OutName      = str(args.outPATH)
OutName     += Dataset
if MC:
  if DSID != '': OutName   += "_" + DSID
else:
  if period != '': OutName   += "_" + period
OutName     += "_" + Channel + "_" + Selection
OutName     += "_" + Tagger + "Tagger"
if MC:
  if useSFs:
    OutName += "_useSFs"
  else:
    OutName += "_noSFs"
  if useSampleWeights:
    OutName += "_useSampleWeights"
  else:
    OutName += "_noSampleWeights"
  if usePRW:
    OutName += "_usePRW"
  else:
    OutName += "_noPRW"
OutName     += "_" + inputFileName
if Debug:
  OutName   += "_Debug"
OutName     += ".root"

# Running on MC signal?
isMCsignal = False
if   MC and "MU" in Channel and "Wmunu" in Dataset: isMCsignal = True
elif MC and "EL" in Channel and "Wenu" in Dataset:  isMCsignal = True

# Produce transfer matrices?
makeTMs = True if isMCsignal else False

# Fill truth distributions only in MC signal
if not isMCsignal: fillTruth = False

#####################
# TTree names
#####################
TDirectoryName       = "TreeAlgo" #TreeAlgo
TTreeName            = "nominal" #"nominal", down then up

#####################
# Event selections
#####################
common = Common()
if Selection == "SR":        SelectionClass = SRselection()
elif Selection == "SRGavin": SelectionClass = SRGavinselection()
elif Selection == "SRwoMET": SelectionClass = SRwoMETselection()
elif Selection == "CR":      SelectionClass = CRselection()
elif Selection == "CRmed":   SelectionClass = CRmedselection()
elif Selection == "Tight":   SelectionClass = Tightselection()
elif Selection == "SRLowPtLooseVeto":   SelectionClass = SRLowPtLooseVetoselection()
elif Selection == "SRLowPtTightVeto":   SelectionClass = SRLowPtTightVetoselection()
elif Selection == "SRHighPtLooseVeto":  SelectionClass = SRHighPtLooseVetoselection()
elif Selection == "SRHighPtTightVeto":  SelectionClass = SRHighPtTightVetoselection()
elif Selection == "CRLowPtLooseVeto":   SelectionClass = CRLowPtLooseVetoselection()
elif Selection == "CRLowPtTightVeto":   SelectionClass = CRLowPtTightVetoselection()
elif Selection == "CRHighPtLooseVeto":  SelectionClass = CRHighPtLooseVetoselection()
elif Selection == "CRHighPtTightVeto":  SelectionClass = CRHighPtTightVetoselection()
else:
  print ("ERROR: Selection not recognized, exiting")
  sys.exit(0)

# Print selection definitions
print('############################################')
print('Selection definitions:')
print(vars(common))
print(vars(SelectionClass))
print('############################################')

# Max number of events for debuging
DebugMAXevents = 1000

###################
# Book histograms
###################

# Cutflow histograms
Types = ["reco"]
if MC and fillTruth: Types.append("truth")
for Type in Types:
  h_cutflow[Type] = TH1D("cutflow_"+Type,"", 1, 1, 2)
  h_cutflow[Type].SetCanExtend(TH1D.kAllAxes)
  h_cutflow_all[Type]           = h_cutflow[Type].GetXaxis().FindBin("All")
  h_cutflow_trigger[Type]       = h_cutflow[Type].GetXaxis().FindBin("Trigger")
  h_cutflow_jetCleaning[Type]   = h_cutflow[Type].GetXaxis().FindBin("Jet cleaning")
  h_cutflow_met[Type]           = h_cutflow[Type].GetXaxis().FindBin("MET")
  h_cutflow_lepPtEta[Type]      = h_cutflow[Type].GetXaxis().FindBin("LepPt")
  h_cutflow_lepIP[Type]         = h_cutflow[Type].GetXaxis().FindBin("LepEta")
  h_cutflow_lepID[Type]         = h_cutflow[Type].GetXaxis().FindBin("LepID")
  h_cutflow_lepIso[Type]        = h_cutflow[Type].GetXaxis().FindBin("LepIso")
  h_cutflow_sigLepton[Type]     = h_cutflow[Type].GetXaxis().FindBin("SignalLepton")
  h_cutflow_lepTrigMatch[Type]  = h_cutflow[Type].GetXaxis().FindBin("LepTrigMatch")
  h_cutflow_lepVeto[Type]       = h_cutflow[Type].GetXaxis().FindBin("LepVeto")
  h_cutflow_mT[Type]            = h_cutflow[Type].GetXaxis().FindBin("mT")
  h_cutflow_OR[Type]            = h_cutflow[Type].GetXaxis().FindBin("OverlapRemoval")
  h_cutflow_jet[Type]           = h_cutflow[Type].GetXaxis().FindBin("Jet")
  h_cutflow_bTagging[Type]      = h_cutflow[Type].GetXaxis().FindBin("Btagging")

# mcEvtWeight
if MC:
  h_mcEventWeight = TH1D("mcEvtWeight","",10000,-5000,5000)
  h_mcEventWeight.Sumw2()

##################################
# Histograms for each observable

# Number of interactions per bunch crossing (<mu>/actualMu)
h_correctedAverageMu = TH1D("correctedAverageMu","",500,0,100)
h_correctedAverageMu.Sumw2()
h_correctedAndScaledAverageMu = TH1D("correctedAndScaledAverageMu","",500,0,100)
h_correctedAndScaledAverageMu.Sumw2()
h_correctedActualMu = TH1D("correctedActualMu","",500,0,100)
h_correctedActualMu.Sumw2()
h_correctedAndScaledActualMu = TH1D("correctedAndScaledActualMu","",500,0,100)
h_correctedAndScaledActualMu.Sumw2()
h_actualInteractionsPerCrossing = TH1D("actualInteractionsPerCrossing","",500,0,100)
h_actualInteractionsPerCrossing.Sumw2()
h_averageInteractionsPerCrossing = TH1D("averageInteractionsPerCrossing","",500,0,100)
h_averageInteractionsPerCrossing.Sumw2()

# 1D histograms for all variables
for Type in Types: # loop over reco/truth
  # Loop over variables
  for var in AllVariables:
    # Loop over njet multiplicities
    for nJet in nJetmultiplicities:
      if var is 'met_mtw': continue # skip 2D histogram here
      for mu in muFlags:    
        if mu != '' and var != 'met': continue # skip low-/high-mu non-met plots
        # Create key for Histogram dict
        extraType = '_truth' if Type == 'truth' else ''
        extraNjet = nJet+'_' if nJet != ''      else ''
        extraMu   = mu+'_'   if mu   != ''      else ''
        key       = extraNjet+extraMu+var+extraType
        # Create TH1D histogram(s)
        HistName = key
        if var in Binning:
          if len(Binning[var]) > 3: # binning given by array
            Histograms[key] = TH1D(HistName,'',len(Binning[var])-1,Binning_array[var])
          else: # binning given by nbins, minVal and maxVal
            Histograms[key] = TH1D(HistName,'',Binning[var][0],Binning[var][1],Binning[var][2])
        else:
          print ('ERROR: no binning provided for this variable: '+var+', exiting')
          sys.exit(0)
        Histograms[key].Sumw2()
        if var == 'j0_eta' or var == 'j1_eta' or var == 'j2_eta':
          for ptbin in pTbins: # loop over pt bins for eta distribution
            PtBin = ptbin.split(":")
            Histograms[extraNjet+var+'__pt_'+PtBin[0]+'_'+PtBin[1]+extraType] = TH1D(extraNjet+var+extraType+"__pt_"+PtBin[0]+"_"+PtBin[1],"",Binning[var][0],Binning[var][1],Binning[var][2])
            Histograms[extraNjet+var+'__pt_'+PtBin[0]+'_'+PtBin[1]+extraType].Sumw2()
    # Book histograms for significance study
    if var in sig_variables and SelectionClass.doSignificanceStudy and Type is not 'truth':
      for variation in sig_variations:
        Key      = var+'_'+variation
        if var is not 'met_mtw':
          if var in Binning:
            if len(Binning[var]) > 3: # binning given by array
              Histograms[Key] = TH1D(Key,'',len(Binning[var])-1,Binning_array[var])
            else: Histograms[Key] = TH1D(Key,'',Binning[var][0],Binning[var][1],Binning[var][2])
          else: 
            print ('ERROR: no binning provided for this variable: '+var+', exiting')
            sys.exit(0)
        if var is 'met_mtw': # book 2D histogram here
          Histograms[Key] = TH2D(Key,'',len(Binning['met'])-1,Binning_array['met'],len(Binning['mT'])-1,Binning_array['mT'])
        Histograms[Key].Sumw2()

# Book TMs for unfolding (only for observables)
if makeTMs:
  print ("INFO: Will make transfer matrices")
  for obs in Observables: # loop over observables
    HistName = 'TM_'+obs
    if len(Binning[obs])>3: # binning given by array
      Histograms_2D[obs] = TH2D(HistName,'',len(Binning[obs])-1,Binning_array[obs],len(Binning[obs])-1,Binning_array[obs])
    else: # binning given by nbins, minVal and maxVal
      Histograms_2D[obs] = TH2D(HistName,'',Binning[obs][0],Binning[obs][1],Binning[obs][2],Binning[obs][0],Binning[obs][1],Binning[obs][2])
    Histograms_2D[obs].Sumw2()

###########################
# Get sumWeights (MC only)
###########################
sumWeights = dict()
if MC:
  # Loop over metadata files
  if Dataset not in MetadataFiles:
    print ("ERROR: No metadata found for "+Dataset+", exiting")
    sys.exit(0)
  for key,value in MetadataFiles[Dataset].items(): #key:dsid, value:path+metadata file
    # open metadata file
    MetadataFile = TFile.Open(value)
    if not MetadataFile:
      print ("ERROR: "+value+" file not found, exiting")
      sys.exit(0)
    # get histogram
    MetadataHist    = MetadataFile.Get("MetaData_EventCount")
    sumWeights[key] = MetadataHist.GetBinContent(3)

#############################
# Get Prescaled Correted Lumi
#############################
#if Selection == "CR" and MC:
#  PrescaleWeights = dict()
#  if "MC16a" in args.path: WeightsFileName = "PrescaledLumiWeights_MC16a.txt"
#  try:
#    with open(WeightsFileName, "r") as mf_weights:
#      for line in mf_weights.readlines():
#        if "#" in line: continue
##        print(line)
#        key, lumi_corr, weight_corr = line.strip().split()
#        PrescaleWeights[key] = float(lumi_corr)
##    print(PrescaleWeights)
#  except:
#    print ("Prescale Weights file " + WeightsFileName + " not found, exiting...")
#    sys.exit(0)

######################################
# Open TFile/TDirectory and get TTree
######################################
print ("INFO: Opening "+args.path+args.inputFile)
tfile = TFile.Open(args.path+args.inputFile)
if not tfile:
  print ("ERROR: "+args.path+args.inputFile+" not found, exiting")
  sys.exit(0)

# Get TNamed object with weight names
if MC:
  TNamedWeights = tfile.Get('WeightNames')
  if not TNamedWeights:
    print ('WARNING: WeightNames TNamed object does not exist, will use index 0 of the nominal weight')
    NominalWeightIndex = 0
  else:
    WeightNames      = TNamedWeights.GetTitle()
    if 'SEP' in WeightNames: # new files
      WeightNamesArrayTmp = WeightNames.split('SEP')
      print ("SEP in WeightNames")
    else: # old files
      WeightNamesArrayTmp = WeightNames.split(':')
    WeightNamesArray    = [x.replace('.','_') for x in WeightNamesArrayTmp]
    WeightNamesArray    = [x.replace('=','')  for x in WeightNamesArray]
    WeightNamesArray    = [x.replace(' ','')  for x in WeightNamesArray]
    WeightNamesArray    = [x.replace(',','')  for x in WeightNamesArray]
    WeightNamesArray    = [x.replace(':','')  for x in WeightNamesArray]        
    if ' nominal ' in WeightNamesArray:
      NominalWeightIndex = WeightNamesArray.index(' nominal ')
      WeightNamesArray[NominalWeightIndex] = 'nominal'
    elif 'nominal' in WeightNamesArray:
      NominalWeightIndex = WeightNamesArray.index('nominal')
    elif 'Weight' in WeightNamesArray:
      NominalWeightIndex = WeightNamesArray.index('Weight')
      WeightNamesArray[NominalWeightIndex] = 'nominal' # Weight -> nominal
    else:
      print('ERROR: nominal MC event weight not found, exiting')
      sys.exit(0)
    print ("INFO: Using index {} as nominal weight".format(NominalWeightIndex))

# Get TDirectoryFile with all the TTrees
tdir = TDirectoryFile()
tdir = tfile.Get(TDirectoryName)
if not tdir:
  print ("ERROR: "+TDirectoryName+" not found, exiting")
  sys.exit(0)

tree = TFile()
tree = tdir.Get(TTreeName)
#tree = tfile.Get(TTreeName)
if not tree:
  print ("WARNING: TTree not found, exiting")
  sys.exit(0)
totalEvents = tree.GetEntries()
print ("INFO: TotalEvents in TTree: "+str(totalEvents))

###################
# Loop over events
###################
event_counter = 0
if Debug: printMemory(0)
for event in tree:
  if Debug: printMemory(1)
  VariablesValues = dict()
  event_counter += 1
  if Debug and event_counter > DebugMAXevents:
    break # skip loop
  #if Debug:
  #  print "DEBUG: EventNumber: "+str(tree.eventNumber)
  if event_counter == 1:
    print ("INFO: Running on event #"+str(event_counter)+" of "+str(totalEvents)+" events")
  if event_counter % 1000000 == 0:
    print ("INFO: Running on event #"+str(event_counter)+" of "+str(totalEvents)+" events")

  ########################
  # Early rejection
  ########################
  if MC and usePRW and tree.weight_pileup == 0:
    if Debug: print ("DEBUG: Early rejection of event due to PRW")
    continue # skip event for MC

  ##################################
  # Fill mcEvtWeight for all events
  ##################################
  if MC:
    if TTreeName == "nominal":
      h_mcEventWeight.Fill(tree.mcEventWeights[NominalWeightIndex])
    else:
      h_mcEventWeight.Fill(tree.mcEventWeight)

  ####################
  # Get event weights
  ####################
  weight   = 1.0
  if useSampleWeights:
    if not readAMI:
      weight *= tree.weight[0] / sumWeights[tree.mcChannelNumber]
    else: # read AMI info again
      weight *= AMIxss[tree.mcChannelNumber]
      weight *= AMIeff[tree.mcChannelNumber]
      weight *= AMIk[tree.mcChannelNumber]
      if TTreeName == "nominal":
        weight *= tree.mcEventWeights[NominalWeightIndex]
      else:
        weight *= tree.mcEventWeight
      weight /= sumWeights[tree.mcChannelNumber]
        
    if Debug:
      #print "DEBUG: tree.mcEventWeight: "+str(tree.mcEventWeights[NominalWeightIndex])
      #print "DEBUG: sumWeights: "+str(sumWeights[tree.mcChannelNumber])
      print ("DEBUG: sampleWeight: "+str(weight))
  if usePRW:
    weight *= tree.weight_pileup

  ##########################################
  # Get number of interactions per crossing
  ##########################################
  #correctedAndScaledAverageMu	 = tree.correctedAndScaledAverageMu
  #averageInteractionsPerCrossing = tree.averageInteractionsPerCrossing
  actualInteractionsPerCrossing	 = tree.actualInteractionsPerCrossing
  #correctedAndScaledActualMu	 = tree.correctedAndScaledActualMu
  #correctedAverageMu		 = tree.correctedAverageMu
  #correctedActualMu 		 = tree.correctedActualMu

  #if Debug: print ("DEBUG: averageInteractionsPerCrossing: "+str(averageInteractionsPerCrossing))

  ##################################################################
  # Apply event/object selections and fill reco/truth distributions
  ##################################################################
  passReco  = False
  passTruth = False
  for Type in Types:
    
    extraType = '_truth' if Type == 'truth' else ''

    ##############################
    # Event and object selections
    ##############################
    if Debug: print ("DEBUG: Apply "+Type+" event/object selections")

    h_cutflow[Type] .Fill(h_cutflow_all[Type],1)

    ########################
    # C0: Trigger Selection
    ########################
    if Type == "reco": # MC and data
      passTrigger = False
      # Create list of triggers to request in data anc MC reco
      if MC:
        if "MC16a" in args.path:
          if tree.rand_run_nr < 297730: Year = "2015"
          else:                         Year = "2016"
        elif "MC16d" in args.path: Year = "2017"
        elif "MC16e" in args.path: Year = "2018"
      else: # data
        if "2015" in args.path:   Year = "2015"
        elif "2016" in args.path: Year = "2016"
        elif "2017" in args.path: Year = "2017"
        elif "2018" in args.path: Year = "2018"
      Triggers = []
      if "EL" in Channel:
        if "SR" in Selection or Selection == "Tight":
          if Year == "2015":   Triggers.extend(common.Unprescaled_ELTriggers_2015)
          elif Year == "2016": Triggers.extend(common.Unprescaled_ELTriggers_2016)
          elif Year == "2017": Triggers.extend(common.Unprescaled_ELTriggers_2017)
          elif Year == "2018": Triggers.extend(common.Unprescaled_ELTriggers_2018)
        elif "CR" in Selection:
          if Year == "2015":   Triggers.extend(common.Prescaled_ELTriggers_2015)     
          elif Year == "2016": Triggers.extend(common.Prescaled_ELTriggers_2016)
          elif Year == "2017": Triggers.extend(common.Prescaled_ELTriggers_2017)
          elif Year == "2018": Triggers.extend(common.Prescaled_ELTriggers_2018)
      #elif "MU" in Channel:
      #  if "SR" in Selection or Selection == "Tight":
      #    if Year == "2015":   Triggers.extend(common.Unprescaled_MUTriggers_2015)
      #    elif Year == "2016": Triggers.extend(common.Unprescaled_MUTriggers_2016)
      #    elif Year == "2017": Triggers.extend(common.Unprescaled_MUTriggers_2017)
      #    elif Year == "2018": Triggers.extend(common.Unprescaled_MUTriggers_2018)
      #  elif "CR" in Selection:
      #    if Year == "2015":   Triggers.extend(common.Prescaled_MUTriggers_2015)
      #    elif Year == "2016": Triggers.extend(common.Prescaled_MUTriggers_2016)
      #    elif Year == "2017": Triggers.extend(common.Prescaled_MUTriggers_2017)
      #    elif Year == "2018": Triggers.extend(common.Prescaled_MUTriggers_2018)
      Triggers = list(dict.fromkeys(Triggers)) # remove duplicates (protection but there shouldn't be any duplicate)
      #print (Triggers)
      #sys.exit(0)
      if Debug:
        print ("DEBUG: Requested triggers:")
        for trigger in Triggers:
          print ("DEBUG:  "+str(trigger))
      if Debug: print ("DEBUG: Fired triggers: ")
      mf_passedTrigger = ""
      for trigger in tree.passedTriggers:
        if Debug: print ("DEBUG:  "+str(trigger))
        if trigger in Triggers:
          passTrigger = True
          #print (">>>>>>>> EVENT REALLY PASSED TRIGGER:  "+str(trigger))
          mf_passedTrigger = trigger
          break
      if not passTrigger:
        if Debug: print ("DEBUG: Event not passed trigger selection")
        continue # skip event for reco
      if Debug: print ("DEBUG: Event passed trigger selection")
      h_cutflow["reco"].Fill(h_cutflow_trigger["reco"],1)

    ###########################################################
    # C1: Jet Cleaning (MC reco only, in data already applied)
    ###########################################################
    if MC and Type == "reco" and SelectionClass.jet_cleaning and not eventIsClean(tree):
      if Debug: print ("DEBUG: Event not passed jet cleaning")
      continue # skip event for MC reco
    if Debug: print ("DEBUG: Event passed jet cleaning")
    if Type == "reco": h_cutflow["reco"].Fill(h_cutflow_jetCleaning["reco"],1)

    ##############
    # C2: MET cut
    ##############
    if Type == "reco": # Temporary FIXME
      MET = getMET(tree)
      if hasattr(SelectionClass,'minMET'): # minMET cut exists in the chosen selection class
        if MET < SelectionClass.minMET:
          if Debug: print ("DEBUG: Event not passed MET cut (MET = {})".format(MET))
          continue # skip event for reco
    if Debug: print ("DEBUG: Event passed MET cut")
    h_cutflow[Type].Fill(h_cutflow_met[Type],1)

    ###################################################
    # C3: Select events with exactly one signal lepton
    ###################################################

    # Get all leptons (for electrons/muons in the EL/MU channel, also decorate those which are signal-like)
    AllLeptons   = dict()
    #OtherChannel = 'EL' if Channel == 'MU' else 'MU'
    AllLeptons[Channel]      = getAllLeptons(tree,Channel,SelectionClass,Type,useSFs,Debug,campaign,Triggers,True)
    #AllLeptons[OtherChannel] = getAllLeptons(tree,OtherChannel,SelectionClass,Type,useSFs,Debug,campaign,Triggers,False)

    if Debug:
      #for fvl in ['MU','EL']:
      for fvl in ['EL']:
        print('DEBUG: {} leptons:'.format(fvl)) #fix following line
	#print({lep:[lep.Pt(),lep.Eta(),lep.Phi(),lep.passLooseSel,lep.passSignalSel] for lep in AllLeptons[fvl]})

    passNLeptonSelection = True
    lep_n = SelectionClass.muon_n if Channel == "MU" else SelectionClass.el_n
    nSignalLikeLeptons = 0
    for lep in AllLeptons[Channel]:
      if lep.passSignalSel:
        nSignalLikeLeptons += 1
        SignalLepton = lep
    if nSignalLikeLeptons != lep_n: passNLeptonSelection = False
    if not passNLeptonSelection:
      if Debug: print ("DEBUG: Event not passed 'N signal-like lepton' requirement")
      continue # skip event
    if Debug: print ("DEBUG: Event passed 'N signal-like lepton' requirement")
    h_cutflow[Type].Fill(h_cutflow_sigLepton[Type],1)

    ##################################################################################################################
    # C4: Vetoes (no muon/electron in electron/muon channel and no additional electron/muon in muon/electron channel)
    ##################################################################################################################

    # Veto 1: skip events with muons (electrons) in electron (muon) channel
    passVeto1 = True
    #nOtherChannelLeptons = 0
    #for lep in AllLeptons[OtherChannel]:
    #  if lep.passLooseSel: nOtherChannelLeptons += 1
    #if nOtherChannelLeptons > 0: passVeto1 = False
    if not passVeto1:
      if Debug: print ("DEBUG: Event not passed 'no muon(electron) in electron(muon) channel' cut")
      continue # skip event
    if Debug: print ("DEBUG: Event passed 'no muon(electron) in electron(muon) channel' cut")

    # Veto 2: skip events with a second muon(electron) in the muon(electron) channel
    # The signal-like lepton selected above is not considered in this veto
    passVeto2 = True
    nAdditionalSignalLeptons = 0
    for lep in AllLeptons[Channel]:
      if lep.passSignalSel: continue # skip signal lepton
      if lep.passLooseSel: nAdditionalSignalLeptons += 1
    if nAdditionalSignalLeptons > 0: passVeto2 = False
    if not passVeto2:
      if Debug: print ("DEBUG: Event not passed 'no additional muon(electron) in muon(electron) channel' cut")
      continue # skip event
    if Debug: print ("DEBUG: Event passed 'no additional muon(electron) in muon(electron) channel' cut")

    h_cutflow[Type].Fill(h_cutflow_lepVeto[Type],1)

    if Debug and Type == 'reco':
      print ("DEBUG: signal lep pt: {}".format(round(SignalLepton.Pt(),2)))
      print ("DEBUG: signal lep eta: {}".format(round(SignalLepton.Eta(),2)))

    ###############################
    # C5: mT(+MET) requirement
    ###############################
    if Type == "reco":
      passmTCut                             = True
      met                                   = getMET(tree)
      met_phi                               = getMETPhi(tree)
      VariablesValues['mT'+extraType]       = TMath.Sqrt(2*SignalLepton.Pt()*met*(1-TMath.Cos(SignalLepton.Phi()-met_phi)))
      VariablesValues['met'+extraType]      = met
      VariablesValues['met_phi'+extraType]  = met_phi
      if hasattr(SelectionClass,'minmT'): # minmT cut exists in the chosen selection class
        if VariablesValues['mT'+extraType] < SelectionClass.minmT: passmTCut = False
        if not passmTCut:
          if Debug: print ("DEBUG: Event not passed mT cut (mT == "+str(VariablesValues['mT'+extraType])+" )")
          continue # skip event
      elif hasattr(SelectionClass,'minmTplusMET'): # mT+MET cut exists in the chosen selection class
        if VariablesValues['mT'+extraType] + VariablesValues['met'+extraType] < SelectionClass.minmTplusMET: passmTCut = False
        if not passmTCut:
          if Debug: print ("DEBUG: Event not passed mT+MET cut (mT+MET == "+str(VariablesValues['mT'+extraType]+VariablesValues['met'+extraType])+" )")
          continue # skip event
    if Debug: print ("DEBUG: Event passed mT cut")
    h_cutflow[Type].Fill(h_cutflow_mT[Type],1)

    ##############################################
    # C6: Select jets and apply OR (if requested)
    ##############################################
    SelectedJets = [] # array of TLorentzVector jets
    bJets        = [] # reco b-tagged jets or truth b-jets
    bJetFound    = False
    nJets        = getNJet(tree) if Type=="reco" else getNJetTruth(tree)
    if Debug: print("DEBUG: Total number of jets = {}".format(nJets))
    for ijet in range(0,nJets): # loop over jets
      jetEta = getRecoJetEta(tree,ijet) if Type=="reco" else getJetEtaTruth(tree,ijet)
      jetPhi = getRecoJetPhi(tree,ijet) if Type=="reco" else getJetPhiTruth(tree,ijet)
      jetPt  = getRecoJetPt (tree,ijet) if Type=="reco" else getJetPtTruth(tree,ijet)
      jetE   = getRecoJetE  (tree,ijet) if Type=="reco" else getJetETruth(tree,ijet)
      if Debug: print ("DEBUG: apply selections to jet (pt={},eta={})".format(jetPt,jetEta))
      if Type == "reco" and SelectionClass.jet_JVTcut:
        if not jetPassJVT(tree,ijet):
          if Debug: print ("DEBUG: Skipping jet (pt={},eta={}) not passing JVT".format(jetPt,jetEta))
          continue # skip pileup jet
      # create an instance of the expanded TLorentzVector class
      TLVjet = iJet()
      TLVjet.SetPtEtaPhiE(jetPt,jetEta,jetPhi,jetE)
      if Type == "reco" and SelectionClass.jet_JVTcut and useSFs: TLVjet.SF *= getJVTSF(tree,ijet) # JVT SF
      jetRapidity = TLVjet.Rapidity()
      # kinematic selection
      if jetPt > SelectionClass.jet_minPt and abs(jetRapidity) < SelectionClass.jet_maxRapidity:
        if Type == "reco":
          if getJetBTag(tree,ijet,Tagger):
            bJetFound         = True
            TLVjet.isBjet     = True
            bJets.append(TLVjet)
            if Debug: print ("DEBUG: Jet (pt={}) is b-tagged".format(jetPt))
            #if SelectionClass.bjetVeto and useSFs: TLVjet.SF = getJetBTagSF(tree,ijet,Tagger) # FIXME (should I use b-tagging SFs for bjet veto?)
        SelectedJets.append(TLVjet)
      else:
        if Debug: print ("DEBUG: Skipping jet (pt={},rapidity={}) not passing pt-rapidity selection".format(jetPt,jetRapidity))

    # Apply OR (event-level selection and remotion of jets overlapping selected leptons)
    if SelectionClass.applyOR:
      passOR,SelectedJets,dRs = applyOR(SignalLepton,SelectedJets)
      if not passOR:
        if Debug: print ("DEBUG: Event not passed Overlap Removal, DeltaR values:")
        if Debug: print(dRs)
        continue # skip event
      else:
        if Debug: print ("DEBUG: Event passed Overlap Removal, DeltaR values:")
        if Debug: print(dRs)
      h_cutflow[Type].Fill(h_cutflow_OR[Type],1)

    # Discard events with no selected jets (if requested)
    if SelectionClass.jet_atleastOne and len(SelectedJets) == 0:
      if Debug: print ("DEBUG: Event not passed at least one jet selection")
      continue # skip event
    if SelectionClass.jet_atleastOne and Debug: print ("DEBUG: Event passed the jet selection")
    else:
      if Debug: print ("DEBUG: Jets selected")
    h_cutflow[Type].Fill(h_cutflow_jet[Type],1)

    ############
    # Get SFs
    ############
    if Type == "reco":
      # Lepton SF
      LeptonSF = 1
      if useSFs:
        LeptonSF *= SignalLepton.SF
      # Jet SF
      JetSF = 1
      if useSFs:
        for jet in SelectedJets:
          JetSF *= jet.SF
      # Final SF
      TotalSF = LeptonSF * JetSF
      weight *= TotalSF

    # Get njets observable
    nSelectedJets = len(SelectedJets)

    ########################################
    # Fill Significance Study Hists if asked
    ########################################
    if SelectionClass.doSignificanceStudy and Type is 'reco':
      mycounter = 0
      for variation in sig_variations: # loop over selection variations
        ###########################################
	# Apply corresponding b-jet veto selection
        ###########################################
        # nominal b-jet veto when njet>2
        if variation is 'bjetVeto' and len(SelectedJets)>2 and bJetFound: continue
        # b-jet veto when njet>0 (for all selected jets)
        elif variation is 'allbjetVeto' and bJetFound: continue
        #########################################
        # Fill histograms for Significance Study
        #########################################
        # Wmass (mT)
        Histograms['mT_'+variation].Fill( VariablesValues['mT'], weight )
        # Njet
        Histograms['njet_'+variation].Fill( nSelectedJets, weight )
        # Variables to compute HT, scalar sum of jet and lep pT
        SumPt_jets     = 0
        atLeastTwoJets = True if nSelectedJets > 1 else False
        for ijet in range(0,nSelectedJets): # loop over selected jets
          SumPt_jets += SelectedJets[ijet].Pt()
        # HT
        Histograms['ht_'+variation].Fill( SumPt_jets + SignalLepton.Pt(), weight )
        # MET
        Histograms['met_'+variation].Fill( VariablesValues['met'], weight )
        # Fill 2D hists MET, MTW
        Histograms['met_mtw_'+variation].Fill( VariablesValues['met'], VariablesValues['mT'], weight )
        mycounter += 1

    ############################
    # C6: Event b-jet selection
    ############################
    if Type == "reco": # b-tagging selection (not needed for truth events)
      if SelectionClass.bjetVeto and len(SelectedJets)>2: # no b-jet in the event if 3 or more jets
        if bJetFound:
          if Debug: print ("DEBUG: Event not passed b-jet veto")
          continue # skip event
      if Debug: print ("DEBUG: Event passed the b-jet selection")
      h_cutflow[Type].Fill(h_cutflow_bTagging[Type],1)

    # Classify event by jet multiplicity
    if nSelectedJets < 6 : nJetFlag = 'e{0}jet_'.format(nSelectedJets)
    else: nJetFlag = 'gt5jet_'

    ##################################
    # Print event info (if requested)
    ##################################
    if PrintInfo and Type == 'reco':
      print ("#################################################################################")
      print ("EVENTINFO: EventNumber: "+str(tree.eventNumber))
      if MC:
        print ("EVENTINFO: mcChannelNumber: {}".format(tree.mcChannelNumber))
        print ("EVENTINFO: mcEventWeight: {}".format(tree.mcEventWeights[NominalWeightIndex]))
        print ("EVENTINFO: AMIxss: {}".format(AMIxss[tree.mcChannelNumber]))
        print ("EVENTINFO: AMIeff: {}".format(AMIeff[tree.mcChannelNumber]))
        print ("EVENTINFO: AMIk: {}".format(AMIk[tree.mcChannelNumber]))
        print ("EVENTINFO: sumWeights: {}".format(round(sumWeights[tree.mcChannelNumber],2)))
        print ("EVENTINFO: weight_pileup: {}".format(round(tree.weight_pileup,2)))
      print ("EVENTINFO: nJets: "+str(nSelectedJets))
      for ijet in range(0,nSelectedJets): # loop over selected jets
        print ("EVENTINFO: jet({}) pt: {}".format(ijet,round(SelectedJets[ijet].Pt(),2)))
        print ("EVENTINFO: jet({}) eta: {}".format(ijet,round(SelectedJets[ijet].Eta(),2)) )
	#if MC: #fixme
        #  print ("EVENTINFO: jet({}) jvtSF: {}".format(ijet,round(JetSF,2)))
      print ("EVENTINFO: lep pt: {}".format(round(SignalLepton.Pt(),2)))
      print ("EVENTINFO: lep eta: {}".format(round(SignalLepton.Eta(),2)))
      print ("EVENTINFO: mT: {}".format(round(VariablesValues['mT'+extraType],2)))
      print ("EVENTINFO: MET: {}".format(round(VariablesValues['met'+extraType],2)))


    ########################################################
    # Get Pescaled Corrected Luminosity based on electron pT
    # Divide MC in CR by corrected luminosity
    ########################################################
    #corrected_lumi = 1
    #signal_lep_pt = SignalLepton.Pt()
    #if Selection == "CR" and MC:
    #  if mf_passedTrigger == "": continue
    #  corrected_lumi = PrescaleWeights[mf_passedTrigger]
    #  #print(" >>> mf_passedTrigger = "+mf_passedTrigger + "correcte_lumi = "+str(corrected_lumi))
    #  weight = weight/corrected_lumi

    ##############################
    # Fill 1D distributions
    ##############################
    if Debug: print ("DEBUG: Filling 1D histograms")
    if Type == "reco":  passReco  = True
    if Type == "truth": passTruth = True

    # Average/actual number of interaction per crossing
    if Type == "reco": # Fill once !
      #h_correctedAndScaledAverageMu.Fill( correctedAndScaledAverageMu, weight )
      #h_averageInteractionsPerCrossing.Fill( averageInteractionsPerCrossing, weight )
      h_actualInteractionsPerCrossing.Fill( actualInteractionsPerCrossing, weight )
      #h_correctedAndScaledActualMu.Fill( correctedAndScaledActualMu, weight )
      #h_correctedAverageMu.Fill( correctedAverageMu, weight )
      #h_correctedActualMu.Fill( correctedActualMu, weight )
 
    # Classify event by mu value
    # using correctedAndScaledAverageMu/ActualMu for 2015+2016/2017+2018
    #muToCheck = correctedAndScaledAverageMu if "2015" in args.path or "2016" in args.path or "MC16a" in args.path else correctedAndScaledActualMu
    muToCheck = actualInteractionsPerCrossing if "2015" in args.path or "2016" in args.path or "MC16a" in args.path else actualInteractionsPerCrossing
    muFlag    = 'lowmu_' if muToCheck < 30 else 'highmu_'

    # Wmass (mT)
    if Type == "reco":
      Histograms['mT'+extraType].Fill( VariablesValues['mT'+extraType], weight )
      Histograms[nJetFlag+'mT'+extraType].Fill( VariablesValues['mT'+extraType], weight )

    # Fill jet distributions
    VariablesValues['njet'+extraType] = nSelectedJets
    Histograms['njet'+extraType].Fill( VariablesValues['njet'+extraType], weight )
    SumPt_jets     = 0 # to compute HT
    atLeastTwoJets = True if nSelectedJets > 1 else False
    for ijet in range(0,nSelectedJets): # loop over selected jets
      SumPt_jets += SelectedJets[ijet].Pt()
      jetPt       = SelectedJets[ijet].Pt()
      jetEta      = SelectedJets[ijet].Eta()
      jetPhi      = SelectedJets[ijet].Phi()
      jetE        = SelectedJets[ijet].E()
      jetY        = SelectedJets[ijet].Rapidity()
      # Fill inclusive jet kinematic distributions
      Histograms['jet_pt'+extraType] .Fill( jetPt, weight )
      Histograms['jet_eta'+extraType].Fill( jetEta, weight )
      Histograms['jet_y'+extraType]  .Fill( jetY, weight )
      Histograms['jet_phi'+extraType].Fill( jetPhi, weight )
      # Fill exclusive jet kinematic distributions
      Histograms[nJetFlag+'jet_pt'+extraType].Fill( jetPt, weight )
      Histograms[nJetFlag+'jet_eta'+extraType].Fill( jetEta, weight )
      Histograms[nJetFlag+'jet_y'+extraType].Fill( jetY, weight )
      Histograms[nJetFlag+'jet_phi'+extraType].Fill( jetPhi, weight )
      deltaRjlep = SelectedJets[ijet].DeltaR(SignalLepton)
      Histograms['deltaRjlep'+extraType].Fill( deltaRjlep, weight)
      Histograms[nJetFlag+'deltaRjlep'+extraType].Fill( deltaRjlep, weight)
      # Fill leading, sub-leading and third-leading distributions
      if ijet < 3:
        Histograms['j'+str(ijet)+'_pt'+extraType] .Fill( jetPt,  weight )
        Histograms['j'+str(ijet)+'_eta'+extraType].Fill( jetEta, weight )
        Histograms['j'+str(ijet)+'_y'+extraType]  .Fill( jetY,   weight )
        Histograms['j'+str(ijet)+'_phi'+extraType].Fill( jetPhi, weight )
        Histograms[nJetFlag+'j'+str(ijet)+'_pt'+extraType] .Fill( jetPt,  weight )
        Histograms[nJetFlag+'j'+str(ijet)+'_eta'+extraType].Fill( jetEta, weight )
        Histograms[nJetFlag+'j'+str(ijet)+'_y'+extraType]  .Fill( jetY,   weight )
        Histograms[nJetFlag+'j'+str(ijet)+'_phi'+extraType].Fill( jetPhi, weight )
        for ptbin in range(0,len(pTbins)):
          ptmin = getPtBinMin(pTbins,ptbin)
          ptmax = getPtBinMax(pTbins,ptbin)
          if jetPt >= ptmin and jetPt < ptmax:
            ptbinstr = '__pt_'+str(ptmin)+'_'+str(ptmax)
            Histograms['j'+str(ijet)+'_eta'+ptbinstr+extraType].Fill( jetEta, weight )
    # Fill dijet distributions
    if atLeastTwoJets:
      VariablesValues['mjj'+extraType]        = (SelectedJets[0]+SelectedJets[1]).M()
      VariablesValues['deltaYjj'+extraType]   = abs(SelectedJets[0].Rapidity() - SelectedJets[1].Rapidity())
      VariablesValues['deltaPhijj'+extraType] = abs(SelectedJets[0].DeltaPhi(SelectedJets[1]))
      VariablesValues['deltaRjj'+extraType]   = SelectedJets[0].DeltaR(SelectedJets[1])
      Histograms['mjj'+extraType]       .Fill( VariablesValues['mjj'+extraType],        weight )
      Histograms['deltaYjj'+extraType]  .Fill( VariablesValues['deltaYjj'+extraType],   weight )
      Histograms['deltaPhijj'+extraType].Fill( VariablesValues['deltaPhijj'+extraType], weight )
      Histograms['deltaRjj'+extraType]  .Fill( VariablesValues['deltaRjj'+extraType],   weight )
      Histograms[nJetFlag+'mjj'+extraType]       .Fill( VariablesValues['mjj'+extraType],        weight )
      Histograms[nJetFlag+'deltaYjj'+extraType]  .Fill( VariablesValues['deltaYjj'+extraType],   weight )
      Histograms[nJetFlag+'deltaPhijj'+extraType].Fill( VariablesValues['deltaPhijj'+extraType], weight )
      Histograms[nJetFlag+'deltaRjj'+extraType]  .Fill( VariablesValues['deltaRjj'+extraType],   weight )

    # Fill lepton distributions
    Histograms['lep_pt'+extraType] .Fill( SignalLepton.Pt(),  weight )
    Histograms['lep_eta'+extraType].Fill( SignalLepton.Eta(), weight )
    Histograms['lep_phi'+extraType].Fill( SignalLepton.Phi(), weight )
    Histograms[nJetFlag+'lep_pt'+extraType] .Fill( SignalLepton.Pt(),  weight )
    Histograms[nJetFlag+'lep_eta'+extraType].Fill( SignalLepton.Eta(), weight )
    Histograms[nJetFlag+'lep_phi'+extraType].Fill( SignalLepton.Phi(), weight )

    # MET
    if Type == "reco":
      Histograms['met'+extraType].Fill( VariablesValues['met'+extraType], weight )
      Histograms[nJetFlag+'met'+extraType].Fill( VariablesValues['met'+extraType], weight )
      Histograms[muFlag+'met'+extraType].Fill( VariablesValues['met'+extraType], weight )
      Histograms[nJetFlag+muFlag+'met'+extraType].Fill( VariablesValues['met'+extraType], weight )

    # HT
    Histograms['ht'+extraType].Fill( SumPt_jets + SignalLepton.Pt(), weight )
    Histograms[nJetFlag+'ht'+extraType].Fill( SumPt_jets + SignalLepton.Pt(), weight )

    # Exclusive njet
    Histograms[nJetFlag+'njet'+extraType].Fill( nSelectedJets, weight )

  ##############################
  # Fill 2D distributions
  ##############################
  if makeTMs:
    if passReco and passTruth:
      if Debug: print ("DEBUG: Filling 2D histograms")
      for obs in Observables:
        if obs in VariablesValues and obs+'_truth' in VariablesValues: Histograms_2D[obs].Fill( VariablesValues[obs], VariablesValues[obs+'_truth'], weight )
    else:
      if Debug: print ("DEBUG: Event did not pass simultaneuously reco and truth selections")
      if Debug and passReco:  print ("DEBUG: Event passed reco selections")
      if Debug and passTruth: print ("DEBUG: Event passed truth selections")

if Debug: printMemory(2)
##################################
# Write histograms to a ROOT file
##################################
outFile = TFile(OutName,"RECREATE")
if MC:
  h_mcEventWeight.Write()
for Type in Types:
  h_cutflow[Type].Write()
  if Type == "reco":
     #h_correctedAndScaledAverageMu.Write()
     #h_averageInteractionsPerCrossing.Write()
     h_actualInteractionsPerCrossing.Write()
     #h_correctedAndScaledActualMu.Write()
     #h_correctedAverageMu.Write()
     #h_correctedActualMu.Write()
  for key in Histograms: Histograms[key].Write()
if makeTMs:
  for key in Histograms_2D: Histograms_2D[key].Write()
outFile.Close()
print ("Histograms saved to "+OutName)
if Debug: printMemory(3)
print (">>> DONE <<<")
