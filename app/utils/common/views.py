# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/21/15.
import hashlib
import json
import requests
from flask import render_template, current_app, Response
from flask.ext.mail import Message, Mail

__author__ = 'Vito'


def make_resp(token='', json_info={}, code=200, error=''):
    resp = Response()
    if json_info:
        resp.set_data(json.dumps(json_info))
    if error:
        resp.headers.add('error-message', error)
    if token:
        resp.headers.add('x-access-token', token)
    resp.headers.add('Content-Type', 'application/json')
    resp.status_code = code
    return resp


def send_email(to, from_email, from_name, subject, template, files='', **kwargs):
    html = render_template(template + '.html', **kwargs)
    if current_app.config['MAIL_SENDER'] == 'SendCloud':

        sc_url = current_app.config['SEND_CLOUD_URL']
        api_user = current_app.config['SEND_CLOUD_API_USER']
        api_key = current_app.config['SEND_CLOUD_API_KEY']
        params = {
            'api_user': api_user,
            'api_key': api_key,
            'to': to,
            'from': from_email,
            'fromname': from_name,
            'subject': subject,
            'html': html
        }

        r = requests.post(sc_url, files=files, data=params)
        # @todo: check the status
        print r.text
    else:
        msg = Message(current_app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                      sender=from_email, recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = html
        with current_app.app_context():
            mail = Mail(current_app)
            mail.send(msg)


def make_md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest().upper()
