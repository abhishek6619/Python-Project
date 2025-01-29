import json

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks, 1):
        status = "[Done]" if task["done"] else "[Pending]"
        print(f"{i}. {status} {task['task']}")


def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                task_number = int(input("Enter task number to mark as done: "))
                mark_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
