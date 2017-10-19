#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Web应用的本质：
# 1.浏览器发送一个HTTP请求
# 2.服务器收到请求，生成一个HTML文档
# 3.服务器把HTML文档作为HTTP响应的Body发送给浏览器
# 4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示

# 常见的HTTP服务器：Apache、Nginx、Lighttpd

# 对于Python，有一个处理TCP连接、HTTP原始请求和响应的统一接口
# WSGI: Web Server Gateway Interface
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求

def application(environ, start_response):
    CONTENT_TYPE = 'text/html; charset=utf-8'
    start_response('200 OK', [('Content-Type', CONTENT_TYPE)])
    pathInfo = environ['PATH_INFO'][1:]
    htmlText = u'<html><body><h1>Hello %s</h1></body></html>' % (pathInfo.decode('utf-8') or u'World')
    return htmlText.encode('utf-8')
# 以上，application函数就是符合WSGI标准的一个HTTP处理函数，接收两个参数：
# 1.environ: 一个包含所有HTTP请求信息的dict对象
# 2.start_response: 一个发送HTTP响应的函数

# 在application()函数中，调用start_response方法就发送了HTTP响应的Header。
# 注意Header只能发送一次，也就是只能调用一次start_response()函数

# start_response()函数接收两个参数：
# 1.HTTP响应码
# 2.一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
# 通常情况下都应该把Content-Type头发送给浏览器，其他常用的HTTP Header也应该发送
# 然后函数的返回值将作为HTTP响应的Body发送给浏览器

# application()函数必须由WSGI服务器来调用，有很多符合WSGI规范的服务器可以用。
# Python内置了一个WSGI服务器，模块名wsgiref，是用纯Pyhton编写的WSGI服务器的参考实现。
# 完全符合WSGI标准，但不考虑任何运行效率，仅供开发和测试使用。

# server.py
# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入自己编写的application函数
#from hello import application

# 创建一个服务器，IP地址为空，商品是8000，处理函数是application
httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000...'
# 开始监听HTTP请示
httpd.serve_forever()

# 无论多么复杂的Web应用程序，入口就是一个WSGI处理函数。
# HTTP请求的所有输入信息都可以通过environ获得
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body

