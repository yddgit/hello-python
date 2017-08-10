#!/usr/bin/env python
# -*- coding: utf-8 -*-

# if语句
# 根据Python的缩进规则，如果if语句判断是True，就执行缩进的两行print语句
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
# if-else语句（注意不要少写:）
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'
# if-elif-else语句
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
# if判断条件可以简写，只要表达式是非零数值、非空字符串、非空list等就判断为True，否则为False
if 1:
    print 'True'

# for...in循环，依赖把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
sum = 0
# 计算1-10的整数之和
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print sum
# 计算1-100的整数之和，可使用range(x)函数生成一个从0开始小于x的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print sum

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# 根据输入的年份进行判断
birth = raw_input('birth: ')
if(birth < 2000):
    print u'00前'
else:
    print u'00后'
# 以上代码输入1989却输出：00后，这显然是不对的
# raw_input读取的内容永远以字符串形式返回，必须先用int()把字符串转换为整型
birth = int(raw_input('birth: '))
print 'birth < 2000:', birth < 2000

