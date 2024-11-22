from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_subscription.settings')

app = Celery('celery_subscription')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
