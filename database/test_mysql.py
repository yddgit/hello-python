#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 下载MySQL: https://dev.mysql.com/downloads/mysql/
# 安装MySQL数据库，设置数据库编码为utf-8，并设置root用户密码

# 安装MySQL驱动:

# 1.mysql-connector-python是MySQL官方的纯Python驱动
#   下载相应的MSI安装包直接安装即可: https://dev.mysql.com/downloads/connector/python/

# 2.MySQL-python是封装了MySQL C驱动的Python驱动，安装MySQL-python之前需要先安装
#   (1) Microsoft Visual C++ Compiler for Python 2.7
#   https://www.microsoft.com/en-us/download/details.aspx?id=44266
#   (2) mysql-connector-c-6.0.2-win32.msi
#   https://dev.mysql.com/downloads/connector/c/6.0.html#downloads
#   最后再使用pip安装: pip install MySQL-python

# 以mysql-connector-python为例，演示如何连接到MySQL服务器的test数据库

# 导入MySQL驱动
import mysql.connector
# 连接数据库test

try:
    conn = mysql.connector.connect(user='root', password='root', database='test', use_unicode=True)
    cursor = conn.cursor()
    # 创建user表
    cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    print cursor.rowcount
    # 提交事务
    conn.commit()
    cursor.close()
    # 运行查询
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print values
finally:
    # 关闭Cursor和Connection
    cursor.close()
    conn.close()

# 注意：MySQL的占位符是%s，通常连接MySQL时传入use_unicode=True让MySQL有DB-API始终返回Unicode
