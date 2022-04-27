from ROOT import *

Colors = [
  kGreen-8,
  kMagenta+1,
  kBlue+1,
  kOrange,
  kPink-7,
  kCyan+1,
  kAzure+1,
]

AltColors = [
  kRed+1,
  kGreen+2,
  kMagenta+2,
  kCyan+3,
  kOrange+10,
  kGray,
  kAzure
]

AltLines = [6,9,8,10]

AltMarkers = [24,21,22,23]

# List of histograms in which Logx will be applied
Logx = [
  'met',
#  "jet_pt",
#  "bjet0_pt",
#  "mu_pt",
]

# List of histograms in which Logy will be applied
Logy = [
  "njet",
  "jet_pt",
  "jet_eta",
  "jet_phi",
  "jet_y",
  "jet_e",
  "j0_pt",
  "j0_eta",
  "j0_phi",
  "j0_e",
  "j1_pt",
  "j2_pt",
  "j1_eta",
  "j1_phi",
  "j2_phi",
  "j1_e",
  "j0_y",
  "j1_y",
  "j2_y",
  "lep_pt",
  "lep_eta",
  "lep_phi",
  "Zmass",
  "Zpt",
  "Zabsy",
  "mjj",
  "deltaYjj",
  "deltaPhijj",
  "deltaRjj",
  "deltaYjlep",
  "deltaPhijlep",
  "deltaRjlep",
  "ht",
  "mT",
  "met",
  "j0_eta__pt_30_40",
  "j1_eta__pt_30_40",
  "j0_eta__pt_100_150",
  "j1_eta__pt_100_150",
  "j0_eta__pt_500_600",
  "j1_eta__pt_500_600",
  "j0_eta__pt_1000_1200",
  "j1_eta__pt_1000_1200",
]

# Axis ranges
XaxisRange = dict()
XaxisRange["jet_pt"]	           = [20,1000]
XaxisRange["lep_pt"]	           = [27,1000]
XaxisRange["Zmass"]	           = [76,106]
XaxisRange["Zpt"]                  = [0,1000]
XaxisRange["Zabsy"]	           = [0,2.5]
XaxisRange["j0_pt"]	           = [20,1000]
XaxisRange["j1_pt"]	           = [20,1000]
XaxisRange["j2_pt"]	           = [20,1000]
XaxisRange["j0_y"]	           = [-3,3]
XaxisRange["j1_y"]	           = [-3,3]
XaxisRange["j2_y"]	           = [-3,3]
XaxisRange["njet"]	           = [0,8]
XaxisRange["j0_eta"]               = [-3,3]
XaxisRange["j0_phi"]               = [-4.5,4.5]
XaxisRange["j0_e"]	           = [20,1000]
XaxisRange["j1_eta"]	           = [-3,3]
XaxisRange["j1_phi"]	           = [-4.5,4.5]
XaxisRange["j1_e"]	           = [20,1000]
XaxisRange["mjj"]	           = [20,1000]
XaxisRange["deltaYjj"]	           = [0,5.0]
XaxisRange["deltaPhijj"]           = [0,3.15]
XaxisRange["deltaRjj"]	           = [0,5.0]
XaxisRange["jet_eta"]              = [-3,3]
XaxisRange["jet_phi"]              = [-4.5,4.5]
XaxisRange["jet_e"]                = [20,1000]
XaxisRange["ht"]                   = [20,1000]
XaxisRange["mT"]                   = [60,500]
XaxisRange["j0_eta__pt_30_40"]     = [-2.5,2.5]
XaxisRange["j1_eta__pt_30_40"]     = [-2.5,2.5]
XaxisRange["j0_eta__pt_100_150"]   = [-2.5,2.5]
XaxisRange["j1_eta__pt_100_150"]   = [-2.5,2.5]
XaxisRange["j0_eta__pt_500_600"]   = [-2.5,2.5]
XaxisRange["j1_eta__pt_500_600"]   = [-2.5,2.5]
XaxisRange["j0_eta__pt_1000_1200"] = [-2.5,2.5]
XaxisRange["j1_eta__pt_1000_1200"] = [-2.5,2.5]
XaxisRange["correctedAndScaledAverageMu"] = [0,70]

