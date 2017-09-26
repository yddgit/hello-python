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

