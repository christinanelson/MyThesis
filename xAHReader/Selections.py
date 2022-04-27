# Common selections
class Common:
  def __init__(self):
    # Impact parameter cuts
    self.ElectronMaxAbsd0sig           = 5
    self.ElectronMaxAbsdeltaz0sintheta = 0.5
    self.MuonMaxAbsd0sig               = 3
    self.MuonMaxAbsdeltaz0sintheta     = 0.5
    # Unprescaled triggers
    # Single muon triggers
    self.Unprescaled_MUTriggers_2015 = [] #"HLT_mu20_iloose_L1MU15","HLT_mu50"]
    self.Unprescaled_MUTriggers_2016 = [] #"HLT_mu26_ivarmedium","HLT_mu50"]
    self.Unprescaled_MUTriggers_2017 = [] #"HLT_mu26_ivarmedium","HLT_mu50"]
    self.Unprescaled_MUTriggers_2018 = [] #"HLT_mu26_ivarmedium","HLT_mu50"]
    # Single electron triggers
    self.Unprescaled_ELTriggers_2015 = ['HLT_e24_lhmedium_L1EM20VH','HLT_e60_lhmedium','HLT_e120_lhloose']
    self.Unprescaled_ELTriggers_2016 = ['HLT_e26_lhtight_nod0_ivarloose','HLT_e60_lhmedium_nod0','HLT_e140_lhloose_nod0','HLT_e300_etcut']
    self.Unprescaled_ELTriggers_2017 = ['HLT_e26_lhtight_nod0_ivarloose','HLT_e60_lhmedium_nod0','HLT_e140_lhloose_nod0','HLT_e300_etcut']
    self.Unprescaled_ELTriggers_2018 = ['HLT_e26_lhtight_nod0_ivarloose','HLT_e60_lhmedium_nod0','HLT_e140_lhloose_nod0','HLT_e300_etcut']
    # Prescaled electron (lhvloose) triggers to get a background-enriched sample (https://twiki.cern.ch/twiki/bin/viewauth/Atlas/TriggerNamingRun2#Electron_Dictionary)
    self.Prescaled_ELTriggers_2015 = ['HLT_e26_lhvloose_nod0_L1EM20VH','HLT_e25_lhvloose_L1EM15','HLT_e30_lhvloose_L1EM15','HLT_e40_lhvloose_L1EM15','HLT_e50_lhvloose_L1EM15','HLT_e70_lhvloose','HLT_e80_lhvloose','HLT_e100_lhvloose','HLT_e40_lhvloose','HLT_e60_lhvloose','HLT_e40_lhvloose_nod0','HLT_e60_lhvloose_nod0','HLT_e26_lhvloose_L1EM20VH']
    self.Prescaled_ELTriggers_2016 = ['HLT_e26_lhvloose_nod0_L1EM20VH','HLT_e25_lhvloose_L1EM15','HLT_e30_lhvloose_L1EM15','HLT_e40_lhvloose_L1EM15','HLT_e50_lhvloose_L1EM15','HLT_e70_lhvloose','HLT_e80_lhvloose','HLT_e100_lhvloose','HLT_e40_lhvloose','HLT_e60_lhvloose','HLT_e40_lhvloose_nod0','HLT_e60_lhvloose_nod0','HLT_e26_lhvloose_L1EM20VH','HLT_e28_lhvloose_nod0_L1EM20VH']
    self.Prescaled_ELTriggers_2017 = ['HLT_e25_lhvloose_nod0_L1EM15'] #'HLT_e24_lhvloose_nod0_L1EM20VH','HLT_e25_lhvloose_nod0_L1EM15','HLT_e26_lhvloose_nod0_L1EM20VH','HLT_e28_lhvloose_nod0_L1EM20VH','HLT_e30_lhvloose_nod0_L1EM15','HLT_e40_lhvloose_nod0_L1EM15','HLT_e50_lhvloose_nod0_L1EM15','HLT_e60_lhvloose_nod0','HLT_e70_lhvloose_nod0_L1EM24VHIM','HLT_e80_lhvloose_nod0_L1EM24VHIM','HLT_e100_lhvloose_nod0_L1EM24VHIM','HLT_e120_lhvloose_nod0_L1EM24VHIM','HLT_e140_lhvloose_nod0_L1EM24VHIM','HLT_e160_lhvloose_nod0_L1EM24VHIM']
    self.Prescaled_ELTriggers_2018 = ['HLT_e20_lhvloose_nod0_L1EM12','HLT_e24_lhvloose_nod0_L1EM20VH','HLT_e25_lhvloose_nod0_L1EM15','HLT_e26_lhvloose_nod0_L1EM22VH','HLT_e28_lhvloose_nod0_L1EM22VH','HLT_e30_lhvloose_nod0_L1EM15','HLT_e40_lhvloose_nod0_L1EM15','HLT_e50_lhvloose_nod0_L1EM15','HLT_e60_lhvloose_nod0','HLT_e70_lhvloose_nod0_L1EM24VHIM','HLT_e80_lhvloose_nod0_L1EM24VHIM','HLT_e100_lhvloose_nod0_L1EM24VHIM','HLT_e120_lhvloose_nod0_L1EM24VHIM','HLT_e140_lhvloose_nod0_L1EM24VHIM','HLT_e160_lhvloose_nod0_L1EM24VHIM']
    # Prescaled muon triggers to get a background-enriched sample
    self.Prescaled_MUTriggers_2015 = []#'HLT_mu0_perf', 'HLT_mu20_L1MU15', 'HLT_mu24_iloose_L1MU15', 'HLT_mu4', 'HLT_mu6', 'HLT_mu24_imedium', 'HLT_mu26_imedium', 'HLT_mu40', 'HLT_mu26', 'HLT_mu24', 'HLT_mu22', 'HLT_mu20', 'HLT_mu24_L1MU15', 'HLT_mu18', 'HLT_mu10', 'HLT_mu11', 'HLT_mu14', 'HLT_mu14_iloose']
    self.Prescaled_MUTriggers_2016 = []#'HLT_mu18', 'HLT_mu0_perf', 'HLT_mu20_ivarmedium_L1MU15', 'HLT_mu20_L1MU15', 'HLT_mu24_ivarmedium', 'HLT_mu4', 'HLT_mu6', 'HLT_mu20_imedium_L1MU10', 'HLT_mu24_imedium', 'HLT_mu20_iloose_L1MU15', 'HLT_mu24_ivarloose', 'HLT_mu32_ivarmedium', 'HLT_mu60', 'HLT_mu20_ivarloose_L1MU15', 'HLT_mu28_imedium', 'HLT_mu20_imedium_L1MU15', 'HLT_mu24_iloose', 'HLT_mu40', 'HLT_mu26', 'HLT_mu24', 'HLT_mu22', 'HLT_mu20', 'HLT_mu14_ivarloose', 'HLT_mu10', 'HLT_mu14', 'HLT_mu28_ivarmedium', 'HLT_mu20_ivarmedium_L1MU10', 'HLT_mu26_imedium', 'HLT_mu14_iloose']
    self.Prescaled_MUTriggers_2017 = []#'HLT_mu0_perf', 'HLT_mu10', 'HLT_mu24_ivarmedium', 'HLT_mu4', 'HLT_mu6', 'HLT_mu22', 'HLT_mu80', 'HLT_mu60', 'HLT_mu24', 'HLT_mu20', 'HLT_mu26', 'HLT_mu14_ivarloose', 'HLT_mu14', 'HLT_mu28_ivarmedium', 'HLT_mu20_ivarmedium_L1MU10', 'HLT_mu26_imedium']
    self.Prescaled_MUTriggers_2018 = []#'HLT_mu24_ivarmedium', 'HLT_mu4', 'HLT_mu6', 'HLT_mu22', 'HLT_mu80', 'HLT_mu60', 'HLT_mu24', 'HLT_mu26', 'HLT_mu20', 'HLT_mu14_ivarloose', 'HLT_mu14', 'HLT_mu10', 'HLT_mu28_ivarmedium', 'HLT_mu20_ivarmedium_L1MU10']

