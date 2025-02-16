<h1 align="center" style="font-weight: bold;">Task Manager API</h1>

<h4 align="center"> IMPORTANT: This README is still being developed and may contain incomplete or inaccurate information.</h4>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Python Badge">
  <img src="https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white&style=for-the-badge" alt="Django Badge">
  
</div>

#

_Other versions:_
[_Clique aqui para Português_](./translations/README-ptBR.md) - TODO

<h4 align="center"> 
     Status: In development 🚧
</h4>

<p align="center">
 <a href="#about-ℹ️">About</a> •
 <a href="#features-💻">Features</a> •
 <a href="#project-demonstration-🖥️">Demonstration</a> •
 <a href="#application-architecture-🏗️">Application Architecture</a> •
 <a href="#api-endpoints-📍">API Endpoints</a> •
 <a href="#setup-⚙️">Setup</a>  • 
 <a href="#author-👨🏻‍💻">Author</a> • 
 <a href="#license-📝">License</a>
</p>

## About ℹ️
This project is a **personal learning exercise** focused on **building a Django REST API** while applying best practices like **pagination, filtering, searching, and OAuth authentication**.

The API allows users to **manage tasks**, including:
- Creating, updating, retrieving, and deleting tasks.
- Filtering tasks by priority, status, and deadline.
- Searching tasks by title or description.
- Authenticating users using **OAuth2 token-based authentication**.

Additionally, a helper script (`helper_functions.py`, inside the script_examples directory) provides **examples of API interactions via Python**, demonstrating how to make authenticated requests for querying and managing tasks programmatically.

## Features 💻
- **OAuth2 authentication**: Secure access to the API using token-based authentication.
- **Task management endpoints**: Supports full CRUD operations (Create, Read, Update, Delete).
- **Filtering & Searching**: Query tasks based on priority, status, deadline, and text search.
- **Pagination**: Ensures efficient handling of large datasets.

## Project Demonstration 🖥️
TODO

## Application Architecture 🏗️

The Task Manager API is built using Django and Django REST framework. The application follows a modular architecture with the following main components:

- **Models**: Define the structure of the database tables. The main model is the `Task` model, which includes fields for title, description, priority, deadline, status, and user association.
- **Serializers**: Convert model instances to JSON format and validate incoming data.
- **Views**: Handle the business logic and interact with the models and serializers. The main views include task creation, retrieval, update, and deletion, as well as user registration.
- **URLs**: Route incoming HTTP requests to the appropriate views.
- **Authentication**: Uses OAuth2 for secure authentication and authorization.

### Data Flow

1. **User Registration**: Users can register by providing a username and password.
2. **Authentication**: Users obtain an access token by providing their credentials.
3. **Task Management**: Authenticated users can create, read, update, and delete tasks.

## API Endpoints 📍

This is the list of the API routes and the expected JSONs.
​
| Route                 | Description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /register/</kbd>     | register users (username and password) [details](#register-user)
| <kbd>POST /o/token/</kbd>     | requests an access token for a user [details](#request-token)
| <kbd>POST /api/tasks/</kbd>     | creates a new task for a user [details](#post-task)
| <kbd>GET /api/tasks/</kbd>     | gets all the tasks from a user [details](#get-tasks)
| <kbd>GET /api/tasks/?param=value</kbd>     | filters tasks with a specific parameter from a user [details](#filter-tasks)
| <kbd>GET /api/tasks/{id}/</kbd>     | gets a task with a specific id from a specific user [details](#get-task-id)
| <kbd>PUT /api/tasks/{id}/</kbd>     | updates a task with a specific id from a specific user [details](#put-task)
| <kbd>DELETE /api/tasks/{id}/</kbd>     | deletes a task with a specific id from a specific user [details](#delete-task)


<h3 id="register-user">POST /register/</h3>

**RESPONSE**
```json
{
  TODO,
}
```

<h3 id="request-token">POST /o/token/</h3>

**REQUEST**
***Data***
```json
{
  "grant_type": "password",
  "username": "your-username-here",
  "password": "your-password-here",
  "client_id": "your-client-id-here",
  "client_secret": "your-client-secret-here"
}
```

**RESPONSE**
```json
{
  "access_token": "9Lcvhiy108thwJzjTSdyisWMv06XsM", 
  "expires_in": 36000, 
  "token_type": "Bearer", 
  "scope": "read write", 
  "refresh_token": "QY8MHHiNaK7JzsXqzuo5YKt3dBckjI"
}
```

<h3 id="post-tasks">POST /api/tasks/</h3>

**REQUEST:**

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

***Data***
```json
{
  "title": "New Task",
  "description": "This is another task",
  "priority": "Low",
  "deadline": "2021-12-31",
  "status": "Pending",
}
```

**RESPONSE**
```json
{
  "id": 2,
  "title": "New Task",
  "description": "This is another task",
  "priority": "Low",
  "deadline": "2021-12-31",
  "status": "Pending",
  "created_at": "2025-02-15T11:49:44.762223Z",
  "updated_at": "2025-02-15T11:49:44.762251Z",
  "user": 4
}
```

<h3 id="get-tasks">GET /api/tasks/</h3>

**REQUEST:**

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

**RESPONSE**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "New Task",
      "description": "This is a new task",
      "priority": "Low",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-15T11:44:35.155255Z",
      "updated_at": "2025-02-15T11:44:35.155284Z",
      "user": 2
    },
    {
      "id": 2,
      "title": "New Task",
      "description": "This is another task",
      "priority": "Low",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-15T11:49:44.762223Z",
      "updated_at": "2025-02-15T11:49:44.762251Z",
      "user": 2
    },
    {
      "id": 3,
      "title": "New Task",
      "description": "This is another new task",
      "priority": "High",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-16T11:17:00.685599Z",
      "updated_at": "2025-02-16T11:17:00.685657Z",
      "user": 2
    }
  ]
}
```
<h3 id="filter-tasks">GET /api/tasks/?param=value</h3>

**REQUEST:**

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

**Query Parameters**
| Parameter          | Type                 | Description                                          
|-----------|---------------|--------------------------------------
search | str | Search for tasks by title or description
priority | str | Filter by priority (Low, Medium, High)
status | str | Filter by status (Pending, Completed)
deadline | date |	Filter tasks by deadline (YYYY-MM-DD format)

**Request URL examples:**

#### ```GET /api/tasks/?search=payment```
#### ```GET /api/tasks/?priority=High```
#### ```GET /api/tasks/?status=Pending```
#### ```GET /api/tasks/?deadline=2025-05-01```
#### ```GET /api/tasks/?priority=High&status=Pending&deadline=2025-05-01```





#### Note: All parameters are optional—you can provide one, multiple, or none at all.


## Setup ⚙️

To run the project locally:

```bash
# Clone the repository
git clone <repo-url>

# Navigate to project folder
cd task_manager

# Create a virtual environment
python3 -m venv .venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations to create necessary tables
python manage.py migrate

# (Optional) Create a superuser to access the Django admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## Author 👨🏻‍💻

This project was designed and developed by **Rafael Meller**.

[![Linkedin Badge](https://img.shields.io/badge/-Rafael_Meller-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafaelmeller/)](https://www.linkedin.com/in/rafaelmeller/) 
[![Gmail Badge](https://img.shields.io/badge/-rafaelmeller.dev@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=rafaelmeller.dev@gmail.com)](mailto:rafaelmeller.dev@gmail.com)
#
## License 📝

This project is licensed under the [MIT](./LICENSE) license.
