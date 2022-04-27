# All possible input files - Also available _Medium1.root and _Medium2.root for all files

# EMPFlow jets
InputFiles = dict() # key should match with one of the types in Samples (see below)
PATH_nom = '/eos/user/n/nelsonc/W+jets/PlotterInputs/2022-01-25/'
PATH_sys = '/eos/user/l/liformen/christina/W+jets/PlotterInputs/MC16a_systs/'

################################
# EL CHANNEL (!) <3
################################
 

################################
# FOR NOMINAL (!) <3
################################

# DATA
# Data15
InputFiles["Signal_data15_EL_SR_DL1r"]      = PATH_nom+"Data1516_MC16a/Data15_EL_SR_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data15_EL_SRwoMET_DL1r"] = PATH_nom+"Data1516_MC16a/Data15_EL_SRwoMET_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data15_EL_CR_DL1r"]      = PATH_nom+"Data1516_MC16a/Data15_EL_CR_DL1rTagger_All_2022-01-25.root"
# Data16
InputFiles["Signal_data16_EL_SR_DL1r"]      = PATH_nom+"Data1516_MC16a/Data16_EL_SR_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data16_EL_SRwoMET_DL1r"] = PATH_nom+"Data1516_MC16a/Data16_EL_SRwoMET_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data16_EL_CR_DL1r"]      = PATH_nom+"Data1516_MC16a/Data16_EL_CR_DL1rTagger_All_2022-01-25.root"
# Data17                                                       
InputFiles["Signal_data17_EL_SR_DL1r"]      = PATH_nom+"Data17_MC16d/Data17_EL_SR_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data17_EL_SRwoMET_DL1r"] = PATH_nom+"Data17_MC16d/Data17_EL_SRwoMET_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data17_EL_CR_DL1r"]      = PATH_nom+"Data17_MC16d/Data17_EL_CR_DL1rTagger_All_2022-01-25.root"
# Data18
InputFiles["Signal_data18_EL_SR_DL1r"]      = PATH_nom+"Data18_MC16e/Data18_EL_SR_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data18_EL_SRwoMET_DL1r"] = PATH_nom+"Data18_MC16e/Data18_EL_SRwoMET_DL1rTagger_All_2022-01-25.root"
InputFiles["Signal_data18_EL_CR_DL1r"]      = PATH_nom+"Data18_MC16e/Data18_EL_CR_DL1rTagger_All_2022-01-25.root"


# NOMINAL
# MC16a Wenu Signal
InputFiles["Signal_MC16a_EL_SR_DL1r"]       = PATH_nom+"Data1516_MC16a/WenuMC16aSherpa_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r"]  = PATH_nom+"Data1516_MC16a/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16a_EL_CR_DL1r"]       = PATH_nom+"Data1516_MC16a/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16a Zee
InputFiles["Zee_MC16a_EL_SR_DL1r"]          = PATH_nom+"Data1516_MC16a/MC16aZee_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r"]     = PATH_nom+"Data1516_MC16a/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16a_EL_CR_DL1r"]          = PATH_nom+"Data1516_MC16a/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16a Top
InputFiles["Top_MC16a_EL_SR_DL1r"]          = PATH_nom+"Data1516_MC16a/MC16aTop_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r"]     = PATH_nom+"Data1516_MC16a/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16a_EL_CR_DL1r"]          = PATH_nom+"Data1516_MC16a/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16a Diboson
InputFiles["Diboson_MC16a_EL_SR_DL1r"]      = PATH_nom+"Data1516_MC16a/MC16aDiboson_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r"] = PATH_nom+"Data1516_MC16a/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r"]      = PATH_nom+"Data1516_MC16a/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"

# MC16d Wenu Signal
InputFiles["Signal_MC16d_EL_SR_DL1r"]       = PATH_nom+"Data17_MC16d/WenuMC16dSherpa_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16d_EL_SRwoMET_DL1r"]  = PATH_nom+"Data17_MC16d/WenuMC16dSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16d_EL_CR_DL1r"]       = PATH_nom+"Data17_MC16d/WenuMC16dSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Zee
InputFiles["Zee_MC16d_EL_SR_DL1r"]          = PATH_nom+"Data17_MC16d/MC16dZee_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16d_EL_SRwoMET_DL1r"]     = PATH_nom+"Data17_MC16d/MC16dZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16d_EL_CR_DL1r"]          = PATH_nom+"Data17_MC16d/MC16dZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Top
InputFiles["Top_MC16d_EL_SR_DL1r"]          = PATH_nom+"Data17_MC16d/MC16dTop_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16d_EL_SRwoMET_DL1r"]     = PATH_nom+"Data17_MC16d/MC16dTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16d_EL_CR_DL1r"]          = PATH_nom+"Data17_MC16d/MC16dTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Diboson
InputFiles["Diboson_MC16d_EL_SR_DL1r"]      = PATH_nom+"Data17_MC16d/MC16dDiboson_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16d_EL_SRwoMET_DL1r"] = PATH_nom+"Data17_MC16d/MC16dDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16d_EL_CR_DL1r"]      = PATH_nom+"Data17_MC16d/MC16dDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"

