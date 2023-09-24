class TaskDetails:
    def __init__(self, description, due_date, completed):
        self.description = description
        self.due_date = due_date
        self.completed = completed

class Operations:
    def __init__(self, description):
        self.description = description
        self.due_date = None
        self.completed = False

    def with_due_date(self, due_date):
        self.due_date = due_date
        return self

    def mark_completed(self):
        self.completed = True
        return self

    def build(self):
        return Task(self.description, self.due_date, self.completed)

class Task:
    def __init__(self, description, due_date, completed):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}, Due: {self.due_date}"

class TaskList:
    def __init__(self):
        self.tasks = []
        self.undo_stack = []

    def add_task(self, task):
        self.tasks.append(task)
        self.undo_stack.append(TaskDetails(task.description, task.due_date, task.completed))

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                self.undo_stack.append(TaskDetails(task.description, task.due_date, task.completed))
                return

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                self.undo_stack.append(None)  # To indicate a deleted task
                return

    def undo(self):
        if self.undo_stack:
            detail = self.undo_stack.pop()
            if detail is not None:
                for task in self.tasks:
                    if task.description == detail.description:
                        task.description = detail.description
                        task.due_date = detail.due_date
                        task.completed = detail.completed
                return detail
            else:
                # If a task was deleted, re-add it
                task = Task(detail.description, detail.due_date, detail.completed)
                self.tasks.append(task)
                return self.tasks

    def view_tasks(self, filter_type):
        if filter_type == "all":
            return self.tasks
        elif filter_type == "completed":
            return [task for task in self.tasks if task.completed]
        elif filter_type == "pending":
            return [task for task in self.tasks if not task.completed]
        else:
            return []

if __name__ == "__main__":
    todo_list = TaskList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Completed")
        print("3. Delete Task")
        print("4. Undo")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (DD-MM): ")
            task = Operations(description).with_due_date(due_date).build()
            todo_list.add_task(task)
        elif choice == "2":
            description = input("Enter task description to mark as completed: ")
            todo_list.mark_completed(description)
        elif choice == "3":
            description = input("Enter task description to delete: ")
            todo_list.delete_task(description)
        elif choice == "4":
            print(todo_list.undo())
        elif choice == "5":
            filter_type = input("Enter filter type (all/completed/pending): ")
            tasks = todo_list.view_tasks(filter_type)
            for task in tasks:
                print(task)
        elif choice == "6":
            break
        else:
            print("Enter your choices from 1-6, based on the above description")
