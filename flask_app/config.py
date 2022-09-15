"""Flask config class."""
from pathlib import Path


class Config(object):
    DEBUG = False
    SECRET_KEY = 'JYJaRtsTjwdjD0faY2MvqA'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_PATH = Path('data')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(__file__).parent.joinpath('user_data.sqlite'))
    UPLOADED_PHOTOS_DEST = Path(__file__).parent.joinpath("static/img")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False