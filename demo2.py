# -*- coding: utf-8 -*-
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/app'  # path：鏈接db的URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 提高性能 減少内存使用
app.config['SECRET-KEY'] = 'root'  # 密鑰：防止CSRF攻擊
db = SQLAlchemy(app)  # 建立對象


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


db.create_all()
a = User('1', '2', '3')
# 增
db.session.add(a)
db.session.commit()
'''
# 查
user = User.query.get()  # 主鍵
print(User.username)

# 查全部
user = User.query.all()

# filter 條件循環查找
user = User.query.filter(User.email == 000)

# 改
user = User.query.get().update('':'')
user = User.query.filter().update('':'')

# 刪
user = User.query.get().delete()
user = User.query.filter().delete()
'''


