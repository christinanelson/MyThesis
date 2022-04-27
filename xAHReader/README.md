#########################################
# INSTRUCTIONS (last update 13/12/2019) #
#########################################

The main code (loop over events) is made in Reader.py

There are scripts with helper classes, functions and dicts

The lists of inputs are declared in InputLists.py

The different event selection options are declared in Selections.py

#######################
# Quick test on LXPLUS
#######################

1) Create file to save the output
$ mkdir Testing/

This will automatically run in debug mode, will run over a single file and a limited number of events

Take a look at LocalTest.py

Choose the channel (electron or muon) with Channel (EL or MU, respectively)

Choose the dataset type. The options are: ZmumuMC16xSherpa, ZeeMC16xSherpa, ZmumuMC16xMG, ZeeMC16xMG, Data15, Data16, Data17, Data18, MC16xTop, MC16xWenu, MC16xWmunu, MC16xDiboson (x = a,d,e)

If you want to use scale factors (SFs) set useSFs to True

If you want to use sample weights set useSampleWeights to True

If you want to fill reco distributions set fillReco to True

If you want to fill truth distributions set fillTruth to True

2) Run the python script in the following way:
$ python LocalTest.py

######################
# HTCondor submission
######################

Make sure to run in AFS, HTCondor is not available in EOS

0) (usually not needed)
The submission scripts are located in SubmissionsScripts/
They only need to be updated if InputLists.py or outPATH are updated
Update them in Prepare_Reader_SubmissionScripts.py (similar options as in LocalTest.py)

1) Run Tar.sh in the following way:
$ source Tar.sh

This will compress the following files in a tar.gz file which will be sent during submission (FilesForSubmission.tar.gz in the Submit/ folder):

Reader.py
Dicts.py
HelperClasses.py
HelperFunctions.py
Selections.py

If any of the above files are updated Tar.sh should be run again

2) Submit

To submit batch jobs, go to  Submit:
$ cd Submit/

Create a folder for the logs (it has to be called Logs!)

$ mkdir Logs

Take a look at Submit.py

You need to specify the channel, dataset, if you want to use SFs/SampleWeights/fillReco/fillTruth and the selection

Then run in the following way:

$ python Submit.py

Several jobs must have submitted

The logfiles will be automatically transferred to Submit/Logs and the outputs to the choosen outhPATH.

There is also a python script to merge output root files so we have a single file for each sample for the plotter

3) Monitoring

You can monitor them with:
$ condor_q

You can kill a given job with:
$ condor_rm JOB_ID

You can kill all jobs with:
$ condor_rm -all

You can also monitor a single job with:
$ condor_wait -status Logs/NAME.log

4) Retry (if jobs are in HOLD state)

Remove output files of HOLD (broken) batch jobs:
$ find *.root -size 0 | xargs rm

Run Submit.py script again (will send jobs only for the files w/o output files)
$ python Submit.py




