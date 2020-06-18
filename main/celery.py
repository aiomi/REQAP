from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default django settings module for the `celery` program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.local_settings')

app = Celery('main')

# Using a string here means the worker doesn't have to serialize
# the configuration the object to child processes.
# - namepsace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
