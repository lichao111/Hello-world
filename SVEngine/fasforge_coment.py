#!/usr/bin/env python
#import svengine.mf.mutforge as mf

import copy, time, re, os, shutil, sys, random, csv, subprocess, traceback, argparse, tempfile, itertools, operator, collections, ConfigParser, json, imp, StringIO, string
from multiprocessing import Pool
import pysam
import pybedtools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
import pybedtools.featurefuncs
import shelve
#properly import muforge
try:
	import mf.mutforge as mf #in debugging
except ImportError:
	import mutforge as mf #in production
starttime=time.time()

#def lumpy2var(bp,ref,nligation):
#	idx=1; delidx=1; insidx=1; traidx=1; invidx=1; dupidx=1; varlist=collections.OrderedDict()
#	for line in bp:
#		if line[10] == "TYPE:DELETION":
#			mid="DEL_"+str(delidx); var="VAR_"+str(idx); idx+=1; delidx+=1
#			varlist[var]=[None] * 10
#			varlist[var][0] = var	#VID
#			varlist[var][1] = mid	#MID
#			varlist[var][2] = 1.0 #VAR FREQ
#			varlist[var][3] = 0		#VAR HAP
#			varlist[var][4] = line[0]		#VAR CHR
#			varlist[var][5] = int(line[1])-nligation #VAR POS
#			varlist[var][6] = True	#VAR DEL
#			varlist[var][7] = int(line[4])-int(line[1])+1 #VAR DEL SIZE
#			varlist[var][8] = False	#VAR INS
#			varlist[var][9] = None	#VAR INS SIZE
#		if line[10] == "TYPE:INVERSION":
#			mid="INV_"+str(invidx); var="VAR_"+str(idx); idx+=1; invidx+=1
#			varlist[var]=[None] * 10
#			varlist[var][0] = var	#VID
#			varlist[var][1] = mid	#MID
#			varlist[var][2] = 1.0 #VAR FREQ
#			varlist[var][3] = 0		#VAR HAP
#			varlist[var][4] = line[0]		#VAR CHR
#			varlist[var][5] = int(line[1])-nligation	#VAR POS
#			varlist[var][6] = True	#VAR DEL
#			varlist[var][7] = int(line[4])-int(line[1])+1 #VAR DEL SIZE
#			varlist[var][8] = True	#VAR INS
#			varlist[var][9] = (ref.name,	line[0], int(line[1]), int(line[4])-int(line[1])+1, 1, True)	#VAR INS SIZE
#		if line[10] == "TYPE:DUPLICATION": #something weird with lumpy's output here, start is bigger than end
#			mid="DUP_"+str(dupidx); var="VAR_"+str(idx); idx+=1; dupidx+=1
#			varlist[var]=[None] * 10
#			varlist[var][0] = var	#VID
#			varlist[var][1] = mid	#MID
#			varlist[var][2] = 1.0 #VAR FREQ
#			varlist[var][3] = 0		#VAR HAP
#			varlist[var][4] = line[0]		#VAR CHR
#			varlist[var][5] = int(line[4])-nligation	#VAR POS
#			varlist[var][6] = True	#VAR DEL
#			varlist[var][7] = int(line[1])-int(line[4])+1 #VAR DEL SIZE
#			varlist[var][8] = True	#VAR INS
#			varlist[var][9] = (ref.name,	line[0], int(line[4]), int(line[1])-int(line[4])+1, 2, False)	#VAR INS SIZE
#		if line[10] == "TYPE:TRANSLOCATION":
#			line2 = bp.next() #this can be ingnored
#			if int(line[2])-int(line[1])==1:#where insertion happens
#				delst=int(line[4]); deled=int(line[5]); delchr=line[3]; insst=int(line[1]); insted=int(line[2]); inschr=line[0]
#			else:
#				delst=int(line[1]); deled=int(line[2]); delchr=line[0]; insst=int(line[4]); insted=int(line[5]); inschr=line[3]
#			#do insertion
#			mid="TRA_"+str(traidx); var="VAR_"+str(idx); idx+=1; 
#			varlist[var]=[None] * 10
#			varlist[var][0] = var	#VID
#			varlist[var][1] = mid	#MID
#			varlist[var][2] = 1.0 #VAR FREQ
#			varlist[var][3] = 0		#VAR HAP
#			varlist[var][4] = inschr		#VAR CHR
#			varlist[var][5] = insst-nligation	#VAR POS
#			varlist[var][6] = False	#VAR DEL
#			varlist[var][7] = 0 #VAR DEL SIZE
#			varlist[var][8] = True	#VAR INS
#			varlist[var][9] = (ref.name,	delchr, delst, deled-delst+1, 1, False)	#VAR INS SIZE
#			mid="TRA_"+str(traidx); var="VAR_"+str(idx); idx+=1; traidx+=1
#			#do deletion
#			varlist[var]=[None] * 10
#			varlist[var][0] = var	#VID
#			varlist[var][1] = mid	#MID
#			varlist[var][2] = 1.0 #VAR FREQ
#			varlist[var][3] = 0		#VAR HAP
#			varlist[var][4] = delchr		#VAR CHR
#			varlist[var][5] = delst-nligation	#VAR POS
#			varlist[var][6] = True	#VAR DEL
#			varlist[var][7] = deled-delst+1 #VAR DEL SIZE
#			varlist[var][8] = False	#VAR INS
#			varlist[var][9] = None	#VAR INS SIZE
#	return varlist

