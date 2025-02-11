import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file in the main folder
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Base URL of the local server
BASE_URL = 'http://localhost:8000'

# Register a new user
def register_user(username, password):
    url = f'{BASE_URL}/register/'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=data)
    print('Register User Response:', response.json())
    return response

# Obtain OAuth2 token
def obtain_token(username, password):
    url = f'{BASE_URL}/o/token/'
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET')
    }
    response = requests.post(url, data=data)
    print('Obtain Token Response:', response.json())
    return response.json()

# Get tasks
def get_tasks(access_token):
    url = f'{BASE_URL}/api/tasks/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    print('Get Tasks Response:', response.json())
    return response

# Create a new task
def post_task(access_token, data_dict):
    url = f'{BASE_URL}/api/tasks/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': data_dict['title'],
        'description': data_dict['description'],
        'priority': data_dict['priority'],
        'deadline': data_dict['deadline'],
        'status': data_dict['status']
    }
    response = requests.post(url, headers=headers, json=data)
    print('Post Task Response:', response.json())
    return response

# Update an existing task
def put_task(access_token, task_id, data_dict):
    url = f'{BASE_URL}/api/tasks/{task_id}/'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': data_dict['title'],
        'description': data_dict['description'],
        'priority': data_dict['priority'],
        'deadline': data_dict['deadline'],
        'status': data_dict['status']
    }
    response = requests.put(url, headers=headers, json=data)
    print('Put Task Response:', response.json())
    return response

# Delete a task
def delete_task(access_token, task_id):
    url = f'{BASE_URL}/api/tasks/{task_id}/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.delete(url, headers=headers)
    print('Delete Task Response:', response.json() if response.content else {"message": "Task deleted successfully"})
    return response