import time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def tail_fibonacci(n, a=0, b=1):
    """
    a и b - это "накопители" (аккумуляторы):
    a = F(n-2), b = F(n-1), где F - число Фибоначчи
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)
n = 35
print("=== Сравнение производительности ===")
print(f"Вычисляем Fibonacci({n})")
print()
start_time = time.time()
result1 = fibonacci(n)
time1 = time.time() - start_time
print(f"Fibonacci({n}) = {result1}")
print(f"Время выполнения (обычная рекурсия): {time1:.6f} секунд")
print()
start_time = time.time()
result2 = tail_fibonacci(n)
time2 = time.time() - start_time
print(f"Tail Fibonacci({n}) = {result2}")
print(f"Время выполнения (хвостовая рекурсия): {time2:.6f} секунд")
print()
if result1 == result2:
    print("✓ Обе функции дали одинаковый результат")
else:
    print("✗ Результаты различаются!")
print(f"\nХвостовая рекурсия быстрее в {time1/time2:.0f} раз!")