# MC16e Wenu Signal
InputFiles["Signal_MC16e_EL_SR_DL1r"]       = PATH_nom+"Data18_MC16e/WenuMC16eSherpa_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16e_EL_SRwoMET_DL1r"]  = PATH_nom+"Data18_MC16e/WenuMC16eSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Signal_MC16e_EL_CR_DL1r"]       = PATH_nom+"Data18_MC16e/WenuMC16eSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Zee
InputFiles["Zee_MC16e_EL_SR_DL1r"]          = PATH_nom+"Data18_MC16e/MC16eZee_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16e_EL_SRwoMET_DL1r"]     = PATH_nom+"Data18_MC16e/MC16eZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Zee_MC16e_EL_CR_DL1r"]          = PATH_nom+"Data18_MC16e/MC16eZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Top
InputFiles["Top_MC16e_EL_SR_DL1r"]          = PATH_nom+"Data18_MC16e/MC16eTop_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16e_EL_SRwoMET_DL1r"]     = PATH_nom+"Data18_MC16e/MC16eTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Top_MC16e_EL_CR_DL1r"]          = PATH_nom+"Data18_MC16e/MC16eTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
# MC16d Diboson
InputFiles["Diboson_MC16e_EL_SR_DL1r"]      = PATH_nom+"Data18_MC16e/MC16eDiboson_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16e_EL_SRwoMET_DL1r"] = PATH_nom+"Data18_MC16e/MC16eDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"
InputFiles["Diboson_MC16e_EL_CR_DL1r"]      = PATH_nom+"Data18_MC16e/MC16eDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-01-25.root"

















################################
# FOR SYSTEMATICS (!) <3
################################
PATH_NomOld = "/eos/user/n/nelsonc/W+jets/PlotterInputs/Systematics/"
# DATA
# Data15
InputFiles["Signal_data15_EL_SR_DL1r_data"]      = PATH_NomOld+"data1516/Data15_EL_SR_DL1rTagger_All_170821_data1516.root"
InputFiles["Signal_data15_EL_SRwoMET_DL1r_data"] = PATH_NomOld+"data1516/Data15_EL_SRwoMET_DL1rTagger_All_170821_data1516.root"
InputFiles["Signal_data15_EL_CR_DL1r_data"]      = PATH_NomOld+"data1516/Data15_EL_CR_DL1rTagger_All_170821_data1516.root"
# Data16
InputFiles["Signal_data16_EL_SR_DL1r_data"]      = PATH_NomOld+"data1516/Data16_EL_SR_DL1rTagger_All_170821_data1516.root"
InputFiles["Signal_data16_EL_SRwoMET_DL1r_data"] = PATH_NomOld+"data1516/Data16_EL_SRwoMET_DL1rTagger_All_170821_data1516.root"
InputFiles["Signal_data16_EL_CR_DL1r_data"]      = PATH_NomOld+"data1516/Data16_EL_CR_DL1rTagger_All_170821_data1516.root"

# NOMINAL
# MC16a Wenu Signal
InputFiles["Signal_MC16a_EL_SR_DL1r_nominal"]       = PATH_NomOld+"nominal/WenuMC16aSherpa_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_nominal"]  = PATH_NomOld+"nominal/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Signal_MC16a_EL_CR_DL1r_nominal"]       = PATH_NomOld+"nominal/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
# Zee
InputFiles["Zee_MC16a_EL_SR_DL1r_nominal"]          = PATH_NomOld+"nominal/MC16aZee_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_nominal"]     = PATH_NomOld+"nominal/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Zee_MC16a_EL_CR_DL1r_nominal"]          = PATH_NomOld+"nominal/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
# MC16a Top
InputFiles["Top_MC16a_EL_SR_DL1r_nominal"]          = PATH_NomOld+"nominal/MC16aTop_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_nominal"]     = PATH_NomOld+"nominal/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Top_MC16a_EL_CR_DL1r_nominal"]          = PATH_NomOld+"nominal/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
# MC16a Diboson
InputFiles["Diboson_MC16a_EL_SR_DL1r_nominal"]      = PATH_NomOld+"nominal/MC16aDiboson_EL_SR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_nominal"] = PATH_NomOld+"nominal/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r_nominal"]      = PATH_NomOld+"nominal/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821.root"


