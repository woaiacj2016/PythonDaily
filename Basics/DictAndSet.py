'''
Dict 和 Set
'''

#dict 键值对存储

#键名可以是变量
c = 'c'
dictionary = {'a':1,'b':2,c:3}

#转化
dictionary = dict([(1,'a'),('b',2),('c',3)])

#后值会覆盖前值
dictionary[c] = 'f'

#通过in和get方法判断key是否存在
boolean = c in dictionary
boolean = dictionary.get(c,False)

#set key集合 不可存入可变对象 自动过滤重复对象
s = set([(1,'a'),('b',2),('c',3)])

#通过add添加元素到set中
s.add(1)

#通过remove删除元素
s.remove(1)