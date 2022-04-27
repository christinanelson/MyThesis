from ROOT import TLorentzVector

class iLepton(TLorentzVector):
  def __init__(self):
    TLorentzVector.__init__(self)
    self.SF                  = 1
    self.passSignalSel       = False
    self.passLooseSel        = False
    self.isTrigMatched       = False
    self.passIP              = False
    self.passKinematicSignal = False
    self.passKinematicLoose  = False
    self.passID              = True
    self.passIDLoose         = True
    self.passIsolation       = True
    self.passIsolationLoose  = True
    self.matchedChains       = []

class iJet(TLorentzVector):
  def __init__(self):
    TLorentzVector.__init__(self)
    self.isBjet             = False
    self.isCjet             = False
    self.SF                 = 1
    self.passJVT            = True
    self.hadronTruthLabelID = 0
    self.btagWeight         = 0
