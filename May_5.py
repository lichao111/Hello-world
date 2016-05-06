#!user/bin/env python
import collections
def red(fi):
	out=fi.name
	print out
for i in xrange(0,10):
	print i
for i in range (0,10):
	print i
print "*******"
type (xrange(10))
type (range(10))
c={"Lic":"23","Teng":"23"}
print c.get("Lic"),c.get('Teng'),c.get('yu'),c.get('yu',"si")
print'pppppppppppppppppp'


dict = { 1 : 2, 'a' : 'b', 'hello' : 'world' }  
print dict.values(),dict.keys()  ,dict.items()
D=sorted(dict.items(),key=lambda t:t[0])  
print D, len(D),D[2],D[1]
f=collections.OrderedDict()
f[1]=collections.OrderedDict({'1':'2'})
#f[2]=collections.OrderDict()
print(type (f)),f
print '+++++++++++'
r=['True','False','True','False']
print r[0]
#print r[4]
for i in range(4):
	r[i]=r[i] in ['Triue']
	print r[i]
for j in range(5):
	print j

