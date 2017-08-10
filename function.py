#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置很多有用的函数，可以直接调用
# 内置函数参考：https://docs.python.org/2/library/functions.html
# 可以在交互式命令行通过help(function_name)查看function_name函数的帮助信息

# abs求绝对值
print abs(100)
print abs(-20)
print abs(12.34)
# 调用函数时如果传入的参数数量不对，会报TypeError的错误，并明确提示参数个数不正确
#abs(1, 2)
# 如果参数数量是对的，但参数类型不对，则会提示参数类型错误
#abs('a')

# 比较函数cmp(x, y)，如果x<y返回-1，如果x==y返回0，如果x>y，返回1
print cmp(1, 2)
print cmp(2, 1)
print cmp(3, 3)

# 数据类型转换函数，如int()将其他数据类型转换为整数
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给函数起了一个别名
a = abs # 变量a指向abs函数
print a(-1) # 所以也可以通过a调用abs函数

# 定义函数
# Python中，定义函数使用def语句，然后在缩进块中编写函数体，函数返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# 调用函数
print my_abs(-45)
# 函数体内部在语句执行时，执行到return时，函数就执行完毕，并将结果返回
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可以简写为return

# 空函数，如果想定义一个什么事也不做的空函数，可以用pass语句
def pop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，如暂未确定函数逻辑可先写pass让代码能运行起来
age = 19
if age >= 18:
    pass

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查，并抛出TypeError
#print my_abs(1, 2)
# 但是如果参数类型不对，Python解释器无法检查，如下：当传入了不恰当的参数时，内置函数abs会检查参数错误，但my_abs没有参数检查
#print my_abs('A')
#print abs('A')

# 给my_abs添加参数检查，只允许整数和浮点数类型的参数，数据类型检查可以用内置函数isinstance实现
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print my_abs1('A')

# 返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
# 其实Python函数返回的仍然是单一值，tuple类型
# 但在语法上，返回tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
r = move(100, 100, 60, math.pi / 6)
print r

# 函数小结：
# 1.定义函数时，需要确定函数名和参数个数
# 2.如果必要，可以先对参数的数据类型做检查
# 3.函数体内部可以用return随时返回函数结果
# 4.函数执行完毕也没有return语句时，自动return None
# 5.函数可以同时返回多个值，但其实就是一个tuple

# Python函数可以使用默认参数、可变参数和关键字参数，简化调用代码

# 默认参数
# 计算X^n，由于经常计算X^2，所以第二个参数默认为2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5) # 相当于power(5, 2)
print power(5, 3)
# 必选参数在前，默认参数在后，否则Python的解释器会报错
# 设置默认参数时，把变化大的参数放前面，变化小的参数放后面
# 使用默认参数最大的好处是能降低调用函数和难度
def enroll(name, gender, age=6, city='Beijing'):
    print '--------------'
    print 'name =', name
    print 'gender =', gender
    print 'age =', age
    print 'city =', city
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
# 有多个默认参数时，调用时即可以按顺序提供默认参数
# 也可以不按顺序提供部分默认参数，不按顺序提供部分默认参数时需要把参数名写上

# 默认参数使用时也会存在问题，如下
def add_end(L = []):
    L.append('END')
    return L
print add_end([1, 2, 3]) # [1, 2, 3, 'END']
print add_end(['x', 'y', 'z']) # ['x', 'y', 'z', 'END']
print add_end() # ['END']
print add_end() # ['END', 'END']
print add_end() # ['END', 'END', 'END']
# Python函数在定义的时候，默认参数L就计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所以，默认参数必须指向不变对象！！
# 上例可以用None这个不变对象来实现
def add_end1(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
# 此时无论调用多少次，都不会有问题
print add_end1()
print add_end1()

# 可变参数，即传入的参数个数是可变的
# 如：计算a^2 + b^2 + c^2 + ...
# 参数前面加一个*号，在函数内部，参数numbers接收到的是一个tuple
# 调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc(1, 2)
print calc(1, 2, 3)
print calc(1, 3, 5, 7)
print calc()
# 如果已经有一个list或tuple，则可以在变量前加*号，把list或tuple的元素变成可变参数传给函数
nums = [1, 2, 3]
print calc(*nums)

# 关键字参数，传入0个或任意个包含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other', kw
# 函数person除了必选参数name和age外，还接受关键字参数kw，在调用该函数时，可以只传入必选参数
person('Michael', 30)
# 也可以传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 关键字参数可以扩展函数功能，如果已经有一个dict，也可以在变量前加**号直接传递给函数
kw = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, **kw)

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中几种
# 但必须保证参数顺序：必选参数、默认参数、可变参数、关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
func(1, 2, 3, 4, 5, x='a', y='b', z='c')
# 最神奇的是通过一个tuple和dict，也可以调用该函数
args = (1, 2, 3, 4)
kw = {'x':99}
func(*args, **kw)
# 所以，对于任意函数，都可通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

# 函数参数小结：
# 1.默认参数必须是不可变对象
# 2.可变参数*args，args接收的是一个tuple
# 3.关键字参数**kw，kw接收的是一个dict
# 4.可变参数既可以直接传入func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入func(*(1, 2, 3))
# 5.关键字参数既可以直接传入func(a=1, b=2)，又可以先组装dict，再通过**kw传入func(**{'a':1,'b':2})
# 6.使用*args和**kw是Python的习惯写法

