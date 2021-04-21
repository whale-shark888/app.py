# -*- coding: utf-8 -*-
from datetime import datetime

from ext import db


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    po_datetime = db.Column(db.DateTime, defualt=datetime.now)
    like_num = db.Column(db.Interger, default=0)
    picture = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)