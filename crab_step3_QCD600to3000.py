from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

the_name='step3_QCD600to3000_01'
config.General.requestName = the_name
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_QCDPt_15_3000_Flat_V27.py'
config.JobType.maxMemoryMB = 2500
config.JobType.outputFiles = ["savehits_output.root"]
#config.JobType.maxJobRuntimeMin = 4320
#config.JobType.numCores = 4

#config.Data.inputDataset = '/SinglePiPt100Eta1p6_2p8/PhaseIITDRFall17DR-noPUFEVT_93X_upgrade2023_realistic_v2-v1/GEN-SIM-RECO'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/lpcml/eusai/'# % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = the_name
config.Data.ignoreLocality = True
#config.Data.totalUnits = 100000
config.Data.userInputFiles = open('step2_QCDPt_15to3000').readlines()
#Data.outputPrimaryDataset

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.ignoreGlobalBlacklist = True
# config.Site.whitelist = ['T2_US_*']
config.Site.whitelist = ['T2_AT_*','T2_BE_*','T2_BR_*','T2_CH_*','T2_CN_*','T2_DE_*','T2_EE_*','T2_ES_CIEMAT','T2_FI_*','T2_FR_*','T2_GR_*','T2_HU_*','T2_IN_*','T2_IT_*','T2_KR_*','T2_MY_*','T2_PK_*','T2_PL_*','T2_PT_*','T2_RU_*','T2_TH_*','T2_TR_*','T2_TW_*','T2_UA_*','T2_UK_*','T2_US_*','T3_BG_*','T3_BY_*','T3_CH_*','T3_CN_*','T3_CO_*','T3_ES_*','T3_FR_*','T3_GR_*','T3_HU_*','T3_IN_*','T3_IT_*','T3_KR_*','T3_MX_*','T3_RU_*','T3_TW_*','T3_UK_*','T3_US_*']
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.blacklist = ['T2_US_Florida']