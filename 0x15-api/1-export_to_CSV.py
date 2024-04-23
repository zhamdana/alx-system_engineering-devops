#!/usr/bin/python3
"""This module is in charge of making the connection with the api and
    export the information about a employee TODO list progress to csv."""
from sys import argv
import csv
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


def to_csv(employee_id, employee_name, tasks):
    """This method is responsible for exporting the information to csv format.

    Args:
        employee_id (int): User identifier number.
        employee_name (str): Username.
        tasks (list): List of users tasks.
    """
    with open("{}.csv".format(employee_id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id, employee_name,
                             task.get("completed"), task.get("title")])


def main_function(employee_id):
    """This method is in charge of processing the task and user
        dictionaries to convert to useful information.

    Args:
        employee_id (int): User identifier number.
    """
    tasks, user = connection(employee_id)

    if len(tasks) == 0 or len(user) == 0:
        return

    to_csv(employee_id, user.get("username"), tasks)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        main_function(int(argv[1]))
