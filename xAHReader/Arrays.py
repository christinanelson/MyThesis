##################################
# Observables and other variables
##################################

# Variables and selection variations for significance studies
sig_variables  = ['mT','njet','ht','met','met_mtw']
sig_variations = ['bjetVeto','nobjetVeto','allbjetVeto']

Observables = [
  'mT',
  'njet',
  'ht'
]

nJetmultiplicities = [
  '', #inclusive in jet multiplicity
  'e0jet',
  'e1jet',
  'e2jet',
  'e3jet',
  'e4jet',
  'e5jet',
  'gt5jet',
]

muFlags = [
  '',
  'lowmu',
  'highmu',
]

import copy
AllVariables = copy.deepcopy(Observables)
AllVariables.append('met')
AllVariables.append('jet_pt')
AllVariables.append('jet_eta')
AllVariables.append('jet_y')
AllVariables.append('jet_phi')
AllVariables.append('j0_pt')
AllVariables.append('j0_eta')
AllVariables.append('j0_y')
AllVariables.append('j0_phi')
AllVariables.append('j1_pt')
AllVariables.append('j1_eta')
AllVariables.append('j1_y')
AllVariables.append('j1_phi')
AllVariables.append('j2_pt')
AllVariables.append('j2_eta')
AllVariables.append('j2_y')
AllVariables.append('j2_phi')
AllVariables.append('mjj')
AllVariables.append('deltaYjj')
AllVariables.append('deltaPhijj')
AllVariables.append('deltaRjj')
AllVariables.append('deltaRjlep')
AllVariables.append('lep_pt')
AllVariables.append('lep_eta')
AllVariables.append('lep_phi')
AllVariables.append('met_mtw')

# pT bins for jet eta distribution
pTbins = ["30:40","70:100","100:150","200:300","500:700","700:1500"]

##################################
# Expected datasets
##################################
MC16campaigns  = ["a","d","e"]
SamplesTypes   = ["WenuMC16xSherpa","WmunuMC16xSherpa","WenuMC16xMGPy","WmunuMC16xMGPy","WenuMC16xPowheg","WmunuMC16xPowheg","Data15","Data16","Data17","Data18","MC16xTop","MC16xDiboson","MC16xZee", "MC16xZmumu", "MC16xZtautau", "MC16xWtaunu", "MC16xDijets", "WenuMC16xMGPy8"]
DatasetOptions = []
for dataset in SamplesTypes:
  if "Data" not in dataset:
    for campaign in MC16campaigns:
      sample = dataset.replace("MC16x","MC16"+campaign)
      DatasetOptions.append(sample)
  else:
    DatasetOptions.append(dataset)

##################################
# Flavour Jet Taggers
##################################
Taggers = ["DL1r"] # "DL1", "MV2c10"