# VARIATION DET1
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Det1_down"]  = PATH_sys+"JET_EffectiveNP_Detector1__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Det1_down"]     = PATH_sys+"JET_EffectiveNP_Detector1__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Det1_down"]     = PATH_sys+"JET_EffectiveNP_Detector1__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Det1_down"] = PATH_sys+"JET_EffectiveNP_Detector1__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION DET1
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Det1_up"]  = PATH_sys+"JET_EffectiveNP_Detector1__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Det1_up"]     = PATH_sys+"JET_EffectiveNP_Detector1__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Det1_up"]     = PATH_sys+"JET_EffectiveNP_Detector1__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Det1_up"] = PATH_sys+"JET_EffectiveNP_Detector1__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION DET2
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Det2_down"]  = PATH_sys+"JET_EffectiveNP_Detector2__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Det2_down"]     = PATH_sys+"JET_EffectiveNP_Detector2__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Det2_down"]     = PATH_sys+"JET_EffectiveNP_Detector2__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Det2_down"] = PATH_sys+"JET_EffectiveNP_Detector2__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION DET2
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Det2_up"]  = PATH_sys+"JET_EffectiveNP_Detector2__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Det2_up"]     = PATH_sys+"JET_EffectiveNP_Detector2__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Det2_up"]     = PATH_sys+"JET_EffectiveNP_Detector2__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Det2_up"] = PATH_sys+"JET_EffectiveNP_Detector2__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION MIX1
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix1_down"]  = PATH_sys+"JET_EffectiveNP_Mixed1__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix1_down"]     = PATH_sys+"JET_EffectiveNP_Mixed1__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix1_down"]     = PATH_sys+"JET_EffectiveNP_Mixed1__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix1_down"] = PATH_sys+"JET_EffectiveNP_Mixed1__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MIX1
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix1_up"]  = PATH_sys+"JET_EffectiveNP_Mixed1__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix1_up"]     = PATH_sys+"JET_EffectiveNP_Mixed1__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix1_up"]     = PATH_sys+"JET_EffectiveNP_Mixed1__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix1_up"] = PATH_sys+"JET_EffectiveNP_Mixed1__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION MIX2
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix2_down"]  = PATH_sys+"JET_EffectiveNP_Mixed2__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix2_down"]     = PATH_sys+"JET_EffectiveNP_Mixed2__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix2_down"]     = PATH_sys+"JET_EffectiveNP_Mixed2__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix2_down"] = PATH_sys+"JET_EffectiveNP_Mixed2__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MIX2
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix2_up"]  = PATH_sys+"JET_EffectiveNP_Mixed2__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix2_up"]     = PATH_sys+"JET_EffectiveNP_Mixed2__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix2_up"]     = PATH_sys+"JET_EffectiveNP_Mixed2__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix2_up"] = PATH_sys+"JET_EffectiveNP_Mixed2__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION MIX3
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix3_down"]  = PATH_sys+"JET_EffectiveNP_Mixed3__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix3_down"]     = PATH_sys+"JET_EffectiveNP_Mixed3__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix3_down"]     = PATH_sys+"JET_EffectiveNP_Mixed3__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix3_down"] = PATH_sys+"JET_EffectiveNP_Mixed3__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MIX3
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Mix3_up"]  = PATH_sys+"JET_EffectiveNP_Mixed3__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Mix3_up"]     = PATH_sys+"JET_EffectiveNP_Mixed3__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Mix3_up"]     = PATH_sys+"JET_EffectiveNP_Mixed3__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Mix3_up"] = PATH_sys+"JET_EffectiveNP_Mixed3__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION MODEL1
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model1_down"]  = PATH_sys+"JET_EffectiveNP_Modelling1__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model1_down"]     = PATH_sys+"JET_EffectiveNP_Modelling1__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model1_down"]     = PATH_sys+"JET_EffectiveNP_Modelling1__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model1_down"] = PATH_sys+"JET_EffectiveNP_Modelling1__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MODEL1
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model1_up"]  = PATH_sys+"JET_EffectiveNP_Modelling1__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model1_up"]     = PATH_sys+"JET_EffectiveNP_Modelling1__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model1_up"]     = PATH_sys+"JET_EffectiveNP_Modelling1__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model1_up"] = PATH_sys+"JET_EffectiveNP_Modelling1__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION MODEL2
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model2_down"]  = PATH_sys+"JET_EffectiveNP_Modelling2__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model2_down"]     = PATH_sys+"JET_EffectiveNP_Modelling2__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model2_down"]     = PATH_sys+"JET_EffectiveNP_Modelling2__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model2_down"] = PATH_sys+"JET_EffectiveNP_Modelling2__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MODEL2
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model2_up"]  = PATH_sys+"JET_EffectiveNP_Modelling2__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model2_up"]     = PATH_sys+"JET_EffectiveNP_Modelling2__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model2_up"]     = PATH_sys+"JET_EffectiveNP_Modelling2__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model2_up"] = PATH_sys+"JET_EffectiveNP_Modelling2__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION MODEL3
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model3_down"]  = PATH_sys+"JET_EffectiveNP_Modelling3__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model3_down"]     = PATH_sys+"JET_EffectiveNP_Modelling3__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model3_down"]     = PATH_sys+"JET_EffectiveNP_Modelling3__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model3_down"] = PATH_sys+"JET_EffectiveNP_Modelling3__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MODEL3
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model3_up"]  = PATH_sys+"JET_EffectiveNP_Modelling3__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model3_up"]     = PATH_sys+"JET_EffectiveNP_Modelling3__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model3_up"]     = PATH_sys+"JET_EffectiveNP_Modelling3__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model3_up"] = PATH_sys+"JET_EffectiveNP_Modelling3__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION MODEL4
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model4_down"]  = PATH_sys+"JET_EffectiveNP_Modelling4__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model4_down"]     = PATH_sys+"JET_EffectiveNP_Modelling4__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model4_down"]     = PATH_sys+"JET_EffectiveNP_Modelling4__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model4_down"] = PATH_sys+"JET_EffectiveNP_Modelling4__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION MODEL4
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Model4_up"]  = PATH_sys+"JET_EffectiveNP_Modelling4__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Model4_up"]     = PATH_sys+"JET_EffectiveNP_Modelling4__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Model4_up"]     = PATH_sys+"JET_EffectiveNP_Modelling4__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Model4_up"] = PATH_sys+"JET_EffectiveNP_Modelling4__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION STAT1
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat1_down"]  = PATH_sys+"JET_EffectiveNP_Statistical1__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat1_down"]     = PATH_sys+"JET_EffectiveNP_Statistical1__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat1_down"]     = PATH_sys+"JET_EffectiveNP_Statistical1__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat1_down"] = PATH_sys+"JET_EffectiveNP_Statistical1__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT1
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat1_up"]  = PATH_sys+"JET_EffectiveNP_Statistical1__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat1_up"]     = PATH_sys+"JET_EffectiveNP_Statistical1__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat1_up"]     = PATH_sys+"JET_EffectiveNP_Statistical1__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat1_up"] = PATH_sys+"JET_EffectiveNP_Statistical1__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION STAT2
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat2_down"]  = PATH_sys+"JET_EffectiveNP_Statistical2__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat2_down"]     = PATH_sys+"JET_EffectiveNP_Statistical2__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat2_down"]     = PATH_sys+"JET_EffectiveNP_Statistical2__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat2_down"] = PATH_sys+"JET_EffectiveNP_Statistical2__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT2
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat2_up"]  = PATH_sys+"JET_EffectiveNP_Statistical2__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat2_up"]     = PATH_sys+"JET_EffectiveNP_Statistical2__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat2_up"]     = PATH_sys+"JET_EffectiveNP_Statistical2__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat2_up"] = PATH_sys+"JET_EffectiveNP_Statistical2__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION STAT3
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat3_down"]  = PATH_sys+"JET_EffectiveNP_Statistical3__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat3_down"]     = PATH_sys+"JET_EffectiveNP_Statistical3__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat3_down"]     = PATH_sys+"JET_EffectiveNP_Statistical3__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat3_down"] = PATH_sys+"JET_EffectiveNP_Statistical3__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT3
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat3_up"]  = PATH_sys+"JET_EffectiveNP_Statistical3__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat3_up"]     = PATH_sys+"JET_EffectiveNP_Statistical3__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat3_up"]     = PATH_sys+"JET_EffectiveNP_Statistical3__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat3_up"] = PATH_sys+"JET_EffectiveNP_Statistical3__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION STAT4
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat4_down"]  = PATH_sys+"JET_EffectiveNP_Statistical4__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat4_down"]     = PATH_sys+"JET_EffectiveNP_Statistical4__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat4_down"]     = PATH_sys+"JET_EffectiveNP_Statistical4__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat4_down"] = PATH_sys+"JET_EffectiveNP_Statistical4__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT4
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat4_up"]  = PATH_sys+"JET_EffectiveNP_Statistical4__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat4_up"]     = PATH_sys+"JET_EffectiveNP_Statistical4__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat4_up"]     = PATH_sys+"JET_EffectiveNP_Statistical4__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat4_up"] = PATH_sys+"JET_EffectiveNP_Statistical4__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION STAT5
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat5_down"]  = PATH_sys+"JET_EffectiveNP_Statistical5__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat5_down"]     = PATH_sys+"JET_EffectiveNP_Statistical5__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat5_down"]     = PATH_sys+"JET_EffectiveNP_Statistical5__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat5_down"] = PATH_sys+"JET_EffectiveNP_Statistical5__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT5
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat5_up"]  = PATH_sys+"JET_EffectiveNP_Statistical5__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat5_up"]     = PATH_sys+"JET_EffectiveNP_Statistical5__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat5_up"]     = PATH_sys+"JET_EffectiveNP_Statistical5__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat5_up"] = PATH_sys+"JET_EffectiveNP_Statistical5__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION STAT6
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat6_down"]  = PATH_sys+"JET_EffectiveNP_Statistical6__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat6_down"]     = PATH_sys+"JET_EffectiveNP_Statistical6__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat6_down"]     = PATH_sys+"JET_EffectiveNP_Statistical6__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat6_down"] = PATH_sys+"JET_EffectiveNP_Statistical6__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION STAT6
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_Stat6_up"]  = PATH_sys+"JET_EffectiveNP_Statistical6__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_Stat6_up"]     = PATH_sys+"JET_EffectiveNP_Statistical6__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_Stat6_up"]     = PATH_sys+"JET_EffectiveNP_Statistical6__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_Stat6_up"] = PATH_sys+"JET_EffectiveNP_Statistical6__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION ETA-INT
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt_down"]  = PATH_sys+"JET_EtaIntercalibration_Modelling__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt_down"]     = PATH_sys+"JET_EtaIntercalibration_Modelling__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt_down"]     = PATH_sys+"JET_EtaIntercalibration_Modelling__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt_down"] = PATH_sys+"JET_EtaIntercalibration_Modelling__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION ETA-INT
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt_up"]  = PATH_sys+"JET_EtaIntercalibration_Modelling__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt_up"]     = PATH_sys+"JET_EtaIntercalibration_Modelling__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt_up"]     = PATH_sys+"JET_EtaIntercalibration_Modelling__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt_up"] = PATH_sys+"JET_EtaIntercalibration_Modelling__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION ETA-INT-HIGH-E
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_down"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_down"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION ETA-INT-HIGH-E
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_up"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-highE_up"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_highE__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION ETA-INT-NEG-ETA
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_down"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_down"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION ETA-INT-NEG-ETA
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_up"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-negEta_up"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_negEta__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION ETA-INT-POS-ETA
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_down"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_down"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_down"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION ETA-INT-POS-ETA
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_up"]  = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_up"]     = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-posEta_up"] = PATH_sys+"JET_EtaIntercalibration_NonClosure_posEta__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION ETA-INT-TOTAL-STAT
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_down"]  = PATH_sys+"JET_EtaIntercalibration_TotalStat__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_down"]     = PATH_sys+"JET_EtaIntercalibration_TotalStat__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_down"]     = PATH_sys+"JET_EtaIntercalibration_TotalStat__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_down"] = PATH_sys+"JET_EtaIntercalibration_TotalStat__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# VARIATION ETA-INT-TOTAL-STAT
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_up"]  = PATH_sys+"JET_EtaIntercalibration_TotalStat__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_up"]     = PATH_sys+"JET_EtaIntercalibration_TotalStat__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_up"]     = PATH_sys+"JET_EtaIntercalibration_TotalStat__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EtaInt-totalStat_up"] = PATH_sys+"JET_EtaIntercalibration_TotalStat__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION FLAVOR-COMPOSITION
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_FlavComp_down"]  = PATH_sys+"JET_Flavor_Composition__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_FlavComp_down"]     = PATH_sys+"JET_Flavor_Composition__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_FlavComp_down"]     = PATH_sys+"JET_Flavor_Composition__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_FlavComp_down"] = PATH_sys+"JET_Flavor_Composition__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_FlavComp_up"]  = PATH_sys+"JET_Flavor_Composition__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_FlavComp_up"]     = PATH_sys+"JET_Flavor_Composition__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_FlavComp_up"]     = PATH_sys+"JET_Flavor_Composition__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_FlavComp_up"] = PATH_sys+"JET_Flavor_Composition__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION FLAVOR-RESPONSE
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_FlavResp_down"]  = PATH_sys+"JET_Flavor_Response__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_FlavResp_down"]     = PATH_sys+"JET_Flavor_Response__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_FlavResp_down"]     = PATH_sys+"JET_Flavor_Response__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_FlavResp_down"] = PATH_sys+"JET_Flavor_Response__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_FlavResp_up"]  = PATH_sys+"JET_Flavor_Response__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_FlavResp_up"]     = PATH_sys+"JET_Flavor_Response__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_FlavResp_up"]     = PATH_sys+"JET_Flavor_Response__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_FlavResp_up"] = PATH_sys+"JET_Flavor_Response__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION MC16
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MC_down"]  = PATH_sys+"JET_JER_DataVsMC_MC16__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MC_down"]     = PATH_sys+"JET_JER_DataVsMC_MC16__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MC_down"]     = PATH_sys+"JET_JER_DataVsMC_MC16__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MC_down"] = PATH_sys+"JET_JER_DataVsMC_MC16__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MC_up"]  = PATH_sys+"JET_JER_DataVsMC_MC16__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MC_up"]     = PATH_sys+"JET_JER_DataVsMC_MC16__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MC_up"]     = PATH_sys+"JET_JER_DataVsMC_MC16__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MC_up"] = PATH_sys+"JET_JER_DataVsMC_MC16__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP1
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP1_down"]  = PATH_sys+"JET_JER_EffectiveNP_1__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP1_down"]     = PATH_sys+"JET_JER_EffectiveNP_1__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP1_down"]     = PATH_sys+"JET_JER_EffectiveNP_1__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP1_down"] = PATH_sys+"JET_JER_EffectiveNP_1__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP1_up"]  = PATH_sys+"JET_JER_EffectiveNP_1__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP1_up"]     = PATH_sys+"JET_JER_EffectiveNP_1__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP1_up"]     = PATH_sys+"JET_JER_EffectiveNP_1__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP1_up"] = PATH_sys+"JET_JER_EffectiveNP_1__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP2
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP2_down"]  = PATH_sys+"JET_JER_EffectiveNP_2__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP2_down"]     = PATH_sys+"JET_JER_EffectiveNP_2__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP2_down"]     = PATH_sys+"JET_JER_EffectiveNP_2__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP2_down"] = PATH_sys+"JET_JER_EffectiveNP_2__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP2_up"]  = PATH_sys+"JET_JER_EffectiveNP_2__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP2_up"]     = PATH_sys+"JET_JER_EffectiveNP_2__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP2_up"]     = PATH_sys+"JET_JER_EffectiveNP_2__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP2_up"] = PATH_sys+"JET_JER_EffectiveNP_2__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION NP3
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP3_down"]  = PATH_sys+"JET_JER_EffectiveNP_3__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP3_down"]     = PATH_sys+"JET_JER_EffectiveNP_3__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP3_down"]     = PATH_sys+"JET_JER_EffectiveNP_3__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP3_down"] = PATH_sys+"JET_JER_EffectiveNP_3__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP3_up"]  = PATH_sys+"JET_JER_EffectiveNP_3__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP3_up"]     = PATH_sys+"JET_JER_EffectiveNP_3__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP3_up"]     = PATH_sys+"JET_JER_EffectiveNP_3__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP3_up"] = PATH_sys+"JET_JER_EffectiveNP_3__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION NP4
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP4_down"]  = PATH_sys+"JET_JER_EffectiveNP_4__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP4_down"]     = PATH_sys+"JET_JER_EffectiveNP_4__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP4_down"]     = PATH_sys+"JET_JER_EffectiveNP_4__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP4_down"] = PATH_sys+"JET_JER_EffectiveNP_4__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP4_up"]  = PATH_sys+"JET_JER_EffectiveNP_4__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP4_up"]     = PATH_sys+"JET_JER_EffectiveNP_4__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP4_up"]     = PATH_sys+"JET_JER_EffectiveNP_4__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP4_up"] = PATH_sys+"JET_JER_EffectiveNP_4__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

