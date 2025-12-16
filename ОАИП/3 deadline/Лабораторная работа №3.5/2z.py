import time
big_list = list(range(100000))
print("Измеряем время удаления из начала списка (pop(0))...")
start_time = time.time()
for i in range(1000):
    if big_list:
        big_list.pop(0)
end_time = time.time()
time_pop_0 = end_time - start_time
print(f"Время выполнения pop(0): {time_pop_0:.4f} секунд\n")
print("Измеряем время удаления с конца списка (pop())...")
big_list = list(range(100000))
start_time = time.time()
for i in range(1000):
    if big_list:
        big_list.pop()
end_time = time.time()
time_pop_end = end_time - start_time
print(f"Время выполнения pop(): {time_pop_end:.4f} секунд\n")
print("=" * 50)
print("РЕЗУЛЬТАТЫ:")
print(f"pop(0): {time_pop_0:.4f} секунд")
print(f"pop() : {time_pop_end:.4f} секунд")
if time_pop_0 > time_pop_end:
    print("\npop() работает БЫСТРЕЕ, чем pop(0)")
    print(f"Разница в {time_pop_0 / time_pop_end:.1f} раз")
else:
    print("\npop(0) работает БЫСТРЕЕ, чем pop()")
print("\n" + "=" * 50)
print("ПОЧЕМУ ТАК ПРОИСХОДИТ:")
print("1. pop() - удаление с конца: O(1)")
print("   Это быстрая операция, так как не нужно двигать другие элементы")
print("2. pop(0) - удаление из начала: O(n)")
print("   Это медленная операция, так как после удаления первого элемента")
print("   нужно сдвинуть ВСЕ остальные элементы на одну позицию влево")
print("   Чем больше список, тем дольше это занимает времени")
