import os

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [1] Show [2] Add [3] Remove [4] Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter a task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == '3':
            show_tasks(tasks)
            num = input("Enter task number to remove: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
