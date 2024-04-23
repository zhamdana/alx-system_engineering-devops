#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    export the information about all employees TODO list progress to json."""
import json
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


def to_json(dictionary):
    """This method is responsible for exporting the information to json format.

    Args:
        dictionay (dict): All formated information.
    """
    with open("todo_all_employees.json", "w") as file:
        json.dump(dictionary, file)


def main_function():
    """This method is in charge of processing the task and user
        dictionaries to convert to useful information.
    """

    tasks_content, users_content = connection()

    dictionary = {}
    for user in users_content:
        tasks_list = []
        employee_id = user.get("id")
        for task in tasks_content:
            if task.get("userId") == employee_id:
                tasks_list.append({"task": task.get("title"),
                                   "completed": task.get("completed"),
                                   "username": user.get("username")})
        dictionary[employee_id] = tasks_list

    to_json(dictionary)


if __name__ == '__main__':
    main_function()
