import os
import json

def showMenu():
    print("""\nTo-do List:\n
          1. Add Task\n
          2. View All Task\n
          3. Mark Task As Done\n
          4. Delete Task\n
          5. Quit Program\n""")
    
def addTask():
    taskDesc = input("What\'s the task: ").strip()
    tasks.append({'Task' : taskDesc, 'Done' : False})
    print("Task added!")

def viewTask():
    if not tasks:
        print("There's no tasks yet. Go add some task.")
    else:
        print("All task:")
        for idx, t in enumerate(tasks, 1):
            status = "Done" if t['Done'] else "Not Done"
            print(f"{idx:>2}. {t['Task']:<20} [{status}]")

def selectTask():
    while True:
            try:
                taskSelected = int(input("Select task number: "))
                if taskSelected < 1 or taskSelected >= len(tasks) + 1:
                    raise IndexError
                return(taskSelected)
            except:
                print("Please choose a valid task number!")

def markAsDone(taskNumber):
    tasks[taskNumber-1].update({'Done' : True})
    print(f"Task {taskNumber} is done.")

def deleteTask(taskNumber):
    tasks.pop(taskNumber-1)
    print("Task deleted")

def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def loadTasks():
    global tasks    
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

tasks = []
loadTasks()
isrunning = True
choice = 0

while isrunning == True:
    showMenu()
    try:
        choice = int(input("Enter your choice(1-5): "))
        if choice < 1 or choice > 5:
            raise IndexError
    except:
        print("Please put integer 1 to 5")
        continue #skip to next loop to prevent using the old 'choice'
    match choice:
        case 1:
            addTask()
        case 2:
            viewTask()
        case 3:
            viewTask()
            if not tasks:
                pass
            else:
                taskSelected = selectTask()
                markAsDone(taskSelected)
        case 4:
            viewTask()
            if not tasks:
                pass
            else:
                taskSelected = selectTask()
                deleteTask(taskSelected)
        case 5:
            print("Thank you")
            saveTasks()
            isrunning = False