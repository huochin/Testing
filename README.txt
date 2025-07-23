To-Do List CLI Application
==========================

A simple command-line to-do list manager written in Python. This application allows you to add, view, mark as done, and delete tasks, with persistent storage using a JSON file.

Features
--------
- Add new tasks
- View all tasks with status (Done/Not Done)
- Mark tasks as done
- Delete tasks
- Tasks are saved to and loaded from `tasks.json`

How to Run
----------
1. Make sure you have Python 3 installed.
2. Open a terminal or command prompt in this directory.
3. Run the application:
   
   ```
   python todoListCLI.py
   ```

Usage
-----
- Follow the on-screen menu to add, view, mark as done, or delete tasks.
- Tasks are automatically saved when you quit the program.

File Descriptions
-----------------
- `todoListCLI.py` : Main Python script for the CLI application.
- `tasks.json`     : Stores your tasks and their status (created automatically).
- `README.txt`     : This file.

Notes
-----
- If `tasks.json` does not exist, it will be created automatically.
- Only integer choices between 1 and 5 are accepted in the menu.

Enjoy managing your tasks!
