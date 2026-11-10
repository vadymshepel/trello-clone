from rest_framework import serializers
from .models import Project, ProjectMembership, Board, Column, Task

class ProjectMembershipSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ProjectMembership
        fields = ['id', 'user', 'username', 'role', 'joined_at']


class ProjectSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    memberships = ProjectMembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'owner_username', 'created_at', 'memberships']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'project', 'position']


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'title', 'board', 'position']


class TaskSerializer(serializers.ModelSerializer):
    assignsee_username = serializers.ReadOnlyField(source='assignsee.username', allow_null=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'column', 
            'assignsee', 'assignsee_username', 'priority', 
            'due_date', 'created_at'
        ]
