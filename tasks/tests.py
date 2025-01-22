from django.test import TestCase
from .models import Task
from django.utils import timezone


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            priority=1,
            deadline=timezone.now(),
            status="pending"
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.status, "pending")