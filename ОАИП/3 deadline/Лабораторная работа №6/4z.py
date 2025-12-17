import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Время выполнения: {elapsed_time:.2f} сек")
        return False
print("Пример 1 - нормальное выполнение:")
with Timer():
    time.sleep(1.5)
    print("  Код внутри блока выполнен")
print("\nПример 2 - быстрое выполнение:")
with Timer():
    for i in range(1000):
        pass
    print("  Цикл выполнен")
print("\nПример 3 - с ошибкой внутри:")
try:
    with Timer():
        time.sleep(0.5)
        result = 1 / 0
except ZeroDivisionError:
    print("  Ошибка была поймана после таймера")
