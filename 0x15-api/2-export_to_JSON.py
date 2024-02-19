#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    from sys import argv
    from urllib.request import urlopen

    url = 'https://jsonplaceholder.typicode.com'
    users_url = "{}/users?id={}".format(url, argv[1])
    with urlopen(users_url) as response:
        user_str_data = response.read().decode("utf-8")
        user_dict_data = json.loads(user_str_data)
    username = user_dict_data[0].get('username')
    json_dict = {}
    json_list = []

    todos_url = "{}/todos?userId={}".format(url, argv[1])
    with urlopen(todos_url) as response:
        todos_str_data = response.read().decode('utf-8')
        todos_dict_data = json.loads(todos_str_data)

    for user in todos_dict_data:
        json_dict["task"] = user.get("title")
        json_dict["completed"] = user.get("completed")
        json_dict["username"] = username

        json_list.append(json_dict)
        json_dict = {}

    json_new_dict = {}
    json_new_dict[argv[1]] = json_list
    json_to_str = json.dumps(json_new_dict)
    with open("{}.json".format(argv[1]), 'w') as file:
        file.write(json_to_str)
