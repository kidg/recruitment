# -*- coding: utf-8 -*-
__author__ = 'RedWall'

from .celery import app

@app.task
def add(x, y):
    return x + y