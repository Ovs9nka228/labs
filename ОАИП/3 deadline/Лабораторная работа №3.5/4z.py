import time
import random
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None
def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        needed = target - num
        if needed in seen:
            return (needed, num)
        seen.add(num)
    return None
print("Генерируем список из 10000 случайных чисел...")
numbers = [random.randint(1, 10000) for _ in range(10000)]
index1 = random.randint(0, 9999)
index2 = random.randint(0, 9999)
while index2 == index1:
    index2 = random.randint(0, 9999)
target = numbers[index1] + numbers[index2]
print(f"Ищем пару чисел, сумма которых равна {target}")
print(f"(Известно, что числа {numbers[index1]} и {numbers[index2]} в сумме дают {target})\n")
print("=" * 50)
print("Тестируем МЕДЛЕННУЮ функцию (O(n²))...")
print("Это может занять некоторое время...")
start_time = time.time()
result_slow = find_pair_slow(numbers, target)
end_time = time.time()
time_slow = end_time - start_time
print(f"Найдена пара: {result_slow}")
print(f"Проверка: {result_slow[0]} + {result_slow[1]} = {result_slow[0] + result_slow[1]}")
print(f"Время выполнения: {time_slow:.4f} секунд\n")
print("=" * 50)
print("Тестируем БЫСТРУЮ функцию (O(n))...")
start_time = time.time()
result_fast = find_pair_fast(numbers, target)
end_time = time.time()
time_fast = end_time - start_time
print(f"Найдена пара: {result_fast}")
print(f"Проверка: {result_fast[0]} + {result_fast[1]} = {result_fast[0] + result_fast[1]}")
print(f"Время выполнения: {time_fast:.4f} секунд\n")
print("=" * 50)
print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
print(f"Медленная функция: {time_slow:.4f} секунд")
print(f"Быстрая функция:   {time_fast:.4f} секунд")
if time_slow > 0 and time_fast > 0:
    times_faster = time_slow / time_fast
    print(f"\nБыстрая функция работает в {times_faster:.0f} раз быстрее!")
else:
    print("\nОдна из функций выполнилась слишком быстро для измерения")
print("\n" + "=" * 50)
print("ПРОВЕРКА ПРАВИЛЬНОСТИ:")
if result_slow and result_fast:
    sum_slow = result_slow[0] + result_slow[1]
    sum_fast = result_fast[0] + result_fast[1]
    print(f"Медленная функция: {result_slow[0]} + {result_slow[1]} = {sum_slow}")
    print(f"Быстрая функция:   {result_fast[0]} + {result_fast[1]} = {sum_fast}")
    if sum_slow == target and sum_fast == target:
        print("✓ Обе функции нашли правильную пару!")
    else:
        print("✗ Что-то пошло не так...")
else:
    print("Одна из функций не нашла пару")
print("\n" + "=" * 50)
print("КАК РАБОТАЕТ БЫСТРАЯ ФУНКЦИЯ:")
print("1. Создаем пустое множество 'seen'")
print("2. Для каждого числа в массиве:")
print("   - Вычисляем, какое число нам нужно: needed = target - num")
print("   - Проверяем, есть ли 'needed' уже в множестве 'seen'")
print("   - Если есть, значит мы нашли пару!")
print("   - Если нет, добавляем текущее число в 'seen'")
print("\nПример: target = 10, числа: [3, 7, 2, 8]")
print("1. Берем 3: needed = 7 (10-3), 7 нет в seen → добавляем 3")
print("2. Берем 7: needed = 3 (10-7), 3 ЕСТЬ в seen → нашли пару (3, 7)!")
print("\nПреимущество: мы проходим по массиву всего ОДИН раз!")
