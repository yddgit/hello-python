#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了一套异常处理机制，进行错误处理
# try...except...finally...

# 当某些代码可能会出错时，可以用try来运行这段代码。
# 如果出错，后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
# 以上，当错误发生时，后续代码并没有被执行，最后finally语句被执行

# 多个except语句块处理不同类型的错误
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'

# 如果没有错误发生，还可以在except语句块后面增加一个else，当没有错误发生时会自动执行else语句
try:
    print 'try...'
    r = 10 / 2
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

# Python所有的错误类型都继承自BaseException，所以在except时，不但捕获该类型的错误，还会把其子类也“一网打尽”
try:
    print 'foo'
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'
# 上面的第二个except永远也得不到执行，因为ValueError是StandardError的子类

# 常见的错误类型和继承关系参考官方文档：
# https://docs.python.org/2/library/exceptions.html#exception-hierarchy

# try...except可以跨越多层调用，如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
def bar(s):
    return 10 / int(s)
def foo(s):
    return bar(s) * 2
def main():
    try:
        foo('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'
main()
# 即不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了

# 调用堆栈

# 如果错误没有被捕获，就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def main():
    foo('0')
#main()
# 执行以上main()方法，会打印出错误的调用函数链

# 记录错误

# 既然能捕获错误，就可以把错误堆栈打印出来，然后分析原因，同时，让程序继续执行下去
# Python内置的loggin模块可以非常容易的记录错误信息
import logging
logging.basicConfig(level=logging.INFO)
def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
main()
print 'END'
# 同样是出错，但程序打印完成错误信息后会继续执行，并正常退出
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查

# 抛出错误

# 根据需要定义错误class，选择好继承关系，然后用raise语句抛出一个错误的实例
class FooError(StandardError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
#foo(0)
# 只有必要的时候才定义我们自己的错误类型，如果可以选择内置错误类型，尽量使用内置的错误类型，如ValueError、TypeError

# 捕获错误后再抛出
# 这种处理主要目的是记录一下错误，便于后续追踪。当前函数并不知道该怎么处理该错误，所以继续往上抛，让顶层调用者去处理
def foo(s):
    n = int(s)
    return 10 / n
def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise
def main():
    bar('0')
#main()
# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外在except中raise一个Error时，还可以把一个类型的错误转化成另一种类型
# 只要转换逻辑合理，决不应该把一个IOError转换成毫不相干的ValueError
def foo():
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
#foo()

# 调试

# 可以用print语句，但调试完后还要一一删除
def foo(s):
    n = int(s)
    print '>>> n = %d' % n
    return 10 / n
#foo('0')

# 断言

# 使用print的地方也可以用断言，启动Python解释器时可以用-O参数来关闭assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
#foo('0')

# logging

# logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    print 10 / n
#foo('0')

# Python调试器pdb

# pdb可以让程序以单步方式运行，随时查看运行状态
# 以参数-m pdb启动：python -m pdb test.py
# 输入[l]查看代码，输入[n]单步执行，输入[p 变量名]来查看变量，输入[q]结束调试

# pdb.set_trace()

# 这个方法也是用pdb，但不需要单步执行，只需要import pdb
# 然后在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb
s = '0'
n = int(s)
#pdb.set_trace()
#print 10 / n
# 程序自动在pdb.set_trace()暂停并进入pdb调试环境，可以用p命令查看变量或者用c命令继续执行

# 如果要比较方便的设置断点、单步执行，就需要一个IDE
# 目前比较好的Python IDE有PyCharm，Eclipse加上pydev插件也可以高度Python程序

# 单元测试

# 编写一个Dict类，行为与dict一致，但是可以通过属性来访问
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

# 编写单元测试需要引入Python自带的unittest模块
import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
# 编写单元测试时，需要编写一个测试类，从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试时不会被执行
# 对每一个类测试都需要编写一个test_xxx()方法

# unittest.TestCase提供了很多内置的条件判断：
class TestDemo(unittest.TestCase):
    def test_demo(self):
        # 常用的断言就是assertEquals()
        self.assertEqual(abs(-1), 1)
        # 另一种就是期待抛出指定类型的Error
        with self.assertRaises(ZeroDivisionError):
            n = 10 / 0

# 运行单元测试
#if __name__ == '__main__':
#    unittest.main()
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试（注意最后跟的是模块名，不是脚本文件名）
# python -m unittest test

# setUp与tearDown
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法，这两个方法每调用一个测试方法的前后分别被执行
class TestSetUpTearDown(unittest.TestCase):
    def setUp(self):
        print 'setUp...'
    def tearDown(self):
        print 'tearDown...'
    def test_run(self):
        self.assertEqual(max((1,2,3,4)), 4)
        print 'test case finished'

# 文档测试

# Pythont很多文档都有示例代码，如re模块就带了很多示例代码
'''
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
'''
# 可以把这些示例代码在Python交互式环境下输入并执行，结果与文档中的示例代码显示的一致
# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档
# 既然这些代码本身就可以粘贴出来直接运行，那么，可否自动执行写在注释中的代码呢？答案是肯定的

# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
# Python严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段输出

# 如下：Dict类
class Dict(dict):
    '''
    Simple dict but also support access as x.y style

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# doctest非常有用，不但可以用来测试，还可以直接作为示例代码

