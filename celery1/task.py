# -*- coding: utf-8 -*-
__author__ = 'RedWall'

from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379',
             include=["run_task"]
             )

@app.task
def add(x, y):
    return x + y

# result = add.delay(4,4)
# print(result.wait())