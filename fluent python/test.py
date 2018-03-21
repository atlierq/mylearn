import array
from array import array
from random import random


floats= array('d',(random() for x in range(100)))
# print(floats[-1])
# fp=open('floats.txt','wb')
# floats.tofile(fp)
# fp.close()
# floats2=array('d')
# fp=open('floats.txt','rb')
# floats2.fromfile(fp,10**7)
# fp.close()
# print(floats2[-1])
print(floats)
print(floats.tolist())
print(floats.typecode)
a=array('d',sorted(floats))
print(a)