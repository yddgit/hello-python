#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 图形界面

# Python支持多种图形界面的第三方库，包括：Tk、wxWidgets、Qt、GTK等
# Python自带的库是支持Tk的Tkinter，无需安装任何包，就可以直接使用

# Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI

from Tkinter import *

# 在GUI中，每个Buttton、Label、输入框，都是一个Widget。Frame是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
# 如下：从Frame派生一个Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello World!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

#app = Application()
#app.master.title("Hello World") # 设置窗口标题
#app.mainloop() # 主消息循环

# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。

# 输入文本

# 在窗口中增加一个文本输入框，让用户可以输入文本，点按钮后，弹出消息对话框

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'World'
        tkMessageBox.showinfo('Messgae', 'Hello, %s' % name)

app = Application()
app.master.title("Hello World") # 设置窗口标题
app.mainloop() # 主消息循环

# 当点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本，使用tkMessageBox.showinfo()可以弹出消息对话框

# Python内置的Tkinter可以满足基本的GUI程序要求，如果是非常复杂的GUI程序，建议采用操作系统原生支持的语言和库来编写

