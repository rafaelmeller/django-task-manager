from rest_framework import serializers
from .models import Task

# Placeholder for Task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Use all fields from the Task model