# Axis titles
XaxisTitles = dict()
XaxisTitles["jet_pt"]                     = "#it{p}_{T}^{jet} [GeV]"
XaxisTitles["Zmass"]                      = "#it{m} (#mu^{+}#mu^{-}) [GeV]"
XaxisTitles["Zpt"]                        = "#it{p}_{T} (#mu^{+}#mu^{-}) [GeV]"
XaxisTitles["Zabsy"]                      = "|y| (#mu^{+}#mu^{-})"
XaxisTitles["mu_pt"]                      = "#it{p}_{T}^{#mu} [GeV]"
XaxisTitles["mu_phi"]                     = "#phi^{#mu}"
XaxisTitles["mu_eta"]                     = "#eta^{#mu}"
XaxisTitles["el_pt"]                      = "#it{p}_{T}^{e} [GeV]"
XaxisTitles["el_phi"]                     = "#phi^{e}"
XaxisTitles["el_eta"]                     = "#eta^{e}"
XaxisTitles["j0_pt"]                      = "#it{p}_{T}^{lead jet} [GeV]"
XaxisTitles["j1_pt"]                      = "#it{p}_{T}^{sublead jet} [GeV]"
XaxisTitles["j2_pt"]                      = "#it{p}_{T}^{subsublead jet} [GeV]"
XaxisTitles["j0_y"]                       = "#it{y}^{lead jet}"
XaxisTitles["j1_y"]                       = "#it{y}^{sublead jet}"
XaxisTitles["j2_y"]                       = "#it{y}^{subsublead jet}"
XaxisTitles["njet"]                       = "N_{jets}"
XaxisTitles["j0_phi"]                     = "#phi^{lead jet}"
XaxisTitles["j0_eta"]                     = "#it{#eta}^{lead jet}"
XaxisTitles["j0_e"]                       = "#it{E}^{lead jet} [GeV]"
XaxisTitles["j1_phi"]                     = "#phi^{jet1}"
XaxisTitles["j2_phi"]                     = "#phi^{jet2}"
XaxisTitles["j1_eta"]                     = "#it{#eta}^{jet1}"
XaxisTitles["j1_e"]                       = "#it{E}^{jet1} [GeV]"
XaxisTitles["jet_phi"]                    = "#phi^{jet}"
XaxisTitles["jet_y"]                      = "y^{jet}"
XaxisTitles["jet_eta"]                    = "#it{#eta}^{jet}"
XaxisTitles["jet_e"]                      = "#it{E}^{jet} [GeV]"
XaxisTitles["mjj"]                        = "#it{m}_{jj} [GeV]"
XaxisTitles["deltaYjj"]                   = "#Delta y^{jj}"
XaxisTitles["deltaPhijj"]                 = "#Delta #Phi^{jj}"
XaxisTitles["deltaRjj"]                   = "#Delta R^{jj}"
XaxisTitles["deltaYjlep"]                 = "#Delta y^{jlep}"
XaxisTitles["deltaPhijlep"]               = "#Delta #Phi^{jlep}"
XaxisTitles["deltaRjlep"]                 = "#Delta R^{jlep}"
XaxisTitles["ht"]                         = "H_{T} [GeV]"
XaxisTitles["mT"]                         = "m_{T}^{W} [GeV]"
XaxisTitles["met"]                        = "MET [GeV]"
XaxisTitles["j0_eta__pt_30_40"]           = "#it{#eta}^{lead jet}_{30,40}"
XaxisTitles["j1_eta__pt_30_40"]           = "#it{#eta}^{sublead jet}_{30,40}"
XaxisTitles["j0_eta__pt_100_150"]         = "#it{#eta}^{lead jet}_{100,150}"
XaxisTitles["j1_eta__pt_100_150"]         = "#it{#eta}^{sublead jet}_{100,150}"
XaxisTitles["j0_eta__pt_500_600"]         = "#it{#eta}^{lead jet}_{500,600}"
XaxisTitles["j1_eta__pt_500_600"]         = "#it{#eta}^{sublead jet}_{500,600}"
XaxisTitles["j0_eta__pt_1000_1200"]       = "#it{#eta}^{lead jet}_{1000,1200}"
XaxisTitles["j1_eta__pt_1000_1200"]       = "#it{#eta}^{sublead jet}_{1000,1200}"
XaxisTitles["MV2c10Weight"]               = "b-tagging discriminant"
XaxisTitles["MV2c10Weight__pt_30_40"]     = "b-tagging discriminant"
XaxisTitles["MV2c10Weight__pt_100_150"]   = "b-tagging discriminant"
XaxisTitles["MV2c10Weight__pt_500_600"]   = "b-tagging discriminant"
XaxisTitles["MV2c10Weight__pt_1000_1200"] = "b-tagging discriminant"
XaxisTitles["DL1Weight"]                  = "b-tagging discriminant"
XaxisTitles["DL1Weight__pt_30_40"]        = "b-tagging discriminant"
XaxisTitles["DL1Weight__pt_100_150"]      = "b-tagging discriminant"
XaxisTitles["DL1Weight__pt_500_600"]      = "b-tagging discriminant"
XaxisTitles["DL1Weight__pt_1000_1200"]    = "b-tagging discriminant"
XaxisTitles["DL1rWeight"]                 = "b-tagging discriminant"
XaxisTitles["DL1rWeight__pt_30_40"]       = "b-tagging discriminant"
XaxisTitles["DL1rWeight__pt_100_150"]     = "b-tagging discriminant"
XaxisTitles["DL1rWeight__pt_500_600"]     = "b-tagging discriminant"
XaxisTitles["DL1rWeight__pt_1000_1200"]   = "b-tagging discriminant"
XaxisTitles["correctedAndScaledAverageMu"]= "<#mu>"
