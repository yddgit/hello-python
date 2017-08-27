#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Python中，一个.py文件就称之为一个模块（Module）。使用模块可以提高代码的可维护性，其次代码不必从零开始。
# 当一个模块编写完毕，就可以被其他地方引用。在编写程序的时候，也经常引用其他模块，包括Python内置的模块和第三方模块。

# 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中。
# 因此，在编写模块时，不必考虑名字会与其他模块冲突。

# 但是也要注意，尽量不要与内置函数名字冲突，访问如下地址查看Python的所有内置函数
# http://docs.python.org/2/library/functions.html

# 同时，为了避免模块名冲突，Python引入了按目录来组织模块的方法，称为包（Package）

# 如，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块
# 假设abc和xyz这两个模块名字与其他模块冲突了，可以通过包来组织模块，避免冲突。
# 方法是选择一个顶层包名，如mycompany，按照如下目录存放
# mycompany
#   +--- __init__.py
#   +--- abc.py
#   \--- xyz.py

# 引入包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突，此时模块名也不一样，
# abc.py的模块名字就变成了mycompany.abc，类似xyz.py的模块名变成mycompany.xyz

# 注意：每个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名称就是mycompany

# 类似的，可以有多级目录，组成多级层次的包结构，如下
# mycompany
#   +--- __init__.py
#   +--- abc.py
#   +--- utils.py
#   +--- xyz.py
#   \--- web
#          +--- __init__.py
#          +--- utils.py
#          \--- www.py
# www.py的模块名称就是mycompany.web.www
# 两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils
# mycompany.web模块对应的文件是mycompany/web/__init__.py

# 使用模块

# Python内置了很多非常有用的模块，以sys模块为例

#####################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Yang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello World!'
    elif len(args) == 2:
        print 'Hello %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()

#####################

# 以上，第1、2行是标准注释，接下来的字符串表示模块的文档注释
# 任何模块代码的第一个字符串都被视为模块的文档注释
# 然后使用__author__变量把作者写进去
# 以上就是Python模块的标准文件模板，后面开始真正的代码部分

# 使用模块的第一步就是导入该模块，如：import sys
# 导入sys模块后，就有了变量sys指向该模块，利用sys变量，就可以访问sys模块的所有功能
# sys模块有一个argv变量，用list存储了命令行的所有参数。
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称
print sys.argv

# 当在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__
# 而如果在其他地方导入模块则不会设置__name__变量。
# 因此，这可以让一个模块通过命令行执行一些额外的代码，常见的就是运行测试

# 别名

# 导入模块时，可以指定别名：import <module_name> as <alias_name>
# 如Python标准库一般会提供StringIO和cStringIO两个库，两者接口和功能相同，
# 但cStringIO是C写的，速度更快，所以经常会有：
try:
    import cStringIO as cStringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
# 这样就可以优先导入cStringIO，如果有些平台不提供，还可降级使用StringIO
# 导入时指定了别名StringIO，因此后续代码引用StringIO即可正常工作

# 还有类似simplejson这样的库，在Python2.6之前是独立的第三方库，从2.6开始内置
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5
# 由于Python是动态语言，函数签名一致接口就一样，因此无论导入哪个模块后续代码都能正常工作

# 作用域

# 在一个模块中，对于公共变量/函数和私有变量/函数，通过_前缀来实现

# 1. 正常的函数和变量名是公开的public，可以直接被引用，如：abc，x123，PI
# 2. 类似__xxx__这样的变量是特殊变量，可以直接引用，但有特殊用途，如：__name__，__author__
# 模块定义的文档注释也可以用特殊变量__doc__访问，自己的变量一般不要使用这种变量名
# 3. 类似_xxx和__xxx这样的函数和变量是非公开的private，不应该直接引用，如：_abc，__abc
# Python并没有一种方法可以完全限制访问private函数或变量，但从编程习惯上不应该引用private函数或变量

def _private_1(name):
    return "Hello, %s" % name

def _private_2(name):
    return "Hi, %s" % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 以上，在模块中公开greeting()函数，把内部逻辑用private函数隐藏起来，调用greeing()函数不用关心内部函数细节
# 这是一种非常有用的代码封装和抽象的方法：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