# Signal region (SR) selection
class SRselection:
  def __init__(self):
    self.name                              = 'SR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = True    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = False     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study

# Signal region (SR) selection to compare with Gavin
class SRGavinselection:
  def __init__(self):
    self.name                              = 'SRGavin'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = True     # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmTplusMET                      = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study

# Signal region (SR) selection with no MET cut
class SRwoMETselection:
  def __init__(self):
    self.name                              = 'SRwoMET'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = True    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = False     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True    # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study


# Tight = Tighter signal region (SR) selection
class Tightselection:
  def __init__(self):
    self.name                              = 'Tight'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 30       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = False    # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 30       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study


# Control region (CR) selection
class CRselection:
  def __init__(self):
    self.name                              = 'CR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = True
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = True    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = False     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 0       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study

# Tighter control region (CR) selection
class CRmedselection:
  def __init__(self):
    self.name                              = 'CRmed'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = True
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study

###############################################################################################################################################
# Selections to study impact of veto selections (second electron/muon in electron/muon channel, no electron (muon) in muon (electron) channel)
###############################################################################################################################################

class SRLowPtLooseVetoselection:
  def __init__(self):
    self.name                              = 'SRLowPtLooseVeto'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study

class SRLowPtTightVetoselection:
  def __init__(self):
    self.name                              = 'SRLowPtTightVeto'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Tight'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Tight'
    self.elLoose_isolation                 = 'Tight'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study


