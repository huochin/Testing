def showMenu():
    print("""\nTo-do List:\n
          1. Add Task\n
          2. View All Task\n
          3. Mark Task As Done\n
          4. Delete Task\n
          5. Quit Program\n""")

tasks = []

while True:
    showMenu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        task_desc = input("Enter task description: ").strip()
        if task_desc:
            tasks.append({'task': task_desc, 'done': False})
            print("Task added.")
        else:
            print("Task description cannot be empty.")
    elif choice == '2':
        if not tasks:
            print("No tasks to show.")
        else:
            print("\nAll Tasks:")
            for idx, t in enumerate(tasks, 1):
                status = "Done" if t['done'] else "Not Done"
                print(f"{idx}. {t['task']} [{status}]")
    elif choice == '3':
        if not tasks:
            print("No tasks to mark as done.")
        else:
            for idx, t in enumerate(tasks, 1):
                status = "Done" if t['done'] else "Not Done"
                print(f"{idx}. {t['task']} [{status}]")
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]['done'] = True
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        if not tasks:
            print("No tasks to delete.")
        else:
            for idx, t in enumerate(tasks, 1):
                status = "Done" if t['done'] else "Not Done"
                print(f"{idx}. {t['task']} [{status}]")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    print(f"Deleted task: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '5':
        print("Quitting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")