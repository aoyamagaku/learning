import psycopg


with psycopg.connect("dbname=todo user=danil", autocommit=True) as conn:
    with conn.cursor() as cur:
        while True:
            try:
                action = int(input("What do you want to do? \n 1. Add task \n 2. Show tasks"
                                   " \n 3. Delete task \n 4. Complete task \n 5. Exit \n Choose an option: "))
            except ValueError:
                print("Please enter a number")
                continue

            if action == 1:
                task = input("Please enter your task: ")
                if not task.strip():
                    print("Please enter a valid task")
                else:
                    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (task,))
                    print("Your task has been added")
            elif action == 2:
                cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
                tasks = cur.fetchall()
                if len(tasks) == 0:
                    print("No tasks added")
                else:
                    print("Tasks: ")
                    for number, task in enumerate(tasks, start=1):
                        if task[2]:
                            mark = "[x]"
                        else:
                            mark = "[ ]"
                        print(f"{number}. {mark} {task[1]}")
            elif action == 3:
                cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
                tasks = cur.fetchall()
                if len(tasks) == 0:
                    print("No tasks to delete!")
                else:
                    print("Choose task for delete: ")
                    for number, task in enumerate(tasks, start=1):
                        if task[2]:
                            mark = "[x]"
                        else:
                            mark = "[ ]"
                        print(f"{number}. {mark} {task[1]}")
                    try:
                        number = int(input())
                    except ValueError:
                        print("Invalid number")
                        continue
                    if 1 <= number <= len(tasks):
                        index = number - 1
                        task_id = tasks[index][0]
                        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                        print("Your task has been deleted")
                    else:
                        print("Invalid number")

            elif action == 4:
                cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
                tasks = cur.fetchall()
                if len(tasks) == 0:
                    print("No tasks to complete")
                else:
                    print("Choose task to complete: ")
                    for number, task in enumerate(tasks, start=1):
                        if task[2]:
                            mark = "[x]"
                        else:
                            mark = "[ ]"
                        print(f"{number}. {mark} {task[1]}")
                    try:
                        number = int(input())
                    except ValueError:
                        print("Invalid number")
                        continue
                    if 1 <= number <= len(tasks):
                        index = number - 1
                        task_id = tasks[index][0]
                        cur.execute("UPDATE tasks SET done = true WHERE id = %s", (task_id,))
                        print("Your task has been completed")
                    else:
                        print("Invalid number")
            elif action == 5:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid option")