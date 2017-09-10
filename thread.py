#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现多任务的三种方式：
# 1.多进程模式：启动多个进程，每个进程只有一个线程，但多个进程可以一块执行多个任务
# 2.多线程模式：启动一个进程，一个进程启动多个线程，多个线程也可以一块执行多个任务
# 3.多进程+多线程模式：启动多个进程，每个进程再启动多个线程，同时执行的任务就更多了，但这种模型更复杂，实际很少采用

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊，普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次。
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

# Python的os模块封装了常见的系统调用，其中就包括fork，在Python程序中轻松创建子进程

#import os
#print 'Process (%s) start...' % os.getpid()
#pid = os.fork()
#if pid == 0:
#    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
#else:
#    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# 由于Windows没有fork调用，上面的代码在Windows上无法运行
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务。
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求

# multiprocessing模块是跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来处理一个进程对象
# 如下，启动一个子进程并等待其结束

#from multiprocessing import Process
#import os
#def run_proc(name):
#    print 'Run child process %s (%s)...' % (name, os.getpid())
#if __name__ == '__main__':
#    print 'Parent process %s.' % os.getpid()
#    p = Process(target=run_proc, args=('test',))
#    print 'Process will start.'
#    p.start()
#    p.join()
#    print 'Process end.'

# 以上代码执行时因为2.7.x的一个bug，需要带-O参数：python -O thread.py（感觉是一个assert语句有问题）
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

# Pool，如果要启动大量子进程，可以用进程池的方式批量创建子进程

#from multiprocessing import Pool
#import os, time, random
#def long_time_task(name):
#    print 'Run task %s (%s)...' % (name, os.getpid())
#    start = time.time()
#    time.sleep(random.random() * 3)
#    end = time.time()
#    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
#if __name__ == '__main__':
#    print 'Parent process %s.' % os.getpid()
#    p = Pool()
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print 'Waiting for all subprocesses done...'
#    p.close()
#    p.join()
#    print 'All subprocesses done.'

# 以上代码执行时也要带上-O参数：python -O thread.py
# 对Pool对象调用join()方法会等待所有子进程执行完毕。
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# Pool的默认大小是CPU核数

# 进程间通信

# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据

#from multiprocessing import Process, Queue
#import os, time, random
# 写数据进程执行的代码
#def write(q):
#    for value in ['A', 'B', 'C', 'D']:
#        print 'Put %s to queue...' % value
#        q.put(value)
#        time.sleep(random.random())
# 读数据进程执行的代码
#def read(q):
#    while True:
#        value = q.get(True)
#        print 'Get %s from queue.' % value
#if __name__ == '__main__':
#    # 父进程创建Queue，并传给各个子进程
#    q = Queue()
#    pw = Process(target=write, args=(q,))
#    pr = Process(target=read, args=(q,))
#    # 启动子进程pw，写入
#    pw.start()
#    # 启动子进程pr，读取
#    pr.start()
#    # 等待pw结束
#    pw.join()
#    # pr进程里是死循环，无法等待其结束，只能强行终止
#    pr.terminate()

# multiprocessing模块封装了fork()调用，使用我们不需要关注fork()的细节。
# 由于Windows没有fork()调用，因此，multiprocessing需要模拟出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去。
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

# 多线程

# 线程是操作系统直接支持的执行单元，Python的线程是真正的Posix Thread，而不是模拟出来的线程
# Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time, threading
# 新线程执行的代码
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name
print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name

# 由于任何进程默认就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程
# Python的threading模块的current_thread()方法永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，若不指定，Python自动给线程命名

# Lock

# 多线程和多进程最大的不同在于，进程之间数据互不影响，但线程之间数据是共享的。
# 多个线程同时改同一个变量，可能导致数据不一致。

import time, threading
# 存款余额
balance = 0
def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(10000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

# 以上balance值的不一致就是由于change_it()不是原子操作，而线程执行时可能中断导致的。
# 必须确保一个线程在修改balance时别的线程不能改。
# 如果要确保balance计算正确，就要给change_it()上一把锁，创建锁通过threading.Lock()来实现。

balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(10000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完释放锁
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

# 当多个线程同时执行lock.acquire()时，只有一个能成功获取锁得以继续执行，其他线程继续等待直到获得锁为止。
# 为了防止死锁，要用try...finally来确保锁一定会被释放。
# 锁可以保证数据一致性，但程序效率会下降。
# 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起。

# 多核CPU

# 用Python写个死循环
import threading, multiprocessing
def loop():
    x = 0
    while True:
        x = x ^ 1
#for i in range(multiprocessing.cpu_count()):
#    t = threading.Thread(target=loop)
#    t.start()
# 以上死循环代码并不能将CPU利用率跑到100%，因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock。
# 任何Python线程执行前，必须先获得GIL锁。然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器

# 所以，Python中可以使用多线程，但不能有效利用多核，如果要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
# 虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响

