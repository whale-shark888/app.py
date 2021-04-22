# -*- coding: utf-8 -*-
from datetime import datetime

from ext import db


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    po_datetime = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('user', backref='content', secondary='ucpc')
    picture = db.relationship('picture', backref='content', secondary='ucpc')
    comment = db.relationship('comment', backref='content', secondary='ucpc')


class Picture(db.Model):
    __tablename__ = 'picture'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    picture_name = db.Column(db.String(128), unique=True, nullable=False)
    picture_datetime = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    picture_binary = db.Column(db.LargeBinary(16777216))

    user = db.relationship('user', backref='picture', secondary='ucpc')
    content = db.relationship('content', backref='picture', secondary='ucpc')
    comment = db.relationship('comment', backref='picture', secondary='ucpc')

# class User_content(db.Model):
#     __tablename__ = 'User_content'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
#
#
# class Content_picture(db.Model):
#     __tablename__ = 'content_picture'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
#     picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)

    user = db.relationship('user', backref='comment', secondary='ucpc')
    content = db.relationship('content', backref='comment', secondary='ucpc')
    picture = db.relationship('picture', backref='comment', secondary='ucpc')


class UCPC(): # user content picture comment
    __tablename__ = 'ucpc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)