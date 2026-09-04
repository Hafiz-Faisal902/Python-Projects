"""A simple in-memory command-line to-do list."""


def show_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\n===== Your Tasks =====")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print("Task added.")


def complete_task(tasks):
    """Mark a task complete by removing it from the active list."""
    if not tasks:
        print("\nNo tasks to complete.")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Task number is out of range.")
        return

    completed = tasks.pop(task_number - 1)
    print(f"Completed: {completed}")


def main():
    """Run the to-do list application."""
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice in {"1", "add"}:
            add_task(tasks)
        elif choice in {"2", "view", "list"}:
            show_tasks(tasks)
        elif choice in {"3", "complete", "done"}:
            complete_task(tasks)
        elif choice in {"4", "exit", "quit"}:
            print("Exiting To-Do List...")
            break
        else:
            print("Invalid choice. Please choose 1-4.")

