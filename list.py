#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置的数据类型list，是一种有序的集合，可以随时添加和删除元素
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
# len()函数可以获得list元素的个数
print len(classmates)
# 用索引来访问list中每一个位置元素，从0开始
print classmates[0], classmates[1], classmates[2] #, classmates[3]
# 当索引超出了范围时，Python会报IndexError错误
# 可以使用-1做索引直接获取最后一个元素，以此类推可获取倒数第2、3...个元素
# 当然，倒数索引如果越界，也会有IndexError的错误
print classmates[-1]
# list是一个可变的有序表，可以向list中追加元素到末尾
classmates.append("Adam")
print classmates
# 也可以把元素插入到指定位置
classmates.insert(1, 'Jack')
print classmates
# 要删除list末尾的元素，用pop()方法
print classmates.pop()
print classmates
# 要删除指定位置的元素，用pop(i)，i是索引位置
print classmates.pop(1)
print classmates
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print classmates
# list里的元素数据类型可以不同
L = ['Apple', 123, True]
print L
# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'schema']
print s
print len(s)
print s[2][1]
# 如果一个list中一个元素也没有，就是一个空的list，长度为0
L = []
print len(L)

