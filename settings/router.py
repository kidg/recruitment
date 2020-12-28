# -*- coding: utf-8 -*-
__author__ = 'RedWall'

import logging

logger = logging.getLogger(__name__)

class DatabaseRouter:
    route_app_labels = {'slave'}

    def db_for_read(self, model, **hints):
        # if model._meta.app_label in self.route_app_labels:
        logger.info ("%s db_for_read record" %(model))
        return 'slave'
        # return 'default'

    def db_for_write(self, model, **hints):
        logger.info ("%s db_for_write record" %(model))
        return 'default'