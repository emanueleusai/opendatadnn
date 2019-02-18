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
'/store/group/lpcml/eusai/CRAB_UserFiles/step2_QCD600to3000_01/190213_183439/',
'/store/group/lpcml/eusai/CRAB_UserFiles/step2_QCD600to3000_02/190213_201625/'


 ]

sub=['0000/','0001/','0002/','0003/','0004/']#,'0005/']

#folder='/store/group/lpcml/eusai/step2_ttbar_p8_03/'
outname='step2_QCDPt_15to3000'

xrootd='root://cmsxrootd-site.fnal.gov/'
outfile=open(outname,'w')

for i in folders:
	for j in sub:
		folder=i+j
		eosls=subprocess.check_output(['eos','root://cmseos.fnal.gov','ls',folder])
		names=eosls.splitlines()
		if 'log' in names:
			names.remove('log')
		if 'failed' in names:
			names.remove('failed')
		for k in names:
			outfile.write(xrootd+folder+k+'\n')

outfile.close()
