from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet, ProjectMembershipViewSet,
    BoardViewSet, ColumnViewSet, TaskViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'memberships', ProjectMembershipViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
