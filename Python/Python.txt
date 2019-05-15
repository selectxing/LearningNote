Python编程从入门到实践笔记
#---HelloWorld---#
1、注释：#行注释；'''块注释；"""文档字符串注释（用于生成文档）
2、彩蛋：import this导入python之禅

#---简单数据类型---#
1、字符串函数：title()、upper()、lower()。删除空格：strip()、rstrip()、lstrip()。str()函数，字符串和数字+连接会报错，用str()将数字转换为字符串
2、浮点除/，整除（地板除）//，取余%
3、布尔值：True、False
4、空值：None
5、格式化：%s，%d，format函数
6、转义字符：\t，\n，\'，\"。使用r'string'的方式可以定义为原始字符串。r表示raw的意思
7、id()，变量内存地址
8、split()方法。拆分字符串。默认无参数按空格拆分，否则按传入参数作为分隔符拆分

#---列表list[]---#
1、空列表：list1=[]。list[0]取第一个元素；list[-1]取最后一个元素。len(list1)：列表长度
2、插入元素：append()列表末尾插入。插入元素：insert() insert(0, "newelement")
3、删除元素：1、del list1[0]；2、pop()删除末尾元素，pop(i)删除位置i的元素。删除时可以赋值给变量使用；3、remove(value)，根据值删除元素。删除时可以赋值给变量使用
4、列表排序：1、sort() sort(reverse=true) 会修改列表元素顺序；2、sorted() 临时排序；3、reverse() 反转顺序
5、遍历列表：for循环 for value in list1:
6、数值列表
    1）创建列表：list(range(1,10,2))。range()参数值：起始值、终止值、步长
    2）列表函数：min()、max()、sum()：数字列表最小值、最大值、总和
    3）列表解析：list1 = [values**2 for value in range(1,4)]
7、切片
    1）list1[0:3]起始值、终止值，终止值的前一个元素。list1[:3]省略起始值默认从列表头开始。list1[2:]省略终止值默认到列表末尾结束。list1[-3:]倒数第三个元素至末尾
    2）复制列表：list2 = list1[:]。注：使用直接=赋值的方式，修改原列表，赋值的新列表也会同时变更

#---元组tuple()---#
1、元组的元素不可修改，但可以给存储元组的变量赋值。元组相对可变：某个元素是列表，修改该列表值，元组也变化。空元组tuple1=()
2、遍历元组：for循环 for value in tuple1:

#---字典dict{}---#
1、空字典：dict1={}。dict1[key]取键key的value。
2、添加键-值对：dict1[key]=value1、dict2[key2]=value2，键-值对排列顺序与添加顺序不同
3、删除键-值对：del dict1[key]
4、遍历字典：for循环 for key, value in dict1.items(): 其中：key、value可以使用易于理解的变量名。dict.keys(): 遍历所有key。dict.values():遍历所有value
5、嵌套：列表中存字典list1=[dict1, dict2, dict3]；字典中存列表dict1={list1, list2, list3}；字典中存字典dictA={dict1, dict2, dict3}

#---集合set()---#
1、需要提供list作为输入集合。set1 = set(list1)。交集&，并集|。集合自动去重

#---if、while控制---#
1、变量判断：==、!=、>、<、>=、<=、and、or、()的使用
2、列表判断：in、not in的使用，判断元素是否在列表中
3、if、if-else、if-elif-else的使用。if 变量：变量非空时返回True
4、while循环。while True:使用标识退出；break、continue关键字
5、input()函数。将输入解读为字符串，如果输入为整数，可以使用int()将字符串转换为整数。python2.7中为raw_input()

#---函数---#
1、形参、实参的概念。可将函数赋给变量，相当于给函数起别名。用pass占位符构建空函数
2、位置实参。传递给函数名称-值对，从而不必关心参数顺序，如：max(par1=1, par2=3)
3、参数默认值。有默认值的参数放在最后
4、返回值，return。返回简单变量、列表、字典等均可。多个返回值：return x,y，返回list
5、任意数量的实参。def func(*para)，传入的参数将封装为元组tuple。任意数量实参可跟形参一起使用，形参放至最前
6、任意数量的关键字实参。def func(**para)，传入的参数为键-值对
7、将函数存入模块.py文件。导入使用方式：
    1）import py，导入模块。import py as p，导入模块并给模块指定别名。调用模块中函数时需使用“模块名.函数名”的方式
    2）from py import func，从模块中导入函数。导入多个函数用“,”分隔。from py import func as f，从模块中导入函数并指定别名。调用函数时无需使用“模块名.函数名”方式，直接调用函数即可
    3）from py import *，从模块中导入全部函数。尽量避免此种方式
    4）from py import Class, 从模块中导入类。导入多个类用“,”分隔。

#---类---#
1、创建类，属性、方法。__init__方法，self参数。根据类型创建对象实例，访问属性，方法
2、修改属性的值的方法：1）直接引用修改，2）通过方法修改，3）通过方法对属性的值递增
3、继承
    1）super()函数：super().__init()__
    2）子类的属性、方法
    3）重写父类方法：方法名与父类相同
    4）实例用作属性。某些属性具有共性，提取为单独类赋给其他类的属性，如：self.battery = Battery()
4、导入类、导入模块。

#---文件和异常---#
1、打开文件open(path,mode)方法。path：相对路径、绝对路径。mode: r读取（默认r）、w写入、a附加、r+读取写入
2、读取文件
    1）read方法：with open(path) as file_object: file_object.read()
    2）逐行读取。for i in file_object，或list1=file_object.readlines()。注意：有readline()和readlines()两个方法，分别为读取一行、所有行
3、写入文件
    1）write()方法。参数只能为字符串，数字需要用str()方法转换后写入
    2）w模式，清除文件内容并写入
    3）a模式，附加到文件末尾
4、异常
    1）try/except
    2）except后面可以跟else执行成功分支的代码
5、存取数据。json.dump()和json.load()