import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nirva.settings')

app = Celery('nirva')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'dispatch_offers': {
        'task': 'smsHandler.tasks.dispatch_offers',
        'schedule': 18.0,  # 1800.0
    },
    'expiry_switch': {
        'task': 'smsHandler.tasks.expiry_switch',
        'schedule': 21600.0,  # 21600.0
    },
}