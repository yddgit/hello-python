#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 协程，又称微线程，纤程。英文名Coroutine。
# 协程概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。

# 子程序，或者称为函数，在所有语言中都是层级调用，如A调用B，B在执行过程中又调用了C，
# C执行完毕返回，B执行完毕返回，最后A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。

# 而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# 注意：在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。如：
def A():
    print '1'
    print '2'
    print '3'
def B():
    print 'x'
    print 'y'
    print 'z'
# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：
'''
1
2
x
y
3
z
'''
# 但是在A中是没用调用B的，所以协程的调用比函数调用理解起来要难一些。
# 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行。

# 相比多线程，协程的优势：
# 1.极高的执行效率，因为子程序切换不是线程切换，由程序自身控制，没有线程切换的开销，和多线程相比，线程数量越多协程的性能优势就越明显
# 2.不需要多线程的锁机制，共享资源不加锁，只需要判断状态

# 协程利用多核CPU的方法是多进程+协程，即充分利用多核，又充分发挥协程的高效率。

# Python对协程的支持非常有限，用在generator中的yield可以一定程度上实现协程。

# 例子：

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。

import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print '[CONSUMER] Consuming %s...' % n
        time.sleep(1)
        r = '200 OK'

def producer(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print '[PRODUCER] Producing %s' % n
        r = c.send(n)
        print '[PRODUCER] Consumer return: %s' % r
    c.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)

# 注意到consumer函数是一个generator(生成器)，把一个consumer传入producer后：
# 1.首先调用c.next()启动生成器
# 2.然后一旦生产了东西，通过c.send(n)切换到consumer执行
# 3.consumer通过yield拿到消息，处理，又通过yield把结果传回
# 4.producer拿到consumer处理的结果，继续生产下一条消息
# 5.producer决定不生产了，通过c.close()关闭consumer，整个过程结束
# 整个过程无锁，由一个线程执行，producer和consumer协作完成，所以称为“协程”，而非线程的抢占式多任务

# Donald Knuth: 子程序就是协程的一种特例

