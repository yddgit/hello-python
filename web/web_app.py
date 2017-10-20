#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python有很多开源的Web框架，这里使用Flask做为示例
# 首先安装：easy_install flask

# 写一个Web程序，处理3个URL，分别是：
# 1. GET / 首页，返回Home
# 2. GET /signin 登录页，显示登录表单
# 3. POST /signin 处理登录表单，显示登录结果

# Flask通过Python的装饰器在内部自动地把URL和函数关联起来
from flask import Flask
from flask import request

app = Flask(__name__)

def getHTML(text):
    '''
    获取HTML文本
    '''
    return '<html><body>%s</body></html>' % text

@app.route('/', methods=['GET', 'POST'])
def home():
    '''
    首页
    '''
    return getHTML('<h1>Home</h1>')

@app.route('/signin', methods=['GET'])
def signin_form():
    '''
    登录页面
    '''
    return getHTML('''
            <form action="/signin" method="post">
            <p><label>Username: <input name="username" type="text"/></label></p>
            <p><label>Password: <input name="password" type="password"/></label></p>
            <p><button type="submit">Sign In</button></p>
            </form>
            ''')

@app.route('/signin', methods=['POST'])
def signin():
    '''
    登录处理
    '''
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return getHTML('<h3>Hello, Admin!</h3>')
    return getHTML('<h3>Bad username or password</h3>')

if __name__ == '__main__':
    app.run()

# 常见的Python Web框架还有：
# 1.Django 全能型Web框架
# 2.web.py 一个小巧的Web框架
# 3.Bottle 与Flask类似的Web框架
# 4.Tornado Facebook的开源异步Web框架

