class SmartList(list):
    def __getitem__(self, index):
        if index < 0:
            positive_index = abs(index) - 1
            return super().__getitem__(positive_index)
        else:
            return super().__getitem__(index)
s1 = SmartList([10, 20, 30])
print("Тестирование SmartList:")
print(f"s1 = {s1}")
print(f"s1[0] = {s1[0]}")
print(f"s1[-1] = {s1[-1]}")
print(f"s1[-2] = {s1[-2]}")
print(f"s1[-3] = {s1[-3]}")
print(f"s1[1] = {s1[1]}")
print(f"s1[2] = {s1[2]}")
s1.append(40)
print(f"\nПосле добавления 40: {s1}")
print(f"s1[-1] = {s1[-1]}")
print(f"s1[-4] = {s1[-4]}")
print("\nСравнение с обычным списком:")
normal_list = [10, 20, 30]
print(f"normal_list[-1] = {normal_list[-1]}")
print(f"s1[-1] = {s1[-1]}")
