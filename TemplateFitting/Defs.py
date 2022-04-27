#######################################################################
# Common defs for TemplateFits.py and PrepareMultijetDistributions.py
#######################################################################

from ROOT import *

# Rebin histograms?
Rebin = False

# Min MET cut in SR
minMET = 25

# Tagger
Tagger = "DL1r"

# Data years
DataSets = ["15"] #, "16", "17", "18"] # "15", "16","17","18"

# List of MC backgrounds
Backgrounds = [
  'Top',
  'Diboson',		
  'Zee',
#  'Ztautau',
#  'Wtaunu',
]

# Will fit pseudo-data generated from the model
ClosureTest = False

# Increase verbosity
Debug = False

# Name of observable used for templates and to fit in data
HistName = "met"

# Type of fits needed based on njet events
nJetCases = [
#  'Inclusive',
  'a1jet',
#  'a2jet',
#  'e0jet',
  'e1jet',
  'e2jet',
  'e3jet',
  'e4jet',
  'e5jet',
  'gt5jet',
]

# Variables/observables which we get a multijet estimation for
Observables = {
  # Need to use full met distribution
  "ht"         : "a0jet", 
  "mT"         : "a0jet",
  "njet"       : "a0jet",
  "met"        : "a0jet", 
  # Need to sum axjet met distributions for x>0
  "j0_pt"      : "a1jet",
  # Need to sum axjet met distributions for x>1
  "j1_pt"      : "a2jet",
  "mjj"        : "a2jet",
  "deltaYjj"   : "a2jet",
  "deltaPhijj" : "a2jet",
  "deltaRjj"   : "a2jet",
}
#  "j0_y", # empty histogram in data_CR?
#  "j1_pt",
#  "j1_y", # empty histogram in data_CR?
#  "lep_pt",
#  "lep_eta",
#  "lep_phi",
#  "deltaRjlep",
#  "jet_pt",
#  "jet_y", # empty histogram in data_CR?
#  "jet_phi",

# Colors for plots
Colors = [kOrange,kCyan+1,kPink-6,kOrange-6]