# VARIATION NP5
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP5_down"]  = PATH_sys+"JET_JER_EffectiveNP_5__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP5_down"]     = PATH_sys+"JET_JER_EffectiveNP_5__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP5_down"]     = PATH_sys+"JET_JER_EffectiveNP_5__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP5_down"] = PATH_sys+"JET_JER_EffectiveNP_5__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP5_up"]  = PATH_sys+"JET_JER_EffectiveNP_5__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP5_up"]     = PATH_sys+"JET_JER_EffectiveNP_5__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP5_up"]     = PATH_sys+"JET_JER_EffectiveNP_5__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP5_up"] = PATH_sys+"JET_JER_EffectiveNP_5__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP6
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP6_down"]  = PATH_sys+"JET_JER_EffectiveNP_6__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP6_down"]     = PATH_sys+"JET_JER_EffectiveNP_6__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP6_down"]     = PATH_sys+"JET_JER_EffectiveNP_6__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP6_down"] = PATH_sys+"JET_JER_EffectiveNP_6__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP6_up"]  = PATH_sys+"JET_JER_EffectiveNP_6__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP6_up"]     = PATH_sys+"JET_JER_EffectiveNP_6__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP6_up"]     = PATH_sys+"JET_JER_EffectiveNP_6__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP6_up"] = PATH_sys+"JET_JER_EffectiveNP_6__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP7
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP7_down"]  = PATH_sys+"JET_JER_EffectiveNP_7__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP7_down"]     = PATH_sys+"JET_JER_EffectiveNP_7__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP7_down"]     = PATH_sys+"JET_JER_EffectiveNP_7__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP7_down"] = PATH_sys+"JET_JER_EffectiveNP_7__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP7_up"]  = PATH_sys+"JET_JER_EffectiveNP_7__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP7_up"]     = PATH_sys+"JET_JER_EffectiveNP_7__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP7_up"]     = PATH_sys+"JET_JER_EffectiveNP_7__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP7_up"] = PATH_sys+"JET_JER_EffectiveNP_7__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP8
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP8_down"]  = PATH_sys+"JET_JER_EffectiveNP_8__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP8_down"]     = PATH_sys+"JET_JER_EffectiveNP_8__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP8_down"]     = PATH_sys+"JET_JER_EffectiveNP_8__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP8_down"] = PATH_sys+"JET_JER_EffectiveNP_8__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP8_up"]  = PATH_sys+"JET_JER_EffectiveNP_8__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP8_up"]     = PATH_sys+"JET_JER_EffectiveNP_8__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP8_up"]     = PATH_sys+"JET_JER_EffectiveNP_8__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP8_up"] = PATH_sys+"JET_JER_EffectiveNP_8__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP9
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP9_down"]  = PATH_sys+"JET_JER_EffectiveNP_9__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP9_down"]     = PATH_sys+"JET_JER_EffectiveNP_9__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP9_down"]     = PATH_sys+"JET_JER_EffectiveNP_9__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP9_down"] = PATH_sys+"JET_JER_EffectiveNP_9__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP9_up"]  = PATH_sys+"JET_JER_EffectiveNP_9__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP9_up"]     = PATH_sys+"JET_JER_EffectiveNP_9__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP9_up"]     = PATH_sys+"JET_JER_EffectiveNP_9__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP9_up"] = PATH_sys+"JET_JER_EffectiveNP_9__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP10
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP10_down"]  = PATH_sys+"JET_JER_EffectiveNP_10__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP10_down"]     = PATH_sys+"JET_JER_EffectiveNP_10__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP10_down"]     = PATH_sys+"JET_JER_EffectiveNP_10__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP10_down"] = PATH_sys+"JET_JER_EffectiveNP_10__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP10_up"]  = PATH_sys+"JET_JER_EffectiveNP_10__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP10_up"]     = PATH_sys+"JET_JER_EffectiveNP_10__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP10_up"]     = PATH_sys+"JET_JER_EffectiveNP_10__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP10_up"] = PATH_sys+"JET_JER_EffectiveNP_10__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP11
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP11_down"]  = PATH_sys+"JET_JER_EffectiveNP_11__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP11_down"]     = PATH_sys+"JET_JER_EffectiveNP_11__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP11_down"]     = PATH_sys+"JET_JER_EffectiveNP_11__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP11_down"] = PATH_sys+"JET_JER_EffectiveNP_11__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP11_up"]  = PATH_sys+"JET_JER_EffectiveNP_11__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP11_up"]     = PATH_sys+"JET_JER_EffectiveNP_11__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP11_up"]     = PATH_sys+"JET_JER_EffectiveNP_11__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP11_up"] = PATH_sys+"JET_JER_EffectiveNP_11__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION NP12
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP12_down"]  = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP12_down"]     = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP12_down"]     = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP12_down"] = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_NP12_up"]  = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_NP12_up"]     = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_NP12_up"]     = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_NP12_up"] = PATH_sys+"JET_JER_EffectiveNP_12restTerm__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION PILEUP OFFSET MU
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUMU_down"]  = PATH_sys+"JET_Pileup_OffsetMu__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUMU_down"]     = PATH_sys+"JET_Pileup_OffsetMu__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUMU_down"]     = PATH_sys+"JET_Pileup_OffsetMu__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUMU_down"] = PATH_sys+"JET_Pileup_OffsetMu__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUMU_up"]  = PATH_sys+"JET_Pileup_OffsetMu__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUMU_up"]     = PATH_sys+"JET_Pileup_OffsetMu__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUMU_up"]     = PATH_sys+"JET_Pileup_OffsetMu__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUMU_up"] = PATH_sys+"JET_Pileup_OffsetMu__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION PILEUP OFFSET NPV
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUNPV_down"]  = PATH_sys+"JET_Pileup_OffsetNPV__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUNPV_down"]     = PATH_sys+"JET_Pileup_OffsetNPV__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUNPV_down"]     = PATH_sys+"JET_Pileup_OffsetNPV__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUNPV_down"] = PATH_sys+"JET_Pileup_OffsetNPV__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUNPV_up"]  = PATH_sys+"JET_Pileup_OffsetNPV__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUNPV_up"]     = PATH_sys+"JET_Pileup_OffsetNPV__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUNPV_up"]     = PATH_sys+"JET_Pileup_OffsetNPV__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUNPV_up"] = PATH_sys+"JET_Pileup_OffsetNPV__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION PILEUP OFFSET PT
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUPt_down"]  = PATH_sys+"JET_Pileup_PtTerm__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUPt_down"]     = PATH_sys+"JET_Pileup_PtTerm__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUPt_down"]     = PATH_sys+"JET_Pileup_PtTerm__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUPt_down"] = PATH_sys+"JET_Pileup_PtTerm__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUPt_up"]  = PATH_sys+"JET_Pileup_PtTerm__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUPt_up"]     = PATH_sys+"JET_Pileup_PtTerm__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUPt_up"]     = PATH_sys+"JET_Pileup_PtTerm__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUPt_up"] = PATH_sys+"JET_Pileup_PtTerm__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION PILEUP OFFSET RHO
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUrho_down"]  = PATH_sys+"JET_Pileup_RhoTopology__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUrho_down"]     = PATH_sys+"JET_Pileup_RhoTopology__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUrho_down"]     = PATH_sys+"JET_Pileup_RhoTopology__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUrho_down"] = PATH_sys+"JET_Pileup_RhoTopology__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_PUrho_up"]  = PATH_sys+"JET_Pileup_RhoTopology__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_PUrho_up"]     = PATH_sys+"JET_Pileup_RhoTopology__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_PUrho_up"]     = PATH_sys+"JET_Pileup_RhoTopology__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_PUrho_up"] = PATH_sys+"JET_Pileup_RhoTopology__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION PUNCH THROUGH
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_punch_down"]  = PATH_sys+"JET_PunchThrough_MC16__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_punch_down"]     = PATH_sys+"JET_PunchThrough_MC16__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_punch_down"]     = PATH_sys+"JET_PunchThrough_MC16__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_punch_down"] = PATH_sys+"JET_PunchThrough_MC16__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_punch_up"]  = PATH_sys+"JET_PunchThrough_MC16__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_punch_up"]     = PATH_sys+"JET_PunchThrough_MC16__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_punch_up"]     = PATH_sys+"JET_PunchThrough_MC16__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_punch_up"] = PATH_sys+"JET_PunchThrough_MC16__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION SINGLE THROUGH
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_single_down"]  = PATH_sys+"JET_SingleParticle_HighPt__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_single_down"]     = PATH_sys+"JET_SingleParticle_HighPt__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_single_down"]     = PATH_sys+"JET_SingleParticle_HighPt__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_single_down"] = PATH_sys+"JET_SingleParticle_HighPt__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_single_up"]  = PATH_sys+"JET_SingleParticle_HighPt__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_single_up"]     = PATH_sys+"JET_SingleParticle_HighPt__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_single_up"]     = PATH_sys+"JET_SingleParticle_HighPt__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_single_up"] = PATH_sys+"JET_SingleParticle_HighPt__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"


