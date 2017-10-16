#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib

# 格式化邮件地址，如果包含中文需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 输入Email地址和口令
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址
smtp_server = raw_input('SMTP Server: ')
# 输入收件人地址
to_addr = raw_input('To: ')

# 邮件正文
msg = MIMEText('Hello, send by Python...(Encrypted)', 'plain', 'utf-8')

# 邮件主题、如何显示发件人、收件人等信息
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr) # 有些邮箱要求必须指定发件人，如新浪邮箱
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP加密的问候……', 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件整个过程可能会被窃听
# 要安全的发送邮件，可以加密SMTP会话，实际就是先创建SSL安全连接，然后再使用SMTP协议发送邮件
server = smtplib.SMTP_SSL(smtp_server, 465) # 有些邮箱要求必须使用SSL连接，如QQ邮箱
# 打印出和SMTP服务器交互的所有信息
server.starttls() # 创建安全连接
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 邮件小结

# 构造一个邮件对象就是一个Message对象：
# 1.MIMEText表示文本邮件对象
# 2.MIMEImage表示一个作为附件的图片
# 3.MIMEMultipart可以把多个对象组合起来
# 4.MIMEBase可以表示任何对象
#
# 其继承关系如下：
# Message
# +--MIMEBase
#    +--MIMEMultipart
#    +--MIMENonMultipart
#       +--MIMEMessage
#       +--MIMEText
#       +--MIMEImage
#
# 这种嵌套关系可以构造出任意复杂的邮件，可以通过
# https://docs.python.org/2/library/email.mime.html
# 查看它们所在的包及详细用法

