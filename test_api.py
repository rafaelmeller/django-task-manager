import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

if __name__ == '__main__':
   
    # User credentials
    USERNAME = 'newuser2'
    PASSWORD = 'password123'

    # Obtain the token
    register_user(USERNAME, PASSWORD)
    token_response = obtain_token(USERNAME, PASSWORD)
    access_token = token_response.get('access_token')

    # Get the tasks
    if access_token:
        get_tasks(access_token)