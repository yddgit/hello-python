#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量。
# 因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。

# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，
# 同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# Python对函数式编程提供部分支持，由于Python允许使用变量，因此，Python不是纯函数式编程语言

# 高阶函数Higher-order function

# 如下abs(-10)是函数调用，而abs是函数本身
print abs(-10)
print abs
# 函数本身也可以赋值给变量，即变量可以指向函数
f = abs
print f(-14)
# 函数名也是变量，函数名其实就是指向函数的变量。如果把abs指向其他对象，就不能通过abs调用该函数了
#abs = 10
#abs(-10)
#print abs
# 注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其他模块也生效，要用__builtin__.abs = 10

# 函数参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称为高阶函数
def add(x, y, f):
    return f(x) + f(y)
print add(-5, 6, abs)

# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce()把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
print reduce(add, [1, 3, 5, 7, 9])
#print sum([1, 3, 5, 7, 9])

# 如果要把[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])

# 将str转换为int
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print reduce(fn, map(char2num, '13579'))
# 整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn, map(char2num, s))
print str2int('123456')
# 还可以用lambda函数进一步简化：
def str2int_(s):
    return reduce(lambda x, y : x * 10 + y, map(char2num, s))
print str2int_('654321')

# 利用map()函数把用户输入的不规范的英文文字变为首字母大写，其他小写的规范名字
def convert_name(name):
    return name[0].upper() + name[1:len(name)].lower()
print convert_name('hellO')
print map(convert_name, ['adam', 'LISA', 'barT'])
# 利用reduce()函数求积
print reduce(lambda x, y : x * y, [1, 2, 3, 4, 5, 6])
