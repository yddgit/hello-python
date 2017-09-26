#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TCP是建立可靠连接并且通信双方都可以以流的形式发送数据，UDP则是面向无连接的协议
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号就可以直接发送数据包
# 虽然UDP传输数据不可靠，但它的优点是速度快，对于不要求可靠到达的数据就可以使用UDP协议

import socket

# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 服务器绑定UDP端口和TCP端口是互不冲突的
s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999...'
# 不需要调用listen()方法，而是直接接收任何客户端的数据
while True:
    # recvfrom()方法返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)

