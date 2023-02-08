#!/usr/bin/python3
"""Exports todo list of all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    allusers = requests.get(url + "users").json()
    with open("todo_all_empoyees.json", "w") as jsonF:
        for user in allusers:
            tasks = requests.get(url + "todos",
                                 params={"userId": user.get("id")}).json()
            for task in tasks:
                json.dump({
                    user.get("id"): [{
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username")
                    }]
                }, jsonF)
