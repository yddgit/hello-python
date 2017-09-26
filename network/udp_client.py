#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 客户端使用UDP时，首先创建基于UDP的Socket，然后不需要调用connect()，直接通过sendto()给服务器发数据

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.sendto(data, ('127.0.0.1', 9999)) # 发送数据
    print s.recv(1024) # 接收数据
s.close()

