#!usr/bin/env python 
import pysam,pybedtools
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def seq2targ(reffile,gaptab):
	seq=[]
	ref=pysam.Fastafile(reffile.name)
	tar_name=[]
	for j in xrange(gaptab.count()):
		while gaptab[j][0]  not in tar_name:
			tar_name.append(gaptab[j][0])
	print tar_name
	for i in xrange(0 , ref.nreferences):
		
		rname=ref.references[i]; rlen=ref.lengths[i]; segst=0;
		print rname
		rseq=Seq(ref.fetch(rname,0,rlen),generic_dna)
		if rname not in tar_name:
			seg=[rseq]
		else:
			for k in xrange(gaptab.count()):
				print gaptab[k],gaptab[k][0]
				if gaptab[k][0] == rname:
					seg =rseq[:gaptab[k].start]+rseq[gaptab[k].end:]
		seq.append( SeqRecord( Seq(''.join([str(s) for s in seg]), generic_dna), id=rname, name=rname, description='tar'+"."+rname ) )
	SeqIO.write(seq,".fnv",'fasta') 
	return { 'filename':".fnv", 'seq':seq }


reffile=file('/home/chao/virtual/sve_vpy/charade-svengine-72146d6c152c/test/example.fas')
gap=open('/home/chao/Documents/github/Hello-world/bedtool')
gaptab=pybedtools.BedTool(gap.read(),from_string=True)
SEQ=seq2targ(reffile,gaptab)
print SEQ['seq']

