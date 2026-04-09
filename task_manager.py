import os

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, priority = line.strip().split(",")
                tasks.append({"name": name, "priority": priority})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['priority']}\n")

def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({"name": name, "priority": priority})
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    name = input("Enter task name to remove: ")
    for task in tasks:
        if task["name"].lower() == name.lower():
            tasks.remove(task)
            save_tasks(tasks)
            print("Task removed successfully!")
            return
    print("Task not found")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - Priority: {task['priority']}")

def recommend_task(tasks):
    for task in tasks:
        if task["priority"].lower() == "high":
            print("Recommended Task:", task["name"])
            return
    print("No high priority tasks available.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1.Add 2.Remove 3.List 4.Recommend 5.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            recommend_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()