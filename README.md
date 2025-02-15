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
The Task Manager API is a Django-based application designed to help users manage their tasks efficiently. It provides endpoints for creating, reading, updating, and deleting tasks, as well as user registration and authentication. The API supports OAuth2 for secure authentication and authorization.

## Features 💻
- User registration and authentication using OAuth2.
- Create, read, update, and delete tasks.
- Assign the attributes title, description, priority, deadline, and status to each task.
- Secure API endpoints with token-based authentication.

## Project Demonstration 🖥️
TODO

## Application Architecture 🏗️

The Task Manager API is built using Django and Django REST framework. The application follows a modular architecture with the following main components:

- **Models**: Define the structure of the database tables. The main model is the `Task` model, which includes fields for title, description, priority, deadline, status, and user association.
- **Serializers**: Convert model instances to JSON format and validate incoming data.
- **Views**: Handle the business logic and interact with the models and serializers. The main views include task creation, retrieval, update, and deletion, as well as user registration.
- **URLs**: Route incoming HTTP requests to the appropriate views.
- **Authentication**: Uses OAuth2 for secure authentication and authorization. The `AccessToken` model is used to manage tokens.

### Data Flow

1. **User Registration**: Users can register by providing a username and password.
2. **Authentication**: Users obtain an access token by providing their credentials.
3. **Task Management**: Authenticated users can create, read, update, and delete tasks.

### Database Design

- **User**: Standard Django user model for authentication.
- **Task**: Model to store task details, including title, description, priority, deadline, status, and user association.

### Main Modules

- **tasks/models.py**: Defines the `Task` model.
- **tasks/serializers.py**: Defines the `TaskSerializer`.
- **tasks/views.py**: Contains views for task management and user registration.
- **tasks/urls.py**: Routes for task-related endpoints.
- **task_manager/urls.py**: Main URL configuration, including authentication routes.

## API Endpoints 📍

This is the list of the API routes and the expected JSONs.
​
| Route                 | Description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /register/</kbd>     | register users (username and password) [response details](#register-user)
| <kbd>POST /o/token/</kbd>     | requests an access token for a specific user [request details](#request-token)
| <kbd>POST /api/tasks/</kbd>     | creates a new task for a specifir user [response details](#post-task)
| <kbd>GET /api/tasks/</kbd>     | gets all the tasks of a specific user [response details](#get-tasks)

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
  "Authorization': f'Bearer your-access-token-here"
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
  "Authorization': f'Bearer your-access-token-here"
}
```

**RESPONSE**
```json
[  
  {"id": 1, "title": "New Task", "description": "This is a new task", "priority": "Low", "deadline": "2021-12-31", "status": "Pending", "created_at": "2025-02-15T11:44:35.155255Z", "updated_at": "2025-02-15T11:44:35.155284Z", "user": 4},
  {"id": 2, "title": "New Task", "description": "This is another task", "priority": "Low", "deadline": "2021-12-31", "status": "Pending", "created_at": "2025-02-15T11:49:44.762223Z", "updated_at": "2025-02-15T11:49:44.762251Z", "user": 4}
]
```

## Setup ⚙️
```bash
python3 exemplo.py
```

## Author 👨🏻‍💻

This project was designed and developed by **Rafael Meller**.

[![Linkedin Badge](https://img.shields.io/badge/-Rafael_Meller-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafaelmeller/)](https://www.linkedin.com/in/rafaelmeller/) 
[![Gmail Badge](https://img.shields.io/badge/-rafaelmeller.dev@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=rafaelmeller.dev@gmail.com)](mailto:rafaelmeller.dev@gmail.com)
#
## License 📝

This project is licensed under the [MIT](./LICENSE) license.
