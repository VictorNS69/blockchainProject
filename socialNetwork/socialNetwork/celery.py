from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os

REDIS_URL = settings.REDIS_URL

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialNetwork.settings')
app = Celery('socialNetwork')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    BROKER_URL=REDIS_URL,
)
