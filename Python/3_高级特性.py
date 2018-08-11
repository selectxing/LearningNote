#---高级特新---#
#切片（Slice）substring的终极升级
lista = list(range(101))
print(lista[1:10])  #从位置1开始，共10个元素
print(lista[-2:-1]) #从倒数第2个位置开始，共1个元素
print(lista[::5])   #从位置0开始，全部元素，步长5
#print(lista[::]) #复制序列

#tuple与list类似
tuplea = tuple(range(101))

#string可以看做是list
a = "abcdefgh"
print(a[0:4])
print(a[::2])

#迭代
dicta = {"a":1,"b":2,"c":3}
for key in dicta:
    print(key)
for value in dicta.values():
    print(value)
for item in dicta.items():
    print(item) #返回tuple
    print(item[1])
for x,y in((1,2),(2,3),(3,4)):
    print(x,y)

#列表生成式
print(list(range(1,11)))
print([x for x in range(1,11)])
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 != 0])
print([m + n for m in "ABC" for n in "XYZ"])

import os
print([d for d in os.listdir('.')])

d = {"A":"x","B":"y", "C":"z"}
print([k + "=" + v for k,v in d.items()])  #多变量列表生成式
L = ['Hello', 'World', 18, 'Apple', None]
print([l.lower() for l in L if isinstance(l, str)])  #利用isinstance判断元素是否某种数据类型

#生成器generator 列表关键字[]，生成器关键字() 一边循环一边计算的机制，称为生成器。避免占用内存
#【生成器的第一种写法】
g = (x for x in "ABC")
for i in g:
    print(i)

#斐波那契数列
def fib(x):
    a, b = 0, 1
    while x > 0:
        print(b)
        a, b = b, a + b
        x = x - 1
    return
print(fib(10))

#fib函数实际是定义了斐波那契数列的推算规则，可以从第一个元素推算出后面元素，这种逻辑非常类似生成器
#fib生成器，只需将print替换为yield即可
#【生成器的第二种写法】
def fib(x):
    a, b = 0, 1
    while x > 0:
        yield(b)
        a, b = b, a + b
        x = x - 1
    return
o = fib(10)
for o1 in o:
    print(o1)

#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [(L + [0])[i] + ([0] + L)[i] for i in range(len(L) + 1)]
o = triangles()
print(next(o),next(o),next(o),next(o))

#迭代器
#可以用for循环的对象统称为：可迭代对象(Iterable)
#可以用next()函数调用并不断返回下一个值的对象称为：迭代器(Iterator)
from collections import Iterable
from collections import Iterator
print(isinstance([x for x in range(1,11)],Iterable))
print(isinstance([x for x in range(1,11)], Iterator))
print(isinstance((x for x in range(1,11)), Iterator))
print(isinstance(iter([x for x in range(1,11)]), Iterator))  #使用iter函数由Iterable获取Iterator

#Python的for循环本质上就是通过不断调用next()函数实现的，以下两种代码等价
for x in [1,2,3,4,5]:
    pass

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break