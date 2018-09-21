import subprocess

inputfolder=['/mnt/hadoop/store/user/eusai/CRAB_PrivateMC/open_ttbar_p8_03/180914_183255/','/mnt/hadoop/store/user/eusai/CRAB_PrivateMC/open_qcd_p8_03/180914_183152/']
outputfolder=['/store/group/lpcml/eusai/open_ttbar_p8_03/','/store/group/lpcml/eusai/open_qcd_p8_03/']
subfolders=['0000/','0001/','0002/','0003/','0004/','0005/']
select='step0'


for index in [0,1]:
	for i in subfolders:
		names=subprocess.check_output(['ls','-1',inputfolder[index]+i]).splitlines() 
		for name in names:
			if select in name:
				command=['xrdcp',inputfolder[index]+i+name,'root://cmseos.fnal.gov/'+outputfolder[index]]
				print command
				try:
					print subprocess.check_output(command)
				except subprocess.CalledProcessError:
					print 'duplicate file'

