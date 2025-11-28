class TODO_app:
    def __init__(self,filename = "Task.txt"):
        self.filename = filename
        self.Mytasks = []
        self.load_tasks()

    def add_task(self):
        Task = str(input("Type your task: ")).strip()
        if Task and Task not in self.Mytasks:
            self.Mytasks.append(Task)
            self.save_task()
            print(f"{Task} added")
        else:
            print("This task is already added")

    def mark_completed(self):
        self.remove_task("mark as complete")

    def view_task(self):
        if len(self.Mytasks) == 0:
            print("Your list is empty")
            return
        for slno,task in enumerate(self.Mytasks, start = 1):
            print(f"{slno}. {task}")

    def remove_task(self,action = "remove"):
        self.view_task()
        to_remove = str(input(f"which task do you want to {action}: ")).strip()
        if to_remove in self.Mytasks:
            self.Mytasks.remove(to_remove)
            self.save_task()
            print(f"'{to_remove}' {action}d")
        else:
            print("no such task in your todo list")

    def load_tasks(self):
        self.Mytasks.clear()
        try:
            with open(self.filename,'r') as file:
                for line in file:
                    self.Mytasks.append(line.strip())
        except FileNotFoundError:
            open(self.file.name,'w').close()

    def save_task(self):
        with open(self.filename,'w') as file:
            for task in self.Mytasks:
                file.write(f"{task}\n")

    def run(self):
        while True:
            choice = str(input("what you wanna do (add, done, view, remove, exit)\n\t")).strip().lower()
            if choice == "add":
                self.add_task()
            elif choice == "remove":
                self.remove_task()
            elif choice == "view":
                self.view_task()
            elif choice == "done":
                self.mark_completed()
            elif choice == "exit":
                break
            else:
                print("invalid input. try again")

if __name__ == "__main__":
    app = TODO_app()
    app.run()