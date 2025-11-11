phone_book = {
    "Мама": "8-900-123-45-67",
    "Папа": "8-900-987-65-43",
    "Сестра": "8-901-555-44-33",
    "Друг": "8-902-111-22-33"
}
while True:
    print("Телефоная книга:")
    print("Выберите действие:")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    choice = input("Введите номер действия (1-4): ")
    if choice == "1":
        print("Все контакты")
        if len(phone_book) == 0:
            print("Телефонная книга пуста")
        else:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
    elif choice == "2":
        name = input("Введите имя контакта:")
        phone = input("Введите номер телефона:")
        if name in phone_book:
            print(f"Контакт с именем '{name}' уже существует")
        else:
            phone_book[name] = phone
            print(f"Контакт '{name}' успешно добавлен!")
    elif choice == "3":
        name = input("Введите имя контакта для удаления")
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт с именем '{name}' успешно удален")
        else:
            print(f"Контакт с именем '{name}' не найден!")
    elif choice == "4":
        print("До свидания!")
        exit()
    else:
        print("Неверный выбор! Введите число от 1 до 4")
