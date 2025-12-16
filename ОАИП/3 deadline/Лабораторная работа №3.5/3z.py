import time
import random
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    if arr[i] not in duplicates:
                        duplicates.append(arr[i])
                    break
    return duplicates
print("Тест 1: Список из 5000 элементов")
print("Генерируем случайные числа...")
list_5000 = [random.randint(1, 10000) for _ in range(5000)]
print("Ищем дубликаты (это может занять некоторое время)...")
start_time = time.time()
duplicates_5000 = find_duplicates(list_5000)
end_time = time.time()
time_5000 = end_time - start_time
print(f"Найдено дубликатов: {len(duplicates_5000)}")
print(f"Время выполнения: {time_5000:.2f} секунд\n")
print("Тест 2: Список из 10000 элементов")
print("Генерируем случайные числа...")
list_10000 = [random.randint(1, 10000) for _ in range(10000)]
print("Ищем дубликаты (это займет больше времени)...")
start_time = time.time()
duplicates_10000 = find_duplicates(list_10000)
end_time = time.time()
time_10000 = end_time - start_time
print(f"Найдено дубликатов: {len(duplicates_10000)}")
print(f"Время выполнения: {time_10000:.2f} секунд\n")
print("=" * 50)
print("РЕЗУЛЬТАТЫ:")
print(f"5000 элементов: {time_5000:.2f} секунд")
print(f"10000 элементов: {time_10000:.2f} секунд")
if time_5000 > 0:
    times_slower = time_10000 / time_5000
    print(f"\nВремя увеличилось в {times_slower:.1f} раза")
    print("\nВОПРОС: Если данные выросли в 2 раза,")
    print("во сколько раз (примерно) выросло время выполнения?")
    print("\nОТВЕТ: Время выросло примерно в", end=" ")
    if 3.5 <= times_slower <= 4.5:
        print(f"{times_slower:.1f} раза (близко к 4 разам)")
        print("Это потому что у нас O(n²) сложность!")
    else:
        print(f"{times_slower:.1f} раза")
        print("Ожидалось около 4 раз для O(n²) сложности")
else:
    print("Первое измерение заняло 0 секунд, сравнить невозможно")
print("\n" + "=" * 50)
print("ПОЧЕМУ ТАК ПРОИСХОДИТ:")
print("У нас два вложенных цикла:")
print("- Внешний цикл проходит по всем n элементам")
print("- Внутренний цикл тоже проходит по всем n элементам")
print("Всего операций: n * n = n²")
print("\nЕсли n = 5000, то операций: 5000 * 5000 = 25 000 000")
print("Если n = 10000, то операций: 10000 * 10000 = 100 000 000")
print("В 4 раза больше операций при увеличении данных в 2 раза!")
