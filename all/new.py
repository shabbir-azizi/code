# A list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" deleted.')
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: add, view, delete, exit")
    option = input("Choose an option: ").lower()

    if option == "add":
        task = input("Enter task: ")
        add_task(task)
    elif option == "view":
        view_tasks()
    elif option == "delete":
        view_tasks()
        task_number = int(input("Enter task number to delete: "))
        delete_task(task_number)
    elif option == "exit":
        break
    else:
        print("Invalid option. Try again.")
