'''
函数
'''

#帮助函数-查看函数帮助信息
help(abs)

#绝对值函数,只接受一个参数
abs(-100)

#最大值函数，接受多个参数，返回最大值
max(5, 1, 2, 6)

#数据类型转换函数
int('12')
float('11.11')
str(12)
bool(1)
bool(0)

#数据类型检查函数
isinstance(12,int)

#定义函数
def first_fun(x):
    print(x)

#空函数
def no():
    pass

#多个返回值-会被放入一个tuple
def mutilple():
    return 1,2

#函数参数

#位置参数-按照位置赋值残烛
def my_add(a,b):
    return a+b

#默认参数-给参数指定默认值(默认参数应指向不变对象)
def my_add(a,b=0):
    return a+b

#可变参数-在参数面前加*
def my_add(*a):
    sum = 0
    for n in a:
        sum = sum + n
    return sum

my_add(1,2,3)

my_add(*(1,2,3))

#关键字参数-在参数面前加**，参数要有参数名
def my_add(**a):
    sum = 0
    if 'addend' in a:
        sum = sum + a['addend']
    if 'augend' in a:
        sum = sum + a['augend']
    return sum

my_add(addend=12,augend=20)

my_add(**{'addend':12,'augend':20})

#命名关键字函数-在接受参数前加*
def my_add(*,addend,augend):
    return addend + augend

#前面有可变参数是时可省略#

def my_add(*a,addend,augend):
    return addend + augend

#参数组合-使用顺序:必选参数、默认参数、可变参数、关键字参数和命名关键字参数
