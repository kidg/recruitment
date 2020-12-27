# -*- coding: utf-8 -*-
__author__ = 'RedWall'
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')

app = Celery('recruitment')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab

#配置
from recruitment.tasks import add
#方法1
app.conf.beat_schedule = {
    'add-every-10-seconds':{
        'task' : 'recruitment.tasks.add',
        'schedule' : 10.0,
        'args' : (16, 4),
    },
}

#方法2
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name='hello every 10')

    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

#方法3 ：后台配置

#方法4：
# import json
# from django_celery_beat.models import PeriodicTask, IntervalSchedule

# 先创建定时策略
# schedule, created = IntervalSchedule.objects.get_or_create(every=15, period=IntervalSchedule.SECONDS)

#在创建任务
# task = PeriodicTask.objects.create(interval=schedule, name='say welcome 2020', task='recruitment.celery.test', args=json.dumps(['welcome']),)
