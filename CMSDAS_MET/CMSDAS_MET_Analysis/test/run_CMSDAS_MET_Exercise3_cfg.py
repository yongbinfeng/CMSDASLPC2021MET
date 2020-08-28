import FWCore.ParameterSet.Config as cms

process = cms.Process("CMSDASMET")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.TFileService = cms.Service("TFileService",
    fileName = cms.string("cmsdas_met_exercise3.root"),
    closeFileFast = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring([
            #'/store/user/cmsdas/2019/short_exercises/METAndPU/data/handson1_dylljets_amcatnlo.root',
            '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FFDCFC59-4ABE-0646-AABE-BD5D65301169.root',
            ]
                                      )
    )

process.cmsdasmetexercise3 = cms.EDAnalyzer('CMSDAS_MET_AnalysisExercise3',
                                   vertices  = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                   mets       = cms.InputTag("slimmedMETs"),
                                   metspuppi  = cms.InputTag("slimmedMETsPuppi"),
                                   muons     = cms.InputTag("slimmedMuons"),
                                   )


process.p = cms.Path(process.cmsdasmetexercise3)
