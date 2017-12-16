'''
函数式编程
'''
from functools import reduce 

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
sorted(l)
sorted(l,reverse=True)
sorted(l,key=abs)
sorted(cmp=None)