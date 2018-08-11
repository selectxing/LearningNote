#---函数---#
print(abs(-100))
print(max(1,3,-5,200))

a = max  #函数名其实就是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”。貌似没什么用
print(a(1,2,3))

#定义函数
def MyABS(x):
    if x > 0:
        return x
    else:
        return -x

print(MyABS(-666))

#空函数 pass占位符
def nop():
    pass

#多个返回值函数
def MultiReturnFunc(x, y):
    retSum = x + y
    retDiff = x - y
    return retSum, retDiff

tupleTest = MultiReturnFunc(20,11)
print(tupleTest[1])

#默认参数
#可变参数
#关键字参数
#命名关键字参数

#递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))