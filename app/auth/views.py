# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from _curses import flash
from gettext import gettext

from flask import session
import flask
from flask.ext.login import login_required
from flask import url_for, redirect
from flask_login import login_user
from werkzeug.contrib.jsrouting import render_template
from app import db

from app.auth import auth
from app.auth.forms import LoginForm
from app.auth.models import AdminUser

__author__ = 'Vito'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return ''

@auth.route('/logout')
@login_required
def logout():
    # logout_user()
    session.clear()
    return redirect(url_for('main.index'))
