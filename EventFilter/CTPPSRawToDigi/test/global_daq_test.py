import FWCore.ParameterSet.Config as cms

process = cms.Process("TotemIntegratedRawDataTest")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
    statistics = cms.untracked.vstring(),
    destinations = cms.untracked.vstring('cerr'),
    cerr = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    )
)

# raw data source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      "file:/afs/cern.ch/user/j/jkaspar/public/run268608_ls0001_streamA_StorageManager.root",
      "file:/afs/cern.ch/user/j/jkaspar/public/run281994.root"
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# raw-to-digi conversion
process.load('CondFormats.CTPPSReadoutObjects.TotemDAQMappingESSourceXML_cfi')
process.TotemDAQMappingESSourceXML.mappingFileNames.append("CondFormats/CTPPSReadoutObjects/xml/ctpps_210_mapping.xml")

process.load("EventFilter.CTPPSRawToDigi.totemTriggerRawToDigi_cfi")
process.totemTriggerRawToDigi.rawDataTag = cms.InputTag("rawDataCollector")

process.load('EventFilter.CTPPSRawToDigi.totemRPRawToDigi_cfi')
process.totemRPRawToDigi.rawDataTag = cms.InputTag("rawDataCollector")

# execution configuration
process.p = cms.Path(
    process.totemTriggerRawToDigi *
    process.totemRPRawToDigi
)
