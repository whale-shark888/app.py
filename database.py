# -*- coding: utf-8 -*-
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import settings
from datetime import datetime


# 放配置文件或主文件，只允許有一個app
app = Flask(__name__)
app.config.from_object(settings)  # config for test
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/app'  # path：鏈接db的URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 提高性能 減少内存使用
app.config['SECRET_KEY'] = 'root'  # 密鑰：防止CSRF攻擊


db = SQLAlchemy(app)  # 建立對象


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)


def add_info(instance):
    db.session.add(instance)
    db.session.commit()


def del_info(user):  # delete date
    obj = User.query.filter(user.email).delete()
    db.session.commit()


def check_info(primary_key):
    obj = User.query.get(primary_key)
    print(obj.id, obj.email, obj.name)


def check_all():
    obj = User.query.all()
    for i in obj:
        print(i.primary_key, i.email, i.name)


def check_filter(user):  # 條件查找
    obj = User.query.filter(user.id, user.email, user.name)


def check_filter_by(user):
    obj = User.query.filter_by(user.id, user.email, user.name).all()


def modify_info(primary_key, name):
    obj = User.query.get(primary_key).update({'name': name})
    db.session.commit()


if __name__ == '__main__':
    db.create_all()

