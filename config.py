import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'God help us'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SSL_REDIRECT = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or '587')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS',
                                  'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[Search]'
    MAIL_SENDER = 'Admin <search@enova.pe>'
    ADMINS = ['yugo132@gmail.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    PAGE_SIZE = os.environ.get('PAGE_SIZE') or 25

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'search.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.MAIL_SENDER,
            toaddrs=cls.ADMINS,
            subject=cls.MAIL_SUBJECT_PREFIX + 'Applicatiton Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class LocalConfig(Config):
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('LOCAL_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'search-local.sqlite')


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        super(DockerConfig, cls).init_app(app)

        # log to stderr

        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.loger.addHandler(file_handler)


class TestingConfig(Config):
    TESTING = True
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
    WTF_CSRF_ENABLED = False


config = {
    'local': LocalConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    'default': LocalConfig
}
