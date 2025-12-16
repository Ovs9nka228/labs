import sys
def create_list(n):
    result = []
    for i in range(n + 1):
        square = i ** 2
        result.append(square)
    return result
def create_gen(n):
    for i in range(n + 1):
        square = i ** 2 
        yield square
def create_gen_simple(n):
    return (i ** 2 for i in range(n + 1))
print("Создаем квадраты чисел от 0 до N")
N = 1000000
print(f"N = {N}\n")
print("Создаем список квадратов...")
start_time = time.time()
my_list = create_list(N)
end_time = time.time()
print(f"Список создан за {end_time - start_time:.2f} секунд")
print(f"Первые 5 элементов списка: {my_list[:5]}")
print("\nСоздаем генератор квадратов...")
start_time = time.time()
my_gen = create_gen(N)
end_time = time.time()
print(f"Генератор создан за {end_time - start_time:.2f} секунд")
print("Извлекаем первые 5 элементов из генератора:")
first_five = []
for i, value in enumerate(my_gen):
    first_five.append(value)
    if i >= 4:
        break
print(f"Первые 5 элементов: {first_five}")
print("\n" + "=" * 50)
print("СРАВНЕНИЕ РАЗМЕРОВ В ПАМЯТИ:")
my_list = create_list(N)
my_gen = create_gen(N)
size_list = sys.getsizeof(my_list)
size_gen = sys.getsizeof(my_gen)
print(f"Размер списка: {size_list:,} байт")
print(f"Размер генератора: {size_gen:,} байт")
if size_list > size_gen:
    times_bigger = size_list / size_gen
    print(f"\nСписок занимает в {times_bigger:.0f} раз больше памяти!")
else:
    print(f"\nГенератор занимает меньше памяти")
print("\n" + "=" * 50)
print("ДЕМОНСТРАЦИЯ РАБОТЫ ГЕНЕРАТОРА:")
small_gen = create_gen(5)
print("Генератор для чисел от 0 до 5:")
print("1. Берем первый элемент:", next(small_gen))
print("2. Берем второй элемент:", next(small_gen))
print("3. Берем третий элемент:", next(small_gen))
print("Оставшиеся элементы:")
for num in small_gen:
    print(f"  {num}")
print("\n" + "=" * 50)
print("СЛОЖНОСТЬ ПО ПАМЯТИ (Space Complexity):")
print("\n1. СПИСОК: O(n)")
print("   Почему: Список хранит ВСЕ элементы сразу в памяти.")
print(f"   Для N={N} хранится {N+1} чисел.")
print("   Чем больше N, тем больше нужно памяти.")
print("\n2. ГЕНЕРАТОР: O(1)")
print("   Почему: Генератор хранит только текущий элемент и состояние.")
print("   Элементы вычисляются 'на лету' по мере необходимости.")
print("   Память не зависит от N, всегда занимает примерно одинаково.")
print("\n" + "=" * 50)
print("ВЫВОД:")
print("Для больших данных используйте генераторы,")
print("если не нужно хранить все элементы сразу в памяти!")
