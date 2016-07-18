#!usr/bin/env python

import random,copy

#tree=[1,[2,[4,[8,[],[]],[9,[],[]]],[5,[10,[],[]],[11,[],[]]]],[3,[6,[12,[],[]],[13,[],[]]],[7,[14,[],[]],[15,[],[]]]]]
#tree=[0,[1,[11,[],[]],[12,[],[]]],[2,[],[]]]
tree=['N',['N',['N',['N',[],[]],['Var4',[],[]]],['Var3',['Var3',[],[]],['Var5',[],[]]]],['Var1',['Var1',[],[]],['Var2',[],[]]]]
l=0;m=1;n=2;s=0;#fre[0]=random.uniform(0,1)

def find_event(t,event=[]):
	if t:
		if t[0] not in event:
			event.append(t[0])
		find_event(t[1],event)
		find_event(t[2],event)
#	else:
	return event	

#print tree
#print find_event(tree)
m=1;n=1
#def get_fre(t,s=0):
#	global m,n
#	if t[1] or t[2] :
#		if s==0:
#			fre[0]=random.uniform(0,1)
#			fre[1]=random.uniform(0,1)
#			fre[2]=random.uniform(0,1)
#		if s==1:
#			fre[m]=random.uniform(0,1)
#			fre[m*10+1]=random.uniform(0,1)
#			fre[m*10+2]=random.uniform(0,1)
#			m=m*10+1
#		if s==2:
#			fre[n]=random.uniform(0,1)
#			fre[n*10+1]=random.uniform(0,1)
#			fre[n*10+2]=random.uniform(0,1)		
#			n=n*10+1
#		
#		get_fre(t[1],1)
#		get_fre(t[2],2)
#	return fre
#print get_fre(tree)


def is_emp(tree,t):
	
	w=len(str(t))
	for i in range(w):
		a=int(str(t)[::-1][w-1])
#		print a
		tree = tree[a]
#		print tree
		w = w-1
	return tree[1] == []
#print is_emp(tree,2)
tail=[]

def g(a):
	b=copy.deepcopy(a)
	for i in range(len(a)):
		b.extend([b[i]*10+1,b[i]*10+2])
	b=list(set(b))
#	print b
#	print a
	for i in a:
		b.remove(i)
	return b
#print g([1,2])
def tai_tre(tree):
	num_index=0;
	t=[1,2]
	b=[]
	tail=[]
	T=[1,2]
	while 1:
		
		for i in t:
			
			try:
				if is_emp(tree,i):
					tail.append(i)
				#tail=list(set(tail))
#				print 'tail=',tail
			except IndexError:
#				print t,'i',i
				T.remove(i)
#				print "T=",T
				#num_index += 1
		#	num_index += 1
		#if num_index == len(t):
		#if num_index == len(t):
#		print "t=",t
		if T==[] :
			return tail#break
 		t=g(T)
 		T=copy.copy(t)
			#except:
			#	return 0
	#return tail	
#print 'zuizhong',tai_tre(tree)
#print tree
#print is_emp(tree,1),is_emp(tree,2),is_emp(tree,11),is_emp(tree,12)
event = find_event(tree)
tail = tai_tre(tree)
print 'tail',tail
print 'event',event 

def mate(tree,event,tail):
	mat={}
	for i in event:
#		print i,type(i) 	
		for j in tail:
#			print '--------',j,'---------'
			tree1=copy.deepcopy(tree)
			w=len(str(j))
			for k in range(w):
		
				a=int(str(j)[::-1][w-1])
#				print a
				tree1 = tree1[a]
#				print tree
				w = w-1
#			return tree[0] == i
#			print tree1,type(tree1[0]),tree1[0],i
			if tree1[0] == i:
#				print 'YES'
				mat[j]=i
	return mat
#print mate(tree,event,tail)
mat = mate(tree,event,tail)

#def unit(a):#get the unit of a number
#	while 1:
#		a = a%10

def che_odd(a): #check a number is odd or even
	if a%2 ==0:
		return False
	else:
		return True
		
	

def get_fre(mat,tail):
	fre={}
	fre[0]=random.uniform(0,1)
	for i in tail:

#		print fre
		w = len(str(i))
		for  j in range(w-1):
			#print i/(10**(w-1))
			fre[i/(10**(w-1))]=random.uniform(0,1)
			w -= 1
			#fre[i] *= fre[i/(10**(w-1))]
	print fre
	for i in tail:
		fre[i]=1
		l=copy.copy(i)
		
#		if che_odd(i):
#			fre[i] = 1-fre[0]
#		else:
#			fre[i] = fre[0]
		print l
		w=len(str(i))
		for k in range(w):
			#l=l/(10**(w-1))
			if che_odd(l):
				fre[i] *= 1-fre[l/(10)]
				print 'fre[%s]' %(i),'*=','1-fre[%s]'%(l/10)
			else:
				fre[i] *= fre[l/(10)]
				print 'fre[%s]'%i,'*=','fre[%s]'%(l/10)
			l = l/10		
	
	return fre

print get_fre(mat,tail)	

		
	
	
	
	
