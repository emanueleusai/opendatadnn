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
folders=[
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

#'/store/group/lpcml/eusai/CRAB_UserFiles/step3_TtbarFromOpen_02/190221_230406/'

#'/store/group/lpcml/eusai/CRAB_PrivateMC/step0_ttbarOD_03/190303_035256/', #Emanuele
#'/store/user/bburkle/E2E/opendata/ttbar_production/CRAB_PrivateMC/step0_ttbarOD_Bjorn/190301_215422/', #Bjorn

#'/store/group/lpcml/mandrews/CRAB_PrivateMC/step0_ttbarOD_Michaelv2/190302_233412/', #Michael
#'/store/group/lpcml/CRAB_PrivateMC/step0_ttbarOD_Sitong/190301_181405/', #Sitong

#'/store/group/lpcljm/CRAB_PrivateMC/step0_ttbarOD_Wenyu/190301_001435/', #Wenyu
#'/store/group/lpcljm/CRAB_PrivateMC/step0_ttbarOD_Jess/190302_145418/', #Jess

#'/store/user/dsunyou/CRAB_PrivateMC/step0_ttbarOD_Daniel/190302_022008/', #Daniel
#'/store/user/mhadley/CRAB_PrivateMC/step0_ttbarOD_Mary_v2/190301_222331/', #Mary
#'/store/user/mhadley/CRAB_PrivateMC/step0_ttbarOD_Mary/190301_000255/', #Mary

#'/store/group/lpcml/eusai/CRAB_PrivateMC/step0_ttbarOD_Xavier/190304_051928/', #Xavier
#'/store/user/jblee/CRAB_PrivateMC/step0_ttbarOD_Jangbae/190304_154655/', #Jangbae

# '/store/user/gbenelli/CRAB_PrivateMC/step0_QCD300to600/190301_203149/', #Gabriele
# '/store/group/lpcljm/CRAB_PrivateMC/step0_QCD300to600/190304_215657/', #Meenakshi
# '/store/group/lpcml/eusai/CRAB_PrivateMC/step0_QCD300to600/190302_041540/', #Emanuele QCD

#'/store/group/lpcml/eusai/CRAB_UserFiles/step1_QCD300to600_01/190306_030339/',
# '/store/group/lpcml/CRAB_UserFiles/step1_ttbarOD_EmBj_01/190306_164221/',
 #'/store/group/lpcml/CRAB_UserFiles/step1_ttbarOD_MaDa_01/190306_221626/',
 #'/store/group/lpcml/CRAB_UserFiles/step1_ttbarOD_MiSi_01/190306_211312/',
#'/store/group/lpcljm/CRAB_UserFiles/step1_ttbarOD_WeJe_01/190306_173032/',
#'/store/group/lpcml/eusai/CRAB_UserFiles/step1_ttbarOD_XaJa_01/190306_191546/',
#'/store/group/lpcml/eusai/CRAB_UserFiles/step2_QCD300to600_01/190308_185209/',
# '/store/group/lpcml/CRAB_UserFiles/step2_ttbarOD_EmBj_01/190308_200019/',
# '/store/group/lpcml/eusai/CRAB_UserFiles/step2_ttbarOD_MaDa_01/190309_215834/',
# '/store/group/lpcml/CRAB_UserFiles/step2_ttbarOD_MiSi_01/190309_221351/',
# '/store/group/lpcljm/CRAB_UserFiles/step2_ttbarOD_WeJe_01/190308_200010/',
# '/store/group/lpcml/eusai/CRAB_UserFiles/step2_ttbarOD_XaJa_01/190308_190833/',

#'/store/group/lpcml/eusai/CRAB_UserFiles/step3_QCD300to600_01/190312_064617/',
# '/store/group/lpcml/eusai/CRAB_UserFiles/step3_QCD600to3000_01/190312_064406/',
# '/store/group/lpcml/eusai/CRAB_UserFiles/step3_ttbarOD_01/190312_064817/',

# '/store/group/lpcml/CRAB_PrivateMC/step0_QCD400to600/190314_003535/',
# '/store/group/lpcml/CRAB_PrivateMC/step0_QCD400to600_E/190314_003928/',

#'/store/group/lpcml/eusai/CRAB_UserFiles/step3_QCD400to600_01/190320_173946/',

'/eos/opendata/cms/upload/emanuele/step2_QCD300to600/',
'/eos/opendata/cms/upload/emanuele/step2_QCD400to600/',
'/eos/opendata/cms/upload/emanuele/step2_QCD_600to3000_01/',
'/eos/opendata/cms/upload/emanuele/step2_QCD_600to3000_02/',
'/eos/opendata/cms/upload/emanuele/step2_ttbarOD_01/',
'/eos/opendata/cms/upload/emanuele/step2_ttbarOD_02/',
'/eos/opendata/cms/upload/emanuele/step2_ttbarOD_03/',
'/eos/opendata/cms/upload/emanuele/step2_ttbarOD_04/',
'/eos/opendata/cms/upload/emanuele/step2_ttbarOD_05/',
'/eos/opendata/cms/upload/emanuele/step3_QCD300to600/',
'/eos/opendata/cms/upload/emanuele/step3_QCD400to600/',
'/eos/opendata/cms/upload/emanuele/step3_QCD600to3000/',
'/eos/opendata/cms/upload/emanuele/step3_ttbarOD/',

 ]

