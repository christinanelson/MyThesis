# Merges Condor Outputs into Single Distribution for plotting the histogram.

Channel       = "EL"   # options: EL and MU
Datasets      = [ # options: WenuMC16xSherpa, Data15, Data16, Data17, Data18, MC16xTop, MC16xZee, MC16xDiboson (where x = "a", "d" or "e")
  "WenuMC16eSherpa",
#  "Data15",
#  "Data16",
#  "Data17",
  "Data18",
  "MC16eZee",
  "MC16eTop",
  "MC16eDiboson",
  "MC16eDijets",
]

# MC Weights (only meaningful for MC, not used at all when running on data)
useSFs           = True # reco, ID, isolation and trigger lepton SFs
useSampleWeights = True # eventWeight * eff * xs / totalevents (sumWeights for Sherpa)
usePRW           = True

# Flavour Jet Tagger
Tagger = "DL1r"

# Selection
Selection = "CR" # options: SR, SRGavin, CR

# Path to condor outputs
Date = "2022-01-25"
PATH = "/eos/user/l/liformen/christina/W+jets/ReaderOutputs/2022-01-25/"
       
# Path to plotter inputs
PlotterInputsPATH = "/eos/user/n/nelsonc/W+jets/PlotterInputs/2022-01-25/"

######################################################################
## DO NOT MODIFY
######################################################################

import os,sys

command = ""

for Dataset in Datasets:
  # MC?
  MC = False
  if "MC" in Dataset:
    MC = True

  command  = "hadd "+PlotterInputsPATH
  command += Dataset+"_"+Channel+"_"+Selection+"_"+Tagger+"Tagger"
  if MC:
    command += "_"
    if useSFs:
      command += "useSFs"
    else:
      command += "noSFs"
    command += "_"
    if useSampleWeights:
      command += "useSampleWeights"
    else:
      command += "noSampleWeights"
    command += "_"
    if usePRW:
      command += "usePRW"
    else:
      command += "noPRW"
  command += "_All_"+Date+".root "+PATH
  command += Dataset+"_*_"
  command += Channel
  command += "_"+Selection
  command += "_"+Tagger+"Tagger"
  if MC:
    command += "_"
    if useSFs:
      command += "useSFs"
    else:
      command += "noSFs"
    command += "_"
    if useSampleWeights:
      command += "useSampleWeights"
    else:
      command += "noSampleWeights"
    command += "_"
    if usePRW:
      command += "usePRW"
    else:
      command += "noPRW"
  command += "_*.root"
  os.system(command)
