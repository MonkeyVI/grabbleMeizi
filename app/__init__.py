# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.
from config import config

__author__ = 'Vito'

from flask import Flask, current_app
from app.exts import cache, celery, db, debug_toolbar, babel, migrate, assets_env, app_admin, \
    bootstrap, login_manager


@babel.localeselector
def get_locale():
    return 'zh_CN'


def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app_admin.init_app(app)
    babel.init_app(app)
    bootstrap.init_app(app)

    db.init_app(app)
    with app.app_context():
        print current_app.name
        db.create_all()
    # login_manager.init_app(app)

    app_admin.base_template = 'layout.html'

    from main import main as main_blueprint
    from admin import admin as admin_blueprint
    from auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    import os.path

    _dir = os.path.dirname(os.path.abspath(__file__))
    app.template_folder = os.path.join(_dir, 'templates')
    app.static_folder = os.path.join(_dir, 'static')

    return app
