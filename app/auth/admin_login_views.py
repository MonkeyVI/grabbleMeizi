# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.

from flask import request, url_for, flash, render_template, redirect, current_app
from flask.ext.babelex import gettext
from flask_login import login_user

from app import db
from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app.auth.modles import AdminUser
from app.utils.common.views import send_email

__author__ = 'Vito'


@auth.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """
    内部工作人员登录
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = AdminUser.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect('/admin')
        flash(gettext('Invalid username or password'))
    return render_template('auth/login.html', form=form)


@auth.route('/admin-register', methods=['GET', 'POST'])
def admin_register():
    """
    内部工作人员注册
    :return:
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = AdminUser(email=form.email.data,
                         user_name=form.username.data,
                         password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, current_app.config['FLASK_MAIL_SENDER'],
                   'Admin', gettext('Confirm Your Account'), 'auth/confirm',
                   user=user, token=token, host=request.url_root, name=user.user_name)
        flash(gettext('A confirmation email has been sent to you be email.'))
        return redirect(url_for('auth.admin_login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/', methods=['GET'])
@auth.route('/confirm', methods=['GET'])
def confirm():
    """
    （注册）确定邮件
    :return:
    """
    token = request.args.get('token', '')
    user_id = request.args.get('user_id', '0')
    user = AdminUser.query.filter_by(id=user_id).first()
    if not user:
        return 'Permission denied', 404
    confirm = user.confirm(token)
    if confirm:
        user.admin_confirmed = True
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash(gettext('confirm success'))
    else:
        flash(gettext('confirm fail'))
    return redirect(url_for('auth.admin_login'))
