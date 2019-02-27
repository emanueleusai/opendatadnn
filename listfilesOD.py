import subprocess

# folder='/store/user/eusai/CRAB_PrivateMC/step1_pigun01/180417_002722/0000/'
# outname='step1_pigun01_list'
# folder='/store/user/eusai/CRAB_PrivateMC/step1_pigun02/180417_010257/0000/'
# outname='step1_pigun02_list'
# folder='/store/user/eusai/CRAB_PrivateMC/step1_pigun03/180417_010544/0000/'
# outname='step1_pigun03_list'
# folder='/store/user/eusai/CRAB_PrivateMC/step1_pigun04/180417_010927/0000/'
# outname='step1_pigun04_list'
# folder='/store/user/eusai/CRAB_PrivateMC/step1_pigun05/180417_012449/0000/'
# outname='step1_pigun05_list'
# folder='/store/user/eusai/CRAB_UserFiles/step3_pigun01/180421_014640/0000/'
# outname='step3_pigun01_list'
folder='/store/group/lpcml/eusai/lhe/'
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_01/190112_004020/',
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_02/190112_021438/',
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_03/190112_021505/',
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_04/190112_021540/',
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_05/190112_021607/',
 # '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD600to3000_06/190112_021631/'
#'/store/group/lpcml/eusai/CRAB_UserFiles/step1_QCD600to3000_01/190209_014953/',
#'/store/group/lpcml/eusai/CRAB_UserFiles/step1_QCD600to3000_02/190209_022632/'
# '/store/group/lpcml/eusai/CRAB_UserFiles/step2_QCD600to3000_01/190213_183439/',
# '/store/group/lpcml/eusai/CRAB_UserFiles/step2_QCD600to3000_02/190213_201625/'
# '/store/user/bburkle/E2E/opendata/step0/CRAB_UserFiles/step0_TtbarHad_00/190116_172403/',
# '/store/user/bburkle/E2E/opendata/step0/CRAB_UserFiles/step0_TtbarHad_01/190116_172524/',
# '/store/user/bburkle/E2E/opendata/step0/CRAB_UserFiles/step0_TtbarHad_02/190116_172614/',
# '/store/user/bburkle/E2E/opendata/step0/CRAB_UserFiles/step0_TtbarHad_03/190116_172738/'
# '/store/group/lpcml/eusai/CRAB_UserFiles/step1_TtbarFromOpen_02/190219_230502/'
#'/store/group/lpcml/eusai/CRAB_UserFiles/step3_QCD600to3000_01/190218_183745/'

 

sub=[
'Emanuele',
'Bjorn',
'Michael',
'Sitong',
'Daniel',
'Wenyu',
'Mary',
'Jess',
'Xavier',
'Jangbae',
]#,'0002/','0003/']#,'0004/']#,'0005/']

#folder='/store/group/lpcml/eusai/step2_ttbar_p8_03/'
outname='stepLHE_ttbarOD_'
#outname='step3_QCD600to300'

xrootd='root://cmsxrootd-site.fnal.gov/'


eosls=subprocess.check_output(['eos','root://cmseos.fnal.gov','ls',folder])
#print eosls
names=eosls.splitlines()
print len(names)/len(sub)
splitted = [names[i:i + len(names)/len(sub)] for i in range(0, len(names), len(names)/len(sub))]
print splitted
for i in range(len(sub)):
	outfile=open(outname+sub[i]+'.py','w')
	outfile.write('lhefiles=[\n')
	for j in splitted[i]:
		outfile.write('"'+xrootd+folder+j+'",\n')
	outfile.write(']\n')
	outfile.close()
