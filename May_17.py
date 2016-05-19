#!user/bin/env python
import csv,re,tempfile
class tree:
	def __init__(self, f, commentstring="/ "or "\ "):        
		self.f = csv.reader(f,delimiter='\t')
		self.commentstring = commentstring
	def next(self):
		line = self.f.next()
		while self.commentstring in line:
			line = self.f.next()
		return line
	def __iter__(self):
		return self
tree=file("/home/lichao/Documents/github/svengine/exam_tree")

#print tree,type(tree),tree.f,tree.commentstring
#for line in tree:
#	print line
class CommentedFile:
	def __init__(self, f, commentstring="#"):             
		self.f = csv.reader(f,delimiter='\t')
		self.commentstring = commentstring
	def next(self):
		line = self.f.next()
		while line[0].startswith(self.commentstring):
			line = self.f.next()
		return line
	def __iter__(self):
		return self
#g=CommentedFile(file('/home/lichao/Documents/github/svengine/meta'))
#for i in g.next
#print tree
temp=open('/home/lichao/Documents/github/svengine/tree1','w+b')
for line in tree:
	if "/" not in line:
		temp.write(line)

#class Node:
#	def __init__(self,i,j,v,a)
#	self.i=i
#	self.j=j
#	self.v=v
#	self.a=a
for (num,value) in enumerate(tree):
    print "line number",num,"is:",value


		
		
















