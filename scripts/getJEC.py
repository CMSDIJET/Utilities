import FWCore.ParameterSet.Config as cms
process = cms.Process("jectxt")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# define your favorite global tag
process.GlobalTag.globaltag = '74X_HLT_mcRun2_asymptotic_fromSpring15DR_v0'
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.readJetCorr    = cms.EDAnalyzer('JetCorrectorDBReader',

                                      # below is the communication to the database
                                      payloadName    = cms.untracked.string('AK4PFchs'),
                                      #payloadName    = cms.untracked.string('AK4PF'),
                                      #payloadName    = cms.untracked.string('AK5Calo'),

                                      # this is used ONLY for the name of the printed txt files. You can use any name that you like,
                                      # but it is recommended to use the GT name that you retrieved the files from.
                                      globalTag      = cms.untracked.string('74X_HLT_mcRun2_asymptotic_fromSpring15DR_v0'),
                                      printScreen    = cms.untracked.bool(False),
                                      createTextFile = cms.untracked.bool(True)
                                      )

process.p = cms.Path(process.readJetCorr)
