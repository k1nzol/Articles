from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'articles.settings')

app = Celery('articles')
app.conf.enable_utc = False

app.conf.update(timezone = "Australia/Tasmania")

app.config_from_object(settings, namespace="CELERY")

# Celery beat settings

app.conf.beat_schedule = {
    'publication_new_article': {
        'task': 'paper.tasks.publish_articles',
        'schedule': crontab(),
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')