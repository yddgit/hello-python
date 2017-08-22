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
