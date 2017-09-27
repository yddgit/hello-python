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

# 构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype，传plain最终MIME就是text/plain，最后用utf-8编码保证多语言兼容性
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

# 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中
# 因此，必须把From、To、Subject添加到MIMEText中，才是一封完整的邮件
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr) # 有些邮箱要求必须指定发件人，如新浪邮箱
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
# 收件箱中看到的收件人名字可能不是我们指定的“管理员”，因为很多邮件服务商在显示邮件时会把收件人名字自动替换成用户注册的名字，但其他收件人名字是显示不受影响
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465) # 有些邮箱要求必须使用SSL连接，如QQ邮箱
# 打印出和SMTP服务器交互的所有信息，可以观察经过编码的邮件头，如：From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?=...
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

