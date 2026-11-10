from rest_framework import viewsets, permissions  # type: ignore[reportMissingImports]
from django.shortcuts import render

from .models import Project, ProjectMembership, Board, Column, Task
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    ProjectSerializer, ProjectMembershipSerializer,
    BoardSerializer, ColumnSerializer, TaskSerializer
)


def home_view(request):
    return render(request, 'index.html')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Автоматически назначаем текущего авторизованного пользователя владельцем проекта
        serializer.save(owner=self.request.user)


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
