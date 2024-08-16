import sys

# Initialize an empty list to store tasks
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['description']} - [{status}]")
    print("\n")

def add_task(description):
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f"Added task: '{description}'\n")

def complete_task(task_number):
    try:
        tasks[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed.\n")
    except IndexError:
        print("Invalid task number.\n")

def main():
    while True:
        print("To-Do List Application")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task_description = input("Enter the task description: ")
            add_task(task_description)
        elif choice == '3':
            show_tasks()
            task_number = int(input("Enter the task number to complete: "))
            complete_task(task_number)
        elif choice == '4':
            print("Exiting To-Do List application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
