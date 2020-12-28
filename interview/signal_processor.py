# -*- coding: utf-8 -*-
__author__ = 'RedWall'
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Candidate
from interview.dingtalk import send

import json, logging
logger = logging.getLogger(__name__)

@receiver(signal=post_save, sender=Candidate, dispatch_uid='candidate_post_save_dispatcher')
def post_save_callback(sender, instance=None, created=False, **kwargs):
    msg = ""
    if isinstance(instance,Candidate):
        msg = "Candidate for {0} has been saved".format(instance.username)
    print(msg)
    logger.info(msg)
    # send(msg)