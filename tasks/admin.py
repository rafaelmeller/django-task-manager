from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'title', 'priority', 'status', 'deadline', 'created_at')  # Columns shown in the list view
    list_filter = ('user', 'id', 'priority', 'status', 'deadline')  # Adds filtering options
    search_fields = ('title', 'description')  # Enables search by title and description
    ordering = ('user',)  # Sorts by deadline (earliest first)
