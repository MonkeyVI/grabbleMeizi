# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask import Blueprint

from .. import app_admin as admin_ext
from flask.ext.babel import lazy_gettext
from app import db
from app.admin.auth_admin import UserAdmin
from app.admin.configuration_admin import ConfigurationAdmin
from app.admin.storage_admin import StorageAdmin
from app.auth.models import AdminUser
from app.configuration.models import Configuration
from app.storage.models import Storage

__author__ = 'Vito'

admin = Blueprint('admin', __name__)

# 初始化基于model的Admin
admin_ext.add_view(UserAdmin(name=lazy_gettext('User'), model=AdminUser, session=db.session))
admin_ext.add_view(
    ConfigurationAdmin(name=lazy_gettext('Configuration'), model=Configuration, session=db.session))

admin_ext.add_view(StorageAdmin(name=lazy_gettext('Storage'), model=Storage, session=db.session))

# 初始化基于view的Admin
# admin_ext.add_view(ConfigAdmin(name=lazy_gettext('Config')))
