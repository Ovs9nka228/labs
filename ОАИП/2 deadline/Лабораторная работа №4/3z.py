tasks = []
while True:
    print("--- Меню ---")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    choice = input("Выберите действие (1-4): ")
    if choice == "1":
        print("--- Ваши задачи ---")
        if len(tasks) == 0:
            print("Задач пока нет!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice == "2":
        new_task = input("Введите описание задачи: ")
        tasks.append(new_task)
        print(f'Задача "{new_task}" добавлена!')
    elif choice == "3":
        print("--- Ваши задачи ---")
        if len(tasks) == 0:
            print("Задач пока нет!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_number = input("Какую задачу выполнили? Введите номер: ")
            if task_number.isdigit():
                task_number = int(task_number)
                if task_number >= 1 and task_number <= len(tasks):
                    removed_task = tasks[task_number - 1]
                    del tasks[task_number - 1]
                    print(f'Задача "{removed_task}" удалена!')
                else:
                    print("Неправильный номер задачи!")
            else:
                print("Пожалуйста, введите число!")
    elif choice == "4":
        print("До свидания!")
        break
    else:
        print("Неправильный выбор! Введите число от 1 до 4")
