#IO编程 open、write函数，io模块StringIO、ByteIO
'''
f = open("e:/practice/1.txt", "r")
f.read()
f.close()

with方式会自动调用close。类似using

read的几种方法
read(size) #每次读取size字节内容
readline() #每次读取一行
readlines() #一次性读取并返回list
'''

#读文件
with open("e:/practice/1.txt", "r", encoding="gbk", errors="ignore") as f: #r表示读文本文件，rb表示读二进制文件，encoding用于指定文件编码格式，errors用于编码错误后如何处理
    print(f.read())

#写文件
with open("e:/practice/1.txt", "a") as f: #w表示写文本文件，wb表示写二进制文件，a表示已append方式写
    f.write("hello world! python")

#StringIO和ByteIO 在内存中读写string和byte类型数据
from io import StringIO, BytesIO
fs = StringIO("hello\npython")
print(fs.getvalue())

fb = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
print(fb.read())

#操作文件和目录 os模块、path模块。注：os模块某些函数与操作系统类型相关，如win系统不支持os.uname()
import os, path
os.name #系统名称
os.environ #系统环境变量