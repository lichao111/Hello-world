#!user/bin/env python
import tempfile,os,string
treefile=file('/home/lichao/Documents/github/svengine/exam_tree')
#tree1=open('/home/lichao/Documents/github/svengine/tree1','w+b')
#for G,line in enumerate(o):
#	print G,line
#home=tempfile.TempFile()
#print 
generation=3
class Node:
	def __init__(self,i,j,v,a):#i:int,j:int,v:dict,a:range[0,1]
		self.i=i
		self.j=j
		self.v=v
		self.a=a

tree1=open('/home/lichao/Documents/github/svengine/tree1','a+')
#tree1=tempfile.TemporaryFile()
#tree1=open('tree1','w+')
for line in treefile:
	if "/" not in line:
		tree1.write(line)
		
#for line in tree1:
#	print line

tree2=open('/home/lichao/Documents/github/svengine/tree2','w+')
for g,line in enumerate(tree1):
	#print g,line
	if g<=generation :
		tree2.write(line)
tree2=open('/home/lichao/Documents/github/svengine/tree2')


#A00=Node(0,0,{'var1':1},0.5)
#print A00,A00.i,A00.j,A00.v,A00.a,type(A00.v)	
for g,line in enumerate(tree2):
	line=line.expandtabs().strip().split(' ')
	#string.translate(line, del=" ")
	#line=line.strip().split(' ')
	#line=line.split(' ')
	l=len(line)
	#for j in range[l]:
	#	if line[j].startwith('\t')
	print line,l
#for g,line in enumerate(tree2):
#	print g,line
#for line in tree1:
#	print line	
	
#tree1.close()
