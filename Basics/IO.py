'''
IO编程
'''

#文件读写 r表示读
f = open('E:/PythonDaily/Basics/test.txt','r')
readstr = f.read()
print(readstr)
f.close()

#用with自动调用close
with open('test.txt','r') as f:
    print(f.read())

#读取单行 readlines
with open('test.txt','r') as f:
    print(f.readlines())

#读取指定大小 read(size)
with open('test.txt','r') as f:
    print(f.read(2))