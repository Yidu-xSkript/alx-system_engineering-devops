#!/usr/bin/python3
"""Export todo list to JSON."""
import sys
import requests
import json

if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonFormat:
        json.dump({userId: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in todos]}, jsonFormat)
