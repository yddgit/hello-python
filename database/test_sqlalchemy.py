#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ORM: Object-Relational Mapping
# Python中最有名的ORM框架是SQLAlchemy
# 安装SQLAlchemy: easy_install sqlalchemy

# 导入SQLAlchemy，并初始化DBSession
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接，SQLAlchemy用一个字符串表示连接信息
# '数据库类型+数据库驱动名称://用户名:口令@主机地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 以上完成SQLAlchemy的初始化和每个表的class定义。如果有多个表，就继续定义其他class

# 向数据库中添加一行记录，可以视为添加一个User对象

# 创建session对象
session = DBSession()
# 创建User对象
new_user = User(id='3', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()

# 以上，关键是获取session，然后把对象添加到session最后提交并关闭。Session可以视为当前数据库连接

# 查询数据，通过ORM查询出来的不再是tuple，而是User对象

# 创建Session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性
print 'type: %s, name: %s' % (type(user), user.name)
# 关闭session
session.close()

# ORM就是把数据库表的行与相应的对象建立关联，互相转换。
# 由于关系数据库的多个表还可以用外键实现一对多，多对多等关联，相应地ORM框架也可以提供这种关联
# 如，一个User拥有多个Book，就可以定义一对多关系如下：
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 多的一方的book表通过外键关联到user表
    user_id = Column(String(20), ForeignKey('user.id'))

# 这样，当查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list

