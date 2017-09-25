#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 常用内建模块

# collecitons是Python内建的一个集合模块，提供了许多有用的集合类

# namedtuple

# tuple可以表示不变集合，例如一个点的二维坐标可以表示成
p = (1, 2)
# 但是看到(1, 2)，很难看出这个tuple是用来表示一个坐标的，定义一个class又比较麻烦，这时namedtuple就派上了用场
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
# namedtuple是一个函数，用来创建一个自定义的tuple对象，规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# 这样，用namedtuple可以很方便的定义一种数据类型
print isinstance(p, Point)
print isinstance(p, tuple)
# 类似的，用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque

# list是线性存储的，数据量较大时，插入和删除效率很低，deque是为了实现高效插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q
q.pop()
print q
q.popleft()
print q

# defaultdict

# 使用dict时，如果引用的Key不存在，就会抛出KeyError，如果希望Key不存在时，返回一个默认值，可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] # key1存在
print dd['key2'] # key2不存在，返回默认值
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
# 除了Key不存在时返回默认值，defaultdict的其他行为和dict是完全一样的

# OrderedDict

# 使用dict时，Key是无序的，做迭代时无法确定Key的顺序，如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od # OrderedDict的Key是有序的
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od.keys() # 按照插入的Key的顺序返回
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.__capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.__capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
fifo = LastUpdatedOrderedDict(3)
fifo['A'] = 1
fifo['B'] = 2
fifo['C'] = 3
fifo['C'] = 4
fifo['D'] = 5
print fifo

# Counter

# Counter是一个简单的计数器，如统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c
# Counter实际上也是dict的一个子类


# base64

# Base64是一种用64个字符来表示任意二进制数据的方法

# Base64原理很简单，准备一个包含64个字符的数组：
# ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6bit
# 这样就得到4个数字作为索引，然后查表，获得相应的4个字符，就编码后的字符串
# 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后文本数据可以在邮件正文、网页等直接显示
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节，Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉

# Python内置base64可以直接进行base64的编解码
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
# 由于标准的Base64编码后可能出现字符+和/，URL中不能直接作为参数，所以又有一种urlsafe的base64编码，就是把+和/变成-和_
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')
# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过通常没有必要

# Base64不能用于加密，适用于小段内容的编码，如数字证书签名、Cookie的内容等
# 由于=字符也可能出现的Base64编码中，但=用在URL、Cookie里会造成歧义，所以，很多Base64编码会把=去掉
# 去掉=后，因为Base64是把3个字节变成4个字节，所以Base64编码的长度永远是4的倍数，因此加上=把Base64字符串的长度变为4的倍数，就可以正常解码了
print base64.b64decode('YWJjZA==')
#print base64.b64decode('YWJjZA')
def safe_b64decode(base64str):
    append_num = 4 - len(base64str) % 4
    temp64str = base64str
    if append_num > 0:
        for i in range(append_num):
            temp64str += '='
    return base64.b64decode(temp64str)
print safe_b64decode('YWJjZA')

# struct

# Python没有专门处理字节的数据类型，由于str即是字符串，又可以表示字节，所以字节数组=str
# Python提供了一个struct模块来解决str和其他二进制数据类型的转换
import struct
# struct的pack()函数把任意数据类型变成字符串
print struct.pack('>I', 10240099)
# pack的第一个参数是处理指令，'>I'表示：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。后面的参数个数要和处理指令一致
# unpack函数把str变成相应的数据类型
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# 根据>IH的说明，后面的str依次变为I（4字节无符号整数）和H（2字节无符号整数）

# Python虽然不适合编写操作字节流的代码，但在对性能要求不高的地方，用struct就方便多了
# struct模块定义的数据类型可以参考Python官方文档：
# https://docs.python.org/2/library/struct.html#format-characters

# Windows的位图文件（.bmp）是一种非常简单的文件格式，读入前30个字节来分析：
with open('test.bmp', 'r') as f:
    s = f.read(30)
    print struct.unpack('<ccIIIIIIHH', s)

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位置
# 一个4字节整数，表示位图大小
# 一个4字节整数，保留位，始终为0
# 一个4字节整数，实际图像的偏移量
# 一个4字节整数，Header的字节数
# 一个4字节整数，图像宽度
# 一个4字节整数，图像高度
# 一个2字节整数，始终为1
# 一个2字节整数，颜色数

# hashlib

# Python的hashlib提供了常见的摘要算法，如MD5、SHA1等等
# 摘要算法又称哈希算法、散列算法，是通过一个函数把任意长度的数据转换为一个长度固定的数据串
# 摘要算法是为了发现原始数据是否被人篡改过

import hashlib
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通过用32位的16进制字符串表示
# 计算一个字符串的MD5值
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()
# 如果数据量大，可以分块多次调用update()，计算结果一样
md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()

# SHA1调用与MD5类似，结果是160bit字节，通常用一个40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update('how to use md5 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()
# SHA256和SHA512比SHA1更安全，不过越安全的算法越慢，而且摘要长度更长

# 摘要算法的应用

