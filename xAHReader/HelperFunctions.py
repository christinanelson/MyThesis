#####################
# TRUTH LEPTONS
#####################
def getNLeptonTruth(tree,channel):
  if "EL" in channel:
    return len(tree.truthElectron_pt_dressed)
  elif "MU" in channel:
    return len(tree.truthMuon_pt_dressed)

def getLeptonPtTruth(tree,i,channel):
  if "EL" in channel:
    return tree.truthElectron_pt_dressed[i]
  elif "MU" in channel:
    return tree.truthMuon_pt_dressed[i]

def getLeptonEtaTruth(tree,i,channel):
  if "EL" in channel:
    return tree.truthElectron_eta_dressed[i]
  elif "MU" in channel:
    return tree.truthMuon_eta_dressed[i]

def getLeptonPhiTruth(tree,i,channel):
  if "EL" in channel:
    return tree.truthElectron_phi_dressed[i]
  elif "MU" in channel:
    return tree.truthMuon_phi_dressed[i]

def getLeptonETruth(tree,i,channel):
  if "EL" in channel:
    return tree.truthElectron_e_dressed[i]
  elif "MU" in channel:
    return tree.truthMuon_e_dressed[i]

#####################
# RECO LEPTONS
#####################
def getNLepton(tree,channel):
  if "EL" in channel:
    return len(tree.el_pt)
  elif "MU" in channel:
    return len(tree.muon_pt)

def getLeptonPt(tree,i,channel):
  if "EL" in channel:
    return tree.el_pt[i]
  elif "MU" in channel:
    return tree.muon_pt[i]

def getLeptonEta(tree,i,channel):
  if "EL" in channel:
    return tree.el_eta[i]
  elif "MU" in channel:
    return tree.muon_eta[i]

def getLeptonPhi(tree,i,channel):
  if "EL" in channel:
    return tree.el_phi[i]
  elif "MU" in channel:
    return tree.muon_phi[i]

def getLeptonM(tree,i,channel):
  if "EL" in channel:
    return tree.el_m[i]
  elif "MU" in channel:
    return tree.muon_m[i]

def passElectronID(tree,i,wp):
  if wp == 'Loose':
    return tree.el_DFCommonElectronsLHLoose[i]
  elif wp == 'Medium':
    return tree.el_DFCommonElectronsLHMedium[i]
  elif wp == 'Tight':
    return tree.el_DFCommonElectronsLHTight[i]

def isElectronLoose(tree,i):
  return tree.el_DFCommonElectronsLHLoose[i]

def isElectronMedium(tree,i):
  return tree.el_DFCommonElectronsLHMedium[i]

def isElectronTight(tree,i):
  return tree.el_DFCommonElectronsLHTight[i]

def isElectronMediumButNotTight(tree,i):
  return tree.el_DFCommonElectronsLHMedium[i] and not tree.el_DFCommonElectronsLHTight[i]

def isElectronLooseButNotTight(tree,i):
  return tree.el_DFCommonElectronsLHLoose[i] and not tree.el_DFCommonElectronsLHTight[i]

def isElectronLooseButNotMedium(tree,i):
  return tree.el_DFCommonElectronsLHLoose[i] and not tree.el_DFCommonElectronsLHMedium[i]

def getLeptonIso(tree,i,channel,WP):
  if "EL" in channel:
    if "Loose" in WP:
      return tree.el_isIsolated_FCLoose[i]
    elif "Tight" in WP:
      return tree.el_isIsolated_FCTight[i]
  elif "MU" in channel:
    if "Loose" in WP:
      return tree.muon_isIsolated_PflowLoose_FixedRad[i]
    elif "Tight" in WP:
      return tree.muon_isIsolated_PflowTight_FixedRad[i]

def getLeptond0sig(tree,i,channel):
  if "EL" in channel:
    return tree.el_trkd0sig[i]
  elif "MU" in channel:
    return tree.muon_trkd0sig[i]

