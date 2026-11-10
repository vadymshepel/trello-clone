from django.contrib import admin
from .models import Project, ProjectMembership, Board, Column, Task

class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMembership
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description')
    inlines = [ProjectMembershipInline]

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'position')
    list_filter = ('project',)

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'position')
    list_filter = ('board__project', 'board')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'assignsee', 'priority', 'due_date')
    list_filter = ('priority', 'column__board__project')
    search_fields = ('title', 'description')
