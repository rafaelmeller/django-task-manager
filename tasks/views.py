from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# View to list all tasks or create a new task
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()  # Get all tasks
    serializer_class = TaskSerializer  # Use the TaskSerializer for this view

# View to retrieve, update, or delete a specific task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()  # Get a single task based on ID
    serializer_class = TaskSerializer  # Use the TaskSerializer for this view
