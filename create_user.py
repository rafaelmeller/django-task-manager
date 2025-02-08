import os
import django
from django.contrib.auth.models import User

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

# Create a user with ID 1
if not User.objects.filter(id=1).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
    print("User with ID 1 created.")
else:
    print("User with ID 1 already exists.")