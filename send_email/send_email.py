#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 电子邮件的基本概念

# 假设：我的邮件地址me@163.com，对方的邮件地址friend@sina.com

# 使用Outlook或Foxmail之类的软件写好邮件，填写对方Email地址，点“发送”，邮件就发出去了。
# 这些电子邮件软件称为MUA：Mail User Agent（邮件用户代码）

# Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent（邮件传输代理），
# 就是那些Email服务提供商，比如网易、新浪等。
# 由于我的电子邮件是163.com，所以Email首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。
# 这个过程中间可能还会经过别的MTA，但是我们不关心具体路线。

# Email到达新浪MTA后，由于对方使用的sina.com的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent（邮件投递代理）。
# Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。
# 对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上。

# 一封电子邮件的旅程：发件人-->MUA-->MTA-->MTA-->...-->MDA<--MUA<--收件人
# 因此，编写程序来发送和接收邮件，本质就是：
# 1.编写MUA把邮件发到MTA
# 2.编写MUA从MDA上收邮件

# 发邮件时：MUA和MTA使用的协议是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议
# 收邮件时：MUA和MDA使用的协议有两种：
# - POP（Post Office Protocol，目前是版本3，俗称POP3）
# - IMAP（Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等）

# 配置邮件客户端软件时，需要先配置SMTP服务器，也就是要发到哪个MTA上，如163提供的SMTP服务器地址：smtp.163.com
# 类似的，从MDA收邮件时，也要配置POP3或IMAP服务器地址、邮箱地址和口令

# Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# 对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtp负责发送邮件。

from email.mime.text import MIMEText
import smtplib

# 输入Email地址和口令
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址
smtp_server = raw_input('SMTP Server: ')
# 输入收件人地址
to_addr = raw_input('To: ')

# 构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype，传plain最终MIME就是text/plain，最后用utf-8编码保证多语言兼容性
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

#server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465) # 有些邮箱要求必须使用SSL连接，如QQ邮箱
# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 以上邮件有如下问题：
# 1.邮件没有主题
# 2.收件人的名字没有显示为友好的名字
# 3.明明收到了邮件，却提示不在收件人中

