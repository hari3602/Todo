def add():
    Task = str(input("Type your task"))
    Mylist.append(Task)
    print(f"{Task} added")

def mark_as_complete():
    pass

def view():
    pass

def remove():
    pass

Mylist = []
while True:
    choice = str(input("what you wanna do (add, done, view, remove, exit)"))
    if choice == "add":
        add()