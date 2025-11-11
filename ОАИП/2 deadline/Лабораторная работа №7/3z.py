def calc_avg(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
def fmt_fio(parts, capitalize=True):
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio
def filter_scores(data_dict, min_value):
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
    return result
print("=== Функция 1: calc_avg ===")
print("Вычисляет среднее арифметическое списка чисел")
numbers_list = [10, 20, 30, 40]
average = calc_avg(numbers_list)
print(f"calc_avg({numbers_list}) = {average}")
empty_list = []
average_empty = calc_avg(empty_list)
print(f"calc_avg({empty_list}) = {average_empty}")
print()
print("=== Функция 2: fmt_fio ===")
print("Форматирует ФИО из списка частей имени")
fio1 = fmt_fio(['иванов', "иван", "сергеевич"])
print(f"fmt_fio(['иванов', 'иван', 'сергеевич']) = '{fio1}'")
fio2 = fmt_fio(['сидорова', "анна", "валерьевна"], capitalize=False)
print(f"fmt_fio(['сидорова', 'анна', 'валерьевна'], capitalize=False) = '{fio2}'")
print()
print("=== Функция 3: filter_scores ===")
print("Фильтрует словарь по минимальному значению")
scores = {"math": 95, "history": 78, "english": 88, "art": 92}
filtered = filter_scores(scores, 90)
print(f"filter_scores({scores}, 90) = {filtered}")
