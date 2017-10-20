#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 为了方便的生成复杂的HTML，需要使用模板技术
# 使用模拟，需要准备一个HTML文档，嵌入一些变量和指令，然后根据输入的数据替换后得到最终的HTML
# 即MVC：Model-View-Controller
# Python中处理URL的函数就是Controller

# Flask通过render_template()函数来实现模板的渲染，Python的模板也有很多种，Flask默认支持jinja2
# 安装jinja2：easy_install jinja2

# 以下程序与模板的目录结构：
# +--app.py
# +--templates
#    +--form.html
#    +--home.html
#    +--signin-ok.html

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    '''
    首页
    '''
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    '''
    登录页面
    '''
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    '''
    登录处理
    '''
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

# 使用模板的好处是，修改方便，保存刷新浏览器就能看到效果，方便调试
# Jinja2模板中，用{{ name }}表示一个需要替换的变量。
# 很多时候还需要循环、条件判断等指令语句，Jinja2中用{% ... %}表示指令
# 比如：循环输出页码
'''
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
'''

# 除了Jinja2，常见的模板还有：
# 1.Mako 用<% ... %>和${xxx}的一个模板
# 2.Cheetah 也是用<% ... %>和${xxx}的一个模板
# 3.Django Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板

