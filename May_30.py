#!user/bin/env python
import csv
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

size=file('/home/lichao/Documents/github/svengine/test/example.var')
size=CommentedFile(size)
print size
print size.f
for i in size:
	print i
	
print size.next

