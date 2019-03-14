import subprocess

#filelist='step3_QCD300to600'
filelist='step3_QCD600to3000'
# filelist='step3_ttbarOD'
folder=filelist+'/'
select='save'

names=open(filelist,'r').read().splitlines() 
for name in names:
	if select in name:
		command=['xrdcp',name,'root://eospublic.cern.ch//eos/opendata/cms/upload/emanuele/'+folder]
		print command
		try:
			print subprocess.check_output(command)
		except subprocess.CalledProcessError:
			print 'duplicate file'