def getLeptondeltaz0sintheta(tree,i,channel):
  if "EL" in channel:
    return tree.el_trkz0sintheta[i]
  elif "MU" in channel:
    return tree.muon_trkz0sintheta[i]

def getLeptonRecoSF(tree,i,channel):
  if "EL" in channel:
    return tree.el_RecoEff_SF[i][0]
  elif "MU" in channel:
    return tree.muon_RecoEff_SF_RecoMedium[i][0]

def getLeptonIsoSF(tree,i,channel,isoWP,pidWP=''):
  if "EL" in channel:
    branch = 'el_IsoEff_SF_{0}_isolFC{1}'.format(pidWP,isoWP)
    return (getattr(tree,branch))[i][0]
  elif "MU" in channel:
    branch = 'muon_IsoEff_SF_IsoPflow{0}_FixedRad'.format(isoWP)
    return (getattr(tree,branch))[i][0]

def getMuonTTVASF(tree,i):
  return tree.muon_TTVAEff_SF[i][0]

def getElectronPIDSF(tree,i,wp):
  if wp == 'Tight':
    branch = 'el_PIDEff_SF_{0}'.format(wp)
    return (getattr(tree,branch))[i][0]
  else: return 1

def getTrigThreshold(trigger):
  return int(trigger.split('_')[1].replace('mu','').replace('e',''))

def isLeptonTrigMatched(tree,i,channel,reqTrigs): # reqTrigs: list of triggers requested
  # Find at least one trigger that matches the lepton and satisfies pt > trigThreshold * 1.05 (muons),  trigThreshold + 1 (electrons)
  if "EL" in channel:
    isTrigMatchedToChain = "el_isTrigMatchedToChain" # !! not in tree ANYMORE need to update this
    #isTrigMatchedToChain = "el_isTrigMatched" # !! not in tree ANYMORE need to update this
    listTrigChains       = "el_listTrigChains"
  elif "MU" in channel:
    isTrigMatchedToChain = "muon_isTrigMatchedToChain"
    listTrigChains       = "muon_listTrigChains"
  Matches    = getattr(tree,isTrigMatchedToChain)[i] # match decision for each trigger (matching order of previous array)
  TrigList   = getattr(tree,listTrigChains)[i]       # full list of triggers (provided in xAH config)
  lepPt      = getLeptonPt(tree,i,channel)
  Chains     = []
  Thresholds = []
  for itrig in range(0,len(TrigList)): # loop over full list of triggers
    TrigName = TrigList[itrig]
    if TrigName not in reqTrigs: continue # skip trigger that is not requested
    trigThreshold = getTrigThreshold(TrigName)
    Matched = False
    if TrigName != 'HLT_e300_etcut':
      if Matches[itrig]: Matched = True
    else: # HLT_e300_etcut
      Matched = True # no need to request matching for this chain
    if Matched and TrigName in tree.passedTriggers: # muon matched to fired trigger
      threshold = 1.05 * trigThreshold if channel == 'MU' else trigThreshold+1
      Chains.append(TrigName)
      Thresholds.append(threshold)
  # Loop over (trigger) threshold of matched chains
  for th in Thresholds:
    if lepPt > th: # trigger matched and above trigger threshold
      return True, Chains
  return False, Chains

def getMuonTrigEffSF(tree,i,campaign):
  SF = 1
  if campaign == "a":
    if   tree.muon_TrigEff_SF_HLT_mu20_iloose_L1MU15_OR_HLT_mu50_RecoMedium[i][0] != -1: SF *= tree.muon_TrigEff_SF_HLT_mu20_iloose_L1MU15_OR_HLT_mu50_RecoMedium[i][0]
    elif tree.muon_TrigEff_SF_HLT_mu26_ivarmedium_OR_HLT_mu50_RecoMedium[i][0]    != -1: SF *= tree.muon_TrigEff_SF_HLT_mu26_ivarmedium_OR_HLT_mu50_RecoMedium[i][0]
  elif campaign == "d" or campaign == "e":
    SF *= tree.muon_TrigEff_SF_HLT_mu26_ivarmedium_OR_HLT_mu50_RecoMedium[i][0]
  return SF

