"""
字符串
"""

ord('A')  # 获取字符的证书表示

chr(65)  # 把编码转换为对应的字符

STRING = '\u4e2d'  # 十六进制

X = b'abc'  # bytes类型数据

string = 'abc'

blob = string.encode('ascii')  # 通过encode方法编码为指定bytes

# 通过decode方法把bytes变为str,如果有一小部分无效字节，可以传入errors=‘ignore’忽略错误字节
string = blob.decode('ascii', errors='ignore')

n = len(string)  # 计算str包含多少个字符，换成bytes格式就计算字节数

# 格式化

hello = 'hello,%s' % 'name'
print(hello)

'''
用%运算符格式化字符串
%d 整数
%f 浮点数
%s 字符串
%x 十六进制整数
%s永远起作用，它会把任何数据类型转换为字符串
'''

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%50d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# format(),它会用传入的参数依次替换字符串内的占位符{0}、{1}……
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
