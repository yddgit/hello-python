#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 切片

L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
print [L[0], L[1], L[2]]
# 取前n个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
print r
# 对这种经常取指定索引范围的操作，Python提供了切片（Slice）操作符
print L[0:3]
# L[0:3]表示，从索引0开始取，直到索引3为止，如果第一个索引是0，可以省略
print L[:3]
# 从索引1开始，取出2个元素
print L[1:3]
# 同样支持倒数切片
print L[-2:]
print L[-2:-1]
# 切片操作十分有用
N = range(100)
print N
print N[:10]   #前10个
print N[-10:]  #后10个
print N[10:20] #前11-20个数
print N[:10:2] #前10个数，每两个取一个
print N[::5]   #所有数每5个取一个
print N[:]     #原样复制一个list

# tuple也可以用切片操作，操作结果仍是tuple
print (0, 1, 2, 3, 4, 5)[:3]

# 字符串'xxx'或Unicode字符串u'xxx'也可以看作是list，因此字符串也可以用切片操作，操作结果仍是字符串
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

# 在很多编程语言中，针对字符串提供了很多截取函数，Python没有，只需要切片一个操作就可以完成

# 迭代

# Python的for循环不仅可以用在list或tuple上，还可以用在其他可迭代对象上
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key
for value in d.itervalues():
    print value
for k,v in d.iteritems():
    print k, '=', v
for ch in 'ABC':
    print ch
# 通过collections模块的Iterable类型判断一个对象是否是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)   # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable)     # 整数是否可迭代
# 通过下标循环list
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
# for循环里同时引用两个变量
for x, y in [(1,1), (2,4), (3,9)]:
    print x, y

# 列表生成式（List Comprehensions）

# 生成[1,2,3,4,5,6,7,8,9,10]
print range(1, 11)
# 生成[1*1,2*2,3*3,4*4,5*5,6*6,7*7,8*8,9*9,10*10]
print [x * x for x in range(1, 11)]
# 生成1-10的仅偶数的平方
print [x * x for x in range(1, 11) if x % 2 == 0]
# 使用两层循环生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']
# 运用列表生成式，列出当前目录下的所有文件和目录名
import os # 导入os模块
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# for循环同时使用两个甚至多个变量
for k, v in {'x':'A', 'y':'B', 'z':'C'}.iteritems():
    print k, '=', v
# 因此列表生成式也可以使用两个变量来生成list
print [k+'='+v for k, v in {'x':'A', 'y':'B', 'z':'C'}.iteritems()]
# 把list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
# 把字符串变成小写时判断数据类型
L = ['Hello', 'World', 18, 'IBM', 'Apple']
print [s.lower() for s in L if isinstance(s, str)]

# 生成器

# 如果列表元素可以按照某种算法推算出来，就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list
# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）
# 要创建一个Generator，有多种方法。第一种方法很简单，只要把列表生成式的[]变成()就创建了一个generator
print [x * x for x in range(10)]
g = (x * x for x in range(10))
print g
# 使用generator的next()方法获取元素值
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
# 没有更多元素时，抛出StopIteration的错误
#print g.next()

# 使用for循环迭代generator对象
for n in (x * x for x in range(10)):
    print n
# 所以创建generator后，基本不会调用next()方法，而是通过for循环来迭代

# Generator如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候还可以用函数来实现
# 如斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1,1,2,3,5,8,...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)
# 要把fib函数变成generator，只需要把print b改为yield b就可以了
# 这是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print fib_g(6)
# 这里generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
print o.next()
print o.next()
print o.next()
#print o.next()
# 可以看到，odd是一个generator，在执行过程中，遇到yield就中断，下次又继续执行
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next()就报错

# 对于一个generator，在循环过程中不断调用yield，就会不断中断
# 所以要给循环设置一个条件来退出循环，不然就会产生一个无限数列
