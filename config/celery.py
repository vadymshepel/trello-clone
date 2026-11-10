import os
from celery import Celery

# Указываем настройки Django по умолчанию (замени 'trello_clone' на реальное имя твоей папки с проектом, если оно отличается)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trello_clone.settings')

app = Celery('trello_clone')

# Читаем конфигурацию из settings.py с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим файлы tasks.py во всех приложениях Django
app.autodiscover_tasks()
