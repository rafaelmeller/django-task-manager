from helper_functions import register_user, obtain_token, get_tasks

USERNAME = 'newuser4'
PASSWORD = 'password123'

def main():
    # Register the user
    register_user(USERNAME, PASSWORD)

    # Obtain the token
    token_response = obtain_token(USERNAME, PASSWORD)
    access_token = token_response.get('access_token')

    # Get the tasks
    if access_token:
        get_tasks(access_token)

if __name__ == "__main__":
    main()