# 用户口令的加密保存，即使运维人员能访问数据库，也无法获知用户的明文口令
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

# 验证用户登录，根据输入的口令返回True或False
db = {
    'michael': calc_md5('michael'),
    'bob': calc_md5('bob'),
    'alice': calc_md5('alice')
}
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password)
    input_pass = md5.hexdigest()
    user_pass = db[user]
    if input_pass == user_pass:
        return True
    else:
        return False
print login('michael', 'michael')
print login('michael', '123456')

# 由于常用口令的MD5很容易计算，所以要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，通过对原始口令加一个复杂字符串来实现，俗称“加盐”
def calc_md5_with_salt(password):
    return calc_md5(password + ' the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令

# itertools

# Python内建模块itertools提供了非常有用的用于操作迭代对象的函数

import itertools

# count()会创建一个无限的迭代器
natuals = itertools.count(1)
#for n in natuals:
#    print n

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
#for c in cs:
#    print c

# repeat()负责把一个元素无限重复下去，如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 5)
for n in ns:
    print n

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建一个迭代对象，并不会事先把无限个元素生成出来
# 无限序列通常会通过takewhile()等函数根据条件判断来截取出一个有限的序列
nutuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n

# itertools提供的几个迭代器操作函数更加有用

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print c

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回值相符，这两个元素就被认为是在一组的，而函数返回值作为组的key
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)

# imap()和map()的区别在于，imap()可以作用于无穷序列，并且两个序列长度不一致，以短的为准
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
# 注意：imap()返回一个迭代对象，而map()返回list。当调用map()时，已经计算完毕
print map(lambda x: x*x, [1, 2, 3])
# 而当调用imap()时，并没有进行任何计算
r = itertools.imap(lambda x: x*x, [1, 2, 3])
print r
# 必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素
for x in r:
    print x
# 这就说明imap()实现了“惰性计算”，类似imap()这样能够实现惰性计算的函数就可以处理无限序列

# ifilter()就是filter()的惰性实现

# XML

# 操作XML有两种方法：DOM和SAX
# DOM：把整个XML读入内存，解析为树，占用内存大，解析慢，优点是可以任意遍历树的节点
# SAX：流模式，边读边解析，占用内存小，解析快，缺点是要自己处理事件
# 通常情况下，优先考虑SAX，在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element、end_element、char_data，准备好这3个函数，就可以解析XML了

# 当SAX解析器读到一个节点时：<a href="/">python</a>
# 会产生3个事件：
# - start_element事件，在读取<a href="/">时
# - char_data事件，在读取python时
# - end_element事件，在读取</a>时

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print 'sax:start_element: %s, attrs: %s' % (name, str(attrs))
    def end_element(self, name):
        print 'sax:end_element: %s' % name
    def char_data(self, text):
        print 'sax:char_data: %s' % text
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
# 设置returns_unicode为True时返回的所有element名称和char_data都是unicode，方便国际化处理
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 注意：读取一大段字符串时，CharacterDataHandler可能被多次调用，所以要先保存起来在EndElementHandler里再合并

# 通常情况下生成XML都比较简单，可以直接拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some &amp; data') # L.append(encode('some & data'))
L.append(r'</root>')
print ''.join(L)
# 建议不要用XML，改成JSON

# HTMLParser

# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析
# Python提供了HTMLParser来方便地解析HTML

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print '<%s>' % tag
    def handle_endtag(self, tag):
        print '<%s>' % tag
    def handle_startendtag(self, tag, attrs):
        print '<%s/>' % tag
    def handle_data(self, data):
        print '%s' % data
    def handle_comment(self, data):
        print '<!-- %s -->' % data
    def handle_entityref(self, name):
        print '&%s;' % name
    def handle_charref(self, name):
        print '&#%s;' % name
parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去
# 特殊字符有两种，一种是英文表示的[&nbsp;]，一种是数字表示的[&#1234;]，这两种字符都可以通过Parser解析出来

# 如下，访问https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后解析HTML
# 输出Python官网发布的会议时间、名称和地点

import re

class PyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__re_title = re.compile(r'/events/python-events/\d+/')
        self.__found_title = False
        self.__event_info = []

    def handle_starttag(self, tag, attrs):
        attrdict = dict(attrs)
        if tag == 'a' and attrdict.has_key('href') and self.__re_title.match(attrdict['href']):
            self.__event_info.append('TITLE: ')
            self.__found_title = True
        if tag == 'time' and self.__found_title:
            self.__event_info.append('  TIME: ')
            self.__found_title = False
        if tag == 'span' and attrdict.has_key('class') and attrdict['class'] == 'event-location':
            self.__event_info.append('  LOCATION: ')

    def handle_endtag(self, tag):
        if len(self.__event_info) > 0:
            print ''.join(self.__event_info)
            self.__event_info = []

    def handle_data(self, data):
        if len(self.__event_info) > 0:
            self.__event_info.append(data.decode('utf-8'))

with open('python-events.html', 'r') as f:
    content = f.read()
    parser = PyHTMLParser()
    parser.feed(content)

