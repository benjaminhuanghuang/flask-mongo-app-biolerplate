import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'

    MONGODB_SETTINGS = {
        'host': 'mongodb://admin:admin1234@ds119618.mlab.com:19618/db_todo'
    }

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER') or 'nobody@example.com'
    MAIL_FLUSH_INTERVAL = 3600  # one hour
    MAIL_ERROR_RECIPIENT = os.environ.get('MAIL_ERROR_RECIPIENT')

    HOSTNAME = "http://localhost"    # used in the email send to user

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/flask-app'
    }

    MAIL_FLUSH_INTERVAL = 60  # one minute


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False    # for testing
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/test-temp'
    }


class ProductionConfig(Config):
    MONGO_URI = 'mongodb://admin:admin1234@ds119618.mlab.com:19618/db_todo'


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,

    'default': DevelopmentConfig
}
