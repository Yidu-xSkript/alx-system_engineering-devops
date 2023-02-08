#!/usr/bin/python3
"""Exports todo list to CSV."""
import sys
import requests
import csv

if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as todo_csv:
        csvFormat = csv.writer(todo_csv, quoting=csv.QUOTE_ALL)
        [csvFormat.writerow(
            [userId, user.get("username"), t.get("completed"), t.get("title")]
         ) for t in todos]
