# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 9/21/15.
import time
import urllib2
import cStringIO
import os.path as op

from PIL import Image
from app.utils.common.views import make_md5
from app.utils.logs.views import get_file_logger
from config import PROJECT_ROOT

__author__ = 'Vito'

log = get_file_logger('file_error')


def save_image(image_url, title='MZ'):
    """
    通过url获取图片并且保存
    :param image_url: 图片url地址
    :param title: 图片标题
    :return: 存在数据库中的名字
    """
    try:
        file = urllib2.urlopen(image_url)
        tmpIm = cStringIO.StringIO(file.read())
        im = Image.open(tmpIm)

        name = make_md5(title + str(time.time())) + '.jpg'
        local_path = op.join(PROJECT_ROOT, name)
        im.save(local_path, 'JPEG')

    except Exception, e:
        log.error(e)

    return 'images/' + name
