#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向对象编程 Object Oriented Programming

# 面向过程的程序设计把计算机程序视为一系列命令集合，即一组函数的顺序执行。为了简化程序设计，
# 面向过程把函数继续切分为子函数，即把大块函数切割成小块函数来降低系统的复杂度。

# 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，
# 并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递

# Python中，所以有数据类型都可以视为对象。自定义的对象就是类（Class）的概念

# 假设要处理学生的成绩表
std1 = {'name':'Michael', 'score':98}
std2 = {'name':'Bob', 'score':81}

# 可以通过函数实现，如打印成绩
def print_score(std):
    print '%s: %s' % (std['name'], std['score'])
print_score(std1)

# 如果采用OOP思想，打印成绩时首先必须创建出这个学生对应的对象，然后给对象发一个print_score消息，让对象自己把数据打印出来
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print '%s: %s' % (self.name, self.score)
# 给对象发消息实际上就是调用对应的函数，称为对象的方法（Method）
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 面向对象的抽象程序比函数要高，因为一个Class既包含数据，又包含操作数据的方法

# 面向对象的三大特点：数据封装、继承和多态

# Python中定义类通过class关键字，后面紧接类名，类名通常大写开头，紧接着是(object)，表示该类是从哪个类继承下来的，通过，如果没有合适的父类，就使用object类，这是所有类的父类
class Book(object):
    pass

# 创建实例是通过类名+()实现
book = Book()
print book # 变量book是指向的是一个Book的object
print Book # Book本身则是一个类

# 可以自由地给一个实例变量绑定属性
book.name = "Jerry's Home"
print book.name

