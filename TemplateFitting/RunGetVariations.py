
CRdef = 'CR' # options: CR and CRmed

doSystematics = "yes" # if set to True, then systematic variations from MC templates
# are included before the MJ fit estimation and syst + stat error summed in quadrature

#################################
# Flags to set are above
# Steering code is below
#################################

import os,sys,copy
sys.path.append("../xAHReader/Plotter/")
sys.path.append("../xAHReader/")

from Defs import *
from Arrays import nJetmultiplicities, muFlags
from SystematicsNames import Systematics

# Clean and Make directories for FitterOutputs, Plots, and Logs
os.system('mkdir Logs FitterOutputs Plots VariationOutputs')
#os.system('mkdir Logs/'+CRdef+' FitterOutputs/'+CRdef+' Plots/'+CRdef)
#os.system('rm Logs/'+CRdef+'/* Plots/'+CRdef+'/* FitterOutputs/'+CRdef+'/*')

if doSystematics == "yes":
  os.system('mkdir Logs/Variations Plots/Variations')
  os.system('rm Logs/Variations/* Plots/Variations/* VariationOutputs/*')
  

# Make list of datasets (combination of all data years listed in Defs.py)
YearCombinations = []
AllYears         = []
for year in DataSets:
  YearCombinations.append([year])
  AllYears.append(year)
if len(YearCombinations) > 1:  YearCombinations.append(AllYears) 
extra = '_closureTest' if ClosureTest else ''

# if doSystematics, then calculate delta betweeen nominal and variation True template, for each systematic
if doSystematics == 'yes':
  command_sys = ''
  for Datasets in YearCombinations:
    DataPeriod = ''
    for year in Datasets: DataPeriod += year
    # Loop over njet cases 
    for case in nJetCases:
      mu = 'Inclusive'
      command_sys += 'python GetTemplateSystVariations.py --years '+DataPeriod+' --njetFlag '+case+' --muFlag '+mu+' > Logs/Variations/Data'+DataPeriod+'_njet'+case+'_mu'+mu+' 2>&1 && '
  command_sys = command_sys[:-2]
  print(command_sys)
  os.system(command_sys)

