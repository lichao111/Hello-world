#!user/bin/env python
a={}
b=['var1:1','var2:0']
map(lambda x:a.setdefault(x.split(':')[0],x.split(':')[1]),b)
print a
