# -*- coding: utf-8 -*-
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ext import db
from flask_login import UserMixin
from apps import login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
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

    # followed = db.relationship('Follow',
    #                            foreign_keys=[Follow.follower_id],
    #                            backref=db.backref('follower', lazy='joined'),
    #                            lazy='dynamic',
    #                            cascade='all, delete-orphan')
    # followers = db.relationship('Follow',
    #                             foreign_keys=[Follow.followed_id],
    #                             backref=db.backref('followed', lazy='joined'),
    #                             lazy='dynamic',
    #                             cascade='all, delete-orphan')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def follow(self, user):
    #     if not self.is_following(user):
    #         f = Follow(follower=self, followed=user)
    #     db.session.add(f)
    #
    #     def unfollow(self, user):
    #         f = self.followed.filter_by(followed_id=user.id).first()
    #
    #     if f:
    #         db.session.delete(f)
    #
    #     def is_following(self, user):
    #         return self.followed.filter_by(followed_id=user.id).first() is not None
    #
    #     def is_followed_by(self, user):
    #         return self.followers.filter_by(
    #             follower_id=user.id).first() is not None

# class Follow(db.Model):
#      __tablename__ = 'follow'
#      follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
#      followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
#      timestamp = db.Column(db.DateTime, default=datetime.utcnow)
















