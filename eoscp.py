import subprocess

folder='/store/user/eusai/CRAB_UserFiles/step3_dipigun03/180619_225942/0000/'
outfolder='/mnt/hadoop/store/user/eusai/step3_dipigun03/'
select='step3'

names=open('out3','r').read().splitlines() 
for name in names:
	if select in name:
		command=['xrdcp','root://cmseos.fnal.gov/'+folder+name,outfolder]
		print command
		try:
			print subprocess.check_output(command)
		except subprocess.CalledProcessError:
			print 'duplicate file'