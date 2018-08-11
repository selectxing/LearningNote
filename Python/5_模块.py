#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#以上第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码
#模块（.py）、包(package)
#每一个包目录下面都会有一个__init__.py

#---使用模块---#
"模块py文件第一个字符串视为文档注释"

__author__ = "selectxing"

#import sys
#def test():
#    args = sys.argv
#    if len(args) == 1:
#        print("hello world")
#    elif len(args) == 2:
#        print("hello %s" % args[1])
#    else:
#        print("there are too many args")

##用于命令行方式调用自身测试结果，类似C中的main方法为程序入口
#if __name__ == "__main__":
#    test()


#__xxx__的变量是特殊变量，可以被直接引用，但是有特殊用途，如：__author__、__name__、__doc__等
#_xxx和__xxx的函数或变量为private，不带_前缀的则为public
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting("1234"))
print(greeting("12"))


import sys
print(sys.path)

#---安装第三方模块---#
#通过包管理工具pip安装第三方包

#命令提示符执行 pip install Pillow
#安装Anaconda