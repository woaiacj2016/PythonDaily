'''
列表和元组
'''

#列表
arr = ['one', 'two', 'three']
#获取长度
num = len(arr)
#用索引访问list中元素，从0开始,可用负数做索引，倒数取值
arr[0]
#追加元素到末尾
arr.append('four')
#插入指定位置
arr.insert(3, 'four')
#删除末尾元素
arr.pop()
#删除指定位置元素
arr.pop(3)
#替换元素，直接复制给对应索引
arr[2] = 'end'


#元组，初始化后不可修改
TUPLE = tuple(arr)
#用索引访问tuple中元素，从0开始,可用负数做索引，倒数取值
TUPLE = TUPLE[0]
