"""
Simple Task Manager CLI Application
"""

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task"""
        self.tasks.append({"task": task, "completed": False})

    def list_tasks(self):
        """List all tasks"""
        if not self.tasks:
            print("No tasks available.")
            return
        
        for i, t in enumerate(self.tasks, 1):
            status = "✔" if t["completed"] else "✘"
            print(f"{i}. {t['task']} [{status}]")

    def complete_task(self, index):
        """Mark a task as completed"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task number")


def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            index = int(input("Enter task number: ")) - 1
            manager.complete_task(index)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()