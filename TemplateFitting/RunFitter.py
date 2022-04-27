
CRdef = 'CR' # options: CR and CRmed

#################################
# Do no modify (below this line)
#################################

import os,sys,copy
from Defs import *

sys.path.append("../xAHReader_nominal/Plotter/")
sys.path.append("../xAHReader_nominal/")

os.system('mkdir Logs FitterOutputs Plots')
os.system('mkdir Logs/'+CRdef+' FitterOutputs/'+CRdef+' Plots/'+CRdef)
os.system('rm Logs/'+CRdef+'/* Plots/'+CRdef+'/* FitterOutputs/'+CRdef+'/*')

# Import lists from Arrays                                                                                                          
from Arrays import nJetmultiplicities, muFlags

# Make list of datasets (combination of all data years listed in DataSets list from Defs.py)
YearCombinations = []
AllYears         = []
for year in DataSets:
  YearCombinations.append([year])
  AllYears.append(year)
YearCombinations.append(AllYears) 

extra = '_closureTest' if ClosureTest else ''

# Loop over year combinations (each year individually and all together)
command = ''
for Datasets in YearCombinations:
  DataPeriod = ''
  for year in Datasets: DataPeriod += year
  # Loop over njet cases (FIXME add mu flag loop)
  for case in nJetCases:
    mu = 'Inclusive' # Temporary FIXME
    command += 'python TemplateFits.py --years '+DataPeriod+' --njetFlag '+case+' --muFlag '+mu+' --CRdef '+CRdef+' > Logs/'+CRdef+'/Data'+DataPeriod+'_njet'+case+'_mu'+mu+extra+' 2>&1 && '
command = command[:-2]
print(command)
os.system(command)


