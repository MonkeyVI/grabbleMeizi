# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from flask import render_template
from app.main import main

__author__ = 'Vito'

@main.route('/')
def index():
    return render_template('index.html')
