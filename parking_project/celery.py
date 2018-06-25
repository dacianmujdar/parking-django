from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.app.control import Control

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parking_project.settings')

from django.conf import settings  # noqa

app = Celery('parking_project')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


# Used for revoking tasks.
control = Control(app)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from celery.contrib import rdb

@app.task
def test():
    rdb.set_trace()
    print('done')