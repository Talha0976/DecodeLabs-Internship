def display_menu():
    print("\n My TO-DO LIST ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append(task)
    print(f'"{task}" added successfully!')

def view_tasks(task_list):
    if not task_list:
        print("No tasks yet. Add one!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def main():
    my_tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()