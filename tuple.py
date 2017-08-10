#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tuple元组是一种有序列表，与list类似，但tuple一旦初始化就不能修改
# 如下，classmates这个tuple是不能变的，也没有append()、insert()这样的方法
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
print classmates[0]
print classmates[-1]
# 因为tuple不可变，所以代码更安全，如果可能，能用tuple替代list就尽量用tuple
# tuple的陷阱：当定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print t
# 定义一个空的tuple
t = ()
print t
# 定义一个只有1个元素的tuple，不能写成()，这会产生歧义
t = (1,)
print t
# 一个“可变”的tuple，tuple所谓的不变是指每个元素指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t

# list和tuple是Python内置的有序集合，一个可变，一个不可变，可根据需要来选择使用它们

