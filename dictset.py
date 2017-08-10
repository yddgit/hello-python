#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dict相当于java中的map，使用key-value存储
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print d['Michael']
# 直接通过key给dict新增元素
d['Adam'] = 67
print d['Adam']
# 使用相同的key赋值会覆盖之前的值
d['Jack'] = 90
print d['Jack']
d['Jack'] = 88
print d['Jack']
# 如果key不存在，dict会报错
#print d['Thomas']
# 可通过in判断key是否存在
print 'Thomas' in d
# dict提供get方法，如果key不存在，可以返回None或自己指定的value
print d.get('Thomas')
print d.get('Thomas', -1)
# pop(key)删除指定的key-value对
print d.pop('Bob')
print d
# dict内部存放的顺序和key存入的顺序没有关联
# dict相比list查找和插入速度更快，但需要占用大量内存，所以dict是用空间来换取时间的一种方法
# dict的key必须是不可变对象
#key = [1, 2, 3]
#d[key] = 'a list'

# set是一个没有重复元素的集合，要创建一个set需要提供一个list作为输入集合
s = set([1, 2, 3])
print s
# 上面代码输出set([1, 2, 3])只是说set内部有1,2,3这3个元素，显示的[]不表示这是一个list
# 重复元素在set中自动被过滤
s = set([1,1,2,2,3,3])
print s
# 通过add(key)方法添加元素到set中
s.add(4)
print s
s.add(4)
print s
# 通过remove(key)方法可以删除元素
s.remove(4)
print s
# set可以做数学意义上的交集、并集操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2
# set的元素必须是不可变对象

# string是不可变对账，list是可变对象，对list操作，其内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print a
# 而对于不可变对象，虽然字符串调用了replace()方法，但变量a的值并没有变
a = 'abc'
print a.replace('a', 'A')
print a
# 所以，不可变对象调用对象自身的任意方法，都不会改变该对象自身的内容，而会创建新的对象并返回

# tuple虽然是不可变对象，但是如果其元素中有list，在dict或set中使用时也会报错
t = (1,2,3)
#t = (1, [2, 3])
d = {t:'a tuple'}
print d
s = set([t])
print s

