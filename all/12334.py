# def task():
    # tasks =[]#empty list
    # print("----WELCOME TO THE TASK MANNAGEMENT APP----")

    # total_task =int(input("Enter how many tast you want to add="))#5
    # for i in range (1, total_task+1):
    #     task_name =input(f"enter task{i} = ")#enter task 3 =
    #     tasks.append(task_name)

    
    # print(f"today's task are\n{tasks}")
    
    # while True:
    #         operation = int(input("enter 1-add\nd-update\n3-delete\n4-view\n5-exit/stop/"))
    #         if operation ==1:
    #              add = input("enter task you want to add = ")
    #              task.append(add)
    #              print(f"task {add} has been successfull added...")
    #         elif operation == 2:
    #              updated_val = input ("enter the task name you want to update =")
    #              if updated_val in tasks:
    #                   up = input("enter new task =")
    #                   ind = task.index(updated_val)#2
    #                   tasks [ind]=up
    #                   print(f"updated task {up}")
    #         elif operation == 3:
    #              del_val =input("which task you want to delete")
    #              if del_val in tasks:
    #                   ind = tasks.index (del_val)
    #                   del tasks[ind]
    #                   print(f"task{del_val} has been deleted...")
    #         elif operation ==4:
    #              print(f"total tasks = {tasks}")

    #         elif operation == 5:
    #              print("closing the program....")
    #              break
            
    #         else: 
    #              print("invalid input")




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

# # Run the task manager
# task_manager()


