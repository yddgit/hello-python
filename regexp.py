#!/usr/bin/env python
# -*- coding: utf-8 -*-

# \d匹配一个数字，'00\d'可以匹配'007'，但无法匹配'00A'
# \w匹配一个字母或数字，'\w\w\d'可以匹配'py3'
# \s可以匹配一个空白字符
# .可以匹配任意字符
# *表示任意个字符，+表示至少一个字符，?表示0个或1个字符
# {n}表示n个字符，{n,m}表示n-m个字符
# \d{3}\-\d{3,8}匹配带区号的电话号码，由于'-'是特殊字符，正则表达式中要用'\-'转义

# []表示范围：
#   [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
#   [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或下划线组成的字符串
#   [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或下划线组成的字符串，也就是Python的合法变量
#   [a-zA-Z\_][0-9a-zA-Z\_]{0,19}更精确的限制了变量的长度是1-20个字符
# A|B可以匹配A或B，(P|p)ython可以匹配'Python'或'python'
# ^表示行的开头，^\d表示必须以数字开头
# $表示行的结束，\d$表示必须以数字结束

# Python提供re模块，包含所有正则表达式的功能
# 由于Python的字符串本身也用\转义，所以要特别注意
s = 'ABC\\-001' # 对应的正则表达式字符串变成：'ABC\-001'
# 因此强烈建议使用Python的r前缀，就不用考虑转义的问题了
s = r'ABC\-001' # 对应的正则表达式字符串不变：'ABC\-001'

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# 常见的判断方法
if m:
    print 'ok'
else:
    print 'failed'

# 切分字符串

# 字符串的split方法，无法识别连续的空格
print 'a b   c'.split(' ')
# 正则表达式分割更方便
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

# 分组

# 正则表达式除匹配外，还可以提取子串，用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
print m.group(0) # group(0)永远是原始字符串
print m.group(1) # group(1)表示第1个子串
print m.group(2) # group(2)表示第2个子串，以此类推

#提取时间字符串中的时分秒
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', '19:05:30')
print m.groups()

# 贪婪匹配，正则表达式默认是贪婪匹配，也就是匹配尽可能多的字符
# 如下：匹配出数字后面的0，由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加?即可
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 编译

# 当使用正则表达式时，re模块需要处理：
# 1. 编译正则表达式，正则表达式本身不合法，会报错
# 2. 用编译后的正则表达式去匹配字符串
# 如果一个正则表达式要重复使用，出于效率的考虑，可以预编译，接下来重复使用时就不用再编译了，直接匹配
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 编译后生成了Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应方法时不用给出正则字符串
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()

# 验证email
import re
re_email = re.compile(r'(\<\w+(\s+\w+)*\>\s+)*(\w+(\.\w+)*)@(\w+(\.\w+)+)')
print re_email.match('someone@gmail.com').groups()
print re_email.match('bill.gates@microsoft.com').groups()
print re_email.match('<Tom Paris> tom@voyager.org').groups()

