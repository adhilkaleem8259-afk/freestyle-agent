from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import MINIMAL
import logging

console = Console()

class TerminalUI:
    def __init__(self, commands):
        self.commands = commands

    def show_main_menu(self):
        table = Table(show_header=False, box=MINIMAL)
        table.add_column("Option", justify="center", width=12)
        table.add_column("Action", justify="left", width=25)

        table.add_row("[cyan]1[/]", "Add Task")
        table.add_row("[cyan]2[/]", "Show Tasks")
        table.add_row("[cyan]3[/]", "Summarize Tasks")
        table.add_row("[cyan]4[/]", "Categorize Task")
        table.add_row("[red]exit[/]", "Quit Agent")

        console.print(Panel(table, title="🎯 Freestyle Agent Menu", padding=(0,2)))

    def handle_choice(self, choice):
        if choice == "1":
            task = input("Enter your task: ")
            self.commands.add_task(task)
        elif choice == "2":
            self.show_tasks()
        elif choice == "3":
            self.show_summary()
        elif choice == "4":
            self.categorize_task()
        else:
            console.print("[red]Invalid choice[/]")
            logging.warning(f"Invalid menu choice: {choice}")

    def show_tasks(self):
        tasks = self.commands.show_tasks()
        if not tasks:
            console.print("[yellow]No tasks found[/]")
            return

        table = Table(show_header=False, box=MINIMAL)
        table.add_column("No.", width=4)
        table.add_column("Task", overflow="fold")
        for i, t in enumerate(tasks, 1):
            table.add_row(str(i), t)
        console.print(Panel(table, title="📝 Your Tasks", padding=(0,1)))

    def show_summary(self):
        tasks = self.commands.show_tasks()
        if not tasks:
            console.print("[yellow]No tasks[/]")
            return

        table = Table(show_header=False, box=MINIMAL)
        for i, t in enumerate(tasks, 1):
            table.add_row(f"Task {i}:", t)
        console.print(Panel(table, title="📌 Task Summary", padding=(0,1), style="green"))

    def categorize_task(self):
        task = input("Enter task to categorize: ")
        category = self.commands.categorize_task(task)
        console.print(Panel(f"[bold]{task}[/] → [cyan]{category}[/]",
                            title="🗂 Task Category", padding=(0,1)))
