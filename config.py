import os

basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.urandom(24)

    pg_user = os.environ.get("PG_USER")
    pg_pwd = os.environ.get("PG_PWD")
    pg_port = os.environ.get("PG_PORT")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

