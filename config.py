# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.
import os

__author__ = 'Vito'


class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'UTC+8:00'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alibabahesishidadao'

    FLASK_MAIL_SUBJECT_PREFIX = ''
    FLASK_MAIL_SENDER = 'pastedmemory@gmail.com'

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
