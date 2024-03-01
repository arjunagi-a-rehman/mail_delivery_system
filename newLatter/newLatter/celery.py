# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu.utils.url import safequote


aws_access_key = safequote("AKIAQEPSLLLX2JSZOC77")
aws_secret_key = safequote("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")

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newLatter.settings')

app = Celery('newLatter',broker=broker_url)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
