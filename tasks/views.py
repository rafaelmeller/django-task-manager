from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

# View to list all tasks or create a new task
class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer  # Use the TaskSerializer for this view
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]  # Ensure the user is authenticated and has the correct scope

    def get_queryset(self):
        # Return tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the task with the authenticated user as the owner
        serializer.save(user=self.request.user)

# View to retrieve, update, or delete a specific task
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer  # Use the TaskSerializer for this view
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]  # Ensure the user is authenticated and has the correct scope

    def get_queryset(self):
        # Return tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save()
        return Response({"message": "Task updated successfully"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['priority', 'status', 'deadline']  # Allows filtering by priority & status
    search_fields = ['title', 'description']  # Enables searching by keywords

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer