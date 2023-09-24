# To-Do-List
This Python application demonstrates the Memento Design Pattern to manage tasks. Users can add, mark tasks as completed, delete tasks, undo previous actions, and view tasks based on their completion status. This readme file provides an overview of the code structure and how to use the application.

## Code Structure
The code is organized into several classes:

1.) TaskDetails: Represents the state of a task with attributes like description, due_date, and completed.

2.) Operations: A builder class for constructing tasks with optional attributes such as due_date and completed.

3.) Task: Represents a task with attributes like description, due_date, and completed. It also has a __str__ method for string representation.

4.) TaskList: Manages a list of tasks and provides operations for adding, marking tasks as completed, deleting tasks, undoing actions, and viewing tasks.

## How to Use the Application

#### Adding a Task:
Choose option 1.
Enter the task description.
Optionally, enter the due date in the format DD-MM.
The task will be added to the task list.

#### Marking a Task as Completed:
Choose option 2.
Enter the task description you want to mark as completed.
The task's status will be updated to "Completed."

#### Deleting a Task:
Choose option 3.
Enter the task description you want to delete.
The task will be removed from the task list.

#### Undoing an Action:
Choose option 4.
The most recent action (addition, completion, or deletion) will be undone.

#### Viewing Tasks:
Choose option 5.
Enter one of the filter types: "all," "completed," or "pending."
The tasks matching the filter criteria will be displayed.

#### Exiting the Application:
Choose option 6 to exit the application.

## Summary
The application uses a pattern to store the state of tasks, allowing users to undo actions.<br>
Task descriptions are used as unique identifiers.<br>
Due dates are optional, and tasks can be marked as completed or pending.<br>
Users can view tasks based on their completion status.<br>
The application continues to run until the user chooses to exit<br>
