#---数据类型---#
#字符串
print('HelloWold' + "Test" + "你好")
print("1","2","3")

#布尔值
a = True
print(a)

#空值
a = None
print(a)

#转义符
print("i'm \'ok\'")
print('''1...2...3''')  #换行？

#浮点除/、整除（地板除）//、取余%
print(9 / 3)   #3.0
print(9 // 3)  #3
print(10 / 3)  #3.3333333333333335
print(10 // 3) #3
print(10 % 3)  #1

#格式化字符串
print("hello %s, welcome to %s, today is %d" % ("zhang", "china", 20170625))
print("hello {0}, welcome to {1}, today is {2}" .format("zhang", "china", 20170625)) #字符串中的“.”写法？

#列表list 关键字[]
lista = ["test1","test2","test3"]
listb = []  #空列表
print("第一个元素：" + lista[0] + " 最后一个元素：" + lista[len(lista) - 1] + " 最后一个元素的另外一种写法：" + lista[-1])
lista[0] = "test0"
lista.append("testadd")  #末尾追加元素
lista.insert(1, "test_insert")  #某位置插入元素
lista.pop()  #删除末尾元素
listb = [11, 22, lista, 33]  #二元列表
print(listb)

#元组tuple 关键字()
#一旦初始化其元素就不能修改，代码安全
tuplea = ("test1","test2","test3")
tupleb = ()  #空tuple
tupleb = (11, 22, tuplea, 33)
tuplec = (11, 22, lista, 33)
lista[-1] = "tuple相对可变"
print(tuplec)

#---dict和set---#
#字典dict 关键字{} 访问元素：字典名[]。判断键key是否存在in。可以修改值value但不可修改键key
dictTest = {"tony":80, "jack":92, "lily":99}
dictTest.pop("tony")
dictTest["lily"] = 75
if "sss" in dictTest:
    print(dictTest["sss"])
elif "lily" in dictTest:
    print(dictTest["lily"])

#集合set 关键字set()，需要提供list作为输入集合。交集&，并集|
setTestA = set([1,2,3,4])
setTestB = set([2,3,5,7,8])
print(setTestA & setTestB)

listTestA = ["A", "B", "C"]
tupleTestA = (1,2,3)
setTestA = set([1,2,tupleTestA,4])
setTestA.add("TTT")

#***重要概念***
#可变对象、不可变对象的概念
#list、dict属于可变对象；string、tuple、set属于不可变对象？？？
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回


#---流程控制---#
#ifelse判断
a = int(input("input first num:")) #input返回为string，所以需要转换为int
b = int(input("input second num:"))
if a > b:
	print("result:",a,">",b)
elif a == b:
	print("result:",a,"=",b)
else:
	print("result:",a,"<",b)

#for循环
tuplefor = (11, 22, ["test1", "test2"], 44)
for tuplei in tuplefor:
    print(tuplei)

#range函数：生成整数序列
sum = 0
listsum = range(101)
for listi in listsum:
    if listi % 2 == 0:
        continue
    sum = sum + listi
print(sum)

#while循环
sum = 100
n = 99
while n > 0:
    if sum > 1000:
        break
    sum = sum + n
    n = n - 2
print(sum)