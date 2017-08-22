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

# Python内建的filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列，和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True/False决定保留还是丢弃该元素
# 如：在一个list中，删除偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1,2,4,5,6,9,10,15])
# 删除一个序列中的空字符串
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 取出1-100的素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n/2):
        if n % i == 0:
            return False
    return True
print filter(is_prime, range(1, 101))

# 排序算法在程序中非常常用，其核心是比较两个元素的大小，通常规定，对于两个元素x和y
# 如果x < y，则返回-1
# 如果x = y，则返回0
# 如果x > y，则返回1
print sorted([36,5,12,9,21])
# 如果要倒序排列
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36,5,12,9,21], reversed_cmp)
# 字符串排序，按照ASCII的大小比较，由于'Z' < 'a'，所以Z会排在a的前面
print sorted(['bob','about','Zoo','Credit'])
# 忽略大小写的排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob','about','Zoo','Credit'], cmp_ignore_case)

# 函数做为返回值

# 如：通常情况下的求和函数是这样定义
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 如果不需要立刻求和，而是在后面的代码中根据需要再计算
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 此时调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
# 调用函数f时才真正计算求和的结果
print f()
# 上例中，lazy_sum中定义函数sum，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回函数中，称为“闭包（Closure）”
# 注意：当调用layz_sum时，每次调用都会返回一个新的函数，即使参数相同
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2 # f1()和f2()的调用结果互不影响

# 闭包

# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以闭包用起来简单，实现起来却不容易
# 返回的函数并没有立刻执行，而是调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3() # 输出9 9 9，而非1 4 9
# 因为返回的函数引用了变量i，但它并非立刻执行，等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 所以返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量，就只能再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count1():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count1()
print f1(), f2(), f3()
# 缺点是代码较长，可利用lambda函数缩短代码

# 匿名函数

# 当传入函数时，有时无需显式地定义函数，直接传入匿名函数更方便
print map(lambda x: x * x, [1,2,3,4,5,6,7,8,9])
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数没有名字，不必担心函数名冲突，此外，也可以把匿名函数赋值给一个变量
f = lambda x: x * x
print f
print f(5)
# 同样的也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
print build(1,2)()
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数

# 装饰器

# 由于函数是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print "2017-8-22"
f = now
f()
# 函数对象有个__name__属性，可以拿到函数的名字
print now.__name__
print f.__name__
# 如果需要在函数调用前后自动打印日志而不修改函数定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 以上decorator，接受一个函数作为参数，并返回一个函数
# 使用Python的@语法，把decorator置于函数的定义处
@log
def now():
    print '2017-08-23'
# 此时，调用now()函数，不仅会运行now()函数本身，还会打印一行日志
now()
# 将@log放在now()函数定义处，相当于执行了语句now = log(now)
# 由于log()是一个decorator，返回一个函数，所以原来的now()函数仍然存在
# 只是现在同名的now()变量指向了新的函数，于是调用now将执行新函数，即在log()函数中返回的wrapper()函数
# wrapper()函数的参数定义是(*args, **kw)，因此wrapper函数接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
# 如：要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2017-08-24'
now()
# 以上带参数的decorator相当于now = log('execute')(now)

# 经过decorator装饰后的函数，__name__发生了改变
print now.__name__
# 所以需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就可以完成

# 一个完整的decorator写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 或者针对带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
# 此时，函数名就不会发生改变了
@log('execute')
def now():
    print '2017-08-24'
now()
print now.__name__

# 在面向对象设计模式中，decorator被称为装饰模式，Python的decorator可以用函数实现也可以用类实现

def trace(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if len(text) > 0:
                log_text = text[0]
            else:
                log_text = 'call'
            print 'begin %s %s()' % (log_text, func.__name__)
            return_val = func(*args, **kw)
            print 'end %s %s()' % (log_text, func.__name__)
            return return_val
        return wrapper
    return decorator
@trace('execute')
def trace1():
    print 'TRACE1'
@trace()
def trace2():
    print 'TRACE2'
trace1()
trace2()

# 偏函数

# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
# 要注意这里的偏函数和数学意义上的偏函数不一样
print int('12345')
print int('12345', base=8)
print int('12345', 16)
# 若要转换大量的二进制字符串，每次都传int(x, base=2)很麻烦，可以定义一个int2函数
def int2(x, base=2):
    return int(x, base)
print int2
print int2('1000000')
print int2('1010101')
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自定义int2()
import functools
int2 = functools.partial(int, base=2)
print int2
print int2('1000000')
print int2('1010101')
# 所以functools.partial作用就是把一个函数的某些参数给固定住（即设置默认值），返回一个新的函数
# 注意int2函数，仅仅是把base参数重新设定默认值为2，但也可以在调用时传入其他值
print int2('1000000', base=10)

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 上例中的int2
print int2('10010')
# 相当于
kw = {'base':2}
print int('10010', **kw)

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是
print max2(5, 6, 7)
# 相当于
args = (10, 5, 6, 7)
print max(*args)

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，固定原函数的部分参数，从而简化调用

