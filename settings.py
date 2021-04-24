import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/app?charset=utf8'  # path：鏈接db的URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 提高性能 減少内存使用
    SECRET_KEY = 'root'  # 密鑰：防止CSRF攻擊
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SENDER = 'email'  # os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'email'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'password'  # os.environ.get('MAIL_PASSWORD')


class Development(Config):
    ENV = 'development'
    DEBUG = True


class Production(Config):
    ENV = 'production'
    DEBUG = False
    # SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))


