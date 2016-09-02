# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.

__author__ = 'Vito'
from flask import current_app

from celery.signals import task_postrun, worker_process_init

from app import db


@worker_process_init.connect
def worker_bootstrap(**_):
    db.init_app(current_app)


@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()
