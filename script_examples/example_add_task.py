from helper_functions import obtain_token, get_tasks, post_task

USERNAME = 'newuser'
PASSWORD = 'password123'

def main():

    # Obtain the token
    token_response = obtain_token(USERNAME, PASSWORD)
    print('Obtain Token Response:', token_response.json())
    access_token = token_response.json().get('access_token')

    # Define new task data
    data_dict = {
        'title': 'New Task',
        'description': 'This another new task',
        'priority': 'High',
        'deadline': '2021-12-31T23:59:59Z',
        'status': 'Pending'
    }

    # Create new task
    if access_token:
        response = post_task(access_token, data_dict)
        print('Status Code:', response.status_code)
        print('Create Task Response:', response.json())
   
    # Get the tasks
    if access_token:
        response = get_tasks(access_token)
        print('Status Code:', response.status_code)
        print('Get Tasks Response:', response.json())

if __name__ == "__main__":
    main()