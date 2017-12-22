#错误、调试和测试

#错误处理,try运行可能出错的代码，出错后跳转到except语句，最后一定执行finally,except语句可以有多个来捕捉不同类型的异常,except语句后可以跟else语句，如果没有错误发生就会执行
import logging
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
#记录错误-python内置的logging模块可以记录错误信息-可指定记录错误级别，可输出错误信息到文件
    logging.exception(e)
    print('except:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('End')

#调用栈-可以定位错误位置

#抛出错误-定义一个错误的class，选择好继承关系，就可以用raise语句抛出一个错误的实例

#断言-如果断言失败会抛出AssertionError 启动python解释器时可以用-O参数关闭assert
def test(n):
    assert n != 0, 'n is zero'
    return n

test(0)

#pdb 让程序以单步方式运行 n 单步执行 p 变量名查看变量 l 查看代码 q 结束调试

import pdb

#设置断点 命令 c 继续运行
pdb.set_trace()