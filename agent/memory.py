import json
import os

class MemoryManager:
    def __init__(self, filename="user_history.json"):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump({"tasks": []}, f)

    def get_tasks(self):
        with open(self.filename, "r") as f:
            return json.load(f).get("tasks", [])

    def add_task(self, task):
        tasks = self.get_tasks()
        tasks.append({"task": task, "agent": "Unassigned"})
        self.save_tasks(tasks)

    def save_tasks(self, tasks):
        with open(self.filename, "w") as f:
            json.dump({"tasks": tasks}, f, indent=2)
