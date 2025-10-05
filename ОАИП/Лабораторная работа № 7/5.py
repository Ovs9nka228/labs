print("Привет! Я калькулятор")
print("Введи пример: число знак число")
user_input = input("Введи пример: ")
parts = user_input.split()

if len(parts) != 3:
    print("Ошибка! Надо ввести: число знак число")
    print("Пример: 5 + 3")
else:
    num1_str = parts[0]
    znak = parts[1]
    num2_str = parts[2]
    oshibka = False
    if num1_str.replace('.', '', 1).isdigit():
        num1 = float(num1_str)
    else:
        print("Первое число неправильное!")
        oshibka = True
    if num2_str.replace('.', '', 1).isdigit():
        num2 = float(num2_str)
    else:
        print("Второе число неправильное!")
        oshibka = True
    if not oshibka:
        if znak == "+":
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif znak == "-":
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif znak == "*":
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif znak == "/":
            if num2 == 0:
                print("Ошибка! На ноль делить нельзя!")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Не знаю такой знак! Используй + - * /")
