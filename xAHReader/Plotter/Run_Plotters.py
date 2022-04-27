
####################################################################
#                                                                  #
# Purpose: Run Data_vs_MC.py and MCplots.py                        #
# Author : Christina Nelson                                        #
#                                                                  #
####################################################################

DataSamples = [
  'Signal_data15',
  'Signal_data16',
  'Signal_data17',
  'Signal_data18',
]

Backgrounds = [
  'Top',
  'Diboson',
#  'Ztautau',
  'Zee',
#  'Wtaunu',
]

AltSignals = [
#  'MGPy8', # MadGraph Pythia8
#  'S2210' # Sherpa 2.2.10
]

compareSelections = [
  'bjetVeto',
  'nobjetVeto',
  'allbjetVeto',
]

SignificanceVariables = [
  'met',
  'njet',
  'ht',
  'mT',
  'met_mtw',
]

Channel          = "EL"
Selection        = "SR"
Tagger           = "DL1r"
ATLASlegend      = "Internal" # Options: Internal, Preliminary, ATLAS and NONE
AddMultijet      = 'Exclusive'     # Options: NONE, Inclusive, Exclusive
AddMJexclusive   = True
CompareShapes    = False
CRdef            = 'CR'  # for picking up correct multijet inputs (options: CR or CRmed)
Debug            = False
CalcSignificance = False
MakePlots        = True

###########################################################################
# DO NOT MODIFY
###########################################################################

import os,sys

if not CalcSignificance and not MakePlots:
  print('ERROR: At least one of the following flags should be True: CalcSignificance MakePlots, exiting')
  sys.exit(0)

if AddMultijet != 'NONE' and AddMultijet != 'Inclusive' and AddMultijet != 'Exclusive':
  print('AddMultijet not recognized, exiting')
  sys.exit(0)

# Import things from Reader
sys.path.insert(1, '../') # insert at 1, 0 is the script path
from Arrays import *

# Make final list of samples
Samples = ["Signal_MC"]
for sample in DataSamples: Samples.append(sample)
for sample in Backgrounds: Samples.append(sample)
for sample in AltSignals: Samples.append('AltSig'+sample) 

# Create output folders
os.system('mkdir Plots')
if MakePlots:
  os.system('mkdir Plots/'+Selection)
  DataPeriod = 'Data'
  for sample in Samples:
    if 'data15' in sample:
      os.system('mkdir Plots/'+Selection+'/Data15')
      DataPeriod += '15'
    elif 'data16' in sample:
      os.system('mkdir Plots/'+Selection+'/Data16')
      DataPeriod += '16'
    elif 'data17' in sample:
      os.system('mkdir Plots/'+Selection+'/Data17')
      DataPeriod += '17'
    elif 'data18' in sample:
      os.system('mkdir Plots/'+Selection+'/Data18')
      DataPeriod += '18'
  os.system('mkdir Plots/'+Selection+'/'+DataPeriod)
if CalcSignificance: 
  os.system('mkdir -p OutputROOTFiles/Significance')

# Get list of histogram names from xAHReader
HistNames = []
for var in AllVariables: HistNames.append(var)

# Add mu histogram
HistNames.append('correctedAndScaledAverageMu')

# Construct strings with selected samples (each period alone and all together)
samples = []
Full    = ''
for sample in Samples: Full += sample+','
Full = Full[:-1]
samples.append(Full)
import copy
# Get list of MC samples
MCsamples   = copy.deepcopy(Samples)
for sample in Samples:
  if 'data' in sample: MCsamples.remove(sample)
# Get list of data samples
Datasamples = copy.deepcopy(Samples)
for sample in Samples:
  if 'data' not in sample: Datasamples.remove(sample)
for sample in Datasamples:
  string = sample+','
  for MCsample in MCsamples: string += MCsample+','
  string = string[:-1]
  samples.append(string)

# Loop over set of samples
for sample in samples:
  command = ''
  if MakePlots:
    # Run Data_vs_MC.py for each histogram
    for name in HistNames: # loop over histograms
      command += 'python Plotter.py --histname '+name
      command += ' --channel '+Channel
      command += ' --selection '+Selection
      command += ' --tagger '+Tagger
      command += ' --atlas '+ATLASlegend
      command += ' --samples '+sample
      command += ' --CRdef '+CRdef
      command += ' --addMultijet '+AddMultijet
      if CompareShapes:
        command += ' --compareshapes'
      if Debug:
        command += ' --debug'
      command += ' --makeplots'
      command += ' && '
  # Run Calculate Significance for subset of histograms
  if CalcSignificance:
    for sig_name in SignificanceVariables: # loop over histograms
      for study in compareSelections:
        name = sig_name+'_'+study
        command += 'python Plotter.py --histname '+name
        command += ' --channel '+Channel
        command += ' --selection '+Selection
        command += ' --tagger '+Tagger
        command += ' --atlas '+ATLASlegend
        command += ' --samples '+sample
        command += ' --CRdef '+CRdef
        command += ' --addMultijet '+AddMultijet
        if CompareShapes:
          command += ' --compareshapes'
        if Debug:
          command += ' --debug'
        command += ' --calcsignificance'
        command += ' && '

  command = command[:-2]
  os.system(command)
