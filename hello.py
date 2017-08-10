#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################

print "Hello World"

# 单行注释，raw_input接受终端用户输入
name = raw_input("Please enter your name: ")

'''
这是一个多行注释的示例
以下语句将刚才输入的内容回显为：Hello xxxx
'''
print "Hello", name

# print absolute value of an integer
# 当语句以冒号“:”结尾时，缩进的语句视为代码块。
a = 100
if a >= 0:
    print a
else:
    print -a

#################################################

# 整数
print "\n=========Integer:"
print 200+300
print -8000
print 0xff00 # 16进制数
print 0xa5b4c3d2
print 011 # 8进制数

# 符点数
print "\n=========Float:"
print 3.1415926
print 1.23
print -9.01
print 1.23e9
print 12.3e8
print 1.2e-5

# 字符串
print "\n=========String:"
print "I'm OK!"
print 'I\'m \"OK\"!' # 转义字符\，支持\n，\t，\\等
print 'I\'m learning\nPython.'
print '\\\n\\'
print '\\\t\\'
print r'\\\t\\' # Python还允许用r''表示''内部的字符串默认不转义
print '''line1
line2
line3''' # Python允许用'''...'''的格式表示多行内容
print r'''line1\n
line2\n
line3\n''' # 多行字符串'''...'''还可以在前面加上r使用

# 布尔值（True/False）
print "\n=========Boolean:"
print True
print False
print "3>2:", 3>2
print "3>5:", 3>5
print "True and True:", True and True
print "True and False:", True and False
print "False and False:", False and False
print "True or True:", True or True
print "True or False:", True or False
print "False or False:", False or False
print "not True:", not True
print "not False:", not False

age = 27
if age >= 18:
    print 'Adult'
else:
    print 'Teenager'

# 空值（None）
# 空值是Python里一个特殊的值，用None表示，None不能理解为0，因为0有意义，None是一个特殊的空值
print "\n=========None:"
print None

#################################################

# 变量
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
print "\n=========Variable"
a = 'ABC'
# 上面一句代码，Python解释器干了两件事情：
# - 在内存中创建了一个'ABC'的字符串；
# - 在内存中创建了一个名为a的变量，并把它指向'ABC'。
b = a
a = 'XYZ'
print b

# 常量
# 通常用全部大写的变量名表示常量，但事实上Python根本不能保证常量值不会被改变
print "\n=========Constant"
PI = 3.14159265359
print PI

# 整数除法
print "\n=========Divide"
print "10 / 3 =", 10 / 3
print "10.0 / 3 =", 10.0 / 3
print "10 % 3 = ", 10 % 3