# -*- coding: utf-8 -*-
from flask import Flask
import settings
from apps.user.view import user_bp
from ext import db
from flask_login import login_manager
import os
from flask_mail import Mail


# config app and create app
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.Development)
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

    db.init_app(app)  # 同ext.db關聯同一個app

    login_manager.session_protection = 'strong'
    # 注冊blueprint
    # app.register_blueprint(user_bp)
    return app
