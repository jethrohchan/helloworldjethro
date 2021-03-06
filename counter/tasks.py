
import logging
import os
from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import Counter
from django.conf import settings
from celery import shared_task


logger = logging.getLogger(__name__)

# @app.task(bind=True)
@task(name="increment")
def increment():
    # increment counter here per visit and save it back into db
    logger.info('Calling Async Increment')
    try:
        counter, created = Counter.objects.get_or_create(id=1)
        counter.visits += 1
        counter.save()
        logger.info('Incrementing Async to ${0}'.format(counter.visits))
    except Exception as e:
        logger.critical(e)

# @task(name="auto_runtime")
@shared_task
def auto_runtime():
    logger.info('Calling Auto Runtime')
    try:
        counter, created = Counter.objects.get_or_create(id=1)
        counter.runtimes += 1
        counter.save()
        logger.info('Auto Runtime to ${0}'.format(counter.runtimes))
    except Exception as e:
        logger.critical(e)
