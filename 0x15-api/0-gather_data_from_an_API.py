#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    prints information about a employee TODO list progress."""
from sys import argv
import requests


def connection():
    """This method is responsible for making the connection with the api
        and decoding the json format.

    Returns:
        dict: Users and tasks in dictionary format.
    """
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    return tasks.json(), users.json()


def main_function(employee_id):
    """This method is in charge of processing the task and user
        dictionaries to print useful information.

    Args:
        employee_id (int): User identifier number.
    """
    if not employee_id.isdigit():
        return

    employee_id = int(employee_id)
    tasks_content, users_content = connection()

    for user in users_content:
        if user.get("id") == employee_id:
            break
    else:
        return

    total = 0
    completed = []
    for task in tasks_content:
        if task.get("userId") == employee_id:
            total += 1
            if task.get("completed") is True:
                completed.append(task.get("title"))
    if total == 0:
        return

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), total))
    for ctask in completed:
        print("\t {}".format(ctask))


if __name__ == '__main__':
    if len(argv) == 2:
        main_function(argv[1])
