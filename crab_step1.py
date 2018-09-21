from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

the_name='open_qcd_p8_step1_03'
config.General.requestName = the_name
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1_qcd.py'
config.JobType.maxMemoryMB = 2500
#config.JobType.maxJobRuntimeMin = 4320
#config.JobType.numCores = 4

#config.Data.inputDataset = '/SinglePiPt100Eta1p6_2p8/PhaseIITDRFall17DR-noPUFEVT_93X_upgrade2023_realistic_v2-v1/GEN-SIM-RECO'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = the_name
config.Data.ignoreLocality = True
#config.Data.totalUnits = 100000
config.Data.userInputFiles = open('open_qcd_p8_03').readlines()
#Data.outputPrimaryDataset

config.Site.storageSite = 'T3_US_Brown'
#config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ['T2_US_*','T3_US_*']
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.blacklist = ['T2_US_Florida']