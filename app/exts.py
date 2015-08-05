# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.

__author__ = 'Vito'

from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask_assets import Environment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask.ext.babelex import Babel
from flask_celery import Celery
from flask_admin import Admin
from flask_bootstrap import Bootstrap



# Setup flask cache
cache = Cache()

# init flask assets
assets_env = Environment()

debug_toolbar = DebugToolbarExtension()

migrate = Migrate()

app_admin = Admin()

celery = Celery()

db = SQLAlchemy()

babel = Babel()

bootstrap = Bootstrap()


login_manager = LoginManager()
login_manager.login_view = "auth.admin_login"
login_manager.login_message_category = "warning"
