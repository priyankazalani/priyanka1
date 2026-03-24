"""
📋 To-Do List Manager
A command-line task manager with add, complete, delete, and save features.
Author: Priyanka
"""

import json
import os
from datetime import datetime

DATA_FILE = "todo_data.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet! Add one to get started.")
        return
    
    print(f"\n{'─' * 50}")
    print(f" {'#':<4} {'Status':<8} {'Task':<25} {'Date'}")
    print(f"{'─' * 50}")
    
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "⬜"
        name = task['name'][:24]
        date = task.get('date', 'N/A')
        print(f" {i:<4} {status:<8} {name:<25} {date}")
    
    print(f"{'─' * 50}")
    done_count = sum(1 for t in tasks if t['done'])
    print(f" 📊 {done_count}/{len(tasks)} completed")

def add_task(tasks):
    name = input("\n📌 Enter task: ").strip()
    if not name:
        print("❌ Task cannot be empty!")
        return
    
    task = {
        'name': name,
        'done': False,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: '{name}'")

def complete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("\n✔️ Task number to complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            save_tasks(tasks)
            print(f"🎉 '{tasks[num-1]['name']}' marked as done!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a number!")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("\n🗑️ Task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: '{removed['name']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a number!")

def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t['done']]
    removed = before - len(tasks)
    save_tasks(tasks)
    print(f"🧹 Cleared {removed} completed tasks!")

def todo_manager():
    print("=" * 40)
    print("   📋 TO-DO LIST MANAGER")
    print("=" * 40)
    
    tasks = load_tasks()
    
    while True:
        print("\n📂 Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Clear completed")
        print("6. Exit")
        
        choice = input("\n👉 Choose (1-6): ").strip()
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            clear_completed(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("\n👋 Tasks saved! Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    todo_manager()
