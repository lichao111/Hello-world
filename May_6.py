#!user/bin/env python
import collections,csv
#def fas2size(fasfile):
#	sizefile = tempfile.NamedTemporaryFile('w',delete=False,prefix="fasize_")
#	fasseq = pysam.Fastafile(fasfile)
#	size = [ fasseq.references[i]+'\t'+str(fasseq.lengths[i]) for i in range(0,min(fasseq.nreferences,maxrefnum)) ]
#		chr				lengths of sequence 
#	sizefile.write('\n'.join(size))
#	sizefile.close()
#	return sizefile.name
#fas2size
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
print '0000000000000000'

#	ifile=CommentedFile(bun.varfile); hapseq=bun.hapseq; nligation=bun.nligation
	#NOTE: CommentedFile can only be iterated once. Need seek to reiterate
varlist=collections.OrderedDict()
example_var=open('/home/lichao/Documents/github/Hello-world/example.var')
ifile = CommentedFile(example_var)
#for row in ifile: 
	#varlist[row[0]]=row;
#	print row,'+++++++++',row[0]
#for var in varlist.keys():
#		varlist[var][2] = float(varlist[var][2])
#		varlist[var][3] = int(varlist[var][3])
#		varlist[var][5] = int(varlist[var][5])-3
#		varlist[var][7] = int(varlist[var][7])
#		varlist[var][8] = varlist[var][8] in ['True']
#		varlist[var][9] = readins(varlist[var][9])
#	
#print varlist.keys()
#g=collections.OrderedDict()
#for j in range(10,20):
#		g[j]=j+1
#print g.keys()
#for i in g.keys():
#	varlist[i][2]=4
#	varlist[i][3]=4
#print g[10]
#print '+++++++++++++++++'
#dic={'I':3,'u':4}
#print dic.values()
#print dic,dic['u']
#dic['uu']=5

#print dic 
print 000000,ifile.next()