def var2seq(brpt,reffile,nligation,oprefix): #assume varbed is checked for nonoverlapping    Chao:what is brpt？ (breakpoint?) what is nligation(把整个序列分成nligetion段？)Ans:nligation是一个缓冲区，把plansize的两端都加上一个长为nligation的区间，作为缓冲！
	#print brpt,reffile,nligation,oprefix
	ref=pysam.Fastafile(reffile.name); seq=[]#reffile是什么，他为什么可以访问name？？  Chao:name可以输出路径和文件名            这里还实例化了一个类ref;定义了空数组seq,用来装什么呢。
	for i in xrange(0,ref.nreferences): #iterate through （i在0到参考序列条数之间变动）                nreferences：ref中序列的条数
		rname=ref.references[i]; rlen=ref.lengths[i]; segst=0;#reference是一个tuple，由所有的名字组成。lengths是这个tuple的长度。
		rseq=Seq(ref.fetch(rname,0,rlen), generic_dna)   #rseq即使这条序列  AGCT~   pysam.fastfile.fetch()作用是取某一段特定的序列！
		if brpt.get(rname,None) == None: #no var at all  Chao:在这条ref中没有variant；  在brpt这个字典key中查找rname，找不到返回None！
			seg = [ rseq ]       #如果没有var，就直接整条ref的序列放到了seg中
		else: #1+ vars
			brs = collections.OrderedDict(sorted(brpt[rname].items(), key=lambda t: t[0]))#ordered是加了顺序的dict，dict没有顺序sort方法还有两个可选参数：key和reverse.
                                                            #按t[0]进行排序，可是t[0]是什么东西呢？按key值进行排序
			seg = []; nbrs=len(brs) #member of seg are Seqs
			#if i==1: print nbrs
			for j in xrange(0,nbrs):
				#VID MID VARFRQ VARHAP VARCHR VARPOS VARDEL VARDELSZ VARINS VARINSSZ
                                # 0   1    2      3      4       5     6        7        8     9
				try:
					var=brs.values()[j]
					if j == (nbrs-1): #last var, seged is          Chao:seged? seged END?  下标与长度之间差
						seged=rlen                #Chao:如果它是最后一个var，那么seged的值就是整条序列的长度
					else:
						seged=brs.values()[j+1][5]   #Chao:如果不是最后一个var，那么seged的值就是下一个var的开始位置
					if j == 0: #the first seg is appended without var
						seg.append(rseq[segst:var[5]]); segst=var[5] #append函数是向list中添加内容的
					seq1 = rseq[segst:seged] #seg if connected is the new seq 
					if var[6]: #work on deletion
						seq1 = seq1[:nligation]+seq1[nligation+var[7]:]#两个数组直接相加，相当于删掉了var[7]长度的序列。
						segst = seged
					if var[8]: #work on insertion
						#['example.fasta', '22', 25202000, 1000, 2, False]
						info = var[9]
						seqi = Seq(pysam.Fastafile(info[0]).fetch(info[1],info[2],info[2]+info[3]), generic_dna) #st=0-based, ed=0-based+1
						if info[5]:
							seqi = seqi.reverse_complement();
						seqi = Seq(str(seqi)*info[4], generic_dna)
						seq1 = seq1[:nligation]+seqi+seq1[nligation:]#这样就插入了seqi这样一个序列
						segst = seged
					seg.append(seq1)
				except TypeError:
					print var
					print >>sys.stderr,"most likely formatting wrong in provided .var file, ignore entry!"
		#print "old:",len(rseq)
		#print "new:",len(SeqRecord( Seq(''.join([str(s) for s in seg]), generic_dna), id=rname, name=rname, description=oprefix+"."+rname ) )
		seq.append( SeqRecord( Seq(''.join([str(s) for s in seg]), generic_dna), id=rname, name=rname, description=oprefix+"."+rname ) )
	SeqIO.write(seq,oprefix+".fnv",'fasta')            #查一下SeqIo的write函数
	return { 'filename':oprefix+".fnv", 'seq':seq }

