from helper_functions import register_user, obtain_token, get_tasks

USERNAME = 'newuser'
PASSWORD = 'password123'

def main():
    # Register the user
    register_user(USERNAME, PASSWORD)

    # Obtain the token
    token_response = obtain_token(USERNAME, PASSWORD)
    access_token = token_response.json().get('access_token')

    # Get the tasks
    if access_token:
        response = get_tasks(access_token)
        print('Status Code:', response.status_code)
        print('Get Tasks Response:', response.json())

if __name__ == "__main__":
    main()