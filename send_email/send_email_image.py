#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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

# 如果要把一个图片嵌入到邮件正文中，可以直接在HTML邮件中链接图片地址，但大部分邮件服务商都会自动屏蔽带有外链的图片
# 要把图片嵌入到邮件正文中，只能先把图片做为附件添加进去，然后在HTML中通过src="cid:0"来引用。
# 如果有多个图片，给它们依次编号，引用不同的cid:x即可
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr) # 有些邮箱要求必须指定发件人，如新浪邮箱
msg['To'] = _format_addr(u'冬冬 <%s>' % to_addr)
msg['Subject'] = Header(u'有图片的一封邮件', 'utf-8').encode()

# 邮件正文中引用附件中的图片
msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src="cid:0/></p></body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('../test_blur.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpeg类型
    mime = MIMEBase('image', 'jpeg', filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attchment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

#server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465) # 有些邮箱要求必须使用SSL连接，如QQ邮箱
# 打印出和SMTP服务器交互的所有信息，可以观察经过编码的邮件头，如：From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?=...
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

