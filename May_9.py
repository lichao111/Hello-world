#user/bin/env python
#import mutforge as mf
import collections
freq1 = [ float(f) for f in [4,5,7]]
print freq1
for f in freq1:
		assert f>=4 and f<=7, "mixfreq must be a float between 0 and 1"
print "OOOOOOOOOOOOOOOOOO"
args="4,5,6,7,8,"
b=args.split(",")
print args,type(args),type(b),type({4,5}),type([4,5])
print '++++++++++++++++++'
try:
	8==9
except no:
	raise Exception("No")
print "-__________________test______________"
#varlist = collections.OrderedDict()
#dic={'nligation':nligation,'varlist':varlist,'oprefix':oprefix,'reffile':reffile,'nploid':nploid,'plansize':plansize,'varcnt':0,'edgein':edgein,'gaptab':gaptab,'varfile':varfile,'parfile':parfile,'parlist':parlist,'nprocs':nprocs,'burnin':burnin,'mergemax':mergemax}
#varlist=mf.file2var(mf.Bunch(dic))
varlist=collections.OrderedDict()
	#for row in ifile: 
varlist["1"]="123456"
varlist['2']="123456"
for var in varlist.keys():
	print varlist[var][2] #= 3#float(varlist[var][2])#VARFRAQ
	print varlist[var][3] #= 4#int(varlist[var][3])#VARHAP
h=str('iamakdsjfkdjafj')
j='kjasdfkljsjadfj'
print type(h),type(j),h[0],j[0]
print 0000000000000000
print type (varlist),len(varlist)	

