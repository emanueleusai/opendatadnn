from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

the_name='step0_TtbarHad_00'
config.General.requestName = the_name
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step0_ttbar_V27.py'
config.JobType.maxMemoryMB = 2500
config.JobType.numCores = 1
config.JobType.scriptExe = 'run0.sh'

#config.Data.inputDataset = '/SinglePiPt100Eta1p6_2p8/PhaseIITDRFall17DR-noPUFEVT_93X_upgrade2023_realistic_v2-v1/GEN-SIM-RECO'
#config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.userInputFiles = open('CMS_MonteCarlo2012_Summer12_DR53X_TTJets_HadronicMGDecays_8TeV-madgraph_AODSIM_PU_RD1_START53_V7N-v1_10000_file_index.txt').read().splitlines()+\
							 open('CMS_MonteCarlo2012_Summer12_DR53X_TTJets_HadronicMGDecays_8TeV-madgraph_AODSIM_PU_RD1_START53_V7N-v1_10001_file_index.txt').read().splitlines()+\
							 open('CMS_MonteCarlo2012_Summer12_DR53X_TTJets_HadronicMGDecays_8TeV-madgraph_AODSIM_PU_RD1_START53_V7N-v1_10002_file_index.txt').read().splitlines()+\
							 open('CMS_MonteCarlo2012_Summer12_DR53X_TTJets_HadronicMGDecays_8TeV-madgraph_AODSIM_PU_RD1_START53_V7N-v1_10003_file_index.txt').read().splitlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 1000 
config.Data.outLFNDirBase = '/store/group/lpcml/eusai/'# % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = the_name
config.Data.ignoreLocality = True
#config.Data.totalUnits = 500000

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ['T2_US_*']
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.blacklist = ['T2_US_Florida']