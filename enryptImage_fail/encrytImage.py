#打开图片修改位加密
import struct
ima = open("../img/kenann.gif",mode='rb')
s = ima.read()
ima.close()
nima = open("hh.gif", mode='wb')
index = ''
for i in s:
    index =str(i)
    fmt = str(len(index)) +'c'
    nima.write(struct.pack(fmt,index))



nima.close()
print(s[0])
