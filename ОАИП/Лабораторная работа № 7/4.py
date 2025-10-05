year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} год является високосным")
        else:
            print(f"{year} год не является високосным")
    else:
        print(f"{year} год является високосным")
else:
    print(f"{year} год не является високосным")
