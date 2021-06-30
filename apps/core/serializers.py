from rest_framework.serializers import ModelSerializer

from .models import Task, Comment


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'text', 'completed']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'task', 'text']
