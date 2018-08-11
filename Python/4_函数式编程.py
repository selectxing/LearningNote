#---函数式编程---#

#高阶函数 把函数作为参数传入另一个函数
def add(x, y, abs):
    return abs(x) + abs(y)
print(add(-5, 6, abs))

#map()/reduce()函数
def squr(x):
    return x * x
print(list(map(squr, [1,2,3,4,5])))  #map返回值为Iterator是惰性序列，通过list()函数让它把整个序列都计算出来并返回一个list
print(list(map(str, [1,2,3,4,5])))

from functools import reduce
def fn(x,y):
    return x * 10 + y
print(reduce(fn, [1,3,5,7,9]))  #计算逻辑reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#map\reduce使用
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int("1133456"))

#使用lambda函数简化
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#map实现字符串首字母大写
def normalize(name):
    return name[:1].upper() + name[1:].lower()
print(list(map(normalize, ["teST","LiKe","Under"])))