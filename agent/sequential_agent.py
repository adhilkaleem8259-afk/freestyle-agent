import asyncio
import logging

class SequentialAgent:
    def __init__(self, name, bus, commands):
        self.name = name
        self.bus = bus
        self.commands = commands

    async def run(self):
        while True:
            tasks = self.commands.show_tasks()
            # Pick the first unassigned task
            for idx, t in enumerate(tasks):
                if t['agent'] == "Unassigned":
                    self.commands.assign_task(idx, self.name)
                    logging.info(f"[{self.name}] Assigned task '{t['task']}'")
                    # Simulate work sequentially
                    await asyncio.sleep(2)
                    logging.info(f"[{self.name}] Completed task '{t['task']}'")
                    self.commands.assign_task(idx, f"{self.name} ✅")
                    break  # Only pick one task at a time
            await asyncio.sleep(1)
