'''
面向对象高级编程
'''

class Student(object):
    pass
s = Student()

#给实例绑定属性
s.name = 'Tom'

#给实例绑定方法
def set_name(self, name):
    self.name = name

from types import MethodType
s.set_name = MethodType(set_name,s)
s.set_name('Rose')

#给class绑定方法，所有实例均可调用
Student.set_name = set_name

#使用__slots__——限制class实例能添加的属性，仅对当前类实例起作用
class Student(object):
    __slots__ = ('name','age')
#新创建的实例只能添加name和age属性

#使用@property,只定义getter不定义setter就是只读属性
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raisse ValueError('score must be an integer!')
        if value <0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

#多重继承一个类可以继承多个类以获得多个父类的功能
class School(object):
    def classroom():
        print('classroom')

class Teacher(object):
    def teach():
        print('teach')

class Student(School,Teacher):
    pass


#定制类

class Student(object):
    __init__(self):
        self.a = 0
    #定制print显示内容
    def __str__(self):
        print('student')
    #定制直接显示变量
    __repr__ = __str__
    #让类可迭代
    def __iter__(self):
        return self
    def __next__(self):
        self.a = self.a + 1
        if self.a>10:
            raise StopIteration()
        return self.a
    #让类可按下标取出元素
    def __getitem__(self,n):
        return n + 1
    