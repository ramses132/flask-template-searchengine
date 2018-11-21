import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'God help us'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['yugo132@gmail.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    PAGE_SIZE = os.environ.get('PAGE_SIZE') or 25

class ProductionConfig(Config):
    DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'search.db')


class LocalConfig(ProductionConfig):
    DEBUG =  True

class TestingConfig(ProductionConfig):
    TESTING = True

