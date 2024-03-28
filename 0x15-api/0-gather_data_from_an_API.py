#!/usr/bin/python3
"""Returns to-do list progress for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_task = [t.get("title") for t in todos if t.get("completed_task") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_task), len(todos)))
    [print("\t {}".format(c)) for c in completed_task]
