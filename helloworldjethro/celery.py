
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from celery import shared_task
# from counter import add_runtime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworldjethro.settings')
app = Celery('helloworldjethro')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# Celery Beat Stuff
app.conf.beat_schedule = {
    'called-every-5-seconds': {
        'task': 'helloworldjethro.counter.tasks.auto_runtime',
        'schedule': 5.0
     },
}
