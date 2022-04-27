####################################################
#                                                  #
# Author: Christina Nelson                         #
# Date:   November 30, 2019                        #
# Submits jobs to HT Condor for efficient          #
# processing of ntuples                            #
####################################################

Channel = "EL" # options: EL and MU
Dataset = "MC16eDijets"
# options: WenuMC16xSherpa, Data15, Data16, Data17, Data18, MC16xTop, MC16xDiboson, MC16axZee (where x = "a", "d" or "e")

# MC Weights (only meaningful for MC, not used at all when running on data)
useSFs           = True # reco, ID, isolation and trigger lepton SFs
useSampleWeights = True # eventWeight * eff * xs / totalevents (sumWeights for Sherpa)
usePRW           = True # pileup reweighting

# Fill Distributions (only meaningful for MC)
fillReco         = True
fillTruth        = True

# Flavour Jet Tagger
Tagger = "DL1r"

# Selection
Selection = "SRwoMET" # options: SR, SRwoMET, CR and Tight

# output path
outputPATH = "/eos/user/l/liformen/christina/W+jets/ReaderOutputs/2022-01-25/"

Test = True

######################################################################
## DO NOT MODIFY
######################################################################

import os,sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')
from Arrays import *

# MC?
MC = False
if "MC" in Dataset:
  MC = True

# Protections
if "EL" not in Channel and "MU" not in Channel:
  print "ERROR: Channel not recognised, exiting"
  sys.exit(0)
if Dataset not in DatasetOptions:
  print "ERROR: Dataset not recognised, exiting"
  sys.exit(0)

# Find all the local Reader's outputs
ROOTfiles = []
AllFiles = os.listdir(outputPATH)
for File in AllFiles:
  if ".root" in File:
    ROOTfiles.append(File)

counter      = 0
scriptsPath  = "../SubmissionScripts/"
localCommand = ""
for File in os.listdir(scriptsPath): # Loop over files
  #print("File = "+File)
  # Skip submissions files that we don't care
  if ".sub" not in File:
    continue
  if Dataset not in File:
    continue
  if Channel not in File:
    continue
  if Selection+'Sel' not in File:
    continue
  if Tagger+"Tag" not in File:
    continue
  if MC:
    if not fillReco and "noReco" not in File:
      continue
    if not fillTruth and "noTruth" not in File:
      continue
    if useSFs and "useSFs" not in File:
      continue
    if not useSFs and "noSFs" not in File:
      continue
    if useSampleWeights and "useSampleWgts" not in File:
      continue
    if not useSampleWeights and "noSampleWgts" not in File:
      continue
    if usePRW and "usePRW" not in File:
      continue
    if not usePRW and "noPRW" not in File:
      continue
  # Check if there is an output already for this job
  ROOTfileFound = False
  FileName      = File.replace("Sel","")
  FileName      = FileName.replace("SampleWgts","SampleWeights")
  FileName      = FileName.replace("Tag","Tagger")
  FileName      = FileName.replace(".sub","")
  #print("Filename = " + FileName)

  for rootFile in ROOTfiles: # Loop over output files    
    #print("rootFile = " + rootFile)
    if FileName in rootFile: # output file for this submission script found
      ROOTfileFound = True
      break
  if ROOTfileFound:
    continue
  counter += 1
  command = "condor_submit "+scriptsPath+File+" &"
  if not Test: os.system(command)
  else: # Print commands to run locally
    FileName = scriptsPath+File.replace(".sub",".sh")
    File     = open(FileName,"r")
    for line in File:
      if "python" in line: localCommand += line + " && "
if Test: print localCommand[:-2]
if counter == 0:
  print "No need to send jobs"
else:
  if not Test: print str(counter)+" jobs will be sent"
  else: print str(counter)+" jobs need to be sent"
