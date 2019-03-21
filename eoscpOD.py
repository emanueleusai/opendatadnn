import subprocess,sys
filelist=sys.argv[1]
folder=filelist+'/'
select='.root'

try:
	print subprocess.check_output(['eos','root://eospublic.cern.ch/','mkdir','/eos/opendata/cms/upload/emanuele/'+folder])
except subprocess.CalledProcessError:
	print 'folder exists'

names=open(filelist,'r').read().splitlines() 
for name in names:
	if select in name:
		command=['xrdcp',name,'root://eospublic.cern.ch//eos/opendata/cms/upload/emanuele/'+folder]
		print command
		try:
			print subprocess.check_output(command)
		except subprocess.CalledProcessError:
			print 'duplicate file'