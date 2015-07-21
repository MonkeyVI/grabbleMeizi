# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask import Blueprint

from .. import app_admin as admin_ext
from flask.ext.babel import lazy_gettext
from app import db
from app.admin.auth_admin import UserAdmin
from app.auth.modles import AdminUser

__author__ = 'Vito'

admin = Blueprint('admin', __name__)

admin_ext.add_view(UserAdmin(name=lazy_gettext('User'), model=AdminUser, session=db.session))
