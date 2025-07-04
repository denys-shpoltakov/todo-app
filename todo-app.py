tasks = []

def add_task():
    task = input('Enter your task: ')
    tasks.append(task)
    print(f"Task '{task}' added to the list\n")

def list_tasks():
    if not tasks:
        print("=======================\n")
        print("        TASKS : \n")
        print("There is no tasks\n")
    else:
        print("=======================\n")
        print("List of tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}\n")

def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the # to delete: "))
        if task_to_delete >=0:
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed")
        else:
            print(f"Task #{task_to_delete} was not found.")
    except:
        print("Invalid input.")    

def menu():
    print("=======================\n")
    print("[1] Add new task")
    print("[2] Show tasks")
    print("[3] Delete tasks")
    print("[4] Exit a programm\n")
    print("=======================\n")

menu()
option = int(input("Enter your option: "))
print("=======================\n")

while True:
    if option == 1:
        add_task()
    elif option == 2:
        list_tasks()
    elif option == 3:
        delete_task()
    elif option == 4:
        print("Program was closed")
        break
    else:
        print("Option is invalid")
    menu()
    option = int(input("Enter your option: "))