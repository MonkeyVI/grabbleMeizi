# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.

__author__ = 'Vito'

from os import path

from flask import current_app
from flask_script import Manager

from celery.bin.beat import beat


class _CeleryCommand(Manager):
    """
    celery command
    """


CeleryCommand = _CeleryCommand()


@CeleryCommand.command
def run_worker():
    """
    celery worker
    """
    with current_app.app_context() as app_context:
        app_context.app.extensions['celery'].celery.worker_main(
            ['worker', '--loglevel=INFO', '--concurrency=20'])


@CeleryCommand.command
def run_beat():
    """
    celery beat
    """
    with current_app.app_context() as context:
        beat(context.app.extensions['celery'].celery).execute_from_commandline(
            argv=['beat', '--loglevel=INFO', '--schedule', path.dirname(__file__) + '/beat.db'])


OrderCeleryCommand = _CeleryCommand()


@OrderCeleryCommand.command
def run_worker():
    """
    order celery worker
    """
    with current_app.app_context() as app_context:
        app_context.app.extensions['order_celery'].celery.worker_main(
            ['worker', '--loglevel=INFO', '--concurrency=20'])
