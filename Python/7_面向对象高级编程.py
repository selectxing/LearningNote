# 面向对象高级编程
# 使用__slots__限制实例动态添加属性。仅对当前类生效，子类无效
class Person(object):
    __slots__ = ("name","sex") #使用tuple定义允许绑定的属性名称

# 使用@property装饰器(decorator)。简化get、set方法
class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('width must between 0 ~ 100!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('height must between 0 ~ 100!')
        self._height = value

    @property
    def resolution(self):   #只读属性
        return self._width * self._height

s = Screen()
s.width = 50
s.height = 60
print(s.resolution)

# 多重继承。多个父类使用,分隔

# 定制类
'''
__init__
__slots__
__str__
__iter__
__getitem__
__getattr__
__call__
'''

# 枚举类Enum
from enum import Enum, unique
Month = Enum("Month", ("Oct","Nov","Dec"))

# 默认从1开始计数
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Mon)
print(Weekday.Mon.value)

# 元类
# 完全没看懂。。。