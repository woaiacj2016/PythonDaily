'''
面向对象高级编程
'''


class Student(object):
    pass


s = Student()

# 给实例绑定属性
s.name = 'Tom'

# 给实例绑定方法


def set_name(self, name):
    self.name = name


from types import MethodType
s.set_name = MethodType(set_name, s)
s.set_name('Rose')

# 给class绑定方法，所有实例均可调用
Student.set_name = set_name

# 使用__slots__——限制class实例能添加的属性，仅对当前类实例起作用


class Student(object):
    __slots__ = ('name', 'age')


# 新创建的实例只能添加name和age属性

# 使用@property,只定义getter不定义setter就是只读属性


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


# 多重继承一个类可以继承多个类以获得多个父类的功能


class School(object):
    def classroom():
        print('classroom')


class Teacher(object):
    def teach():
        print('teach')


class Student(School, Teacher):
    pass


# 定制类
class Student(object):   
    def __init__(self):
        self.a = 0

    def __str__(self):
        return 'student'

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a = self.a + 1
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __call__(self):
        print('调用实例')


for x in Student():
    print(x)

#使用枚举类

from enum import Enum, unique

Num = Enum('Num',('One','Two','Three'))

#unique装饰器帮助检查没有重复值
@unique
class Num(Enum):
    One = 1
    Two = 2
    Three = 3

#使用元类

#s使用type创建新的类型 参数 1.class的名称 2.继承的父类集合 3.方法名称余函数绑定
def test(self,status='success'):
    print('Test,%s'%status)

Test = type('Type',(object,),dict(test = test))

#metaclass 从type类型拍成，接受四个参数，准备创建的类的对象，类的名字，类继承的父类集合，类的方法集合