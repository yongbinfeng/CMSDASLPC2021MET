#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor


from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ExampleAnalysis(Module):
    def __init__(self):
	self.writeHistFile=True
	self.puppimetBranchName= "PuppiMET"
	self.rawmetBranchName= "RawMET"
	self.pfmetBranchName= "MET"
        self.flagBranchName= "Flag"

    def beginJob(self,histFile=None,histDirName=None):
	Module.beginJob(self,histFile,histDirName)

	self.h_rawmet=ROOT.TH1F('rawmet',   'rawmet',   25, 0, 500)
	self.h_pfmet=ROOT.TH1F('pfmet',   'pfmet',   25, 0, 500)
	self.h_puppimet=ROOT.TH1F('puppimet',   'puppimet',   25, 0, 500)
        self.addObject(self.h_rawmet )
        self.addObject(self.h_pfmet )
        self.addObject(self.h_puppimet )

    def analyze(self, event):
        jets = Collection(event, "Jet")
        muons = Collection(event, "Muon")
        pfmet = Object(event, self.pfmetBranchName)
        rawmet = Object(event, self.rawmetBranchName)
        puppimet = Object(event, self.puppimetBranchName)
        flag= Object(event,self.flagBranchName)


        #print flag.goodVertices, flag.HBHENoiseFilter, flag.HBHENoiseIsoFilter, flag.EcalDeadCellTriggerPrimitiveFilter, flag.BadPFMuonFilter, flag.ecalBadCalibFilter
        if (flag.goodVertices  == False or flag.HBHENoiseFilter == False or flag.HBHENoiseIsoFilter  == False or flag.EcalDeadCellTriggerPrimitiveFilter  == False or  flag.BadPFMuonFilter  == False or flag.ecalBadCalibFilter == False) : return False


	#select events with at least 2 muons
	if len(muons) >=2 :
          
	  self.h_rawmet.Fill(rawmet.pt) #fill histogram
          self.h_pfmet.Fill(pfmet.pt) #fill histogram
	  self.h_puppimet.Fill(puppimet.pt) #fill histogram
        return True


preselection="Jet_pt[0] > 250"
files=["root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv6/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/60000/AF2405EC-2325-3A44-B7C2-AE7616557973.root"]
#files=[" root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/2CE738F9-C212-E811-BD0E-EC0D9A8222CE.root"]
p=PostProcessor(".",files,cut=preselection,branchsel=None,modules=[ExampleAnalysis()],noOut=True,histFileName="histOut.root",histDirName="plots")
p.run()


