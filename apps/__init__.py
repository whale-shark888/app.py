# -*- coding: utf-8 -*-
from flask import Flask
import settings
from apps.user.view import user_bp
from ext import db


# config app and create app
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.Development)
    db.init_app(app)  # 同ext.db關聯同一個app
    # 注冊blueprint
    app.register_blueprint(user_bp)
    return app
