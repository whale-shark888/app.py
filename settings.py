class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/app?charset=utf8'  # path：鏈接db的URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 提高性能 減少内存使用
    SECRET_KEY = 'root'  # 密鑰：防止CSRF攻擊


class Development(Config):
    ENV = 'development'
    DEBUG = True


class Production(Config):
    ENV = 'production'
    DEBUG = False



