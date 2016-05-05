#! user/bin/env python
import json,tempfile
dict_1={1:2,3:4}
print type(dict_1), dict_1[1]
dict_2=json.dumps(dict_1)
print type (dict_2),dict_2,dict_2[0],dict_2[1],dict_2[2]
dict_3=json.loads(dict_2)
print type (dict_3),dict_3,dict_3['1'],dict_3['3']
print"-------------------"

def fun(a,b):
	return a+b
print fun(3,5)
print'+++++++++++++++++++'
a=str(345)
b=345
c=34.5
print type(a),a,type(b),b,type(c),c
print'____________________'
sizefile = tempfile.NamedTemporaryFile('w',delete=False,prefix="fasize_")
print sizefile.name
print '______________'
a=[1,2,34,4]
#print a.sort(down),a,type(a.sort())
print ")))))))))))))))))"
class Bunch(object):
	def __init__(self, adict):    
		self.__dict__.update(adict)
a={'Lichao':'23'}
b={'tengteng':'23'}
Bunch(a)
#print Bunch(a,b)
#print Bunch(a,b)


class bunch:
	a={}
	def __init__(self, adict,bdict):   
		self.a=adict.update(bdict)
		#.update(bdict)
	def speak(self):
		print a
bunch(a,b).speak()
	
