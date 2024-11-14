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









# To-Do List App in Python

# Task class to hold task details
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

# ToDoList class to manage the list of tasks
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f'Task "{description}" added.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task.description}" removed.')
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f'Task "{self.tasks[index].description}" marked as completed.')
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        print()

# Main function to run the To-Do List App
def main():
    todo_list = ToDoList()

    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show All Tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.show_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            todo_list.show_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
