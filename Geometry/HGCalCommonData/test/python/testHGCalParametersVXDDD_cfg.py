###############################################################################
# Way to use this:
#   cmsRun testHGCalParametersVXDDD_cfg.py type=V17
#
#   Options for type V15, V16, V17
#
###############################################################################
import FWCore.ParameterSet.Config as cms
import os, sys, imp, re
import FWCore.ParameterSet.VarParsing as VarParsing

####################################################################
### SETUP OPTIONS
options = VarParsing.VarParsing('standard')
options.register('type',
                 "V17",
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "type of operations: V15, V16, V17")

### get and parse the command line arguments
options.parseArguments()
print(options)

from Configuration.Eras.Era_Phase2C11_cff import Phase2C11

process = cms.Process("HGCalParametersTest",Phase2C11)

####################################################################
# Use the options
if (options.type == "V15"):
    process.load("Geometry.HGCalCommonData.testHGCalV15XML_cfi")
elif (options.type == "V16"):
    process.load("Geometry.HGCalCommonData.testHGCalV16XML_cfi")
else:
    process.load("Geometry.HGCalCommonData.testHGCalV17XML_cfi")

process.load("SimGeneral.HepPDTESSource.pdt_cfi")
process.load("Geometry.HGCalCommonData.hgcalV15ParametersInitialization_cfi")
process.load('FWCore.MessageService.MessageLogger_cfi')

if hasattr(process,'MessageLogger'):
    process.MessageLogger.HGCalGeom=dict()

process.load("IOMC.RandomEngine.IOMC_cff")
process.RandomNumberGeneratorService.generator.initialSeed = 456789

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(14),
        MinEta = cms.double(-3.5),
        MaxEta = cms.double(3.5),
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        MinE   = cms.double(9.99),
        MaxE   = cms.double(10.01)
    ),
    AddAntiParticle = cms.bool(False),
    Verbosity       = cms.untracked.int32(0),
    firstRun        = cms.untracked.uint32(1)
)
 
process.load("Geometry.HGCalCommonData.hgcParameterTesterEE_cfi")

process.hgcParameterTesterHESil = process.hgcParameterTesterEE.clone(
    Name = cms.string("HGCalHESiliconSensitive")
)

process.hgcParameterTesterHESci = process.hgcParameterTesterEE.clone(
    Name = cms.string("HGCalHEScintillatorSensitive"),
    Mode = cms.int32(2)
)
 
process.p1 = cms.Path(process.generator*process.hgcParameterTesterEE*process.hgcParameterTesterHESil*process.hgcParameterTesterHESci)
