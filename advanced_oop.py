#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向对象高级特性：多重继承、定制类和元类

# 使用__slots__

# 正常情况下，定义并创建一个class的实例后，可以给该实例绑定任何属性和方法，这是动态语言的灵活性
class Student(object):
    pass
s = Student()

# 给实例绑定一个属性
s.name = 'Michael'
print s.name

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25) # 调用实例方法
print s.age # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
#s2.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)
# 给class绑定方法后，所有实例均可调用
s.set_score(100)
s2.set_score(99)
print s.score
print s2.score

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行过程中动态给class加上功能

# 但是，如果要限制class的属性，如，只允许对Student实例添加name和age属性，
# 就需要在定义class的时候，定义一个特殊的__slots__变量，来限制class能添加的属性

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s = Student()
s.name = 'Michael'
s.age = 25
#s.score = 99
# 上面由于score没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class CollegeStudent(Student):
    __slots__ = ('score')
c = CollegeStudent()
c.name = "Lucy"
c.age = 30
c.score = 89
#c.gender = 'Male'

# 使用@property

# 在绑定属性时，如果直接把属性暴露出去，虽然简单，但无法检查参数，导致数据可以随便改
cs = CollegeStudent()
cs.score = 9999
# 这显示不合逻辑，为了限制score的范围，通过set_score()方法来设置score属性，再通过get_score()来获取score属性
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
s = Student()
s.set_score(60)
print s.get_score()
#s.set_score(9999)

# 但是上面的调用方法略显复杂，没有直接调用属性那么简单，此时可以使用装饰器（decorator）
# Python内置@property装饰器就负责把一个方法成属性调用
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
# 于是我们就拥有一个可控的属性操作
s = Student()
s.score = 60
print s.score
#s.score = 9999

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2017 - self._birth
# 上面的birth属性可读可写，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
s = Student()
s.birth = 1989
print s.age
#s.age = 29

# 多重继承

# 动物
class Animal(object):
    pass
# 大类：Mammal和Bird
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
# 现在要给动物们加上Runnable和Flyable的功能
class Runnable(object):
    def run(self):
        print 'Running...'
class Flyable(object):
    def fly(self):
        print 'Flying...'
# 对于需要Runnable功能的动物，就多继承一个Runnable，如
class Dog(Mammal, Runnable):
    pass
# 对于需要Flyable功能的动物，就多继承一个FLyable，如
class Bat(Mammal, Flyable):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能

# Mixin

# 在设计类的继承关系时，通常主线都是单一继承下来的，如果需要“混入”额外功能，通过多继承就可以实现，这种设计通常称之为Mixin
# 为了更好的看出继承关系，我们可以把上例中的Runnable和Flyable改名为RunnableMixin和FlyableMixin。
# 类似的，还可以定义出肉食动物CarnivorousMixin和草食动物HerbivorousMixin，让某个动物拥有好几个Mixin
class RunnableMixin(object):
    def run(self):
        print 'Running...'
class FlyableMixin(object):
    def fly(self):
        print 'Flying...'
class CarnivorousMixin(object):
    def eat(self):
        print 'Eating meat...'
class HerbivorousMixin(object):
    def eat(self):
        print 'Eating grass...'
class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass

# Mixin的目的就是给一个类增加多个功能，这样，在设计类时，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂继承关系
# Python自带的很多库也使用了Mixin
# 如TCPServer和UDPServer这两类网络服务，要同时服务多个用户就必须使用多进程或多线程模型，这两种模块由ForkingMixin和ThreadingMixin提供。
# 通过组合，我们就可以创造出合适的服务来

from SocketServer import TCPServer,ForkingMixIn,UDPServer,ThreadingMixIn
# 比如，编写一个多进程模式的TCP服务，定义如下
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 编写一个多线程模式的UDP服务，定义如下
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 如果要搞一个更先进的协程模型，可以编写一个CoroutineMixin
#class MyTCPServer(TCPServer, CoroutineMixIn):
#    pass
# 这样一来，不需要复杂而庞大的继承链，只要选择组合不同类的功能就可以快速构造出所需要的子类

# 定制类

# 类似__slots__这种形如__xxx__的变量或者函数名在Python中是有特殊用途的
# __slots__限制class的属性
# __len__()使class作用于len()函数

# __str__指定打印对象时输出的内容

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
s = Student('Michael')
print s
# 如果不用print，直接敲变量，打印出来的对象依然不是__str__()方法的返回值
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是
# __str__()返回用户看到的字符串
# __repr__()返回程序开发者看到的字符串，即__repr__()是为调试服务用的
# 解决办法是再定义一个__repr__()方法，但通过两者代码都一样，可以写作
# __repr__ = __str__

# __iter__实现可循环对象，实现__iter__()方法，该方法返回一个迭代对象，
# Python的for循环就会不断调用该迭代对象的next()方法拿到下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration
        return self.a
for n in Fib():
    print n

# __getitem__如果要对象表现的像list一样可以按照下标取出元素，需要实现__getitem__()方法

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print f[0]
print f[1]
print f[8]

# list还有切片方法，对于__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print f[0:5]
print f[:10]

# 但是没有对step参数作处理，也没有对负数作处理，所以要正确实现一个__getitem__()还有很多工作要做
# 此处，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，如str

# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值，最后还有一个__delitem__()方法用于删除某个元素

# 通过上面的方法，可将自定义类表现得和Python的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口

# __getattr__

# 当调用类的方法或属性时，如果不存在，就会报错。要避免这个错误，除了加上一个score属性外，还可以实现__getattr__()方法动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
# 当调用的属性不存在时，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性score
s = Student()
print s.name
print s.score
# 返回函数也是完全可以的
class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
# 调用方式也要变为
s = Student()
print s.age()
print s.abc
# 注意：只有在没有找到属性的情况下，才调用__getattr__，已有的属性不会在__getattr__中查找
# 另外，以上示例中任意调用如s.abc都会返回None，这是因为定义的__getattr__默认返回None，
# 要让class只响应特定的几个属性，需要按照约定，抛出AttributeError错误
class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError("'Student' object has no attribute '%s'" % attr)
s = Student()
print s.age()
#print s.abc

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理，这种特性的使用场景一般是：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 对于类似这种REST API，如果要写SDK，每个URL都写一个方法，很麻烦，而且API一旦改动，SDK也得改
# 利用完全动态的__getattr__，可以写出一个链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
print Chain().status.user.timeline.list
# 这样无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且不随API的增加而改变
# 还有些REST API会把参数放到URL中，如
# GET /users/:user/repos
# 调用时需要把:user替换为实际用户名，如果能写出这样的链式调用
# Chain().users('michael').repos
# 就可以非常方便的调用API了

# __call__

# 一个对象的方法可以通过instance.method()来调用，如果定义一个__call__()方法，就可以通过实例本身直接调用此方法instance()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print ('My name is %s' % self.name)
s = Student("Michael")
s()

# __call__()方法还可以定义参数，对实例进行直接调用就好比对一个函数调用一样。
# 即把对象看作函数，把函数看作对象，这两者本身也没有区别。
# 如果要判断一个变量是对象还函数，需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数可以判断一个对象是否是“可调用”对象
print callable(Student('Sam'))
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')

# 更多可定制方法参考Python的官方文档
# http://docs.python.org/2/reference/datamodel.html#special-method-names