class SRHighPtLooseVetoselection:
  def __init__(self):
    self.name                              = 'SRHighPtLooseVeto'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 28       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 35       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study

class SRHighPtTightVetoselection:
  def __init__(self):
    self.name                              = 'SRHighPtTightVeto'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 28       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Tight'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'Tight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 35       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Tight'
    self.elLoose_isolation                 = 'Tight'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = False
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = True
    self.el_Isolation                      = 'Tight'
    self.impactParameterRequirements       = True     # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 25       # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = True
    self.doSignificanceStudy               = True     # varies selection for significance study

# Control region (CR) selection
class CRLowPtLooseVetoselection:
  def __init__(self):
    self.name                              = 'CR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = True
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study


# Control region (CR) selection
class CRLowPtTightVetoselection:
  def __init__(self):
    self.name                              = 'CR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 10       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Tight'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 10       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Tight'
    self.elLoose_isolation                 = 'Tight'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = True
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study

# Control region (CR) selection
class CRHighPtLooseVetoselection:
  def __init__(self):
    self.name                              = 'CR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 28       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Loose'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 35       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Loose'
    self.elLoose_isolation                 = 'Loose'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = True
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study


# Control region (CR) selection
class CRHighPtTightVetoselection:
  def __init__(self):
    self.name                              = 'CR'
    # muons
    self.muon_n                            = 1        # require exactly one muon
    self.muonLoose_minPt                   = 28       # GeV
    self.muonLoose_maxEta                  = 2.5      # absolute eta
    self.muonLoose_isolation               = 'Tight'
    self.muon_minPt                        = 28       # GeV (must be at least 1.05 * online threshold)
    self.muon_Isolation                    = 'InvTight'
    # electrons
    self.excludeTransitionRegion4Electrons = True     # exclude 1.37<|eta|<1.52
    self.el_n                              = 1        # require exactly one electron
    self.elLoose_minPt                     = 35       # GeV
    self.elLoose_maxEta                    = 2.47     # absolute eta
    self.elLoose_ID                        = 'Tight'
    self.elLoose_isolation                 = 'Tight'
    self.el_minPt                          = 35       # GeV (must be at least 1 GeV larger than online threshold)
    self.el_Medium                         = False
    self.el_LooseButNotTight               = True
    self.el_LooseButNotMedium              = False
    self.el_MediumButNotTight              = False
    self.el_Tight                          = False
    self.el_Isolation                      = 'InvTight'
    self.impactParameterRequirements       = False    # |d0sig|<5 and |z0sintheta|<0.5
    # jets
    self.jet_atleastOne                    = False    # At least one jet
    self.jet_minPt                         = 25       # GeV
    self.jet_maxRapidity                   = 2.5      # |y|
    self.jet_cleaning                      = True     # remove events not passing jet cleaning (MC only, not-clean events in data already removed)
    self.jet_minDRJetLepton                = 0.4      # minimum DeltaR (jet, any signal lepton)
    self.jet_JVTcut                        = True     # select only jets passing JVT (Tight)
    self.bjetVeto                          = True     # discard events with at least one b-jet
    # other
    self.applyOR                           = True     # dR(jet,signal lepton)<0.2 -> reject jet, 0.2<dR(jet,signal lepton)<0.4 -> reject event
    self.minMET                            = 0        # GeV
    self.minmT                             = 60       # GeV
    self.triggerMatching                   = False
    self.doSignificanceStudy               = True     # varies selection for significance study