# VARIATION BJES
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_BJES_down"]  = PATH_sys+"JET_BJES_Response__1down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_BJES_down"]     = PATH_sys+"JET_BJES_Response__1down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_BJES_down"]     = PATH_sys+"JET_BJES_Response__1down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_BJES_down"] = PATH_sys+"JET_BJES_Response__1down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_BJES_up"]  = PATH_sys+"JET_BJES_Response__1up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_BJES_up"]     = PATH_sys+"JET_BJES_Response__1up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_BJES_up"]     = PATH_sys+"JET_BJES_Response__1up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_BJES_up"] = PATH_sys+"JET_BJES_Response__1up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_2022-02.root"

PATH_old = "/eos/user/n/nelsonc/W+jets/PlotterInputs/Systematics/"
# VARIATION MET SOFT TRACK RESOLUTION PARALLEL / PERPENDICULAR
# PARA    
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPara"]  = PATH_old+"MET_SoftTrk_ResoPara/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPara"]     = PATH_old+"MET_SoftTrk_ResoPara/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPara"]     = PATH_old+"MET_SoftTrk_ResoPara/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPara"] = PATH_old+"MET_SoftTrk_ResoPara/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Signal_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPara"]  = PATH_old+"MET_SoftTrk_ResoPara/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Zee_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPara"]     = PATH_old+"MET_SoftTrk_ResoPara/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Top_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPara"]     = PATH_old+"MET_SoftTrk_ResoPara/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPara"] = PATH_old+"MET_SoftTrk_ResoPara/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPara.root"
# PERP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPerp"]  = PATH_old+"MET_SoftTrk_ResoPerp/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPerp"]     = PATH_old+"MET_SoftTrk_ResoPerp/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPerp"]     = PATH_old+"MET_SoftTrk_ResoPerp/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_ResoPerp"] = PATH_old+"MET_SoftTrk_ResoPerp/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Signal_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPerp"]  = PATH_old+"MET_SoftTrk_ResoPerp/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Zee_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPerp"]     = PATH_old+"MET_SoftTrk_ResoPerp/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Top_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPerp"]     = PATH_old+"MET_SoftTrk_ResoPerp/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r_MET_SoftTrk_ResoPerp"] = PATH_old+"MET_SoftTrk_ResoPerp/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_ResoPerp.root"

