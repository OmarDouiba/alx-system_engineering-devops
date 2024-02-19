#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv
    import json

    url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users?id={}'.format(url, argv[1])

    with urlopen(users_url) as response:
        str_data = response.read().decode("utf-8")
        dict_data = json.loads(str_data)

    employee_name = dict_data[0].get('name')

    todos_url = '{}/todos?userId={}'.format(url, argv[1])
    with urlopen(todos_url) as response:
        str_todos_data = response.read().decode('utf-8')
        dict_todos_data = json.loads(str_todos_data)

    num_tasks = len(dict_todos_data)
    num_tasks_completed = 0

    for task in dict_todos_data:
        if task.get('completed'):
            num_tasks_completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_tasks_completed, num_tasks
    ))

    titles = []
    for task in dict_todos_data:
        if task.get('completed'):
            titles.append("\t {}".format(task.get('title')))
    for title in titles:
        print(title)
