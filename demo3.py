# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
from flask import render_template
import settings
import database
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.config.from_object(settings)  # config for test
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/app'  # path：鏈接db的URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 提高性能 減少内存使用
app.config['SECRET-KEY'] = 'root'  # 密鑰：防止CSRF攻擊
# WSGI  Flask is a class， app is a object
db = SQLAlchemy(app)


@app.route('/')  # 路由 網址
def index():  # mtv: view函數；index可任意取名
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login2', methods=['POST'])
def login2():
    username = request.form.get('username')
    password = request.form.get('password')
    pass
    return 'aa'


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register2', methods=['POST'])
def register2():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    re_password = request.form.get('password2')
    if password == re_password:
        user = database.User(email=email, username=username, password=password)
        database.add_info(user)
        return 'content'
    else:
        pass
        return 'fail'


if __name__ == '__main__':
    app.run()  # debug=True 用于調試；port defaults to 5000
    # flask 内置服務器 運行server
