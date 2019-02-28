from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

the_name='step0_ttbarOD_Daniel'
config.General.requestName = the_name
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step0_ttbarOD_Daniel.py'
config.JobType.maxMemoryMB = 2000
config.JobType.numCores = 1

#config.Data.inputDataset = '/SinglePiPt100Eta1p6_2p8/PhaseIITDRFall17DR-noPUFEVT_93X_upgrade2023_realistic_v2-v1/GEN-SIM-RECO'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 200
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = the_name
config.Data.ignoreLocality = True
config.Data.totalUnits = 1000000

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ['T2_US_*,','T3_US_*','T2_CH_*,','T3_CH_*','T2_IT_*,','T3_IT_*','T2_DE_*,','T3_DE_*','T2_FR_*,','T3_FR_*',]
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.blacklist = ['T2_US_Florida']
