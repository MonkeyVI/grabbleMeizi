# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/7/15.
from app import db
from app.core.modles import BaseModel

__author__ = 'Vito'


class Storage(BaseModel):
    __tablename__ = 'storage'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __repr__(self):
        return self.title
