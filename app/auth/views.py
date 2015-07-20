# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask import session, redirect, url_for
from flask.ext.login import login_required, logout_user
from app.auth import auth

__author__ = 'Vito'


@auth.route('/logout')
@login_required
def logout():
    # logout_user()
    session.clear()
    return redirect(url_for('main.index'))
