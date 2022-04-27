# This file prepares all the selected submission scripts for batch jobs to HT Condor.
# Select Channel(s) and Dataset(s)


from Arrays import *

# Channel options: "EL" (electron), "MU" (muon) 
Channels      = ["EL"] #["EL","MU"]

# Dataset options: WenuMC16xSherpa, WmunuMC16xSherpa, WenuMC16xMGPy, WmunuMC16xMGPy, WenuMC16xPowheg, WmunuMC16xPowheg, Data15, Data16, Data17, Data18, MC16xttbar, MC16xSingleTop, MC16xDiboson, MC16xZee (where x = "a", "d" or "e")
Datasets      = [
  "Data18",
  "WenuMC16eSherpa",
  "MC16eTop",
  "MC16eDiboson",
  "MC16eZee",
  "MC16eDijets",
]

# Location where the output ROOT files will be written
outPATH = "/eos/user/l/liformen/christina/W+jets/ReaderOutputs/"
DATE    = '2022-01-25/'

# MC Weights (only meaningful for MC, not used at all when running on data)
useSFs           = True  # reco, ID, isolation and trigger lepton SFs
useSampleWeights = True  # eventWeight * eff * xs / totalevents (sumWeights for Sherpa)
usePRW           = True  # pileup reweighting

# Fill Distributions (only meaningful for MC)
fillReco         = True
fillTruth        = True

# Flavour Jet Tagger
Taggers          = ["DL1r"] # Options: DL1r, DL1

# Selection
Selections       = ["SR", "SRwoMET", "CR"] # options: SR, SRwoMET, CR, Tight, SRLowPtLooseVeto, SRLowPtTightVeto, SRHighPtLooseVeto, SRHighPtTightVeto

# Debugging
Debug     = False

# Re-calculate sample weights
redoWeights = True

###################################################
## DO NOT MODIFY
###################################################

# Final output path
outPATH = outPATH + DATE

print "<<< Creating submission scripts <<<"

from ROOT import *
import os,sys

os.system("rm -r SubmissionScripts/")
os.system("mkdir SubmissionScripts")

from InputLists import Inputs
from HelperFunctions import *
from Dicts import *

# Loop over channels
for Channel in Channels:
  # Loop over taggers
  for Tagger in Taggers:
    # Loop over Selection types
    for Selection in Selections:
      # Loop over datasets
      for Dataset in Datasets:

        # Protections
        if Dataset not in DatasetOptions:
          print "ERROR: Dataset not recognised, exiting"
          sys.exit(0)
        if not Inputs.has_key(Dataset):
          print "ERROR: There are no inputs yet for the dataset provided, exiting"
          sys.exit(0)
	if Channel == 'EL':
          if 'Zmumu' in Dataset or 'Wmunu' in Dataset: continue # skip sample
	elif Channel == 'MU':
          if 'Zemu' in Dataset or 'Wenu' in Dataset: continue # skip sample

        # Select input files for the given dataset
        InputFiles = Inputs[Dataset]

        # MC?
        MC = False
        if "MC" in Dataset:
          MC = True

        ###########################
        # Loop over input files
        ###########################
        for path in InputFiles: # Loop over paths

          if MC:
            DSID = getDSID(path)
          else:
            period = getPeriod(path)

          for File in os.listdir(path): # Loop over files
  
            if ".root" not in File:
              continue

            # Check if TTree exists
            tfile = TFile.Open(path+'/'+File)
            Dir   = tfile.Get("TreeAlgo")
            tree  = Dir.Get("nominal")
            if not tree:
              print "Skipping "+path+'/'+File+' with no TTree'
              continue # empty file

            # Create submission script
            ExtraArgs   = ""
            ScriptName  = Dataset
            if MC:
              ScriptName += "_" + DSID
            else:
              ScriptName += "_" + period
            ScriptName += "_" + Channel + "_" + Selection + "Sel"
            ScriptName += "_" + Tagger + "Tag"
            if MC:
              if useSFs:
                ScriptName += "_useSFs"
              else:
                ScriptName += "_noSFs"
                ExtraArgs  += " --noSFs"
              if useSampleWeights:
                ScriptName += "_useSampleWgts"
              else:
                ScriptName += "_noSampleWgts"
                ExtraArgs  += " --noSampleWeights"
              if usePRW:
                ScriptName += "_usePRW"
              else:
                ScriptName += "_noPRW"
                ExtraArgs  += " --noPRW"
              if not fillTruth:
                ScriptName += "noTruth"
                ExtraArgs  += " --noTruth"
              if not fillReco:
                ScriptName += "noReco"
                ExtraArgs  += " --noReco"
              if redoWeights:
                ExtraArgs  += " --readAMI"

            ScriptName += "_" + File
            outputFile = open("SubmissionScripts/"+ScriptName+".sub","w")
            outputFile.write("executable = ../SubmissionScripts/"+ScriptName+".sh\n")
            outputFile.write("input      = FilesForSubmission.tar.gz\n")
            outputFile.write("output     = Logs/"+DATE+Selection+'/'+ScriptName+".$(ClusterId).$(ProcId).out\n")
            outputFile.write("error      = Logs/"+DATE+Selection+'/'+ScriptName+".$(ClusterId).$(ProcId).err\n")
            outputFile.write("log        = Logs/"+DATE+Selection+'/'+ScriptName+".$(ClusterId).log\n")
            #outputFile.write("RequestMemory   = 6000\n")
            #outputFile.write("RequestCpus = 4\n")
            #outputFile.write("+JobFlavour = 'tomorrow'\n")
            outputFile.write("transfer_output_files = \"\" \n")
            outputFile.write('+JobFlavour = "tomorrow"\n')
            outputFile.write("arguments  = $(ClusterId) $(ProcId)\n")
            outputFile.write("queue")
            outputFile.close()

            # Create bash script which will run the Reader
            outputFile = open("SubmissionScripts/"+ScriptName+".sh","w")
            outputFile.write("#!/bin/bash\n")
            outputFile.write("tar xvzf FilesForSubmission.tar.gz\n")
            outputFile.write("export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n") # for setupATLAS
            outputFile.write("source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n") # setupATLAS
            outputFile.write("lsetup 'root 6.14.04-x86_64-slc6-gcc62-opt'\n")
            outputFile.write("python Reader.py --path "+path+" --outPATH "+outPATH+" --file "+File+" --channel "+Channel+" --dataset "+Dataset+" --selection "+Selection+ExtraArgs+" --tagger "+Tagger)
            outputFile.close()

print "<<< All DONE <<<"
