# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.


from flask.ext.babelex import lazy_gettext
from app.auth.modles import AdminUser

__author__ = 'Vito'

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Email, Required, Length, Regexp, EqualTo


class LoginForm(Form):
    email = StringField(lazy_gettext('Email'), validators=[Required(), Length(1, 64), Email()])

    password = PasswordField(lazy_gettext('Password'), validators=[Required()])
    remember_me = BooleanField(lazy_gettext('Keep me logged in'))
    submit = SubmitField(lazy_gettext('Log In'))


class RegistrationForm(Form):
    email = StringField(lazy_gettext('Email'), validators=[Required(), Length(1, 50), Email()])
    username = StringField(lazy_gettext('Username'), validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, lazy_gettext(
            'Usernames must have letter, numbers, dots or underscores'))
    ])

    password = PasswordField(lazy_gettext('Password'), validators=[
        Required(), EqualTo('password2', message=lazy_gettext('Password must match.'))
    ])

    password2 = PasswordField(lazy_gettext('Confirm password'), validators=[Required()])
    submit = SubmitField(lazy_gettext('Register'))

    def validate_email(self, field):
        if AdminUser.query.filter_by(email=field.data).first():
            raise ValidationError(lazy_gettext('Email already registered.'))

            # def validate_username(self, field):
            # if User.query.filter_by(username=field.data).first():
            #         raise ValidationError(lazy_gettext('Username already in use.'))
