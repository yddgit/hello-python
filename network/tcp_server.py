#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 服务器进程要绑定一个端口并监听来自其他客户端的连接。
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接。

# 服务器需要同时响应多个客户端的请求，所以每个连接都需要一个新的进程或者新的线程来处理。

# 编写一个服务器程序，接收客户端连接，把客户端发过来的字符串加上Hello再发回去

import socket, time, threading
# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听的地址和端口，可以用0.0.0.0绑定所有网络地址
# 端口可以选择一个大于1024的端口，小于1024的端口号必须要有管理员权限才能绑定
# 同一个端口被绑定以后，就不能被别的Socket绑定了
s.bind(('127.0.0.1', 9999))
# 开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print 'Waiting for connection...'
# 连接建立后，服务器先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端
# 如果客户端发送了exit字符串，就直接关闭连接
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
# 通过循环来接受客户端连接，accept()会等待并返回一个客户端连接
while True:
    sock, addr = s.accept() # 接受一个新连接
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

