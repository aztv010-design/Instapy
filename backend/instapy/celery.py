import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instapy.settings')

app = Celery('instapy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'analyze-profiles-daily': {
        'task': 'instapy.celery_tasks.analyze_profile',
        'schedule': crontab(hour=0, minute=0),
    },
}
