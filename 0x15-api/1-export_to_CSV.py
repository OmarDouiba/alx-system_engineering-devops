#!/usr/bin/python3
"""
text
"""
if __name__ == "__main__":
    import csv
    import json
    from sys import argv
    from urllib.request import urlopen

    url = 'https://jsonplaceholder.typicode.com'
    users_url = "{}/users?id={}".format(url, argv[1])

    with urlopen(users_url) as response:
        str_data = response.read().decode("utf-8")
        dict_data = json.loads(str_data)

    EMPLOYEE_NAME = dict_data[0].get('name')

    todos_url = "{}/todos?userId={}".format(url, argv[1])
    with urlopen(todos_url) as response:
        decode_data = response.read().decode("utf-8")
        to_dict_data = json.loads(decode_data)

    csv_data = ''
    for task in to_dict_data:
        csv_data += '"{}", "{}", "{}", "{}"\n'.format(
            task.get("userId"), EMPLOYEE_NAME,
            task.get('completed'), task.get('title'))
    with open("{}.csv".format(argv[1]), 'w') as file:
        file.write(csv_data)
