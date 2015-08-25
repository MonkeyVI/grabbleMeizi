# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.
import os
import os.path as op

__author__ = 'Vito'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = op.dirname(__file__) + '/app/static/images'


class Config(object):
    """
        基本配置
    """

    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'UTC+8:00'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alibabahesishidadao'

    FLASK_MAIL_SUBJECT_PREFIX = ''
    FLASK_MAIL_SENDER = 'pastedmemory@gmail.com'

    MAIL_SENDER = 'SendCloud'
    SEND_CLOUD_API_USER = 'WenKeFei_test_Bxk0NG'
    SEND_CLOUD_API_KEY = 'AkIPNXW3QFRbGZS8'
    SEND_CLOUD_URL = 'http://sendcloud.sohu.com/webapi/mail.send.json'

    # celery
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('tasks',)
    CELERY_DEFAULT_QUEUE = "as-vip-default"

    CELERY_BROKER_URL = 'redis://{}'.format(os.environ.get('REDIS_URI', 'localhost:6379/0'))
    CELERY_IGNORE_RESULT = True

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'STAGING_DATABASE_URI') or 'mysql://root:@localhost:3308/grabble'

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('grabbleMeiZi@163.com')
    MAIL_PASSWORD = os.environ.get('meng1989q')
    SQLALCHEMY_ECHO = True


class StagingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'STAGING_DATABASE_URI') or 'mysql://root:@localhost:3308/grabble'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging import FileHandler

        syslog_handler = FileHandler(os.path.join(config.BASEDIR, 'logs/staging.log'))
        syslog_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(syslog_handler)


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'STAGING_DATABASE_URI') or 'mysql://root:@localhost:3308/grabble'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'staging': StagingConfig,
}