# 由于类可以起到模板的作用，因此，可以创建实例的时候把一些必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例时把属性绑定上去
# __init__方法的第一个参数永远是self，表示创建的实例本身，因此在__init__方法内部就可以把属性绑定到self
class Car(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
# 有了__init__方法，在创建实例的时候就不能传入空参数了，必须传入与__init__方法匹配的参数，但不需要传self，Python解释器自已会把实例变量传进去
myCar = Car('Honda', 100000)
print myCar.name, myCar.price

# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且调用时不用传递该参数

# 数据封装，在类内部定义访问数据的函数，通过访问这些函数来操作实例数据。
# 定义的方法除了第一个参数是self外，其他和普通函数一样，调用时除了self不用传递，其他参数正常传入

# Python与静态语言不同，它允许对实例变量绑定任何数据，即对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
tom = Student('Tom', 59)
jack = Student('Jack', 87)
tom.age = 8
print tom.age
#print jack.age

# 访问限制

# 在Class内部，可以有属性和方法，外部代码通过调用方法来操作数据，隐藏内部逻辑，但从前面的Student类的定义来看，外部代码还是可以自由修改name、score属性
bart = Student('Bart Simpson', 98)
print bart.score
bart.score = 59
print bart.score

# 如果要让内部属性不被外部访问，可以在属性名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问，外部不能访问
class People(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_age(self):
        print '%s: %s' % (self.__name, self.__age)
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0 and age < 200:
            self.__age = age
        else:
            raise ValueError('bad age')
# 此时已经无法从外部访问实例变量__name和__age了
girl = People('Marry', 18)
#print girl.__name
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护使代码更加健壮
# 如果要获取name和age可以增加相应的get_name和get_age方法
print girl.get_name(), girl.get_age()
# 如果要允许修改age，可以增加set_age方法，并在此方法中对参数做检查，避免传入无效参数
girl.set_age(19)
print girl.get_age()

# 注意：变量名类似__xxx__的，也是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 是可以直接访问的，不是private变量，所以不能用__name__、__score__这样的变量名

# 有时会看到以一个下划线开头的实例变量名，如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，这种变量虽然可以访问，但请视作私有变量，不要随意访问

# 双下划线开头的实例变量也不一定不能从外部访问，不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
# 所以，仍然可以通过_People__name来访问__name变量
print girl._People__name

# 强烈建议不要这么写，因为不同版本Python解释器可能会把__name改成不同的变量名
# 总之Python本身没有任何机制阻止访问数据，一切全靠自觉

# 继承和多态

class Animal(object):
    def run(self):
        print "Animal is running..."
class Dog(Animal):
    pass
class Cat(Animal):
    pass
print Dog
print Cat

# 对于Dog，Animal是它的父类，对于Animal，Dog是它的子类
# Dog、Cat自动拥有了父类的run()方法
dog = Dog()
dog.run()
cat = Cat()
cat.run()
# 子类也可以增加一些方法
class Tiger(Animal):
    def run(self):
        print 'Tiger is running'
    def eat(self):
        print 'Eating meat...'
tiger = Tiger()
tiger.run()
tiger.eat()
# 子类也可以覆盖父类方法，在代码运行的时候，总会调用子类的方法，这就是：多态
class Lion(Animal):
    def run(self):
        print 'Lion is running...'
lion = Lion()
lion.run()
print isinstance(lion, Animal)
print isinstance(lion, Lion)

# 多态的好处
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Tiger())
run_twice(Lion())
# 如果再定义一个Tortoise类型，run_twice()也不用做任何改动
class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'
run_twice(Tortoise())
# 多态即可能实现：
# 对扩展开放：允许新增Animal子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice()函数

# 继承可以一级一级继承下去，而任何类，最终都可以追溯到根类object
# 旧的方式定义Python类允许不从object继承，但这种方式已不推荐使用。任何时候，没有合适的父类时，则继承object类

# 获取对象信息

# 使用type()函数判断对象类型
print type(123)
print type('str')
print type(None)
# 也可以判断函数或者类
print type(abs)
print type(lion)
# type()函数返回type类型，如果在if语句中判断，就需要判断两个变量的type类型是否相同
print type(123) == type(456)
print type('abc') == type('123')
print type('abc') == type(123)
# Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入
import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(int) == type(str) == types.TypeType

# 使用isinstance()
# 要判断class的类型，可以使用isinstance()函数，如果继承关系是：object -> Animal -> Dog
# 那么isinstance()就可以告诉我们一个对象是否是某种类型
a = Animal()
d = Dog()
print isinstance(d, Dog)
print isinstance(d, Animal)
print isinstance(a, Dog)
# d虽然是Dog类型的，但由于Dog是从Animal继承下来的，所以d也是Animal类型
# 因此，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

# isinstance()也可以判断基本类型
print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance('a', unicode)

# 还可以判断一个变量是否是某些类型中的一种
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
# 由于str和unicode都是从basestring继承下来的，所以，以上代码可以简化为
print isinstance(u'a', basestring)

# 使用dir()

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，如，获得一个str对象的所有属性和方法
print dir('ABC')
# 类型__xxx__的属性和方法在Python中都是有特殊用途的，如__len__方法返回长度，在调用len()函数时，实际上会自动去调用对象的__len__()方法
# 下面的代码是等价的：
print len('ABC')
print 'ABC'.__len__()

# 对于自定义的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyObject(object):
    def __len__(self):
        return 100
obj = MyObject()
print len(obj)
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x') # 有属性'x'吗？
print obj.x
print hasattr(obj, 'y') # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print hasattr(obj, 'y') # 有属性'y'吗？
print getattr(obj, 'y') # 获取属性'y'
print obj.y # 获取属性'y'
# 如果试图获取不存在的属性，会抛出AttributeError的错误
#getattr(obj, 'z') # 获取属性'z'
# 可以传入一个default参数，如果属性不存在，就返回默认值
print getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 也可以获得对象的方法
print hasattr(obj, 'power') # 有属性'power'吗？
print getattr(obj, 'power') # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print fn
print fn()

# 通过内置的一系列函数，可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 只有在不知道对象信息时，我们才需要去获取对象信息，如果可以直接写obj.x，就不要写getattr(obj, 'x')
# 正确示例：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
# 假设要从文件流fp中读取图像，首先要判断该fp对象是否存在read()方法。
# 如果存在，则该对象是一个流，如果不存在，则无法读取。这时就可以使用hasattr()方法了

