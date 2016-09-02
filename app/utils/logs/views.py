# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.
import os
import logging

__author__ = 'Vito'


def get_file_logger(name, format_msg='%(asctime)s %(levelname)s\n%(message)s\n',
                    level=logging.DEBUG):
    log = logging.getLogger(name)
    if not log.handlers:
        handler = logging.FileHandler('%s/logs/%s.log' % (os.getcwd(), name))
        formatter = logging.Formatter(format_msg)
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(level)
    return log
