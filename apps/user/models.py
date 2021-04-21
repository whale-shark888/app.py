# -*- coding: utf-8 -*-
from datetime import datetime

from ext import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(32), nullable=False, unique=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    register_time = db.Column(db.DateTime, default=datetime.now)
    deleted = db.Column(db.Boolean, default=False)
    online = db.Column(db.Boolean, default=False)
    content = db.relationship('Content', backref='user')

    def __str__(self):
        return self.username
