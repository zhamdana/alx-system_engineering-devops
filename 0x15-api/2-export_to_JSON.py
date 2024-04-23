#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    export the information about a employee TODO list progress to json."""
from sys import argv
import json
import requests


def connection(employee_id):
    """This method is responsible for making the connection with the api
        and decoding the json format.

    Returns:
        dict: Users and tasks in dictionary format.
    """
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id))
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id))
    return tasks.json(), users.json()


def to_json(employee_id, employee_username, tasks):
    """This method is responsible for exporting the information to json format.

    Args:
        employee_id (int): User identifier number.
        employee_username (str): Username.
        tasks (dict): User tasks.
    """
    with open("{}.json".format(employee_id), "w") as file:
        tasks_list = []
        for task in tasks:
            tasks_list.append({"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": employee_username})
        dictionary = {}
        dictionary[employee_id] = tasks_list
        json.dump(dictionary, file)


def main_function(employee_id):
    """This method is in charge of processing the task and user
        dictionaries to convert to useful information.

    Args:
        employee_id (int): User identifier number.
    """
    tasks, user = connection(employee_id)

    if len(tasks) == 0 or len(user) == 0:
        return

    to_json(employee_id, user.get("username"), tasks)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        main_function(int(argv[1]))
