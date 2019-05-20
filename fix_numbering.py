import subprocess,sys

folders=[
'step2_QCD300to600',
'step2_QCD400to600',
'step2_QCD_600to3000_01',
'step2_QCD_600to3000_02',
'step2_ttbarOD_01',
'step2_ttbarOD_02',
'step2_ttbarOD_03',
'step2_ttbarOD_04',
'step2_ttbarOD_05',
'step3_QCD300to600',
'step3_QCD400to600',
'step3_QCD600to3000',
'step3_ttbarOD',
]


# step2_OpenData_1002.root
# savehits_output_1006.root

for folder in folders:
	filelist=subprocess.check_output(['eos','root://eospublic.cern.ch/','ls','-1','/eos/opendata/cms/upload/emanuele/'+folder])
	files=filelist.split('\n')[:-1]
	#print files
	for file in files:
		number=file.split('_')[-1].split('.')[0]
		# if len(number)>4:
		# 	print number
		# 	fix_number=number[:-2]
		# 	print fix_number
		# 	file_fix=file.replace('15.root','.root')
		# 	command=['eos','root://eospublic.cern.ch/','mv','/eos/opendata/cms/upload/emanuele/'+folder+'/'+file,'/eos/opendata/cms/upload/emanuele/'+folder+'/'+file_fix]
		# 	print command
		# 	print subprocess.check_output(command)
		if len(number)!=4:
			fix_number='0'*(4-len(number))+number
			file_fix=file.replace(number+'.root',fix_number+'.root')
			command=['eos','root://eospublic.cern.ch/','mv','/eos/opendata/cms/upload/emanuele/'+folder+'/'+file,'/eos/opendata/cms/upload/emanuele/'+folder+'/'+file_fix]
			print command
			print subprocess.check_output(command)


