# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/5/15.
from flask.ext.babel import lazy_gettext
from app.core.modles import BaseModelView

__author__ = 'Vito'


class ConfigurationAdmin(BaseModelView):
    column_labels = {
        'created_at': lazy_gettext('Created At'),
        'updated_at': lazy_gettext('Updated At'),
        'name': lazy_gettext('Name'),
        'description': lazy_gettext('Description'),
        'image_class': lazy_gettext('Image Class'),
        'name_class': lazy_gettext('Name Class'),
        '': lazy_gettext(''),

    }
    pass
