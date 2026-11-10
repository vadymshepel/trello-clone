import os
from celery import Celery
from celery.schedules import crontab

# Меняем 'trello_clone.settings' на 'config.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Меняем имя приложения Celery на 'config' (или оставляй любое, но лучше по имени папки)
app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'check-deadlines-every-hour': {
        'task': 'boards.tasks.check_task_deadlines',
        'schedule': crontab(minute=0),
    },
}
app.conf.timezone = 'Europe/Berlin'

app.autodiscover_tasks()
