#!/usr/bin/python3

import requests
import sys
import json


if __name__ == '__main__':
    userId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + userId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {userId: []}
    for task in tasks:
        dictionary[userId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(userId), 'w') as filename:
        json.dump(dictionary, filename)
