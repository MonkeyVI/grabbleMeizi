# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/7/15.
from flask import url_for
from markupsafe import Markup
from app.core.modles import BaseModelView

__author__ = 'Vito'


class StorageAdmin(BaseModelView):
    column_list = ('title', 'image')

    column_formatters = {
        "image": lambda v, c, m, p: Markup("""
        <img src="{img}" width="50px" class="img-circle">""".format(
            img=url_for('static', filename=m.image_url) if bool(m.image_url) else ''))
    }
