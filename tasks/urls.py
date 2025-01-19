from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('', TaskListCreate.as_view(), name='task-list-create'),  # List and create tasks
    path('<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),  # Retrieve, update, or delete task by ID
]
