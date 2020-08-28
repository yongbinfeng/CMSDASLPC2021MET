from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'my_CRAB_project_directory'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'run_CMSDAS_MET_Exercise3_cfg.py'
config.JobType.outputFiles = ['cmsdas_met_exercise3.root']
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/user/saghosh/DASTEST/'
#config.Data.outLFNDirBase = '/store/user/loukas/DASTEST/'
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_CMSDAS2020_TRY'

config.section_("Site")
#config.Site.whitelist = ['T3_US_FNALLPC']
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_DE_RWTH'

config.section_("User")
config.User.voGroup = 'dcms'
