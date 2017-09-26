#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建一个基于TCP连接的Socket

import socket
# 创建一个socket
# AF_INET指定使用IPv4协议，要使用IPv6则指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议
# 此时，Socket对象创建成功，但还没有建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接，参数是一个tuple，包含地址和端口号
s.connect(('www.baidu.com', 80))
# TCP连接创建的是双向通道，双方谁先发谁后发，怎么协调要根据具体协议来决定
# HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端
s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# 发送的文件必须符合HTTP标准，如果格式没问题，就可以接收服务器返回的数据了
buffer = []
while True:
    d = s.recv(1024) # 每次最多接收1K字节
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# 数据接收完后调用close()方法关闭Socket
s.close()
# 接收到的数据包括HTTP头和网页本身，只需要把HTTP头和网页分离，打印HTTP头，保存网页内容到文件
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件
#with open('baidu.html', 'wb') as f:
#    f.write(html)

# tcp_server.py的客户端程序

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data) # 发送数据
    print s.recv(1024)
s.send('exit')
s.close()

