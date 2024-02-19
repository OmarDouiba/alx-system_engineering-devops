#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    import json
    from sys import argv
    from urllib.request import urlopen

    url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users?id={}'.format(url, argv[1])

    with urlopen(users_url) as response:
        str_data = response.read().decode("utf-8")
        dict_data = json.loads(str_data)

    EMPLOYEE_NAME = dict_data[0].get('name')

    todos_url = '{}/todos?userId={}'.format(url, argv[1])
    with urlopen(todos_url) as response:
        str_todos_data = response.read().decode('utf-8')
        dict_todos_data = json.loads(str_todos_data)

    TOTAL_NUMBER_OF_TASKS = len(dict_todos_data)
    NUMBER_OF_DONE_TASKS = 0

    for task in dict_todos_data:
        if task.get('completed'):
            NUMBER_OF_DONE_TASKS += 1

    titles = []
    for task in dict_todos_data:
        if task.get('completed'):
            titles.append("\t {}".format(task.get('title')))

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))

    for title in titles:
        print(title)
