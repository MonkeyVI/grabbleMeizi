# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.

__author__ = 'Vito'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
