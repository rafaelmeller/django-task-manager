from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

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

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)