def getElectronTrigEffSF(tree,i,pidWP,isoWP):
  if pidWP == 'Tight' and isoWP == 'Tight':
    branch = 'el_TrigEff_SF_SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_2018_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0_{0}_isolFC{1}'.format(pidWP,isoWP)
    return (getattr(tree,branch))[i][0]
  else: return 1

#####################
# TRUTH JETS
#####################
def getNJetTruth(tree):
  return len(tree.truthJet_pt)

def getJetPtTruth(tree,i):
  return tree.truthJet_pt[i]

def getJetPhiTruth(tree,i):
  return tree.truthJet_phi[i]

def getJetEtaTruth(tree,i):
  return tree.truthJet_eta[i]

def getJetETruth(tree,i):
  return tree.truthJet_E[i]

def getJetPartonTruthLabelID(tree,i):
  return tree.truthJet_PartonTruthLabelID[i]

def getTruthJetHadronTruthLabelID(tree,i):
  return tree.truthJet_HadronConeExclTruthLabelID[i]

#####################
# RECO JETS
#####################
def getNJet(tree):
  return len(tree.jet_pt)

def getRecoJetPt(tree,i):
  return tree.jet_pt[i]

def getRecoJetPhi(tree,i):
  return tree.jet_phi[i]

def getRecoJetEta(tree,i):
  return tree.jet_eta[i]

def getRecoJetE(tree,i):
  return tree.jet_E[i]

def eventIsClean(tree):
  return tree.eventClean_LooseBad

def jetPassJVT(tree,i):
  return tree.jet_JvtPass_Tight[i]

def getJVTSF(tree,i):
  SF = getattr(tree,'jet_JvtEff_SF_Tight',-1)
  SF = SF[0][0] if SF != -1 else 1
  return SF

def getJetBTag(tree,i,tagger):
  decision = getattr(tree,'jet_is_'+tagger+'_FixedCutBEff_85',0)
  return decision[i]

def getJetBTagSF(tree,i,tagger):
  SF = getattr(tree,'jet_SF_'+tagger+'_FixedCutBEff_85',0)
  return decision[i][0]

def getJetHadronTruthLabelID(tree,i):
  return tree.jet_HadronConeExclTruthLabelID[i]

#####################
# MET
#####################
def getMET(tree):
  return tree.metFinalTrk

def getMETPhi(tree):
  return tree.metFinalTrkPhi

#####################
# Other
#####################
def getPtBinMin(array,i):
  ptrange = array[i].split(":")
  return int(ptrange[0])

def getPtBinMax(array,i):
  ptrange = array[i].split(":")
  return int(ptrange[1])

def getDSID(path):
  if path.find("3610") != -1:
    return path[path.find("3610"):path.find("3610")+6]
  elif path.find("3611") != -1:
    return path[path.find("3611"):path.find("3611")+6]
  elif path.find("7001") != -1:
    return path[path.find("7001"):path.find("7001")+6]
  elif path.find("3641") != -1:
    return path[path.find("3641"):path.find("3641")+6]
  elif path.find("4104") != -1:
    return path[path.find("4104"):path.find("4104")+6]
  elif path.find("3616") != -1:
    return path[path.find("3616"):path.find("3616")+6]
  elif path.find("4106") != -1:
    return path[path.find("4106"):path.find("4106")+6]
  elif path.find("3457") != -1:
    return path[path.find("3457"):path.find("3457")+6]
  elif path.find("3642") != -1:
    return path[path.find("3642"):path.find("3642")+6]
  elif path.find("3636") != -1:
    return path[path.find("3636"):path.find("3636")+6]
  elif path.find("3631") != -1:
    return path[path.find("3631"):path.find("3631")+6]
  elif path.find("3633") != -1:
    return path[path.find("3633"):path.find("3633")+6]
  elif path.find("3634") != -1:
    return path[path.find("3634"):path.find("3634")+6]
  else: return 'Unknown'

