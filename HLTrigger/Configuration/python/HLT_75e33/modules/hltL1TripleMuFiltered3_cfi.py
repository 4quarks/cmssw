import FWCore.ParameterSet.Config as cms

hltL1TripleMuFiltered3 = cms.EDFilter("L1TTkMuonFilter",
    MaxEta = cms.double(2.4),
    MinEta = cms.double(-2.4),
    MinN = cms.int32(3),
    MinPt = cms.double(3.0),
    Scalings = cms.PSet(
        barrel = cms.vdouble(0.820128, 1.04124, 0.0),
        endcap = cms.vdouble(0.864715, 1.03215, 0.0),
        overlap = cms.vdouble(0.920897, 1.03712, 0.0)
    ),
    inputTag = cms.InputTag("hltL1TkMuons"),
    saveTags = cms.bool(True)
)
