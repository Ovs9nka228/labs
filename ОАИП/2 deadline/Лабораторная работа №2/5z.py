a = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(a):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)
max_number = max(numbers)
min_number = min(numbers)
average = sum(numbers)/a
count_above_average = 0
for num in numbers:
    if num > average:
        count_above_average += 1
print(f"Результаты:")
print(f"Максимальное: {max_number}")
print(f"Минимальное: {min_number}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count_above_average}")
