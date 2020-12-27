# -*- coding: utf-8 -*-
__author__ = 'RedWall'
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append('G:/python/recruitment/')
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from celery1.task import add

result = add.delay(4,4)
print("Is task ready: %s" % result.ready())

#注释了这两行，celery -A task worker 才能启动
run_result = result.get(timeout=1)
print("task result: %s" % run_result)