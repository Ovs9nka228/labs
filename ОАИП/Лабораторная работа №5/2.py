numbers = input("Введите три числа через пробел:")
numbers_list = numbers.split()

num1 = int(numbers_list[0])
num2 = int(numbers_list[1])
num3 = int(numbers_list[2])

um1 = num1 * num2
um2 = num2 * num3
um3 = num3 * num1

a = num1 ** 4
b = num2 % num3
c = num3 // num1
print("Результаты умножения:")
print("Первое число умножить на второе:", um1)
print("Второе число умножить на третье:", um2)
print("Третье число умножить на первое:", um3)
print("Результаты других операций:")
print("Первое число в 4 степени:", a)
print("Остаток от деления второго на третье:", b)
print("Целочисленное деление третьего на первое:", c)
sum_result = a + b + c
print("Сумма результатов из пункта 5:", sum_result)
