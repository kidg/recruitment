# -*- coding: utf-8 -*-
__author__ = 'RedWall'

from celery import shared_task
from .dingtalk import send

@shared_task
def send_dingtalk_message(msg):
    send(msg)