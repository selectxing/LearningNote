#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"6_面向对象"

__author__ = "selectxing"

#面向对象#
class Student(object):
    #__init__方法的第一个参数永远是self，表示创建的实例本身，在init内部可把各种属性赋值给self
    #__init中的属性为强制属性，创建实例时必须赋值
    def __init__(self, name, age, score):
        self.name = name
        self.score = score
        self.__age = age #private属性

    #类中定义的函数第一参数永远是self，调用时不用传递该参数        
    def print_score(self):
        print("%s's score is: %s" % (self.name, self.score))

    def print_grade(self):
        if self.score >= 90:
            print("优秀")
        elif self.score >=60:
            print("良")
        else:
            print("不及格")

    #get、set方法
    def get_age(self):
        return self.__age

    #set方法可对参数做检查，避免传入无效的参数：
    def set_age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("无效年龄")

jack = Student("jack", 17, 99)
jack.print_score()

#可以自由地给一个实例变量绑定属性
jack.sex = "男"
print(jack.sex)

jack.print_grade()
print(jack.get_age())

jack.set_age(151)
print(jack.get_age())