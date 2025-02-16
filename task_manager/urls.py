"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from tasks.views import UserRegistrationView


def api_root(request):
    return JsonResponse({"message": "Welcome to the Task Manager API"})

urlpatterns = [
    path('', api_root),  # Add a response for the root URL
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),  # Placeholder for tasks app routes
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # Include OAuth2 provider routes
    path('register/', UserRegistrationView.as_view(), name='user-registration'),  # Registration endpoint
]
