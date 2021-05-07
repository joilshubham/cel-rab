from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from . import celeryconfig

from celery import bootsteps
from kombu import Consumer, Exchange, Queue


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_main.settings')
app = Celery('app_main', broker='pyamqp://guest@localhost//')
app.config_from_object(celeryconfig)


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


my_queue = Queue('celery', Exchange('celery'), 'routing_key')


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()
app.steps['consumer'].add(MyConsumerStep)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))