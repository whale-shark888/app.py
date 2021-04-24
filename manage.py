from flask import Flask, request, make_response, current_app, session, redirect, url_for
from flask import render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User
from apps.share_content.models import Content
from apps.gmail.send_mail import *
import random
from flask_login import current_user, login_user


from werkzeug.security import generate_password_hash, check_password_hash
import requests
from apps import create_app
from ext import db
import os
from flask_mail import Message, Mail

app = create_app()
# login = LoginManager(app)
manager = Manager(app=app)
# WSGI  Flask is a class， app is a object
migrate = Migrate(app=app, db=db)  # config
manager.add_command('db', MigrateCommand)  # config CLI 用mapping建立數據庫表


@app.route('/')  # 路由 網址
def index():  # mtv: view函數；index可任意取名
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login2', methods=['POST', 'GET'])
def login2():
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    else:
        if request.method == 'POST':
            try:
                email = request.form.get('email')
                password = request.form.get('password')
                user = User.query.filter_by(email=email).first()

                if user.check_password(password):
                    login_user(user)
                    return 'login successfully'
            except AttributeError:
                return 'error of username or password'


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register2', methods=['POST', 'GET'])
def register2():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('password2')
        if password == re_password and len(password) >= 8:
            i = 6
            b = []
            while i >= 1:
                a = random.randint(0, 9)
                i -= 1

                b.append(str(a))
            print(b)
            ve_num = ''.join(b)
            en_num = generate_password_hash(ve_num)
            senmail('verify', 'x1098952061@gmail.com', 'verify', ve_num)
            ip = input('verify:')
            if check_password_hash(en_num, ip):
                user = User()
                user.email = email
                user.username = username
                # user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # encrypted
                # 需要加密密碼
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                return 'content'
            else:
                print('code is wrong')
        else:
            pass
            return 'fail'


# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     if current_user.is_authenticated:
#


@app.route('/select', methods=['GET', 'POST'])
def user_select():
    info = request.form.get('email')
    user_list = User.query.filter_by(User.username.startswith(info)).all()
    email_list = User.query.filter_by(User.email.startswith(info)).all()
    id_list = User.query.filter_by(User.id.startswith(info)).all()
    return render_template('', user_list=user_list, email_list=email_list, id_list=id_list)


@app.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'POST':
        text = request.form.get('content')
        us_id = request.form.get('us_id')
        content = Content()
        content.text = text
        # content.picture =
        content.user_id = us_id
        db.session.add(content)
        db.session.commit()
        return 'complement'
    else:
        users = User.query.filter(User.deleted == False).all()


if __name__ == '__main__':
    manager.run()  # debug=True 用于調試；port defaults to 5000
    # flask 内置服務器 運行server
