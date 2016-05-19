from __future__ import absolute_import
from celery import Celery
from kombu import Queue

app = Celery('jobseek',
             broker='amqp://guest@localhost//',
             include=['worker.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_WORKER_DIRECT=True,
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_RESULT_BACKEND='amqp://',
    CELERY_DEFAULT_QUEUE = 'general',
    CELERY_QUEUES = (
        Queue('general', routing_key='general'),
    ),
    CELERY_ACCEPT_CONTENT = ['json','pickle'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',

    # Set timezone
    CELERY_ENABLE_UTC = True,
    TIME_ZONE = 'Australia/Brisbane',
    USE_TZ = True,

    # Fix timeout issues
    CELERY_ACKS_LATE = True,
    CELERYD_PREFETCH_MULTIPLIER = 1,
)