sub=['']#['0000/','0001/','0002/','0003/']#,'0004/','0005/']#,'0006/','0007/','0008/','0009/','0010/']

#folder='/store/group/lpcml/eusai/step2_ttbar_p8_03/'
#outname='step3_TtbarFromOpen'
#outname='step3_QCD600to300'
outnames=[

'step2_QCD300to600_OD',
'step2_QCD400to600_OD',
'step2_QCD_600to3000_01_OD',
'step2_QCD_600to3000_02_OD',
'step2_ttbarOD_01_OD',
'step2_ttbarOD_02_OD',
'step2_ttbarOD_03_OD',
'step2_ttbarOD_04_OD',
'step2_ttbarOD_05_OD',
'step3_QCD300to600_OD',
'step3_QCD400to600_OD',
'step3_QCD600to3000_OD',
'step3_ttbarOD_OD',

#'step0_ttbarOD_Emanuele',
#'step0_ttbarOD_Bjorn',

#'step0_ttbarOD_Michael',
#'step0_ttbarOD_Sitong',

#'step0_ttbarOD_Wenyu',
#'step0_ttbarOD_Jess',

# 'step0_ttbarOD_Daniel_2',
# 'step0_ttbarOD_Mary_2',
#'step0_ttbarOD_Maryv2',

#'step0_ttbarOD_Xavier',
#'step0_ttbarOD_Jangbae',

# 'step0_QCD300to600_Gabriele',
# 'step0_QCD300to600_Meenakshi',
# 'step0_QCD300to600_Emanuele',

# 'step1_QCD300to600',
# 'step1_ttbarOD_EmBj',
 #'step1_ttbarOD_MaDa',
 #'step1_ttbarOD_MiSi',
#'step1_ttbarOD_WeJe',
# 'step1_ttbarOD_XaJa',

# 'step2_QCD300to600',

#'step3_QCD300to600',
# 'step3_QCD600to3000',
# 'step3_ttbarOD',

# 'step0_QCD400to600',
# 'step0_QCD400to600_E',

 #'step3_QCD400to600',
]

xrootd='root://eospublic.cern.ch/'
#xrootd='root://cmseos.fnal.gov/'

for i in range(len(folders)):
	outfile=open(outnames[i],'w')
	for j in sub:
		folder=folders[i]+j
		eosls=subprocess.check_output(['eos','root://eospublic.cern.ch/','ls',folder])
		#print eosls
		names=eosls.splitlines()
		if 'log' in names:
			names.remove('log')
		if 'failed' in names:
			names.remove('failed')
		for k in names:
			outfile.write(xrootd+folder+k+'\n')
	outfile.close()


