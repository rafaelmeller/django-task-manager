from helper_functions import obtain_token, get_tasks

USERNAME = 'newuser3'
PASSWORD = 'password123'

def main():

    # Obtain the token
    token_response = obtain_token(USERNAME, PASSWORD)
    access_token = token_response.get('access_token')

    # Get the tasks
    if access_token:
        get_tasks(access_token)

if __name__ == "__main__":
    main()