def main(args):
	burnin = args.burnin
	edgein = args.edgein
	outbam = args.outbam
	nprocs = args.nprocs
	varfile = args.varfile
	metafile = args.metafile
	reffile = args.reffile
	gapfile = args.gapfile
	parfile = args.parfile
	parlist = ConfigParser.ConfigParser()#操作配置文件
	parlist.readfp(parfile)#读取配置选项
	plansize = args.plansize
	mergemax = args.mergemax
	layout = args.layout
	tempfile.tempdir = args.tmpdir
	try:
		os.mkdir(tempfile.tempdir)#os.mkdir用于创建目录，一级目录
	except:
		print >>sys.stderr, tempfile.tempdir, "error!, either it exists or cann't be created! please change path"#Chao:创建不成功时输出
		quit()#退出
	print >>sys.stderr, "tmpdir=", tempfile.tempdir
	pybedtools.set_tempdir(tempfile.tempdir)#Chao:查一下pybedtools的set_tempdir函数

	runmode=0 #1 meta, 2 var, 3 var+meta
	if varfile!=None and metafile!=None:#   Chao：既有var file又有meta file！
		runmode=3;
		oname=varfile.name.rsplit(".")[0]	#以'.'划分取第0个; oname是var文件的名字。除去.var的后缀
		#don't allow mode 3
		print >>sys.stderr, "either a .meta or a .var file can be specified but not both"
		quit()#既有meta文件也有var文件报错，退出.why，为什么不让varfile和metafile同时出现呢？？？
	elif varfile!=None and metafile==None:  #有var文件而没有meta文件
		runmode=2;
		oname=varfile.name.rsplit(".")[0]	
	elif metafile!=None and varfile==None:     #有meta文件而没有var文件
		runmode=1;
		oname=metafile.name.rsplit(".")[0]	#oname是metafile文件的名字。除去.meta的后缀
	else:
		raise Exception("must provide meta and/or var files!")
	oprefix = oname if not args.oprefix else args.oprefix#没有提供oprefix就把oname复制给oprefix,如果提供了，就用提供的
	nligation = 0; nploid = 1; #in fasforge, nligation is always 0 and nploid always is 1        ## fastforge中都处理的是单倍体
	freq1 = [ float(f) for f in args.mixfreq.split(",") ]#split之后成为一个list
	for f in freq1:
		assert f>=0 and f<=1, "mixfreq must be a float between 0 and 1" #断言，f若不再0，1之间就报错！！
	try:#try 后面的语句作用是：把gapfile中的区间在左右各自延长的edgein bp的长度。#TODO 什么用呢？？
		sizefile = mf.fas2size(reffile.name) #create genome size file
		gaptab=pybedtools.BedTool(gapfile.read(),from_string=True)#用已有的BED文件生成了一个BEDtool。
		gaptab=gaptab.slop(g=sizefile, b=edgein)# slop改变序列的interval,可以查看bedtools中的slop suboption，详见firfox书签！！！！gaptab是个bed file！！
	except pybedtools.cbedtools.BedToolsFileError:
		raise Exception("incorrect gapfile provided, must in BED format")
	#create a string meta file:
	#FINS	2500	adeno.fna,fix_...	fix_1	fix_1	fix_1	fix_1	fix_1	#FINS=COPY*INS, foreign insertion
	#DINS	2500	fix_...	fix_1	fix_1	fix_1	fix_1	fix_1	#DINS=COPY*INS, domestic insertion
	#inssize="fix_100_200_300_400_500_600_700_800_900_1000_1000_2000_3000_4000_5000_6000_7000_8000_9000_10000"
	#metastr='\n'.join([ "\t".join(['FINS',str(2),'adeno.fna,'+inssize,'fix_1','fix_1','fix_1','fix_1','fix_1' ]),
	#					"\t".join(['DINS',str(2),'fix_100_200','fix_1','fix_1','fix_1','fix_1','fix_1' ]) ])
	varlist = collections.OrderedDict()
	dic={'nligation':nligation,'varlist':varlist,'oprefix':oprefix,'reffile':reffile,'nploid':nploid,'plansize':plansize,'varcnt':0,\'edgein':edgein,gaptab':gaptab,'varfile':varfile,'parfile':parfile,'parlist':parlist,'nprocs':nprocs,'burnin':burnin,'mergemax':mergemax}
	print >>sys.stderr, "runmode=", runmode
	dic['hapseq']=[pysam.Fastafile(reffile.name)];#这样字典dic中有多了一组值！在这里，hapseq就是reference

	if runmode > 1: #have var input
		varintype = varfile.name.split(".")[-1]     
		if varintype == 'lumpy':                 #varfilr问什么会有lumpy的拓展名？？？？如果是lumpy的扩展名，转化成Var
			bp=mf.CommentedFile(varfile) #blue print
			#bp=csv.reader(varfile,delimiter="\t")
			#somehow we need to set ligation setting 
			#assume that every true var pos out of program is true position
			#every true var pos inside the program is position+nligation
			varlist=mf.lumpy2var(bp,reffile,nligation)    #mf中的lumpy2var()函数
		elif varintype == 'var':
			varlist=mf.file2var(mf.Bunch(dic))            #mf中的file2var()函数
		else:
			raise Exception("varintype %s hasn't been implemented" % varintype)
		dic['varcnt']=len(varlist) #this is needed for continuously counting
		dic['varlist']=varlist #this is needed for continuously counting
		#d.iloc[0:1,0:1]; deoverlapping
		vartab=mf.var2bed(mf.Bunch(dic))#Chao: trans varfile to bed file
		#print "br1"
		if(len(varlist)>1): #only needed if input is more than 2#chao:这个if的作用是检查区间是否重复，没有办法直接检查varfile，只能是转化成bedfile，在利用bedtools检查。
				varlist=mf.deovlpvar(dic) 
				dic['varcnt']=len(varlist) 
				dic['varlist']=varlist 
				vartab=mf.var2bed(mf.Bunch(dic))
				assert mf.chkvar(vartab) == True, "==Warn: varfile still contains self overlaps, which is not allowed, bail out"
		#print "br2"
		gaptab=vartab.cat(gaptab.each(pybedtools.featurefuncs.extend_fields,n=vartab.field_count()).saveas())#此函数的作用是把gapfile 和vartab这两个bed文件结合成一个，由于列多少可能不同。所以要用点把gaptab的列补全成和vartab的列一样多。
#pybedtools.BEDtools.cat 的作用是把两个bed file 结合起来，默认把feature也结合起来。
#pybedtools.BEDtools.each的作用是用user自己定义的函数于每一个feature（bed中的每一条）。输入输出都要是interval
#extend_fields的作用  Pads the fields of the feature with "." to a total length of n fields, CHAO: 扩展bedfile的列，用.来补
#field_count的作用 Return the number of fields in the features this file contains. Checks the first n features.  TMD,就是统计bedfile有几列
#saveas :Make a copy of the BedTool
		dic['gaptab']=gaptab #considerring var tab as pre-existing mask that works for meta-variant 

		#print "br3"

	if runmode%2 == 1: #have meta input, merge var with meta
		metatab = mf.CommentedFile(metafile)
		#for row in metatab: #force input of fix_1 columns 5-8 
		#	row[4:8]=['fix_1']*4
		varlist,varcnt = mf.makevar(mf.Bunch(dic),metatab,fas=True)#把meta转化成var
		dic['varlist'] = varlist
		dic['varcnt'] = varcnt
		vartab=mf.var2bed(mf.Bunch(dic))
		if(len(varlist)>1): #only needed if input is more than 2
				varlist=mf.deovlpvar(dic) 
				dic['varcnt']=len(varlist) 
				dic['varlist']=varlist 
				vartab=mf.var2bed(mf.Bunch(dic))
				assert mf.chkvar(vartab) == True, "==Warn: varfile still contains self overlaps, which is not allowed, bail out"                             #chkvar函数中用到了py的count函数和sort函数！检验有没有重叠的办法主要就是把区间合并之后看数目和合并之前是否一样！

	mf.var2file(mf.Bunch(dic))
	#read in bedpe to generate varlist
	#now we need to check whether the	sv has been correctly inserted
	#we also need to check whether the position is properly selected 
	brpt=collections.OrderedDict()
	#print "br4"
	for key in varlist.keys():#把所有的var用brpt表示，brpt［chr］［pos］
		var = varlist[key]
		if brpt.get(var[4],None) == None:
			brpt[var[4]] = collections.OrderedDict({var[5]:var})
		else:
			brpt[var[4]][var[5]]=var	#brpt[chr][pos]
	#print "br5"
	ref = pysam.Fastafile(reffile.name)
	seq0 = { 'filename':reffile.name, 'seq':[ SeqRecord(Seq(ref.fetch(ref.references[i],0,ref.lengths[i]) ),id=ref.references[i],name=ref.references[i],description=ref.references[i]) for i in xrange(0,ref.nreferences) ] } #input sequence
#SeqRecord:该类是 Bio.SeqIO 序列输入/输出交互界面的基本数据类型。可以把identifiers 和features等高级属性与序列关联起来。详见firefox书签“biopython”
	#print "br6"
	seq1 = var2seq(brpt,reffile,nligation,oprefix)
	print >>sys.stderr, "done var2seq", time.time()-starttime, " seconds" 

	nlibrary=parlist.getint('xwgsim', 'nlibrary')#从xwgism中读取nlibrary作为int型
#Chao:关于configparse的注释
#ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。
	libnames=json.loads(parlist.get('xwgsim', 'libnames'))
#Chao:
#json.loads
#
	#bams = [None] * nlibrary

	if layout:
		print >>sys.stderr, "done layout and fas file generation"
		quit()
	
	pariter=[]
	for lib in range(0,nlibrary):
		for fi in range(0,len(freq1)):
			pariter.append([parlist,nligation,reffile.name,nploid,seq0,lib,freq1[fi],seq0,seq1,lib,oprefix,mergemax])
                                      #0	 1	      2		3	4   5	 6	  7	8   9	10	  11

	#NOTE: debug code
	ffq=[]
	if nprocs<2:
		for parit in pariter:
			ffq.append(makefq(parit))
	else:
		pool = Pool(processes=int(nprocs))#pool处理多个进程  进程池
		ffq=pool.map(makefq,pariter,1)#调用了xwgsim。生成了read数据／多线程下
	print >>sys.stderr, "done var2fq", time.time()-starttime, " seconds"

	if outbam:
		libbams = mf.fq2bam(ffq,mf.Bunch(dic))
		
		print >>sys.stderr, "done fq2bam", time.time()-starttime, " seconds"

		fbam = [None] * nlibrary
		for lib in range(0,nlibrary): #there will be only one bam in libbams[lib]
			sbam = '.'.join([oprefix,libnames[lib]]) # oprefix.lib.st
			tbam = tempfile.NamedTemporaryFile('w',delete=False).name
			mbam = mf.mergebam([libbams[lib]],tbam,mergemax)
			sort_cmd = "samtools sort -@ %s %s %s" % (nprocs, mbam, sbam)
			#print sort_cmd #
			mf.syscmd(sort_cmd)
			fbam[lib] = sbam+".bam" #post processing: librarywise merging bams;

		print >>sys.stderr, "done merge to final bam:", str(fbam), time.time()-starttime, " seconds"

	shutil.rmtree(tempfile.tempdir) #clean temp files
	print >>sys.stderr, "done fasforge"
	
	return None

#OBSOLETE
def makebam(parit):#Chao：这个函数好像没有用，在fasforge和muteforge中		
	print "processing lib %s freq %s regions" % (str(parit[5]),str(parit[6]))
	parlist=parit[0]; nligation=parit[1]; rname=parit[2]; nploid=parit[3]; seq0=parit[4]; lib=parit[5]; freq1=parit[6]; freq0=1-freq1; seq0=parit[7]; seq1=parit[8]; lib=parit[9]; oprefix=parit[10]
	libnames=json.loads(parlist.get('xwgsim', 'libnames'))
	bam0 = mf.runwgs(parlist,nligation,rname,nploid,seq0,lib,freq0)          #mf中的runwgs()函数
	bam1 = mf.runwgs(parlist,nligation,rname,nploid,seq1,lib,freq1)
	#print [bam0,bam1]
	bam = mf.mergebam([bam0,bam1],oprefix+"."+libnames[lib])                #mf中的mergebam()函数！
	print "done lib %s freq %s regions" % (str(parit[5]),str(parit[6]))
	return bam

def makefq(parit):		
	print "processing lib %s freq %s regions" % (str(parit[5]),str(parit[6]))
	parlist=parit[0]; nligation=parit[1]; rname=parit[2]; nploid=parit[3]; lib=parit[5]; freq1=parit[6]; freq0=1-freq1; seq0=parit[7]; seq1=parit[8]; lib=parit[9]; oprefix=parit[10]; mergemax=parit[11] #seq0=parit[4]; 
	libnames = json.loads(parlist.get('xwgsim', 'libnames'))
	wgs0 = mf.fqwgs(parlist,nligation,rname,nploid,seq0,lib,freq0,mergemax) #调用了mf中的fqwgs函数
	wgs1 = mf.fqwgs(parlist,nligation,rname,nploid,seq1,lib,freq1,mergemax)
	#bam0 = mf.runwgs(parlist,nligation,rname,nploid,seq0,lib,freq0)
	#bam1 = mf.runwgs(parlist,nligation,rname,nploid,seq1,lib,freq1)
	#print [bam0,bam1]
	ffq = mf.mergefq([wgs0,wgs1],oprefix+"."+libnames[lib],mergemax)        #mf中的mergefq函数
	print "done lib %s freq %s" % (str(parit[5]+1),str(parit[6])), time.time()-starttime, " seconds"
	return ffq

def run():
	parser = argparse.ArgumentParser(description="spike-in mutations to fasta files,\
 we insert mutations into a provided reference \
																								this script is haplotype insensitive and ligation less")     #在fasta文件中加入免疫，fasforge对于haplotype和ligation是不起作用的。
	parser.add_argument('gapfile', metavar='gapfile', type=argparse.FileType('rU'), #example.bed
												help="inputfile of gap or other banned regions, required")
	parser.add_argument('parfile', metavar='parfile', type=argparse.FileType('rU'), #example.par
												help="inputfile of library-wise parameters, required"),
	parser.add_argument('reffile', metavar='reffile', type=argparse.FileType('rU'), #example.fasta
												help="inputfile of ref file(s), required"),
	parser.add_argument('-m', '--metafile', dest='metafile', type=argparse.FileType('rU'), #example.meta
												help="inputfile of meta specification")	# variants to be randomly added
	parser.add_argument('-v', '--varfile', dest='varfile', type=argparse.FileType('rU'),	#example.var/op
												help="inputfile of variant specification") # prespecified variants, bedpe format or others
	parser.add_argument('-o', '--oprefix', dest='oprefix', default=None, #output1,output2,output3,...
												help="prefix for output files")
	parser.add_argument('-f', '--plansize', dest='plansize', type=int, default=100000,
												help="palnsize is the grain size for genome planning, exluding ligation buffer (default= %(default)s bp)")
	parser.add_argument('-b', '--burnin', dest='burnin', type=int, default=1000000,
												help="burnin is the chromosome tip skip size for genome planning to avoid tip padding Ns, default: %(default)s bp")
	parser.add_argument('-e', '--edgein', dest='edgein', type=int, default=100000,
												help="edgein is the gap neibourgh region skip size for genome planning, default: %(default)s bp")
	parser.add_argument('-q', '--mixfreq', dest='mixfreq', default="1",
												help="generated spikein-in mixing frequency, homozygous=1")
	parser.add_argument('-n', '--nprocs', dest='nprocs', type=int, default=1,
												help="split into multiple processes (default= %(default)s )")
	parser.add_argument('-r', '--mergemax', dest='mergemax', default=2000, type=int,
												help="max number of files in one iteration of merging (default: %(default)s )") 
	parser.add_argument('-d', '--tmpdir', dest='tmpdir', default=os.path.join(os.environ['HOME'],'svetmp_'+''.join([random.choice(string.ascii_letters) for i in range(4)])),
												help="root dir for keeping temporary files, default (last 4 digits random): %(default)s")
	parser.add_argument('--layout', dest='layout', action='store_true', default=False,
												help="only dry layout")
	parser.add_argument('--outbam', action='store_true', dest='outbam', default=False, 
												help="wet run to bam")
	args = parser.parse_args()
	main(args)    #chao:运行mian()函数!!!!!!!!!

if __name__ == '__main__':
	run()
	print "total runtime: ", time.time()-starttime, " seconds"
	