def getPeriod(path):
  return path[path.find("period"):path.find("period")+7]

# Apply custom Overlap Removal
def applyOR(lepton,jets):
  # Jets overlapping with leptons (deltaR<0.2) are discarded
  # Events with at least one jet satisfying 0.2<deltaR(jet,any lepton)<0.4 are discarded
  Jets = []
  dRs  = {}
  for jet in jets: # loop over jets
    keep   = True
    dR = jet.DeltaR(lepton)
    dRs[jet.Pt()] = dR
    if dR < 0.2: # discard jet
      keep = False
    elif dR >= 0.2 and dR < 0.4: # discard event
      return False,[],dRs
    if keep:
      Jets.append(jet)
  return True,Jets,dRs

# Check if a given lepton passes Loose/Signal kinematic requirements
def passKinematicCut(flavour,selection,Type,leptonPt,leptonEta,debug,isLoose):
  if isLoose:
    extra  = 'Loose'
    minPt  = selection.elLoose_minPt  if flavour == 'EL' else selection.muonLoose_minPt
  else:
    extra  = 'Final'
    minPt  = selection.el_minPt  if flavour == 'EL' else selection.muon_minPt
  maxEta = selection.elLoose_maxEta if flavour == 'EL' else selection.muonLoose_maxEta
  passKinematicCut = False
  if leptonPt > minPt and abs(leptonEta) < maxEta:
    passKinematicCut = True
    if flavour == 'EL':
      passExcludeTransitionRegion4Electrons = False
      if selection.excludeTransitionRegion4Electrons:
        if abs(leptonEta)<=1.37 or abs(leptonEta)>=1.52: # Outside transition region
          passExcludeTransitionRegion4Electrons = True
      if not passExcludeTransitionRegion4Electrons: passKinematicCut = False
  if not passKinematicCut and debug: print('DEBUG: Lepton not passed {} kinematic selections'.format(extra))
  return passKinematicCut

# Check if a given lepton passes Loose/Signal ID requirement
def passID(selection,tree,ilep,debug,isLoose):
  if isLoose:
    if not passElectronID(tree,ilep,selection.elLoose_ID):
      if debug: print ("DEBUG: Electron not passed {} ID requirement".format(selection.elLoose_ID))
      return False
  else: # signal
    if selection.el_Medium and not isElectronMedium(tree,ilep):
      if debug: print ("DEBUG: Electron not passed Medium ID requirement")
      return False
    elif selection.el_MediumButNotTight and not isElectronMediumButNotTight(tree,ilep):
      if debug: print ("DEBUG: Electron not passed MediumButNotTight ID requirement")
      return False
    elif selection.el_LooseButNotTight and not isElectronLooseButNotTight(tree,ilep):
      if debug: print ("DEBUG: Electron not passed LooseButNotTight ID requirement")
      return False
    elif selection.el_LooseButNotMedium and not isElectronLooseButNotMedium(tree,ilep):
      if debug: print ("DEBUG: Electron not passed LooseButNotMedium ID requirement")
      return False
    elif selection.el_Tight and not isElectronTight(tree,ilep):
      if debug: print ("DEBUG: Electron not passed Tight ID requirement")
      return False
  return True

# Check if a given lepton passes Loose/Signal isolation requirement
def passIsolation(flavour,selection,tree,ilep,debug,isLoose):
  if isLoose:
    looseIsoWP    = selection.elLoose_isolation if flavour == 'EL' else selection.muonLoose_isolation
    passIsolation = getLeptonIso(tree,ilep,flavour,looseIsoWP) if flavour == 'EL' else getLeptonIso(tree,ilep,flavour,looseIsoWP)
    if not passIsolation:
      if debug: print ("DEBUG: Lepton not passed {} isolation requirement".format(looseIsoWP))
    return passIsolation
  else: # signal
    isoWP           = selection.el_Isolation if flavour == 'EL' else selection.muon_Isolation
    leptonIsolation = getLeptonIso(tree,ilep,flavour,isoWP)
    if "Inv" not in isoWP: passIsolation = leptonIsolation
    else: passIsolation = not leptonIsolation
    if not passIsolation:
      if debug: print('DEBUG: Lepton not passed {} isolation requirement'.format(isoWP))
    return passIsolation

