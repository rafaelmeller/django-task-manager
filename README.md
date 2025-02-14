# Task Manager API

**IMPORTANT: THIS README IS STILL BEING DEVELOPED AND MAY CONTAIN INCOMPLETE OR INACCURATE INFORMATION.**

TODO: ADD BADGES

_Other versions:_
[_Clique aqui para Português_](./translations/README-ptBR.md) - TODO

<h4 align="center"> 
     Status: In development 🚧
</h4>

<p align="center">
 <a href="#about">About</a> •
 <a href="#features">Features</a> •
 <a href="#demonstration">Demonstration</a> •
 <a href="#architecture">Application Architecture</a> •
 <a href="#api-endpoints">API Endpoints</a> •
 <a href="#setup">Setup</a>  • 
 <a href="#author">Author</a> • 
 <a href="#license">License</a>
</p>

## About ℹ️
The Task Manager API is a Django-based application designed to help users manage their tasks efficiently. It provides endpoints for creating, reading, updating, and deleting tasks, as well as user registration and authentication. The API supports OAuth2 for secure authentication and authorization.

## Features 💻
- User registration and authentication using OAuth2.
- Create, read, update, and delete tasks.
- Assign attributes like title, description, priority, deadline, and status to each task.
- Secure API endpoints with token-based authentication.
- Detailed API documentation for easy integration.

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
| <kbd>POST /register</kbd>     | register users (username and password) [response details](#register-user)
| <kbd>POST /o/token</kbd>     | requests an access token for the user [request details](#request-token)

<h3 id="register-user">POST /register</h3>

**RESPONSE**
```json
{
  TODO,
}
```

<h3 id="request-token">POST /o/token</h3>

**REQUEST**
```json
{
    "grant_type": "password",
    "username": "your-username",
    "password": "your-password",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
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
