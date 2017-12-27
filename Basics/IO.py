'''
IO编程
'''

#文件读写 r表示读
f = open('E:/PythonDaily/Basics/test.txt','r',encoding='utf-8')
readstr = f.read()
print(readstr)
f.close()

#用with自动调用close
with open('test.txt','r',encoding='utf-8') as f:
    print(f.read())

#读取单行 readlines
with open('test.txt','r',encoding='utf-8') as f:
    print(f.readlines())

#读取指定大小 read(size)
with open('test.txt','r',encoding='utf-8') as f:
    print(f.read(2))

#二进制文件
f = open('test.txt','rb')
print(f.readlines())
    
#字符编码,用errors忽略编码错误
f = open('test.txt','r',encoding='utf-8',errors='ignore')
print(f.read())

#写文件-传入标识符w或wb
f = open('test.txt','w')
f.write('Hello,Python!')
f.close()

with open('test.txt','a') as f:
    f.write('Hi')