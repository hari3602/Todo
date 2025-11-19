def add():
    Task = str(input("Type your task: "))
    if Task not in Mylist:
        Mylist.append(Task)
        print(f"{Task} added")
    else:
        print("this task is already added")

def completed():
    remove("mark as completed")

def view():
    if len(Mylist) == 0:
        print("Your list is empty")
    for slno,task in enumerate(Mylist, start = 1):
        print(f"{slno}. {task}")

def remove(remove):
    view()
    to_remove = str(input(f"which task do you want to {remove}: "))
    if to_remove in Mylist:
        Mylist.remove(to_remove)
    else:
        print("no such task in your todo list")

Mylist = []

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