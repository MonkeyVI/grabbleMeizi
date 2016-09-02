# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/7/15.

import requests
from lxml import etree

from app import db
from app.storage.models import Storage
from app.utils.file.views import save_image
from app.utils.logs.views import get_file_logger

__author__ = 'Vito'

log = get_file_logger('spider_web')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/45.0.2454.93 Safari/537.37'


class SpiderWeb(object):
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
    def run(cls, url='', step=18, total=100):
        headers = {"User-Agent": user_agent}
        for i in range(0, total, step):
            url = 'http://www.douban.com/photos/album/134725479/?start={count}'.format(count=i)
            content = cls.get_html(url=url, headers=headers)
            tree = etree.HTML(content)
            nodes = tree.xpath("//div[@class='photo_wrap']")
            for n in nodes:
                source_url = n.find('a').items()[0][1]
                source_content = cls.get_html(source_url, headers=headers)
                source_tree = etree.HTML(source_content)
                source_nodes = source_tree.xpath("//div[@class='image-show-inner']")

                for sn in source_nodes:
                    try:
                        title = sn.find('a').items()[2][1]
                        image_url = sn.find('a').items()[1][1]

                        src = sn.find('a').items()[0][1]
                        image_src = save_image(src, title=title)

                        storage = Storage()
                        storage.title = title
                        storage.image_url = image_src
                        storage.url = image_url
                        db.session.add(storage)
                    except Exception, e:
                        print e
        db.session.commit()
