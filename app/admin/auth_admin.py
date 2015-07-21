# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask.ext.babelex import lazy_gettext
from app.core.modles import BaseModelView

__author__ = 'Vito'


class UserAdmin(BaseModelView):
    column_labels = {
        'created_at': lazy_gettext('Created At'),
        'updated_at': lazy_gettext('Updated At'),
        'email': lazy_gettext('Email'),
        'user_name': lazy_gettext('User Name'),
        'confirmed': lazy_gettext('Confirmed'),
        'administer': lazy_gettext('Administer'),
    }

    form_excluded_columns = ('password_hash',)
    column_exclude_list = ('password_hash',)
