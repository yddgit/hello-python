#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户电脑或手机上，最常用的POP协议，目前版本号是3，俗称POP3
# Python内置poplib模块实现了POP3协议，可以直接用来收邮件

# 收邮件分两步：
# 1.用poplib把邮件原始文本下载到本地
# 2.用email解析原始文本，还原为邮件对象

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址、口令和POP3服务器地址
email = raw_input('Email: ')
password = raw_input('Password: ')
pop3_server = raw_input('POP3 server: ')

# 连接到POP3服务器，有些邮箱必须使用安全连接，如QQ邮箱
#server = poplib.POP3(pop3_server)
server = poplib.POP3_SSL(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 打印POP3服务器的欢迎文字
print server.getwelcome()
# 身份认证
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间
print 'Message: %s. Size: %s' % server.stat()
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184']
print mails
# 获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = '\r\n'.join(lines)
# 稍后解析出邮件(需要导入必要的模块)
msg = Parser().parsestr(msg_content)
# 可以根据邮件索引号直接从服务器删除邮件
#server.dele(index)
# 关闭连接
server.quit()

# 邮件Subject和Email中包含的名字都是经过编码的str，要正常显示需要decode
# decode_header()返回一个list，因为像Cc，Bcc这样的字段可能包含多个邮件地址
# 以下代码，只取第一个元素
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件内容也是str，还需要检测编码，否则非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    # 先从msg对象获取编码
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 解析邮件内容
# 接收到的Message对象本身可能是一个MIMEMultipart对象，
# 包含嵌套的MIMEBase对象，嵌套可能不止一层，需要递归解析
def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的From、To、Subject存在于根对象上
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串
                    value = decode_str(value)
                else:
                    # 需要解码Email地址
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print '%s%s: %s' % ('  ' * indent, header, value)
    if (msg.is_multipart()):
        # 如果邮件对象是一个MIMEMultipart
        # get_payload()返回list，包含所有子对象
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print '%spart %s' % ('  ' * indent, n)
            print '%s-------------------' % ('  ' * indent)
            # 递归打印每个子对象
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个MIMEMultipart，就根据content_type判断
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 纯文本或HTML内容
            content = msg.get_payload(decode=True)
            # 要检测文本编码
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print '%sText: %s' % ('  ' * indent, content + '...')
        else:
            # 不是文本，作为附件处理
            print '%sAttachment: %s' % ('  ' * indent, content_type)

# 打印邮件内容
print_info(msg)
