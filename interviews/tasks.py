from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task

from giterview.celery import app

@shared_task
def add(x, y):
    time.sleep(15)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def say_hello():
    print('hwanil nim hihihi')