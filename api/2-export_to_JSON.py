#!/usr/bin/python3
"""
Exports an employee's TODO list data to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./2-export_to_JSON.py <employee_id>")

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    username = user.get("username")

    data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)
