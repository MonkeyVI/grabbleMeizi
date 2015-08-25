# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 8/5/15.
from app import db
from app.core.modles import BaseModel

__author__ = 'Vito'


class Configuration(BaseModel):
    __tablename__ = 'configurations'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    image_class = db.Column(db.String(255))

    name_class = db.Column(db.String(255))

    def __repr__(self):
        return self.name
