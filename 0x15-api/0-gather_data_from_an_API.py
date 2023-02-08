#!/usr/bin/python3
"""API req to return todo list."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    tasks = []
    for i in todos:
        if i.get("completed") is True:
            tasks.append(i.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(tasks), len(todos)))
    [print("\t {}".format(task)) for task in tasks]
