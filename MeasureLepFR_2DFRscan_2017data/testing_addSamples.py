
print 'hello world'

increment = 0.01;
initial = 0.0;
end = 0.5;
loop = (int) ( ( end - initial ) / increment ) + 1;
muFR=0.;
elFR=0.;
print 'scanning ddbkg using each muFR and elFR from ',  initial , ' to ' , end , ' with increment of ', increment ,'(' ,loop ,' loops) .'

sample={}
bkg=[]
ddbkgList_scan = []

dilep = ['EE','MM','ME']
dict_dilep = {dilep[0]:'DoubleEG',dilep[1]:'DoubleMuon',dilep[2]:'MuonEG'}
run = ['B','C','D']

index = 0
FRscanIndex = 0
for muFRindex in xrange(loop):
	for elFRindex in xrange(loop):
		ddbkgList_temp = []
		for i in xrange(len(run)):
			for j in xrange(len(dilep)):
				sample['DataDrivenBkg'+dilep[j]+'PR'+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex)]=dict_dilep[dilep[j]]+'_PR'+run[i]
				print 'muFR = ',initial+increment*muFRindex,' elFR = ',initial+increment*elFRindex,' --> DataDrivenBkg'+dilep[j]+'PR'+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex) , ':', dict_dilep[dilep[j]]+'_PR'+run[i]
				bkg.append('DataDrivenBkg'+dilep[j]+'PR'+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex))
				print bkg[index]
				ddbkgList_temp.append('DataDrivenBkg'+dilep[j]+'PR'+run[i]+'muFR'+str(muFRindex)+'elFR'+str(elFRindex))
				index+=1
		ddbkgList_scan.append(ddbkgList_temp)
		#ddbkgList_scan.append(['DataDrivenBkgEEPRBmuFR'+str(muFRindex),'DataDrivenBkgEEPRCmuFR'+str(muFRindex),'DataDrivenBkgEEPRDmuFR'+str(muFRindex),'DataDrivenBkgMMPRBmuFR'+str(muFRindex),'DataDrivenBkgMMPRCmuFR'+str(muFRindex),'DataDrivenBkgMMPRDmuFR'+str(muFRindex),'DataDrivenBkgMEPRBmuFR'+str(muFRindex),'DataDrivenBkgMEPRCmuFR'+str(muFRindex),'DataDrivenBkgMEPRDmuFR'+str(muFRindex)])
		print 'ddbkgList_scan[',FRscanIndex,'] = ',ddbkgList_scan[FRscanIndex]
		FRscanIndex+=1

# print ''
# print 'Check:'
# print ''
# 	
# for key in sorted(sample.keys()):
# 	print key,':',sample[key]
# 
# print ''
# print bkg


