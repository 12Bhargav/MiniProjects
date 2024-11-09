def main():
    tasks = []
    completed_tasks = []

    while True:
        print("\nTODO LIST")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Display Live Tasks")
        print("4. Display Completed Tasks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_title = input("Enter task title: ")
            status = "Incomplete"
            tasks.append({"title": task_title, "status": status})
            print("Task added successfully!")

        elif choice == 2:
            if not tasks:
                print("No tasks to update.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task['title']}")
                task_index = int(input("Enter task number to update: ")) - 1
                if task_index >= 0 and task_index < len(tasks):
                    new_status = input("Enter new status (Completed/Incomplete): ")
                    tasks[task_index]['status'] = new_status
                    if new_status.lower() == "completed":
                        completed_tasks.append(tasks.pop(task_index))
                        print("Task marked as completed and moved to completed tasks.")
                    else:
                        print("Task updated successfully!")
                else:
                    print("Invalid task number.")

        elif choice == 3:
            if not tasks:
                print("No live tasks.")
            else:
                print("Live Tasks:")
                for task in tasks:
                    print(f"- {task['title']} ({task['status']})")

        elif choice == 4:
            if not completed_tasks:
                print("No completed tasks.")
            else:
                print("Completed Tasks:")
                for task in completed_tasks:
                    print(f"- {task['title']}")

        elif choice == 5:
            print("Exiting")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()