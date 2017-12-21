'''
模块
提高代码可维护性
一次编写，处处使用
'''

#包-为了避免模块名冲突,每个包目录下必须有__init__.py文件

import sys
arg = sys.argv
print('参数:%s' % arg)

#入口模块的__name__会被置为__main__
if __name__ == '__main__':
    print('测试')

#作用域 __xx__是特殊变量，文档注释可以用__doc__访问，_x非公开变量

#安装第三方模块-通过pip包管理器

#Anaconda-基于python的数据处理和科学计算平台

#模块搜索路径-sys的path变量，环境变量中的PYTHONPATH