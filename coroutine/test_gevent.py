#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python通过yield提供了对协程的基本支持，而第三方的gevent为Python提供了比较完善的协程支持
# gevent是第三方库，通过greenlet实现协程，其基本思想是：
# 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
# 由于IO操作非常耗时，经常使用程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

# 由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        # 要让greenlet交替运行，可以通过gevent.sleep()交出控制权
        gevent.sleep(0)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

# 实际应用中，不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print 'GET: %s' % url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s' % (len(data), url))

gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://github.com'),
    gevent.spawn(f, 'https://www.baidu.com'),
])

# 从结果看，3个网络操作是并发执行的，而结束顺序不同，但只有一个线程

# 使用gevent，可以获得极高的并发性能，但gevent只能在Unix/Linux下运行，Windows下不保证正常安装和运行（经测试可以正常运行）
# 由于gevent是基于IO切换的协程，所以编写好的WebApp代码，在部署的时候选择一个支持gevent的WSGI服务器即可立刻获得数倍的性能提升

