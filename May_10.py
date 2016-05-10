#!user/bin/env python
import operator
a=set()
a.add("lichao")
a.add("tengteng")
a.add("child")
b=[]

print a,type(a),len(a)
print type(b),len(b)
print '0000000000000000'
b=[0,1,1,3,4,5,6,7,8]
#if fas: b[1:3]==[1]*2
print 'yes'*5
D="fix_500_500_1000_2000_2000"
E=D.split('_')
print E,type(E)
def isint(a):
	if a==int (a):return True
	else: 
		return False 
values = [ int(x) if isint(x) else float(x) for x in E[1:len(E)] ]
print values
print '000000000000000'
mydict={1:2,3:4}
i= mydict.items()
print i , type(i[0])
o=operator.itemgetter(1)
print o(b)
print sorted(mydict)
print '999999999999999999999999'
def demultiplex(m):#C!
	return [i for i, x in enumerate([int(x) for x in bin(m)[2:][::-1]]) if x == 1]
print demultiplex(3)
print "'the differeft between break & continue'"
for x in range(10):
    if x==5:
        break
for x in xrange(10):
	if x == 5:
		continue
 
        print x
print 'def of demultiplex'
print demultiplex(0),demultiplex(1),demultiplex(2),demultiplex(3)








