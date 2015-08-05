# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/17/15.

__author__ = 'Vito'

from app.exts import cache, celery, db, debug_toolbar, babel, migrate, assets_env, app_admin, \
    bootstrap, login_manager

from config import config

from flask import Flask, current_app, redirect, url_for
from flask_admin import AdminIndexView, Admin
from flask_login import current_user

class admin_index_view(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.confirmed

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.admin_login'))

app_admin = Admin(index_view=admin_index_view())

@babel.localeselector
def get_locale():
    return 'zh_CN'


def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app_admin.init_app(app)
    babel.init_app(app)
    celery.init_app(app)
    bootstrap.init_app(app)

    db.init_app(app)
    with app.app_context():
        print current_app.name
        db.create_all()
    login_manager.init_app(app)

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
