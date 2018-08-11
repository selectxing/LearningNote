#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"6_面向对象"

__author__ = "selectxing"

#继承和多态
class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def __init__(self):
        self.classname = "狗子"
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Dog is eating...")

class Cat(Animal):
    pass

#继承父类方法
mimi = Cat()
mimi.run()

#多态
wangcai = Dog()
wangcai.run()
wangcai.eat()

class Tortoise(Animal):
    def run(self):
        print("Tortoise running slowly...")

def animal_runtwice(animal):
    animal.run()
    animal.run()

animal_runtwice(Tortoise())

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
# 由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
# 1、对扩展开放：允许新增Animal子类
# 2、对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

# 获取对象信息
# type()函数
print(type(123))
print(type(wangcai))

# types模块
import types
print(type(animal_runtwice)== types.FunctionType)

# isinstance
print(isinstance(wangcai, Cat))
print(isinstance(wangcai, Dog))
print(isinstance(wangcai, Animal))
print(isinstance(123, int))

# dir()、 getattr()、setattr()、hasattr()
print(dir(Dog))
print(hasattr(wangcai, "classname"))
print(getattr(wangcai, "classname"))
setattr(wangcai, "color", "黑色")
print(hasattr(wangcai, "color"))
print(getattr(wangcai, "color"))

print(hasattr(wangcai, "eat"))
print(getattr(wangcai, "eat"))
