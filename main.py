tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")


def delete_task(task):
    tasks.remove(task)
    print(f"Deleted task: {task}")


def view_tasks():
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


def main_menu():
    while True:
        print("\nTo-Do List")
        print("---------")
        print("1. Add task")
        print("2. Delete task")
        print("3. View tasks")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            task = input("Enter the number of the task to delete: ")
            delete_task(tasks[int(task)-1])
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


main_menu()
