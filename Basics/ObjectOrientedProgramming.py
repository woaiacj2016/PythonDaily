'''
面向对象编程(OOP)
把对象作为程序的基本单元，包含了数据和操作数据的函数
'''

#面向过程把计算机程序视为一系列命令集合

talk = {'me':'Hello','you':'Hi'}
answer = {'me':'NTMY','you':'MTMYT'}

def ttalk(arg):
    if isinstance(arg,dict):
        print('%s\r\n%s'%(arg['me'],arg['you']))
    else:
        pass

ttalk(talk)

class Chat(object):
    def __init__(self,me,you):
        self.mine = me
        self.you = you

    def print_talk(self):
        print('%s\r\n%s'%(self.mine,self.you))

talk = Chat(talk['me'],talk['you'])
answer = Chat(answer['me'],answer['you'])
talk.print_talk()
answer.print_talk()

#类和实例-类是抽象的模板，定义类通过class关键字 类名(父类)
class Student(object):
    pass

#实例通过类名()实现
st = Student()

#类可以起到模板作用，创建实例时，把要绑定的属性填写进去，通过__init__方法在创建时绑定
class Student(object):
    #第一个参数永远是self，表示创建实例本身，有了__init__方法，创建实例时，就不能传入空参数了
    def __init__(self,name,score):
        self.name = name
        self.score = score
    #数据封装，在类的内部定义访问数据的函数，称为类的方法，可以通过实例调用
    def print_score(self):
        print('%s:%s'%(self.name,self.score))

#访问限制，在属性名前加两个下划线__,就成为私有变量，外部不能访问，通过get，set方法获取和修改

#继承和多态，在定义class的时候，可以从现有的class继承，新的class称为子类(Subclass)，被继承的class称为基类，父类和超类(Base class、Super Class)
class Animal(object):
    def run(self):
        print('Animal is running...')

#子类继承父类全部功能
class Dog(Animal):
    pass

#子类可以重写父类方法,对扩展开放，对修改封闭
class Cat(Animal):
    def run(self):
        print('Cat is running...')

#获取对象信息

#通过type判断
type(Dog) == Dog

#使用isinstance
isinstance(Dog(),Dog)

#使用dir函数，返回包含对象所有属性和方法的list，配合getattr，setattr以及hasattr操作对象状态
dir(Dog())

getattr(Dog(),'__class__')

setattr(Dog(),'test',100)

hasattr(Dog(),'__name__')

#实例属性和类属性

#直接在class中定义属性，这种属性所有实例都可以访问到，实例属性和类属性同名时，类属性会被覆盖
