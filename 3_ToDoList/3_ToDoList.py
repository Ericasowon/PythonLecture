# Goal
# Add, delete, and view to-do tasks
# Execute desired task based on menu selection
# Include an option to exit

# Concepts used
# list (to store tasks), while True: (loop), input() (user input)
# if-elif-else (conditional branching)


todo_list = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose a menu number: ")

    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"✅ '{task}' has been added.")

    elif choice == '2':
        if not todo_list:
            print("❗ There are no tasks to delete.")
            continue
        for i, task in enumerate(todo_list, start =1):
            print(f"{i}. {task}")
        try:
            num = int(input("Enter the number of the task to delete: "))
            removed = todo_list.pop(num-1)
            print(f"🗑️ '{removed}'has been deleted.")
        except (ValueError, IndexError):
            print("❗ Please enter a valid number.")

    elif choice == '3':
        if not todo_list:
            print("🕊️ There are no tasks at the moment.")
        else:
            print("\n📌 Current To-Do List: ")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif choice == '4':
        print("👋 Exiting the program.")
        break

    else:
        print("❗ Please enter a valid menu number.")
