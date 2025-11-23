import asyncio
import logging

class ParallelAgent:
    def __init__(self, name, bus, commands):
        self.name = name
        self.bus = bus
        self.commands = commands

    async def run(self):
        while True:
            tasks = self.commands.show_tasks()
            # Pick all unassigned tasks at once
            unassigned = [(idx, t) for idx, t in enumerate(tasks) if t['agent'] == "Unassigned"]
            for idx, t in unassigned:
                self.commands.assign_task(idx, self.name)
                logging.info(f"[{self.name}] Assigned task '{t['task']}'")
                # Simulate work concurrently
                asyncio.create_task(self.complete_task(idx, t['task']))
            await asyncio.sleep(3)

    async def complete_task(self, idx, task_name):
        await asyncio.sleep(2)  # simulate work
        logging.info(f"[{self.name}] Completed task '{task_name}'")
        self.commands.assign_task(idx, f"{self.name} ✅")
