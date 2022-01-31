#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee
    ID, returns information about his/her TODO list progress.
"""
import requests
import json
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get('{}/users/{}'.format(url, sys.argv[1])).json()
    todo_res = requests.get('{}/todos?userId={}'.format(
        url, sys.argv[1])).json()

    def task_completed(todo_res):
        """
            Return task completed
        """
        count = 0
        for value in todo_res:
            if value['completed']:
                count += 1
        return count

    print("Employee {} is done with tasks({}/{}):".format(
        user_res['name'], task_completed(todo_res), len(todo_res)))
    for listdict in todo_res:
        if listdict['completed']:
            print("\t{ }".format(listdict['title']))
