#!/usr/bin/env bash
text="\nprocess.maxEvents.input = cms.untracked.int32(1000)\nprocess.source.skipEvents = cms.untracked.uint32(0)\n"
printf "$text" >> PSet.py
cmsRun -j FrameworkJobReport.xml -p PSet.py