# VARIATION MET SOFT TRACK SCALE
# DOWN    
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_down"]  = PATH_old+"MET_SoftTrk_Scale/down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_down"]     = PATH_old+"MET_SoftTrk_Scale/down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_down"]     = PATH_old+"MET_SoftTrk_Scale/down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_down"] = PATH_old+"MET_SoftTrk_Scale/down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Signal_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_down"]  = PATH_old+"MET_SoftTrk_Scale/down/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Zee_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_down"]     = PATH_old+"MET_SoftTrk_Scale/down/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Top_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_down"]     = PATH_old+"MET_SoftTrk_Scale/down/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_down"] = PATH_old+"MET_SoftTrk_Scale/down/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_down.root"

# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_up"]  = PATH_old+"MET_SoftTrk_Scale/up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_up"]     = PATH_old+"MET_SoftTrk_Scale/up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_up"]     = PATH_old+"MET_SoftTrk_Scale/up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_MET_SoftTrk_Scale_up"] = PATH_old+"MET_SoftTrk_Scale/up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Signal_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_up"]  = PATH_old+"MET_SoftTrk_Scale/up/WenuMC16aSherpa_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Zee_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_up"]     = PATH_old+"MET_SoftTrk_Scale/up/MC16aZee_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Top_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_up"]     = PATH_old+"MET_SoftTrk_Scale/up/MC16aTop_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"
InputFiles["Diboson_MC16a_EL_CR_DL1r_MET_SoftTrk_Scale_up"] = PATH_old+"MET_SoftTrk_Scale/up/MC16aDiboson_EL_CR_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_MET_SoftTrk_Scale_up.root"



