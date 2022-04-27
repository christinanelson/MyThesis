# Local Test to run before Submitting Batch jobs to Condor
# Output saved in Testing Directory

#!/usr/bin/env python

import ROOT

import os

# Inputs
InputFiles = [ # path to ROOT files
  "/afs/cern.ch/user/n/nelsonc/work/McGill/WorkingDir_systs_2022/source/MakeTTrees_Wjets/scripts/submitDir_syst/MC16a/"
]
Channel   = "EL" # options: MU or EL
Dataset   = "WenuMC16aSherpa" # options: "WenuMC16xSherpa","WmunuMC16xSherpa","WenuMC16xMGPy8","WmunuMC16xMGPy8","WenuMC16xPowheg","WmunuMC16xPowheg","Data15","Data16","Data17","Data18","MC16xttbar","MC16xSingleTop","MC16xDiboson" (where x = "a", "d" or "e")

# MC Weights (only meaningful for MC, not used at all when running on data)
useSFs           = True  # reco, ID, isolation and trigger lepton SFs
useSampleWeights = True  # eventWeight * eff * xs / totalevents (sumWeights for Sherpa)
usePRW           = True  # pileup reweighting

# Flavour Jet Tagger
Tagger           = "DL1r"

# Selection
Selection = "SRwoMET" # options: SR, CR, Tight and SRGavin

# Distributions
fillReco  = True # fill reco distributions
fillTruth = True # fill truth distributions

# Print event level info
PrintInfo = False

# Debugging
Debug     = False

###################################################
## DO NOT MODIFY
###################################################

readAMI = True

from ROOT import *
import os,sys
from Arrays import *

# Protections
if "EL" not in Channel and "MU" not in Channel:
  print ("ERROR: Channel not recognised, exiting")
  sys.exit(0)
if Dataset not in DatasetOptions:
  print ("ERROR: Dataset not recognised, exiting")
  sys.exit(0)

# MC?
MC = False
if "MC" in Dataset:
  MC = True

if not MC: readAMI = False # data

# Protections
if not MC: # data
  if useSFs:           useSFs           = False
  if useSampleWeights: useSampleWeights = False
  if usePRW:           usePRW           = False
  if fillTruth:        fillTruth        = False

# Run over a single file from the chosen dataset
counter = 0
command = ""
for File in os.listdir(InputFiles[0]): # Loop over files
  if ".root" not in File:
    continue
  if counter > 0:
    break

  # Run test job
  command += "python Reader.py --path "+InputFiles[0]+" --outPATH Testing/ --file "+File+" --channel "+Channel+" --dataset "+Dataset+" --selection "+Selection+" --tagger "+Tagger
  if Debug:
    command += " --debug"
  if not fillTruth:
    command += " --noTruth"
  if readAMI: command += " --readAMI"
  if not fillReco:
    command += " --noReco"
  if not useSFs:
    command += " --noSFs"
  if not useSampleWeights:
    command += " --noSampleWeights"
  if not usePRW:
    command += " --noPRW"
  if PrintInfo:
    command += " --printInfo"
  command += " && "

  counter += 1

command = command[:-2]
os.system(command)