from Dicts import *
# Get all electrons/muons and decorate those that pass 'Loose' and 'Signal' selections
def getAllLeptons(tree,flavour,selection,Type,useSFs,debug,campaign,trigList,isSignalChannel):
  # Create an list of iLepton leptons and decorate those which pass all the signal-like selections
  from Selections    import Common
  from HelperClasses import iLepton
  common     = Common()
  AllLeptons = []
  nLeptons   = getNLepton(tree,flavour) if Type=="reco" else getNLeptonTruth(tree,flavour)
  if debug:
    print ("DEBUG: Get all leptons ("+flavour+")")
    print ("DEBUG: Initial number of leptons = {}".format(nLeptons))
  ####################
  # Loop over leptons
  for ilep in range(0,nLeptons):
    passLoose  = True
    passSignal = True
    # Create iLepton for this lepton
    TLVLepton = iLepton()
    leptonPt  = getLeptonPt (tree,ilep,flavour) if Type=="reco" else getLeptonPtTruth(tree,ilep,flavour)
    leptonEta = getLeptonEta(tree,ilep,flavour) if Type=="reco" else getLeptonEtaTruth(tree,ilep,flavour)
    leptonPhi = getLeptonPhi(tree,ilep,flavour) if Type=="reco" else getLeptonPhiTruth(tree,ilep,flavour)
    if Type == "reco": leptonM = getLeptonM(tree,ilep,flavour)
    else:              leptonE = getLeptonETruth(tree,ilep,flavour) # truth
    if debug:
      print('DEBUG: Decorate following lepton w/ loose and signal-like selection decisions (pt,eta,phi) : {},{},{}'.format(leptonPt,leptonEta,leptonPhi))
    if Type == "reco":
      TLVLepton.SetPtEtaPhiM(leptonPt,leptonEta,leptonPhi,leptonM)
      if isSignalChannel and selection.triggerMatching: TLVLepton.isTrigMatched, TLVLepton.matchedChains = isLeptonTrigMatched(tree,ilep,flavour,trigList)
    else: # truth
      TLVLepton.SetPtEtaPhiE(leptonPt,leptonEta,leptonPhi,leptonE)
    #################################################################
    # kinematic selection
    TLVLepton.passKinematicLoose = passKinematicCut(flavour,selection,Type,leptonPt,leptonEta,debug,True)
    if isSignalChannel: TLVLepton.passKinematicSignal = passKinematicCut(flavour,selection,Type,leptonPt,leptonEta,debug,False)
    if not TLVLepton.passKinematicLoose:  passLoose  = False
    if not TLVLepton.passKinematicSignal: passSignal = False
    #if not passLoose and not passSignal: continue # skip lepton
    if not passSignal: continue # skip lepton
    h_cutflow[Type].Fill(h_cutflow_lepPtEta[Type],1)

    ###########################################
    # Impact parameter requirements (only for reco and if requested)
    if Type == "reco" and selection.impactParameterRequirements:
      passIP              = True
      lep_d0sig           = getLeptond0sig(tree,ilep,flavour)
      lep_deltaz0sintheta = getLeptondeltaz0sintheta(tree,ilep,flavour)
      if flavour == 'EL': 
        if abs(lep_d0sig) > common.ElectronMaxAbsd0sig or abs(lep_deltaz0sintheta) > common.ElectronMaxAbsdeltaz0sintheta: passIP = False
      if flavour == 'MU': 
        if abs(lep_d0sig) > common.MuonMaxAbsd0sig or abs(lep_deltaz0sintheta) > common.MuonMaxAbsdeltaz0sintheta: passIP = False      
      if not passIP:
        if debug: print ("DEBUG: Lepton not passed impact parameter cuts")
        continue # skip lepton
    h_cutflow[Type].Fill(h_cutflow_lepIP[Type],1)

    ######################
    # ID requirement (only for reco electrons)
    if Type == 'reco' and flavour == 'EL':
    #  TLVLepton.passIDLoose = passID(selection,tree,ilep,debug,True)
      if isSignalChannel: TLVLepton.passID = passID(selection,tree,ilep,debug,False)
    #  if passLoose  and not TLVLepton.passIDLoose: passLoose  = False
      if passSignal and not TLVLepton.passID:      passSignal = False
    #  if not passLoose and not passSignal: continue # skip lepton
      if not passSignal: continue
    h_cutflow[Type].Fill(h_cutflow_lepID[Type],1)

    ########################################
    # Isolation requirement (only for reco)
    if Type == 'reco':
    #  TLVLepton.passIsolationLoose = passIsolation(flavour,selection,tree,ilep,debug,True)
      if isSignalChannel: TLVLepton.passIsolation = passIsolation(flavour,selection,tree,ilep,debug,False)
    #  if passLoose  and not TLVLepton.passIsolationLoose: passLoose  = False
      if passSignal and not TLVLepton.passIsolation:      passSignal = False
    #  if not passLoose and not passSignal: continue # skip lepton
      if not passSignal: continue
    h_cutflow[Type].Fill(h_cutflow_lepIso[Type],1)

    ########################################################
    # Decorate lepton with loose/signal selection decisions
    #TLVLepton.passLooseSel = True if TLVLepton.passKinematicLoose and TLVLepton.passIDLoose and TLVLepton.passIsolationLoose else False
    if isSignalChannel:
      #TLVLepton.passSignalSel = True if TLVLepton.passKinematicSignal and TLVLepton.passIsolation else False
      TLVLepton.passSignalSel = True if TLVLepton.passKinematicSignal and TLVLepton.passID and TLVLepton.passIsolation else False
      # Trigger matching requirement (only for reco)
      #if Type == 'reco' and selection.triggerMatching and not TLVLepton.isTrigMatched:
      #  if debug: print ("DEBUG: Lepton not passed trigger matching requirement")
      #  TLVLepton.passSignalSel = False
    ########################################
    # Decorate signal-like leptons with SFs
    if isSignalChannel and Type == 'reco' and useSFs and TLVLepton.passSignalSel and 'CR' not in selection.name:
      isoWP = selection.el_Isolation if flavour == 'EL' else selection.muon_Isolation
      if flavour == 'EL':
        idWP = 'Tight'
        if not selection.el_Tight:
          if selection.el_LooseButNotTight or selection.el_LooseButNotMedium: idWP = 'Loose'
          elif selection.el_MediumButNotTight: idWP = 'Medium'
        TLVLepton.SF = getLeptonRecoSF(tree,ilep,'EL')*getLeptonIsoSF(tree,ilep,'EL',isoWP,idWP)*getElectronPIDSF(tree,ilep,'Tight')*getElectronTrigEffSF(tree,ilep,'Tight',isoWP)
      else: # MU
        TLVLepton.SF = getLeptonRecoSF(tree,ilep,'MU')*getLeptonIsoSF(tree,ilep,'MU',isoWP)*getMuonTTVASF(tree,ilep)*getMuonTrigEffSF(tree,ilep,campaign)
    AllLeptons.append(TLVLepton)
  if debug: print("DEBUG: Number of selected leptons = {}".format(len(AllLeptons)))
  return AllLeptons

# Pring memory usage
def printMemory(i):
  import resource
  print ("DEBUG: Memory usage ({0}) = {1} (MB)".format(i,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024))
