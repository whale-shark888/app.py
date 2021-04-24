# -*- coding: utf-8 -*-
from datetime import datetime

from ext import db


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    po_datetime = db.Column(db.DateTime, default=datetime.now)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    users = db.relationship('User', backref='content', secondary='ucpc')
    pictures = db.relationship('Picture', backref='content', secondary='ucpc')
    comments = db.relationship('Comment', backref='content', secondary='ucpc')


class Picture(db.Model):
    __tablename__ = 'picture'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    picture_name = db.Column(db.String(128), unique=True, nullable=False)
    picture_datetime = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    picture_binary = db.Column(db.LargeBinary(16777216))

    users = db.relationship('User', backref='picture', secondary='ucpc')
    contents = db.relationship('Content', backref='picture', secondary='ucpc')
    comments = db.relationship('Comment', backref='picture', secondary='ucpc')

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

    users = db.relationship('User', backref='comment', secondary='ucpc')
    contents = db.relationship('Content', backref='comment', secondary='ucpc')
    pictures = db.relationship('Picture', backref='comment', secondary='ucpc')


class UCPC(db.Model): # user content picture comment
    __tablename__ = 'ucpc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)