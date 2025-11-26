import os

def add():
    read_task()
    Task = str(input("Type your task: "))
    if Task not in Mylist:
        Mylist.append(Task)
        write_task()
        print(f"{Task} added")
    else:
        print("this task is already added")

def completed():
    remove("mark as completed")

def view():
    read_task()
    if len(Mylist) == 0:
        print("Your list is empty")
        return
    for slno,task in enumerate(Mylist, start = 1):
        print(f"{slno}. {task}")

def remove(remove):
    view()
    to_remove = str(input(f"which task do you want to {remove}: "))
    if to_remove in Mylist:
        Mylist.remove(to_remove)
        write_task()
    else:
        print("no such task in your todo list")

Mylist = []
def read_task():
    Mylist.clear()
    with open("Task.txt",'r') as file:
        for line in file:
            Mylist.append(line.strip())
    return Mylist

def write_task():
    with open("Task.txt",'w') as file:
        for task in Mylist:
            file.write(f"{task}\n")
    
if os.path.exists("Task.txt") is False:
    with open("Task.txt",'w') as file:
        pass
    
while True:
    choice = str(input("what you wanna do (add, done, view, remove, exit)\n\t"))
    if choice == "add":
        add()
    elif choice == "remove":
        remove("remove")
    elif choice == "view":
        view()
    elif choice == "done":
        completed()
    elif choice == "exit":
        break
    else:
        print("invalid input. try again")