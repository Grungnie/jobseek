# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings
#
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobseek.settings')
# app = Celery('jobseek',
#              broker='amqp://guest@localhost//',)
#
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
# app.conf.update(
#     CELERY_WORKER_DIRECT=True,
#     CELERY_TASK_RESULT_EXPIRES=3600,
#     CELERY_RESULT_BACKEND='amqp://',
#     CELERY_ACCEPT_CONTENT = ['json',],
#     CELERY_TASK_SERIALIZER = 'json',
#     CELERY_RESULT_SERIALIZER = 'json',
# )


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
)