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


def task_manager():
    tasks = []  # empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are: {tasks}")

    while True:
        operation = input("Enter 1 to add\n2 to update\n3 to delete\n4 to view\n5 to exit: ")

        if operation == '1':
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == '2':
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                new_task = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print(f"Updated task: {new_task}")
            else:
                print("Task not found.")

        elif operation == '3':
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted...")
            else:
                print("Task not found.")

        elif operation == '4':
            print(f"Total tasks: {tasks}")

        elif operation == '5':
            print("Closing the program...")
            break

        else:
            print("Invalid option. Please try again.")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          