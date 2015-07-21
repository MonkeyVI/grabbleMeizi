# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask import current_app
from flask.ext.login import UserMixin
from app import db, login_manager
from app.core.modles import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

__author__ = 'Vito'


class AdminUser(UserMixin, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), primary_key=True)
    user_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean, default=False)
    administer = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(AdminUser, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def can(self, action=None, module=None):
    #     if self.administer:
    #         return True
    #     if self.role is not None:
    #         for permission in self.role.permission:
    #             if permission.module.name == module:
    #                 if action == 'view':
    #                     return permission.view
    #                 elif action == 'edit':
    #                     return permission.edit
    #                 elif action == 'create':
    #                     return permission.create
    #                 elif action == 'delete':
    #                     return permission.delete
    #                 elif action == 'sync':
    #                     return permission.sync_order
    #                 elif action == 'cancel':
    #                     return permission.cancel_order
    #     return False

    def is_administrator(self):
        return self.administer

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'admin-confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False

        if data.get('admin-confirm') != self.id:
            return False
        self.admin_confirmed = True
        db.session.add(self)
        return True

    def is_authenticated(self):
        if not self.confirmed:
            return False
        return super(AdminUser, self).is_authenticated()

    def __repr__(self):
        return self.user_name


@login_manager.user_loader
def load_user(user_id):
    return AdminUser.query.get(int(user_id))
