'''
函数式编程
'''
from functools import reduce 
from functools import wraps
import datetime

#高阶函数(Higher-order function)

#变量可以指向函数
T = type

#函数接受另一个函数作为参数，就是告诫函数
def add(x,y,f):
    return f(x) + f(y)

add(5,-5,abs)

#map,接受两个参数，一个函数，一个Iterable，返回一个Iterator
def square(x):
    return x*x

l = map(square,range(5))
'''
'''
def multiply(tst, lsl):
    return tst*lsl

#randuce把结果和下一个元素做累计运算
l = reduce(multiply,range(1,101))

#filter-过滤序列，根据返回值判断是否保留㢝
l = [0,1,1.1,2,2.1]

def only_int(x):
    return x == int(x)

l = list(filter(only_int,l))

#sorted 排序
sorted(l, key=abs, reverse=False)

sorted(l, reverse = False)

#返回函数
def return_fun(arg):
    if arg == 1:
        return type
    if arg == 2:
        return abs
    else:
        return str

#闭包
def numtostr():
    arr = range(5)
    def loop():
        for i in arr:
            print(i)
    return loop

#匿名函数 lambda 参数：表达式 只能又一个表达式，返回值就是表达式结果
anonymity = lambda x:x*x
print(anonymity(2))

#装饰器-在代码运行期间动态增加功能
def log(fun):
    @wraps(fun) #复制原始函数属性
    def wrapper(*arg,**keyarg):
        print('name:%s,time:%s'%(fun.__name__,datetime.datetime.now()))
    return wrapper

@log
def test():
    print('test')

#偏函数，固定函数参数 接受函数对象/*args/**kw三个参数
import functools
inttwo = functools.partial(int,base=2)
print(inttwo('100'))

test()
