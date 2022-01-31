#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee
    ID, returns information about his/her TODO list progress.
"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get('{}/users/{}'.format(url, sys.argv[1])).json()
    todo_res = requests.get('{}/todos?userId={}'.format(
        url, sys.argv[1])).json()

    with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
        fieldnames = ["userId", "id", "completed", "title"]

        writer = csv.DictWriter(
                csvfile, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)

        for row in todo_res:
            row['id'] = "Antonette"
            writer.writerow(row)