# VARIATION ELECTRON RESOLUTION
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_down"]  = PATH_old+"EG_RESOLUTION_ALL/down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_down.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_down"]     = PATH_old+"EG_RESOLUTION_ALL/down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_down.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_down"]     = PATH_old+"EG_RESOLUTION_ALL/down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_down.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_down"] = PATH_old+"EG_RESOLUTION_ALL/down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_down.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_up"]  = PATH_old+"EG_RESOLUTION_ALL/up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_up.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_up"]     = PATH_old+"EG_RESOLUTION_ALL/up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_up.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_up"]     = PATH_old+"EG_RESOLUTION_ALL/up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_up.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EG_RESOLUTION_ALL_up"] = PATH_old+"EG_RESOLUTION_ALL/up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_RESOLUTION_ALL_up.root"


# VARIATION ELECTRON SCALE
# DOWN
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_down"]  = PATH_old+"EG_SCALE_ALL/down/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_down.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_down"]     = PATH_old+"EG_SCALE_ALL/down/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_down.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_down"]     = PATH_old+"EG_SCALE_ALL/down/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_down.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_down"] = PATH_old+"EG_SCALE_ALL/down/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_down.root"
# UP
InputFiles["Signal_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_up"]  = PATH_old+"EG_SCALE_ALL/up/WenuMC16aSherpa_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_up.root"
InputFiles["Zee_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_up"]     = PATH_old+"EG_SCALE_ALL/up/MC16aZee_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_up.root"
InputFiles["Top_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_up"]     = PATH_old+"EG_SCALE_ALL/up/MC16aTop_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_up.root"
InputFiles["Diboson_MC16a_EL_SRwoMET_DL1r_EG_SCALE_ALL_up"] = PATH_old+"EG_SCALE_ALL/up/MC16aDiboson_EL_SRwoMET_DL1rTagger_useSFs_useSampleWeights_usePRW_All_170821_EG_SCALE_ALL_up.root"


























