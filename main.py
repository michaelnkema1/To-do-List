import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Save and Exit")

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = [task.strip() for task in file.readlines()]
    else:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

# Function to display tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("NO TASK ADDED")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function
def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
