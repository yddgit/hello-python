#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python内置了SQLite3
# 要操作关系数据库，首先需要连接到数据库Connection，连接后需要打开游标Cursor
# 通过Cursor执行SQL语句，然后获得执行结果
# Python定义了一套操作数据库的API接口，由于SQLite驱动内置在Python标准库中，所以可以直接使用

# 导入SQLite驱动
import sqlite3
# 连接到SQLite数据库，数据库文件是test.db，如果文件不存在会自动创建
try:
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 继续执行一条SQL，插入一条记录
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    # 通过rowcount获得插入的行数
    print cursor.rowcount
except sqlite3.Error, e:
    print e
finally:
    # 关闭Cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭Connection
    conn.close()

# 查询记录
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句
    cursor.execute('select * from user where id = ?', ('1',))
    # 获得查询结果
    values = cursor.fetchall()
    print values
except sqlite3.Error, e:
    print e
finally:
    cursor.close()
    conn.close()

# 使用Python DB API时，Connection和Cursor对象打开后一定要关闭

# 使用Cursor对象
# 1.执行insert、update、delete语句时，执行结果由rowcount返回影像的行数就可以拿到执行结果
# 2.执行select语句时，通过fetchall()可以拿到结果集，结果集是一个list，每个元素都是这个tuple对应一行记录

# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?点位符就必须对应几个参数

