#!/usr/bin/python3
"""
script to export data in the CSV format.
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

    user_name = dict_data[0].get('username')

    todos_url = "{}/todos?userId={}".format(url, argv[1])
    with urlopen(todos_url) as response:
        decode_data = response.read().decode("utf-8")
        to_dict_data = json.loads(decode_data)

    csv_data = ''
    for task in to_dict_data:
        csv_data += '"{}","{}","{}","{}"\n'.format(
            task.get("userId"), user_name,
            task.get('completed'), task.get('title'))
    with open("{}.csv".format(argv[1]), 'w') as file:
        file.write(csv_data)
