from celery import shared_task
from django.utils import timezone
from .models import Task
import logging

logger = logging.getLogger(__name__)

@shared_task
def check_task_deadlines():
    """
    Фоновая задача: проверяет задачи с приближающимся или наступившим дедлайном
    и симулирует отправку уведомлений.
    """
    now = timezone.now()
    # Находим задачи, у которых есть дедлайн, он уже наступил, а они еще актуальны
    # (для примера возьмем те, у которых due_date меньше текущего времени)
    overdue_tasks = Task.objects.filter(due_date__lte=now)
    
    count = overdue_tasks.count()
    if count > 0:
        logger.warning(f"⚠️ Внимание! Найдено просроченных задач: {count}")
        for task in overdue_tasks:
            # Здесь в будущем будет логика отправки email через send_mail()
            assignee_name = task.assignsee.username if task.assignsee else "Не назначен"
            logger.info(f"-> Уведомление по задаче '{task.title}' (Исполнитель: {assignee_name}) просрочена!")
    else:
        logger.info("✅ Проверка дедлайнов: просроченных задач нет.")

    return f"Проверено задач с дедлайнами: {Task.objects.count()}. Просрочено: {count}."
