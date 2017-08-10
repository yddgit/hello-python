#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第一行注释是告诉Linux/OSX系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会乱码
# 除了要加上# -*- coding: utf-8 -*-外，中文字符串必须是Unicode字符串：u'中文字符串'

print "A to ASCII:", ord('A')
print "66 to ASCII Char:", chr(66)
print u"这是中文，"u'没有乱码'
print u'中'u'\u4e2d' # \u后面是十六进制的Unicode码

# 字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码
# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
# 把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法
print u'ABC'.encode('utf-8') # 'ABC'
print u'中文'.encode('utf-8') # '\xe4\xb8\xad\xe6\x96\x87'
print 'abc'.decode('utf-8') # u'abc'
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # u'\u4e2d\u6587'

# 英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同）
# 而中文字符转换后1个Unicode字符将变为3个UTF-8字符，你看到的\xe4就是其中一个
# 字节，因为它的值是228，没有对应的字母可以显示，所以以十六进制显示字节的数值。

# len()函数可以返回字符串的长度
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

# 确保.py源文件是以UTF-8无BOM格式保存的，且其中的中文字符串必须是Unicode字符串

# 字符串的格式化输出
# %运算符是用来格式化字符串的
#   %s 字符串
#   %d 整数
#   %f 浮点数
#   %x 十六进制整数
# 有几个%点位符，后面就跟几个变量或者值，顺序要对应好，如果只有一个%，括号可以省略
print 'Hello %s' %'World'
print 'Hi, %s, you have $%d.' %('Michael', 1000000)
# %d %f 可指定是否补0和整数与小数位数
print '%2d-%02d' % (3,1)
print '%.2f' % 3.1415926
# 如果不确定数据类型，则可使用%s，它会把任何数据类型转换为字符串
print 'Age: %s. Gender: %s' % (25, True)
# 对于Unicode字符串，用法完全一样，但最好确保替换的字符串也是Unicode字符串
print u'Hi, %s' % u'Michael'
# 用%%来转义，表示一个%
print 'Growth rate: %d%%' % 7

# 由于历史遗留问题，但在语法上需要'xxx'和u'xxx'两种字符串表示方式
# Python也支持其他编码方式，比如Unicode编码成GB2312
print u'中文'.encode('gb2312')

# 在Python3.x中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样
# 而以字节形式表示的字符串则必须加上b前缀b'xxx'
# 格式化字符串时，可使用Python的交互式命令行测试

