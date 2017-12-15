'''
高级特性
'''
from collections import Iterable

NUM = [1,2,3,4,5]

#切片-取指定索引范围值
N = NUM[0:3]

#第一个参数为0可以省略
N = NUM[:3]

#支持倒数
N = NUM[-5:-3]

#迭代
for n in NUM:
    print(n)

#通过cllections模块的Iterable类型判断
isinstance('string',Iterable)

#列表生成式
LIST = [x*x for x in range(5)]
LIST = [m*n for m in range(5) for n in range(5,10)]

#生成器-迭代器对象
LIST = (x*x for x in range(5))

#获取下一个返回值
next(LIST)

#函数方式
def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    return 6

g = generator()
n = next(g)
n = next(g)
n = next(g)
n = next(g)
n = next(g)

#捕获返回值
try:
    n = next(g)
except StopIteration as e:
     print('Generator return value:', e.value)