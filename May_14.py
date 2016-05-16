#!user/bin/env phthon
import time
a= False 
if a == False:
	print 'ok'
else:
	raise Exception("no")
print time.time(),time.ctime()
#time.sleep(5)
print time.time(),time.ctime()
dic={} #common dictionary interface for passing parameters
for i in ('hapseq','gaptab','reffile','plansize','nligation','nploid','oprefix','nprocs','edgein','burnin','mergemax'):
	dic[i] = locals()[i]
print dic
