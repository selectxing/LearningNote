# python zen

```python
import this
```

# 编码格式

```python
# -*- coding: UTF-8 -*-
#coding=utf-8
```

>  注意：第二种方式=两边不能有空格

# 引用包

- import：引用整个包，调用包中某个类时需要写包名
- from import：引用包中某个类，调用该类时无需再写包名
- import as：引用并设置别名

```python
import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.now())

import datetime as dt
print(dt.datetime.now())

from datetime import datetime as dt
print(dt.now())
```

# 变量、列表、元组赋值

> 注意：列表不能直接赋值给新变量，需要用切片复制或list构造函数方式

```python
oldlist = [1,2,3,4]

newlist1 = oldlist

newlist2 = list(oldlist)

newlist3 = oldlist[:]

oldlist[0] = 111

print(oldlist)

print(newlist1)

print(newlist2)

print(newlist3)
```

*列表复制的5种方式*

```python
import copy

a = [[10], 20]

b = a[:]

c = list(a)

d = a * 1

e = copy.copy(a)

f = copy.deepcopy(a)

a.append(21)

a[0].append(11)

print(id(a), a)

print(id(b), b)

print(id(c), c)

print(id(d), d)

print(id(e), e)

print(id(f), f)
```

# 	if \_\_name__ == '\_\_main__'

[如何简单地理解Python中的if __name__ == '__main__'](https://blog.csdn.net/yjk13703623757/article/details/77918633/)

1. 程序的虚拟入口

   当.py文件被直接运行时，`if __name__ == '__main__'`之下的代码块将被运行

   当.py文件以模块形式被导入时，`if __name__ == '__main__'`之下的代码块不被运行

2. \_\_name__

3. \_\_main__

