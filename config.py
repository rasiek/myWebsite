import os

basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret-key'

    pg_user = "postgres"
    pg_pwd = "Meneaelbote1157"
    pg_port = "5432"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Meneaelbote1157@localhost/pj_flask2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopementConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

