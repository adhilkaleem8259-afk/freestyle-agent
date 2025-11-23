class CommandHandler:
    def __init__(self, memory, llm):
        self.memory = memory
        self.llm = llm

    def add_task(self, task):
        self.memory.add_task(task)

    def show_tasks(self):
        tasks = self.memory.get_tasks()
        for t in tasks:
            if 'agent' not in t:
                t['agent'] = "Unassigned"
        return tasks

    def assign_task(self, task_index, agent_name):
        tasks = self.memory.get_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index]['agent'] = agent_name
            self.memory.save_tasks(tasks)
