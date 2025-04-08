# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.MedelSerializer):
    class Meta:
        model = Task
        fields = '__all__' # include all fields from the Task model
