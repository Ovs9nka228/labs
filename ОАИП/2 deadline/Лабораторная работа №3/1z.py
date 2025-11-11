fruits = {
    "яблок": 5,
    "бананов": 3,
    "апельсинов": 10,
    "арбузов":33
}
print("Начальное количество фруктов:")
for fruit, count in fruits.items():
    print(f"за прилавком есть {count} {fruit}")
print()
print("Продали 2 яблока")
fruits["яблок"] = fruits["яблок"] - 2
print("Ашот Похититель Арбузов украл все арбузы!")
fruits["арбузов"] = 0
print()
print("Итоговое количество фруктов:")
for fruit, count in fruits.items():
    print(f"за прилавком осталось {count} {fruit}")
