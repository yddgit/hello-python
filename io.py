#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了读写文件的函数，用法与C兼容

# 读文件open()函数

# 以只读方式打开文件
f = open('test.txt', 'r')
# 如果文件不存在会抛出IOError的错误
#file_not_found = open('notfound.txt', 'r')
# 打开成功，调用read()方法读取文件内容，Python把内容读到内存，用一个str对象表示
print f.read()
# 最后调用close()方法关闭文件
f.close()

# 由于读写时都可能产生IOError，为保证文件始终正确关闭，可以用try...finally
try:
    f = open('test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
# 为了方便，Python引入了with语句自动调用close()方法
with open('test.txt', 'r') as f:
    print f.read()
# 效果和try...finally一样，但代码更加简洁，不必调用f.close()方法

# 调用read()方法会一次性把文件全部内容读取到内存。
# 对于大文件，可以反复调用read(size)方法，每次最多读取size个字节内容。
# 调用readline()可以每次读取一行内容
# 调用readlines()可以一次读取所有内容并按行返回list

# 如果文件很小，read()一次性读取最方便，如果不能确定文件大小，反复调用read(size)，如果是配置文件，调用readlines()最方便
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print line.strip() # 把末尾的\n去掉

# 类似open函数这样返回有read()方法的对象，在Python中称为file-like Object
# 除了file外，还可以是内存的字节流、网络流、自定义流等。file-like Object不需要从特定类继承，只要写个read()方法就行
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲

# 二进制文件

# 如果要打开二进制文件，如图片、视频等，用'rb'模式打开
with open('test.jpg', 'rb') as f:
    print f.read(20)

# 字符编码

# 要读取非ASCII编码的文本文件，必须以二进制模式打开，再解码
with open('test-gbk.txt', 'rb') as f:
    print f.read().decode('gbk')
# Python还提供了一个codecs模块在读文件时自动转换编码，直接读取unicode
import codecs
with codecs.open('test-gbk.txt', 'r', 'gbk') as f:
    print f.read()

# 写文件时，open函数传入'w'或'wb'表示写文本文件或写二进制文件
with open('test.txt', 'w') as f:
    f.write('Hello World!')
with codecs.open('test-gbk.txt', 'w', 'gbk') as f:
    f.write(u'测试完成')

# 操作文件和目录

import os
print os.name # 操作系统名字
#print os.uname() # 详细系统信息（Windows上不提供）
print os.environ # 环境变量保存在dict中
print os.getenv('TMP') # 获取环境变量

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

# 查看当前目录的绝对路径
print os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print os.path.join('C:\\tmp', 'testdir')
# 然后创建目录
os.mkdir(os.path.join('C:\\tmp', 'testdir'))
# 删除一个目录
os.rmdir('C:\\tmp\\testdir')
# 把两个路径合在一起时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 同样拆分路径时，不要直接拆字符串，而要通过os.path.split()函数，这可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.split('C:\\tmp\\testdir')
# os.path.splitext()可以直接得到文件扩展名
print os.path.splitext('C:\\tmp\\testdir\\file.txt')
# 这些合并、拆分路径的函数并不要求目录和文件真实存在，只是对字符串进行操作
# 对文件重命名
#os.rename('test.txt', 'test.bak')
# 删除文件
#os.remove('test.bak')

# os模块中没有复制文件的函数，可以通过读写函数实现复制
# shutil模块提供了copyfile()函数，同时也提供了很多实用函数，可以看做是os模块的补充

# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# 查找当前目录及其子目录下包含指定字符串的文件，并打印出文件路径
def search(s, path):
    files = os.listdir(path)
    for f in files:
        fap = os.path.abspath(f)
        if os.path.isdir(f):
            search(s, fap)
        elif os.path.isfile(f) and s in os.path.split(fap)[1]:
            print fap
search('test', '.')

# 序列化，把变量从内存中变成可存储或传输的过程称之为序列化

# 在Python中叫pickling，也称之为serialization、marshalling、flattening等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# Python提供两个模块来实现序列化：cPickle和pickle。
# 这两个模块功能相同，区别是cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
try:
    import cPickle as pickle
except ImportError:
    import pickle

# 把一个对象序列化并写入文件
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个str，然后就可以把这个str写入文件
print pickle.dumps(d)
# 也可以用pickle.dump()直接把对象序列化后写入一个file-like Object
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

# 把反序列化内容读到一个str，然后用pickle.loads()方法反序列化出对象
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
with open('dump.txt', 'rb') as f:
    print pickle.load(f)
# 当然这个反序列化的变量和原来的变量完全不相干，只是内容相同而已

# Pickle序列化的数据只能用于Python，并且可能不同版本的Python彼此都不兼容

# JSON

# JSON类型 --> Python类型
# {} --> dict
# [] --> list
# "string" --> 'str'或u'unicode'
# 1234.56 --> int或float
# true/false --> True/False
# null --> None

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name='Jack', age=21, score=89)

# dumps()方法返回一个str，dump()方法可以直接把JSON写入一个file-like Object
print json.dumps(d)
with open('json.txt', 'w') as f:
    json.dump(d, f)
# 将JSON反序列化为Python对象，用loads()或者load()方法
json_str = '{"age": 21, "score": 89, "name": "Jack"}'
print json.loads(json_str)
with open('json.txt', 'r') as f:
    print json.load(f)
# 反序列化得到的所有字符串对象默认都是unicode而不是str

# class对象和JSON之间的互相转换
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Adam', 25, 98)
# json.dumps()方法的参数列表，除了第一个必须的obj参数，还提供一些可选参数来定制JSON序列化
# https://docs.python.org/2/library/json.html#json.dumps
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，只需要为要转换的对象编写一个转换函数
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
# 这样Student实例首先被student2dict()函数转换成dict，然后再序列为JSON
print json.dumps(s, default=student2dict)
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，如定义了__slots__的class
print json.dumps(s, default=lambda obj: obj.__dict__)
# 同样，如果要反序列化，json.loads()方法首先转换出一个dict对象，然后传入object_hook函数负责把dict转换为对应的class实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 25, "score": 98, "name": "Adam"}'
print json.loads(json_str, object_hook=dict2student)

