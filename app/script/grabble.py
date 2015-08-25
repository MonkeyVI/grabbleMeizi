# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/7/15.
import time
import os.path as op
import cStringIO
import urllib2

import requests
from lxml import etree

from PIL import Image

from app import db
from app.storage.models import Storage
from app.utils.common.views import make_md5
from app.utils.logs.views import get_file_logger
from config import PROJECT_ROOT

__author__ = 'Vito'

log = get_file_logger('spider_web')


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


class SpiderWeb(object):
    def __init__(self):
        pass

    @staticmethod
    def get_html(url='', headers=None, cookies=None, timeout=30, auth=None):
        """
        :param url: 目标url
        :param cookies: 浏览器 cookies
        :param timeout: 超时时间
        :param auth: 用户名密码 eg. auth=('user', 'pass')
        :param headers: 浏览器 headers
        :return: 目标url的html 内容
        """
        try:
            r = requests.get(url, cookies=cookies, timeout=timeout, auth=auth, headers=headers)
            html = r.text
        except Exception, e:
            log.error(e)
            return ''
        return html

    @classmethod
    def run(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4)' \
                     ' AppleWebKit/537.36 (KHTML, like Gecko)' \
                     ' Chrome/44.0.2403.130 Safari/537.36'
        headers = {"User-Agent": user_agent}
        for i in range(0, 100, 18):
            url = 'http://www.douban.com/photos/album/134725479/?start={count}'.format(count=i)
            content = self.get_html(url=url, headers=headers)
            tree = etree.HTML(content)
            nodes = tree.xpath("//div[@class='photo_wrap']")
            for n in nodes:
                src = n.find('a')[0].items()[0][1]

                title = 'DB 美女'
                image_src = save_image(src, title=title)
                url = n.find('a').items()[0][1]
                storage = Storage()
                storage.title = title
                storage.image_url = image_src
                storage.url = url
                db.session.add(storage)
                db.session.commit()
