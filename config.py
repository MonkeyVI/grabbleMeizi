# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.
import os

__author__ = 'Vito'


class Config(object):
    ABEL_DEFAULT_LOCALE = 'zh_CN'
    BABEL_DEFAULT_TIMEZONE = 'UTC+8:00'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alibabahesishidadao'

    FLASK_MAIL_SUBJECT_PREFIX = ''
    FLASK_MAIL_SENDER = 'pastedmemory@gmail.com'

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
