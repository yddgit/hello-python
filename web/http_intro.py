#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Web应用中，服务器把网页传给浏览器，实际就是把HTML代码发送给浏览器，让浏览器显示出来。
# 浏览器与服务器之间的传输协议是HTTP，所以：
# 1. HTML是一种用来定义网页的文本
# 2. HTTP是在网络上传输HTML的协议，约定服务器和浏览器的通信规则

# 一个HTTP请求头示例
'''
GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: PSTM=1502644000; BD_CK_SAM=1; BD_HOME=0; BD_UPN=12314753
'''
# 第一行：GET读取请求，/表示URL的路径，HTTP/1.1指使用HTTP协议的1.1版本，与1.0的主要区别是允许多个HTTP请求复用一个TCP连接以加快传输速度
# 第二行开始，每一行都类似于XXX: abcdfeg，如[Host: www.baidu.com]表示请求的域名是www.baidu.com。
# 如果一台服务器有多个网站，服务器就需要通过Host来区分浏览器请求的是哪个网站

# 一个HTTP响应头示例
'''
HTTP/1.1 200 OK
Cache-Control: private
Connection: Keep-Alive
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
Date: Thu, 19 Oct 2017 08:09:28 GMT
Expires: Thu, 19 Oct 2017 08:09:24 GMT
Server: BWS/1.1
Set-Cookie: BD_HOME=0; path=/
Strict-Transport-Security: max-age=172800
Vary: Accept-Encoding
X-Powered-By: HPHP
X-Ua-Compatible: IE=Edge,chrome=1
Transfer-Encoding: chunked
'''
# 第一行：200表示一个成功的响应，后面的OK是说明。
# 失败的响应有404 Not Found网页不存在，500 Interval Server Error服务器内部出错，等等
# Content-Type指示响应的内容，text/html表示HTML网页，浏览器就是依靠Content-Type来判断响应的内容是网页还是图片

# HTTP请求：
# 方法：GET还是POST，GET仅请求资源，POST会附带用户数据
# 路径：/full/url/path
# 域名：由Host头指定，Host: www.baidu.com
# 其他相关的Header，如果是POST，请求还包括一个Body，包含用户数据

# HTTP响应：
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务端处理时发生了错误
# 响应类型：由Content-Type指定
# 其他相关的Header，通常服务器的响应会携带一个Body，包含响应内容，如网页的HTML源码

# HTTP协议采用了非常简单的请求-响应模式，大大简化了开发。
# 编写一个页面，只需要通过HTTP响应把HTML发送出去，不需要考虑如何附带图片、视频。
# 浏览器如果需要请求图片和视频，它会发送另一个HTTP请求。
# 一个HTTP请求只处理一个资源。

# HTTP请求和响应都遵循相同的格式，包含Header和Body两部分，Body是可选的。
# HTTP GET请求格式：每个Header一行一个，换行符是\r\n
'''
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
'''
# HTTP POST请求格式：当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body
'''
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''
# HTTP响应的格式：响应如果包含Body，也是通过\r\n\r\n来分隔的
'''
HTTP/1.1 200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''
# Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据
# 当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip
# 因此看到Content-Encoding: gzip时，需要将Body数据先解压缩才能得到真正的数据。压缩是为了减少Body的大小，加快网络传输

# HTTP协议书籍：《HTTP: The Definitive Guide》，中文译本：《HTTP权威指南》
