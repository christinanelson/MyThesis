import array

# Cutflow histograms
h_cutflow             = dict()
h_cutflow_all         = dict()
h_cutflow_trigger     = dict()
h_cutflow_jetCleaning = dict()
h_cutflow_met         = dict()
h_cutflow_lepPtEta    = dict()
h_cutflow_lepIP       = dict()
h_cutflow_lepID       = dict()
h_cutflow_lepIso      = dict()
h_cutflow_sigLepton   = dict()
h_cutflow_lepTrigMatch= dict()
h_cutflow_lepVeto     = dict()
h_cutflow_mT          = dict()
h_cutflow_OR          = dict()
h_cutflow_jet         = dict()
h_cutflow_bTagging    = dict()

# Histograms
Histograms    = dict()
Histograms_2D = dict()

################################
# Binning of observables
################################

# Binning given by array
Binning       = dict()
Binning_array = dict()
# Wmass (mT)
Binning['mT']                  = [0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.,80.,90.,100.,200.,500.,1000.,2000.,4000.]
Binning_array['mT']            = array.array('d',Binning['mT'])
# HT
Binning['ht']             = [0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.,80.,90.,100.,200.,500.,1000.,2000.,4000.,10000.]
Binning_array['ht']       = array.array('d',Binning['ht'])
# MET
Binning['met']            = [0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95.,100.,105.,110.,115.,120.,125.,130.,135.,140.,145.,150,155.,160.,165.,170.,175.,180.,185.,190.,195.,200.,205.,210.,215.,220.,225.,230.,235.,240.,245.,250.,255.,260.,265.,270.,275.,280.,285.,290.,295.,300.,305.,310.,315.,320.,325.,330.,335.,340.,345.,350.,400.,450.,500.,1000.,2000.,4000.]
Binning_array['met']      = array.array('d',Binning['met'])
# Jet pT
Binning['jet_pt']         = [20.,30.,40.,50.,100.,200.,500.,1000.,2000.,4000.]
Binning_array['jet_pt']   = array.array('d',Binning['jet_pt'])
Binning['j0_pt']          = Binning['jet_pt']
Binning_array['j0_pt']    = array.array('d',Binning['jet_pt'])
Binning['j1_pt']          = Binning['jet_pt']
Binning_array['j1_pt']    = array.array('d',Binning['jet_pt'])
Binning['j2_pt']          = Binning['jet_pt']
Binning_array['j2_pt']    = array.array('d',Binning['jet_pt'])
# deltaRjj and deltaYjj
Binning['deltaRjj']         = [0, 0.4, 0.9, 1.3, 1.8, 2.3, 2.7, 3.1, 3.5, 4.0, 5.0, 6.3]
Binning_array['deltaRjj']   = array.array('d',Binning['deltaRjj'])
Binning['deltaYjj']         = Binning['deltaRjj']
Binning_array['deltaYjj']   = Binning_array['deltaRjj']
Binning['deltaRjlep']       = Binning['deltaRjj']
Binning_array['deltaRjlep'] = Binning_array['deltaRjj']
# Lepton pT
Binning['lep_pt']         = [0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.,80.,90.,100.,200.,500.,1000.,2000.,4000.]
Binning_array['lep_pt']   = array.array('d',Binning['lep_pt'])
# Binning given by nBins, minVal and maxVal
# deltaPhijj
Binning['deltaPhijj']     = [12,0,3.15]
# njet
Binning['njet']           = [20,-0.5,19.5]
# Jet eta / rapidity
Binning['jet_eta']        = [500,-4.5,4.5]
Binning['j0_eta']         = Binning['jet_eta']
Binning['j1_eta']         = Binning['jet_eta']
Binning['j2_eta']         = Binning['jet_eta']
Binning['jet_y']          = Binning['jet_eta']
Binning['j0_y']           = Binning['jet_eta']
Binning['j1_y']           = Binning['jet_eta']
Binning['j2_y']           = Binning['jet_eta']
# Jet phi
Binning['jet_phi']        = [500,-3.25,3.25]
Binning['j0_phi']         = Binning['jet_phi'] 
Binning['j1_phi']         = Binning['jet_phi'] 
Binning['j2_phi']         = Binning['jet_phi'] 
# mjj
Binning['mjj']            = [500, 0, 5000]
# Lepton eta
Binning['lep_eta']        = [500,-2.5,2.5]
# Lepton phi
Binning['lep_phi']        = [500,-3.25,3.25]
