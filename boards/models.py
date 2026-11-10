from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """Проект (контейнер для досок и задач)"""
    title = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="owned_projects", 
        verbose_name="Владелец"
    )
    members = models.ManyToManyField(
        User, 
        through='ProjectMembership', 
        related_name="projects", 
        verbose_name="Участники"
    )

    def __str__(self):
        return self.title


class ProjectMembership(models.Model):
    """Промежуточная таблица для связи пользователей и проектов с указанием роли"""
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('member', 'Участник'),
        ('viewer', 'Наблюдатель'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_memberships',
        verbose_name='Пользователь',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='memberships',
        verbose_name='Проект',
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member', verbose_name="Роль")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} -> {self.project} ({self.get_role_display()})"


class Board(models.Model):
    """Доска внутри проекта (например, 'Спринт 1', 'Разработка')"""
    title = models.CharField(max_length=255, verbose_name="Название доски")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="boards", verbose_name="Проект")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиция")

    def __str__(self):
        return f"{self.project.title} -> {self.title}"


class Column(models.Model):
    """Колонка на доске (например, 'Backlog', 'In Progress', 'Done')"""
    title = models.CharField(max_length=100, verbose_name="Название колонки")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="columns", verbose_name="Доска")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиция")

    def __str__(self):
        return f"{self.board.title} [{self.title}]"


class Task(models.Model):
    """Задача (карточка)"""
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    title = models.CharField(max_length=255, verbose_name="Заголовок задачи")
    description = models.TextField(blank=True, verbose_name="Описание")
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="tasks", verbose_name="Колонка")
    assignsee = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="assigned_tasks", 
        verbose_name="Исполнитель"
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Приоритет")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Срок выполнения (Дедлайн)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
