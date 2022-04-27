#################################
# Steering code is below
#################################

import os,sys,copy
sys.path.append("../xAHReader/Plotter/")
sys.path.append("../xAHReader/")

from Defs import *
from Arrays import nJetmultiplicities, muFlags
from SystematicsNames import Systematics

# Clean and Make directories for FitterOutputs, Plots, and Logs
os.system('mkdir Logs')
os.system('mkdir Logs/SR_ratios/')
os.system('rm Logs/SR_ratios/*')


# Make list of datasets (combination of all data years listed in Defs.py)
YearCombinations = []
AllYears         = []
for year in DataSets:
  YearCombinations.append([year])
  AllYears.append(year)
if len(YearCombinations) > 1:  YearCombinations.append(AllYears) 
extra = '_closureTest' if ClosureTest else ''


command = ''
for Datasets in YearCombinations:
  DataPeriod = ''
  for year in Datasets: DataPeriod += year
  # Loop over njet cases (FIXME add mu flag loop)
  for case in nJetCases:
    mu = 'Inclusive' # Temporary FIXME
    command += 'python GetSR_MC-Data_ratios.py --years '+DataPeriod+' --njetFlag '+case+' --muFlag '+mu+' > Logs/SR_ratios/Data'+DataPeriod+'_njet'+case+'_mu'+mu+extra+' 2>&1 && '
command = command[:-2]
print(command)
os.system(command)

