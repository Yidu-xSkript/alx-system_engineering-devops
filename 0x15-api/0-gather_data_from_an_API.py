#!/usr/bin/python3
"""API req to return todo list."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    tasks = [ta.get("title") for ta in todos if ta.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(tasks), len(todos)))
    [print("\t {}".format(task)) for task in tasks]
