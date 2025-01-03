from django.db import models

# My models
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)  # Short title for the task
    description = models.TextField(blank=True, null=True)  # Optional longer description
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')  # Priority of the task
    deadline = models.DateField()  # Deadline for the task
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # Status of the task
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set when task is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto set when task is updated

    def __str__(self):
        return self.title  # String representation of the task