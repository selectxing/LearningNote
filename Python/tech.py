# python之禅
import this

# import、from import、import as区别
'''
import：引入整个包，调用包中某个类时需要写包名
from import：引入包中某个类，调用该类时无需再写包名
import as：引用并设置别名
'''
import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.now())

import datetime as dt
print(dt.datetime.now())

from datetime import datetime as dt
print(dt.now())

# 变量、列表、元组赋值差异。列表不能直接赋值给新变量，需要用复制方式
a = "hello"
b = a
print(a)
print(b)

a = "world"
print(a)
print(b)

list1 = ['a','b','c','d']
list2 = list1
print(list1)
print(list2)

list1[0] = "z"
print(list1)
print(list2)

tuple1 = (1,2,3)
tuple2 = tuple1
print(tuple1)
print(tuple2)

tuple1 = (5,5,5)
print(tuple1)
print(tuple2)

# 如何简单地理解Python中的if __name__ == '__main__'
'''
https://blog.csdn.net/yjk13703623757/article/details/77918633/
'''