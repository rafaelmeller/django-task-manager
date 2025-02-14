from helper_functions import obtain_token, get_tasks, post_task

USERNAME = 'newuser3'
PASSWORD = 'password123'

def main():

    # Obtain the token
    token_response = obtain_token(USERNAME, PASSWORD)
    access_token = token_response.get('access_token')

    # Define new task data
    data_dict = {
        'title': 'New Task',
        'description': 'This is a new task',
        'priority': 'Low',
        'deadline': '2021-12-31T23:59:59Z',
        'status': 'Pending'
    }

    # Create new task
    if access_token:
        post_task(access_token, data_dict)
   
    # Get the tasks
    if access_token:
        get_tasks(access_token)

if __name__ == "__main__":
    main()