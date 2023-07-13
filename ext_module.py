#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python有大量的第三方模块，基本都会在PyPI - the Python Package Index（https://pypi.python.org/）上注册
# 只要找到对应模块名字，即可用easy_install或pip安装

# PIL

# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库，功能强大，简单易用

# 安装PIL：pip install Pillow
# PIL的官方网站：http://pythonware.com/products/pil/

# 操作图像：图像缩放

#from PIL import Image
#im = Image.open('test.jpg') # 打开一个jpg图像
#w, h = im.size # 获取图像尺寸
#im.thumbnail((w//2, h//2)) # 缩小到50%
#im.save('thumb.jpg', 'jpeg') # 把缩放后的图像用jpeg格式保存

# 操作图像：切片、旋转、滤镜、输出文字、调色板等

# 如：模糊效果
#from PIL import Image, ImageFilter
#im = Image.open('test_blur.jpg')
#im2 = im.filter(ImageFilter.BLUR)
#im2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，可以直接绘图，如生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240x60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# PIL官方文档：http://effbot.org/imagingbook/
# Pillow官方文档：https://pillow.readthedocs.org/

# requests

# urllib使用麻烦，缺少实用的高级功能，可以使用第三方库requests
import requests

r = requests.get('https://www.google.com/')
print(r.status_code)
print(r.text[0:100], '...')

r = requests.get('https://www.google.com/', params={'q': 'python'})  # 传递参数
print(r.url)  # 实际请求的url
print(r.encoding)  # requests自动检测编码
print(r.content[0:100], '...')  # 使用content获得响应内容的bytes对象

r = requests.get('https://yesno.wtf/api')
print(r.json())  # 对于特定类型的响应，如：直接获取JSON

r = requests.get('https://www.google.com', headers={'X-Client-Type': 'chrome browser'})  # 传递header使用dict
print(r.text[0:100], '...')

r = requests.post('https://yesno.wtf/api', data={'force': 'yes'})  # 默认使用application/x-www-form-urlencoded
print(r.text[0:100], '...')
r = requests.post('http://yesno.wtf/api', json={'force': 'yes'})  # 传递JSON数据
print(r.json())

# 上传文件，需要用rb模式读取，这样bytes的长度才是文件的长度
#r = requests.post('https://yesno.wtf/api', files={'file': open('report.xls', 'rb')})

r = requests.get('https://www.google.com')
print(r.headers)  # 获取headers
print(r.headers['Content-Type'])
print(r.cookies['AEC'])  # 获取cookies

r = requests.get('https://yesno.wtf/api', cookies={'token': '12345', 'status': 'working'})  # 传入Cookie
print(r.text[0:100], '...')
r = requests.get('https://yesno.wtf/api', timeout=2.5)  # 指定超时时间（秒）
print(r.text[0:100], '...')

# chardet

import chardet

print(chardet.detect(b'Hello World'))
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# confidence表示检测的概率是1.0，即100%

print(chardet.detect('这是一段中文，拜托'.encode('gbk')))  # GBK是GB2312的超集
print(chardet.detect('这是一段中文'.encode('utf-8')))
print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))

# https://chardet.readthedocs.io/en/latest/supported-encodings.html

# psutil

# process and system utilities

import psutil

print('cpu count:', psutil.cpu_count())
print('physical cpu count:', psutil.cpu_count(logical=False))
print('cpu times:', psutil.cpu_times())
for x in range(10):
    print('cpu percent:', psutil.cpu_percent(interval=1, percpu=True))
print('virtual mem:', psutil.virtual_memory())
print('swap mem:', psutil.swap_memory())
print('disk partition:', psutil.disk_partitions())
print('disk usage:', psutil.disk_usage('C:'))
print('disk io:', psutil.disk_io_counters())
print('network io:', psutil.net_io_counters())
print('network if address:', psutil.net_if_addrs())
print('network if stats:', psutil.net_if_stats())
print('network connections:', psutil.net_connections())
print('pids:', psutil.pids())
# p = psutil.Process(6432)
# p.name()  # 进程名称
# p.exe()  # 进程exe路径
# p.cwd()  # 进程工作目录
# p.cmdline()  # 进程启动的命令行
# p.ppid()  # 父进程ID
# p.parent()  # 父进程
# p.children()  # 子进程列表
# p.status()  # 进程状态
# p.username()  # 进程用户名
# p.create_time()  # 进程创建时间
# p.terminal()  # 进程终端
# p.cpu_times()  # 进程使用的CPU时间
# p.memory_info()  # 进程使用的内存
# p.open_files()  # 进程打开的文件
# p.connections()  # 进程相关的网络连接
# p.num_threads()  # 进程的线程数量
# p.threads()  # 所有线程信息
# p.environ()  # 进程环境变更
# p.terminate()  # 结束进程
psutil.test()  # 类似ps命令的效果
