from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta


@periodic_task(run_every=(timedelta(seconds=20)), name='FT')
def my_first_task():
    print('This is my first task')


@shared_task
def my_second_task():
    print('This is my second task')


@shared_task
def my_third_task():
    print('This is my third task')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
