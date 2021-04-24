# -*- coding: utf-8 -*-
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ext import db
# from flask_login import UserMixin
# from app import login


# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    register_time = db.Column(db.DateTime, default=datetime.now)
    # confirmed = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    icon = db.Column(db.LargeBinary(65536), default=False)
    # content = db.relationship('Content', backref='user')
    contents = db.relationship('Content', backref='user', secondary='ucpc')
    pictures = db.relationship('Picture', backref='user', secondary='ucpc')
    comments = db.relationship('Comment', backref='user', secondary='ucpc')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


















