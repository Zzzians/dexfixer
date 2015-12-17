#/bin/python3
import hashlib
import zlib
import sys
def tobyte(val,n,reverse=0):
    a=[]
    for i in range(n):
        a.append(int(val&255))
        val=val>>8
    if(reverse):a.reverse()
    return a
f=open(sys.argv[1],"rb")
data=f.read()
magic=list(data[:8])
data1=data[32:]
sha1=tobyte(int(hashlib.sha1(data1).hexdigest(),16),20,1)
data2=sha1
data2.extend(data1)
adler=tobyte(zlib.adler32(bytes(data2)),4)
adler.extend(data2)
magic.extend(adler)
f.close()
f=open(sys.argv[2],"wb")
f.write(bytes(magic))
f.close()



