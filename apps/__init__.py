# -*- coding: utf-8 -*-
from flask import Flask
import settings
# from apps.user.view import user_bp
from apps.gmail import mail
from ext import db
from flask_login import LoginManager


from flask_sslify import SSLify
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login2'
# config app and create app
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.Development)
    db.init_app(app)  # 同ext.db關聯同一個app
    mail.init_app(app)
    login_manager.init_app(app)
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        sslify = SSLify(app)

   # login_manager.session_protection = 'strong'
    # 注冊blueprint
    # app.register_blueprint(user_bp)
    return app

