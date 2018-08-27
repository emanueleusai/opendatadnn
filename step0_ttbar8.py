# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: SinglePiE1000_cfi.py --fileout file:step0_qcd6.root --mc --step GEN,SIM --eventcontent RAWSIM --datatier GEN-SIM --conditions START53_V27::All --python_filename step0_qcd6.py --no_exec -n 1000
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    # annotation = cms.untracked.string('SinglePiE1000_cfi.py nevts:1000'),
    annotation = cms.untracked.string('Summer2012-Z2star sample with PYTHIA6: QCD dijet production, pThat = 15 .. 3000 GeV, weighted, TuneZ2star'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:step0_ttbar8.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

# process.generator = cms.EDProducer("FlatRandomEGunProducer",
#     PGunParameters = cms.PSet(
#         PartID = cms.vint32(211),
#         MaxEta = cms.double(5.0),
#         MaxPhi = cms.double(3.14159265359),
#         MinEta = cms.double(-5.0),
#         MinE = cms.double(999.99),
#         MinPhi = cms.double(-3.14159265359),
#         MaxE = cms.double(1000.01)
#     ),
#     Verbosity = cms.untracked.int32(0),
#     psethack = cms.string('single pi E 1000'),
#     AddAntiParticle = cms.bool(True),
#     firstRun = cms.untracked.uint32(1)
# )

# process.generator = cms.EDFilter("Pythia8GeneratorFilter",
#     comEnergy = cms.double(8000.0),
#     crossSection = cms.untracked.double(1.246406e+09),
#     filterEfficiency = cms.untracked.double(1),
#     maxEventsToPrint = cms.untracked.int32(0),
#     pythiaHepMCVerbosity = cms.untracked.bool(False),
#     pythiaPylistVerbosity = cms.untracked.int32(0),
#     # useUserHook = cms.bool(True),

#     PythiaParameters = cms.PSet(
#         processParameters = cms.vstring(
#             'Main:timesAllowErrors    = 10000',
#             'ParticleDecays:limitTau0 = on',
#             'ParticleDecays:tauMax = 10',
#             'HardQCD:all = on',
#             'PhaseSpace:pTHatMin = 15',
#             'PhaseSpace:pTHatMax = 3000',
#             'Tune:pp 5',
#             'Tune:ee 3',

#         ),
#         parameterSets = cms.vstring('processParameters')
#     )
# )

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),

    crossSection = cms.untracked.double(159.6),
    
    PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
                        'Top:gg2ttbar    = on',
                        'Top:qqbar2ttbar = on',
                        '6:m0 = 172.5',    # top mass',
        ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CUEP8M1Settings',
                                        'processParameters',
                                        )
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

