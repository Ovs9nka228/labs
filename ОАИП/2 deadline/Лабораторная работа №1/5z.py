text = input("Введите строка: ")
glas = "аеёиоуыэюяaeiou"
glas += glas.upper()
result = ""
i = 0
while i < len(text):
    char = text[i]
    if char not in glas:
        result += char
    i += 1
print(f"Результат: {result}")
