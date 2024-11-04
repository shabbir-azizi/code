def task():
    tasks =[]#empty list
    print("----WELCOME TO THE TASK MANNAGEMENT APP----")

    total_task =int(input("Enter how many tast you want to add="))#5
    for i in range (1, total_task+1):
        task_name =input(f"enter task{i} = ")#enter task 3 =
        tasks.append(task_name)

    
    print(f"today's task are\n{tasks}")
    
    while True:
            operation = int(input("enter 1-add\nd-update\n3-delete\n4-view\n5-exit/stop/"))
            if operation ==1:
                 add = input("enter task you want to add = ")
                 task.append(add)
                 print(f"task {add} has been successfull added...")
            elif operation == 2:
                 updated_val = input ("enter the task name you want to update =")
                 if updated_val in tasks:
                      up = input("enter new task =")
                      ind = task.index(updated_val)#2
                      tasks [ind]=up
                      print(f"updated task {up}")
                      


                 